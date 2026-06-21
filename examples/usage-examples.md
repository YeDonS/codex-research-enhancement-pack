# 使用示例

## 示例 0：可复现文献调研

```text
使用 $literature-landscape-researcher 调研“证据约束是否降低 LLM 文献综述中的 unsupported claims”。

要求：
1. 先把问题改写为中性问题，拒绝只找支持证据。
2. 定义 inclusion/exclusion、数据库、日期、语言和停止规则。
3. 记录 exact query、filters、hits 和 export。
4. 分阶段筛选并记录理由，按 DOI 去重。
5. 保留 positive、null 和 contradictory evidence。
6. 输出 evidence landscape、gap audit 和 3-5 篇全文精读队列。
```

预期输出：

- 不从一个数据库或一个查询推出 research gap。
- Abstract-only 不进入强综合。
- 下一步能直接交给 `$literature-evidence-reader`。

## 示例 1：处理新一批小红书笔记

```text
使用 $xhs-method-ingester 处理下面 6 条小红书笔记和 2 段评论截图。

目标：只保留能提升科研生产力的方法，尤其是文献阅读、选题、实验设计和长期任务管理。

要求：
1. 先标注哪些链接、截图、评论可读。
2. 不做摘要堆积，按方法卡提炼：问题、方法、步骤、适用场景、风险限制。
3. 将可用方法转成 skill 草案、科研 workflow、自查 checklist。
4. 更新 progress.md 五栏记录。
5. 最后 review：Keep / Rewrite / Weak signal / Drop。
```

预期输出：

- `progress.md` 新增批次。
- 新增或更新 skill/workflow/checklist。
- 阶段 review 说明哪些方法被保留或删除。

## 示例 2：单篇论文精读入库

```text
使用 $literature-evidence-reader 处理 /path/to/paper.pdf。

研究问题：该论文提出的干预是否能在低资源医学影像场景下提升模型泛化？

请先做 preflight：
- 全文是否可读
- 图表是否可读
- supplement 是否可读
- 代码和数据链接是否存在

如果材料不足，停止并列缺口。
如果材料足够，输出 Paper Reading Pack，包括证据卡、方法卡、变量表、可复现实验要点和 Obsidian 入库候选卡。
```

预期输出：

- 每个关键结论有页码、图、表或 supplement 定位。
- 不把摘要当成知识库主体。
- 明确哪些卡片可以入库，哪些不能。

## 示例 3：选题压力测试

```text
使用 $research-question-council 审查这个选题：
“用多模态大模型辅助病理切片诊断是否能减少低年资医生漏诊率？”

输入材料：
- 3 篇相关论文摘要和 evidence cards
- 可用数据：本院历史匿名病例 800 例
- 限制：不能做前瞻性临床试验；2 个月内完成初步结果

请生成 3 个候选研究问题，用反对者、第一性原理者、扩展者、局外人、执行者五个角色审查，并按新颖性、证据基础、可证伪性、可行性、贡献打分。最后给出继续、缩小、转向或停止。
```

预期输出：

- 候选问题不空泛，包含对象、变量、指标或数据。
- 至少一个问题被明确淘汰，并说明原因。
- 下一步是一个能在一坐内完成的行动。

## 示例 4：实验设计

```text
围绕这个假设设计最小可运行实验：
“加入证据引用约束后，LLM 生成的文献综述事实错误率会下降。”

已有材料：
- 30 篇论文 PDF
- 10 个综述写作问题
- 一个人工标注事实错误的样例表

输出实验计划：变量、处理组、对照组、指标、样本筛选、统计方法、运行命令、输出路径、失败标准和下一轮决策。
先设计最小实验，不要直接跑全量。
```

预期输出：

- 假设和反假设明确。
- 指标能衡量事实错误率，而不是只看语言质量。
- 失败标准在实验前定义。

## 示例 5：长期任务 handoff

```text
使用 $research-handoff-review 结束本轮“文献综述证据矩阵”任务。

请写 handoff：
- 本轮目标
- 输入材料
- 改动文件
- 生成的表格/笔记路径
- 未解决问题
- 风险
- 下一步

然后用独立 review 视角检查本轮产物，只返回问题清单和修正建议。
```

预期输出：

- 新对话可以只读 handoff 继续。
- review 先列问题，不做泛泛总结。
- 不提交二进制、隐私、密钥或无关文件。

## 示例 6：数据分析核验

```text
使用 $reproduction-data-analyst 审查这个 notebook 结果是否能写进论文：

输入：
- 数据：analysis/retention_panel.csv
- Notebook：analysis/notebooks/retention_effect.ipynb
- 输出表：analysis/outputs/retention_table1.csv
- Claim：Intervention A improves 30-day retention by +6.1 pp, p = 0.018; prediction AUC = 0.82

请先核验：
- 数据单位和重复主体
- 缺失值是否按处理组、严重程度和结果分层
- 排除规则是否在看结果前定义
- train/test split 是否有 user-level leakage
- 预测指标和效应估计是否被混在一起解释

如果存在缺失值偏差或泄漏，不要润色 claim；输出最小诊断和重跑计划。
```

预期输出：

- 不把显著性或高 AUC 当成充分证据。
- 明确哪些 claim 不能报告，哪些需要弱化。
- 给出 missingness audit、grouped split 和 sensitivity analysis 的下一步。

## 示例 7：投稿准备审查

```text
使用 $submission-readiness-reviewer 审查这个投稿包是否 ready：

输入：
- Manuscript：paper/main.tex
- Figures：paper/figures/
- Tables：paper/tables/
- Logs：runs/main_experiment/metrics.json, runs/ablation/metrics.json
- Venue：匿名提交，8 页正文限制，必须有 reproducibility statement 和 data/code availability statement

请先输出 blockers，不要先润色。重点检查：
- abstract 和 conclusion 的强 claim 是否有证据
- figure/table 是否被正文引用并可追溯到输出
- 匿名、页数和 venue compliance
- reproducibility statement 是否包含环境、数据版本、命令、seed、输出路径
- limitations 是否覆盖真实风险
```

预期输出：

- ready/minor/major/blocked 决策。
- findings 先于总结或润色建议。
- 每个 blocker 有 manuscript 位置、artifact path 或 venue rule 依据。

## 示例 8：科研知识库整理

```text
使用 $research-knowledge-curator 整理下面材料到 Obsidian vault：

输入：
- PDFs：papers/
- Zotero export：zotero_export/library.json
- 已有笔记：vault/papers/, vault/evidence/
- 实验日志：runs/pilot_2026-06-20/metrics.json
- 项目：evidence-grounded literature review

目标：
1. 不要把材料直接总结成长笔记。
2. 先做 source audit，标出全文、abstract-only、metadata-only、重复、冲突和 drop。
3. 规划 paper cards、evidence cards、experiment cards 和 project index。
4. 每条 claim 必须链接 DOI/URL、页码/图表/日志/命令/输出路径。
5. 输出 write queue、review queue 和 do-not-ingest。
```

预期输出：

- 先给 note plan，再写入或建议写入。
- abstract-only 只进 review queue，不作为强证据。
- 重复 DOI 和旧 claim 有 dedupe/conflict 记录。

## 示例 9：长期科研计划管理

```text
使用 $research-program-manager 管理这个跨月科研目标。

输入：
- 完整目标和逐项完成标准
- 当前 repo、progress、handoff、实验日志和外部依赖
- 时间、数据、compute、伦理和审批约束

要求：
1. 先做 requirement-by-requirement evidence audit。
2. 区分结构通过、真实能力验证和缺失证据。
3. 建 milestones 和 decision log。
4. 同时只保留一个 in-progress 动作。
5. blocker 记录出现次数、已试缓解和升级条件。
6. 不因预算、时间或文件存在提前标记 complete。
7. 输出下一会话无需重读聊天即可执行的动作。
```

预期输出：

- Program charter、requirement audit、milestones、work queue 和 decision log。
- Scope drift 被拒绝或映射到完成标准。
- Completion/blocked 状态由证据和规则决定。
