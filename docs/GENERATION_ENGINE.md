# Generation Engine

**Status:** Initial deterministic implementation; template output only.  
**Location:** This engine lives inside Family-IP-Register. Do not create a second generator repository.

## Purpose

Generate repeatable first drafts for three artifact families from one JSON job format:
- editorial content;
- digital product briefs and sales-page drafts;
- software starter files (README, Python entry point, unit-test starter).

The initial engine uses Python's standard library only. It does not call an AI model, network service, paid API, or publishing platform. AI-assisted generation can be added later as an optional adapter, never as a required runtime dependency.

## Run

From the repository root:

\x60\x60\x60bash
python3 scripts/generate.py --job examples/jobs/content.example.json --output-dir build/generated/content
python3 scripts/generate.py --job examples/jobs/digital-product.example.json --output-dir build/generated/product
python3 scripts/generate.py --job examples/jobs/software.example.json --output-dir build/generated/software
python3 -m unittest discover -s tests
\x60\x60\x60

Use `--force` only when intentionally replacing prior generated files. Outputs should normally be written under an ignored local build directory; do not commit generated drafts automatically.

## Job contract

Each job is JSON with:
- `kind`: `content`, `digital_product`, or `software`;
- `data`: values substituted into the selected templates;
- `source_refs`: optional source identifiers or URLs to retain in the receipt.

Template tokens use `{{key}}` and dotted paths such as `{{project.name}}`. Missing values fail closed. Template text is treated as data; no shell, Python, or expression evaluation occurs.

## Provenance and controls

Every run writes `generation-receipt.json` with the job hash, template hashes, output hashes, generator version, timestamp, source references, and review status. This is traceability, not proof that sources are accurate or that rights are cleared.

- Output paths cannot be absolute or traverse outside the output directory.
- Existing outputs are not overwritten unless `--force` is supplied.
- No secrets, private family data, or confidential inputs belong in jobs or receipts.
- Generated content is always a draft; human review is mandatory before publication, release, or sale.
- Do not fabricate evidence, testimonials, prices, legal compliance, customer demand, or ownership.
- The engine does not publish, deploy, send messages, accept payments, or modify source projects.

## Extension contract

Add a new artifact family by adding templates and a catalog entry, plus tests and an example job. Keep generation deterministic and provider-neutral. Any model adapter must be optional, record model/provider and prompt/version metadata, and preserve the same review and rights gates.
