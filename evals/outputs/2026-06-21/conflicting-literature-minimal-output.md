# Eval Output: Conflicting Literature Minimal

Fixture: `evals/fixtures/conflicting-literature-minimal.md`

Skill: `literature-evidence-reader`

# Cross-Paper Evidence Pack

## Preflight

- Full text: Fixture excerpts only; both papers provide Methods, result table references, and limitations.
- Figures/tables: Paper A Table 2, Paper B Table 1, and Paper B Figure 3 are available as textual descriptions.
- Supplement: Not available in fixture.
- Reading goal: Decide whether Method X improves low-resource classification generalization across conflicting studies.
- Stop condition: Do not produce a universal conclusion because the two studies differ by language setting and label noise.

## Conflict-Preserving Synthesis

Method X appears beneficial in Paper A's clean English low-resource datasets, but Paper B shows failure or negligible benefit under noisy multilingual low-resource datasets. The current evidence supports a moderator hypothesis, not a global claim: Method X may help under clean labels and English-only settings, while label noise, multilingual data, or noisy minority classes may erase or reverse the benefit.

## Evidence Cards

| Paper | Claim | Evidence Location | Method/Data | Result | Limitation | Confidence |
|---|---|---|---|---|---|---|
| Paper A | Method X improves macro-F1 on clean English low-resource classification | Paper A Table 2 | 3 English datasets, 500 train / 2,000 test each; Transformer baseline | +3.7, +1.4, +1.9 macro-F1 | No multilingual data; no noisy labels | Medium |
| Paper A | Paper A cannot support noisy or multilingual claims | Paper A Limitations | Scope statement | No multilingual or noisy-label evaluation | Boundary is explicit | High |
| Paper B | Method X does not reliably improve macro-F1 under noisy multilingual conditions | Paper B Table 1 | 2 multilingual datasets, 400 train / 2,000 test each; 20% synthetic label noise | -2.2 and +0.3 macro-F1 | Synthetic noise may not match real noise | Medium |
| Paper B | Method X worsens calibration under Paper B conditions | Paper B Table 1 | Calibration error evaluation | Calibration error worsens in both datasets | Exact calibration values absent | Medium |
| Paper B | Minority-class noisy labels may explain failure | Paper B Figure 3 | Error analysis | Method X overfits noisy minority-class labels | Figure description lacks raw counts | Medium |
| Paper B | Paper B cannot refute clean English benefits | Paper B Limitations | Scope statement | Clean-label English-only datasets not tested | Boundary is explicit | High |

## Method Cards

| Method Step | Paper A | Paper B | Conflict-Relevant Difference |
|---|---|---|---|
| Dataset language | English text classification | Multilingual classification | Language setting may moderate effect |
| Training size | 500 examples per dataset | 400 examples per dataset | Similar low-resource regime, not identical |
| Label quality | No noisy-label condition reported | 20% synthetic label noise | Label noise is a major moderator candidate |
| Baseline | Transformer without Method X | Same Transformer architecture without Method X | Baseline broadly comparable |
| Metrics | Macro-F1 and accuracy | Macro-F1 and calibration error | Calibration degradation appears only in Paper B |
| Error analysis | Not reported in fixture | Figure 3 minority-class noise overfitting | Mechanistic clue exists only for failure case |

## Variable Table

| Variable | Values | Role | Evidence | Caveats |
|---|---|---|---|---|
| Method X | absent vs present | Treatment | Paper A and Paper B methods | Implementation equivalence assumed, not proven |
| Language setting | English vs multilingual | Moderator | Paper A Methods; Paper B Methods | Language and dataset differences are confounded |
| Label noise | clean/unspecified vs 20% synthetic noise | Moderator | Paper B Methods; Paper A Limitations | Paper A may still contain natural noise but did not test it |
| Training size | 500 vs 400 examples | Context | Methods sections | Slightly different sample size |
| Macro-F1 | changes in both papers | Outcome | Paper A Table 2; Paper B Table 1 | Statistical significance not provided |
| Calibration error | worsens in Paper B | Secondary outcome | Paper B Table 1 | Paper A does not report calibration |
| Minority-class noisy labels | overfit in Paper B | Mechanism candidate | Paper B Figure 3 | Raw counts absent |

## Conflict Matrix

| Condition | Paper A Evidence | Paper B Evidence | Synthesis |
|---|---|---|---|
| Clean English low-resource | Positive macro-F1 gains | Not tested | Method X may help; needs replication |
| Noisy multilingual low-resource | Not tested | Macro-F1 mixed/negative; calibration worse | Method X may fail or harm |
| Label noise | Not tested | 20% synthetic noise plus minority-class overfitting | Strong moderator candidate |
| Calibration | Not reported | Worse in both datasets | Benefit claims should include calibration checks |

## Moderator Hypotheses

1. Label-noise hypothesis: Method X amplifies noisy minority-class signals, improving clean-label macro-F1 but harming noisy-label generalization.
2. Language-setting hypothesis: Method X is tuned to English text features and does not transfer to multilingual datasets.
3. Calibration tradeoff hypothesis: Even when macro-F1 is neutral, Method X may worsen probability calibration.

## Do Not Store As

- “Method X improves low-resource classification.”
- “Method X fails in low-resource classification.”
- “The literature is mixed” without naming the moderators.

## Store As

Method X has condition-dependent evidence: Paper A supports macro-F1 gains in clean English low-resource datasets, while Paper B reports mixed/negative macro-F1 and worse calibration under noisy multilingual conditions. Label noise, multilingual setting, and minority-class noise are candidate moderators.

## Next Discriminating Experiment

Run a 2x2 experiment on the same datasets and model implementation:

| Factor | Levels |
|---|---|
| Language setting | English, multilingual |
| Label noise | 0%, 20% |

Measure macro-F1, calibration error, and minority-class error rate. This directly tests whether label noise and language setting explain the Paper A/Paper B conflict.

## Acceptance Result

| Criterion | Result |
|---|---|
| Does not collapse conflict into a single conclusion | Pass |
| Preserves condition-specific evidence | Pass |
| Cites Paper A Table 2 and limitations | Pass |
| Cites Paper B Table 1, Figure 3, and limitations | Pass |
| Proposes moderator hypotheses | Pass |
| Next step is a discriminating experiment | Pass |
