# Deployment

| Path | Command | Details |
| --- | --- | --- |
| Local Python | `make run` / `make e2e` | uvicorn on 127.0.0.1:8000 |
| Docker Desktop | `make up-docker`, `make k8s-docker` | [Desktop labs](learning/DESKTOP-LABS.md#1a-docker-desktop) |
| Podman Desktop | `make up-podman`, `make k8s-kind` | [Desktop labs](learning/DESKTOP-LABS.md#1b-podman-desktop) |
| Rancher Desktop | `make up-rancher`, `make k8s-rancher` | [Desktop labs](learning/DESKTOP-LABS.md#1c-rancher-desktop) |
| Managed Kubernetes | `kubectl apply -k deploy/kubernetes/overlays/cloud` | Set the image with `kustomize edit set image` |
| Helm | `helm upgrade --install fde-service deploy/helm/fde-service` | `--set route.enabled=true` on OpenShift |
| OpenShift | `oc apply -k deploy/openshift` | Route with edge TLS |
| AWS / Azure / GCP | `make tf-<cloud>-plan` then the stack README | [Cloud labs](learning/CLOUD-LABS.md) |

## Release

1. Update `CHANGELOG.md`, bump the version in `pyproject.toml`, `Chart.yaml` and Terraform `image_tag` defaults.
2. Tag `vX.Y.Z` and push the tag. The `publish-starter` workflow regenerates the starter repo.
3. Build and push the image to each registry you deploy to, tagged with the same version.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Readiness never turns green | `kubectl logs`, container logs; missing env vars or secrets |
| 5xx after deploy | `HighErrorRate` alert, recent changes in `CHANGELOG.md`, roll back the image tag |
| Cloud service will not start | Image exists in the registry with the expected tag; secret has a value; region matches |
| Budget alert received | `make tf-<cloud>-destroy`; check for orphaned resources in the console |
