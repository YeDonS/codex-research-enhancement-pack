---
name: research-program-manager
description: Use when the user has a long-running research goal spanning days, tools, papers, experiments, or writing stages and needs milestone planning, evidence-based progress tracking, decision logs, blocker handling, reviews, and reliable context recovery.
---

# Research Program Manager

## Trigger

Use this skill when a research task spans multiple sessions, phases, tools, repositories, papers, experiments, people, or deliverables, or when the user asks Codex to maintain a long-term goal, progress plan, recurring review, or resumable research program.

## Inputs

- Full objective and explicit completion criteria.
- Current workspace, authoritative files, prior progress logs, handoffs, experiments, and decisions.
- Constraints: time, budget, compute, data access, ethics, dependencies, and user approvals.
- Known milestones, blockers, risks, recurring tasks, and external deadlines.
- Desired review cadence and notification/automation preferences, if any.

## Procedure

1. Create the program charter:
   - Preserve the user's full objective and derive concrete completion evidence for every criterion.
   - Do not redefine success around the work already completed.
2. Compile rough goals before planning:
   - Rewrite a one-sentence request into outcome, scope, deliverables, completion evidence, constraints, and explicit assumptions.
   - Infer non-blocking defaults from the workspace and name them; ask only questions that change safety, external state, or verifiability.
   - For inspection, debugging, refactoring, or repair requests, separate diagnosis from execution and record the required approval gate.
3. Audit current state:
   - Inspect authoritative files, logs, commands, outputs, tests, and external state.
   - Classify each requirement as proven, contradicted, partial, weak evidence, missing, or blocked.
4. Build milestones:
   - Define outcomes, dependencies, acceptance checks, risks, and required artifacts.
   - Keep planning tied to the real end state, not easy proxy tasks.
5. Maintain the work queue:
   - Keep at most one item in progress.
   - Choose 1-3 next actions that can produce inspectable evidence in the current session.
6. Record execution evidence:
   - For each action, record inputs, commands, changed files, outputs, validation, and remaining uncertainty.
7. Keep a decision log:
   - Record decisions, alternatives, evidence, owner, date, and reversal condition.
   - Distinguish user decisions from agent assumptions.
8. Handle blockers and drift:
   - Try concrete alternatives before escalating.
   - Do not mark blocked on first occurrence; track recurrence and the exact condition.
   - Reject unrelated work or scope shrinkage unless it materially advances a completion criterion.
9. Review and hand off:
   - At each stage, review what improved capability, what was generic, and what should be deleted or rewritten.
   - End with a next action that can be executed without rereading the full conversation.

## Output Format

```markdown
# Research Program Status

## Program Charter
| Objective | Completion Evidence | Constraint |

## Goal Brief
| Outcome | Scope | Assumptions | Approval Gate | Deliverables |

## Requirement Audit
| Requirement | Status | Evidence | Gap | Next Proof |

## Milestones
| Milestone | Outcome | Dependencies | Acceptance | Status |

## Work Queue
| Priority | Action | Expected Evidence | Status |

## Execution Log
| Date | Action | Inputs/Commands | Outputs | Validation |

## Decision Log
| Decision | Evidence | Alternative | Reversal Condition |

## Risks and Blockers
| Condition | Occurrences | Mitigation | Escalation Trigger |

## Stage Review

## Next Session
```

## Quality Standards

- The full user objective and original completion criteria remain visible.
- A rough goal is compiled into a bounded outcome before it becomes a long work queue.
- Questions are limited to genuine execution blockers; non-blocking uncertainty is recorded as an assumption.
- Every progress claim links to authoritative evidence, not intent or file existence alone.
- At most one work item is in progress.
- Milestones describe outcomes and acceptance evidence, not only activities.
- Completion is never inferred from budget exhaustion, elapsed time, green structure checks, or plausible prose.
- Blockers record recurrence, attempted mitigations, and the condition needed to resume.
- The next session can continue from files and logs without reconstructing chat history.
- Stage reviews explicitly identify effective methods, generic advice, and delete/rewrite candidates.

## Failure Repair

- If the plan becomes a large wish list, reduce the active queue while preserving the full objective.
- If progress uses weak evidence, inspect the real artifact, runtime, test, or external state before updating status.
- If the work drifts, map the proposed action to a completion criterion or remove it.
- If a blocker appears once, try alternatives and log it; escalate only after the defined recurrence rule or a true safety boundary.
- If handoff is vague, add paths, commands, outputs, decisions, risks, and the next executable action.
- If completion is claimed early, run a requirement-by-requirement audit and reopen every unproven item.
- If a repair request mixes diagnosis and changes, finish the inspection first and request approval before mutating the target unless the user has explicitly authorized immediate changes.
