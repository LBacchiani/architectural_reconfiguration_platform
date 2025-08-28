# Architectural Reconfiguration Platform

The following instructions explain how to use/deploy the specification and implementation level architectural reconfiguration platform.

## Specification Level

The specification level simulation is distributed as a docker container.
To start the corresponding container run:

`docker run -it lorenzobacchiani/architectural_reconfiguration_platform /bin/bash`

Once inside the container, you will find a convenient script to compile ABS models.

### Teastore 

To execute the Teastore simulation adapted with the reactive global scaling approach run: 

`./compile global_scaling teastore erlang`

To execute the Teastore simulation adapted with the reactive local scaling approach run: 

`./compile local_scaling teastore erlang`

Once the compilation phase successfully end, you should see a `gen` folder containing the executable simulation. To execute it, you must run 

`gen/erl/run`

### Email Pipeline System
To execute the Email Pipeline System simulation adapted with the reactive global scaling approach, you must first check that the `proactiveness()` flag in `global_scaling/email_system/email_sys_param.abs`
is set to `false`. If not, run 

`nano global_scaling/email_system/email_sys_param.abs`

and change it accordingly. Once you have ensured that, to compile the ABS model run

`./compile global_scaling email_system erlang`

To execute the Email Pipeline System simulation adapted with the reactive local scaling approach run: 

`./compile local_scaling email_system erlang`

To execute the Email Pipeline System simulation adapted with the proactive local scaling approach, you must first check that the `proactiveness()` flag in `global_scaling/email_system/email_sys_param.abs` is set to `true`. If not, run:

`nano global_scaling/email_system/email_sys_param.abs`

and change it accordingly. Once you have ensured that, to compile the ABS model run: 

`./compile global_scaling email_system erlang`

To execute the Email Pipeline System simulation adapted with the proactive local scaling approach, you must first check that the `proactiveness()` and `mixing()` flags in `global_scaling/email_system/email_sys_param.abs` are set to `true`. If not, run:

`nano global_scaling/email_system/email_sys_param.abs`

and change them accordingly. Once you have ensured that, to compile the ABS model run: 

`./compile global_scaling email_system erlang`

Once the compilation phase successfully end, you should see a `gen` folder containing the executable simulation. To execute it, you must run: 

`gen/erl/run`

###  Industrial low latency anomaly detection architecture

To execute the Industrial low latency anomaly detection architecture simulation adapted with the reactive global scaling approach run: 

`./compile migration birex erlang`


## Implementation Level
Implementation level simulations are designed to be executed inside a Kubernetes cluster. We provide the necessary Kubernetes manifests in order to facilitate the deployment of the various systems.

### Teastore and Email pipeline systems.

The Kubernetes manifests for the Teastore and Email Pipeline systems are located in the `implementation_level/k8s` directory along with a deployment script, `deploy.sh`. Please refer to the instruction provided inside the [directory](implementation_level/k8s/README.md) for deployment details.

### Industrial low latency anomaly detection architecture
The folder `implementation_level/birex_orchestrator` contains both the implementation and the Kubernetes manifests for the Industrial low latency anomaly detection architecture. In order to deploy the system navigate to `implementation_level/birex_orchestrator/multiple_orchestration`.

You'll find a file called `run_launcher.sh` that will launch the necessary Kubernetes resources and also starts the simulation, also producing a log file with the results.

Please, give the `run_launcher.sh` file execution permissions by running on a terminal:

```bash
chmod +x run_launcher.sh
```

Also ensure that the configuration for the Kubernetes cluster is properly set up and that you have the necessary permissions to deploy resources.

## Data Analysis 

We implemented our data analysis using a Jupyter notebook. To run it, you must first ensure that `Python 3.xx` is installed. Then, to install requierd dependencies run: 

`pip install -r requirements.txt` 

Then, to start a Jupyter notebook local server, run:

`jupyter notebook` 

and open `main.ipynb`


