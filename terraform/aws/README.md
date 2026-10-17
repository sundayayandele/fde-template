# AWS lab stack

ECR, ECS Fargate (0.25 vCPU, 512 MB, one task, public IP, no load balancer), CloudWatch Logs,
Secrets Manager and a monthly budget with alerts at 50, 80 and 100 percent of USD 50.

```bash
make tf-aws-init
terraform -chdir=terraform/aws plan -out=tfplan -var alert_email=you@example.com -var allowed_cidr=$(curl -s ifconfig.me)/32
make tf-aws-apply

# Push the image, set the secret, then roll the service
REPO=$(terraform -chdir=terraform/aws output -raw ecr_repository_url)
aws ecr get-login-password | docker login --username AWS --password-stdin ${REPO%/*}
docker tag fde-service:local $REPO:0.1.0 && docker push $REPO:0.1.0
aws secretsmanager put-secret-value --secret-id $(terraform -chdir=terraform/aws output -raw secret_arn) \
  --secret-string "{\"MISTRAL_API_KEY\":\"$MISTRAL_API_KEY\"}"
aws ecs update-service --cluster fde-service --service fde-service --force-new-deployment

# Smoke test, then destroy
IP=$(eval "$(terraform -chdir=terraform/aws output -raw find_public_ip)")
python scripts/smoke_test.py --base-url http://$IP:8000
make tf-aws-destroy
```

Build the image for `linux/amd64` if you are on Apple silicon: `docker build --platform linux/amd64 ...`.
Costs are listed in `docs/COST-TCO.md`. Use a sandbox account, never production.
