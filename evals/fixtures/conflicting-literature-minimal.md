# Fixture: Conflicting Literature Minimal

## User Request

使用 `literature-evidence-reader` 做跨文献整合。研究问题：Method X 是否能提升低资源分类任务的泛化？

## Paper A Excerpt

Title: Method X Improves Low-Resource Classification

Methods: Paper A evaluates Method X on three English text classification datasets. Each dataset has 500 training examples and 2,000 test examples. The baseline is a Transformer without Method X. Metrics are macro-F1 and accuracy.

Table 2: Method X improves macro-F1 over baseline by +3.7, +1.4, and +1.9 points across the three datasets.

Limitations: Paper A does not evaluate multilingual datasets and does not test noisy labels.

## Paper B Excerpt

Title: Method X Fails Under Label Noise

Methods: Paper B evaluates Method X on two low-resource multilingual classification datasets with 20% synthetic label noise. Each dataset has 400 training examples and 2,000 test examples. The baseline is the same Transformer architecture without Method X. Metrics are macro-F1 and calibration error.

Table 1: Method X changes macro-F1 by -2.2 and +0.3 points compared with baseline. Calibration error worsens in both datasets.

Figure 3: Error analysis shows Method X overfits noisy minority-class labels.

Limitations: Paper B does not test clean-label English-only datasets.

## Expected Evaluation Focus

- The output must not collapse Paper A and Paper B into a single “Method X works” conclusion.
- It should preserve the conflict by condition: clean English datasets versus noisy multilingual datasets.
- Evidence cards should cite Paper A Table 2 and limitations, Paper B Table 1, Figure 3, and limitations.
- The synthesis should propose a moderator hypothesis: label noise, multilingual setting, or minority-class noise may explain the conflict.
- The next step should be a discriminating experiment, not more generic reading.
