---
name: research-question-council
description: Use when the user wants to generate, refine, challenge, or select research questions, hypotheses, experiment designs, grant ideas, thesis topics, or paper directions using multiple critical perspectives and a final decision rubric.
---

# Research Question Council

## Trigger

Use this skill when the user asks whether a research idea is good, wants new research questions, needs to pressure-test a hypothesis, or is deciding between project directions.

## Inputs

- Candidate topic, question, hypothesis, or study plan.
- Field context and target venue if available.
- Key papers, evidence cards, constraints, data availability, budget, timeline, and user expertise.
- Desired output count, such as 3 candidate questions or 1 final recommendation.

## Procedure

1. Restate the real decision: topic selection, hypothesis design, experiment plan, literature gap, or writing angle.
2. Convene five roles:
   - Opponent: finds the weakest assumption and strongest reason to reject.
   - First-principles analyst: reformulates the problem from mechanism, variables, and causal structure.
   - Expander: finds adjacent opportunities, stronger framing, or underused data.
   - Outsider: identifies obvious missing context, hidden audience assumptions, or unclear terms.
   - Executor: converts the idea into the next smallest research action.
3. Force disagreement:
   - Each role must name at least one concrete risk.
   - Weak, generic, or duplicative points are removed.
4. Score candidates:
   - Novelty.
   - Evidence grounding.
   - Feasibility.
   - Falsifiability.
   - Expected contribution.
   - Data and method readiness.
5. Final裁决:
   - Continue, narrow, pivot, or stop.
   - Define the next experiment, literature check, or data audit.

## Output Format

```markdown
# Research Question Council

## Decision Being Made

## Role Findings
| Role | Strongest Point | Concrete Risk | Repair |

## Candidate Questions
| Question | Why It Matters | Evidence Base | Feasibility | Falsifiability | Score |

## Final Verdict
- Decision:
- Chosen question:
- Rejected options:
- Why:

## Next Smallest Action
```

## Quality Standards

- Final question is narrow enough to test.
- Variables or constructs are named.
- At least one rejection reason is serious, not cosmetic.
- Next action can be completed in one sitting or one small batch.
- If evidence is missing, the output says what evidence is needed before commitment.

## Failure Repair

- If the council produces generic advice, require each role to cite an input paper, constraint, dataset, or user goal.
- If the final question is broad, constrain population, method, variable, dataset, or outcome.
- If all roles agree too easily, rerun with an explicit hostile reviewer.
- If no feasible path exists, output a stop or pivot recommendation instead of inventing a plan.
