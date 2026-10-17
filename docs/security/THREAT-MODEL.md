# Threat model

> STRIDE-style summary. Phase repos extend it for their data and model risks
> (prompt injection, PII leakage, model abuse).

## Assets

API availability, LLM API keys, any data sent to the API, cloud account spend.

## Threats and mitigations

| Threat | STRIDE | Mitigation in template | Residual risk |
| --- | --- | --- | --- |
| Leaked API key in Git | Information disclosure | `.gitignore`, gitleaks in CI, secret stores | Keys pasted into issues or logs |
| Regulated data sent to a non-sovereign LLM | Information disclosure | `regulated_data_allowed` guard | Code that bypasses `LLMClient` |
| Container breakout or privilege escalation | Elevation of privilege | Non-root, read-only FS, dropped capabilities, restricted PSS | Kernel vulnerabilities |
| Denial of service or runaway cost | Denial of service | Resource limits, max replicas, scale-to-zero, budgets | No API rate limiting in the template |
| Vulnerable dependency or base image | Tampering | pip-audit, Trivy, ECR scan | Zero-days |
| Unauthenticated access to lab endpoint | Spoofing | Local labs bind 127.0.0.1; AWS restricted by CIDR | Azure and GCP lab endpoints are public while deployed |

## Accepted lab trade-offs

These are deliberate to keep each cloud lab within USD 50 per month, and are reported (not blocking) by the Trivy misconfiguration scan:

- Public lab endpoints on Azure Container Apps and Cloud Run while a lab runs; destroy afterwards.
- Provider-managed encryption keys, not customer-managed keys.
- Open egress, because the service calls hosted LLM APIs. fde-05 shows the air-gapped alternative.
- No load balancer or WAF on AWS.
