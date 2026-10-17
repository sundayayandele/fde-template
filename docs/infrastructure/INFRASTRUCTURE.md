# Infrastructure

| Environment | Runtime | Image source | Secrets | Telemetry |
| --- | --- | --- | --- | --- |
| Local Python | uvicorn | none | `.env` | `/metrics/` |
| Docker Desktop | Compose; built-in Kubernetes | local build | shell environment / K8s Secret | Compose `observability` profile |
| Podman Desktop | `podman kube play`; kind | `localhost/` image | Podman secret / K8s Secret | same |
| Rancher Desktop | Compose on dockerd; k3s | local build (shared store) | shell environment / K8s Secret | same |
| OpenShift | Deployment + Route | internal registry | Secret | cluster monitoring |
| AWS | ECS Fargate | ECR | Secrets Manager | CloudWatch Logs |
| Azure | Container Apps | ACR | Key Vault via managed identity | Log Analytics |
| GCP | Cloud Run | Artifact Registry | Secret Manager | Cloud Logging |

Network: local labs bind to 127.0.0.1. Kubernetes allows ingress only on port 8000. Cloud labs use public endpoints during the lab only (AWS restricted by CIDR).

From fde-05 the matrix adds GPU serving: serverless GPU endpoints (RunPod, Modal, Vast.ai) for learning, and an on-prem Kubernetes or OpenShift GPU node as the regulated-customer reference.
