import subprocess
import tempfile
from pathlib import Path
from enum import Enum
import yaml
import shutil
from typing import Dict, List

Op = Enum("Op", [("DEPLOY", "deploy"), ("DESTROY", "destroy")])

def execute_fully_automatic(file_path: str, stack_name: str, operation: str, project_path: str, replica_multiplier: int):
    mappings = get_service_mappings_auto()
    print("REPLICAS: " + str(replica_multiplier))
    try:
        return execute_pulumi_auto(file_path, stack_name, operation, project_path, mappings, replica_multiplier)         
    except Exception as e:
        print(f"Execution failed: {e}")
        return False

def get_service_mappings_auto() -> Dict[str, List[str]]:
    """Auto-detect service mappings with fallbacks"""
    try:
        # Try in-cluster config first
        from kubernetes import client, config
        config.load_incluster_config()
        print("Using in-cluster Kubernetes config")
    except:
        try:
            from kubernetes import client, config
            config.load_kube_config()
            print("Using local kubeconfig")
        except Exception as e:
            print(f"No Kubernetes config found: {e}")
            return {}
    
    try:
        v1 = client.CoreV1Api()
        services = v1.list_service_for_all_namespaces().items
        
        type_map: Dict[str, List[str]] = {}
        for svc in services:
            name = svc.metadata.name
            labels = svc.metadata.labels or {}
            svc_type = labels.get("type")
            if svc_type:
                type_map.setdefault(svc_type, []).append(name)
        
        print(f"Found {len(type_map)} service type mappings")
        return type_map
    except Exception as e:
        print(f"Could not get service mappings: {e}")
        return {}

def execute_pulumi_auto(file_path: str, stack_name: str, operation: str, project_path: str, mapping: Dict[str, List[str]], replica_multiplier: int) -> bool:
    """Fully automatic Pulumi execution"""
    try:
        project_path = Path(project_path)
        project_path.mkdir(parents=True, exist_ok=True)
        
        # Process resources
        resources_data = yaml.safe_load(Path(file_path).read_text())
        
        # Auto-substitute environments
        for res in resources_data.get("resources", {}).values():
            template_spec = res.get("properties", {}).get("spec", {}).get("template", {}).get("spec", {})
            for container in template_spec.get("containers", []):
                for env in container.get("env", []):
                    if "type" in env:
                        type_key = env.pop("type")
                        if type_key in mapping and mapping[type_key]:
                            env["value"] = "http://" + mapping[type_key][0] + "/request"
                        else:
                            env["value"] = f"missing-{type_key}"
        
        # Auto-scale
        if replica_multiplier > 0:
            for res in resources_data.get("resources", {}).values():
                spec = res.get("properties", {}).get("spec", {})
                if "replicas" in spec:
                    spec["replicas"] = spec["replicas"] * replica_multiplier
            (project_path / "Pulumi.yaml").write_text(yaml.safe_dump(resources_data, default_flow_style=False))
            
            # Auto-login if needed
            login_check = subprocess.run(["pulumi", "whoami"], capture_output=True)
            if login_check.returncode != 0:
                print("Auto-login to Pulumi (local backend)...")
                subprocess.run(["pulumi", "login", "--local"], cwd=project_path, check=True)
            
            # Auto-create/select stack
            subprocess.run([
                "bash", "-c",
                f"pulumi stack select {stack_name} 2>/dev/null || pulumi stack init {stack_name}"
            ], cwd=project_path, check=True)
            
            # Execute command
            command = "up" if operation == Op.DEPLOY.value else "destroy"
            print(f"Running pulumi {command}...")
            
            result = subprocess.run([
                "pulumi", command, "--yes", "--non-interactive", "--skip-preview",
                "--parallel", "20", "--stack", f"{stack_name}"
            ], cwd=project_path, capture_output=True, text=True, timeout=600)
            
            if result.returncode == 0:
                print(f"Pulumi {command} completed successfully")
                return True
            else:
                print(f"Pulumi {command} failed")
                if result.stderr:
                    print(result.stderr)
                return False
        else:
            # ELSE branch: scale all deployments to 0 via kubectl
            print("Scaling all deployments to 0 replicas via kubectl...")
            for res_name in resources_data.get("resources", {}):
                subprocess.run(["kubectl", "scale", "deployment", res_name, "--replicas=0", "--namespace=default"], check=False)
            print("All deployments scaled to 0.")
            return True
            
                
    except Exception as e:
        print(f"Pulumi execution failed: {e}")
        return False