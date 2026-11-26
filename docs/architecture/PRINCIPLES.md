# Shared Architecture Principles

**Status:** Baseline v0.1.0  
**Applies to:** Shared capabilities and independent consuming projects

## 1. Local-first, not local-only

The core user journey must work on one supported device without network access. Remote services may extend the system but cannot be mandatory for basic access to locally held records.

## 2. Human ownership and agency

The human data owner controls access and consequential actions. Automation may prepare, validate and recommend. It does not grant itself authority.

## 3. Data before agents

Canonical state lives in inspectable, versioned data and deterministic code. AI is optional, replaceable and downstream of evidence. Never make model memory the only copy of a fact or decision.

## 4. Least privilege by default

Every component receives only the data and operations needed for its task. Read-only is the default for discovery and analysis. Write access is explicit, narrow, logged and revocable.

## 5. Independent projects, interoperable boundaries

A shared standard does not require a shared codebase. Prefer versioned schemas, portable files and documented APIs over hidden imports, shared mutable databases or forced monorepos.

## 6. Privacy by separation

Separate public project metadata, private personal records, confidential source material, credentials and potentially patent-sensitive details. A public repository must never become the family's private database.

## 7. Provenance travels with the artifact

Preserve source references, creators/contributors, licence and rights status, transformation history, tool/version metadata, review state and output hashes where appropriate. Provenance supports review; it does not prove ownership or accuracy by itself.

## 8. Fail closed

Unknown identity references, invalid schemas, unsafe paths, missing permissions, unresolved conflicts and unverifiable claims must not silently become accepted state.

## 9. Recovery is part of correctness

Define export, backup, restore, integrity checking and conflict handling before claiming that information is resilient. A backup that has never been restored is unverified.

## 10. Complexity must earn its place

Do not add distributed storage, peer discovery, consensus, autonomous agents, microservices or hosted infrastructure until a concrete user requirement cannot be met more simply.

## 11. Android-first accessibility

For user-facing applications, support small screens, touch interaction, low bandwidth and practical use from Android browsers. Do not make a desktop development environment a prerequisite for ordinary use.

## 12. Evidence over architecture claims

Mark capabilities as proposed, implemented, tested or verified. A design document is not implementation evidence. Each claimed guarantee needs a test, inspection record or clearly stated limitation.

## Decision test

Before adding a shared component, answer:

1. Which current project needs it?
2. What real workflow does it improve?
3. Can an existing component already do it?
4. What data and authority does it require?
5. What happens offline or when it fails?
6. How can the user export, recover or replace it?
7. What measurable test proves it works?

If these questions have no concrete answers, defer the component.
