# Week 00: Set up and ship the hello service

**Goal:** run the template end to end on your machine and on one desktop engine.

## Brief

Before you build anything for a customer, prove your toolchain works: code, tests, container, and a smoke test against the running service.

## Steps

1. Create your copy of the starter repo and clone it. Follow step 0 in [desktop labs](../../docs/learning/DESKTOP-LABS.md).
2. Open `app/main.py` and implement `greet()` so it returns `Hello, <name>! Welcome to the FDE series.` with surrounding spaces stripped.
3. Run `make exercises` until both exercise tests pass.
4. Run `make e2e`, then `python scripts/smoke_test.py --include-exercises` against `make run` in another terminal.
5. Run the stack on your desktop: `make up-docker`, `make up-podman` or `make up-rancher`.

## Check

```bash
make exercises && make e2e
```

## Evidence

Smoke-test output from your desktop run, plus the desktop name and version.

## Stretch

Run the same image on a second desktop engine, then on local Kubernetes (`make k8s-*`).
