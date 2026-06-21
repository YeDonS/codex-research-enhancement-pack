# Fixture: Project Conversation Curation

## Goal

整理一个跨多轮系统实验项目的对话，减少重复解释，并生成可恢复的 handoff。

## Inputs

| Session | Extract |
|---|---|
| S1 | “调度器已经让后台任务 yield，所以读延迟应该下降。”没有附日志。 |
| S2 | 代码显示 high-priority read 从独立 HP tail 开始，并将 LP tail 向后移动。 |
| S3 | 压测中 `yield_count=0`，但 read latency 比基线更好。 |
| S4 | “这个机制符合真实 NAND 抢占。”没有硬件资料或模型说明。 |
| S5 | 用户连续追问：为什么 yield 为 0 但结果变好？为什么有改善但 p99 变差？ |

## Required Output

1. Goal brief，标出是否可直接改代码。
2. Conversation inventory 和 source audit。
3. verified facts、model assumptions、unverified claims、user decisions、open questions 的分类。
4. 重复问题聚类，给出一条 canonical diagnosis path。
5. issue register、decision log 和不超过一页的 context capsule。
6. 不得把 “yield_count=0” 写成机制已被证明有效；不得把模拟 HP/LP 规则写成真实设备事实。
