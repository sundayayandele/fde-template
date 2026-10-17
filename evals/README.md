# Evals

Phase repos put their evaluation harness here:

| Path | Content |
| --- | --- |
| `evals/run.py` | Entry point: `python evals/run.py --mode fixtures|live`; writes `evals/results/*.md` |
| `evals/golden/` | Versioned golden sets (small, licence-compatible, no PII) or scripts that build them |
| `evals/fixtures/` | Recorded model responses so pull requests never call a paid API |
| `evals/results/` | Committed result reports; the README results table is copied from here |

The `evals` workflow runs `evals/run.py` on pull requests (fixtures) and nightly (live).
