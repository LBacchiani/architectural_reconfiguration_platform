# k8s_smart_deployer


Before running the tool you need to run Zephyrus2 using the following command:

```
sudo docker pull jacopomauro/zephyrus2
sudo docker run -d -p <PORT>:9001 --name zephyrus_container jacopomauro/zephyrus2
```
where ```<PORT>``` is a user-defined port

To run the tool open a terminal in the root folder and execute 
```
python main.py ARG1 ARG2 ARG3 ARG4 ARG5 ARG6
```
where

```
ARG1 is the orchestration name
ARG2 is the folder where microservice specifications are (without final '/')
ARG3 is the yaml file containing the target configuration requirements
ARG4 is the yaml file containing virtual machines requirements
ARG5 is the value of the <PORT> specified after launching the zephyrus2 container
ARG6 is optional. It is a flag '--optimal' and its presence enable optimal placement within existing nodes. If this flag is enabled, Pulumi deployment will be slower.
```
Examples are provided in annotation_examples
