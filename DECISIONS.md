# Decision log

Use ISO dates (YYYY-MM-DD). Record decisions, evidence, owner of the action, and a review date. Correct errors transparently rather than silently rewriting history.

## 2026-10-31 — Register established

- **Decision:** establish a separate public repository for family-level IP inventory and stewardship.
- **Reason:** this is a cross-project governance layer, distinct from any one research or software repository.
- **Scope:** record projects, authorship/contribution evidence, licences, disclosure history, third-party rights, commercial signals, and protection decisions.
- **Boundary:** no private family records, credentials, identity data, or confidential source material in this public repository.
- **Status:** initial inventory is provisional and must be verified asset by asset.
- **Next action:** verify repository histories and licences, beginning with Dawny and EN125; record primary evidence and unresolved questions.

## 2026-10-31 — Shared family project standard adopted

- **Decision:** establish a common operating standard and asset manifest for the family project ecosystem.
- **Model:** one shared foundation, a governed reusable asset library, and independent product/research projects.
- **Reason:** make projects interoperable and consistently maintained without forcing them into one codebase, licence, architecture, or release cycle.
- **Controls:** asset-level provenance and rights checks; reusable/adaptable/restricted/unknown classifications; minimum documentation; proportionate quality, security, privacy, safety, and release gates.
- **Adoption:** pilot on Dawny first; then adapt the standard for EN125, BabelGlobalKreole, and MKC before wider rollout.
- **Boundary:** no mass repository restructuring until the Dawny pilot demonstrates which requirements are useful.
- **Status:** standard v1.0 published; adoption not yet tested in a project repository.
- **Next action:** use the scheduled Dawny and EN125 evidence review to establish the baseline, then apply the minimum viable standard to Dawny.


## 2026-11-01 — Dawny and EN125 evidence review

- **Decision:** record the repository evidence and unresolved rights questions for FIP-001 (Dawny-4pp), FIP-002 (Dawny-pup), and FIP-003 (EN125-Electric-Conversion-Canonical) in `REGISTER.md`.
- **Dawny finding:** the private repository contains a local FastAPI/SQLite planning prototype and an MIT licence file, but no live remittance integration or money movement. The public companion repository is empty at review. No public disclosure of Dawny-4pp implementation was evidenced in the inspected GitHub locations.
- **EN125 finding:** the root CC0 1.0 Universal licence text is present from the initial 2026-01-14 commit. Public Git history shows a high-level conversion concept, governance/structure documents, and a 2026-10-17/18 Cabo Verde research/planning package. The reviewed tree does not evidence a complete, validated conversion design. The cited `v1.0.0-canonical` tag reference does not resolve.
- **Authorship treatment:** sampled GitHub commit records identify the `Francois-EF-WebOps` account as author. This is account-level attribution only; it does not establish sole authorship, inventorship, or ownership.
- **Rights boundary:** no employment, client, contractor, educational, contributor-assignment, or third-party-rights records were available to complete either chain of title. Both project records therefore remain **Provisional**.
- **Disclosure boundary:** commit dates are recorded as Git-history dates, not proof of the exact date either repository first became public. No patentability or filing conclusion is made. No private Dawny commit SHAs, source code, credentials, personal information, or unpublished technical detail are reproduced in this public register.
- **Next action:** privately establish the creator/contributor and agreement history for both projects; confirm whether any employment/client obligations apply; reconcile the EN125 tag and divergent branch; and verify any disclosures outside GitHub before changing either record's status.


## 2026-11-26 — Shared architecture baseline established

- **Decision:** document one shared architecture for independent family projects, with FamilyOS as the first intended application-level proof rather than the exclusive owner of the architecture.
- **Canonical home:** Family-IP-Register; no new repository.
- **Existing foundations retained:** Project Standard, Operations Runtime, Generation Engine, shared identity registry, evidence/provenance records, and Universal Character Studio.
- **Architecture boundary:** shared capabilities are logical contracts, not mandatory microservices or a shared codebase. Each application retains its own domain rules, data classification, tests, licence and release cadence.
- **Principles:** local-first and Android-aware; human authority; least privilege; optional AI; portable data; explicit provenance; tested recovery; complexity must be justified by a demonstrated use case.
- **BorgIOS treatment:** external research reference only. No code, dependency, protocol or network component adopted. Its declared GPL-3.0 licence and inspected unsafe TLS/crypto patterns are recorded for future review.
- **Deferred:** peer discovery, distributed storage, shared remote memory, consensus, autonomous agent colonies, cloud control plane and mandatory hosted services.
- **Next action:** map one bounded FamilyOS workflow to existing capabilities and identify the minimum local data model and acceptance tests before implementation.
- **Status:** documentation baseline created on branch `docs/shared-architecture-foundation`; implementation and security guarantees are not claimed.
