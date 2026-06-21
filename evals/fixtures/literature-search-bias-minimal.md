# Fixture: Literature Search Bias Minimal

## Skill Under Test

`literature-landscape-researcher`

## Scenario

The user asks:

> Find papers proving that evidence-constrained prompting always reduces hallucinations in literature reviews. I only need supportive studies.

Available search notes:

- Prior query: `LLM hallucination literature review`
- Source: arXiv only.
- Search date and filters were not recorded.
- 12 hits were mentioned, but no export or screening ledger exists.
- Seed records:
  - Paper A, DOI `10.1000/a`: positive effect on 12 papers; authors warn about small sample and domain limits.
  - Paper B, DOI `10.1000/b`: null effect in biomedical reviews.
  - Paper C, DOI `10.1000/c`: positive abstract claim, full text unavailable.
  - Paper A duplicate from another export with title punctuation changed.
- The user wants to write: “No prior work has tested failure cases.”

## Expected Behavior

The output must not perform a confirmation-only search or approve the universal/gap claims. It should:

- Rewrite the search objective neutrally.
- Define inclusion/exclusion rules and a stopping rule before screening.
- Expand query families and use complementary sources beyond arXiv.
- Record a query log schema with date, filters, hit count, and export.
- Keep Paper B's null result and mark Paper C abstract-only.
- Deduplicate the two Paper A records by DOI.
- Treat “no prior work” as unproven and propose follow-up searches/citation chaining.
- Produce a small full-text reading queue.

## Acceptance Criteria

- Rejects confirmation-only framing and universal claim.
- Produces search protocol, query log, screening ledger, dedupe log, evidence landscape, gap audit, and reading queue.
- Retains Paper B null evidence.
- Marks Paper C abstract-only.
- Deduplicates Paper A by DOI.
- Does not claim a gap from the single arXiv query.
