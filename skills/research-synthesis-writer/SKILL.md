---
name: research-synthesis-writer
description: Use when the user wants to turn evidence cards, paper notes, experiment results, or review matrices into literature review prose, manuscript sections, abstracts, reviewer responses, submission materials, or writing revisions without losing evidence traceability.
---

# Research Synthesis Writer

## Trigger

Use this skill when the user asks to write, revise, polish, or prepare research text from evidence: related work, literature review, introduction, discussion, abstract, cover letter, reviewer response, rebuttal, grant background, or submission checklist.

## Inputs

- Evidence cards, method cards, variable tables, paper notes, or experiment results.
- Target text type: related work, intro, discussion, abstract, reviewer response, cover letter, or submission package.
- Target audience, venue, word limit, tone, citation style, and claims the user wants to make.
- Known limitations, conflicting evidence, missing sources, and claims that must not be made.
- Existing draft if revising.

## Procedure

1. Audit evidence before writing:
   - Separate supported claims, weak claims, conflicts, and missing evidence.
   - Reject or flag any requested claim without source support.
   - Identify which evidence can support background, gap, method motivation, results interpretation, or limitation.
2. Build claim hierarchy:
   - High-level argument.
   - Subclaims with source locations.
   - Counterevidence and boundary conditions.
   - Contribution statement that does not exceed the evidence.
3. Draft with traceability:
   - Every substantive claim must map to evidence cards, source locations, or experiment outputs.
   - Preserve uncertainty when evidence is mixed.
   - Do not invent citations, methods, sample sizes, or results.
4. Improve prose:
   - Tighten structure, transitions, and signposting.
   - Remove overclaiming, vague novelty language, and unsupported causal language.
   - Keep claims scoped to population, dataset, method, metric, and setting.
5. Prepare review/submission materials if requested:
   - Reviewer response: quote or paraphrase criticism, state action taken, point to changed section, and note limitations.
   - Cover letter: contribution, fit, and ethics/data availability without hype.
   - Submission checklist: figures, tables, references, data/code availability, conflicts, reporting standards.
6. Run final claim lint:
   - Unsupported claims become questions, TODOs, or are removed.
   - Conflicting evidence is kept visible.
   - Limitations and next steps are explicit.

## Output Format

```markdown
# Research Synthesis Output

## Evidence Audit
| Claim | Support | Source | Status | Action |

## Claim Hierarchy

## Draft

## Traceability Map
| Draft Claim | Evidence Source | Confidence | Caveat |

## Removed or Weakened Claims

## Final Checklist
```

## Quality Standards

- No substantive claim appears only in prose; it must appear in the traceability map.
- The draft keeps conflicts, uncertainty, and scope limits visible.
- Novelty and contribution claims are bounded by the evidence.
- Reviewer responses identify the change made and where.
- Submission materials do not claim data/code/ethics availability unless provided.
- The output improves readability without converting weak evidence into strong claims.

## Failure Repair

- If the user asks for unsupported stronger wording, refuse the overclaim and offer scoped alternatives.
- If evidence is missing, create a gap list instead of writing around it.
- If sources conflict, write condition-specific synthesis rather than averaging them away.
- If the draft becomes generic, rebuild from claim hierarchy and evidence cards.
- If citation or venue requirements are unknown, write a neutral draft and list the missing formatting requirements.
