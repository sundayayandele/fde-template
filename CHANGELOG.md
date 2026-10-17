# Changelog

All notable changes. Versions follow semantic versioning; the starter repo is republished on every `v*` tag.

## [Unreleased]

## [0.1.0] - 2026-10-13

### Added
- FastAPI service with health, metrics and a hello endpoint; provider-agnostic LLM client (Mistral default; OpenAI, DeepSeek, Qwen, Kimi, self-hosted) with a data-residency guard.
- Deployment matrix: Compose (Docker, Podman, Rancher Desktop), Podman pod spec, Kubernetes base with docker-desktop, rancher-desktop, kind and cloud overlays, OpenShift overlay, Helm chart, Terraform for AWS, Azure and GCP with budget alerts.
- Starter generator (`scripts/make_starter.py`), `publish-starter` workflow, end-to-end smoke test, structure check.
- CI workflows: ci, e2e (process, Compose, kind), security, iac, manifests, diagrams, evals.
- Documentation set: architecture, ADRs, customer, security, MLOps, datasets, infrastructure, learning, TCO.
