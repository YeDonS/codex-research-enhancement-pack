# Eval Output: Project Conversation Curation

## Goal Brief

| Outcome | Scope | Approval Gate | Deliverable |
|---|---|---|---|
| 判断 HP/LP 调度是否解释 request-level tail-latency 变化，并建立可恢复 handoff | 对话、代码片段和 benchmark counters；不直接宣称物理 NAND 行为 | 先审计，再决定是否修改调度语义 | issue register、decision log、context capsule |

## Source Audit

| Source | Quality | Decision | Reason |
|---|---|---|---|
| S1 | Unverified claim | Review | 没有 code/log evidence |
| S2 | Model evidence | Keep as model assumption | 只证明当前模拟器路径 |
| S3 | Experiment evidence | Keep as counterfactual | 说明 latency improvement 不能归因于 yield |
| S4 | Unsupported physical claim | Do not ingest | 缺硬件资料和边界 |
| S5 | Repeated question cluster | Compress | 指向同一归因缺口 |

## Decision and Assumption Log

| Item | Type | Evidence | Status | Reversal Condition |
|---|---|---|---|---|
| HP/LP bypass exists in the simulator | Model assumption | S2 code path | Verified for model only | Code path changes |
| Yield caused the observed improvement | Unverified claim | S3 has `yield_count=0` | Rejected for this run | A run with nonzero yield plus controlled baseline |
| HP/LP bypass models real NAND preemption | Physical claim | None | Open decision | Device documentation or an explicit queue-level framing |

## Repeated-Question Clusters

| Cluster | Canonical Answer | Evidence Needed | Do Not Repeat |
|---|---|---|---|
| “Why did latency improve when yield is zero?” | Improvement may come from a different scheduler path or a confounder; zero yield rules out yield as the direct explanation. | Counter breakdown and isolated ablation | Do not infer causality from one improved aggregate metric. |
| “Why can p99 worsen?” | The primary metric and guardrail may diverge; inspect request-level wait decomposition and workload equivalence. | Same config/seed plus latency histogram | Do not average p99 away with throughput. |

## Context Capsule

- Goal: attribute request-level latency changes to one defined scheduler mechanism.
- Verified state: the simulator contains a HP/LP scheduling rule; the observed run has zero yield.
- Open decision: present bypass as a queue model or require a non-preemptive model.
- Current blocker: treatment and baseline are not yet isolated.
- Next action: run a one-resource trace where LP backlog exists before a read, then report HP/LP start/end, request latency, and counter deltas.

## Acceptance Result

- Pass: separates model behavior from hardware claim.
- Pass: does not attribute a zero-yield run to yield.
- Pass: compresses repeated questions into evidence and a discriminating next experiment.
