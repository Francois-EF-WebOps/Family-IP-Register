# Family Project Standard

**Version:** 1.0  
**Status:** Initial operating standard  
**Applies to:** Family projects, repositories, research collections, products, and shared assets  
**Purpose:** Make independent projects interoperable without forcing them into one product or one technical architecture.

## 1. Product-family model

Treat the portfolio as a small technology and creative group with three layers:

1. **Family foundation** — shared principles, project identity, documentation conventions, evidence and provenance practices, security expectations, accessibility, contribution rules, and asset-reuse procedures.
2. **Shared asset library** — reusable components, code, schemas, templates, design elements, research methods, media, and operational workflows. Every asset has its own provenance and reuse conditions.
3. **Independent projects** — products and research initiatives with their own users, purpose, architecture, roadmap, licence, release cadence, and risk profile.

A shared standard does not mean a shared codebase. Projects may use different languages, frameworks, hosting, and licences where their needs justify it.

## 2. Core rules

- Keep each project independently understandable, buildable, and maintainable where practical.
- Reuse a shared asset only after checking its creator, rights, licence, dependencies, privacy, safety, and suitability.
- Do not copy credentials, personal data, confidential information, client material, or restricted third-party assets into shared repositories.
- Do not claim a feature is implemented because it appears in a plan, mock-up, generated scaffold, or README.
- Label evidence, assumptions, unknowns, and validation status separately.
- Make the smallest useful release; avoid imposing enterprise-scale process on a small project.
- Record external demand honestly: actual users, buyers, employers, partners, payments, and contracts are different from interest or internal enthusiasm.

## 3. Minimum project documentation

Every active project should have the following documents. Use the minimum set that fits the project; mark genuinely inapplicable sections rather than creating empty boilerplate.

| File | Required content |
|---|---|
| `README.md` | What it is, who it serves, current status, quick start, links to key documents, licence |
| `PROJECT.md` | Problem, intended users, scope, non-goals, success criteria, current milestone |
| `ARCHITECTURE.md` | Main components, data flows, trust boundaries, external services, important decisions |
| `ASSETS.md` | Asset inventory and reuse classification; link to detailed manifest where needed |
| `EVIDENCE.md` | Sources, tests, validation, provenance, known limitations, unresolved claims |
| `LICENSE` | Exact licence text, or an explicit statement that no licence has been granted |
| `CONTRIBUTING.md` | How to propose changes, test work, report issues, and document contributions |
| `CHANGELOG.md` | User-visible changes by release or dated milestone |

Use `docs/` for longer guides, research notes, decisions, and reference material; `src/` or the framework's conventional source directory for implementation; and `tests/` for automated checks. Do not reorganise a working project merely to match this directory example.

### Project-specific additions

Add only what the project needs, for example:

- `THREAT_MODEL.md` for products handling accounts, money, personal data, devices, or privileged operations.
- `SAFETY.md` for physical, health, environmental, or emergency-related guidance.
- `DATA_DICTIONARY.md` and source registers for datasets and research.
- `CONTENT_RIGHTS.md` for music, images, text, video, and generated media.
- `OPERATIONS.md` for deployment, backup, recovery, monitoring, and support.
- `API.md` for a public or internal interface.

## 4. Project identity and status

Every README must state:

- Canonical project name and one-sentence purpose.
- Intended users or audience.
- Current status: **concept**, **prototype**, **alpha**, **beta**, **released**, **maintenance**, or **archived**.
- What currently works and what does not.
- The next verifiable milestone.
- Licence and contribution route, if applicable.

Use status labels accurately. A repository being public does not mean the product is released, safe, complete, validated, or supported.

## 5. Architecture and interoperability

Projects should integrate through documented, stable boundaries rather than hidden coupling.

Preferred shared interfaces include:

- Versioned JSON/CSV schemas with examples and validation.
- Documented APIs and export/import formats.
- Portable assets with explicit file formats and metadata.
- Small reusable libraries with tests and dependency declarations.
- Human-readable records that remain useful without a particular app or vendor.

For every shared interface, record its owner/maintainer, version, compatibility expectations, and migration approach. Avoid a central service becoming a single point of failure unless the product genuinely requires one.

## 6. Asset reuse protocol

Before copying, adapting, publishing, or selling an asset, create or update its record using [ASSET_MANIFEST_TEMPLATE.md](ASSET_MANIFEST_TEMPLATE.md).

Classify each asset:

- **REUSABLE** — rights and licence permit the intended reuse; provenance and dependencies are recorded.
- **ADAPTABLE** — reuse may be possible after attribution, permission, compatibility, privacy, safety, or validation work.
- **RESTRICTED** — do not reuse or redistribute without explicit clearance. Examples include confidential/client material, personal data, credentials, third-party content without adequate rights, and potentially patent-sensitive details.
- **UNKNOWN** — rights or provenance have not been established. Treat as restricted until reviewed.

A repository-level licence does not automatically cover every image, dataset, font, recording, model output, dependency, or contribution inside it. Check asset-level rights.

When reusing an asset, preserve required notices and attribution, record the source version/commit, record modifications, and identify the consuming project. Do not silently transfer a licence or imply endorsement by the original project.

## 7. Quality gates

A project may use a lightweight checklist. Do not claim a gate passed unless evidence exists.

### Gate A — Before public contribution
- Scope and status are clear.
- Licence and contribution expectations are clear.
- No secrets, private family data, or unauthorised third-party content are present.
- Setup and test instructions are usable.

### Gate B — Before release
- Core user journey has been tested.
- Known limitations and risks are documented.
- Dependencies and licences have been reviewed.
- Release notes and version are recorded.
- Backup, rollback, or recovery expectations are defined where relevant.

### Gate C — Before asset reuse
- Creator and provenance are known or uncertainty is stated.
- Licence/permission covers the intended use.
- Dependencies and third-party rights are checked.
- Privacy and safety implications are checked.
- Source and changes are recorded in the consuming project.

### Gate D — Before commercial use
- A real user/customer/employer need is identified.
- Ownership and contractual obligations are checked.
- Pricing, support, delivery, and operational costs are understood.
- Regulatory, safety, and consumer obligations are assessed where relevant.
- No claim of certification, endorsement, or compliance is made without evidence.

## 8. Security, privacy, and safety baseline

- Never commit API keys, passwords, signing keys, access tokens, private keys, or production credentials.
- Use environment variables or an appropriate secret manager; provide safe example configuration only.
- Minimise personal data. Do not put family or children's private information in public repositories.
- Define data retention, deletion, backup, and access controls for systems that store personal information.
- Treat external input, generated content, model output, and imported files as untrusted until checked.
- Physical-world instructions require appropriate validation and prominent limitations. Unvalidated survival, medical, electrical, vehicle, or other hazardous guidance must not be presented as safe operational instruction.
- Products involving money must clearly distinguish records, quotes, authorisations, and confirmed settlement. Never simulate a successful real-world transaction.

## 9. Contribution and change management

- Use issues or a written change proposal for material changes.
- Keep changes small enough to review.
- Add or update tests when behaviour changes.
- Record decisions that affect interfaces, data, licences, safety, or long-term maintenance.
- Credit contributors accurately; do not assume a contribution is assigned to the repository owner.
- Use version control history and release tags as evidence, not as the sole proof of authorship or ownership.

## 10. Adoption plan

Do not retrofit every repository at once.

1. Apply this standard to **Dawny** as the first product pilot.
2. Identify which documents and gates are genuinely useful; record exceptions.
3. Review **EN125** as a documentation/research project, not as a software product.
4. Apply the appropriate subset to **BabelGlobalKreole** and **MKC**.
5. Roll out by project type in small batches.

The standard itself should evolve from practical use. Propose revisions with a reason, an example, and the projects affected.