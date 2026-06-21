---
name: xhs-method-ingester
description: Use when the user provides Xiaohongshu notes, comments, screenshots, or similar external experience posts and wants Codex to extract reusable methods, convert them into skills, research workflows, checklists, and maintain a progress record. Trigger for ongoing Codex capability improvement from external notes, especially research productivity methods.
---

# XHS Method Ingester

## Trigger

Use this skill when the user sends a batch of 小红书笔记, screenshots, copied comments, tutorials, or reference material and asks to improve Codex workflows, research workflows, skills, prompts, or long-term task management.

## Inputs

- Source links or screenshots.
- Visible note正文 and useful comments if available.
- User's target capability area, such as literature review, paper reading, research question generation, experiment design, writing, coding reproduction, data analysis, or knowledge management.
- Existing progress document if present.

## Procedure

1. Capture source status: record which links or images were readable, which comments were accessible, and which material is missing.
2. Extract transferable method units, not summaries. For each unit identify problem, method, steps, applicable scene, expected output, and risk.
3. Classify each method as one of:
   - Keep: concrete, reusable, and verifiable.
   - Rewrite: useful but too vague; needs a stricter trigger or output format.
   - Weak signal: relevant topic but lacks procedure.
   - Drop: motivational, duplicative, or unsafe.
4. Convert kept or rewritten units into at least three artifact classes:
   - Skill draft.
   - Research workflow template.
   - Acceptance or self-check checklist.
5. For every capability, write trigger, inputs, steps, output format, quality standards, and failure repair.
6. Update the progress table with exactly these columns: 输入材料, 提炼结论, 转化产物, 验证结果, 下一步.
7. Run a stage review: what improved Codex ability, what is generic advice, what should be deleted or rewritten.

## Output Format

Return or update:

- `progress.md`: batch log and next plan.
- `skills/<skill-name>/SKILL.md`: concise executable skill drafts.
- `workflows/*.md`: task flows for research use.
- `checklists/*.md`: validation checklists.
- `reviews/*.md`: stage review.

## Quality Standards

- Do not paste raw notes as the main artifact.
- Do not infer comments that were not accessible.
- Each capability must have a failure path.
- Each workflow must produce auditable artifacts, not only chat answers.
- Prefer narrow single-task workflows over large fully automated pipelines.

## Failure Repair

- If source pages are inaccessible, ask for screenshots or copied text and create only a placeholder intake record.
- If a note is vague, mark it as weak signal and do not create a full skill from it.
- If an artifact repeats generic advice, rewrite it around a concrete trigger, input, and output.
- If the process produces too many files, merge checklist and workflow content before adding more skills.
