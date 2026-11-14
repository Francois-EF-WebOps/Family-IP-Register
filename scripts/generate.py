#!/usr/bin/env python3
"""Deterministic, local-first multi-format generation engine (Python stdlib only)."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "generation" / "catalog.json"
VERSION = "0.1.0"
TOKEN = re.compile(r"{{\\s*([a-zA-Z_][a-zA-Z0-9_.-]*)\\s*}}")

class GenerationError(Exception):
    pass

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def value_at(data: dict, key: str):
    value = data
    for part in key.split("."):
        if not isinstance(value, dict) or part not in value:
            raise GenerationError(f"Missing template value: {key}")
        value = value[part]
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, indent=2)
    return str(value)

def render(template: str, data: dict) -> str:
    return TOKEN.sub(lambda m: value_at(data, m.group(1)), template)

def safe_output(root: Path, relative: str) -> Path:
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts:
        raise GenerationError(f"Unsafe output path: {relative}")
    target = (root / rel).resolve()
    if root.resolve() not in target.parents:
        raise GenerationError(f"Output escapes destination: {relative}")
    return target

def generate(job_path: Path, output_dir: Path, force: bool = False) -> list[Path]:
    job_bytes = job_path.read_bytes()
    try:
        job = json.loads(job_bytes)
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise GenerationError(str(exc)) from exc
    kind = job.get("kind")
    spec = catalog.get("kinds", {}).get(kind)
    if not spec:
        raise GenerationError(f"Unsupported generation kind: {kind}")
    data = job.get("data", {})
    if not isinstance(data, dict):
        raise GenerationError("job.data must be a JSON object")
    artifacts = spec.get("artifacts", [])
    if not artifacts:
        raise GenerationError(f"No artifacts configured for kind: {kind}")

    rendered = []
    for artifact in artifacts:
        template_path = (ROOT / artifact["template"]).resolve()
        if ROOT.resolve() not in template_path.parents or not template_path.is_file():
            raise GenerationError(f"Invalid or missing template: {artifact['template']}")
        template_bytes = template_path.read_bytes()
        body = render(template_bytes.decode("utf-8"), data)
        target = safe_output(output_dir, artifact["output"])
        if target.exists() and not force:
            raise GenerationError(f"Refusing to overwrite {target}; pass --force")
        rendered.append((target, body.encode("utf-8"), artifact, digest(template_bytes)))

    # Validate every output before writing any of them.
    for target, _, _, _ in rendered:
        target.parent.mkdir(parents=True, exist_ok=True)
    for target, content, _, _ in rendered:
        target.write_bytes(content)

    receipt = {
        "schema_version": 1,
        "generator": "Family-IP-Register deterministic generator",
        "generator_version": VERSION,
        "kind": kind,
        "job_file": job_path.name,
        "job_sha256": digest(job_bytes),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_refs": job.get("source_refs", []),
        "artifacts": [
            {"path": str(target.relative_to(output_dir.resolve())),
             "sha256": digest(content), "template": artifact["template"],
             "template_sha256": template_hash}
            for target, content, artifact, template_hash in rendered
        ],
        "review_status": "DRAFT_REQUIRES_HUMAN_REVIEW"
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    receipt_path = output_dir / "generation-receipt.json"
    if receipt_path.exists() and not force:
        raise GenerationError(f"Refusing to overwrite {receipt_path}; pass --force")
    receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    return [target for target, _, _, _ in rendered] + [receipt_path]

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--job", required=True, type=Path, help="JSON job specification")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--force", action="store_true", help="allow replacing existing outputs")
    args = parser.parse_args()
    try:
        for path in generate(args.job, args.output_dir, args.force):
            print(path)
    except (GenerationError, OSError) as exc:
        print(f"generation failed: {exc}", file=sys.stderr)
        return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
