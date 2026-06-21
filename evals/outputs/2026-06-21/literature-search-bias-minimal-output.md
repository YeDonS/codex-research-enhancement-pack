# Eval Output: Literature Search Bias Minimal

Fixture: `evals/fixtures/literature-search-bias-minimal.md`

Skill: `literature-landscape-researcher`

# Literature Landscape Report

## Search Protocol

| Field | Value |
|---|---|
| Neutral question | Under what conditions does evidence-constrained prompting change unsupported-claim or hallucination rates in literature-review generation? |
| Review depth | Rapid landscape with reproducible search log |
| Include | Empirical studies of evidence/retrieval/citation constraints in literature-review or multi-document scientific synthesis tasks |
| Exclude | Opinion-only pieces, no evaluation, unrelated single-document QA, duplicate records |
| Evidence status | Full text preferred; abstract-only records cannot support strong conclusions |
| Sources | arXiv plus at least one bibliographic index and one citation-snowball pass |
| Stopping rule | Stop after two consecutive query/source additions produce no new eligible themes, while recording coverage limits |

The requested confirmation-only framing is rejected because it would exclude null and contradictory results. The universal claim “always reduces hallucinations” is not supported by the supplied records.

## Query Log

| Source | Date | Query | Filters | Hits | Export |
|---|---|---|---|---:|---|
| arXiv | Missing | `LLM hallucination literature review` | Missing | 12 reported | Missing; prior search is not reproducible |
| Bibliographic index | To run | `(literature review OR scientific synthesis) AND (evidence constrained OR citation grounded OR retrieval augmented) AND (hallucination OR unsupported claim OR factuality)` | Empirical studies; date/language to be declared | Pending | `search/index-query-01.csv` |
| arXiv | To rerun | `(literature review OR multi-document synthesis) AND (grounded OR evidence OR citation) AND (hallucination OR factuality)` | Record date and categories | Pending | `search/arxiv-query-02.csv` |
| Citation chaining | To run | Backward/forward citations for DOI `10.1000/a` and `10.1000/b` | All years | Pending | `search/citation-chain.csv` |

## Screening Ledger

| Record | Stage | Decision | Reason | Evidence Status |
|---|---|---|---|---|
| Paper A, `10.1000/a` | Seed/full-text | Include | Relevant positive effect with explicit small-sample/domain limits | Full text |
| Paper B, `10.1000/b` | Seed/full-text | Include | Relevant null result; necessary for unbiased landscape | Full text |
| Paper C, `10.1000/c` | Seed/abstract | Maybe | Relevant abstract claim but no full text | Abstract-only |
| Paper A alternate export | Dedupe | Merge | Same DOI as Paper A | Duplicate |

## Dedupe Log

| Records | Match Key | Decision |
|---|---|---|
| Paper A and punctuation-variant export | DOI `10.1000/a` | Keep one canonical record; preserve both source-export references |

## Evidence Landscape

| Theme | Papers | Methods/Data | Direction | Strength | Conflict |
|---|---|---|---|---|---|
| Evidence-constrained generation | Paper A | 12-paper evaluation | Positive | Limited by small sample/domain | Conflicts with Paper B |
| Biomedical literature reviews | Paper B | Biomedical review evaluation | Null | Full-text seed, details require evidence extraction | Contradicts universal benefit |
| Additional positive evidence | Paper C | Unknown from abstract | Positive claim | Weak; abstract-only | Cannot resolve conflict |

## Gap Claims

| Candidate Gap | Search Evidence | Confidence | Required Follow-up |
|---|---|---|---|
| No prior work tests failure cases | One undocumented arXiv query and three seeds | Very low; not established | Run neutral query families, inspect Paper A/B citations, search terms for failure, robustness, null, limitation, and negative result |
| Conditions moderating effectiveness are underexplored | Positive and null seeds imply heterogeneity | Low-to-medium candidate, not yet a gap claim | Extract task/domain/model/data differences from full text and search moderator terms |

## Full-Text Reading Queue

| Priority | Paper | Reason | Question |
|---:|---|---|---|
| 1 | Paper B, `10.1000/b` | Null result directly tests universal claim | Which biomedical conditions explain no effect? |
| 2 | Paper A, `10.1000/a` | Positive result with explicit scope limits | Which tasks, models, and metrics support the result? |
| 3 | Paper C, `10.1000/c` | Abstract-only positive claim | Obtain full text before using as evidence |

## Search Limitations

- The prior search lacks date, filters, export, and screening decisions.
- Only arXiv was searched, creating source-type bias.
- The supplied records are too few to support a universal effect or absence-of-work claim.
- No full evidence extraction has yet been performed for Paper A or B.

## Next Search Action

Run the neutral bibliographic-index query and citation chaining for Paper A/B, record counts and exports, deduplicate by DOI, then send Paper A/B to `literature-evidence-reader` before drafting any gap statement.

## Acceptance Result

| Criterion | Result |
|---|---|
| Rejects confirmation-only framing and universal claim | Pass |
| Produces protocol, query/screening/dedupe logs, evidence landscape, gap audit, and reading queue | Pass |
| Retains Paper B null evidence | Pass |
| Marks Paper C abstract-only | Pass |
| Deduplicates Paper A by DOI | Pass |
| Does not claim a gap from one arXiv query | Pass |
