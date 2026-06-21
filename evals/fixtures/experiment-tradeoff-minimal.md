# Fixture: Experiment Tradeoff Minimal

## User Request

使用 `experiment-design-planner` 设计并审查一个实验。假设：证据引用约束可以降低 LLM 文献综述中的事实错误。

## Materials

- Dataset: 10 literature-review questions over 30 local PDFs.
- Baseline prompt: asks the model to answer in prose.
- Treatment prompt: requires every factual claim to include a source location.
- Existing pilot result:
  - Unsupported claim rate improves from 28% to 16%.
  - Citation-location accuracy is 74%.
  - Average answer length increases by 65%.
  - Calibration self-rating worsens: model reports high confidence on 40% of unsupported claims.
  - Subgroup issue: for methods papers, unsupported claim rate improves; for clinical papers, it stays at 27%.
- Constraint: only 6 hours of annotation time remains.

## Expected Evaluation Focus

- The output must not declare the treatment successful based only on unsupported claim rate.
- It should define primary and guardrail metrics before scaling.
- It should treat calibration and clinical-paper subgroup performance as blocking or revision conditions.
- It should propose a smallest follow-up that fits the 6-hour annotation budget.
- It should include reproducibility fields: PDF version, prompt version, model version, seeds or sampling settings, output path, and annotation rubric.
