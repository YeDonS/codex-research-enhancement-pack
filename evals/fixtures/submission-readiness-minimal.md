# Fixture: Submission Readiness Minimal

## Skill Under Test

`submission-readiness-reviewer`

## Scenario

The user asks whether a draft paper is ready for submission to a machine learning conference.

Available materials:

- Manuscript: `paper/main.tex`
- Figures: `paper/figures/fig1.pdf`, `paper/figures/fig2.pdf`
- Tables: `paper/tables/table1.tex`, `paper/tables/table2.tex`
- Experiment logs: `runs/main_experiment/metrics.json`, `runs/ablation/metrics.json`
- Target venue:
  - Anonymous submission required.
  - Reproducibility statement required.
  - Data/code availability statement required.
  - Main paper limit: 8 pages excluding references.

Known issues in the draft:

- Abstract says "our method consistently outperforms all baselines across tasks."
- `table1.tex` has 3 datasets, but the method loses on Dataset B macro-F1.
- `fig2.pdf` is not referenced in the text.
- Table 2 reports ablation numbers but `runs/ablation/metrics.json` has no seed field.
- The reproducibility statement says "code will be released later" but gives no environment, data version, seed, or output path.
- The manuscript thanks "Dr. Chen from our lab" in the acknowledgements, violating anonymity.
- Page count is 9 pages before references.

## Expected Behavior

The output must not say the paper is ready. It should:

- Mark the submission as blocked or major revision.
- Flag the overclaim in the abstract and tie it to Dataset B.
- Flag anonymity violation.
- Flag missing reproducibility details.
- Flag page-limit violation.
- Identify unreferenced Figure 2.
- Provide next smallest actions before prose polishing.

## Acceptance Criteria

- Findings appear before general summary or polishing.
- Decision is not "ready".
- At least one blocker cites anonymity or page limit.
- Claim-evidence map catches the "consistently outperforms" overclaim.
- Reproducibility check catches missing seeds/environment/data version/output path.
- Figure/table audit catches unreferenced Figure 2.
