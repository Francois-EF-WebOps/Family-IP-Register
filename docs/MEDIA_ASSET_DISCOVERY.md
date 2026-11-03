# Media and Character Asset Discovery

**Status:** Initial discovery register. No canonical presenter-character/persona source files have yet been verified.
**Prepared:** 2026-11-03

## Purpose

Locate the already-designed presenter characters, persona definitions, voice references, and reusable media across existing repositories. This is a discovery index, not a replacement asset library. Preserve source files in their original repositories.

## Verified leads

| Lead | Exact source | Verified | Not yet verified | Status |
|---|---|---|---|---|
| Artist persona schema | [ai-music-provenance/schema/persona.schema.json](https://github.com/Francois-EF-WebOps/ai-music-provenance/blob/bbc5c571debf22c5f1daf2a5ce4e1652915d6d36/schema/persona.schema.json), commit [bbc5c57](https://github.com/Francois-EF-WebOps/ai-music-provenance/commit/bbc5c571debf22c5f1daf2a5ce4e1652915d6d36) | Schema supports human_artist, virtual_character, collective, and project_alias; includes fictional bio and voice/likeness reference fields. | No actual persona instance or linked character artwork was found in the inspected commit. | Schema verified; instances unknown |
| MKC creative references | [ARTS_AND_CULTURAL_KNOWLEDGE.md](https://github.com/Francois-EF-WebOps/mascarene-knowledge-commons/blob/main/docs/ARTS_AND_CULTURAL_KNOWLEDGE.md) | Explicitly names My Voice Lab TTS, Babel Creole / “Down by the Shore”, music catalogue preservation, and AI-assisted media. | The document says the source projects remain separate and require inventory; it does not identify presenter files. | References verified; assets unlocated |
| MKC production model | [KNOWLEDGE_TO_DISTRIBUTION_SYSTEM.md](https://github.com/Francois-EF-WebOps/mascarene-knowledge-commons/blob/main/docs/KNOWLEDGE_TO_DISTRIBUTION_SYSTEM.md) | Defines a multimedia/social distribution pipeline and minimum asset-record fields. | It is a workflow specification, not a character inventory. | Process verified; assets unlocated |
| Prompt reference library | [Ultimate-Nano-Banana-Pro-Collection.-Fr](https://github.com/Francois-EF-WebOps/Ultimate-Nano-Banana-Pro-Collection.-Fr) | Contains a large collection of externally attributed image-generation prompts, including character/portrait examples. | These examples are not confirmed as the user's established presenter cast or original artwork. | Reference only |
| Man and woman cutouts discussed in chat | Current conversation image history | A separate man and woman were discussed; the man cutout had missing/jagged lower legs and background remnants. | Original file paths, final approved artwork, and canonical repository are not known from this pass. | Chat lead; source files unknown |

## Candidate repositories

These are inspection targets, not claims that the assets are present:

1. `ai-music-provenance` — persona instances, voice references, and provenance records.
2. `10COgraphie` — creative archive and media references; current README mainly identifies an AI Studio app scaffold.
3. `Blue-Sea-Print` and `Blue-Sea-Print-Core` — illustration and educational media.
4. `Ultimate-Nano-Banana-Pro-Collection.-Fr` — distinguish original designs from third-party prompt references.
5. `Francois-Essaie`, `Elbaph-OS`, `Louis`, `Marani`, and `editor` — inspect for embedded visual assets, storyboards, and media.
6. Resolve the exact repositories behind My Voice Lab TTS and “Down by the Shore” before assuming they contain the presenter personas.

## Index fields

For each discovered asset, record:

- stable asset ID and name;
- role: presenter, character, narrator, voice, pose, expression, storyboard, animation, background, music, or other;
- canonical repository, exact path, and immutable commit/tag;
- source type: original, adaptation, third-party reference, generated derivative, or unknown;
- linked persona and voice reference;
- format and dimensions/duration where relevant;
- rights, licence, consent, attribution, and restrictions;
- status: located, inspected, approved, rights-reviewed, animation-ready;
- known defects and next action.

## Guardrails

- Do not invent, rename, or redesign established personas during discovery.
- Do not substitute generic prompt-library characters for the existing cast.
- Do not move, overwrite, or duplicate original media.
- Treat filename matches as leads, not proof of identity.
- Keep private family information and confidential source material out of this public register.

## Current limitation and next action

The connected GitHub code-search index does not cover enough of the candidate repositories to establish a complete file inventory. The next technical step is a read-only, contents-level inventory of candidate repository paths and file metadata, followed by targeted inspection of likely persona sheets and media manifests. Do not begin the animation build until the canonical man/woman artwork and linked persona/voice references are located.
