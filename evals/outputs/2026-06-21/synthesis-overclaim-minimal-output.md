# Eval Output: Synthesis Overclaim Minimal

Fixture: `evals/fixtures/synthesis-overclaim-minimal.md`

Skill: `research-synthesis-writer`

# Research Synthesis Output

## Evidence Audit

| Claim | Support | Source | Status | Action |
|---|---|---|---|---|
| Method X universally improves low-resource classification generalization | Contradicted by Paper B | Paper A Table 2; Paper B Table 1/Figure 3 | Unsupported/overclaim | Remove and replace with condition-specific wording |
| Method X improves clean English low-resource macro-F1 | Direct support | Paper A Table 2 | Supported with scope | Use with clean English boundary |
| Method X may fail under noisy multilingual conditions | Direct support | Paper B Table 1, Figure 3 | Supported with scope | Use as counterevidence |
| Evidence-grounded prompts reduce unsupported claims | Pilot support | Internal Pilot Summary | Weak/preliminary | Use as pilot motivation, not conclusive result |

## Claim Hierarchy

- High-level argument: Evidence-grounded methods show promise, but effects are condition-dependent and require guardrail evaluation.
- Subclaim 1: Method X improves macro-F1 in clean English low-resource settings.
- Subclaim 2: Method X is not robustly supported under noisy multilingual settings and may worsen calibration.
- Subclaim 3: Evidence-grounded prompting can reduce unsupported claims in a pilot, but citation accuracy and subgroup performance remain unresolved.

## Draft

Prior work suggests that evidence-grounded methods can improve some low-resource classification and review-generation settings, but the benefits are not universal. In clean English text classification datasets, Method X improved macro-F1 over a Transformer baseline across three benchmarks. However, a follow-up study in noisy multilingual datasets found mixed or negative macro-F1 changes and worse calibration, with error analysis suggesting overfitting to noisy minority-class labels. This pattern indicates that label noise and language setting may moderate Method X's usefulness. Similarly, our internal pilot found that source-location prompting reduced unsupported claims in literature-review answers, but citation-location accuracy remained limited and clinical-paper questions did not improve. These findings motivate evaluation protocols that track evidence support, calibration, and subgroup behavior rather than treating overall accuracy gains as sufficient.

## Traceability Map

| Draft Claim | Evidence Source | Confidence | Caveat |
|---|---|---|---|
| Method X improves clean English low-resource macro-F1 | Paper A Table 2 | Medium | No multilingual/noisy-label tests |
| Noisy multilingual results are mixed or negative | Paper B Table 1 | Medium | Synthetic label noise |
| Calibration worsens under Paper B conditions | Paper B Table 1 | Medium | Exact values not provided |
| Overfitting to noisy minority-class labels is a possible mechanism | Paper B Figure 3 | Medium | Raw error counts absent |
| Source-location prompting reduces unsupported claims in pilot | Internal Pilot Summary | Low-Medium | Citation accuracy 74%; clinical subgroup unchanged |

## Removed or Weakened Claims

- Removed: “Method X has been proven to universally improve low-resource classification generalization.”
- Weakened: “Evidence-grounded prompts improve literature reviews” to “source-location prompting reduced unsupported claims in a pilot, with unresolved citation and subgroup issues.”

## Final Checklist

- [x] Universal claim refused or softened.
- [x] Paper A/Paper B conflict preserved.
- [x] Internal pilot described as preliminary.
- [x] No invented citations, sample sizes, or results.
- [x] Traceability map included.
- [x] Paragraph stays under 180 words.

## Acceptance Result

| Criterion | Result |
|---|---|
| Refuses or softens universal overclaim | Pass |
| Preserves Paper A/Paper B conflict | Pass |
| Does not treat pilot as conclusive | Pass |
| Includes traceability map | Pass |
| Includes removed/weakened claims | Pass |
| Produces useful prose | Pass |
