# Real-Task Validation: Storage Simulator Repair

Date: 2026-06-22

## Scope

This validation applied `research-program-manager`,
`reproduction-data-analyst`, and `experiment-design-planner` to a real
multi-variant storage-simulator project. The task was to repair code and
evaluation validity after a conversation audit found model-claim ambiguity,
confounded variants, mixed metric layers, and missing runtime identity.

Private conversations and local paths remain outside this public package.

## Input Materials

- Existing HP/LP timing implementation and per-resource locking.
- Latency1/2/3 wrapper variants and build mapping.
- SQLite and FIO experiment scripts.
- Static/model tests, result analyzer, and prior diagnostic handoff.

## Extracted Methods

1. Label simulator semantics in runtime output; do not infer hardware
   preemption from queue-tail arithmetic.
2. Add a minimal one-resource synthetic trace that contrasts the implemented
   model with a non-preemptive reference.
3. Export raw histogram buckets, not only percentiles, and require sample
   conservation.
4. Freeze module/artifact hashes, compile flags, workload parameters, seeds,
   and drain policy in a per-run manifest.
5. Reject mechanism attribution when trigger/use counters are zero or when
   baseline and treatment manifests differ outside the intended intervention.

## Implemented Artifacts

| Artifact | Purpose |
|---|---|
| Model label and synthetic trace | Bounds the claim to queue deferral and exposes the non-preemptive alternative |
| Raw request-latency histogram output | Makes p50/p95/p99/p999 independently auditable |
| Histogram analyzer contract | Rejects bucket/sample count mismatch |
| Per-run JSON manifest | Records module/artifact hashes, parameters, environment and model |
| Compile/model/metric strict contracts | Fails invalid runs before comparison |
| FIO and SQLite integration | Generates manifests for each experiment case |
| Research runbook | Defines canonical variants, metric dictionary and claim gates |

## Verification

| Check | Result |
|---|---|
| Static latency invariants | Pass |
| Queue-deferral vs non-preemptive synthetic trace | Pass |
| SQLite analyzer regression and verdict tests | Pass |
| Manifest capture/strict-contract/compare tests | Pass |
| Python compilation and shell syntax | Pass |
| One-case FIO dry-run manifest generation | Pass |
| Target Linux kernel-module build/load/stress | Pending; unavailable on the development host |

## Capability Verdict

| Capability | Verdict | Evidence |
|---|---|---|
| Program state recovery and scoped repair | Pass | Audit issues mapped to bounded code/test/doc changes |
| Reproducibility instrumentation | Pass for static/dry-run scope | Hash manifests and strict comparison contracts execute |
| Model-semantic claim control | Pass | Runtime label and discriminating synthetic trace added |
| Runtime systems validation | Partial | Target-kernel module build/load and stress remain required |

## Generalization Decision

Keep and add to skills:

- Immutable run-manifest comparison.
- Raw-distribution sample conservation.
- Counter-gated mechanism attribution.
- Simulator-versus-hardware model contract.

Rewrite or delete:

- Delete “performance improved, therefore mechanism X worked.”
- Rewrite “read priority preempts NAND” as queue-deferral behavior unless
  device-level evidence supports physical suspension/preemption.
- Delete any comparison whose compile flags or workload manifest do not match.

## Next Validation

Build and load the repaired module on the target Linux kernel, run the canonical
four-variant matrix, retain foreground and post-drain counters, and compare only
manifests whose strict contracts pass.
