# Codex 科研能力增强包

版本：v1.4

这个包把本批小红书笔记中可迁移的方法沉淀为可复用的 Codex 科研流程。当前产物是 workspace 内的草案包，尚未安装到 `$CODEX_HOME/skills`。

GitHub：[YeDonS/codex-research-enhancement-pack](https://github.com/YeDonS/codex-research-enhancement-pack)

## Skill 清单

| Skill | 用途 | 状态 |
|---|---|---|
| `xhs-method-ingester` | 把小红书笔记、评论和参考材料提炼为可迁移方法，并转成 skill/workflow/checklist | 草案可用 |
| `literature-landscape-researcher` | 可复现地检索、筛选和去重多来源文献，保留冲突并审计 research gap | 草案可用，待真实数据库验证 |
| `literature-evidence-reader` | 单篇论文精读，产出证据卡、方法卡、变量表和入库笔记 | 草案可用，待真实 PDF 验证 |
| `research-question-council` | 用多角色委员会压力测试研究问题、假设和实验计划 | 草案可用，待 A/B 验证 |
| `experiment-design-planner` | 设计和审查实验，明确假设、变量、指标、guardrails、决策规则和复现记录 | 草案可用，待真实实验验证 |
| `reproduction-data-analyst` | 审查论文代码复现和数据分析结果，记录环境、数据版本、命令、随机种子、指标差异和下一步排查 | 草案可用，待真实复现验证 |
| `research-synthesis-writer` | 将证据卡、论文笔记和实验结果转为可追溯的综述、论文段落、审稿回复和投稿材料 | 草案可用，待真实写作任务验证 |
| `submission-readiness-reviewer` | 投稿、预印本、camera-ready、rebuttal 或修订前审查 claim、图表、可复现性、匿名和 venue compliance | 草案可用，待真实投稿包验证 |
| `research-knowledge-curator` | 整理 Obsidian/Zotero/论文卡/证据卡/实验卡和索引笔记，避免摘要堆积和弱证据入库 | 草案可用，待真实 vault 验证 |
| `research-program-manager` | 维护长期科研目标、里程碑、证据审计、决策日志、阻塞升级、阶段 review 和可恢复状态 | 草案可用，待真实跨天任务验证 |
| `research-handoff-review` | 管理跨天科研任务、PR/handoff、独立审查和复盘 | 草案可用，待项目试跑 |

每个 skill 都包含 `SKILL.md` 和 `agents/openai.yaml`，并通过 skill-creator 的基础结构验证。验证记录见 [phase-1-validation.md](validation/phase-1-validation.md)。

## 使用与安装

- [中文使用手册](docs/USER_GUIDE.md)：skill 选择、推荐科研链路、新笔记批处理和质量门槛。
- [安装与 GitHub 同步说明](docs/INSTALLATION_AND_SYNC.md)：安装、更新、选择性安装、贡献和安全边界。
- `python3 scripts/install_skills.py --list`：查看可用 skill。
- `python3 scripts/install_skills.py --all --dry-run`：预览安装。

## 包级验证

运行结构守门脚本：

```bash
python3 codex-research-enhancement-pack/scripts/validate_pack.py codex-research-enhancement-pack
```

当前验证结果：通过。脚本检查必需产物、11 个 skill 的核心章节、`agents/openai.yaml`、进度五栏、eval fixtures 和 smoke eval 输出。最小 eval 计划见 [eval-plan.md](evals/eval-plan.md)，同会话 smoke eval 结果见 [eval-results-2026-06-21.md](validation/eval-results-2026-06-21.md)，独立输出位于 [evals/outputs/2026-06-21](evals/outputs/2026-06-21)。v1.4 新增长期科研 program manager 和目标漂移 adversarial fixture。

## 科研任务流程

主要流程见 [research-task-flows.md](workflows/research-task-flows.md)：

- 文献调研：中性协议、query log、多来源检索、筛选、去重、证据图谱和 gap audit。
- 单篇精读：preflight、全文解析、图表/supplement 检查、证据卡入库。
- 研究问题生成：材料约束、多角色评审、问题打分、实验路线。
- 实验设计：假设、变量、数据、基线、指标、失败预案。
- 代码复现/数据分析：环境、命令、数据版本、缺失值、泄漏、指标差异和敏感性分析。
- 投稿准备：claim-evidence、图表、页数、匿名、可复现性、data/code availability 和 reviewer response。
- 知识库整理：source audit、论文卡、证据卡、实验卡、索引笔记、去重、冲突和 review queue。
- 长期任务管理：完整目标、requirement audit、里程碑、单一 active task、决策日志、阻塞升级、handoff 和 review。

## Prompt/Goal 模板

模板见 [prompt-goal-templates.md](templates/prompt-goal-templates.md)。优先使用 goal 约束长期任务，用 prompt 启动单轮任务。

## 质量评估 Rubric

完整评分表见 [research-capability-rubric.md](rubrics/research-capability-rubric.md)。核心维度是来源可追溯、任务边界、方法可执行、证据质量、研究问题质量、实验可复现、低人工负担和可复用沉淀。

## 使用示例

完整示例见 [usage-examples.md](examples/usage-examples.md)，覆盖新笔记批处理、文献调研、单篇论文精读、选题压力测试、实验设计和长期任务 handoff。
