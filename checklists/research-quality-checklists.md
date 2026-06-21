# 科研能力验收与自查清单

## A. 外部笔记提炼清单

- [ ] 是否记录每条输入材料的可访问状态。
- [ ] 是否明确评论区是否读取成功。
- [ ] 是否把摘要、观点、操作步骤、风险限制分开。
- [ ] 是否至少产出 skill 草案、科研 workflow、验收 checklist 三类产物。
- [ ] 是否为每个能力写明触发条件、输入、步骤、输出、质量标准、失败修正。
- [ ] 是否把弱信号和不可验证内容标为待补充。

## B. Skill 草案清单

- [ ] `name` 使用小写、数字和连字符。
- [ ] `description` 写清楚什么时候触发。
- [ ] SKILL.md 正文少而精，没有堆背景材料。
- [ ] 步骤可执行，不依赖“自己理解一下”。
- [ ] 输出格式固定，方便复用。
- [ ] 有质量标准和失败修正。
- [ ] 没有把一次性 prompt 伪装成 skill。

## C. 文献调研清单

- [ ] 是否在检索前定义中性问题、inclusion/exclusion、日期、语言、来源和停止规则。
- [ ] 是否记录每个数据库的 exact query、搜索日期、过滤器、命中数和 export。
- [ ] 是否按 DOI 或规范化 title/year/authors 去重并保留 dedupe log。
- [ ] 是否记录 title/abstract 和 full-text 阶段的 include/exclude/maybe 理由。
- [ ] 是否保留 negative、null 和 contradictory evidence。
- [ ] abstract-only 是否被标为弱证据。
- [ ] gap claim 是否与检索覆盖范围绑定，而不是由一个查询没命中推出。

## D. 文献精读清单

- [ ] 全文是否可读，不是只有摘要。
- [ ] 图、表、appendix、supplement 是否检查。
- [ ] 每个关键结论是否有页码、节、图或表定位。
- [ ] 是否产出证据卡、方法卡、变量表。
- [ ] 是否区分作者主张、证据、解释和下一步。
- [ ] 是否明确哪些内容不入库。
- [ ] 是否避免“需要人工审核”的大段垃圾输出。

## E. 研究问题清单

- [ ] 研究对象、变量或机制是否明确。
- [ ] 问题是否可证伪。
- [ ] 是否有证据或文献 gap 支撑。
- [ ] 是否能在当前数据和资源下推进。
- [ ] 是否存在严重混杂因素或伦理风险。
- [ ] 是否定义了下一步最小行动。

## F. 实验设计清单

- [ ] 假设和反假设是否写明。
- [ ] 数据来源、样本筛选、排除标准是否明确。
- [ ] 基线、指标和统计方法是否匹配。
- [ ] 失败标准是否在实验前定义。
- [ ] 环境、命令、随机种子和输出路径是否记录。
- [ ] 是否先跑最小实验再扩展。

## G. 长期任务与 handoff 清单

- [ ] 完整目标和原始完成标准是否仍可见。
- [ ] 每个 requirement 是否标记 proven/partial/weak/missing/blocked 并链接证据。
- [ ] 是否最多只有一个任务标记 in progress。
- [ ] 里程碑是否写 outcome、dependency、acceptance 和 risk，而不只是活动。
- [ ] decision log 是否记录证据、替代方案和反转条件。
- [ ] blocker 是否记录出现次数、缓解动作和升级阈值。
- [ ] 任务目标和范围是否明确。
- [ ] 本轮改了什么、没改什么是否写清楚。
- [ ] 产物路径、命令、日志是否可追踪。
- [ ] 是否有独立审查结果。
- [ ] 是否避免提交二进制、密钥、隐私和无关文件。
- [ ] 下一步是否能在不读完整聊天记录的情况下执行。

## H. 数据分析核验清单

- [ ] 数据单位是否明确，是用户、样本、访问、切片、token 还是实验 run。
- [ ] 缺失值比例是否按处理组、结果、关键协变量或严重程度分层检查。
- [ ] 排除规则是否在看结果前定义，是否发生在处理或标签生成之后。
- [ ] train/test split 是否按主体、时间、站点或其他必要分组隔离。
- [ ] 是否检查 label leakage、future leakage、重复主体泄漏和派生特征泄漏。
- [ ] 显著性、效应量、置信区间和敏感性分析是否一起报告。
- [ ] 预测指标和因果/效应估计是否分开解释。

## I. 投稿准备清单

- [ ] 目标 venue 的页数、匿名、格式、artifact、data/code、ethics 要求是否列明。
- [ ] Abstract、contribution 和 conclusion 的强声明是否能映射到 figure/table/log/citation。
- [ ] 每张图表是否在正文引用，caption 是否包含必要样本量、单位、指标和不确定性。
- [ ] 结果表是否能追溯到实验日志、数据版本、命令、seed 和输出路径。
- [ ] Reproducibility statement 是否说明环境、代码、数据、超参、compute 和 release plan。
- [ ] Limitations 是否覆盖真实外部有效性、数据偏差、统计、伦理和部署风险。
- [ ] Rebuttal/revision 是否把每条 reviewer comment 映射到 response、改动位置和残余风险。

## J. 知识库整理清单

- [ ] 是否先做 source audit，而不是直接写摘要。
- [ ] 是否区分 paper card、evidence card、method card、experiment card、claim record 和 index note。
- [ ] 每条可复用 claim 是否链接 DOI/URL、页码、图表、日志、命令或输出路径。
- [ ] abstract-only、metadata-only、截图或评论材料是否被标为弱证据或 review queue。
- [ ] 重复 DOI、重复标题、旧笔记和冲突 claim 是否被合并、链接或保留条件。
- [ ] 是否明确目标路径、frontmatter、tags、backlinks 和验收条件。
- [ ] 是否记录 do-not-ingest、write queue 和下一轮 review queue。

## K. 阶段 Review 清单

- [ ] 哪些方法确实减少了人工负担。
- [ ] 哪些方法提升了证据质量或可复现性。
- [ ] 哪些只是泛泛建议，需要删除。
- [ ] 哪些需要重写为更窄触发条件。
- [ ] 下一阶段验证任务是否具体到材料和产物。

## L. Goal 编译与项目对话压缩清单

- [ ] 粗略目标是否已转成 outcome、范围、交付物、完成证据、约束和假设。
- [ ] 是否只询问会改变安全性、外部状态或可验证性的阻塞问题。
- [ ] 检查/修复类任务是否区分 diagnosis 与 approval 后的 mutation。
- [ ] 是否列出会话 ID、日期、主题、最终产物和当前状态，而不是只给聊天摘要。
- [ ] 每个关键结论是否标为 verified fact、model assumption、unverified claim、user decision 或 open question。
- [ ] assistant 的说法是否已回查到代码、日志、命令、论文或用户确认。
- [ ] 是否把重复问答合并为 root-cause cluster、canonical answer、证据和下一项诊断。
- [ ] 是否显式保留前后矛盾的解释及其 reversal condition。
- [ ] 是否剔除了 tool chatter、注入的 continuation text 和无决策价值的重复输入。
- [ ] context capsule 是否含目标、已证实状态、开放决策、blocker 和下一步动作。
- [ ] 私有会话、绝对路径、凭据或项目数据是否没有进入公开技能包。
