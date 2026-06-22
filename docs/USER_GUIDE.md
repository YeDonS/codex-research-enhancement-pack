# Codex 科研能力增强包使用手册

## 1. 适用范围

本包用于把外部经验、论文、实验、写作任务和长期研究状态转成可复用的 Codex 工作流。它不替代领域专家判断，也不把结构校验等同于真实科研有效性。

## 2. 快速开始

1. 在包根目录运行结构校验：

```bash
python3 scripts/validate_pack.py .
```

2. 查看可安装 skill：

```bash
python3 scripts/install_skills.py --list
```

3. 先预览安装动作：

```bash
python3 scripts/install_skills.py --all --dry-run
```

4. 安装全部 skill：

```bash
python3 scripts/install_skills.py --all
```

安装和更新细节见 [INSTALLATION_AND_SYNC.md](INSTALLATION_AND_SYNC.md)。

## 3. Skill 选择

| 任务 | Skill | 最小输入 |
|---|---|---|
| 处理新一批小红书笔记/评论 | `$xhs-method-ingester` | 链接、正文、截图、评论、目标能力范围 |
| 检索领域文献和找 gap | `$literature-landscape-researcher` | 研究问题、范围、数据库/时间限制、种子论文 |
| 单篇论文精读和证据卡 | `$literature-evidence-reader` | PDF/DOI、阅读问题、supplement |
| 生成和压力测试研究问题 | `$research-question-council` | 方向、已有证据、数据和时间限制 |
| 设计实验 | `$experiment-design-planner` | 假设、数据、基线、指标、预算 |
| 复现代码/审查数据分析 | `$reproduction-data-analyst` | repo/notebook、数据版本、命令、日志、目标指标 |
| 写综述/论文段落/审稿回复 | `$research-synthesis-writer` | 证据卡、结果、冲突、目标文本类型 |
| 投稿前检查 | `$submission-readiness-reviewer` | manuscript、figures/tables、日志、venue 规则 |
| 整理 Obsidian/Zotero/项目对话 | `$research-knowledge-curator` | PDF、旧笔记、实验日志、会话导出、thread IDs、vault/项目约定 |
| 管理长期科研计划 | `$research-program-manager` | 完整目标、完成标准、当前证据、约束、里程碑和阻塞 |
| 跨天任务交接和独立 review | `$research-handoff-review` | 目标、改动、命令、产物路径、风险 |

## 4. 推荐科研链路

### 文献到选题

1. 用 `$literature-landscape-researcher` 记录检索协议、筛选和冲突。
2. 把 3-5 篇高优先级全文交给 `$literature-evidence-reader`。
3. 用 `$research-question-council` 生成并淘汰候选问题。
4. 用 `$research-knowledge-curator` 入库证据和开放问题。

### 假设到实验

1. 用 `$experiment-design-planner` 定义假设、反假设、primary/guardrail metrics。
2. 用 `$reproduction-data-analyst` 记录环境、数据、命令、seed 和输出。
3. 结果冲突时先做 mismatch/leakage/missingness audit，不先润色结论。

### 写作到投稿

1. 用 `$research-synthesis-writer` 从证据卡生成可追溯草稿。
2. 用 `$submission-readiness-reviewer` 检查 claim、图表、匿名、页数和复现声明。
3. 用 `$research-handoff-review` 写本轮交接和下一步。

### 长期科研计划

1. 用 `$research-program-manager` 固定完整目标和逐项完成证据。
2. 每轮只保留一个 in-progress 动作，记录命令、文件、输出和验证。
3. 阶段结束时区分结构通过、真实能力通过和仍缺证据。
4. 用 `$research-handoff-review` 生成下一会话可直接执行的交接。
5. 对话已膨胀时，用 `$research-knowledge-curator` 先建 conversation inventory、decision/assumption log 和 context capsule，再继续执行。

## 5. 处理新笔记批次

每一批都必须：

1. 标记链接、截图、正文和评论是否真实可读。
2. 分离摘要、可迁移方法、执行步骤、适用场景和风险限制。
3. 至少更新 skill/workflow/checklist 三类产物。
4. 在 `progress.md` 五栏表追加记录，不覆盖历史批次。
5. 新建阶段 review，明确 Keep、Rewrite、Weak signal 和 Drop。
6. 运行包级校验和相关 fixture。

## 6. 质量门槛

- 文献 gap 不能由一个窄查询或“没搜到”直接推出。
- 强 claim 必须能回到 PDF 页码、图表、代码、日志或数据输出。
- Abstract-only、截图和评论默认是弱证据。
- 实验和数据分析必须记录数据版本、环境、命令、seed、输出和失败标准。
- 投稿准备先检查 blocker，再做语言润色。
- 知识库先做 source audit 和 note plan，不批量制造摘要。
- 长期目标不能因预算耗尽、文件存在或结构检查通过而提前标记完成。

## 7. 验证

- `evals/fixtures/`：最小和 adversarial 输入。
- `evals/outputs/`：期望输出及 acceptance result。
- `validation/`：阶段验证记录。
- `reviews/`：每阶段方法有效性复盘。

结构校验通过只证明包完整，不证明真实科研能力已经验证。真实任务结果应继续追加到 `validation/` 和 `progress.md`。

## 8. 真实任务参考

- [WiscKey + HotRAP：面向范围扫描的分层 Value Log](../validation/real-task-hot-value-tiering-2026-06-21.md)：展示如何从两篇全文证据出发，淘汰弱创新表述，形成研究问题、系统草图、GC/一致性协议、2 GB capacity policy、实验 guardrails 和 stop/revise/continue 规则。
- [Goal Prompt 与项目对话压缩](../validation/goal-prompt-and-conversation-curation-2026-06-22.md)：展示如何把多轮对话压成 Goal Brief、证据状态、重复问题簇、决策日志和可恢复 context capsule。
- [真实存储模拟器修复](../validation/real-task-storage-simulator-repair-2026-06-22.md)：展示 model contract、严格 run manifest、原始直方图守恒和 counter-gated mechanism attribution。
- 真实任务报告中的 `Pass` 只评价对应 skill 产物；没有运行代码时，实验设计必须标 `plan-only` 或 `Partial Pass`。
