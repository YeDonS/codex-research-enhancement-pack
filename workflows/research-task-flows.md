# 科研任务流程模板

## 1. 文献调研流程

触发条件：用户要了解一个方向、写 related work、找 gap、准备开题或综述。

输入材料：研究主题、关键词、时间范围、目标领域、已有论文、排除条件。

步骤：
1. 定义中性研究问题和边界：对象、变量、方法、应用场景、时间跨度。
2. 在搜索前写 inclusion/exclusion、数据库、语言、日期和停止规则。
3. 建 query families，记录 exact query、日期、过滤器、命中数和 export。
4. 分阶段筛选并记录理由；按 DOI/title/year/authors 去重。
5. 保留正向、负向、null 和冲突结果，形成 evidence landscape。
6. 审计 gap claim：区分“本次没搜到”和“没有研究”。
7. 选 3-5 篇进入精读，不直接批量总结几十篇。
8. 生成 related work 骨架：主题簇、共识、冲突、候选缺口、本文切入点。

输出格式：search protocol、query log、screening ledger、dedupe log、evidence landscape、gap audit、精读候选。

质量标准：检索可复现；每个 gap 与覆盖范围绑定；不能只列论文名；abstract-only 和不确定来源单独标注。

失败修正：结果太散时缩小一个范围维度并记录 query revision；结果太少时扩展同义词、数据库和 citation chaining；证据不足时停止写 gap/综述。

## 2. 单篇论文精读流程

触发条件：用户提供 PDF/DOI/Zotero 条目，希望形成可入库知识。

输入材料：PDF、supplement、研究问题、目标输出位置。

步骤：
1. Preflight：全文、图表、表格、supplement、代码和数据链接是否可读。
2. 结构阅读：问题、方法、实验、结果、局限。
3. 证据卡：主张、证据位置、数据、结果、限制、可信度。
4. 方法卡：步骤、输入、参数、假设、复现难点。
5. 变量表：变量定义、测量方式、角色、混杂因素。
6. 入库决策：只把有来源定位、可复用的卡片写入知识库。

输出格式：Paper Reading Pack。

质量标准：不能只写摘要；必须检查图表和 supplement；关键结论有页码/图表/表格定位。

失败修正：读不完整时停止并列缺口；任务过大时只读方法或结果一节；输出摘要化时重跑证据卡。

## 3. 研究问题生成流程

触发条件：用户要选题、找创新点、改 hypothesis、决定实验方向。

输入材料：方向描述、已有文献、数据可用性、时间和能力限制。

步骤：
1. 收束目标：基础研究、应用、方法改进、复现、对比、综述。
2. 生成候选问题：每个问题必须包含对象、变量/机制、方法或数据、可观察结果。
3. Council 审查：反对者、第一性原理、扩展者、局外人、执行者。
4. 打分：新颖性、可证伪性、证据基础、可行性、贡献、风险。
5. 选择 1 个主问题和 1 个备选问题。
6. 定义下一步：补读论文、数据审计、最小实验或写作提纲。

输出格式：候选问题表、角色审查表、最终裁决、下一步任务。

质量标准：问题不能大到“研究某领域”；必须能被一个实验、数据分析或系统综述推进。

失败修正：如果问题太大，限定人群/数据集/变量/指标；如果没有数据，先做数据可得性审计。

## 4. 实验设计流程

触发条件：用户有研究假设，准备复现、对比实验、消融实验或数据分析。

输入材料：假设、数据、代码、指标、基线、资源限制。

步骤：
1. 写明假设和反假设。
2. 定义变量、处理、控制、混杂因素。
3. 确定数据来源、样本筛选、伦理/隐私限制。
4. 选基线、指标、统计方法和失败判定。
5. 设计最小可运行实验，不先跑全量。
6. 记录实验配置、命令、环境、随机种子、输出路径。
7. 复盘结果：支持、反驳、不确定、需要补实验。

输出格式：实验计划、运行日志、结果表、解释限制、下一轮实验。

质量标准：实验可复现；指标和假设匹配；失败标准预先定义。

失败修正：跑不动则降采样；指标不稳则补置信区间/重复实验；结果解释过度则回到证据表。

## 5. 数据分析核验流程

触发条件：用户要报告统计结果、审查 notebook/CSV、比较模型指标、判断一个显著结果或 AUC 是否可信。

输入材料：数据文件、notebook/script、输出表、变量定义、分组键、缺失值规则、排除标准、目标 claim。

步骤：
1. 定义分析目标：效应估计、预测、描述统计、复现论文表格或探索性分析。
2. 审数据单位和分组键：主体、样本、访问、时间、站点、实验 run 是否混用。
3. 审缺失值和排除规则：按处理组、结果、关键协变量、严重程度分层。
4. 审泄漏：label leakage、future leakage、重复主体 train/test leakage、派生特征泄漏。
5. 审指标解释：效应量、置信区间、p 值、AUC、calibration、subgroup 指标分别解释。
6. 设计最小诊断：missingness audit、grouped split、敏感性分析或 bounds。
7. 输出是否可报告、需弱化、需重跑或需停止。

输出格式：数据分析核验报告、风险表、敏感性分析计划、可报告 claim 和不可报告 claim。

质量标准：不能只看 p 值或 AUC；必须先确认缺失值、分组、泄漏和排除规则；预测和效应估计分开判断。

失败修正：目标不清则先问 estimand；数据单位混乱则先建数据字典；泄漏未排除则不解释模型指标；缺失机制不明则先做敏感性分析。

## 6. 投稿准备审查流程

触发条件：用户要投稿、发预印本、交 camera-ready、写 rebuttal、做 revision 或提交 supplement。

输入材料：论文草稿、figure/table、实验日志、证据卡、supplement、目标 venue 规则、rebuttal/comment 列表。

步骤：
1. 明确提交类型和 venue 约束：匿名、页数、格式、artifact、ethics、data/code availability。
2. 审 claim-evidence：abstract、introduction、contribution、result、conclusion 的强声明是否能追溯到证据。
3. 审 figure/table：编号、引用、caption、单位、样本量、置信区间、统计检验和输出路径。
4. 审 reproducibility：数据版本、代码、环境、命令、seed、超参、compute、availability statement。
5. 审 limitations 和 ethics：外部有效性、数据偏差、隐私、IRB、部署边界是否具体。
6. 审 reviewer response：每条评论是否有回应、改动位置和残余风险。
7. 给出 ready/minor/major/blocked 决策和最小修复清单。

输出格式：Submission Readiness Review、findings、claim-evidence map、figure/table audit、compliance checklist、next actions。

质量标准：先列 blocker 再润色；每个 blocker 有位置或规则依据；不能让 unsupported claim、匿名违规、复现缺口进入 ready 状态。

失败修正：venue 规则缺失则标为 unresolved；证据路径缺失则不批准 claim；页数/匿名违规先修复，再做语言 polishing。

## 7. 科研知识库整理流程

触发条件：用户要整理 Obsidian/Zotero、论文卡、证据卡、实验日志、文献矩阵、项目索引或长期知识库。

输入材料：PDF、Zotero/BibTeX、已有笔记、证据卡、实验日志、截图、评论、目标 vault 结构、命名和标签规则。

步骤：
1. 明确整理范围：主题、来源类型、目标文件夹、是否 ingest、cleanup、migration 或 review。
2. 审 source quality：全文、abstract-only、metadata-only、实验日志、弱信号、重复、冲突、drop。
3. 选择 note type：paper card、evidence card、method card、variable card、experiment card、claim record、index note。
4. 规范 metadata：title、authors、year、DOI/URL、source path、evidence level、review status、tags。
5. 去重与冲突处理：按 DOI/title/path 合并，冲突 claim 保留条件，不平均成单结论。
6. 先写 note plan，再小批量写入；每条写入有路径、来源、验收条件。
7. 输出 write queue、review queue、do-not-ingest 和下一轮维护任务。

输出格式：Research Knowledge Curation Report、source audit、note plan、claim registry、dedupe/conflict log、write queue、review queue。

质量标准：知识库是证据优先，不是摘要堆积；abstract-only 不进强证据；下一轮能从 queue 接续。

失败修正：结构缺失先提 schema；来源太多先抽样 triage；证据定位缺失则入 review queue；已有 vault 约定优先。

## 8. 长期科研任务管理流程

触发条件：任务跨天、跨工具、跨论文、跨代码仓库或需要周期性推进。

输入材料：总目标、阶段计划、昨天日志、当前文件、阻塞点。

步骤：
1. 固定完整目标和逐项 completion evidence，不按已有文件缩小成功标准。
2. 审计当前状态：proven、contradicted、partial、weak、missing、blocked。
3. 建里程碑：outcome、dependency、acceptance、risk、status。
4. Work queue 同时只保留一个 in-progress，当前轮选择 1-3 个可产出证据的动作。
5. 执行中记录输入、命令、改动文件、输出、验证和剩余不确定性。
6. 记录 decision log：证据、替代方案、owner、反转条件。
7. 记录 blocker occurrence、缓解动作和升级阈值；第一次出现不自动全局 blocked。
8. 结束时写 stage review、handoff、未解决问题和下一步可执行动作。

输出格式：program charter、requirement audit、milestones、work queue、execution log、decision log、risks/blockers、stage review、handoff。

质量标准：完整目标不漂移；进度绑定权威证据；只有一个 active task；下一次打开项目能直接执行；自动化减少重复解释。

失败修正：活动过多则缩 active queue 但保留完整目标；证据弱则检查真实 artifact/runtime；漂移任务必须映射 completion criterion；日志空泛则补路径/命令/证据/下一步。

## 9. 项目对话压缩与 Goal 编译流程

触发条件：项目跨多次 Codex/agent 对话，出现重复追问、相互矛盾的解释、散落的实验结论，或用户只给出一句模糊任务目标。

输入材料：会话导出或 thread IDs、项目目录、关键代码/日志/图表、当前目标、现有 handoff、是否允许直接修改目标项目。

步骤：
1. 先把粗略目标编译为 outcome、范围、交付物、完成证据、约束、合理假设和 approval gate。
2. 建会话清单：日期、主题、最终产物、被修改文件、未解决问题；不把 tool chatter 当知识。
3. 对每个重要结论回查代码、日志、命令或用户确认，将其标为 verified fact、model assumption、unverified claim、user decision 或 open question。
4. 将重复问题聚为一个 root-cause cluster；每组只保留 canonical answer、证据位置和下一项诊断。
5. 把相互冲突的解释写入 decision log，给出可反转条件；禁止用最后一次回答覆盖前面未验证的结论。
6. 输出不超过一页的 context capsule：目标、已证实状态、开放决策、当前 blocker、下一条命令或审计动作。
7. 若需要写入项目目录，先给 write plan；私有对话或路径不得混入公开 skill/repo。

输出格式：Conversation Curation Report、goal brief、issue register、decision/assumption log、repeated-question clusters、context capsule、handoff。

质量标准：下一会话只读 capsule 和链接的证据就能继续；结论不依赖聊天记忆；无证据的 assistant 解释不会升级为项目事实；只问真正阻塞执行的问题。

失败修正：如果压缩后仍有大量“为什么”，回到一个可观测量、一段代码或一条日志重新定位；如果修复路径会改变模型语义，先把它升级为 user decision，不直接改实现。
