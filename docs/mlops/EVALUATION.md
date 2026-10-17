# Evaluation

> Phase repos describe here how every number in the README results table is produced.

## Rules

1. Define the business metric before building, then the technical metrics that predict it.
2. Freeze the test split (or golden set) and record its version and checksum.
3. Compare every candidate on the same data, with the same method, on the same date.
4. Report quality, p50/p95 latency, memory, and cost per 1,000 requests together.
5. Keep failure analysis: examples of errors and what they have in common.
6. Results are produced by a script (`evals/run.py` or `make measure`), not by hand.

## Promotion gate

A candidate is promoted only if it meets the agreed quality bar without breaking the latency and cost limits. The gate is written in the repo's decision memo before the comparison is run.
