# Common Global Scaler
This directory contains the implementation of the global scaler used for both the tea store and mail pipeline use case systems.
This is a shared component that provides the necessary functionality to scale the applications based on the workload and resource availability.

The global scaler is deployed inside a Kubernetes cluster as a separate microservice and can be configured with all the necessary parameters to adapt to different use cases.

## Building the global scaler for a target system.

### Base Docker Image
Since it's containerized is possible to build the global scaler as a Docker image specifically tailored for the target system.
`Dockerfile` located in the `common_global_scaler` is used as base image that could be extended with additional layers to include any system-specific dependencies or configurations.

Once you've setup the `Dockerfile`, you can build the Docker image using the following command:

```bash
docker build -t global-scaler:<tag> .
```

Replace `<tag>` with a meaningful tag for your image. After building the image, you can push it to a container registry or deploy it directly to your Kubernetes cluster.

### Extend the global scaler
Once the base image is ready it can be used for creating variations of the global scaler for different use cases. This can be achieved by creating new Dockerfiles that extend the base image and include the increments manifests.

```bash
FROM your-repo/global-scaler:<tag>

COPY ./manifests/ ./target-folder/

ENV FOLDER_PATH=/app/target-folder
````



