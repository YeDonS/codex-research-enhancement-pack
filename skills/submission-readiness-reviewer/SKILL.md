---
name: submission-readiness-reviewer
description: Use when the user is preparing a paper, preprint, thesis, camera-ready, rebuttal, revision, or submission package and needs to audit claims, figures, tables, references, limitations, reproducibility statements, venue requirements, and reviewer-response readiness before submission.
---

# Submission Readiness Reviewer

## Trigger

Use this skill when the user asks whether a manuscript, preprint, thesis chapter, camera-ready package, rebuttal, revision, or supplement is ready to submit or needs a pre-submission audit.

## Inputs

- Manuscript draft, abstract, figures, tables, supplement, appendix, response letter, or submission checklist.
- Target venue or journal requirements: page limit, anonymity, artifact policy, data/code availability, ethics, formatting, and file rules.
- Evidence cards, experiment logs, analysis outputs, result tables, code/data manifests, and reproducibility records.
- Reviewer comments and revision notes if auditing a response or resubmission.

## Procedure

1. Define submission scope:
   - Identify target venue, submission type, deadline, anonymity rules, and required files.
   - Stop if venue constraints or manuscript scope are unclear enough to affect readiness.
2. Audit claim-evidence traceability:
   - Map abstract, introduction, contribution, result, and conclusion claims to citations, figures, tables, experiments, or analysis logs.
   - Flag unsupported novelty, causality, universality, superiority, and clinical/practical impact claims.
3. Audit figures and tables:
   - Check numbering, captions, units, sample sizes, uncertainty, statistical tests, axis labels, legends, and whether each is cited in text.
   - Verify every table/figure claim matches the underlying output path or evidence card.
4. Audit methods and reproducibility:
   - Check data, code, environment, seeds, hyperparameters, preprocessing, exclusion criteria, compute, ethics/IRB, and availability statements.
   - Flag missing artifacts or statements that prevent reproduction.
5. Audit limitations and risk statements:
   - Ensure limitations cover known data, method, external validity, statistical, ethical, and deployment boundaries.
   - Reject limitations that only soften wording without naming actual risks.
6. Audit reviewer-response readiness:
   - For revisions, map each reviewer comment to a response, manuscript change, location, and residual risk.
   - Flag comments answered only rhetorically without a manuscript change or evidence.
7. Decide readiness:
   - Classify findings as Blocker, Major, Minor, or Ready.
   - Provide the smallest fix list before writing or polishing prose.

## Output Format

```markdown
# Submission Readiness Review

## Scope
| Item | Value |

## Decision
- Status:
- Reason:

## Findings
| Priority | Area | Finding | Evidence | Required Fix |

## Claim-Evidence Map
| Claim | Location | Evidence | Verdict |

## Figure/Table Audit
| Item | Issue | Evidence Path | Fix |

## Reproducibility and Compliance
| Requirement | Status | Evidence | Fix |

## Reviewer Response Map
| Comment | Response | Manuscript Change | Status |

## Next Smallest Actions
```

## Quality Standards

- Findings come before prose polishing.
- Every blocker cites a manuscript location, artifact path, venue rule, reviewer comment, or evidence card.
- Claims are not accepted unless they trace to evidence.
- Figure/table numbers, captions, metrics, sample sizes, and uncertainty must be internally consistent.
- Reproducibility, ethics, data/code availability, and anonymity rules are checked when relevant.
- Reviewer responses must map to concrete manuscript changes or explain why no change is appropriate.
- The final decision distinguishes ready, minor edits, major revision, and blocked submission.

## Failure Repair

- If manuscript files are missing, audit the available sections and list missing required files.
- If venue rules are unknown, run a generic readiness audit but mark venue compliance as unresolved.
- If evidence paths are missing, stop claim approval and request logs, tables, figures, or evidence cards.
- If the user asks only for polishing while blockers exist, report blockers first and defer polishing.
- If reviewer comments are vague, rewrite them into checkable requirements before judging the response.
