import os
import time
import threading
from components.sys_scaler import SysScaler
from components.mixer import Mixer
from components.guard_logger import GuardLogger
from prometheus_api_client import PrometheusConnect
import numpy as np
import requests


class Guard:
    def __init__(
            self,
            scaler: SysScaler,
            mixer: Mixer,
            predictions,
            k_big=20,
            k=10,
            sleep=10,
    ):
        self.guard_thread = None
        self.log_thread = None
        self.k_big = k_big
        self.k = k
        self.sleep = sleep
        self.running = True

        self.request_scaling = False
        self.scaler = scaler
        self.mixer = mixer

        prometheus_service_address = os.environ.get("PROMETHEUS_SERVICE_ADDRESS", "localhost")
        prometheus_service_port = os.environ.get("PROMETHEUS_SERVICE_PORT", "64671")

        self.monitor_only = os.environ.get("MONITOR_ONLY", "false").lower() == 'true'
        prometheus_url = f"http://{prometheus_service_address}:{prometheus_service_port}"
        self.prometheus_instance = PrometheusConnect(url=prometheus_url)

        self.proactiveness = os.environ.get("PROACTIVE", "false").lower() == 'true'
        self.proactive_reactive = self.proactiveness and os.environ.get("PROACTIVE_REACTIVE", "false").lower() == 'true' 
        self.predictions = predictions
        
        # Metrics names from environment variables
        self.http_requests_metric = os.environ.get("HTTP_REQUESTS_METRIC", "http_requests_total_webUI_counter")
        self.behaviour_execution_metric = os.environ.get("BEHAVIOUR_EXECUTION_METRIC", "behaviour_execution")
        self.behaviour_time_metric = os.environ.get("BEHAVIOUR_TIME_METRIC", "behaviour_time_execution")
        self.message_lost_metric = os.environ.get("MESSAGE_LOST_METRIC", "message_lost_webUI")

        self.logger = GuardLogger.from_env()

    def start(self) -> None:
        self.guard_thread = threading.Thread(target=self.guard)
        self.guard_thread.start()

    def should_scale(self, inbound_workload, current_mcl) -> bool:
        return inbound_workload - (current_mcl - self.k_big) > self.k or \
               (current_mcl - self.k_big) - inbound_workload > self.k
    
    def _execute_prometheus_query(self, query: str):
        try:
            data = self.prometheus_instance.custom_query(query)
            return float(data[0]['value'][1])
        except (requests.exceptions.RequestException, KeyError, IndexError):
            return None

    def guard(self) -> None:
        print("Monitoring the system...")
        iter = 0
        last_pred_conf = []
        current_mcl = self.scaler.get_mcl()
        pred_workload = 0
        config = self.scaler.get_current_config()

        if self.proactiveness:
            pred_workload = sum(self.predictions[iter-self.sleep:])/self.sleep
            last_pred_conf = self.scaler.calculate_configuration(pred_workload + self.k_big)
            current_mcl, _ = self.scaler.process_request(last_pred_conf)
        
        sleep_time = 1
        while self.running:
            tot = self._execute_prometheus_query(
                f"sum(increase({self.http_requests_metric}[{self.sleep}s]))"
            )
            completed = self._execute_prometheus_query(
                f"sum(increase({self.behaviour_execution_metric}[{self.sleep}s]))"
            )
            latency = self._execute_prometheus_query(
                f"sum(increase({self.behaviour_time_metric}[{self.sleep}s]))"
            )
            avg_lat = (latency if latency is not None else 0.0) / (completed if (completed is not None and completed > 0) else 1)
            loss = self._execute_prometheus_query(
                f"sum(increase({self.message_lost_metric}[{self.sleep}s]))"
            )

            if tot is not None and (tot > 0 or iter > 0): 
                sleep_time = self.sleep
                measured_workload = (tot if tot is not None else 0.0) / self.sleep
                target_workload = measured_workload
                
                if iter > 0 and self.proactiveness:
                    diff = iter - self.sleep
                    pred_workload = sum(self.predictions[diff if diff > 0 else 0:iter]) / self.sleep
                    target_workload = pred_workload
                
                config = np.sum(self.scaler.get_current_config()) if not self.monitor_only else self._execute_prometheus_query("sum(total_instances_number)")
                
                mixed_workload = None
                if iter > 0 and self.proactive_reactive:
                    measured_conf = self.scaler.calculate_configuration(measured_workload + self.k_big)
                    mixed_workload = self.mixer.mix(measured_workload, pred_workload, last_pred_conf, measured_conf)
                    target_workload = mixed_workload
                    last_pred_conf = self.scaler.calculate_configuration(pred_workload + self.k_big)
                
                self.logger.log_metrics(
                    iter_num=iter,
                    avg_lat=avg_lat,
                    measured_workload=measured_workload,
                    current_mcl=current_mcl,
                    config=config,
                    total_requests=measured_workload * self.sleep,
                    completed=completed if completed is not None else 0,
                    loss=loss if loss is not None else 0,
                    pred_workload=pred_workload if self.proactiveness and iter > 0 else None,
                    mixed_workload=mixed_workload
                )

                if self.should_scale(target_workload, current_mcl) and not self.monitor_only:
                    target_conf = self.scaler.calculate_configuration(target_workload + self.k_big)
                    current_mcl, _ = self.scaler.process_request(target_conf)    

                iter += self.sleep
        
            else: 
                self.logger.log_metrics(
                    iter_num=iter,
                    avg_lat=avg_lat,
                    measured_workload=0.0,
                    current_mcl=current_mcl,
                    config=0,
                    total_requests=0,
                    completed=0,
                    loss=0
                )
                iter = 0 

            time.sleep(sleep_time)
