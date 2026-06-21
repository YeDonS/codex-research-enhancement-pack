# Eval Output: Paper Reading Minimal

Fixture: `evals/fixtures/paper-reading-minimal.md`

Skill: `literature-evidence-reader`

# Paper Reading Pack

## Preflight

- Full text: Partial fixture text only. It includes Abstract, Methods Section 3, Table 1, Figure 2, Limitations Section 6, and Supplement Appendix A summary.
- Figures/tables: Table 1 and Figure 2 are available as textual descriptions.
- Supplement: Appendix A is available as a summary of included items, but exact hyperparameter values are not provided.
- Reading goal: Determine whether Method X improves generalization in low-resource classification.
- Stop condition: Do not claim real-paper completeness because this is an excerpt, not a full PDF.

## One-Sentence Use

Use this paper as cautious evidence that Method X may improve macro-F1 in low-resource classification, with weaker support for Dataset B and no support for multilingual or >1B parameter settings.

## Evidence Cards

| Claim | Evidence Location | Method/Data | Result | Limitation | Confidence |
|---|---|---|---|---|---|
| Method X improves macro-F1 across three low-resource datasets | Table 1 | Baseline Transformer vs Transformer + Method X; 500 train and 2,000 test examples per dataset | Macro-F1 improves from 61.2 to 64.9, 58.7 to 60.1, and 64.1 to 66.0 | No statistical test or confidence interval values shown in the table excerpt | Medium |
| Dataset B improvement should be treated cautiously | Figure 2 | Validation stability comparison for Dataset B | Confidence intervals overlap with baseline | Figure is only described textually; raw intervals are missing | Medium |
| Experimental setting is low-resource classification | Methods Section 3 | Three datasets, 500 training examples each | Study design matches low-resource classification | Dataset domains and class counts are missing | High |
| Reproduction requires Appendix A | Supplement Appendix A | Learning rate, batch size, random seeds, early stopping rules | Reproduction metadata exists in supplement | Exact values are not in the fixture excerpt | Medium |
| Claims should not be generalized to multilingual data or large models | Limitations Section 6 | No multilingual evaluation and no models larger than 1B parameters | External validity is bounded | Unknown whether failure would occur outside tested setting | High |

## Method Cards

| Method Step | Inputs | Assumptions | Parameters | Repro Notes |
|---|---|---|---|---|
| Train baseline Transformer | Three low-resource datasets with 500 train and 2,000 test examples each | Dataset splits are fixed and comparable | Hyperparameters in Appendix A | Need exact learning rate, batch size, seed, early stopping from supplement |
| Train Transformer with Method X | Same datasets and splits as baseline | Method X is the only intended treatment difference | Hyperparameters in Appendix A plus Method X settings | Need Method X implementation details, not present in excerpt |
| Evaluate classification performance | Test sets for all three datasets | Macro-F1 and accuracy match the research question | Metrics: accuracy and macro-F1 | Fixture gives only macro-F1 values; accuracy should be retrieved from full paper |
| Assess validation stability | Validation curves or intervals from Figure 2 | Overlapping intervals weaken robustness claims | Confidence interval method not provided | Need numeric intervals before claiming Dataset B stability |
| Bound external validity | Limitations Section 6 | Missing tests define non-claim areas | Multilingual and >1B model settings excluded | Do not cite this paper as evidence for multilingual or large-model generalization |

## Variable Table

| Variable | Definition | Measurement | Role | Caveats |
|---|---|---|---|---|
| Method | Baseline Transformer vs Transformer + Method X | Training condition | Independent variable | Method X details absent from fixture |
| Dataset | Three low-resource classification datasets | Dataset identity | Context/moderator | Domain, label count, and sampling unclear |
| Training size | 500 examples per dataset | Count | Resource constraint | Class balance unknown |
| Test size | 2,000 examples per dataset | Count | Evaluation basis | Test construction unknown |
| Macro-F1 | Main reported metric in Table 1 | Score per dataset | Outcome | Confidence intervals absent in table |
| Accuracy | Mentioned metric in Methods | Score per dataset | Outcome | Values not given in fixture |
| Model size | Up to 1B parameters | Parameter scale | Scope boundary | Larger models not evaluated |
| Language setting | Non-multilingual setting | Dataset language coverage | Scope boundary | Multilingual generalization unsupported |

## Reusable Notes

Evidence worth storing:

- Table 1 macro-F1 improvements as preliminary evidence for Method X in low-resource classification.
- Figure 2 caution for Dataset B due to overlapping confidence intervals.
- Section 6 limitation that multilingual data and >1B models were not tested.

Do not store:

- A broad claim that Method X “improves generalization” without scope.
- Any claim about multilingual, large-model, or production settings.
- Exact hyperparameter values, because they are not included in the fixture excerpt.

## Open Questions

- What are the exact Method X mechanics and parameters?
- What are the Table 1 accuracy results?
- Are improvements statistically significant?
- What are the numeric confidence intervals in Figure 2?
- What are the dataset domains and class balances?

## Next Step

Retrieve the full paper or supplement details, then repair the method card with exact hyperparameters and Method X implementation details before using this as reproduction evidence.

## Acceptance Result

| Criterion | Result |
|---|---|
| Preflight first | Pass |
| Evidence cards present | Pass |
| Method cards present | Pass |
| Variable table present | Pass |
| Key claims cite section/table/figure/supplement | Pass |
| Not abstract-only | Pass |
