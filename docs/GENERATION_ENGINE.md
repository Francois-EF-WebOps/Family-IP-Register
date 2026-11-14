# Generation Engine

**Status:** Deterministic template engine with shared identity registry; generated outputs remain drafts.  
**Location:** This engine lives inside Family-IP-Register. Do not create a second generator repository.

## Purpose

Generate repeatable first drafts for three artifact families from one JSON job format:
- editorial content;
- digital product briefs and sales-page drafts;
- software starter files (README, Python entry point, unit-test starter).

Every generation kind can reference the same identity records. The identity layer is shared; content formats and commercial properties remain distinct.

## Shared identity

Canonical source: `generation/identity/registry.json`.

The registry supports a master identity, personas/persona groups, characters, places, styles, visual systems, audio signatures, content formats, and reusable brand assets. It also records relationships, source references, and recovery status.

Recovered or referenced records currently include:
- Captain Narrator — Digital Voyager;
- Casual Duo — Everyday Adventurers;
- Meiling — Urban Operative;
- Fin and Nik, whose cast-continuity documentation exists in Blue-Sea-Print-Core;
- a separately tracked Tropical Adventurer Couple whose mapping to Casual Duo is unresolved;
- canonical presenter assets character_left.png and character_right.png, not located in the last recorded asset scan.

Their definitions are deliberately marked partial or unresolved. The registry does not invent the missing master-brand name, individual Duo member names, locations, visual specifications, or signature details. Do not equate Casual Duo with the Tropical Adventurer Couple without source evidence. Do not substitute Meiling or another character for the missing canonical presenter assets. Existing character sheets and source exports must be reconciled into the registry before those fields are treated as authoritative.

A job may reference registry IDs:

```json
{
  "kind": "content",
  "identity_refs": ["identity.master", "persona.captain-narrator"],
  "data": {
    "title": "Example",
    "audience": "Readers",
    "purpose": "Explain",
    "body": "Draft notes",
    "source_notes": "Sources to verify"
  }
}
```

Referenced records are available to templates under `identity.entities`, for example:

```
{{identity.entities.persona_captain_narrator.display_name}}
```

Unknown IDs and missing template values fail closed. The receipt records the exact identity IDs and SHA-256 hash of the registry used. This makes later identity changes traceable across all generated formats.

Identity references are optional during the transition. Do not claim a deliverable is brand-consistent merely because it was generated; only use identity fields that have been recovered and validated.

## Run

From the repository root:

```bash
python3 scripts/generate.py --job examples/jobs/content.example.json --output-dir build/generated/content
python3 scripts/generate.py --job examples/jobs/digital-product.example.json --output-dir build/generated/product
python3 scripts/generate.py --job examples/jobs/software.example.json --output-dir build/generated/software
python3 -m unittest discover -s tests
```

Use `--force` only when intentionally replacing prior generated files. Outputs should normally be written under an ignored local build directory; do not commit generated drafts automatically.

## Job contract

Each job is JSON with:
- `kind`: `content`, `digital_product`, or `software`;
- `data`: values substituted into the selected templates;
- `identity_refs`: optional IDs from the shared identity registry;
- `source_refs`: optional source identifiers or URLs to retain in the receipt.

Template tokens use `{{key}}` and dotted paths such as `{{project.name}}`. Missing values fail closed. Template text is treated as data; no shell, Python, or expression evaluation occurs.

## Provenance and controls

Every run writes `generation-receipt.json` with the job hash, template hashes, output hashes, generator version, timestamp, source references, identity registry hash and referenced identity IDs, and review status. This is traceability, not proof that sources are accurate or that rights are cleared.

- Output paths cannot be absolute or traverse outside the output directory.
- Existing outputs are not overwritten unless `--force` is supplied.
- No secrets, private family data, or confidential inputs belong in jobs or receipts.
- Generated content is always a draft; human review is mandatory before publication, release, or sale.
- Do not fabricate evidence, testimonials, prices, legal compliance, customer demand, or ownership.
- The engine does not publish, deploy, send messages, accept payments, or modify source projects.

## Extension contract

Add a new artifact family by adding templates and a catalog entry, plus tests and an example job. Keep generation deterministic and provider-neutral. Any model adapter must be optional, record model/provider and prompt/version metadata, and preserve the same review and rights gates.
