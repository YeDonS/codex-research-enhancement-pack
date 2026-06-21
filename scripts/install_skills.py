#!/usr/bin/env python3
"""Install selected skill directories from this pack into a Codex skills root."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def default_target() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    return (Path(codex_home) if codex_home else Path.home() / ".codex") / "skills"


def discover_skills(pack_root: Path) -> dict[str, Path]:
    skills_root = pack_root / "skills"
    return {
        path.name: path
        for path in sorted(skills_root.iterdir())
        if path.is_dir() and (path / "SKILL.md").exists()
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List available skills and exit")
    parser.add_argument("--all", action="store_true", help="Install every skill in this pack")
    parser.add_argument("--skill", action="append", default=[], help="Skill name to install; repeat as needed")
    parser.add_argument("--target", type=Path, default=default_target(), help="Destination skills directory")
    parser.add_argument("--dry-run", action="store_true", help="Print planned actions without writing")
    parser.add_argument("--force", action="store_true", help="Replace an existing destination skill directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pack_root = Path(__file__).resolve().parents[1]
    available = discover_skills(pack_root)

    if args.list:
        for name in available:
            print(name)
        return 0

    selected = list(available) if args.all else list(dict.fromkeys(args.skill))
    if not selected:
        print("Select --all or at least one --skill. Use --list to inspect names.", file=sys.stderr)
        return 2

    unknown = [name for name in selected if name not in available]
    if unknown:
        print(f"Unknown skill(s): {', '.join(unknown)}", file=sys.stderr)
        return 2

    target = args.target.expanduser().resolve()
    conflicts: list[str] = []
    for name in selected:
        source = available[name]
        destination = target / name
        if destination.exists() and not args.force:
            conflicts.append(name)
            print(f"SKIP {name}: destination exists; rerun with --force to replace it")
            continue

        action = "REPLACE" if destination.exists() else "INSTALL"
        print(f"{action} {name}: {source} -> {destination}")
        if args.dry_run:
            continue

        target.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination)

    if conflicts:
        print(f"Not installed due to conflicts: {', '.join(conflicts)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
