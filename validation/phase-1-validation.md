# Phase 1 Validation

验证日期：2026-06-21

## 结构验证

使用 skill-creator 的 `quick_validate.py` 对 11 个 skill 草案执行基础验证。

| Skill | 验证命令 | 结果 |
|---|---|---|
| `xhs-method-ingester` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/xhs-method-ingester` | 通过：`Skill is valid!` |
| `literature-landscape-researcher` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/literature-landscape-researcher` | 通过：`Skill is valid!` |
| `literature-evidence-reader` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/literature-evidence-reader` | 通过：`Skill is valid!` |
| `research-question-council` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/research-question-council` | 通过：`Skill is valid!` |
| `experiment-design-planner` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/experiment-design-planner` | 通过：`Skill is valid!` |
| `reproduction-data-analyst` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/reproduction-data-analyst` | 通过：`Skill is valid!` |
| `research-synthesis-writer` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/research-synthesis-writer` | 通过：`Skill is valid!` |
| `submission-readiness-reviewer` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/submission-readiness-reviewer` | 通过：`Skill is valid!` |
| `research-knowledge-curator` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/research-knowledge-curator` | 通过：`Skill is valid!` |
| `research-program-manager` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/research-program-manager` | 通过：`Skill is valid!` |
| `research-handoff-review` | `python3 $CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py skills/research-handoff-review` | 通过：`Skill is valid!` |

## UI 元数据

已为每个 skill 生成 `agents/openai.yaml`，包含 `display_name`、`short_description` 和显式引用 `$skill-name` 的 `default_prompt`。

| Skill | Metadata |
|---|---|
| `xhs-method-ingester` | `skills/xhs-method-ingester/agents/openai.yaml` |
| `literature-landscape-researcher` | `skills/literature-landscape-researcher/agents/openai.yaml` |
| `literature-evidence-reader` | `skills/literature-evidence-reader/agents/openai.yaml` |
| `research-question-council` | `skills/research-question-council/agents/openai.yaml` |
| `experiment-design-planner` | `skills/experiment-design-planner/agents/openai.yaml` |
| `reproduction-data-analyst` | `skills/reproduction-data-analyst/agents/openai.yaml` |
| `research-synthesis-writer` | `skills/research-synthesis-writer/agents/openai.yaml` |
| `submission-readiness-reviewer` | `skills/submission-readiness-reviewer/agents/openai.yaml` |
| `research-knowledge-curator` | `skills/research-knowledge-curator/agents/openai.yaml` |
| `research-program-manager` | `skills/research-program-manager/agents/openai.yaml` |
| `research-handoff-review` | `skills/research-handoff-review/agents/openai.yaml` |

YAML 解析补充检查：

| Skill | YAML 解析 | `default_prompt` 引用 |
|---|---|---|
| `xhs-method-ingester` | 通过 | 包含 `$xhs-method-ingester` |
| `literature-landscape-researcher` | 通过 | 包含 `$literature-landscape-researcher` |
| `literature-evidence-reader` | 通过 | 包含 `$literature-evidence-reader` |
| `research-question-council` | 通过 | 包含 `$research-question-council` |
| `experiment-design-planner` | 通过 | 包含 `$experiment-design-planner` |
| `reproduction-data-analyst` | 通过 | 包含 `$reproduction-data-analyst` |
| `research-synthesis-writer` | 通过 | 包含 `$research-synthesis-writer` |
| `submission-readiness-reviewer` | 通过 | 包含 `$submission-readiness-reviewer` |
| `research-knowledge-curator` | 通过 | 包含 `$research-knowledge-curator` |
| `research-program-manager` | 通过 | 包含 `$research-program-manager` |
| `research-handoff-review` | 通过 | 包含 `$research-handoff-review` |

## 能力验证计划

结构验证只证明 skill 文件格式可用，不证明科研能力有效。下一阶段必须用真实任务验证。

| 能力 | 验证任务 | 输入 | 通过标准 | 失败修正 |
|---|---|---|---|---|
| 外部笔记到 skill 提炼 | 下一批小红书笔记批处理 | 新笔记链接、截图、评论 | `progress.md` 新增五栏记录；至少 1 个方法被明确 Drop 或 Rewrite；产物不复述原文 | 若只有摘要，重跑方法卡；若评论不可读，标注而不推断 |
| 可复现文献调研 | 真实主题检索 | 中性问题、来源范围、种子论文 | query/screening/dedupe log 完整；保留 null/冲突；gap 与覆盖范围绑定 | 若迎合 confirmation-only 或 gap 过强，重写协议并扩展来源 |
| 文献证据精读 | 单篇 PDF 精读 | 1 篇论文 PDF、研究问题、supplement | 关键结论有来源定位；至少 5 张证据卡；检查图表/supplement | 若只生成摘要，缩到一个章节重跑证据卡 |
| 研究问题委员会 | 选题压力测试 | 研究方向、3 篇论文卡、数据限制 | 产生 3 个候选问题；至少淘汰 1 个；最终下一步可执行 | 若建议泛泛，强制每个角色引用输入材料 |
| 科研知识库整理 | 真实 vault 小批量整理 | Obsidian/Zotero 样例、PDF、旧笔记、实验日志 | 先做 source audit；abstract-only 不进强证据；重复和冲突可追踪；write queue 可接续 | 若变成摘要堆积，重跑 note plan 和 claim registry |
| 长期科研计划管理 | 真实跨天研究任务 | 完整目标、完成标准、日志、外部依赖 | 逐项证据审计；单一 active task；blocker recurrence；下一会话可恢复 | 若提前 complete 或多个 in-progress，重建 program status |
| 科研 handoff/review | 一次跨文件科研任务 | 工作区、产物路径、日志 | 新对话能只读 handoff 接续；review 找到具体风险或确认无问题 | 若 handoff 空泛，补路径、命令、产物和风险 |

## 包级验证脚本

新增 `scripts/validate_pack.py`，用于每次新增笔记、skill 或模板后做结构守门。

验证命令：

```bash
python3 codex-research-enhancement-pack/scripts/validate_pack.py codex-research-enhancement-pack
```

验证结果：

```text
PACK VALIDATION PASSED
- root: `<repo-root>`
- skills: 11
- required files: 23
- eval fixtures: 13
- eval outputs: 13
```

脚本覆盖：

- 必需交付物是否存在：README、progress、workflow、checklist、templates、rubric、examples、review、validation、eval plan。
- 11 个 skill 是否包含 `Trigger`、`Inputs`、`Procedure`、`Output Format`、`Quality Standards`、`Failure Repair`。
- `agents/openai.yaml` 是否存在并引用对应 `$skill-name`。
- `progress.md` 是否保留五栏追踪表、待验证问题和下一步计划。
- Markdown 本地链接是否指向存在的文件或目录，避免 GitHub 手册断链。
- 13 个最小/adversarial eval fixture 是否存在。
- 13 个 smoke eval 输出是否存在，并包含 `Acceptance Result`。

## 安装脚本验证

验证命令：

```bash
python3 scripts/install_skills.py --list
python3 scripts/install_skills.py --all --dry-run --target /private/tmp/codex-skills-v14.UOEebb
python3 scripts/install_skills.py --all --target /private/tmp/codex-skills-v14.UOEebb
python3 scripts/install_skills.py --all --target /private/tmp/codex-skills-v14.UOEebb
python3 scripts/install_skills.py --skill research-program-manager --force --target /private/tmp/codex-skills-v14.UOEebb
```

验证结果：

- `--list` 返回 11 个 skill。
- `--dry-run` 只打印计划，不写入。
- 首次安装成功，临时目录包含 11 个 `SKILL.md`。
- 重复安装在未传 `--force` 时退出码为 1，并逐项标记 `SKIP`。
- 显式 `--force` 可替换指定 skill，退出码为 0。

## 最小 Eval Fixtures

| Fixture | 对应能力 | 当前状态 |
|---|---|---|
| `evals/fixtures/xhs-batch-minimal.md` | 外部笔记到 skill 提炼 | Smoke eval 通过 |
| `evals/fixtures/literature-search-bias-minimal.md` | 可复现文献调研 | Smoke eval 通过；拒绝 confirmation-only 搜索并保留 null/abstract-only/duplicate 状态 |
| `evals/fixtures/paper-reading-minimal.md` | 文献证据精读 | Smoke eval 通过；完整输出含显式 Method Cards |
| `evals/fixtures/conflicting-literature-minimal.md` | 冲突文献整合 | Smoke eval 通过；输出保留条件化冲突和 moderator hypotheses |
| `evals/fixtures/research-question-minimal.md` | 研究问题委员会 | Smoke eval 通过 |
| `evals/fixtures/experiment-tradeoff-minimal.md` | 实验设计规划 | Smoke eval 通过；输出包含 primary/guardrail metrics 和冲突指标决策规则 |
| `evals/fixtures/reproduction-mismatch-minimal.md` | 代码复现与数据分析核验 | Smoke eval 通过；输出拒绝伪复现并定位 dataset/split/seed mismatch |
| `evals/fixtures/data-analysis-leakage-minimal.md` | 数据分析核验 | Smoke eval 通过；输出拒绝把显著性/AUC 作为充分证据，并定位 missingness 和 user leakage |
| `evals/fixtures/synthesis-overclaim-minimal.md` | 科研写作综合 | Smoke eval 通过；输出拒绝 universal overclaim 并包含 traceability map |
| `evals/fixtures/submission-readiness-minimal.md` | 投稿准备审查 | Smoke eval 通过；输出抓出匿名/页数 blocker、abstract overclaim、缺复现细节和未引用 Figure 2 |
| `evals/fixtures/knowledge-curation-minimal.md` | 科研知识库整理 | Smoke eval 通过；输出 source audit、note plan、claim registry、dedupe/conflict log、write queue 和 do-not-ingest |
| `evals/fixtures/long-running-goal-drift-minimal.md` | 长期科研计划管理 | Smoke eval 通过；不误判 complete/blocked，限制单一 active task，记录 blocker 次数并拒绝 scope drift |
| `evals/fixtures/handoff-minimal.md` | 科研 handoff/review | Smoke eval 通过 |

详细结果见 [eval-results-2026-06-21.md](eval-results-2026-06-21.md)。

## 当前限制

- 本批小红书评论接口无登录不可读，未纳入评论区讨论。
- 没有真实论文 PDF，因此 `literature-evidence-reader` 尚未证明能处理图表、supplement 和证据定位。
- 没有真实科研选题，因此 `research-question-council` 尚未完成 A/B 对照验证。
- 这些 skill 目前位于工作区增强包内，未安装到 `$CODEX_HOME/skills`；如需全局触发，应复制或安装对应 skill 目录。
