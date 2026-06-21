# Eval Output: Reproduction Mismatch Minimal

Fixture: `evals/fixtures/reproduction-mismatch-minimal.md`

Skill: `reproduction-data-analyst`

# Reproduction/Data Analysis Report

## Target

| Item | Value |
|---|---|
| Paper | Method Y for Robust Classification |
| Target result | Table 3, Dataset Z, macro-F1 = 92.4 |
| Claimed setup | Dataset Z v1, official split, seed 13, `config/table3.yaml` |
| Match tolerance | +/- 0.5 macro-F1 |

## Preflight

| Area | Status | Evidence | Risk |
|---|---|---|---|
| Repository command | Present | `python train.py --config config/table3.yaml --dataset data/z` | Command is usable but not sufficient for target match |
| Config | Incomplete | `config/table3.yaml`, local seed missing | Paper target uses seed 13; local run used `seed=None` |
| Dataset version | Mismatch | `data/z/VERSION` is `v2`; paper uses v1 | High risk: results not comparable |
| Dataset split/size | Mismatch | Local train/test 12,400/2,100 vs paper 11,900/2,000 | High risk: split differs |
| Environment | Recorded | Python 3.11, torch 2.4, CUDA 12.4 | Unknown paper environment; possible dependency drift |
| Output path | Present | `runs/table3_local_v2_seed_none/metrics.json` | Good for audit |

## Run Log

| Command | CWD | Config | Seed | Output | Status |
|---|---|---|---|---|---|
| `python train.py --config config/table3.yaml --dataset data/z` | `/repo` | `config/table3.yaml` | `None` | `runs/table3_local_v2_seed_none/metrics.json` | Completed |

## Metric Comparison

| Metric | Paper Target | Local Result | Delta | Tolerance | Verdict |
|---|---:|---:|---:|---:|---|
| Dataset Z macro-F1 | 92.4 | 89.1 | -3.3 | +/- 0.5 | Not reproduced |

## Mismatch Triage

| Suspected Cause | Evidence | Next Check |
|---|---|---|
| Dataset version mismatch | Local `VERSION` is v2; paper used v1 | Download or restore Dataset Z v1 and verify manifest |
| Split mismatch | Local rows 12,400/2,100 vs paper 11,900/2,000 | Compare official v1 split files and row counts |
| Missing seed | Paper seed 13; local `seed=None` | Set seed 13 in config and rerun only after dataset v1 is restored |
| Environment drift | Local Python/torch/CUDA recorded; paper env unknown | Check paper repo tags, lockfiles, or appendix for dependency versions |
| Metric implementation mismatch | Not yet checked | After data/seed repair, inspect macro-F1 implementation if mismatch remains |

## Reproducibility Record

- Paper target: Table 3, Dataset Z macro-F1 92.4.
- Local command: `python train.py --config config/table3.yaml --dataset data/z`.
- Local CWD: `/repo`.
- Local environment: Python 3.11, torch 2.4, CUDA 12.4.
- Local dataset version: Dataset Z v2.
- Local train/test rows: 12,400/2,100.
- Paper dataset version: Dataset Z v1.
- Paper train/test rows: 11,900/2,000.
- Local seed: `None`.
- Paper seed: 13.
- Local output: `runs/table3_local_v2_seed_none/metrics.json`.

## Decision

- Reproduced: No.
- Not reproduced: Table 3 Dataset Z macro-F1. The local result is 3.3 points below target, outside the +/- 0.5 tolerance, and the local run used the wrong dataset version/split with no fixed seed.
- Next smallest action: Restore Dataset Z v1 and official split, verify row counts match 11,900/2,000, set seed 13, then rerun the same config once. Only inspect metric code if the corrected run remains outside tolerance.

## Acceptance Result

| Criterion | Result |
|---|---|
| Does not call mismatch reproduced | Pass |
| Identifies dataset version/split mismatch | Pass |
| Identifies missing seed | Pass |
| Compares target/local/delta/tolerance | Pass |
| Proposes next smallest diagnostic run | Pass |
| Includes reproducibility record and run log | Pass |
