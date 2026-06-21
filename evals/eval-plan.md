# Eval Plan

用途：给每个 skill 一组最小输入样例和验收标准。当前 eval 是人工/半自动评估，不替代真实论文、真实选题和真实科研任务验证。

## 运行方式

1. 运行结构守门：

```bash
python3 codex-research-enhancement-pack/scripts/validate_pack.py codex-research-enhancement-pack
```

2. 对每个 fixture，显式调用对应 skill，检查输出是否满足“通过标准”。
3. 将结果记录到 `validation/phase-*.md`，不要覆盖旧记录。

## Fixture 映射

| Fixture | Skill | 通过标准 |
|---|---|---|
| `fixtures/xhs-batch-minimal.md` | `xhs-method-ingester` | 至少提炼 2 个方法；标出 1 个弱信号或 Drop；输出 skill/workflow/checklist 三类产物草案；包含五栏进度行 |
| `fixtures/literature-search-bias-minimal.md` | `literature-landscape-researcher` | 拒绝 confirmation-only 搜索和 universal claim；记录 protocol/query/screening/dedupe；保留 null result；abstract-only 降级；不从单一查询推出 gap |
| `fixtures/paper-reading-minimal.md` | `literature-evidence-reader` | 先做 preflight；输出证据卡、方法卡、变量表；每个关键结论指向段落、表或图；不只写摘要 |
| `fixtures/conflicting-literature-minimal.md` | `literature-evidence-reader` | 保留互相矛盾的证据；按条件区分结论；提出 moderator hypothesis 和判别实验；不能强行合并为单一结论 |
| `fixtures/research-question-minimal.md` | `research-question-council` | 五角色均给出具体风险；生成 3 个候选问题；至少淘汰 1 个；最终给出下一步最小行动 |
| `fixtures/experiment-tradeoff-minimal.md` | `experiment-design-planner` | 不只看主指标；定义 primary 和 guardrail metrics；处理 calibration/subgroup tradeoff；给出预算内 follow-up；记录复现字段 |
| `fixtures/reproduction-mismatch-minimal.md` | `reproduction-data-analyst` | 不把 mismatch 说成复现成功；比较 target/local/delta/tolerance；优先定位数据版本、split、seed；输出 run log 和 reproducibility record |
| `fixtures/data-analysis-leakage-minimal.md` | `reproduction-data-analyst` | 不把显著性或 AUC 当成充分证据；识别 treatment/severity missingness 和 user-level leakage；分开审查效应估计和预测；提出 sensitivity analysis 与 grouped split |
| `fixtures/synthesis-overclaim-minimal.md` | `research-synthesis-writer` | 拒绝或弱化无证据强声明；保留冲突证据；不把 pilot 写成定论；输出 traceability map 和 removed/weakened claims |
| `fixtures/submission-readiness-minimal.md` | `submission-readiness-reviewer` | 不先润色；决策不是 ready；抓出匿名/页数 blocker、abstract overclaim、缺复现细节和未引用 Figure 2 |
| `fixtures/knowledge-curation-minimal.md` | `research-knowledge-curator` | 不做摘要堆积；识别 abstract-only 弱证据、重复 DOI 和 unsupported universal claim；输出 source audit、note plan、claim registry、write/review queue |
| `fixtures/long-running-goal-drift-minimal.md` | `research-program-manager` | 不误判 complete/blocked；保留真实验证标准；只有一个 in-progress；记录 blocker 次数；拒绝无关 CSS scope drift；输出 next proof |
| `fixtures/handoff-minimal.md` | `research-handoff-review` | 生成 handoff；列出改动、未改动、证据、风险、下一步；review findings 先于总结 |
| `fixtures/project-conversation-curation-minimal.md` | `research-knowledge-curator` + `research-program-manager` | 先做会话 source audit；区分 verified/model/unverified/user decision；合并重复问答；不把模拟规则写成硬件事实；输出 context capsule |

## 失败处理

- 如果输出泛泛，收窄输入并要求引用 fixture 中的具体材料。
- 如果输出只做摘要，重跑并要求方法卡或证据卡。
- 如果输出无法复用，补触发条件、输入、输出格式和失败修正。
- 如果 fixture 无法覆盖真实风险，在下一批真实任务后新增 fixture。
