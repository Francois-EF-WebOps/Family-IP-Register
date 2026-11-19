# Universal Character Studio — MVP 0.1

A mobile-first, local-first character editor inside Family-IP-Register.

**Promise:** Create once. Extend endlessly. Keep the identity.

## Run

Open `index.html` through a local static server or GitHub Pages. For example, from the repository root:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000/character-studio/`. No build step, package manager, backend, account, API key, or subscription is required.

## Use

1. Choose Fin or Nik.
2. Review the source-backed identity summary (read-only).
3. Change garment colour/style or toggle the documented accessory.
4. Save the appearance locally in the current browser, or export JSON/SVG.
5. Treat every export as a draft pending human review.

## Data boundaries

- Fixture identity facts are transcribed from `assets/fin-and-nik/README.md`.
- Body proportions remain unknown; the SVG uses a generic placeholder body and does not claim to match a canonical reference sheet.
- Appearance controls change only the `appearance` object.
- Loading a local save restores identity from the checked-in fixture and applies only saved appearance values.
- Local saves use browser localStorage and do not sync between devices.
- JSON exports preserve source references, licensing status and review state.

## Limitations

This first release is a procedural SVG editor, not an AI image generator, photorealistic character-consistency system, 3D modeller, animation tool, or collaborative service. The SVG uses simplified generic shapes; skin/hair drawing values are illustrative render choices, not a full colour specification or source-approved palette. Nik's embroidery and Fin's documented lower-garment details are not yet reproduced faithfully in the renderer.

The fixture records remain marked `SOURCE_RECONCILIATION_REQUIRED`. This tool does not establish copyright ownership, licensing clearance, or commercial rights. Do not publish or sell generated character sheets without source and rights review.

## Technical shape

- Static HTML/CSS/JavaScript; no third-party runtime dependencies.
- Versioned fixture data in `characters.json`.
- Deterministic SVG string renderer in `studio.js`.
- Stable identity and mutable appearance stored separately.
- Future renderers (including Three.js) should consume the same character definition; do not make renderer output the source of truth.

## Next engineering increments

1. Add automated browser-level tests for SVG output and appearance/identity separation.
2. Reconcile exact canonical character-sheet references and review fixture fields against them.
3. Add expressions and pose controls only after source-backed anchor definitions exist.
4. Validate real buyer demand with one paid character-sheet pilot before expanding into 3D or subscriptions.
