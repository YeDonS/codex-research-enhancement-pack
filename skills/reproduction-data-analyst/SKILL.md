---
name: reproduction-data-analyst
description: Use when the user wants to reproduce paper code, audit a computational result, run data analysis, compare local results to a paper, debug metric mismatches, or produce reproducible research logs with data, environment, commands, seeds, and outputs.
---

# Reproduction Data Analyst

## Trigger

Use this skill when the user asks to reproduce a paper, run or audit code, analyze data, validate metrics, compare results to a paper/table/figure, debug failed reproduction, or create a reproducible analysis report.

## Inputs

- Paper target result, table, figure, or claim to reproduce.
- Repository, scripts, notebooks, configuration files, or command examples.
- Dataset location, version, split rules, preprocessing, labels, and checksums if available.
- Environment details: OS, package manager, dependencies, GPU/CPU, model versions, seeds.
- Local run logs, errors, metrics, artifacts, and expected metrics.
- Tolerance threshold for matching the target result.
- Simulator/model semantics, loaded binary or module identity, compile flags, and mechanism counters when the result depends on an implementation model.
- Missingness rules, exclusion criteria, grouping keys, leakage risks, and sensitivity analyses if the task is data analysis rather than code reproduction.

## Procedure

1. Define reproduction target:
   - Name the exact paper table, figure, metric, dataset split, and tolerance.
   - Stop if the target is vague.
2. Preflight repository and environment:
   - Inspect README, configs, dependency files, scripts, and expected data paths.
   - Record package versions, hardware, model/checkpoint versions, and random seed controls.
   - Freeze a run manifest containing source/binary hashes, compile flags, model semantics, workload parameters, seeds, and drain/completion policy.
3. Audit data provenance and analysis validity:
   - Verify dataset version, split, preprocessing, filtering, label mapping, and checksums.
   - For data analysis, check missingness, exclusion timing, grouping keys, repeated subjects, label leakage, train/test leakage, and whether sensitivity analyses are needed.
   - Identify paper/local differences before running expensive jobs.
4. Run smallest credible command:
   - Prefer smoke test or single-seed/small-slice run before full reproduction.
   - Capture exact command, working directory, config, seed, stdout/stderr, output path, and runtime.
5. Compare metrics:
   - Report target, local result, delta, tolerance, and pass/fail.
   - Include confidence intervals or seed variance when available.
   - Preserve raw distributions or histogram buckets when a tail/percentile claim is central, and verify that bucket/sample totals match the reported request count.
6. Diagnose mismatch:
   - Check data version, preprocessing, split, dependency drift, checkpoint mismatch, nondeterminism, metric implementation, hardware differences, missingness bias, and leakage.
   - Do not declare success if the metric is outside tolerance.
   - Require nonzero trigger/use counters before attributing a result to a scheduler, cache, migration, GC, or other claimed mechanism.
   - Separate simulator behavior from hardware behavior unless device evidence validates the same semantics.
7. Produce handoff:
   - Record what was reproduced, what failed, evidence paths, suspected causes, and next smallest diagnostic run.

## Output Format

```markdown
# Reproduction/Data Analysis Report

## Target
| Item | Value |

## Preflight
| Area | Status | Evidence | Risk |

## Run Log
| Command | CWD | Config | Seed | Output | Status |

## Metric Comparison
| Metric | Paper Target | Local Result | Delta | Tolerance | Verdict |

## Mismatch Triage
| Suspected Cause | Evidence | Next Check |

## Reproducibility Record

## Model And Mechanism Contract
| Claim | Model Boundary | Trigger Counter | Use Counter | Evidence | Verdict |

## Decision
- Reproduced:
- Not reproduced:
- Next smallest action:
```

## Quality Standards

- Every reported metric links to a command, config, data version, and output path.
- Dataset version and split are checked before interpreting results.
- Missingness, exclusions, repeated subjects, grouping keys, and leakage are checked before accepting data-analysis claims.
- Matching criteria or tolerance are explicit.
- Failed reproduction is reported as failed, not softened into success.
- Mismatch triage names concrete causes and next checks.
- Long runs start with a smoke test or small-slice test unless the user explicitly approves full cost.
- Generated artifacts are not committed blindly; large data and model files are referenced by path or manifest.
- Baseline and treatment manifests match on every non-treatment field before metrics are compared.
- Tail claims retain recomputable distributions and pass sample-conservation checks.
- A mechanism with zero observed trigger/use count cannot explain an improvement.
- Static tests do not substitute for building and running the loaded binary/module on the target environment.

## Failure Repair

- If target result is vague, ask for table/figure/metric/dataset/tolerance before running.
- If data version is unknown, run a data manifest audit first.
- If dependency installation fails, record the failure and isolate environment requirements before changing code.
- If local result differs, compare one cause at a time instead of editing multiple variables.
- If a data-analysis result is significant but missingness or leakage is unresolved, do not report the claim as final; run sensitivity analysis or grouped evaluation first.
- If runs are nondeterministic, repeat seeds or report variance before deciding.
- If output paths are missing, stop and add run logging before continuing.
- If manifests differ outside the treatment variable, reject the comparison and rerun a clean ablation.
- If model semantics are ambiguous, label the result as simulator-only and add a discriminating synthetic trace before making a hardware claim.
- If a percentile summary cannot be recomputed or its samples do not balance, repair instrumentation before interpreting performance.
