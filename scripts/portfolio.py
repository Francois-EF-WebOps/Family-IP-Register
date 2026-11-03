#!/usr/bin/env python3
"""Offline-first inventory of Git repositories. Python standard library only."""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


MARKERS = (
    "README.md", "LICENSE", "PROJECT.md", "ARCHITECTURE.md",
    "EVIDENCE.md", "CONTRIBUTING.md", "CHANGELOG.md",
    "pyproject.toml", "package.json", "Cargo.toml", "go.mod",
    "requirements.txt", "pom.xml", "build.gradle", ".github/workflows",
)


def git(path: Path, *args: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(path), *args],
            check=False, capture_output=True, text=True, timeout=5,
        )
        return result.stdout.strip() if result.returncode == 0 else ""
    except (OSError, subprocess.TimeoutExpired):
        return ""


def discover(root: Path, max_depth: int) -> list[Path]:
    found: list[Path] = []
    root = root.resolve()
    for candidate in [root, *root.rglob(".git")]:
        repo = candidate if candidate.name != ".git" else candidate.parent
        try:
            depth = len(repo.relative_to(root).parts)
        except ValueError:
            continue
        if depth <= max_depth and git(repo, "rev-parse", "--is-inside-work-tree") == "true":
            found.append(repo)
    return sorted(set(found), key=lambda p: str(p).lower())


def inspect(repo: Path, root: Path) -> dict:
    branch = git(repo, "branch", "--show-current") or "(detached)"
    commit = git(repo, "rev-parse", "--short", "HEAD")
    status = git(repo, "status", "--porcelain")
    markers = [m for m in MARKERS if (repo / m).exists()]
    try:
        name = str(repo.relative_to(root))
    except ValueError:
        name = str(repo)
    return {
        "path": name or ".",
        "branch": branch,
        "commit": commit,
        "dirty": bool(status),
        "changed_file_count": len(status.splitlines()) if status else 0,
        "markers": markers,
        "has_readme": (repo / "README.md").is_file(),
        "has_license": (repo / "LICENSE").is_file(),
    }


def markdown(rows: list[dict]) -> str:
    lines = [
        "# Local Portfolio Inventory", "",
        f"Repositories discovered: **{len(rows)}**", "",
        "| Repository | Branch | Commit | Working tree | README | Licence |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['path']} | {row['branch']} | {row['commit']} | "
            f"{'dirty (' + str(row['changed_file_count']) + ')' if row['dirty'] else 'clean'} | "
            f"{'yes' if row['has_readme'] else 'no'} | "
            f"{'yes' if row['has_license'] else 'no'} |"
        )
    lines += ["", "> Generated from local Git metadata and file markers. No network or AI calls were made.", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("scan", help="Discover and inventory local Git repositories")
    scan.add_argument("root", nargs="?", default=".")
    scan.add_argument("--max-depth", type=int, default=4)
    scan.add_argument("--format", choices=("json", "markdown"), default="json")
    scan.add_argument("--output", help="Write report to this path instead of stdout")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    rows = [inspect(repo, root) for repo in discover(root, args.max_depth)]
    output = json.dumps({"repositories": rows}, indent=2) + "\n" if args.format == "json" else markdown(rows)
    if args.output:
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
