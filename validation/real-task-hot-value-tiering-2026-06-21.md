# 真实科研任务验证：面向范围扫描的分层 Value Log

日期：2026-06-21
状态：选题可继续，需先完成 trace-level pilot 和系统原型
暂定名称：RangeTier-VLog，仅用于讨论，不代表最终系统命名

## 1. 决策摘要

**可以做，但不能把贡献写成“把热 value 从慢层搬到快层”。** HotRAP 已经实现 record-level hotness tracking、retention 和 promotion。更有区分度且被两篇论文共同支持的方向是：

> 在 key/value 分离的 tiered LSM 中，识别被重复范围扫描的 hot key ranges，把这些范围的 values 按 key 顺序组织成 fast-vLog extents，并用容量感知的 admission、demotion 和 GC 协同机制降低慢层访问，同时限制额外写放大。

建议把核心贡献限定为三点：

1. **Range-aware hotness**：跟踪重复范围扫描，而不是只跟踪随机 point-hot keys。
2. **Value-only, key-ordered promotion**：只移动 values，并在快层按 key 顺序形成连续 extent；这区别于把完整记录重新送入 LSM compaction 路径。
3. **GC-aware relocation with correctness protocol**：利用 GC 已经发生的读搬迁机会，但通过 copy-persist-validate-publish-reclaim 顺序保证并发更新和崩溃一致性。

初步判断是：工程可行，研究问题可证伪；**新颖性仍未确认**。本轮只做了两篇种子论文和少量定向 related-work 边界检查，不能替代系统性文献调研。

## 2. 输入与 Preflight

| 材料 | 可用性 | 本轮用途 | 限制 |
|---|---|---|---|
| WiscKey 全文 PDF | 全文、图、表可读 | value separation、range query、vLog GC、write amplification | 未检查原始代码和补充材料 |
| HotRAP 全文 PDF | 全文、图、表可读 | tiered LSM、热度跟踪、promotion、concurrency、scan limitation | 未运行作者实现 |
| 两篇 Obsidian 既有笔记 | 可读 | 对齐用户已有理解和研究动机 | 只作为导航，不作为论文证据 |
| 定向 related-work 元数据 | 可读 | 检查 PrismDB、MirrorKV、Range Cache 等近邻边界 | 不是系统性检索，不能支持“首次”声明 |

阅读目标：判断该方向是否值得做，并形成一份能直接进入 pilot 的研究问题和实验计划。

## 3. 论文证据卡

### 3.1 WiscKey

来源：[WiscKey, FAST 2016](https://www.usenix.org/conference/fast16/technical-sessions/presentation/lu)

| Claim | Evidence Location | Method/Data | Result | Limitation | Confidence |
|---|---|---|---|---|---|
| 将 keys 和 value locations 留在 LSM、values 写入独立 vLog，可显著降低大 value 工作负载的写放大 | PDF p.6, Section 3.2, Figure 4 | 16 B key、1 KB value 的示例模型 | 示例有效 WA 为 1.14 | 不包含新增 tier migration、双 vLog GC 和 pointer update 成本 | 高 |
| value separation 使 range query 访问无序 vLog，原本的顺序读取退化为随机读取 | PDF p.7, Section 3.3.1 | LSM iterator 返回 keys 后按 value address 取值 | 需要利用 SSD 并行随机读和预取缓解 | 对慢盘或 value 较小场景不一定有效 | 高 |
| WiscKey 用连续 iterator 访问检测和多线程预取优化 range query | PDF p.7, Section 3.3.1 | 识别连续 key-value 请求，后台线程并行读取 | 在合适 value size 和 SSD 上提升扫描性能 | 仍没有恢复 value 的 key-order physical locality | 高 |
| vLog GC 从 tail 读取 chunk，用 LSM 当前映射判断 value 是否仍有效，再把 live values 追加到 head | PDF pp.7-8, Section 3.3.2, Figure 5 | head/tail circular log、validity lookup | 回收 overwritten/deleted value 空间 | live-value copy 会产生额外 I/O | 高 |
| GC 的安全顺序要求先追加并持久化 value，再同步更新 LSM 中的新地址，最后回收旧空间 | PDF p.8, Section 3.3.2 | append, fsync, address/tail update, reclaim | 崩溃时避免索引指向未持久化 value | 双层搬迁仍需版本检查和跨 log 恢复协议 | 高 |
| 大 value 下 WiscKey 的 random-load WA 接近 1 | PDF p.10, Figure 10 | 10 GB random load，不同 value sizes | WiscKey 随 value 变大趋近 1，LevelDB 仍较高 | 是单 vLog、单设备结果 | 高 |
| range-query 收益强依赖 value size 和装载顺序 | PDF p.11, Figure 12 | random-loaded 与 sequentially-loaded DB | 较大 value 时可明显优于 LevelDB；64 B 时可能显著更差 | 说明小 value 是重要负对照 | 高 |
| GC 吞吐受 live-data 比例影响 | PDF p.11, Figure 13 及 Section 4.1.3 | 4 KB KV，不同 free-space ratios | 含 live copy 时吞吐下降更明显 | 不能假设“GC 顺便搬迁”没有成本 | 高 |

### 3.2 HotRAP

来源：[HotRAP, USENIX ATC 2025](https://www.usenix.org/conference/atc25/presentation/qiu)

| Claim | Evidence Location | Method/Data | Result | Limitation | Confidence |
|---|---|---|---|---|---|
| HotRAP 已经在 tiered RocksDB 中实现 record-level hotness tracking、retention 和 promotion | PDF pp.4-6, Sections 2-3, Figure 2 | RALT、promotion buffer、hotness-aware compaction、promotion by flush | 热 records 可留在或回到 fast disk | 因此“热 value 提升”本身不是充分创新 | 高 |
| RALT 只存 key、value length 和 hotness/tick，不存 value，并支持 key-range scan 和 range hot-size estimate | PDF pp.5-7, Sections 3.1-3.3 | 小型 on-disk LSM | range estimate 用于 compaction cost-benefit | 不是对 scan workload 的 hot-range admission | 高 |
| promotion by flush 把慢层访问到的热 record 批量 flush 到 L0 | PDF pp.5-6, Figure 2 | 默认 64 MiB promotion buffer | 比仅依赖 compaction 更快地提升热点 | 会留下慢层副本，后续仍需 compaction 合并 |
| promotion 需要处理旧版本覆盖新版本的竞态 | PDF p.8, Sections 3.5-3.6, Figure 4 | SSTable 状态检查、superversion snapshot、immutable memtable 标记 | 避免 stale record 被重新提升并遮蔽新值 | 双 vLog 设计也必须有等价的 version check | 高 |
| 热数据保留和提升会增加 FD/SD compaction，不保证降低总写放大 | PDF p.9, Section 3.8 | 根据 cold fraction 和 level size ratio 建模 | 可通过参数调节成本 | 用户提出的“降低 WA”必须作为待验证假设 | 高 |
| 不做 hotness check 会在 uniform workload 下产生灾难性 promotion/compaction 流量 | PDF pp.12-13, Section 4.5, Table 4 | ablation | no-hotness-check 的 promotion 和 compaction 远高于 HotRAP | admission policy 是核心，不是附属优化 | 高 |
| Fast-tier hit rate 和收益受 hot-set 是否超过 fast-tier capacity 约束 | PDF pp.9-13, Sections 4.1-4.5 | 100 GB SD、10 GB FD、1 GB memory | hotspot 小于容量时收益高，超过容量时下降 | “2 GB 快层”必须按数据集比例和 GC headroom 解释 | 高 |
| HotRAP 没有优化 scan workload | PDF p.14, Section 5 | scanned records 不进入 RALT/promotion buffer | 行为与 RocksDB-tiering 相同 | 这是本课题最直接的缺口证据 | 高 |
| 论文把“维护 promoted ranges，使 scan 避开 SD”列为 future work | PDF p.14, Section 5 | 讨论性主张 | 明确提出 range promotion 方向 | future-work 句子不等于该问题尚无其他研究 | 高 |
| auto-tuning 假设 hot records 被随机访问，sequential flooding 可能失效 | PDF p.14, Section 5 | 依赖采样间隔参数 | 一次性顺序扫描可能不被正确捕获 | 新方案必须有 repeated-reuse 门槛和 flood guard | 高 |

## 4. 方法卡与边界

| Method Step | Inputs | Assumptions | Parameters | Repro Notes |
|---|---|---|---|---|
| Key/value separation | key、value、LSM index、vLog | value 足够大，减少 value compaction 的收益大于额外 lookup | value size threshold | 先用 1 KiB/4 KiB，64 B 作为负对照 |
| Point-hot tracking | key access stream | 热点会被重复 point access | decay、sample interval、hot threshold | HotRAP 已覆盖，不能作为主贡献 |
| Range-hot tracking | scan start/end、bytes、time | 热范围会被重复扫描 | range granularity、decay、minimum reuse | 需要区分一次性全表扫与稳定重复范围 |
| Range promotion | selected key range、slow-vLog records | 快层能容纳稳定 hot range | extent size、batch size、admission threshold | value 应按 key 顺序写入 fast extent，不能只做散点 copy |
| Pointer publication | destination location、value version | index update 可原子提交或有 generation indirection | batch size、manifest generation | 必须先 persist destination，再 publish mapping |
| GC-assisted relocation | slow/fast GC candidate、hotness | GC 已经支付 source read 的一部分成本 | live ratio、buffer budget、GC headroom | range values 可能需暂存并按 key 排序，不能声称零成本 |
| Cold eviction | capacity pressure、decayed score | temperature 有滞后，避免频繁抖动 | high/low watermarks、hysteresis | 预留 10%-15% 快层空间给 GC 和 in-flight promotion |

## 5. Related-Work Gap Audit

本轮定向检查只支持“需要进一步检索”，不支持“首次提出”。

| 近邻工作 | 已覆盖 | 与本题仍可能不同 |
|---|---|---|
| HotRAP | record-level heat、fast-tier retention/promotion、并发控制 | 明确不处理 scan workload；没有 key-ordered fast-vLog extent |
| PrismDB | hot record tiering、compaction-driven promotion | 仍沿 LSM/tier compaction 路径，不等于 value-only range layout |
| MirrorKV | key/value 分离、hot blocks/SSTables 的 hybrid placement | granularity 更粗；需核对是否已有 range-contiguous value promotion |
| Range Cache | LSM range-query cache | 主要是 memory cache；与持久化 fast-vLog、GC 和 write amplification 目标不同 |
| WiscKey family / blob KV stores | value separation 和 vLog/blob GC | 需系统检索是否已有 dual-vLog、hot value relocation、range-aware layout |

提交论文前必须补做：forward/backward citation chaining、`dual value log`、`tiered value log`、`hot value relocation`、`range-aware LSM`、`blob tiering`、`hybrid SSD HDD KV` 六组 query family，并逐篇核对机制粒度。

## 6. Research Question Council

### Decision Being Made

决定该想法应继续、收窄、转向还是停止，以及最小研究单元是什么。

### Role Findings

| Role | Strongest Point | Concrete Risk | Repair |
|---|---|---|---|
| Opponent | HotRAP 已经做热 record promotion | 只换成“value”可能被认为是直接拼接两篇论文 | 把问题限定到 repeated range scans、key-order extent 和总 WA 边界 |
| First-principles analyst | 性能收益来自减少 slow bytes 和恢复 value locality，不是“热”这个标签 | 单 key pointer update 可能制造新的 LSM WA | 同时比较 direct pointer 与 range manifest/generation indirection |
| Expander | GC source read 可用于发现和搬迁 hot live values | GC tail 顺序通常不是 key 顺序，直接 piggyback 会破坏 scan locality | GC 只负责候选发现/读取摊销，range buffer 负责排序成 extent |
| Outsider | 2 GB 是明确资源约束，可形成容量敏感研究 | 不说明 DB size、热集大小和 reserve，2 GB 没有可比意义 | 报告 `C_fast / DB_size`，并扫 0.5x/1x/2x hot-set capacity |
| Executor | 可以先做 trace simulator，无需先改完整 RocksDB | 一上来改 storage engine 会把选题验证变成长期工程 | 先验证 admission、churn、migration bytes 和理论收益，再做最小原型 |

### Candidate Questions

评分为 1-5；总分依次覆盖 novelty、evidence grounding、feasibility、falsifiability、expected contribution、readiness。

| Question | Scores | Total | Decision |
|---|---|---:|---|
| Q1: 热 key 被访问时，将 value 从 slow vlog 提升到 fast vlog，是否提高性能？ | 2/5/4/4/2/4 | 21/30 | 拒绝为主问题：HotRAP 已覆盖大部分机制 |
| Q2: 重复范围扫描驱动的 key-ordered value extent promotion，能否在有限快层中降低 slow-tier bytes，同时限制总 WA？ | 4/5/3/5/5/3 | 25/30 | 继续并收窄：主问题 |
| Q3: 在 vLog GC 时顺便做冷热搬迁，能否降低额外 promotion I/O？ | 3/4/3/5/3/3 | 21/30 | 保留为机制与 ablation，不单独成题 |
| Q4: 用 range manifest 替代逐 key pointer update，能否降低 promotion-induced index WA？ | 4/4/3/5/4/2 | 22/30 | 作为第二阶段优化，先做 correctness baseline |

### Final Verdict

- Decision：**Narrow and continue**。
- Chosen question：在 key/value 分离的 tiered LSM 中，针对重复扫描的 hot key ranges，key-ordered value-only promotion 是否能在 2 GB fast tier 下显著降低 p95 range-scan latency 和 slow-tier read bytes，同时把 total physical write amplification 控制在预设 guardrail 内？
- Rejected option：只做 point-hot value promotion，因为与 HotRAP 的差异不足。
- Secondary question：GC-assisted relocation 与 range manifest 是否分别减少 promotion read cost 和 index WA？

## 7. 可证伪假设

| ID | Hypothesis | Failure Alternative |
|---|---|---|
| H1 | 对稳定重复范围扫描，range promotion 会降低 p95 normalized scan latency 和 slow-tier bytes | 热范围复用不足，promotion 成本高于后续读取节省 |
| H2 | key-ordered extent 优于逐 key 散点 promotion | 快设备随机读已足够快，重排和批量 publish 成本反而更高 |
| H3 | GC-assisted source reading 会降低额外 promotion read bytes | GC 时机与热范围不匹配，等待 GC 导致提升太晚 |
| H4 | range manifest/generation indirection 会降低 index WA | 额外 lookup、metadata recovery 和 cache miss 抵消写入收益 |
| H5 | admission + hysteresis 能在 hot set 超过 2 GB 或发生 sequential flooding 时限制 churn | 方案出现反复升降级，fast tier 被一次性扫描污染 |

## 8. 系统草图

### 8.1 数据布局

```text
Key LSM / Range Directory
  key -> {value_version, tier, segment_id, offset, length, checksum}
                    |
       +------------+-------------+
       |                          |
Fast vLog / range extents    Slow vLog
2 GB budget                 bulk cold values
key-ordered promoted data   append + GC
```

两种 mapping 方案都应实现并比较：

1. **Direct pointer MVP**：每个 key 的 index value 指向新 tier/location。实现直接，但 range promotion 会产生大量 index updates。
2. **Range manifest**：发布 `range_id -> fast segment + generation`，key index 保留版本或 fallback pointer。它可能减少 LSM 写入，但增加 lookup、恢复和 snapshot 复杂度。

### 8.2 Range Hotness 与 Admission

建议先使用固定 range/segment，再考虑自适应合并：

- 观测：scan start/end、returned bytes、slow-tier bytes、完成时间、reuse interval。
- 热度：recency-decayed scan reuse，不以一次 scan 的字节数直接判热。
- admission：仅当预期未来 slow-read saving 大于 promotion、metadata、GC 和 capacity opportunity cost 时进入快层。
- flood guard：至少两次独立 reuse，或 ghost history 命中后才提升；一次性 full scan 不得直接填满快层。
- extent：按 key 顺序批量写入，而不是沿旧 vLog offset 顺序复制。
- hysteresis：promotion 与 eviction 使用不同阈值，避免临界热点反复迁移。

### 8.3 2 GB Capacity Policy

- 报告绝对容量 2 GB，同时报告 `C_fast / DB_size`。
- pilot 先用 20 GB DB，使快层比例为 10%，与 HotRAP 的 10 GB/100 GB 量级可比。
- 快层 occupancy high watermark 先设 85%-90%；其余空间留给 GC、in-flight extent 和 crash recovery。
- hot range working set 扫描 0.5 GB、1 GB、2 GB、4 GB，覆盖低于、等于和高于容量。
- eviction 优先按 benefit density，而不是只按 LRU：预计节省的 slow bytes / 占用字节。

## 9. GC 与一致性

### 9.1 回答“GC 时刚好搬迁吗”

**可以协同，但不能把 GC 搬迁当成免费优化。**

- Slow-vLog GC 已经读取 tail chunk，可以复用这次 source read 来识别 live hot values。
- 但 tail chunk 的记录顺序通常不等于 key 顺序。若直接逐条写 fast-vLog，range scan 仍会变成散点读取。
- 因此更合理的设计是：GC 负责 source-read amortization 和候选发现，候选进入 bounded range buffer；buffer 按 key 排序后生成 fast extent。
- 如果等待 GC 会错过热度窗口，则必须允许 eager promotion。GC-assisted 是一条路径，不应是唯一触发器。

### 9.2 安全发布顺序

对每个 value version 或 range generation：

1. Copy：把目标 values 写入 destination vlog/extent。
2. Persist：`fsync` destination data 和必要 metadata。
3. Validate：核对 key 的当前 value version；若并发更新已发生，放弃发布该旧版本。
4. Publish：用原子 WriteBatch 或 range manifest generation 发布新映射。
5. Reclaim：只有在新映射可恢复后，旧副本才能由 GC 回收。

崩溃状态应满足：

- 在 publish 前崩溃：destination 只是 orphan，由 GC 清理，读仍走旧映射。
- publish 后、reclaim 前崩溃：存在重复副本，但新映射可读。
- reclaim 后崩溃：WAL/manifest 必须能恢复已经发布的新映射。

并发更新测试必须覆盖：promotion copy 期间 update、publish 前 delete、snapshot scan 跨 generation、fast/slow GC 与 foreground write 同时发生。

### 9.3 Demotion

- 若 slow 层仍保留同版本副本，可先切回 slow mapping，再删除 fast replica。
- 若 slow 副本已回收，必须先 copy-persist-validate-publish 到 slow，再回收 fast value。
- 为降低 space amplification，可以采用“短暂 replica-first，稳定后 move semantics”，不能永久保留所有 slow replicas。

## 10. Write-Amplification 模型

不要只报告 LSM compaction WA。至少拆为：

```text
WA_total = WA_key_lsm
         + WA_user_value_append
         + WA_promotion_copy
         + WA_fast_gc
         + WA_slow_gc
         + WA_mapping_update
         + WA_demotion
```

还应分别报告 fast-tier device WA proxy 和 slow-tier physical bytes written。预期降低的是 value 参与 LSM compaction 的写入，以及读取侧 slow bytes；promotion 不会天然降低 `WA_total`。

## 11. 最小可信实验

### 11.1 Decision

- Hypothesis：Q2/H1-H5。
- Null：范围复用不足、capacity churn 或 mapping/GC 写入使总成本不优于 baseline。
- Decision enabled：continue to prototype、revise admission/layout，或停止该方向。

### 11.2 Baselines 与 Treatments

| Component | Choice | Rationale | Risk |
|---|---|---|---|
| B0 | WiscKey-style single slow vLog + parallel prefetch | value separation 基线 | 旧实现环境可能难复现 |
| B1 | Static two-tier：key index 在快层、全部 values 在慢层 | 隔离设备 tiering 的自然收益 | 不含 promotion |
| B2 | HotRAP / tiered RocksDB，可运行时纳入 | record-level promotion 对照 | 架构不同，需避免不公平配置 |
| B3 | Range Cache 或 RocksDB row cache proxy | range caching 对照 | memory cache 与 persistent tier 目标不同 |
| T1 | Per-key hot value promotion | 验证“只搬热 value” | 可能破坏 scan locality |
| T2 | Range-hot + key-ordered extent | 主 treatment | 需要排序和批量 publish |
| T3 | T2 + GC-assisted source read | 检验 GC 协同 | 热度窗口与 GC 时机不一致 |
| T4 | T2 + range manifest | 检验 mapping WA | lookup/recovery 复杂度高 |
| Oracle | 已知未来扫描的 ideal placement | 估计策略上限 | 不能作为可部署 baseline |

### 11.3 数据与工作负载

- DB：20 GB；fast value tier：2 GB；slow tier：其余 values；key index 位置固定并明确报告。
- Value sizes：1 KiB、4 KiB；64 B 作为 negative control。
- Scan lengths：100、1,000、10,000 keys，报告 returned bytes。
- Stable repeated ranges：hot set 0.5/1/2/4 GB。
- Shifting ranges：每固定操作数迁移热点，测 adaptation lag 和 churn。
- Sequential flooding：一次性大范围/full scan，验证不会污染快层。
- Mixed workload：scan + point read + update，至少包含 read-heavy 和 50/50 read-write。
- Point-hot control：验证新 range policy 不应显著破坏普通热点。
- 每个配置至少 3 个独立重复；固定并记录 seed，报告分布而不是只报均值。

### 11.4 Metrics

| Metric | Type | Pilot Threshold | Why |
|---|---|---|---|
| p95 normalized range-scan latency per returned MiB | Primary | 相对 B1 改善至少 1.5x | 直接回答 scan 目标；阈值是 pilot 决策值，不是文献事实 |
| slow-tier bytes read per returned byte | Co-primary diagnostic | 至少下降 50% | 区分真正避开慢层与并发掩盖 |
| total physical WA | Critical guardrail | 不超过 B1 的 1.15x | 防止用大量搬迁换读性能；15% 是初始预算 |
| promotion + demotion bytes | Guardrail | 单独报告 | 识别 churn |
| fast/slow GC bytes | Guardrail | 单独报告 | 检验 GC-assisted 是否真的摊销成本 |
| mapping/index bytes written | Guardrail | 单独报告 | 检验 direct pointer 与 manifest |
| p99 point-read latency | Guardrail | 不劣化超过 10% | 防止 range 优化伤害普通读 |
| foreground write throughput | Guardrail | 不劣化超过 10% | 检查 publish 和 GC 干扰 |
| fast-tier occupancy/headroom | Capacity | 不长期超过 high watermark | 保证 GC 和恢复空间 |
| stale-read/corruption/recovery failures | Correctness | 必须为 0 | 任何一次都阻止继续扩展 |

### 11.5 Ablations

1. 无 range heat，只用 point heat。
2. 无 key-order layout，只逐 key append。
3. eager promotion vs GC-assisted vs hybrid。
4. direct pointer vs range manifest。
5. 无 flood guard。
6. 无 hysteresis。
7. 不同 extent size 和 reserve ratio。

### 11.6 Decision Rules

- Continue：稳定重复范围下 primary 和 slow-byte 指标达标，关键 guardrails 全通过，且 correctness failures 为 0。
- Revise：只在 hot set 小于 2 GB 时有效；或 latency 达标但 WA/foreground guardrail 失败。优先调整 admission、extent、manifest 和 GC trigger，不平均掉冲突指标。
- Stop/Pivot：sequential flooding 持续污染快层；promotion/demotion 长期主导物理写入；range ordering 无显著收益；或 crash/concurrency 协议无法简洁验证。

## 12. 执行阶段

### P0: Trace-Level Simulator

输入 synthetic scan/update traces，先实现：range heat、2 GB capacity、admission、hysteresis、eviction、promotion/demotion byte accounting。输出 hit ratio、slow bytes、migration bytes、occupancy 和 churn。

完成标准：能复现 stable hotspot、capacity overflow、shifting hotspot 和 sequential flooding 四种行为，并用 oracle 给出上限。

### P1: Correctness MVP

实现双 vLog 和 direct pointer mapping；先不做 range manifest。加入 version check、copy-persist-publish-reclaim 和 crash injection。

完成标准：并发 update/delete、重启和 GC stress 下无 stale read/corruption。

### P2: Range Layout

加入 range buffer 和 key-ordered fast extents，对比 per-key append。

完成标准：证明收益来自 physical locality 或 slow-tier avoidance，而不是只来自更高并发。

### P3: GC 与 Mapping 优化

加入 GC-assisted path 和 range manifest，分别做 ablation。

完成标准：至少一个优化减少可归因的 physical bytes 或 index WA，且没有破坏 P1 correctness。

## 13. Skill 真实任务验收

| Skill | Result | Evidence | Gap |
|---|---|---|---|
| `literature-evidence-reader` | Pass | 两篇全文、图表、方法、限制和页码级 evidence cards；既有笔记未替代原文 | 未检查代码/supplement |
| `research-question-council` | Pass | 淘汰泛化问题，收窄为可证伪的 range-aware value-only tiering | novelty 仍需系统检索 |
| `experiment-design-planner` | Partial Pass | 假设、基线、变量、指标、guardrails、ablation、decision rules 已给出 | 尚无选定 codebase、设备清单和可运行命令 |

按包级 rubric 本轮为 **15/16**：来源可追溯、任务边界、方法、证据、研究问题和可复用沉淀均满足；实验复现性暂记 1 分，因为尚未确定实现仓库、硬件和命令。该结果足以进入 pilot，不足以声明方法有效。

## 14. 不应入库的声明

- “这是首次把热 value 放到快层。”
- “GC 顺便搬迁，所以没有额外写放大。”
- “2 GB 一定足够。”
- “范围热度一定比随机 key 热度更好。”
- “更新 key index 会降低写放大。”
- “HotRAP 不能支持 range query。”准确说法是：论文当前设计不对 scan workload 做热度跟踪或 promotion 优化。

## 15. Open Questions

1. 原型基于 WiscKey、RocksDB BlobDB/Titan、HotRAP fork，还是新的最小 KV harness？
2. 快层和慢层的真实设备是什么，带宽、IOPS、latency 和 endurance 约束如何？
3. range unit 用固定 key prefix、固定返回字节、learned boundary 还是 SST/extent boundary？
4. 快层 value 采用 move semantics、replica semantics，还是短暂 replica 后转 move？
5. scan snapshot 跨 range generation 时如何保证同一版本视图？
6. 目标是课程 project、硕士课题、系统论文，还是工程 prototype？这会改变 related-work 深度和实现规模。

## 16. Next Smallest Action

先做 P0 trace-level simulator，并行补一轮系统性 related-work protocol。只有当 simulator 在 stable range reuse 下显示可接受的 migration/WA 边界，且定向检索没有发现等价的 dual-vLog range promotion 机制，才进入完整 storage-engine 原型。
