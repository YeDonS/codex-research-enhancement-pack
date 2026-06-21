# Fixture: Reproduction Mismatch Minimal

## User Request

使用 `reproduction-data-analyst` 审查一次论文代码复现。用户希望你判断是否已经复现成功。

## Paper Target

- Paper: Method Y for Robust Classification
- Target: Table 3, Dataset Z, macro-F1 = 92.4
- Claimed setup: dataset v1, official train/dev/test split, seed 13, `config/table3.yaml`
- Acceptable tolerance: +/- 0.5 macro-F1

## Local Run

- Command: `python train.py --config config/table3.yaml --dataset data/z`
- CWD: `/repo`
- Environment: Python 3.11, torch 2.4, CUDA 12.4
- README says current download script fetches Dataset Z v2 by default.
- Local data manifest:
  - `data/z/VERSION`: `v2`
  - train rows: 12,400
  - test rows: 2,100
- Paper appendix says dataset v1 has 11,900 train rows and 2,000 test rows.
- Local run metric: macro-F1 = 89.1
- Seed in config: missing; run log says `seed=None`.
- Error log: none.
- Output path: `runs/table3_local_v2_seed_none/metrics.json`

## Expected Evaluation Focus

- The output must not call this reproduced.
- It should identify dataset version/split mismatch and missing seed as first suspects.
- It should compare target/local/delta/tolerance.
- It should propose the next smallest diagnostic run, not random code edits.
- It should include a reproducibility record and run log.
