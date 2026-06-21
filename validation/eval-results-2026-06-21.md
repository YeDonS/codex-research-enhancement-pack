# Eval Results：2026-06-21 Smoke Eval

说明：本文件记录同一会话内对 13 个最小/adversarial fixture 的 smoke eval。它证明 skill 输出形态和检查标准能跑通，但不等同于独立会话验证，也不等同于真实科研任务验证。每个 fixture 的完整输出已拆到 `evals/outputs/2026-06-21/`。

## 1. XHS Batch Minimal

Fixture：`evals/fixtures/xhs-batch-minimal.md`

对应 skill：`xhs-method-ingester`

完整输出：`evals/outputs/2026-06-21/xhs-batch-minimal-output.md`

### 提炼结果

| 输入 | 判定 | 可迁移方法 | 风险限制 | 转化产物 |
|---|---|---|---|---|
| Note A：论文阅读不要一口气全自动 | Keep | 单篇 preflight 后再证据卡/方法卡入库 | 不适合批量无监督跑；必须确认全文、图表、supplement | `literature-evidence-reader` 流程、文献精读 checklist |
| Note B：AI 科研效率提升 100 倍 | Drop | 无 | 只有效果宣称，没有步骤、输入、输出或验收 | 不转化 |
| Note C：跨天任务写 handoff | Keep | 每晚写改动、命令、结果、失败、下一步；补随机种子、数据版本、环境 | handoff 空泛会无法接续 | `research-handoff-review` 流程、handoff checklist |

### 验收

| 标准 | 结果 |
|---|---|
| 至少提炼 2 个方法 | Pass |
| 标出 1 个弱信号或 Drop | Pass |
| 输出 skill/workflow/checklist 三类产物草案 | Pass |
| 包含五栏进度行 | Pass |

## 2. Paper Reading Minimal

Fixture：`evals/fixtures/paper-reading-minimal.md`

对应 skill：`literature-evidence-reader`

完整输出：`evals/outputs/2026-06-21/paper-reading-minimal-output.md`

### Paper Reading Pack 摘要

Preflight：

- Full text：fixture 摘录覆盖 Abstract、Methods、Table 1、Figure 2、Limitations、Supplement，但不是完整 PDF。
- Figures/tables：Table 1 和 Figure 2 可读。
- Supplement：Appendix A 摘要可读。
- Reading goal：判断 Method X 是否在低资源分类任务中提升泛化。

Evidence cards：

| Claim | Evidence Location | Method/Data | Result | Limitation | Confidence |
|---|---|---|---|---|---|
| Method X 在 3 个低资源数据集上提升 macro-F1 | Table 1 | 3 datasets, 500 train / 2,000 test each | 61.2→64.9, 58.7→60.1, 64.1→66.0 | 只给汇总结果，缺显著性检验 | Medium |
| Dataset B 的提升不稳健 | Figure 2 | validation stability comparison | confidence intervals overlap with baseline | 只描述图，没有原始区间值 | Medium |
| 实验设置为低资源分类 | Methods Section 3 | Transformer baseline vs Method X | 500 training examples per dataset | 不知道任务领域和类别数 | High |
| 复现需要 Appendix A 超参 | Supplement Appendix A | LR, batch size, seeds, early stopping | 复现要素存在 | fixture 未给具体数值 | Medium |
| 泛化结论不能外推到多语言或大模型 | Limitations Section 6 | no multilingual, no >1B models | 外部有效性有限 | 作者未测试这些场景 | High |

Variable table：

| Variable | Definition | Measurement | Role | Caveats |
|---|---|---|---|---|
| Method | baseline Transformer vs Transformer + Method X | training condition | independent variable | Method X 细节缺失 |
| Dataset | 3 low-resource datasets | dataset identity | context/moderator | 领域未知 |
| Training size | 500 examples | count | resource constraint | 是否均衡未知 |
| Metric | accuracy, macro-F1 | evaluation metric | outcome | fixture 只给 macro-F1 |
| Model size | <= 1B tested | parameter scale | boundary | 大模型未验证 |

Conclusion：Method X 在 fixture 给出的 3 个数据集上 macro-F1 均提高，但 Dataset B 因置信区间重叠只能给谨慎结论；不能外推到多语言和大于 1B 参数模型。

### Method Cards 补充

完整输出已补充显式 Method Cards，覆盖 baseline 训练、Method X 训练、评估、稳定性检查和外部有效性边界。

### 验收

| 标准 | 结果 |
|---|---|
| 先做 preflight | Pass |
| 输出证据卡、方法卡、变量表 | Pass |
| 关键结论指向段落、表或图 | Pass |
| 不只写摘要 | Pass |

## 3. Research Question Minimal

Fixture：`evals/fixtures/research-question-minimal.md`

对应 skill：`research-question-council`

完整输出：`evals/outputs/2026-06-21/research-question-minimal-output.md`

### Council 摘要

Decision：不要直接做完整 benchmark；先做小样本 pilot，验证“证据引用约束”是否降低 unsupported claim rate。

Role findings：

| Role | Strongest Point | Concrete Risk | Repair |
|---|---|---|---|
| Opponent | 50 条错误标注太小，容易得出偶然结论 | 样本不足导致效果不稳 | 先做 pilot，只报告探索性结果 |
| First-principles | 核心变量是“结论是否被 PDF 中可定位证据支持” | 普通事实错误率定义可能混乱 | 拆成 unsupported claim rate 和 citation-location accuracy |
| Expander | 可把任务做成综述生成质量控制方法 | 贡献可能只是 prompt trick | 加入错误类型 taxonomy |
| Outsider | 本地 30 篇 PDF 限制了外部泛化 | 数据来源窄 | 把结论限定为本地论文集 |
| Executor | 最小动作是 5 篇论文、2 个 prompt、10 个问题 | 全量跑会拖慢 | 先完成 20 个输出的人工复核 |

Candidate questions：

| Question | Verdict | Reason |
|---|---|---|
| 证据引用约束是否降低 unsupported claim rate？ | Keep | 可测量，和现有标注表匹配 |
| 证据引用约束是否提升综述整体质量？ | Reject | 过宽，质量维度和人工标注成本过高 |
| 引用定位准确率能否预测事实错误率？ | Keep as secondary | 可作为机制分析，但需要额外标注 |

Next smallest action：选 5 篇 PDF 和 3 个综述问题，生成普通 prompt 与引用约束 prompt 的输出各 15 条，人工标注 unsupported claim 和 citation-location accuracy。

### 验收

| 标准 | 结果 |
|---|---|
| 五角色均给出具体风险 | Pass |
| 生成 3 个候选问题 | Pass |
| 至少淘汰 1 个 | Pass |
| 下一步是 pilot 而非全量 benchmark | Pass |

## 4. Handoff Minimal

Fixture：`evals/fixtures/handoff-minimal.md`

对应 skill：`research-handoff-review`

完整输出：`evals/outputs/2026-06-21/handoff-minimal-output.md`

### Handoff 摘要

Objective：建立文献综述证据矩阵。

Changed：

- `notes/evidence_matrix.md`
- `notes/paper_cards/paper_a.md`
- `notes/paper_cards/paper_b.md`

Evidence：

- 读取 5 篇摘要和 2 篇全文。
- 运行 `python scripts/extract_pdf_text.py papers/a.pdf`。

Not complete：

- 3 篇只有摘要，未下载全文。
- `paper_b.md` 中 Figure 3 的结论缺页码定位。

Review findings：

1. `paper_b.md` 的 Figure 3 结论缺来源定位，不能入库为强证据。
2. related work 草稿如果基于 3 篇摘要继续扩写，会违反“全文优先”的质量标准。
3. 数据集名称不一致需要先规范化，否则证据矩阵后续难以聚合。

Next step：先补 3 篇全文或把它们降级为摘要候选；修复 Figure 3 定位；统一数据集名称后再写 prose。

### 验收

| 标准 | 结果 |
|---|---|
| 新会话可只读 handoff 接续 | Pass |
| Review flag abstract-only evidence and missing Figure 3 | Pass |
| 下一步优先证据修复而非写作 | Pass |

## 5-13. 后续 Adversarial Outputs

| Fixture | 对应 skill | 完整输出 | 关键通过信号 |
|---|---|---|---|
| `literature-search-bias-minimal.md` | `literature-landscape-researcher` | `evals/outputs/2026-06-21/literature-search-bias-minimal-output.md` | 拒绝 confirmation-only，保留 null result，abstract-only 降级，单一查询不推出 gap |
| `conflicting-literature-minimal.md` | `literature-evidence-reader` | `evals/outputs/2026-06-21/conflicting-literature-minimal-output.md` | 保留条件化冲突，提出 moderator hypothesis 和判别实验 |
| `experiment-tradeoff-minimal.md` | `experiment-design-planner` | `evals/outputs/2026-06-21/experiment-tradeoff-minimal-output.md` | 不只看主指标，处理 calibration/subgroup guardrails |
| `reproduction-mismatch-minimal.md` | `reproduction-data-analyst` | `evals/outputs/2026-06-21/reproduction-mismatch-minimal-output.md` | 拒绝伪复现，定位 dataset/split/seed mismatch |
| `data-analysis-leakage-minimal.md` | `reproduction-data-analyst` | `evals/outputs/2026-06-21/data-analysis-leakage-minimal-output.md` | 拒绝把显著性/AUC 当充分证据，定位 missingness 和 user leakage |
| `synthesis-overclaim-minimal.md` | `research-synthesis-writer` | `evals/outputs/2026-06-21/synthesis-overclaim-minimal-output.md` | 拒绝 universal overclaim，输出 traceability map |
| `submission-readiness-minimal.md` | `submission-readiness-reviewer` | `evals/outputs/2026-06-21/submission-readiness-minimal-output.md` | 先列 blocker，抓出匿名/页数、overclaim、复现缺口和未引用图 |
| `knowledge-curation-minimal.md` | `research-knowledge-curator` | `evals/outputs/2026-06-21/knowledge-curation-minimal-output.md` | 不做摘要堆积，识别 abstract-only 弱证据、重复 DOI 和 unsupported universal claim |
| `long-running-goal-drift-minimal.md` | `research-program-manager` | `evals/outputs/2026-06-21/long-running-goal-drift-minimal-output.md` | 不误判 complete/blocked，只保留一个 active task，记录 blocker recurrence 并拒绝 scope drift |

## 总结

| Skill | Smoke Eval Result | Residual Risk |
|---|---|---|
| `xhs-method-ingester` | Pass | 需要下一批真实笔记验证评论处理和进度追加 |
| `literature-landscape-researcher` | Pass | 需要真实数据库验证 query syntax、搜索覆盖和筛选一致性 |
| `literature-evidence-reader` | Pass | 需要真实 PDF 验证图表和 supplement |
| `research-question-council` | Pass | 需要真实选题和 A/B 对照普通 brainstorm |
| `experiment-design-planner` | Pass | 需要真实实验验证 guardrail 决策是否可操作 |
| `reproduction-data-analyst` | Pass | 需要真实 repo/notebook/CSV 验证环境失败、长时运行和数据 schema |
| `research-synthesis-writer` | Pass | 需要真实论文段落和审稿回复验证写作边界 |
| `submission-readiness-reviewer` | Pass | 需要真实投稿包验证页数、匿名扫描和 venue rules |
| `research-knowledge-curator` | Pass | 需要真实 Obsidian/Zotero vault 验证 frontmatter、backlinks、断链和重复 DOI |
| `research-program-manager` | Pass | 需要真实跨天任务验证状态恢复、决策日志和 blocker 升级 |
| `research-handoff-review` | Pass | 需要真实跨天任务验证是否减少重复解释 |
