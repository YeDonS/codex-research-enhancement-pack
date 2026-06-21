---
name: literature-landscape-researcher
description: Use when the user wants a reproducible literature search, scoping review, research landscape, systematic search protocol, paper screening, evidence map, or defensible research-gap analysis across multiple sources.
---

# Literature Landscape Researcher

## Trigger

Use this skill when the user asks to search a research area, find related work, map a field, identify gaps, prepare a scoping/systematic review, compare many papers, or build a reproducible literature screening pipeline.

## Inputs

- Research question, population/context, intervention/exposure, outcome, method, or other scope dimensions.
- Date range, languages, publication types, venues/databases, and access constraints.
- Seed papers, known terminology, prior queries, existing bibliography, and exclusion rules.
- Desired depth: rapid landscape, scoping review, systematic search, or update search.
- Target output format and downstream task such as proposal, related work, evidence matrix, or paper-reading queue.

## Procedure

1. Write the search protocol before searching:
   - Define scope dimensions, inclusion/exclusion criteria, date/language limits, source types, and stopping rule.
   - Reject requests to search only for evidence supporting a preferred conclusion.
2. Build query families:
   - Expand concepts into synonyms, spelling variants, acronyms, controlled vocabulary, and negative terms.
   - Record exact query strings and version changes.
3. Search multiple source types:
   - Use appropriate scholarly databases, publisher indexes, preprint servers, citation graphs, and authoritative repositories.
   - Record database, date, query, filters, hit count, and export path.
4. Deduplicate:
   - Match DOI first, then normalized title/year/authors.
   - Keep a dedupe log instead of silently deleting records.
5. Screen in stages:
   - Title/abstract screen, then full-text screen.
   - Record include/exclude/maybe decisions and explicit exclusion reasons.
6. Map evidence:
   - Group papers by question, method, dataset/population, result direction, limitation, and evidence strength.
   - Preserve negative/null results and contradictory studies.
7. Test gap claims:
   - Distinguish “not found by this search” from “does not exist.”
   - Require at least one query revision or citation-snowball pass before claiming a gap.
8. Handoff to deep reading:
   - Select a small full-text queue for `literature-evidence-reader` with reasons and unresolved questions.

## Output Format

```markdown
# Literature Landscape Report

## Search Protocol
| Field | Value |

## Query Log
| Source | Date | Query | Filters | Hits | Export |

## Screening Ledger
| Record | Stage | Decision | Reason | Evidence Status |

## Dedupe Log
| Records | Match Key | Decision |

## Evidence Landscape
| Theme | Papers | Methods/Data | Direction | Strength | Conflict |

## Gap Claims
| Candidate Gap | Search Evidence | Confidence | Required Follow-up |

## Full-Text Reading Queue
| Priority | Paper | Reason | Question |

## Search Limitations

## Next Search Action
```

## Quality Standards

- Exact queries, databases, dates, filters, and hit counts are recorded.
- Inclusion/exclusion criteria are defined before screening results are interpreted.
- Negative, null, and contradictory evidence is retained.
- Duplicate handling is traceable by DOI or normalized bibliographic fields.
- Gap claims are calibrated to search coverage and never inferred from one narrow query.
- Every included record has a DOI, stable URL, repository ID, or local source path when available.
- The final reading queue is small enough for full-text evidence extraction.

## Failure Repair

- If results are too broad, narrow one scope dimension and log the query revision.
- If results are too sparse, expand synonyms, databases, citation chaining, or date range before claiming a gap.
- If only abstracts are available, mark evidence as abstract-only and keep it out of strong synthesis.
- If one database dominates, add a complementary source type or state the coverage bias.
- If screening becomes inconsistent, restate criteria and recheck a sample before continuing.
- If the user requests confirmation-only evidence, include disconfirming searches and explain the bias risk.
