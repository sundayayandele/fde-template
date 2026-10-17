# Capacity planning

> Measure before you size. Phase repos replace the estimates below with load-test results.

## Method

1. Run the service at a fixed resource limit (for example 0.5 vCPU, 512 MiB).
2. Load-test the main endpoint with a ramp (for example `hey`, `k6` or `locust`) and record requests per second at the p95 latency target.
3. Divide expected peak traffic by that throughput, add headroom (30-50%), and round up to replicas.
4. Re-check after every model or dependency change.

## Starting estimates (template, not measured)

| Component | Request | Limit | Notes |
| --- | --- | --- | --- |
| API pod | 100m CPU, 128 MiB | 500m CPU, 512 MiB | FastAPI without a model; most time is spent waiting on LLM APIs |
| Desktop engine VM | 2 CPU, 4 GiB | 4 CPU, 8 GiB | Enough for the API plus Prometheus and Grafana |

LLM-backed endpoints are usually bound by provider latency and rate limits, not local CPU. Size replicas by concurrent requests in flight, and record tokens per request for cost.
