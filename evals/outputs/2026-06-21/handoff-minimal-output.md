# Eval Output: Handoff Minimal

Fixture: `evals/fixtures/handoff-minimal.md`

Skill: `research-handoff-review`

# Handoff

## Objective

Build a literature-review evidence matrix that can support later related-work writing without relying on abstract-only claims.

## Scope

Changed:

- `notes/evidence_matrix.md`
- `notes/paper_cards/paper_a.md`
- `notes/paper_cards/paper_b.md`

Intentionally not changed:

- No related-work prose should be finalized yet.
- No evidence cards should be promoted for the 3 abstract-only papers.

Out of scope:

- Full systematic review.
- Any claims requiring papers not yet downloaded.

## Evidence

Commands:

- `python scripts/extract_pdf_text.py papers/a.pdf`

Outputs:

- `notes/evidence_matrix.md`
- `notes/paper_cards/paper_a.md`
- `notes/paper_cards/paper_b.md`

Source material:

- 5 paper abstracts.
- 2 full papers.

## Open Items

- Download or otherwise obtain full text for 3 abstract-only papers.
- Add page or figure location for Figure 3 claim in `notes/paper_cards/paper_b.md`.
- Normalize dataset names across the two paper cards.

## Review Notes

Findings:

1. `notes/paper_cards/paper_b.md` contains a Figure 3 claim without page or figure-location evidence, so it should not be treated as strong evidence.
2. The current evidence matrix risks abstract-only synthesis because 3 of 5 papers lack full text.
3. Dataset naming inconsistency will make cross-paper grouping unreliable.

Residual risk:

- If prose writing starts before full-text repair, the related work may overstate weak evidence.
- If dataset names are normalized manually without a mapping note, later audits may lose provenance.

## Next Step

Before writing related-work prose, retrieve the 3 missing full texts or mark them as abstract-only candidates, repair the Figure 3 location in `paper_b.md`, and add a dataset-name normalization note to `notes/evidence_matrix.md`.

## Acceptance Result

| Criterion | Result |
|---|---|
| New session can resume from handoff | Pass |
| Abstract-only evidence flagged | Pass |
| Missing Figure 3 location flagged | Pass |
| Next step prioritizes evidence repair | Pass |
