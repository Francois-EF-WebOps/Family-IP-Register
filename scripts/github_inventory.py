#!/usr/bin/env python3
"""Read-only GitHub account inventory. Uses only the Python standard library."""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def fetch_page(owner, page, token):
    query = urllib.parse.urlencode({"per_page": 100, "page": page, "sort": "updated"})
    url = f"https://api.github.com/users/{urllib.parse.quote(owner)}/repos?{query}"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "family-operations-runtime",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def collect(owner, token):
    repositories = []
    page = 1
    while True:
        batch = fetch_page(owner, page, token)
        if not isinstance(batch, list):
            raise RuntimeError("GitHub API returned an unexpected response")
        repositories.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repositories


def clean(repo):
    license_info = repo.get("license") or {}
    return {
        "full_name": repo.get("full_name"),
        "name": repo.get("name"),
        "description": repo.get("description"),
        "url": repo.get("html_url"),
        "visibility": repo.get("visibility") or ("private" if repo.get("private") else "public"),
        "archived": bool(repo.get("archived")),
        "fork": bool(repo.get("fork")),
        "default_branch": repo.get("default_branch"),
        "language": repo.get("language"),
        "license": license_info.get("spdx_id") or license_info.get("name"),
        "created_at": repo.get("created_at"),
        "updated_at": repo.get("updated_at"),
        "pushed_at": repo.get("pushed_at"),
        "size_kb": repo.get("size"),
        "stars": repo.get("stargazers_count"),
        "forks": repo.get("forks_count"),
        "open_issues": repo.get("open_issues_count"),
    }


def markdown(owner, rows):
    lines = [
        "# GitHub Portfolio Inventory",
        "",
        f"- Owner: **{owner}**",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        "- Source: GitHub REST API repository metadata",
        "- Scope: metadata only; no repository contents cloned or downloaded",
        f"- Repositories: **{len(rows)}**",
        "",
        "| Repository | Visibility | Archived | Default branch | Language | Licence | Last push |",
        "|---|---|---:|---|---|---|---|",
    ]
    for row in sorted(rows, key=lambda item: (item["full_name"] or "").lower()):
        values = [
            row["full_name"] or "",
            row["visibility"] or "",
            "yes" if row["archived"] else "no",
            row["default_branch"] or "",
            row["language"] or "",
            row["license"] or "",
            (row["pushed_at"] or "")[:10],
        ]
        lines.append("| " + " | ".join(str(v).replace("|", "\\|").replace("\n", " ") for v in values) + " |")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", required=True, help="GitHub account login")
    parser.add_argument("--json-output", default="reports/github-inventory.json")
    parser.add_argument("--markdown-output", default="reports/github-inventory.md")
    args = parser.parse_args()
    token = os.environ.get("GH_PORTFOLIO_TOKEN")
    if not token:
        print("Missing GH_PORTFOLIO_TOKEN. Configure a read-only GitHub token as a repository Actions secret.", file=sys.stderr)
        return 2
    try:
        repos = collect(args.owner, token)
        rows = [clean(repo) for repo in repos]
        Path(args.json_output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.markdown_output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.json_output).write_text(
            json.dumps({"owner": args.owner, "generated_at": datetime.now(timezone.utc).isoformat(),
                        "repository_count": len(rows), "repositories": rows}, indent=2) + "\n",
            encoding="utf-8",
        )
        Path(args.markdown_output).write_text(markdown(args.owner, rows), encoding="utf-8")
        print(f"Inventory complete: {len(rows)} repositories")
        print(f"Markdown: {args.markdown_output}")
        print(f"JSON: {args.json_output}")
        return 0
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"GitHub inventory failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
