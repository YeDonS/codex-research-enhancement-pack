#!/usr/bin/env python3
"""Validate the Codex research enhancement pack.

This is a structural gate, not a research-quality proof. It catches missing
artifacts and stale skill metadata before a batch is considered packaged.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - validation environment should include PyYAML
    yaml = None


REQUIRED_FILES = [
    "README.md",
    "progress.md",
    "workflows/research-task-flows.md",
    "checklists/research-quality-checklists.md",
    "templates/prompt-goal-templates.md",
    "rubrics/research-capability-rubric.md",
    "examples/usage-examples.md",
    "docs/USER_GUIDE.md",
    "docs/INSTALLATION_AND_SYNC.md",
    "scripts/install_skills.py",
    "reviews/stage-2026-06-21-review.md",
    "reviews/stage-2026-06-21-v0.5-review.md",
    "reviews/stage-2026-06-21-v0.6-review.md",
    "reviews/stage-2026-06-21-v0.7-review.md",
    "reviews/stage-2026-06-21-v0.8-review.md",
    "reviews/stage-2026-06-21-v0.9-review.md",
    "reviews/stage-2026-06-21-v1.0-review.md",
    "reviews/stage-2026-06-21-v1.1-review.md",
    "reviews/stage-2026-06-21-v1.2-review.md",
    "reviews/stage-2026-06-21-v1.3-review.md",
    "reviews/stage-2026-06-21-v1.4-review.md",
    "validation/phase-1-validation.md",
    "evals/eval-plan.md",
]

REQUIRED_SKILLS = [
    "xhs-method-ingester",
    "literature-landscape-researcher",
    "literature-evidence-reader",
    "research-question-council",
    "experiment-design-planner",
    "reproduction-data-analyst",
    "research-synthesis-writer",
    "submission-readiness-reviewer",
    "research-knowledge-curator",
    "research-program-manager",
    "research-handoff-review",
]

REQUIRED_SKILL_SECTIONS = [
    "## Trigger",
    "## Inputs",
    "## Procedure",
    "## Output Format",
    "## Quality Standards",
    "## Failure Repair",
]

PROGRESS_HEADER = "| 输入材料 | 提炼结论 | 转化产物 | 验证结果 | 下一步 |"
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

FIXTURES = [
    "evals/fixtures/xhs-batch-minimal.md",
    "evals/fixtures/literature-search-bias-minimal.md",
    "evals/fixtures/paper-reading-minimal.md",
    "evals/fixtures/conflicting-literature-minimal.md",
    "evals/fixtures/research-question-minimal.md",
    "evals/fixtures/experiment-tradeoff-minimal.md",
    "evals/fixtures/reproduction-mismatch-minimal.md",
    "evals/fixtures/data-analysis-leakage-minimal.md",
    "evals/fixtures/synthesis-overclaim-minimal.md",
    "evals/fixtures/submission-readiness-minimal.md",
    "evals/fixtures/knowledge-curation-minimal.md",
    "evals/fixtures/long-running-goal-drift-minimal.md",
    "evals/fixtures/handoff-minimal.md",
]

EVAL_OUTPUTS = [
    "evals/outputs/2026-06-21/xhs-batch-minimal-output.md",
    "evals/outputs/2026-06-21/literature-search-bias-minimal-output.md",
    "evals/outputs/2026-06-21/paper-reading-minimal-output.md",
    "evals/outputs/2026-06-21/conflicting-literature-minimal-output.md",
    "evals/outputs/2026-06-21/research-question-minimal-output.md",
    "evals/outputs/2026-06-21/experiment-tradeoff-minimal-output.md",
    "evals/outputs/2026-06-21/reproduction-mismatch-minimal-output.md",
    "evals/outputs/2026-06-21/data-analysis-leakage-minimal-output.md",
    "evals/outputs/2026-06-21/synthesis-overclaim-minimal-output.md",
    "evals/outputs/2026-06-21/submission-readiness-minimal-output.md",
    "evals/outputs/2026-06-21/knowledge-curation-minimal-output.md",
    "evals/outputs/2026-06-21/long-running-goal-drift-minimal-output.md",
    "evals/outputs/2026-06-21/handoff-minimal-output.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def parse_frontmatter(skill_md: Path) -> dict:
    content = read_text(skill_md)
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    if yaml is None:
        data: dict[str, str] = {}
        for line in match.group(1).splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip().strip('"')
        return data
    parsed = yaml.safe_load(match.group(1))
    return parsed if isinstance(parsed, dict) else {}


def validate_skill(root: Path, skill_name: str, errors: list[str]) -> None:
    skill_dir = root / "skills" / skill_name
    skill_md = skill_dir / "SKILL.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"

    check(skill_md.exists(), f"missing SKILL.md for {skill_name}", errors)
    check(openai_yaml.exists(), f"missing agents/openai.yaml for {skill_name}", errors)
    if not skill_md.exists():
        return

    content = read_text(skill_md)
    frontmatter = parse_frontmatter(skill_md)
    check(frontmatter.get("name") == skill_name, f"{skill_name} frontmatter name mismatch", errors)
    check(bool(frontmatter.get("description")), f"{skill_name} missing description", errors)
    for section in REQUIRED_SKILL_SECTIONS:
        check(section in content, f"{skill_name} missing section {section}", errors)

    if openai_yaml.exists():
        if yaml is None:
            meta = read_text(openai_yaml)
            check(f"${skill_name}" in meta, f"{skill_name} default prompt does not reference skill", errors)
            return
        try:
            meta = yaml.safe_load(read_text(openai_yaml))
        except Exception as exc:  # noqa: BLE001 - validator should report any parse failure
            errors.append(f"{skill_name} openai.yaml parse error: {exc}")
            return
        interface = meta.get("interface", {}) if isinstance(meta, dict) else {}
        check(bool(interface.get("display_name")), f"{skill_name} missing display_name", errors)
        check(bool(interface.get("short_description")), f"{skill_name} missing short_description", errors)
        default_prompt = interface.get("default_prompt", "")
        check(f"${skill_name}" in default_prompt, f"{skill_name} default_prompt missing ${skill_name}", errors)


def validate_markdown_links(root: Path, errors: list[str]) -> None:
    for markdown in root.rglob("*.md"):
        content = read_text(markdown)
        for raw_target in MARKDOWN_LINK_PATTERN.findall(content):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative_target = target.split("#", 1)[0]
            if not relative_target:
                continue
            resolved = (markdown.parent / relative_target).resolve()
            check(
                resolved.exists(),
                f"broken markdown link in {markdown.relative_to(root)}: {target}",
                errors,
            )


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors: list[str] = []

    check(root.exists(), f"pack root does not exist: {root}", errors)
    for rel in REQUIRED_FILES:
        check((root / rel).exists(), f"missing required file: {rel}", errors)
    for rel in FIXTURES:
        check((root / rel).exists(), f"missing eval fixture: {rel}", errors)
    for rel in EVAL_OUTPUTS:
        output = root / rel
        check(output.exists(), f"missing eval output: {rel}", errors)
        if output.exists():
            text = read_text(output)
            check("## Acceptance Result" in text, f"eval output missing acceptance results: {rel}", errors)
            check("Pass" in text, f"eval output has no passing acceptance checks: {rel}", errors)

    progress = root / "progress.md"
    if progress.exists():
        progress_text = read_text(progress)
        check(PROGRESS_HEADER in progress_text, "progress.md missing required five-column tracking table", errors)
        check("## 待验证问题" in progress_text, "progress.md missing pending validation section", errors)
        check("## 下一步计划" in progress_text, "progress.md missing next plan section", errors)

    validate_markdown_links(root, errors)

    for skill in REQUIRED_SKILLS:
        validate_skill(root, skill, errors)

    skill_count = len([p for p in (root / "skills").glob("*/SKILL.md")]) if (root / "skills").exists() else 0
    check(skill_count >= 11, "expected at least 11 skill drafts", errors)

    if errors:
        print("PACK VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PACK VALIDATION PASSED")
    print(f"- root: {root}")
    print(f"- skills: {skill_count}")
    print(f"- required files: {len(REQUIRED_FILES)}")
    print(f"- eval fixtures: {len(FIXTURES)}")
    print(f"- eval outputs: {len(EVAL_OUTPUTS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
