# Copilot instructions — Family-IP-Register

## Project role
This repository is the shared, local-first source of truth for family IP records, identity definitions, deterministic generation, provenance, and reusable generation workflows. Universal Character Studio is an application capability built on these foundations, not a reason to create a duplicate repository.

## Working rules
- Read the existing README, architecture docs, generation catalog, identity registry, generator, and tests before editing.
- Reuse existing schemas, IDs, utilities, and provenance mechanisms. Do not duplicate the identity registry or generation engine.
- Treat Git and versioned files as the source of truth. AI is optional and replaceable; deterministic code must work without an AI provider, API key, network call, or subscription.
- Keep private family information, credentials, tokens, and personal data out of public files, logs, tests, and generated examples.
- Use fictional demo characters only. Fin and Nik may be used as fictional test fixtures based only on their documented fictional canon.
- Preserve source attribution, licensing, provenance, human-review status, and version history. Never claim copyright ownership, exclusivity, clearance, or commercial rights without evidence.
- Prefer small, reviewable changes. Do not rewrite unrelated systems, rename existing identifiers, or create a new repository.
- Do not add paid APIs, mandatory hosted services, telemetry, tracking, or dependencies that require a subscription.
- Keep the experience responsive and usable on Android/mobile browsers, with accessible labels, keyboard support, and sensible touch targets.
- Validate inputs and fail closed on malformed data, unknown identity references, unsafe paths, and unsupported output formats.
- Add tests for every new schema, renderer, export, and validation rule. Run the existing test suite and report exact commands and outcomes.
- Do not mark work complete if tests were not run. Do not silently skip failing tests.
- Never merge, publish, deploy, or change repository settings. Work on the assigned branch and open a pull request for human review.

## Product direction
Universal Character Studio: create a character once, approve a canonical identity, then extend it into consistent views, expressions, poses, outfits, scenes, and eventually 3D/animation. Keep identity separate from changeable appearance. A renderer or AI provider must never become the canonical source of identity.

## Definition of done
A working, testable increment beats a broad plan. Include screenshots or a short demo description where possible, update documentation, explain limitations honestly, and list remaining work.
