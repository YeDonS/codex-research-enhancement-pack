# Eval Output: XHS Batch Minimal

Fixture: `evals/fixtures/xhs-batch-minimal.md`

Skill: `xhs-method-ingester`

## Source Access

| Source | Status | Notes |
|---|---|---|
| Note A | Readable | Includes note body and one useful comment |
| Note B | Readable | No useful comment |
| Note C | Readable | Includes note body and one useful comment |

## Method Extraction

| Source | Decision | Transferable Method | Steps | Scenario | Risk Limits |
|---|---|---|---|---|---|
| Note A | Keep | Stage literature reading before knowledge-base ingestion | 1. Read one paper first. 2. Run preflight for full text, figures, supplement. 3. Extract evidence cards and method cards. 4. Human-confirm cards before Obsidian ingestion. | Paper reading, literature review, evidence knowledge base | Batch automation causes token blowup and abstract-only notes; comments must become concrete checks, not generic “manual review” |
| Note B | Drop | None | None | None | Contains motivation only: no inputs, procedure, output, or validation |
| Note C | Keep | End each cross-day task with a compact handoff | 1. Record changed work. 2. Record commands. 3. Record outputs and failures. 4. Record next action. 5. Add seed, data version, and environment for experiments. | Reproduction, data analysis, long literature projects | Handoff is useless if it omits paths, commands, data versions, or unresolved risks |

## Converted Artifacts

Skill draft updates:

- `literature-evidence-reader`: reinforce single-paper preflight, evidence cards, method cards, and concrete figure/table checks.
- `research-handoff-review`: reinforce environment, seed, data version, output path, and next-action recording.

Workflow template updates:

- Single-paper ingestion before batch literature automation.
- Cross-day research task closeout with handoff and independent review.

Checklist updates:

- Replace “needs manual review” with named checks, such as figure support, table sample size, supplement availability, seed, data version, and command logs.

## Progress Row Draft

| 输入材料 | 提炼结论 | 转化产物 | 验证结果 | 下一步 |
|---|---|---|---|---|
| Fixture XHS batch: Note A/B/C | Note A and C are reusable; Note B is dropped as motivational only. Valuable methods are staged paper ingestion and compact task handoff. | `literature-evidence-reader`, `research-handoff-review`, workflow/checklist updates | Smoke eval pass: extracted 2 keep methods and 1 drop; comments were incorporated as concrete checks | Test with a real PDF and one cross-day task |

## Acceptance Result

| Criterion | Result |
|---|---|
| At least 2 methods extracted | Pass |
| At least 1 Weak signal or Drop | Pass |
| Skill/workflow/checklist artifacts present | Pass |
| Five-column progress row present | Pass |
