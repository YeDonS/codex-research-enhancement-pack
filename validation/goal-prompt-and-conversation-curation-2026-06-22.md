# Goal 编译与项目对话压缩验证

日期：2026-06-22

## Scope

验证两类方法能否减少 Codex 在长期科研项目中的重复问答和错误自信：

1. 从 `goal-prompt-template-skill` 吸收的 outcome-first goal compilation、非阻塞默认假设、最少澄清问题和 inspection/repair approval gate。
2. 对多轮项目对话进行 source audit、decision extraction、重复问题聚类、冲突保留和 context capsule 压缩。

## Source Status

| Source | Status | Use |
|---|---|---|
| 小红书短链 `7TV5moYC2gx` | 不可读，HTTPS/HTTP 均返回 404 | 只记录来源失败，不提炼内容 |
| [goal-prompt-template-skill](https://github.com/linhucong814-cyber/goal-prompt-template-skill) | 可读 | 提炼 goal compiler 的四项可迁移规则 |
| 多轮存储系统项目对话 | 私有原始材料，仅本地审计 | 验证 conversation curation；公开包不复制原对话或本机路径 |

## Transferable Method Units

| Unit | Keep/Rewrite | Transfer | Risk Limit |
|---|---|---|---|
| 一句话目标先编译成 outcome、范围、交付物、完成证据和假设 | Keep | `research-program-manager` Goal Brief | 不能把合理假设伪装成用户确认 |
| 只问影响安全、外部状态或可验证性的缺失信息 | Keep | long-running goal intake | 不得借此跳过真实 blocker |
| inspection 与 repair mutation 分离 | Rewrite | 默认用于未授权的检查/修复任务 | 用户明确授权立即修复时不额外阻塞 |
| 项目对话只保留决策和证据，不保留所有轮次 | Keep | `research-knowledge-curator` conversation curation | 不能删除冲突或无证据强 claim |
| 反复“为什么”聚为 canonical diagnosis path | Keep | workflow、checklist、fixture | 必须链接一个可观测量、代码或日志 |

## Real-Task Validation

私有多轮项目审计成功产出：session inventory、issue register、decision/assumption log、repeated-question clusters 和 context capsule。它暴露出关键质量门槛：模型层 HP/LP 规则不能直接等同于真实硬件 preemption；实验性能变化不能在 yield counter 为零时归因给 yield。

## Acceptance

| Check | Result |
|---|---|
| 新来源先记录可读性，不臆测不可读短链内容 | Pass |
| 已转化为 skill、workflow、checklist、template、fixture 和 review | Pass |
| 每项方法保留触发、输入、步骤、输出、标准和 failure repair | Pass, via updated skills and workflow |
| 私有会话不进入公开仓库 | Pass |
| 真实项目可从 context capsule 恢复 | Pass, pending user approval to save the private report under the project directory |

## Remaining Validation

- 在第二个独立项目中重跑 conversation-capture fixture，检查是否仍能发现 contradictions 而不是机械摘要。
- 对 goal compiler 做 A/B：原始一句话任务与 Goal Brief 的首次执行成功率、追问数和返工次数。
