# Eval Output: Long-Running Goal Drift Minimal

Fixture: `evals/fixtures/long-running-goal-drift-minimal.md`

Skill: `research-program-manager`

# Research Program Status

## Program Charter

| Objective | Completion Evidence | Constraint |
|---|---|---|
| Build a reusable Codex research enhancement pack from research notes | Skills, workflows, checklists, progress, reviews, templates, rubric, examples, plus successful validation on real research materials | Real PDF/database/notebook/manuscript not yet supplied; GitHub CLI not authenticated |

## Requirement Audit

| Requirement | Status | Evidence | Gap | Next Proof |
|---|---|---|---|---|
| Reusable skills/workflows/checklists | Proven structurally | Files exist and package validator passes | Real task behavior unproven | Run one skill on real material and score with rubric |
| Trigger/input/steps/output/quality/failure fields | Proven structurally | Skill validator and package validator pass | Generalization unproven | Independent real-task output review |
| Progress and stage reviews | Proven structurally | `progress.md` and review files exist | Longitudinal usefulness unproven | Resume one later session from files only |
| Prompt/goal templates, rubric, examples | Proven structurally | Required files exist | Usage effectiveness unproven | Use templates in one real task and record friction |
| Real research validation | Missing | No real PDF, database search, notebook/CSV, or manuscript run | Explicit completion criterion unmet | Run smallest available real-material task |
| GitHub synchronization | Partial/external dependency | Local package ready; `gh auth status` failed twice | Authentication required | User completes `gh auth login`, then create/push repo |

Decision: The objective is active, not complete. It is also not globally blocked because real-material validation can proceed independently of GitHub authentication.

## Milestones

| Milestone | Outcome | Dependencies | Acceptance | Status |
|---|---|---|---|---|
| M1 Structural package | Required artifacts and validators | Local workspace | Package validator passes | Completed |
| M2 Real-material pilot | One real research input processed end to end | Real PDF/search/notebook/manuscript | Output meets relevant rubric and records failures | In progress |
| M3 Independent reuse | New session resumes from files and reruns fixture/real task | M2 artifacts and handoff | No full-chat reconstruction required | Pending |
| M4 GitHub publication | Public/private repo synchronized with manual | GitHub authentication and visibility decision | Remote URL exists and pushed commit matches local validation | Pending |

## Work Queue

| Priority | Action | Expected Evidence | Status |
|---:|---|---|---|
| P1 | Run the smallest available skill on one real research artifact | Real input path, output, rubric score, failure notes | In progress |
| P2 | Recheck GitHub authentication after user action | Successful `gh auth status` | Pending |
| P3 | Publish validated package | Remote repository and commit URL | Pending |
| Drop | Redesign unrelated CSS | No completion criterion advanced | Rejected as scope drift |

## Execution Log

| Date | Action | Inputs/Commands | Outputs | Validation |
|---|---|---|---|---|
| Current stage | Structural package validation | Package files and validator | Passing structural report | Strong evidence for structure only; weak for real capability |

## Decision Log

| Decision | Evidence | Alternative | Reversal Condition |
|---|---|---|---|
| Do not mark complete | Real-material validation criterion is unmet | Treat file existence as completion | Reverse only after real-task evidence passes audit |
| Do not mark globally blocked | Real validation can proceed without GitHub | Stop all work for auth | Reconsider only if no meaningful task can proceed |
| Reject CSS task | It maps to no completion criterion | Do easy unrelated work | Reconsider only if objective changes |
| Keep one active item | Twelve concurrent items obscure status | Leave all in progress | Add another active item only after P1 completes or stops |

## Risks and Blockers

| Condition | Occurrences | Mitigation | Escalation Trigger |
|---|---:|---|---|
| GitHub CLI unauthenticated | 2 | Ask user to run `gh auth login`; continue local/real validation work | Escalate as a publication blocker after the defined recurrence threshold and no alternative publication route |
| No real material available | 1 | Search workspace for a suitable non-sensitive artifact or request one | Escalate only if no meaningful synthetic/structural improvement remains and user input is essential |
| Structural checks mistaken for capability proof | 1 | Keep evidence classes separate in requirement audit | Reopen any completion claim lacking real-task evidence |

## Stage Review

- Effective: explicit required artifacts, structural validator, adversarial fixtures, progress/review files.
- Generic unless validated: “reusable,” “improves research,” and “reduces effort” claims.
- Rewrite/delete: any statement claiming full completion from passing structure checks alone.

## Next Session

Select one real non-sensitive artifact already available in the workspace, run the matching skill, save the output and rubric score, then update the requirement audit. Do not start the unrelated CSS task.

## Acceptance Result

| Criterion | Result |
|---|---|
| Does not mark complete or blocked | Pass |
| Identifies missing real-material validation | Pass |
| Keeps one item in progress | Pass |
| Records GitHub auth occurrence and escalation rule | Pass |
| Rejects unrelated CSS scope drift | Pass |
| Produces evidence-based milestones and next proof | Pass |
