# Architectural Reconfiguration Platform
Repository for Architectural Reconfiguration Platform paper

## Structure
- `common_global_scaler/`: Contains the source code of the global scaler.
- `k8s_smart_deployer/`: Contains the source code for the Kubernetes orchestration synthetizer tool.
- `k8s/`: Contains the Kubernetes manifests
  - `global-scaler/`: Manifests for the global scaler.
  - `tea-store/`: Manifests for the tea store use case system.
  - `mail-pipeline/`: Manifests for the mail pipeline use case system.
- `k6-test/`: Contains the k6 load tests for both systems.
  - `mail/`: Contains the k6 load tests for the mail pipeline use case system.
  - `tea-store/`: Contains the k6 load tests for the tea store use case system.
- `annotations/`: Contains the Kubernetes annotations used by the k8s_smart_deployer tool for generating the orchestrations.

