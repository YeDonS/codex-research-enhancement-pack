# Fixture: Knowledge Curation Minimal

## Skill Under Test

`research-knowledge-curator`

## Scenario

The user asks:

> Put these materials into my Obsidian research vault and make them useful for the "evidence-grounded literature review" project.

Available materials:

- `papers/a.pdf`
  - Full text available.
  - DOI: `10.1234/a`
  - Table 2 reports unsupported-claim rate drops from 18% to 11%.
  - Limitation section says only 12 papers were tested.
- `notes/paper_a_old.md`
  - Existing note for the same DOI.
  - Says "method reduces hallucinations across all literature reviews."
  - Has no page, table, or output links.
- `zotero_export/paper_b.json`
  - Metadata and abstract only.
  - No PDF.
  - Abstract claims "retrieval improves factuality."
- `runs/pilot_2026-06-20/metrics.json`
  - Local pilot: 5 PDFs, unsupported-claim rate 14% baseline vs 10% evidence-constrained.
  - Seed: 7.
  - Command: `python eval_review.py --config configs/pilot.yaml --seed 7`.
- Target vault conventions:
  - Paper cards: `vault/papers/{year}-{slug}.md`
  - Evidence cards: `vault/evidence/{claim-slug}.md`
  - Experiment cards: `vault/experiments/{date}-{slug}.md`
  - Index: `vault/indexes/evidence-grounded-literature-review.md`

## Expected Behavior

The output must not dump all material as summaries. It should:

- Merge or update the old Paper A note rather than creating an unlinked duplicate.
- Downgrade Paper A's old universal claim because it lacks evidence and contradicts the 12-paper limitation.
- Treat Paper B as abstract-only and put it in a review queue, not strong evidence.
- Create separate paper, evidence, experiment, and index note plans.
- Link the local pilot metric to command, seed, config, and output path.
- Preserve uncertainty and avoid a universal conclusion.

## Acceptance Criteria

- Produces source audit, note plan, claim registry, dedupe/conflict log, write queue, and do-not-ingest/review queue.
- Does not ingest abstract-only Paper B as strong evidence.
- Detects duplicate Paper A note by DOI.
- Rewrites or flags the unsupported universal claim.
- Separates paper evidence from local experiment evidence.
- Includes target paths using the given vault conventions.
