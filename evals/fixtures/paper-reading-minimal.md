# Fixture: Paper Reading Minimal

## User Request

使用 `literature-evidence-reader` 阅读下面的论文摘录。研究问题：方法 X 是否能在低资源分类任务中提升泛化？

## Paper Excerpt

Title: Method X for Low-Resource Classification

Abstract: We propose Method X, a regularization strategy for low-resource classification.

Methods, Section 3: We train a baseline Transformer and a Transformer with Method X on three datasets. Each dataset has 500 training examples and 2,000 test examples. We use accuracy and macro-F1 as metrics. Hyperparameters are listed in Appendix A.

Table 1: Baseline macro-F1 is 61.2, 58.7, and 64.1. Method X macro-F1 is 64.9, 60.1, and 66.0 across the same datasets.

Figure 2: Method X improves validation stability in Dataset A but has overlapping confidence intervals with baseline in Dataset B.

Limitations, Section 6: We did not test multilingual data. We also did not evaluate models larger than 1B parameters.

Supplement: Appendix A includes learning rate, batch size, random seeds, and early stopping rules.

## Expected Evaluation Focus

- The output should not rely only on the abstract.
- Evidence cards should cite Section 3, Table 1, Figure 2, Section 6, and Appendix A.
- The conclusion should be cautious for Dataset B because confidence intervals overlap.
- The variable table should include training size, dataset, method, metric, and model size.
