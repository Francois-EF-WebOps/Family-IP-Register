#!/usr/bin/env python3
"""Offline-first inventory of Git repositories with durable, redacted run logs."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import subprocess
import sys
import time
from pathlib import Path


MARKERS = (
    "README.md", "LICENSE", "PROJECT.md", "ARCHITECTURE.md",
    "EVIDENCE.md", "CONTRIBUTING.md", "CHANGELOG.md",
    "pyproject.toml", "package.json", "Cargo.toml", "go.mod",
    "requirements.txt", "pom.xml", "build.gradle", ".github/workflows",
)
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".tox"}


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
    """Walk without descending into repository internals or common bulky folders."""
    root = root.resolve()
    found: list[Path] = []
    if git(root, "rev-parse", "--is-inside-work-tree") == "true":
        found.append(root)

    def walk(directory: Path, depth: int) -> None:
        if depth >= max_depth:
            return
        try:
            children = sorted(directory.iterdir(), key=lambda p: p.name.lower())
        except OSError:
            return
        for child in children:
            if not child.is_dir() or child.is_symlink() or child.name in SKIP_DIRS:
                continue
            if (child / ".git").exists() and git(child, "rev-parse", "--is-inside-work-tree") == "true":
                found.append(child)
                # A repository is a boundary; do not scan nested content.
                continue
            walk(child, depth + 1)

    walk(root, 0)
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


def append_log(path: Path, record: dict) -> None:
    """Append one JSONL event. Records contain metadata only, never file contents or secrets."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("scan", help="Discover and inventory local Git repositories")
    scan.add_argument("root", nargs="?", default=".")
    scan.add_argument("--max-depth", type=int, default=4)
    scan.add_argument("--format", choices=("json", "markdown"), default="json")
    scan.add_argument("--output", help="Write report to this path instead of stdout")
    scan.add_argument(
        "--log-file", default=".family-ops/logs/runtime.jsonl",
        help="Append run events here (default: .family-ops/logs/runtime.jsonl)",
    )
    args = parser.parse_args()

    started = time.monotonic()
    timestamp = datetime.now(timezone.utc).isoformat()
    root = Path(args.root).resolve()
    log_path = Path(args.log_file).resolve()
    event = {
        "timestamp": timestamp,
        "event": "command_started",
        "command": "scan",
        "root": str(root),
        "format": args.format,
        "report_path": str(Path(args.output).resolve()) if args.output else None,
    }
    try:
        append_log(log_path, event)
        if not root.is_dir():
            raise NotADirectoryError(f"Scan root is not a directory: {root}")
        if args.max_depth < 0:
            raise ValueError("--max-depth must be zero or greater")

        rows = [inspect(repo, root) for repo in discover(root, args.max_depth)]
        output = json.dumps({"repositories": rows}, indent=2) + "\n" if args.format == "json" else markdown(rows)
        if args.output:
            target = Path(args.output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(output, encoding="utf-8")
        else:
            print(output, end="")

        append_log(log_path, {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event": "command_completed",
            "command": "scan",
            "status": "success",
            "root": str(root),
            "repository_count": len(rows),
            "duration_ms": round((time.monotonic() - started) * 1000),
            "report_path": str(Path(args.output).resolve()) if args.output else "stdout",
        })
        print(f"Log: {log_path}", file=sys.stderr)
        return 0
    except Exception as exc:
        try:
            append_log(log_path, {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "event": "command_failed",
                "command": "scan",
                "status": "error",
                "root": str(root),
                "error_type": type(exc).__name__,
                "error": str(exc),
                "duration_ms": round((time.monotonic() - started) * 1000),
            })
        except OSError as log_exc:
            print(f"Could not write runtime log: {log_exc}", file=sys.stderr)
        print(f"Scan failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
