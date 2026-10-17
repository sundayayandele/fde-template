# Security

## Controls in the template

| Area | Control | Where |
| --- | --- | --- |
| Container | Non-root user (UID 10001, group 0 for OpenShift), read-only root filesystem, all capabilities dropped, no privilege escalation | `Dockerfile`, Compose, pod spec, Kubernetes base, Helm |
| Kubernetes | Pod Security Standard `restricted` on the namespace, seccomp `RuntimeDefault`, no service-account token, NetworkPolicy on ingress | `deploy/kubernetes/base` |
| Secrets | Never in Git; environment, Kubernetes Secret, Secrets Manager, Key Vault (RBAC + managed identity) or Secret Manager | `.gitignore`, Terraform |
| Data residency | `regulated_data_allowed` per provider; `DataResidencyError` guard in the LLM client | `config/providers.yaml`, `llm.py` |
| Supply chain | pip-audit, Trivy (dependencies, secrets, image), gitleaks, ECR scan on push | `security` workflow |
| Local labs | Ports bound to 127.0.0.1 only | Compose, pod spec |
| Cloud | Budgets with alerts; lab endpoints restricted by CIDR on AWS | Terraform |

## Reporting a vulnerability

Open a private security advisory on the repository (Security → Advisories), not a public issue.

## Not covered by the template

Authentication and authorisation on the API, rate limiting, WAF and TLS for public endpoints are added by phase repos that expose real data (from fde-05, which adds an authenticated gateway). See the [threat model](THREAT-MODEL.md).
