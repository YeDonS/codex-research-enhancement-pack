---
name: experiment-design-planner
description: Use when the user needs to design, audit, or repair a research experiment, reproduction study, ablation, benchmark, data analysis plan, or pilot study. Focuses on hypotheses, variables, controls, metrics, confounders, failure criteria, reproducibility, and risk tradeoffs.
---

# Experiment Design Planner

## Trigger

Use this skill when the user asks to design an experiment, test a hypothesis, plan a reproduction, compare methods, run an ablation, define evaluation metrics, or decide whether an experiment result is trustworthy.

## Inputs

- Research question or hypothesis.
- Candidate intervention, model, method, prompt, workflow, or treatment.
- Data sources, sample size, inclusion/exclusion rules, labels, and known data quality issues.
- Baselines, metrics, expected effects, constraints, time/budget/compute limits.
- Existing code, logs, prior runs, paper methods, or evidence cards.
- Risk priorities such as fairness, calibration, safety, privacy, reproducibility, or subgroup performance.

## Procedure

1. Frame the decision:
   - State the hypothesis and the null or failure alternative.
   - Identify what decision the experiment should enable: continue, reject, narrow, scale, or redesign.
2. Define variables:
   - Independent variable, dependent variables, controls, moderators, confounders, and exclusion criteria.
   - Include subgroup variables if fairness or heterogeneous effects are plausible.
3. Choose metrics:
   - Pick primary metric before seeing results.
   - Add guardrail metrics for calibration, subgroup performance, cost, latency, safety, or error types.
   - Define the minimum effect size or practical threshold.
4. Design the smallest credible test:
   - Prefer a pilot or slice before full benchmark.
   - Define sample size, split, random seed, baseline, ablations, and stopping condition.
   - Separate exploratory analysis from confirmatory claims.
5. Plan reproducibility:
   - Record data version, code version, environment, commands, seeds, outputs, and artifact paths.
   - Predefine how to handle failed runs, missing labels, and excluded data.
6. Audit tradeoffs:
   - Check whether the primary metric can improve while guardrail metrics worsen.
   - Require a decision rule for conflicting metrics.
   - Do not recommend scaling an experiment if a critical guardrail fails.
7. Output a runnable plan and review checklist.

## Output Format

```markdown
# Experiment Plan

## Decision
- Hypothesis:
- Null/failure alternative:
- Decision enabled:

## Design
| Component | Choice | Rationale | Risk |

## Variables
| Variable | Role | Measurement | Notes |

## Metrics
| Metric | Type | Threshold | Why |

## Run Plan
- Data:
- Baseline:
- Treatment:
- Commands:
- Seeds:
- Outputs:

## Decision Rules
- Continue if:
- Revise if:
- Stop if:

## Reproducibility Record

## Review Checklist
```

## Quality Standards

- The hypothesis is falsifiable.
- The primary metric is named before the run.
- At least one guardrail metric is included when harms or regressions are plausible.
- Confounders and subgroup risks are explicitly listed.
- The plan includes commands or concrete execution steps when code is available.
- Decision rules include what to do if metrics conflict.
- Reproducibility details are sufficient for another session to rerun or audit.

## Failure Repair

- If the experiment is too broad, shrink to one dataset, one method, one metric, or one subgroup.
- If metrics conflict, do not average them away; define a tradeoff rule or run a discriminating follow-up.
- If data quality is weak, run a data audit before model comparison.
- If the result is underpowered, label it exploratory and avoid strong claims.
- If reproduction details are missing, stop and create a run log template before executing.
