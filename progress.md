# Codex 科研能力增强进度记录

更新时间：2026-06-22

## 包级进展

- v0.1：完成第一批 11 条小红书笔记采集、方法提炼、4 个 skill 草案、科研 workflow、checklist、prompt/goal 模板和阶段 review。
- v0.2：补充每个 skill 的 `agents/openai.yaml`，通过 skill-creator 基础结构验证；新增独立质量评估 rubric、使用示例和 Phase 1 验证记录。
- v0.3：新增包级验证脚本 `scripts/validate_pack.py` 和 4 个最小 eval fixture；验证脚本已通过，能检查必需产物、skill 核心章节、进度五栏和 UI 元数据引用。
- v0.4：执行 4 个 fixture 的同会话 smoke eval，并记录结果；其中 `literature-evidence-reader` 部分通过，暴露出 smoke eval 需要显式输出 Method Cards 的修正点。
- v0.5：将 4 个 smoke eval 拆成独立输出文件；补全文献精读 Method Cards；包级验证脚本新增 eval output 检查。
- v0.5 review：记录结构验证和真实科研能力验证的边界，明确下一步要独立会话重跑 fixture，并新增 adversarial fixture。
- v0.6：新增冲突文献 adversarial fixture 和输出，验证跨文献整合是否保留条件化冲突、moderator hypotheses 和判别实验；包级验证脚本纳入第 5 个 fixture/output。
- v0.6 review：明确跨文献整合的失败标准：不能平均掉冲突，不能只说“结果不一致”，必须保留条件差异并提出判别实验。
- v0.7：新增 `experiment-design-planner` skill、实验 tradeoff adversarial fixture 和输出，验证实验计划是否处理主指标提升但 calibration/subgroup guardrails 失败的情况。
- v0.7 review：明确实验设计失败标准：不能只看主指标，不能平均掉 guardrail 失败，必须有复现记录和 stop/revise/continue 决策规则。
- v0.8：新增 `research-synthesis-writer` skill、写作 overclaim adversarial fixture 和输出，验证文献综述/论文段落是否拒绝无证据强声明并保留 traceability map。
- v0.8 review：明确科研写作失败标准：不能为流畅删除冲突证据，不能迎合更强结论，reviewer response 必须说明修改位置。
- v0.9：新增 `reproduction-data-analyst` skill、复现 mismatch adversarial fixture 和输出，验证本地指标不匹配时是否拒绝伪复现，并优先排查数据版本、split 和 seed。
- v0.9 review：明确复现失败标准：不能把超出容差的 mismatch 写成 reproduced，不能跳过 data/split/seed 直接改模型，run log 必须可追踪。
- v1.0：新增数据分析 leakage adversarial fixture 和输出，验证显著性/AUC 是否会被缺失值偏差和重复主体泄漏拦截。
- v1.0 review：明确数据分析失败标准：不能只看 p 值或 AUC，必须先审 missingness、exclusion、group leakage 和 sensitivity analysis。
- v1.1：新增 `submission-readiness-reviewer` skill、投稿准备 fixture 和输出，验证提交前是否先抓匿名、页数、claim-evidence、图表引用和 reproducibility blockers。
- v1.1 review：明确投稿准备失败标准：不能先润色，必须先判定 ready/minor/major/blocked 并给出可追溯 blocker。
- v1.2：新增 `research-knowledge-curator` skill、知识库整理 fixture 和输出，验证是否能避免摘要堆积、识别 abstract-only 弱证据、重复 DOI 和 unsupported claim。
- v1.2 review：明确知识库整理失败标准：不能无审计批量入库，必须输出 source audit、note plan、claim registry、write queue 和 review queue。
- v1.3：新增 `literature-landscape-researcher` skill、检索偏差 fixture、中文使用手册、安装/GitHub 同步说明和安全安装脚本。
- v1.3 review：明确文献调研失败标准：不能迎合 confirmation-only 搜索，必须记录 query/screening/dedupe，不能从一个窄查询推出 gap。
- v1.3 validation：安装脚本通过 list、dry-run、10-skill install、冲突拒绝和显式 force 替换测试；整包验证通过。
- v1.4：新增 `research-program-manager` skill、长期目标漂移 fixture 和输出，覆盖 requirement audit、milestones、单一 active task、decision log 和 blocker recurrence。
- v1.4 review：明确长期任务失败标准：不能把结构通过当完成，不能多个 in-progress，不能因单个外部依赖停止全部工作。
- v1.4 validation：11 个 skill 完整安装成功；重复安装被拒绝；显式 `--force` 可替换指定 skill；整包和 Markdown 链接验证通过。
- v1.4 GitHub：已发布公开仓库 `https://github.com/YeDonS/codex-research-enhancement-pack`；初始远端提交 `e53b0fc` 与本地 `main` 一致。
- v1.5：使用 WiscKey 和 HotRAP 两篇真实 PDF 及已有 Obsidian 笔记，联合验证 `literature-evidence-reader`、`research-question-council` 和 `experiment-design-planner`。
- v1.5 verdict：淘汰“普通热 value promotion”表述，将问题收窄为 repeated hot-range tracking、key-ordered fast-vLog extent、GC-assisted relocation 和 total WA guardrail。
- v1.5 validation：真实任务产物 rubric 15/16；文献精读与选题委员会通过，实验计划因 codebase、硬件和命令未定而部分通过。
- v1.6：学习 `goal-prompt-template-skill` 的 outcome-first goal compiler，并对真实多会话存储系统项目执行对话审计。
- v1.6 verdict：不新增重复 prompt skill；将 Goal Brief/approval gate 并入 `research-program-manager`，将对话压缩、重复问题聚类和冲突保留并入 `research-knowledge-curator`。
- v1.6 validation：新增对话压缩 fixture/output；真实项目产生私有 handoff，公开包仅保留去标识化规则和验证记录。
- v1.6 installation：11 个自定义 skill 已安装到 `$CODEX_HOME/skills`；安装器 dry-run 正确拒绝静默覆盖，安装后的 `SKILL.md` 与包内版本逐项一致。
- v1.7：在真实存储模拟器代码修复任务中验证 `research-program-manager`、`reproduction-data-analyst` 和 `experiment-design-planner`；新增模型契约、完整请求直方图、sample conservation、严格 run manifest 和 counter-gated mechanism attribution。
- v1.7 verdict：静态、合成模型、分析器、manifest 和 FIO dry-run 通过；目标 Linux module build/load/stress 未执行，因此 runtime correctness 仍为 Partial。
- v1.7 completion audit：六条原始完成标准逐项 Proven；11 个 skill、9 类 workflow、12 组 checklist、9 类模板、rubric、12 个示例、14 组 fixture/output、安装一致性和 Markdown 链接均已验证；PR #1 已合并，GitHub `main` 已读回确认版本为 v1.7。

## 批次 2026-06-21：小红书 Codex/Skill/科研工作流笔记

采集结论：11 条短链均成功解析到小红书网页首屏状态，获得标题、作者、正文、标签、图片数量和互动元数据。评论列表在首屏状态中为空，公开评论接口返回“无登录信息，或登录信息为空”，本批次不把评论内容作为证据。

| 输入材料 | 提炼结论 | 转化产物 | 验证结果 | 下一步 |
|---|---|---|---|---|
| 1. [开源：把经验做成可复用 Skill 的 Skill](https://xhslink.com/o/1mWvi9xBj6E) | 有价值的不是“把方法论写厚”，而是把重复 SOP 产品化为可触发、可验证、可迭代的 skill。关键链路是调研、分析、计划、开发、验证、测试、审计验收、总结迭代。 | `xhs-method-ingester` skill；skill 草案质量清单；进度表字段。 | 正文可读，评论不可读。方法可迁移到“从外部经验提炼 skill”的元流程。 | 后续批次继续用该 skill 处理输入，积累失败案例和可删泛泛建议。 |
| 2. [Vibe coding 别一直傻聊了](https://xhslink.com/o/1zlwgJQIsB0) | 长上下文会让主对话带着惯性自证正确；独立 subagent 适合代码审核、文件检查、资料整理、摘要提炼、测试生成和格式检查。科研里可迁移为“独立审稿/证据检查员”。 | `research-handoff-review` skill；审查清单中的“独立上下文审查”。 | 正文可读，评论不可读。建议清晰可执行。 | 用真实论文笔记让独立审查者找证据缺口。 |
| 3. [LLM Council](https://xhslink.com/o/zGuvxXf41k) | 多角色委员会能做压力测试：反对者找弱点，第一性原理者重构问题，扩展者找机会，局外人指出盲点，执行者给下一步。科研里适合选题、假设和实验计划评审。 | `research-question-council` skill；研究问题生成模板；选题质量 rubric。 | 正文可读，评论不可读。原文偏通用决策，需要科研化改写。 | 以后用 1 个课题方向做 A/B：普通 brainstorm vs council 输出质量。 |
| 4. [CC 和 Codex 协作](https://xhslink.com/o/3hvHKaYNqpw) | 工具链价值由“是否减少人工负担”衡量，不是越自动越好。适合把“思考/方案”和“执行/改代码”分角色，但避免过多复制粘贴。 | 长期任务工作流中的角色分工规则；review 里保留“负担减少”指标。 | 正文可读，评论不可读。属于经验判断，需结合实际任务验证。 | 对科研工作流设置“人工操作次数”指标。 |
| 5. [Codex 实战 10 条](https://xhslink.com/o/7MWaLYwd3Cg) | 分层记忆、自动化、跨软件整合、计划模式、可中止修正、高频任务封装 skill，是长期科研任务管理的基础设施。 | prompt/goal 模板；长期任务清单；进度文档结构。 | 正文可读，评论不可读。多条建议有价值，但需拆成具体科研动作。 | 建立 Obsidian/Zotero/论文 PDF 的最小输入规范。 |
| 6. [Codex 科研工作流技能](https://xhslink.com/o/8dlcKBTYaO2) | 正文只有话题标签，无法提取具体操作。只作为“科研技能需求存在”的弱信号。 | 暂不生成独立能力。 | 正文信息不足，评论不可读。 | 若后续提供截图或正文，重新纳入。 |
| 7. [自动找 paper 的 skill](https://xhslink.com/o/AoXjHG04Jv2) | 好的科研 skill 应降低安装和使用门槛，并把反馈入口前置。对文献搜索能力的启发是：输入少、输出结构化、可反馈修正。 | `literature-evidence-reader` 中加入“检索入口和失败反馈”；文献流程模板。 | 正文可读但细节不足，评论不可读。 | 需要真实 paper-finder prompt 或 repo 后再转成可执行检索脚本。 |
| 8. [GPT + Codex 协作详细教程](https://xhslink.com/o/5k19EnrUfPQ) | 用 GitHub PR 做中间通道，减少文件搬运；每轮任务独立分支，写 handoff，PR 承载 diff 和审查记录；提交前不要盲目 `git add .`。科研可迁移为“每轮分析/实验/写作都有 handoff 和审查记录”。 | `research-handoff-review` skill；长期科研任务 handoff 模板；Git/交接清单。 | 正文可读，评论不可读。流程具体可执行。 | 在下一次代码复现实验中试用 PR + handoff。 |
| 9. [Codex + Obsidian 学习日常](https://xhslink.com/o/1ULOv5cYaai) | 自动化应形成闭环：计划、学习页、练习记录、归档笔记、日志。科研里对应：研究计划、阅读卡、复现记录、证据库、每日/每周日志。 | 科研任务流程模板；长期任务管理清单；goal 模板。 | 正文可读，评论不可读。适合长期研究管理。 | 建立“每日科研 heartbeat”或定时 automation 的最小任务定义。 |
| 10. [ChatGPT 和 Codex 自己协作](https://xhslink.com/o/53CNeJy7z47) | 新架构明确角色：ChatGPT 拆任务/审 PR，Codex 执行，GitHub PR 记录，用户拍板。核心规则：不直接改 main、不越权重构、不提交二进制/密钥/隐私、范围不清先问。 | `research-handoff-review` skill；协作流程；风险清单。 | 正文可读，评论不可读。与第 8 条互相印证。 | 把规则迁移到科研项目 repo 的 `AGENTS.md`。 |
| 11. [Codex 文献阅读流程](https://xhslink.com/o/GplQCgP5nk) | “文献阅读到 Obsidian 知识库”不宜一口气全自动。失败点是跑太久、token 爆炸、只产摘要、没读图表/supplement、全靠人工审核。应先做单篇精读，经人工确认后入库，知识库存证据卡/方法卡/变量表/结论来源，而不是摘要堆积。 | `literature-evidence-reader` skill；文献流程模板；文献质量清单。 | 正文可读，评论不可读。与目标高度相关，是本批次最高价值输入。 | 选择 1 篇论文跑单篇精读，验证 evidence card 是否可用。 |

## 真实科研任务批次 2026-06-21：WiscKey + HotRAP

| 输入材料 | 提炼结论 | 转化产物 | 验证结果 | 下一步 |
|---|---|---|---|---|
| WiscKey 全文 PDF、HotRAP 全文 PDF、两篇 Obsidian 既有笔记、少量定向 related-work 元数据 | 普通 record-hot promotion 已被 HotRAP 覆盖；更有价值的问题是 repeated range hotness、value-only key-ordered extent、2 GB capacity admission、GC-assisted relocation 和 crash-safe mapping publication。GC 只能摊销部分 source read，不能视为零成本；逐 key index update 可能增加 WA。 | [真实任务验证报告](validation/real-task-hot-value-tiering-2026-06-21.md)；研究问题 council；双 vLog 系统草图；P0-P3 实验路线；v1.5 review；实验 skill 的 execution-readiness 修正规则。 | 文献精读 Pass；研究问题委员会 Pass；实验计划 Partial Pass。Rubric 15/16，缺少选定 codebase、设备、版本和可运行命令；未声明系统方法有效或 novelty 已确认。 | 建 systematic related-work protocol；先做 2 GB trace simulator；通过后实现 direct-pointer correctness MVP 和 crash tests。 |

## 学习与真实项目批次 2026-06-22：Goal Prompt 与对话压缩

| 输入材料 | 提炼结论 | 转化产物 | 验证结果 | 下一步 |
|---|---|---|---|---|
| 小红书短链 `7TV5moYC2gx`、公开 `goal-prompt-template-skill`、存储系统项目的最近四个会话、代码和结果摘要 | 短链 HTTP/HTTPS 均 404，不能提炼；公开 skill 中 outcome-first、默认假设、最少 blocker questions、inspection/repair gate 可迁移。真实项目证明：对话必须压成 session inventory、verified/model/unverified 分类、decision log、重复问题 cluster 和 context capsule；不能把模拟器规则写成硬件事实。 | 更新 `research-program-manager`、`research-knowledge-curator`、workflow、checklist、prompt templates、使用示例；新增 adversarial fixture/output、[验证记录](validation/goal-prompt-and-conversation-curation-2026-06-22.md) 和 v1.6 review；生成未公开的项目 handoff 并复制到目标项目 `docs/`。 | Goal compiler 与 conversation curation Pass；私有项目 audit 找到模型语义、机制归因、变体混杂、指标混用、runtime build 和版本管理问题。小红书内容为 Drop/待补材料。 | 在第二项目 A/B 验证减少追问与返工；为 storage 项目先固定 run manifest 和 request-level latency gate。 |

## 真实代码任务批次 2026-06-22：存储模拟器修复与实验守门

| 输入材料 | 提炼结论 | 转化产物 | 验证结果 | 下一步 |
|---|---|---|---|---|
| 存储模拟器 HP/LP timing 代码、latency1/2/3 wrapper、SQLite/FIO 脚本、静态测试、分析器和私有对话审计 | 模拟器调度必须声明 model boundary；p99 结论必须保留可复算 raw histogram 并检查 sample conservation；机制归因必须有非零 trigger/use counter；baseline/treatment 必须先通过 hash、flags、seed、workload 和 drain policy 的 run-manifest 比较。 | 更新 `reproduction-data-analyst`、`experiment-design-planner`；新增[真实代码验证](validation/real-task-storage-simulator-repair-2026-06-22.md)和 v1.7 review；目标项目新增模型 trace、严格 manifest、完整直方图、分析器测试和 runbook。 | 静态 invariants、合成模型、分析器、manifest unit test、Python/shell syntax 和单例 FIO dry-run Pass；目标 Linux module build/load/stress Pending，因此不声称 runtime/physical validity。 | 在目标 Linux 内核构建并加载模块；跑 canonical 四变体矩阵；只比较 compile/model/metric 三重契约均通过的 manifest，并保留 foreground/post-drain counters。 |

## 本批次沉淀出的能力

| 能力 | 触发条件 | 输入材料 | 执行步骤 | 输出格式 | 质量标准 | 失败时修正 |
|---|---|---|---|---|---|---|
| 外部笔记到 skill 提炼 | 收到一批经验帖、教程、评论讨论或参考材料 | 链接、截图、正文、评论、已有流程 | 采集可见内容；分离事实、方法、观点；判定是否值得 skill 化；抽取触发条件、输入、步骤、输出、验收、风险；写入进度记录 | 方法卡、skill 草案、workflow、checklist | 不抄原文；每条方法都有适用场景和限制；不可验证处标注 | 内容不足则只记录弱信号；评论不可读则不使用评论结论 |
| 可复现文献调研 | 用户要找 related work、做领域地图、scoping/systematic search 或审计 research gap | 中性研究问题、范围、时间/语言/数据库限制、种子论文、已有 query | 写 protocol；建 query families；记录 query log；分阶段筛选；按 DOI 去重；保留冲突/null；审计 gap；交接精读队列 | Literature Landscape Report、query/screening/dedupe log、evidence landscape、gap audit、reading queue | 检索可复现；不做 confirmation-only；abstract-only 降级；gap 与覆盖范围绑定 | 太宽则缩一个维度；太少则扩同义词/数据库/citation chaining；一个查询没命中不能声称无研究 |
| 文献证据精读 | 用户要读论文、综述、写 related work、做科研知识库 | PDF、Zotero 条目、DOI、补充材料、用户研究问题 | preflight；全文和图表检查；生成证据卡/方法卡/变量表；人工确认后入库；跨文献整合 | 单篇精读包、Obsidian 笔记、证据矩阵 | 证据必须有页码/图表/表格定位；不只写摘要；结论和证据分离 | 任务过大则缩到单篇单问题；全文缺失则先补源；证据不足则停止入库 |
| 研究问题委员会 | 需要判断选题、假设、实验设计或投稿策略 | 研究方向、已有文献、限制条件、候选问题 | 5 角色审议；互相挑战；删除弱论点；输出最终裁决和下一步 | 角色意见、争议点、最终问题、实验建议 | 最终建议要可实验、可证伪、可落地；不确定处说不知道 | 角色意见泛泛则要求引用材料证据；问题太大则缩小对象和变量 |
| 实验设计规划 | 用户要设计实验、复现、ablation、benchmark 或 pilot | 假设、数据、方法、基线、指标、约束、风险优先级 | 定义假设/反假设；列变量和混杂；设 primary/guardrail metrics；规划最小可信实验；写复现记录和决策规则 | 实验计划、变量表、指标表、运行计划、决策规则、复现记录 | 假设可证伪；主指标预先定义；guardrails 覆盖可能伤害；冲突指标有决策规则 | 实验过大则缩小；指标冲突则不平均掉；数据弱则先审计；复现缺失则先补 run log |
| 代码复现与数据分析核验 | 用户要复现论文代码、审查数据分析、比较本地指标和论文结果 | 论文目标表/图/指标、repo、脚本、notebook、数据版本、环境、日志、输出路径、容差、缺失值和分组键 | 定义复现/分析目标；审 repo/env；审数据版本、split、missingness、exclusion、leakage；跑最小命令；比较 target/local/delta/tolerance；排查 mismatch；写复现记录 | 复现/数据分析报告、preflight 表、run log、metric comparison、mismatch/leakage triage、reproducibility record | 每个指标有命令/config/data/output；容差明确；不把 mismatch 写成成功；不把 p 值/AUC 当充分证据；先 smoke test 或最小诊断 | 目标不清则先问；数据未知先 manifest；依赖失败先记录；结果不符一次只排查一个原因；泄漏或缺失值未解决则不报告最终 claim |
| 科研写作综合 | 用户要从证据卡、论文笔记或实验结果写综述、论文段落、审稿回复或投稿材料 | 证据卡、方法卡、实验结果、目标文本类型、目标期刊/会议、限制和冲突证据 | 先审证据；建 claim hierarchy；写可追溯草稿；保留冲突和局限；生成 traceability map；列删除/弱化声明 | 证据审计、claim hierarchy、草稿、traceability map、删除/弱化声明、最终清单 | 实质性声明必须有来源；不发明引用；不过度新颖性/因果声明；pilot 不写成定论 | 用户要求强写法时拒绝 overclaim；缺证据则列 gap；冲突证据条件化综合 |
| 投稿准备审查 | 用户要投稿、发预印本、交 camera-ready、写 rebuttal 或 revision | Manuscript、figures、tables、supplement、实验日志、证据卡、目标 venue 规则、reviewer comments | 明确 submission scope；审 claim-evidence；审 figure/table；审 reproducibility、anonymity、page limit、data/code availability；审 reviewer response；给出 ready/minor/major/blocked | Submission Readiness Review、findings、claim-evidence map、figure/table audit、compliance checklist、next actions | findings 先于润色；每个 blocker 有位置/路径/规则依据；unsupported claim 和 venue blocker 不能进入 ready | venue 规则缺失则标 unresolved；证据路径缺失则不批准 claim；匿名/页数/复现缺口先修复再 polish |
| 科研知识库整理 | 用户要整理 Obsidian/Zotero、论文卡、证据卡、实验卡、文献矩阵或项目索引 | PDF、Zotero/BibTeX、已有笔记、证据卡、实验日志、截图、评论、目标 vault 结构 | 定义整理范围；审 source quality；选择 note type；规范 metadata；去重和保留冲突；先写 note plan；输出 handoff | Research Knowledge Curation Report、source audit、note plan、claim registry、dedupe/conflict log、write queue、review queue | 证据优先而非摘要堆积；abstract-only 不进强证据；重复和冲突显式处理；下一轮可从 queue 接续 | 结构缺失先提 schema；来源太多先抽样；证据定位缺失入 review queue；遵守已有 vault 约定 |
| 长期科研计划管理 | 目标跨天、跨工具、跨论文/实验/写作阶段，或需要持续追踪 | 完整目标、完成标准、workspace、progress、handoff、日志、约束、blockers | 固定 charter；逐项 evidence audit；建 milestones；维护单一 active queue；记录执行/决策/blocker；阶段 review 和 handoff | Research Program Status、requirement audit、milestones、work queue、execution/decision log、risks/blockers、next session | 目标不漂移；进度有权威证据；只有一个 in-progress；complete/blocked 不提前；下一会话可恢复 | 活动过多缩 active queue；证据弱查真实 artifact；scope drift 删除；blocker 记录次数和升级阈值 |
| 科研任务 handoff/review | 任务跨天、跨工具、跨 PR，或需要 ChatGPT/Codex 协作 | repo、任务目标、改动 diff、实验日志、数据文件路径 | 建分支；限定范围；执行；写 handoff；独立审查；用户拍板 | `docs/handoff/latest.md`、任务记录、PR/review 清单 | diff 可审查；未改内容写清楚；风险和下一步明确 | 范围不清先问；误改无关模块则回退本任务改动；二进制走外部通道 |

## 待验证问题

- 评论区无法无登录读取，是否由用户提供截图或复制评论后纳入下一轮。
- `literature-evidence-reader` 已通过两篇真实 PDF 的全文、图表和方法验证；仍需在有 supplement/code 的论文上验证跨材料追踪。
- `research-question-council` 已在真实选题上完成压力测试；仍需比较是否真的优于普通 brainstorm，指标包括问题新颖性、可证伪性、实验成本和证据一致性。
- `experiment-design-planner` 已在真实系统代码中验证 manifest、模型 trace 和机制计数设计；目标内核 runtime 尚未执行，仍不能判为完整 execution pass。
- `reproduction-data-analyst` 已在真实代码修复中通过静态、分析器、manifest 和 dry-run 验证；仍需目标 Linux module build/load/stress 和真实四变体结果。
- `research-knowledge-curator` 和 `research-program-manager` 已通过一组真实多会话项目；仍需在独立项目复跑，检查是否真能减少追问和返工。
- 长期任务 handoff 是否适合非代码科研任务，需要用一次数据分析或文献综述任务试跑。
- 最小 eval fixture 已完成同会话 smoke eval 并拆分为独立输出文件，但尚未由独立会话逐项执行；下一步应独立重跑 13 个 fixture 并记录评分。

## 下一步计划

1. 围绕 dual-vLog、range-aware tiering 和 hot value relocation 运行 `literature-landscape-researcher`，验证 query syntax、筛选、citation chaining 和 gap audit。
2. 为 2 GB fast tier 建 trace-level simulator，验证 stable hotspot、capacity overflow、shifting range 和 sequential flooding。
3. 在目标 Linux 主机执行 storage simulator module build/load、并发 stress 和四变体严格 manifest 对比。
4. 用一个真实 notebook/CSV 运行 `reproduction-data-analyst`，验证缺失值、泄漏和敏感性分析检查是否足够具体。
5. 用一个真实论文草稿或投稿包运行 `submission-readiness-reviewer`，验证 blocker 检查是否比单纯润色更有用。
6. 用一个真实 Obsidian/Zotero 写入任务运行 `research-knowledge-curator`，验证 frontmatter、backlinks、write queue 和 review queue 是否可维护。
7. 对 Goal Brief 做 A/B，记录首次执行追问数、返工数和可验证完成率。
8. 下一批小红书笔记继续按本表五栏追加，不覆盖旧结论。
