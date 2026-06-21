# Eval Output: Knowledge Curation Minimal

Fixture: `evals/fixtures/knowledge-curation-minimal.md`

Skill: `research-knowledge-curator`

# Research Knowledge Curation Report

## Scope

| Item | Value |
|---|---|
| Project | Evidence-grounded literature review |
| Target vault | `vault/` |
| Operation | Curate mixed paper, Zotero metadata, old note, and experiment log |
| Destination rules | Paper cards, evidence cards, experiment cards, project index |

## Source Audit

| Source | Type | Quality | Decision | Reason |
|---|---|---|---|---|
| `papers/a.pdf` | Full paper | Strong source | Keep and link to existing Paper A note | Full text, DOI, Table 2, limitation section available |
| `notes/paper_a_old.md` | Existing paper note | Stale/unsupported | Rewrite, do not keep old universal claim | Same DOI as Paper A; claim lacks evidence and overgeneralizes |
| `zotero_export/paper_b.json` | Metadata/abstract only | Weak source | Review queue, not strong evidence | No PDF or table/figure evidence |
| `runs/pilot_2026-06-20/metrics.json` | Experiment log | Usable local evidence | Keep as experiment card | Has command, seed, config, output path, and metric values |

## Note Plan

| Path | Note Type | Operation | Source | Required Fields |
|---|---|---|---|---|
| `vault/papers/unknown-paper-a.md` | Paper card | Update/replace duplicate | `papers/a.pdf`, `notes/paper_a_old.md` | title, DOI `10.1234/a`, evidence status, limitation, links to evidence cards |
| `vault/evidence/unsupported-claim-rate-drop-paper-a.md` | Evidence card | Create | `papers/a.pdf` Table 2 | claim, source DOI, evidence location Table 2, metric 18% to 11%, limitation 12 papers |
| `vault/experiments/2026-06-20-pilot-evidence-constrained-review.md` | Experiment card | Create | `runs/pilot_2026-06-20/metrics.json` | command, config, seed, data size, metrics, output path, interpretation limits |
| `vault/indexes/evidence-grounded-literature-review.md` | Index note | Update | Paper A evidence and local pilot | active claims, open questions, linked paper/evidence/experiment cards |
| `vault/review-queue/paper-b.md` | Review queue item | Create | `zotero_export/paper_b.json` | title/metadata if available, abstract-only status, PDF-needed task |

## Claim Registry

| Claim | Source | Evidence Location | Status | Links |
|---|---|---|---|---|
| Evidence-grounded reviewing reduces unsupported-claim rate in Paper A's tested setting | `papers/a.pdf` | Table 2 | Supported with scope limit | `vault/evidence/unsupported-claim-rate-drop-paper-a.md` |
| Method reduces hallucinations across all literature reviews | `notes/paper_a_old.md` | None; contradicted by 12-paper limitation | Reject/rewrite | Replace in Paper A card |
| Retrieval improves factuality | `zotero_export/paper_b.json` | Abstract only | Weak signal | `vault/review-queue/paper-b.md` |
| Local pilot reduced unsupported-claim rate from 14% to 10% | `runs/pilot_2026-06-20/metrics.json` | output log, seed 7, command listed | Local pilot evidence only | `vault/experiments/2026-06-20-pilot-evidence-constrained-review.md` |

## Dedupe and Conflict Log

| Item | Issue | Decision | Follow-up |
|---|---|---|---|
| Paper A | `papers/a.pdf` and `notes/paper_a_old.md` refer to DOI `10.1234/a` | Use one paper card and preserve old note only as rewritten history if needed | Confirm title/year for final slug |
| Universal claim | Old note says "across all literature reviews" | Remove as strong claim | Replace with scoped Table 2 claim |
| Paper B | Abstract-only metadata could be mistaken for evidence | Keep out of evidence folder | Fetch PDF before creating paper/evidence cards |
| Paper A vs local pilot | Both support lower unsupported-claim rate but with different data sizes | Keep as separate paper and experiment evidence | Later synthesize only after more studies |

## Write Queue

| Priority | Action | Path | Acceptance Check |
|---|---|---|---|
| P1 | Update duplicate Paper A card with scoped evidence | `vault/papers/unknown-paper-a.md` | DOI present; old universal claim removed |
| P1 | Create Paper A evidence card | `vault/evidence/unsupported-claim-rate-drop-paper-a.md` | Table 2 and 12-paper limitation included |
| P1 | Create local pilot experiment card | `vault/experiments/2026-06-20-pilot-evidence-constrained-review.md` | command, seed 7, config, output path included |
| P2 | Update project index | `vault/indexes/evidence-grounded-literature-review.md` | Links paper/evidence/experiment/review queue |
| P2 | Create Paper B review item | `vault/review-queue/paper-b.md` | Marked abstract-only and PDF-needed |

## Do Not Ingest

| Source | Reason |
|---|---|
| Paper A old universal claim | Unsupported, lacks evidence location, conflicts with 12-paper limitation |
| Paper B abstract claim as evidence | Abstract-only and no full text or result table |

## Next Review

1. Confirm Paper A title/year to replace `unknown-paper-a.md` with the final slug.
2. Fetch Paper B PDF before creating any evidence card.
3. After adding two more full papers, synthesize whether unsupported-claim reduction generalizes beyond pilot settings.

## Acceptance Result

| Criterion | Result |
|---|---|
| Produces source audit, note plan, claim registry, dedupe/conflict log, write queue, and do-not-ingest queue | Pass |
| Does not ingest Paper B abstract as strong evidence | Pass |
| Detects duplicate Paper A note by DOI | Pass |
| Flags unsupported universal claim | Pass |
| Separates paper evidence from local experiment evidence | Pass |
| Uses target vault path conventions | Pass |
