---
name: literature-evidence-reader
description: Use for research paper reading, literature review, Zotero or Obsidian knowledge-base ingestion, PDF parsing, evidence extraction, method analysis, variable tables, and preventing shallow AI summaries. Trigger when the user wants Codex to turn papers into reusable research knowledge.
---

# Literature Evidence Reader

## Trigger

Use this skill when the user asks Codex to read papers, build a literature knowledge base, summarize a PDF, prepare related work, extract methods, compare studies, or import paper notes into Obsidian/Zotero.

## Inputs

- PDF, DOI, URL, Zotero export, or local paper folder.
- User's research question or reading purpose.
- Optional supplement, code repo, dataset link, figures, tables, or prior notes.
- Target output location, such as Obsidian, Markdown, CSV, or project docs.

## Procedure

1. Preflight:
   - Confirm full text is available.
   - Check whether figures, tables, appendix, and supplement are accessible.
   - Identify paper type: empirical, methods, benchmark, review, theory, dataset, clinical, or position.
   - Stop if only abstract is available unless the user explicitly accepts an abstract-only pass.
2. Scope:
   - Choose one reading goal: understand, reproduce, compare, extract evidence, or support writing.
   - Limit to one paper or one narrow question unless the user asks for a broader review.
3. Extract evidence:
   - Build evidence cards with claim, evidence location, method, sample/data, metric, result, limitation, and confidence.
   - Build method cards with protocol, assumptions, required data, variables, parameters, and reproducibility notes.
   - Build variable tables for constructs, operational definitions, measures, and confounders.
4. Read beyond abstract:
   - Inspect methods, results, figures, tables, supplement, and limitations.
   - Separate author claims from directly supported evidence.
5. Decide入库:
   - Only store cards that have a source location and a reason to reuse.
   - Store summaries as navigation aids, not as the primary knowledge object.
6. Cross-paper integration, if multiple papers:
   - Compare claims, methods, datasets, contradictions, and evidence strength.
   - Do not merge papers without keeping per-paper provenance.
7. Final lint:
   - Check every key claim has a citation location.
   - Mark open questions and missing material.
   - Suggest the smallest next reading or experiment.

## Output Format

```markdown
# Paper Reading Pack

## Preflight
- Full text:
- Figures/tables:
- Supplement:
- Reading goal:

## One-Sentence Use

## Evidence Cards
| Claim | Evidence Location | Method/Data | Result | Limitation | Confidence |

## Method Cards
| Method Step | Inputs | Assumptions | Parameters | Repro Notes |

## Variable Table
| Variable | Definition | Measurement | Role | Caveats |

## Reusable Notes
- Evidence worth storing:
- Do not store:

## Open Questions

## Next Step
```

## Quality Standards

- At least 5 evidence cards for a full empirical paper unless the paper is very short.
- Every major claim points to page, section, figure, table, or supplement.
- Figures and tables are explicitly checked.
- The output distinguishes summary, evidence, interpretation, and next action.
- No “needs manual review” dump without saying what exactly must be checked.

## Failure Repair

- If token or runtime grows, shrink to one section, one figure, or one claim.
- If PDF parsing fails, ask for PDF pages/images or use a text extraction fallback.
- If evidence is weak, output “not enough evidence” and do not入库.
- If output becomes summary-only, rerun from evidence card extraction and require source locations.
- If the user wants full automation, propose staged automation: single paper first, then confirmed batch ingestion.
