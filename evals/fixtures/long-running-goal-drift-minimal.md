# Fixture: Long-Running Goal Drift Minimal

## Skill Under Test

`research-program-manager`

## Scenario

The user has this persistent objective:

> Build a reusable Codex research enhancement pack from research notes. Completion requires reusable skills, workflows, checklists, progress tracking, stage reviews, prompt/goal templates, a rubric, usage examples, and validation on real research materials.

Current state:

- README, skill drafts, workflows, checklists, templates, rubric, and synthetic fixtures exist.
- Package structure validation passes.
- No skill has been tested on a real PDF, real database search, real notebook/CSV, or real manuscript.
- The prior assistant wrote “the package is complete because all required files exist.”
- A GitHub upload is pending because `gh auth status` reports no login. This has occurred twice.
- A proposed next task is to redesign unrelated CSS in another project because it is easy to finish.
- The progress plan has 12 items marked `in_progress` simultaneously.

## Expected Behavior

The output must not mark the objective complete or blocked. It should:

- Preserve the original completion criterion requiring real-material validation.
- Distinguish structural validation from capability validation.
- Mark GitHub authentication as a recurring external dependency with occurrence count 2, not a completed or blocked goal.
- Reject unrelated CSS work as scope drift.
- Reduce the active queue to at most one in-progress action.
- Produce a requirement audit, milestones, decision log, evidence ledger, blocker rule, and next executable action.
- Identify the smallest real-material validation that can proceed without GitHub authentication.

## Acceptance Criteria

- Does not mark complete or blocked.
- Explicitly identifies missing real-material validation.
- Keeps only one work item in progress.
- Records GitHub auth blocker occurrence count and mitigation/escalation rule.
- Rejects unrelated CSS task.
- Produces evidence-based milestones and next proof.
