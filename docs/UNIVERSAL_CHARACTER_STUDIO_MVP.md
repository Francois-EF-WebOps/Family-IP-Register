# Universal Character Studio — Copilot implementation task

## Objective
Build the first usable, mobile-first Character Builder Studio capability by extending this repository. This is implementation work, not an architecture-only exercise.

Product promise: **Create once. Extend endlessly. Keep the identity.**

## Repository context
Existing foundations to reuse:
- `generation/identity/registry.json`: shared identity registry. Fin and Nik currently exist as records requiring source reconciliation; do not overwrite them with guessed attributes.
- `scripts/generate.py`: deterministic local-first Python generation engine.
- `generation/catalog.json` and existing templates: generation catalog and artifact templates.
- `tests/test_generate.py`: existing test conventions and safety checks.
- `assets/fin-and-nik/README.md`: provenance and canon record.
- Canonical creative source: `ai-music-provenance/projects/fin-and-nik/README.md` in the separate ai-music-provenance repository. Do not copy unverified images or invent reference-image locations.

## Required first release (MVP)
1. Inspect the repository and identify the smallest compatible way to provide a usable browser UI. Reuse an existing app stack if one exists. If none exists, choose a minimal dependency-light approach; document the decision.
2. Define a versioned Character Definition Model (CDM) in a machine-readable schema. Separate:
   - stable identity: character ID, species/type, body proportions, face/eyes/hair anchors, distinctive features;
   - mutable appearance: clothing, accessories, palette and styling;
   - personality/behaviour: traits, expressions and gestures;
   - references and provenance: source refs, creator/source notes, licensing status, generated asset refs, timestamps and review state;
   - version and schema metadata.
3. Include two fictional fixtures, Fin and Nik, using only facts already documented in this repository and the canonical Fin & Nik README. Mark uncertain or missing fields as unknown/empty; do not invent details. Keep the current registry as the identity source of truth and add structured details through a traceable, reviewed change.
4. Build an interactive SVG renderer that uses the CDM, not hard-coded character names. It must render a recognizable stylized placeholder character with configurable body, face, hair, clothing and accessories. A user must be able to change clothing/accessories without changing stable identity fields.
5. Build a responsive character editor with controls for the supported attributes, live preview, save/load locally, and a clear distinction between identity fields and appearance fields.
6. Support export of the character definition as JSON and a printable/downloadable SVG character sheet. Include a visible draft/review state and provenance details in the exported data.
7. Add validation and automated tests proving:
   - schema validation and stable IDs;
   - appearance edits do not mutate identity fields;
   - the same definition produces deterministic SVG output;
   - unknown or malformed fields fail safely;
   - JSON and SVG exports contain the expected identity/provenance data.
8. Update README/docs with setup, run, test, mobile usage, limitations, and a short demo workflow.

## Architecture boundaries
- SVG is the first renderer and must be deterministic. Keep renderer interfaces modular so Three.js can be added later without changing the CDM.
- Do not add Three.js, Blender, image-generation APIs, Python graphics dependencies, or a backend unless the repository inspection proves they are necessary for this MVP. Record a small follow-up plan for 3D rather than expanding scope.
- AI image generation is optional and explicitly out of scope for this first release. No API keys, paid services, or network calls.
- No user accounts, cloud sync, payments, subscriptions, analytics, or multi-user collaboration in this MVP.
- Do not create another repository or a second identity registry.
- Do not claim that procedural SVG can reproduce photorealistic character identity. State the visual limitations.

## Design and usability
- Mobile-first layout, usable on a phone in portrait orientation.
- Clear controls, readable labels, accessible contrast, keyboard focus, and touch targets.
- Preview must update immediately when supported appearance attributes change.
- Make the identity/appearance boundary obvious in the UI.
- Use fictional demo content only; never include family photos or private personal data.

## Delivery requirements
- Work only on the assigned feature branch.
- Implement the smallest complete vertical slice; do not stop after writing a plan.
- Run all relevant tests and report exact results. Fix failures caused by your changes.
- Provide a concise summary of changed files, how to run the app, how to test it, and what remains.
- Open a pull request against main. Do not merge it.
- If blocked by missing source assets or unclear canon, keep the field explicitly unresolved and continue with the renderer/editor using neutral placeholder values.
