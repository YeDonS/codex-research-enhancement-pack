# Eval Output: Experiment Tradeoff Minimal

Fixture: `evals/fixtures/experiment-tradeoff-minimal.md`

Skill: `experiment-design-planner`

# Experiment Plan

## Decision

- Hypothesis: Requiring source locations for every factual claim reduces unsupported claims in LLM literature-review answers.
- Null/failure alternative: Source-location prompting does not reduce unsupported claims enough to justify added length, calibration risk, or subgroup regressions.
- Decision enabled: Revise and rerun a constrained pilot before scaling; do not declare treatment successful from unsupported claim rate alone.

## Design

| Component | Choice | Rationale | Risk |
|---|---|---|---|
| Unit of analysis | Individual factual claim | Unsupported claim rate is claim-level | Claim segmentation may vary by annotator |
| Dataset | 10 questions over 30 local PDFs | Matches current pilot | May overfit local corpus |
| Baseline | Prose-only prompt | Current control | Baseline may be shorter and less auditable |
| Treatment | Source-location prompt | Current intervention | Longer answers and false confidence may increase review cost |
| Follow-up sample | Focused 6-hour annotation slice | Fits remaining budget | Smaller sample limits confirmatory claims |
| Stratification | Methods papers vs clinical papers | Clinical subgroup did not improve | Requires balanced question selection |

## Variables

| Variable | Role | Measurement | Notes |
|---|---|---|---|
| Prompt type | Independent variable | Baseline vs source-location prompt | Keep model and PDFs fixed |
| Unsupported claim rate | Primary outcome | Unsupported claims / total factual claims | Predefine annotation rubric |
| Citation-location accuracy | Guardrail metric | Correct locations / cited locations | 74% pilot accuracy may be too low |
| Calibration self-rating | Guardrail metric | High confidence on unsupported claims | Worsened in pilot; possible blocking issue |
| Answer length | Cost metric | Token or word count | +65% length may increase human review time |
| Paper type | Moderator/subgroup | Methods vs clinical | Clinical papers show no improvement |
| Model version | Control | Exact model identifier | Must be fixed across arms |
| Sampling settings | Control | temperature, seed if available | Needed for reproducibility |

## Metrics

| Metric | Type | Threshold | Why |
|---|---|---|---|
| Unsupported claim rate | Primary | Treatment must reduce absolute rate by at least 8 points overall and in each priority subgroup | Measures factual reliability |
| Citation-location accuracy | Guardrail | Must be >= 90% before scaling | Bad citations create false auditability |
| High-confidence unsupported claims | Guardrail | Must not exceed baseline rate; target < 10% | Prevents confident misinformation |
| Clinical-paper unsupported claim rate | Guardrail/subgroup | Must improve by at least 5 points or trigger redesign | Clinical subgroup did not improve in pilot |
| Answer length | Cost | Increase should stay below 30% unless accuracy gain is large | Controls review burden |

## Run Plan

- Data: Use the same 30 local PDFs, but allocate the remaining annotation to a balanced slice: 2 methods questions and 2 clinical questions, with both baseline and treatment outputs.
- Baseline: Existing prose prompt, frozen prompt version `baseline-v1`.
- Treatment: Source-location prompt revised to require source spans and confidence only after evidence is found, prompt version `source-location-v2`.
- Commands: Record generation command or UI settings in `runs/source_location_pilot_02/run_log.md`.
- Seeds: Record random seed if API supports it; otherwise record model version, temperature, top_p, timestamp, and full prompt.
- Outputs:
  - `runs/source_location_pilot_02/outputs/baseline.jsonl`
  - `runs/source_location_pilot_02/outputs/treatment.jsonl`
  - `runs/source_location_pilot_02/annotations/claims.csv`
  - `runs/source_location_pilot_02/summary.md`

## Decision Rules

- Continue if:
  - Unsupported claim rate improves by >= 8 absolute points overall.
  - Clinical-paper subgroup improves by >= 5 absolute points.
  - Citation-location accuracy is >= 90%.
  - High-confidence unsupported claims decrease or remain below 10%.
- Revise if:
  - Overall unsupported claims improve but citation-location accuracy or calibration fails.
  - Methods papers improve but clinical papers do not.
  - Answer length increases by > 30% without proportional reliability gains.
- Stop if:
  - Unsupported claim rate improvement disappears in the balanced slice.
  - High-confidence unsupported claims remain high.
  - Clinical subgroup remains at or above 27% unsupported claim rate.

## Reproducibility Record

Record before rerun:

- PDF manifest with file hashes and versions.
- Prompt versions: `baseline-v1`, `source-location-v2`.
- Model version and provider.
- Sampling settings: temperature, top_p, max tokens, seed if available.
- Claim segmentation and annotation rubric.
- Annotator ID or process.
- Output paths and timestamp.
- Exclusion rules for ambiguous claims or missing source locations.

## Review Checklist

- [ ] Primary metric was selected before the rerun.
- [ ] Guardrails include citation accuracy, calibration, answer length, and clinical subgroup performance.
- [ ] The pilot is labeled exploratory, not confirmatory.
- [ ] The plan does not average away clinical subgroup failure.
- [ ] The remaining 6-hour annotation budget is respected.
- [ ] Scaling is blocked if guardrail metrics fail.

## Acceptance Result

| Criterion | Result |
|---|---|
| Does not declare success from unsupported claim rate alone | Pass |
| Defines primary and guardrail metrics | Pass |
| Treats calibration and clinical subgroup as blocking/revision conditions | Pass |
| Proposes smallest feasible follow-up within 6 hours | Pass |
| Includes reproducibility fields | Pass |
