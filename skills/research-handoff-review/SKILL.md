---
name: research-handoff-review
description: Use for long-running research tasks that need Codex handoff, GitHub PR review, independent subagent-style review, experiment logs, branch hygiene, or staged human approval. Trigger when work spans multiple sessions, files, tools, or agents.
---

# Research Handoff Review

## Trigger

Use this skill when a research or coding task spans multiple turns, involves code/data/docs changes, needs review, or risks losing state across ChatGPT, Codex, GitHub, Obsidian, Zotero, or local files.

## Inputs

- Task objective and allowed scope.
- Repo or workspace path.
- Changed files, experiment outputs, data paths, and logs.
- Review target: code, analysis, paper notes, workflow, or writing.
- Any existing `docs/handoff/` files.

## Procedure

1. Start clean:
   - Inspect current state and existing uncommitted changes.
   - Define allowed files and forbidden files.
   - If using Git, work on a task branch and never directly mutate main for a task.
2. Execute narrowly:
   - Keep changes inside the task boundary.
   - Avoid committing binaries, secrets, `.env`, personal data, or large generated artifacts unless explicitly intended.
3. Write handoff:
   - What changed.
   - What did not change.
   - Commands or analyses run.
   - Evidence or outputs produced.
   - Known risks and open questions.
   - Next recommended action.
4. Independent review:
   - Use a fresh review stance for bug/risk/quality gaps.
   - Review diff, handoff, logs, and task objective.
   - Return findings first, then residual risk.
5. Decision:
   - User or lead agent chooses merge, revise, pause, or discard.
   - Update latest handoff after revision.

## Output Format

```markdown
# Handoff

## Objective

## Scope
- Changed:
- Intentionally not changed:
- Out of scope:

## Evidence
- Commands:
- Outputs:
- Source material:

## Review Notes
- Findings:
- Residual risk:

## Next Step
```

## Quality Standards

- Handoff lets a fresh agent resume without reading the whole chat.
- Review uses a clean context and is not self-congratulatory.
- Every produced artifact has a path or source reference.
- Git scope is explicit; no blind `git add .`.
- Long-running tasks have a stop condition and next checkpoint.

## Failure Repair

- If scope is unclear, stop and ask one concise question before editing.
- If too many files changed, split task or create separate handoffs.
- If review finds unrelated changes, do not revert user work; isolate your own changes.
- If the handoff is too vague, rewrite it with concrete file paths, commands, outputs, and unresolved risks.
- If automation increases manual burden, simplify the toolchain and remove unnecessary handoffs.
