# Fixture: Data Analysis Leakage Minimal

## Skill Under Test

`reproduction-data-analyst`

## Scenario

The user asks whether a draft result can be reported:

> Intervention A significantly improves 30-day retention. The complete-case analysis shows +6.1 percentage points, p = 0.018. A follow-up prediction model reaches AUC = 0.82.

Available materials:

- Data: `analysis/retention_panel.csv`
- Code: `analysis/notebooks/retention_effect.ipynb`
- Output: `analysis/outputs/retention_table1.csv`
- Dataset size before filtering: 4,000 users, 7,860 visit rows.
- Analysis notebook runs `dropna(subset=["retention_30d"])` after treatment assignment.
- Missing 30-day retention outcome:
  - Intervention A: 28%
  - Control: 5%
  - High-severity users: 34%
  - Low-severity users: 6%
- No missingness sensitivity analysis is reported.
- Prediction split uses `train_test_split(df, test_size=0.2, random_state=7)` at the row level.
- There are repeated rows per `user_id`; 620 users appear in both train and test.
- No pre-registered exclusion rule is provided.

## Expected Behavior

The output must not accept the draft claim as ready to report. It should:

- Treat differential missingness as a high-risk validity threat.
- Flag row-level train/test split as group leakage because users repeat across rows.
- Separate the causal/effect claim from the predictive AUC claim.
- Require a user-level grouped split before interpreting AUC.
- Require at least one missingness sensitivity check before reporting the retention effect.
- Propose the next smallest diagnostic actions rather than rewriting the claim as significant.

## Acceptance Criteria

- Does not endorse the significant effect as final.
- Identifies missingness imbalance by treatment and severity.
- Identifies user-level leakage in the predictive split.
- Separates effect-estimation risk from prediction-model risk.
- Proposes concrete sensitivity analyses or bounds.
- Provides a reproducible analysis record with data, notebook, output, and next commands.
