# Fixture: XHS Batch Minimal

## Input Notes

### Note A

标题：用 AI 做论文阅读不要一口气全自动

正文：我试过把 40 篇 PDF 全部丢给 AI，让它自动总结并写进 Obsidian。结果 token 爆炸，很多只读了摘要，图表和 supplement 根本没看。后来改成每次只读 1 篇，先做 preflight，确认全文、图表、补充材料都可读，再生成证据卡和方法卡。人工确认后才入库。效果比批量摘要好很多。

评论摘录：有人建议把“需要人工审核”改成具体检查项，比如“Figure 2 是否支持主结论”“Table 1 的样本量是否匹配方法”。

### Note B

标题：我的 AI 科研效率提升 100 倍

正文：多用 AI，多总结，多坚持，效率就会越来越高。

评论摘录：无。

### Note C

标题：跨天任务要写 handoff

正文：做复现实验时，每晚写 5 行 handoff：今天改了什么、跑了什么命令、结果放哪里、哪里失败、明天先做什么。第二天不用重新翻聊天记录。

评论摘录：最好把随机种子、数据版本和环境也写进去。

## Expected Evaluation Focus

- Note A should become a Keep method for `literature-evidence-reader`.
- Note B should be marked Weak signal or Drop.
- Note C should become a Keep method for `research-handoff-review`.
