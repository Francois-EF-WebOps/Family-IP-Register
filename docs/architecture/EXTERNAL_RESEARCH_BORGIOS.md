# External Architecture Research: BorgIOS

**Status:** Concept review recorded; no code adopted  
**Reviewed source:** [bitmonky/BorgIOS](https://github.com/bitmonky/BorgIOS)  
**Related interface project:** [bitmonky/borgHUI](https://github.com/bitmonky/borgHUI)  
**Purpose:** Record useful architectural questions and implementation cautions without creating a dependency or copying code.

## Source characterization

BorgIOS describes itself as an experimental peer-to-peer/distributed operating-system concept involving peer networking, cryptographic identity, distributed storage, shared memory and AI agents. Its README describes a multi-node experimental network. These are project-author descriptions, not independent production validation.

The repository declares GPL-3.0. This record adopts no BorgIOS source code. Any future code reuse requires a separate compatibility and attribution review. Architectural ideas and independently written specifications must not be confused with permission to copy implementation.

## Concept assessment

| External concept | Our treatment | Reason / condition |
|---|---|---|
| Cryptographic identity | Adapt as a design topic | Separate authentication, identity claims, device identity and authorization; a keypair alone does not establish real-world identity or permission |
| Peer-to-peer networking | Defer | No demonstrated multi-device requirement currently outweighs complexity |
| Distributed shards/storage | Defer | First define local storage, backup, integrity, deletion and recovery |
| Shared persistent memory | Redesign | Explicit ownership, data classification, access scope, retention and deletion are prerequisites |
| Agent colonies / autonomous agents | Reject as default | Agents must be bounded workers; human approval remains required for consequential actions |
| Self-healing network | Research only | Define measurable failure modes and recovery tests before claiming resilience |
| Resource accounting | Consider if needed | Adopt only if a real workload requires quotas or resource governance |

## Security observations from inspected source

The inspected source contains patterns that must not be copied into our architecture:

- A peer networking file sets Node.js TLS certificate verification off globally (NODE_TLS_REJECT_UNAUTHORIZED=0).
- The browser conduit includes HTTPS requests configured with rejectUnauthorized: false.
- An agent code path uses legacy password-based crypto APIs and automated activation patterns.

These observations are limited to the inspected files and revision; they are not a complete security audit of BorgIOS. They are sufficient to reject those patterns as defaults in our own systems.

The repository's descriptions of distributed memory and agent behaviour do not establish end-to-end confidentiality, access isolation, secure deletion, or safe execution. Those properties would require separate design evidence and adversarial testing.

## Independent design decisions

1. Keep our canonical records in portable local files and existing project stores.
2. Reuse the current identity registry and generation receipts; do not create parallel registries.
3. Keep agents read-only unless a human grants a bounded write operation.
4. Require authenticated, certificate-verified transport for any future network integration.
5. Define encryption, key ownership, rotation, recovery and threat model before storing sensitive data remotely.
6. Make synchronization explicit and conflict-aware; never assume replicated data is automatically trustworthy.
7. Require offline usefulness before considering distributed availability a feature.

## Research sources

- [BorgIOS README](https://github.com/bitmonky/BorgIOS/blob/main/README.md)
- [BorgIOS licence](https://github.com/bitmonky/BorgIOS/blob/main/LICENSE)
- [PeerTree source](https://github.com/bitmonky/BorgIOS/blob/main/nodeJS/src/peerTree.js)
- [Agent brain source](https://github.com/bitmonky/BorgIOS/blob/main/nodeJS/src/borgAgentBrain.js)
- [borgHUI README](https://github.com/bitmonky/borgHUI/blob/main/README.md)
- [borgHUI conduit source](https://github.com/bitmonky/borgHUI/blob/main/borgHUIconduit.js)

## Limitations and follow-up

This is a targeted concept and source-pattern review, not a complete code audit, licence opinion, penetration test or interoperability assessment. Before any technical adoption, inspect the exact source revision, dependencies, licences and threat model again.

**Current decision:** use BorgIOS as a research reference only. No dependency, code, protocol or network component is adopted.
