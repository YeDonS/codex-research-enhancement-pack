# Fixture: Research Question Minimal

## User Request

使用 `research-question-council` 审查这个方向：证据引用约束能否降低 LLM 文献综述中的事实错误。

## Materials

- 已有材料：30 篇机器学习论文 PDF；10 个综述写作问题；一个小型人工标注表，包含 50 条模型输出中的事实错误。
- 约束：两周内完成初步实验；没有预算做大规模人工标注；只能使用本地已有 PDF。
- 初步想法：比较“普通提示词”和“要求每个结论附来源定位”的提示词。

## Expected Evaluation Focus

- Candidates should name measurable outcomes, such as unsupported claim rate or citation-location accuracy.
- The council should flag the small annotation set as a risk.
- At least one candidate should be rejected for being too broad or too expensive.
- The next smallest action should be a pilot with a small subset, not a full benchmark.
