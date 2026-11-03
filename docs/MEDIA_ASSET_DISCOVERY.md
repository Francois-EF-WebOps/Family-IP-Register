# Media and Character Asset Discovery

**Status:** Initial discovery register — no character/persona source files have yet been verified.
**Prepared:** 2026-11-03
**Purpose:** Locate existing presenter characters, persona definitions, voice references, and reusable media across the existing portfolio without copying or replacing source assets.

## Search result summary

The connected GitHub account exposes 20 repositories in the current repository listing. GitHub code search returned no matches for the broad character/persona/animation queries used in this pass. This is not proof that the files do not exist: most candidate repositories are not marked as code-search indexed, and some private repositories may require a different access path.

### Verified leads

| Lead | Exact location | What is verified | What is not verified | Status |
|---|---|---|---|---|
| Artist persona schema | [ai-music-provenance/schema/persona.schema.json](https://github.com/Francois-EF-WebOps/ai-music-provenance/blob/bbc5c571debf22c5f1daf2a5ce4e1652915d6d36/schema/persona.schema.json) at commit [bbc5c57](https://github.com/Francois-EF-WebOps/ai-music-provenance/commit/bbc5c571debf22c5f1daf2a5ce4e1652915d6d36) | JSON Schema supports artist identity types including virtual_character, fictional bio, voice/likeness reference, permission evidence, and disclosure notes. | No actual character/persona record or associated image/audio asset was found in the inspected commit. | VERIFIED SCHEMA; INSTANCE UNKNOWN |
| MKC creative coordination | [docs/ARTS_AND_CULTURAL_KNOWLEDGE.md](https://github.com/Francois-EF-WebOps/mascarene-knowledge-commons/blob/main/docs/ARTS_AND_CULTURAL_KNOWLEDGE.md) | Names My Voice Lab TTS, Babel Creole / “Down by the Shore”, music catalogue preservation, and AI-assisted media as coordination points. | The document explicitly says source projects remain separate and must be inventoried; no character files or persona sheets are identified there. | VERIFIED REFERENCES; ASSETS UNLOCATED |
| MKC distribution model | [docs/KNOWLEDGE_TO_DISTRIBUTION_SYSTEM.md](https://github.com/Francois-EF-WebOps/mascarene-knowledge-commons/blob/main/docs/KNOWLEDGE_TO_DISTRIBUTION_SYSTEM.md) | Defines a multimedia/social distribution pipeline and minimum asset metadata. | It is an operating model, not an inventory of the actual characters. | VERIFIED PROCESS; ASSETS UNLOCATED |
| Prompt reference collection | [Ultimate-Nano-Banana-Pro-Collection.-Fr](https://github.com/Francois-EF-WebOps/Ultimate-Nano-Banana-Pro-Collection.-Fr) | Repository contains a large prompt library with character/portrait prompt examples. | These are not confirmed to be the user's original presenter characters; many entries are attributed to external sources. Do not treat them as source artwork or reuse them as the established cast. | REFERENCE ONLY |
| Existing character cutouts from current conversation | Current conversation attachments / image-generation history | User has discussed separate man and woman cutouts; the man version had incomplete lower legs/feet and background remnants. | The original source file, canonical repository, and final approved versions are not identified in this GitHub pass. | CHAT CONTEXT; SOURCE FILE UNKNOWN |

## Candidate repositories to inspect next

These are leads based on existing project references and repository purpose, not claims that the assets are present:

1. `ai-music-provenance` — inspect persona instances, artist/virtual identity records, voice references, and provenance metadata.
2. `10COgraphie` — inspect creative archive and any linked media/prompt records; the current README primarily identifies an AI Studio app scaffold.
3. `Ultimate-Nano-Banana-Pro-Collection.-Fr` — distinguish reference prompts from original character designs; do not adopt unrelated prompt examples.
4. `Blue-Sea-Print` and `Blue-Sea-Print-Core` — inspect illustration, educational media, and reusable visual assets.
5. `Francois-Essaie`, `Elbaph-OS`, `Louis`, `Marani`, and `editor` — inspect for app-embedded character assets, storyboards, and media files.
6. Private project references in MKC — resolve the exact repository and path for My Voice Lab TTS and the “Down by the Shore” work before assuming either contains presenter personas.

## Required index fields

Each discovered asset should be recorded with:

- stable asset ID and display name;
- asset role: presenter / character / narrator / voice / pose / expression / storyboard / animation / background / music / other;
- canonical repository, exact path, and immutable commit or release;
- source type: original / adaptation / third-party reference / generated derivative / unknown;
- linked persona record and voice reference, if any;
- file format, dimensions or duration where relevant;
- rights, licence, consent, attribution, and restrictions;
- status: located / inspected / approved / rights-reviewed / animation-ready;
- known defects and next action.

## Guardrails

- Do not invent or rename established personas.
- Do not substitute generic prompt-library characters for the user's existing cast.
- Do not modify, move, or duplicate original media during discovery.
- Treat third-party prompt examples and images as references until rights and provenance are established.
- Keep private family information and non-public source material out of this public-facing register.
- A filename match is a lead, not proof that an asset is the intended character.

## Next execution step

Obtain a read-only, contents-level inventory of the candidate repositories (file paths and metadata only), then fetch only likely persona sheets and media manifests. The present connector's code search does not cover enough repositories to complete that inventory. No broad media copy or animation build should begin until the canonical man/woman artwork and their persona/voice references are located.
