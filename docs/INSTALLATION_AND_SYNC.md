# 安装、更新与 GitHub 同步说明

## 1. 获取仓库

```bash
git clone https://github.com/YeDonS/codex-research-enhancement-pack.git
cd codex-research-enhancement-pack
python3 scripts/validate_pack.py .
```

## 2. 安装 Skill

默认目标是 `$CODEX_HOME/skills`；如果未设置 `CODEX_HOME`，则使用 `~/.codex/skills`。

查看列表：

```bash
python3 scripts/install_skills.py --list
```

预览全部安装：

```bash
python3 scripts/install_skills.py --all --dry-run
```

安装全部：

```bash
python3 scripts/install_skills.py --all
```

只安装指定 skill：

```bash
python3 scripts/install_skills.py \
  --skill literature-landscape-researcher \
  --skill literature-evidence-reader
```

安装到自定义目录：

```bash
python3 scripts/install_skills.py --all --target /path/to/skills
```

如果目标已存在，脚本默认拒绝覆盖。确认已有目录可替换后才能使用 `--force`。

## 3. 更新

```bash
git pull --ff-only
python3 scripts/validate_pack.py .
python3 scripts/install_skills.py --all --dry-run --force
python3 scripts/install_skills.py --all --force
```

更新前应保留本地自定义修改；`--force` 会替换目标 skill 目录。

## 4. 本地贡献流程

```bash
git switch -c codex/describe-change
# 编辑文件并运行验证
python3 scripts/validate_pack.py .
git status --short
git add <明确的文件路径>
git commit -m "describe change"
git push -u origin codex/describe-change
```

在 GitHub 上创建 draft PR。PR 说明应包含改动、原因、影响和验证命令。

## 5. 新笔记同步规则

1. 在 `progress.md` 追加批次五栏表。
2. 更新或新增 skill、workflow、checklist。
3. 新增 fixture/output 和阶段 review。
4. 更新 `README.md` 版本与验证计数。
5. 运行 `quick_validate.py` 和 `scripts/validate_pack.py`。
6. 提交到独立分支，通过 PR 合并。

## 6. 安全边界

- 不提交论文 PDF、私有数据、API key、登录 cookie、患者信息或未脱敏评论截图。
- 大模型权重、数据集和二进制产物只记录 manifest/path，不直接提交。
- GitHub 公开仓库中的示例必须使用合成或已公开材料。
- 推送前运行 `git status --short`，不要默认 `git add .`。
