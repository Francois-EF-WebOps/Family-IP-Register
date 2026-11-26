# Shared Architecture

**Status:** Initial architecture baseline — documentation only  
**Version:** 0.1.0  
**Canonical home:** Family-IP-Register  
**Scope:** Shared principles and interoperable capabilities for independent family projects

## Purpose

Define a common technical foundation that lets independent projects reuse trustworthy capabilities without forcing them into one application, repository, language, database, deployment model, or release cycle.

This is an architecture for our project family, not a new product or a replacement for each project's own architecture. FamilyOS is the first intended application-level proof, subject to a separate scoped implementation decision.

## Existing foundations — do not duplicate

- **Project governance and interoperability:** [PROJECT_STANDARD.md](PROJECT_STANDARD.md).
- **Portfolio operations:** [docs/OPERATIONS_RUNTIME.md](docs/OPERATIONS_RUNTIME.md) (control plane, runtime, workers, adapters and human approval).
- **Deterministic artifact generation:** [docs/GENERATION_ENGINE.md](docs/GENERATION_ENGINE.md) and [scripts/generate.py](scripts/generate.py).
- **Shared identity records:** [generation/identity/registry.json](generation/identity/registry.json).
- **Provenance and rights evidence:** [EVIDENCE.md](EVIDENCE.md), [REGISTER.md](REGISTER.md), asset manifests and generation receipts.
- **First local-first application:** [character-studio/](character-studio/).

The architecture extends these assets. It does not introduce a second identity registry, generator, agent framework, or portfolio runtime.

## Architectural model

### 1. Human and device layer

People remain the owners and approvers of consequential actions. Devices may include Android phones and later computers. A project must remain useful on its supported device without assuming a permanently connected service.

### 2. Foundation capabilities

- **Storage and portability:** ordinary files and documented formats; SQLite where structured local queries justify it.
- **Identity and trust:** stable identifiers, explicit relationships, authentication where required, and clear separation between identity facts and presentation.
- **Permissions and consent:** least privilege, explicit scope, revocable access, and human approval for consequential operations.
- **Security and privacy:** data minimisation, safe defaults, secret isolation, encryption when a real threat model requires it.
- **Recovery and integrity:** backups, checksums, version history, import/export and tested restore procedures.
- **Synchronization:** optional, conflict-aware exchange between devices; never silently overwrite canonical data.

### 3. Shared capabilities

- **Knowledge and records:** source-backed records, search indexes, archives and references.
- **Generation:** deterministic templates and renderers using the existing engine and identity registry.
- **Workflow and orchestration:** bounded task packets, state transitions, validation and approval gates.
- **Agents and AI adapters:** optional assistants that receive only scoped inputs and cannot bypass authorization.
- **Provenance and governance:** source, creator, licence, transformation, version, review and release records.

These are logical capabilities, not a requirement to deploy separate services or microservices.

### 4. Independent applications

Applications consume only the capabilities they need through documented interfaces. They own their user experience, domain rules, data classification, tests, operational risks and release decisions.

Initial mapping:

| Project | Architectural role | Boundary |
|---|---|---|
| FamilyOS / Family Sovereignty | First candidate application for household knowledge and operations | Private family data must remain outside this public repository; implementation scope still needs a separate decision |
| Universal Character Studio | Existing local-first identity/appearance application | Continue using the existing identity registry and provenance; no duplicate generator |
| BabelGlobalKreole | Evidence-led language research and data application | Preserve source IDs, dataset provenance and community/third-party rights |
| Dawny | Independent financial-workflow prototype | No shared autonomous payment capability; transaction records and real settlement must remain distinct |

## Integration contracts

Prefer the smallest stable boundary that fits the use case:

1. Versioned JSON schemas for structured exchange.
2. Markdown and ordinary files for human-readable records.
3. SQLite for local relational state when required.
4. Documented import/export before network APIs.
5. Explicit API contracts only when two independently maintained components need runtime communication.

Every shared contract must identify its owner, version, compatibility expectations, validation rules, data classification and migration approach. Do not share private application data merely because a common schema exists.

## Data flow and trust boundaries

- Treat imported files, external repositories, model output, generated content and network responses as untrusted input.
- Validate at the boundary; preserve source references and integrity metadata.
- Keep identity facts, mutable presentation, user preferences and generated outputs separate.
- Keep public architecture and provenance metadata free of family records, credentials, confidential material and patent-sensitive implementation details.
- An AI result is a proposal, never authorization or source-of-truth evidence.
- No worker may publish, spend, transfer funds, delete data, change rights, or contact an external party without explicit human approval.

## Deployment model

**Default:** one-device, local operation.

**Optional later:** encrypted backup, user-controlled synchronization, peer-to-peer exchange or hosted adapters, only where a demonstrated requirement justifies the added attack surface and maintenance burden.

A single-device implementation must not depend on discovery, consensus, distributed storage, an always-on agent, or a cloud control plane.

## Non-goals for this baseline

- Building a new operating system or general-purpose distributed platform.
- Replacing GitHub, Android, existing project stacks or the current generation engine.
- Introducing mandatory cloud hosting, paid APIs, telemetry or subscriptions.
- Autonomous agent colonies or unattended financial/publication actions.
- Migrating every project to a common codebase.
- Claiming security, privacy, resilience or interoperability without tests and evidence.

## Acceptance criteria for future implementation

A proposed shared capability is ready to implement only when it has:
- a real use case and named consuming project;
- a documented data owner and classification;
- a small interface and failure behaviour;
- a threat/privacy review proportionate to the data;
- a portable fallback or export path;
- tests demonstrating the claimed behaviour;
- a migration and rollback approach where existing data is affected.

## Related records

- [Architecture principles](docs/architecture/PRINCIPLES.md)
- [BorgIOS research record](docs/architecture/EXTERNAL_RESEARCH_BORGIOS.md)
- [Project standard](PROJECT_STANDARD.md)
- [Operations runtime](docs/OPERATIONS_RUNTIME.md)
- [Generation engine](docs/GENERATION_ENGINE.md)
- [Evidence standard](EVIDENCE.md)
