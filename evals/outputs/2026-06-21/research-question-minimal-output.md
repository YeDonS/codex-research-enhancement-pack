# Eval Output: Research Question Minimal

Fixture: `evals/fixtures/research-question-minimal.md`

Skill: `research-question-council`

# Research Question Council

## Decision Being Made

Should the project test whether citation-grounded prompting reduces factual errors in LLM-generated literature reviews, and if so, what is the smallest feasible research question?

## Role Findings

| Role | Strongest Point | Concrete Risk | Repair |
|---|---|---|---|
| Opponent | The project has a measurable core: unsupported claim rate can be compared between two prompt conditions | 50 annotated errors are too few for strong claims, and annotation bias may dominate | Treat first run as pilot; predefine error taxonomy; report uncertainty |
| First-principles analyst | The mechanism is not “better writing” but forcing each claim to map to source evidence | “Fact error” is too broad and will blur unsupported claims, wrong citations, and bad synthesis | Split metrics into unsupported claim rate, citation-location accuracy, and synthesis error |
| Expander | The work can produce a reusable evaluation workflow for evidence-constrained literature review | If framed as a prompt trick, contribution is weak | Frame as evidence-traceability protocol and release rubric/checklist |
| Outsider | The local PDF-only corpus limits generality but improves auditability | Review questions may overfit to the 30 local papers | State scope as local-corpus literature review assistance |
| Executor | A two-week pilot is feasible with 5 papers and 3 questions | Full benchmark would exceed time and annotation budget | Run 2 prompt conditions on a small subset before expanding |

## Candidate Questions

| Question | Why It Matters | Evidence Base | Feasibility | Falsifiability | Score |
|---|---|---|---|---|---|
| Does citation-grounded prompting reduce unsupported claim rate in LLM literature-review answers over a local 30-paper corpus? | Directly targets factual reliability | Uses existing PDFs and error labels | High as pilot | Yes: compare unsupported claim rates | 8/10 |
| Does citation-grounded prompting improve overall review quality? | Broader and more publishable if valid | Needs new quality rubric and more annotation | Low for two weeks | Weak unless quality dimensions are defined | 4/10 |
| Does citation-location accuracy predict factual error rate? | Tests mechanism behind evidence grounding | Can reuse generated outputs, needs extra labels | Medium | Yes: correlate location accuracy with errors | 7/10 |

## Final Verdict

- Decision: Continue, but narrow to a pilot.
- Chosen question: Does citation-grounded prompting reduce unsupported claim rate in LLM literature-review answers over a local 30-paper corpus?
- Rejected option: Overall review quality, because it is too broad and too expensive to annotate in two weeks.
- Why: The chosen question is measurable, fits current materials, and has a clear falsification path.

## Next Smallest Action

Select 5 PDFs and 3 review questions. Generate answers with ordinary prompting and citation-grounded prompting. Label each generated claim for unsupported claim status and citation-location accuracy. Decide whether the pilot effect is large and stable enough to scale.

## Acceptance Result

| Criterion | Result |
|---|---|
| Five roles provide concrete risks | Pass |
| Three candidate questions generated | Pass |
| At least one candidate rejected | Pass |
| Final next action is a small pilot | Pass |
