# Eval Output: Submission Readiness Minimal

Fixture: `evals/fixtures/submission-readiness-minimal.md`

Skill: `submission-readiness-reviewer`

# Submission Readiness Review

## Scope

| Item | Value |
|---|---|
| Manuscript | `paper/main.tex` |
| Target venue | Anonymous ML conference submission |
| Required files checked | Main paper, figures, tables, experiment logs |
| Venue requirements in fixture | Anonymous, reproducibility statement, data/code availability, 8 pages excluding references |

## Decision

- Status: Blocked.
- Reason: The draft violates anonymity and page limit requirements, contains an unsupported abstract overclaim, and lacks enough reproducibility detail to support the reported results.

## Findings

| Priority | Area | Finding | Evidence | Required Fix |
|---|---|---|---|---|
| Blocker | Anonymity | Acknowledgements identify "Dr. Chen from our lab" | `paper/main.tex` acknowledgements | Remove or anonymize acknowledgements for review copy |
| Blocker | Page limit | Main paper is 9 pages before references; venue limit is 8 | Venue requirement and current draft count | Cut or move content to appendix until main paper is <= 8 pages |
| Major | Abstract claim | "Consistently outperforms all baselines" is contradicted by Dataset B | `paper/tables/table1.tex` has 3 datasets; method loses on Dataset B macro-F1 | Rewrite to condition the claim, e.g. "improves on two of three datasets" if supported |
| Major | Reproducibility | Statement says "code will be released later" but omits environment, data version, seeds, and output paths | Reproducibility statement; `runs/ablation/metrics.json` has no seed field | Add environment, data version, commands, seeds, output paths, and artifact status |
| Major | Ablation traceability | Table 2 ablation numbers lack seed metadata | `paper/tables/table2.tex`, `runs/ablation/metrics.json` | Re-run or regenerate log with seed/config fields before finalizing table |
| Minor | Figure reference | Figure 2 is present but not cited in text | `paper/figures/fig2.pdf` | Cite Figure 2 in the relevant results section or remove it |

## Claim-Evidence Map

| Claim | Location | Evidence | Verdict |
|---|---|---|---|
| Method consistently outperforms all baselines across tasks | Abstract | `table1.tex` shows a loss on Dataset B macro-F1 | Reject/Rewrite |
| Ablation supports the main component contribution | Table 2 discussion | `runs/ablation/metrics.json` lacks seed field | Not approved until run metadata is fixed |
| Results are reproducible | Reproducibility statement | No environment, data version, command, seed, or output path | Reject |

## Figure/Table Audit

| Item | Issue | Evidence Path | Fix |
|---|---|---|---|
| Figure 2 | Not referenced in text | `paper/figures/fig2.pdf` | Add textual reference or remove figure |
| Table 1 | Abstract overgeneralizes result | `paper/tables/table1.tex` | Align claim with per-dataset results |
| Table 2 | Missing seed traceability | `paper/tables/table2.tex`, `runs/ablation/metrics.json` | Add seed/config metadata or rerun |

## Reproducibility and Compliance

| Requirement | Status | Evidence | Fix |
|---|---|---|---|
| Anonymous submission | Failed | Acknowledgements name lab colleague | Remove identifying acknowledgement |
| Page limit | Failed | 9 pages before references; limit is 8 | Reduce one page or move material |
| Reproducibility statement | Failed | No environment, data version, seed, command, output path | Add reproducibility record |
| Data/code availability | Incomplete | "Code will be released later" has no artifact plan | State what will be released, where, and when allowed by venue |

## Reviewer Response Map

Not applicable: this is an initial submission readiness audit, not a revision response.

## Next Smallest Actions

1. Produce an anonymous 8-page review copy.
2. Rewrite the abstract claim to match Table 1, especially Dataset B.
3. Add reproducibility details: environment, data version, commands, seeds, output paths, and release plan.
4. Fix or remove Figure 2.
5. Regenerate ablation logs with seed/config metadata before final table approval.

## Acceptance Result

| Criterion | Result |
|---|---|
| Findings appear before polishing | Pass |
| Decision is not ready | Pass |
| Catches anonymity or page-limit blocker | Pass |
| Catches "consistently outperforms" overclaim | Pass |
| Catches missing reproducibility details | Pass |
| Catches unreferenced Figure 2 | Pass |
