# Cost and total cost of ownership

> Prices change often. Phase repos fill the price table from each provider's pricing page,
> with the date checked, and compute costs from measured usage rather than guesses.

## Price table (fill in, with date)

| Item | Unit | Price | Source page | Checked on |
| --- | --- | --- | --- | --- |
| AWS Fargate vCPU / GB | per hour | | aws.amazon.com/fargate/pricing | |
| Azure Container Apps vCPU / GiB | per second (consumption) | | azure.microsoft.com/pricing/details/container-apps | |
| GCP Cloud Run vCPU / GiB | per second | | cloud.google.com/run/pricing | |
| Mistral model (per role) | per million tokens in / out | | mistral.ai/pricing | |
| GPU (fde-04 to fde-06) | per second / hour | | provider pricing page | |

## How to compute

```text
monthly_compute = hours_running × (vCPU × vCPU_price + GB × GB_price)
cost_per_1k_requests = 1000 × (compute_per_request + tokens_in × price_in + tokens_out × price_out)
```

Measure `tokens_in`, `tokens_out` and requests per second from your own runs (metrics and logs), not from estimates.

## Three scenarios

| Scenario | When it fits | Main cost drivers |
| --- | --- | --- |
| Local / on-prem / private cloud | Regulated data, steady load, existing hardware (for example BlueHarvest or OpenShift) | Hardware amortisation, power, operations staff |
| Self-hosted VPS | Small pilots, predictable load | Fixed monthly instance; your time to operate it |
| Hyperscaler (AWS, Azure, GCP) | Spiky load, managed services, enterprise procurement | Per-use compute, egress, managed service fees, LLM tokens |

## Lab budget

USD 50 per month per cloud and USD 100 per month for GPUs across fde-04 to fde-06. Every stack creates a budget alert; every lab ends with `destroy`.
