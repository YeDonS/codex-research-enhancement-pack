# Eval Output: Data Analysis Leakage Minimal

Fixture: `evals/fixtures/data-analysis-leakage-minimal.md`

Skill: `reproduction-data-analyst`

# Reproduction/Data Analysis Report

## Target

| Item | Value |
|---|---|
| Draft claim | Intervention A improves 30-day retention by +6.1 percentage points, p = 0.018; prediction model AUC = 0.82 |
| Analysis data | `analysis/retention_panel.csv` |
| Notebook | `analysis/notebooks/retention_effect.ipynb` |
| Reported output | `analysis/outputs/retention_table1.csv` |
| Decision needed | Whether the result is valid enough to report |

## Preflight

| Area | Status | Evidence | Risk |
|---|---|---|---|
| Data unit | High risk | 4,000 users but 7,860 visit rows | Repeated users require grouped analysis or clustered uncertainty |
| Outcome filtering | High risk | Notebook runs `dropna(subset=["retention_30d"])` after assignment | Complete-case effect may be biased |
| Missingness balance | Failed | Intervention A missing 28%, control missing 5%; high severity missing 34%, low severity missing 6% | Missingness is associated with treatment and severity |
| Exclusion rule | Missing | No pre-registered exclusion rule provided | Analysis choice may be post hoc |
| Prediction split | Failed | Row-level split; 620 users appear in both train and test | AUC is likely inflated by user leakage |
| Output path | Present | `analysis/outputs/retention_table1.csv` | Output is traceable but not decision-ready |

## Run Log

| Command | CWD | Config | Seed | Output | Status |
|---|---|---|---|---|---|
| `jupyter nbconvert --execute analysis/notebooks/retention_effect.ipynb --to notebook` | project root | notebook defaults | `random_state=7` for row split | `analysis/outputs/retention_table1.csv` | Existing run is auditable but invalid for final reporting |

## Metric Comparison

| Metric or Claim | Reported Result | Audit Finding | Tolerance or Standard | Verdict |
|---|---:|---|---|---|
| 30-day retention effect | +6.1 pp, p = 0.018 | Complete-case analysis after differential missingness | Sensitivity analysis required when missingness differs by treatment/severity | Not accepted |
| Prediction AUC | 0.82 | 620 users appear in both train and test | No repeated subject leakage in held-out evaluation | Not accepted |

## Mismatch Triage

| Suspected Cause | Evidence | Next Check |
|---|---|---|
| Differential outcome missingness | Intervention A 28% missing vs control 5%; high severity 34% vs low severity 6% | Produce missingness table by treatment, severity, and baseline covariates |
| Post-assignment complete-case filtering | `dropna(subset=["retention_30d"])` occurs after assignment | Compare complete-case, missing-as-failure, inverse probability weighting, multiple imputation, or worst/best-case bounds |
| Group leakage in prediction | Row split with repeated `user_id`; 620 users in both train and test | Re-run with `GroupShuffleSplit` or equivalent user-level split |
| Inflated AUC | Same users leak across train/test | Report grouped-split AUC with confidence interval before interpreting model quality |
| Unclear estimand | Draft mixes treatment effect and prediction performance | Split report into causal/effect-estimation claim and predictive validation claim |

## Reproducibility Record

- Data: `analysis/retention_panel.csv`
- Notebook: `analysis/notebooks/retention_effect.ipynb`
- Output: `analysis/outputs/retention_table1.csv`
- Initial rows: 4,000 users, 7,860 visit rows.
- Missing outcome rates: Intervention A 28%, control 5%, high severity 34%, low severity 6%.
- Prediction split: row-level `train_test_split(..., random_state=7)`.
- Leakage evidence: 620 users appear in both train and test.
- Current decision: the result is audit-failed and should not be reported as final.

## Decision

- Reproduced: No final scientific claim is reproduced or accepted.
- Not reproduced: The complete-case retention effect and AUC are not valid enough for reporting because both depend on an analysis pipeline with major validity threats.
- Next smallest action: First generate a missingness audit table and rerun the prediction model with a user-level grouped split. Then rerun the retention effect under at least two missingness sensitivity checks: missing-as-failure and inverse-probability weighting or multiple imputation. Only after those results are stable should the draft claim be rewritten.

## Acceptance Result

| Criterion | Result |
|---|---|
| Does not endorse significant effect as final | Pass |
| Identifies treatment/severity missingness imbalance | Pass |
| Identifies user-level prediction leakage | Pass |
| Separates effect-estimation and prediction risks | Pass |
| Proposes concrete sensitivity analyses | Pass |
| Includes reproducible analysis record | Pass |
