# Fixture: Handoff Minimal

## User Request

使用 `research-handoff-review` 结束本轮任务。

## Task State

目标：建立文献综述证据矩阵。

本轮已完成：

- 读取 5 篇论文摘要和 2 篇全文。
- 创建 `notes/evidence_matrix.md`。
- 创建 `notes/paper_cards/paper_a.md` 和 `notes/paper_cards/paper_b.md`。
- 运行命令：`python scripts/extract_pdf_text.py papers/a.pdf`。

未完成：

- 还有 3 篇只有摘要，未下载全文。
- `paper_b.md` 中 Figure 3 的结论还没有定位页码。

风险：

- 目前 related work 草稿可能过度依赖摘要。
- 数据集名称在两篇论文中写法不一致。

## Expected Evaluation Focus

- Handoff should let a new session continue without reading the chat.
- Review should flag abstract-only evidence and missing Figure 3 location.
- Next step should prioritize full text retrieval or evidence repair before writing prose.
