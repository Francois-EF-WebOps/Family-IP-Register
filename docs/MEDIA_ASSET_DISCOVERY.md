# Media and Character Asset Discovery

**Status:** Initial discovery register — character/persona source material has been located in archived conversations; canonical production files still need recovery and validation.
**Prepared:** 2026-11-03

## Purpose

Locate the already-designed presenter characters, persona definitions, voice references, and reusable media across existing repositories. This is a discovery index, not a replacement asset library. Preserve source files in their original repositories.

## Discovery coverage

The connected GitHub account exposes **25 repositories**. A read-only recursive file-path scan was completed across those repositories. It found a small number of relevant media or archive leads, but no dedicated central character library or clean presenter-asset directory. Filename/code search alone was insufficient; archived conversation exports contained important character definitions.

## Verified leads

| Lead | Exact source | Verified | Status |
|---|---|---|---|
| Meiling character sheet | [xanat/chat (4).html](https://github.com/Francois-EF-WebOps/xanat/blob/main/chat%20(4).html), conversation **“Meiling Character Sheet Update”** | A detailed character sheet and 3D-model illustration specification are embedded in the archived conversation. It defines her core identity, visual canon, outfit states, movement, personality, rigging/pose, materials, and turnaround requirements. The conversation also records several reference-image attachments. | Character definition located in chat archive; standalone canonical sheet and source images not recovered into a dedicated asset path. Treat attached photo references as restricted pending consent/rights review. |
| Character A face descriptor | [xanat/chat (4).html](https://github.com/Francois-EF-WebOps/xanat/blob/main/chat%20(4).html), conversation **“Face description JSON prompt”** | A reusable structured face-description schema and a sample Character A descriptor are present. | Template and sample located; Character A's identity and link to the recent man cutout are unconfirmed. |
| Young island boy and spirit cat | [xanat/chat (4).html](https://github.com/Francois-EF-WebOps/xanat/blob/main/chat%20(4).html), conversation **“AI video prompting styles”** | A short-video character brief specifies the boy's clothing/accessories and an orange-and-brown magical cat spirit, with Whisk subject/scene/style prompts. | Creative brief located; no standalone character sheet or approved image asset identified. |
| Vava, Yaya, Nana and family cast | [xanat/chat (4).html](https://github.com/Francois-EF-WebOps/xanat/blob/main/chat%20(4).html), conversation **“Story integration request”** | A story and illustration prompts define three girls and a family-of-five visual direction. | Story/illustration prompts located; not confirmed as the current presenter cast. |
| Frenchy artist persona | [xanat/chat (2).html](https://github.com/Francois-EF-WebOps/xanat/blob/main/chat%20(2).html), conversation **“Frenchy Persona Blueprint”** | Artist persona identity, archetype, themes, mission, sound and launch direction are recorded. | Artist persona, not yet confirmed as an explainer presenter. |
| Tropical adventurer couple image | [xanat image file](https://github.com/Francois-EF-WebOps/xanat/blob/main/file-1uT3NFSXJQXjzshCwzbNBg-DALL%C2%B7E%202025-01-15%2021.59.37%20-%20A%20vibrant%2C%20cartoon-style%20artwork%20of%20two%20cheerful%20adventurers%20having%20lunch%20on%20a%20tropical%20beach.%20The%20male%20adventurer%20has%20a%20dark%20African-style%20skin%20compl.webp) | The repository contains ten filenames for this image, all pointing to the same blob SHA; they are duplicate paths, not ten distinct artworks. The image shows a stylised man and woman adventurer pair. The archived conversation records the user supplying it as a reference and asking for four additional scenes. | Reference artwork located and visually inspected; relationship to the recently discussed cutouts or the explainer cast is unconfirmed. Not yet approved as canonical presenter art. |
| Artist persona schema | [ai-music-provenance/schema/persona.schema.json](https://github.com/Francois-EF-WebOps/ai-music-provenance/blob/bbc5c571debf22c5f1daf2a5ce4e1652915d6d36/schema/persona.schema.json), commit [bbc5c57](https://github.com/Francois-EF-WebOps/ai-music-provenance/commit/bbc5c571debf22c5f1daf2a5ce4e1652915d6d36) | Schema supports human_artist, virtual_character, collective, and project_alias; includes fictional bio and voice/likeness reference fields. | No actual presenter persona instances were found in the inspected AI Music Provenance tree. | Schema verified; presenter records unknown |
| MKC creative references | [ARTS_AND_CULTURAL_KNOWLEDGE.md](https://github.com/Francois-EF-WebOps/mascarene-knowledge-commons/blob/main/docs/ARTS_AND_CULTURAL_KNOWLEDGE.md) | Explicitly names My Voice Lab TTS, Babel Creole / “Down by the Shore”, music catalogue preservation, and AI-assisted media. | The document says source projects remain separate and require inventory; it does not identify presenter files. | References verified; assets unlocated |
| MKC production model | [KNOWLEDGE_TO_DISTRIBUTION_SYSTEM.md](https://github.com/Francois-EF-WebOps/mascarene-knowledge-commons/blob/main/docs/KNOWLEDGE_TO_DISTRIBUTION_SYSTEM.md) | Defines a multimedia/social distribution pipeline and minimum asset-record fields. | It is a workflow specification, not a character inventory. | Process verified; assets unlocated |
| Prompt reference library | [Ultimate-Nano-Banana-Pro-Collection.-Fr](https://github.com/Francois-EF-WebOps/Ultimate-Nano-Banana-Pro-Collection.-Fr) | Contains a large collection of externally attributed image-generation prompts, including character/portrait examples. | These examples are not confirmed as the user's established presenter cast or original artwork. | Reference only |
| Recurring presenter pair from the recent production thread | Prior conversation records: `character_left.png` (female) and `character_right.png` (male) | These are the established recurring presenter pair for fast explainers; the user requested one transparent full-body character per page. The female cutout was close but needed tan bag/strap restoration and cleanup; the male cutout needed complete lower legs/feet and background removal. | Neither exact filename was found in the 25 scanned repository trees or the `xanat` chat exports. Their current canonical source location and final approved versions remain unknown. Do not substitute Meiling or the tropical adventurer couple without an explicit match. | Presenter identities established; files not located in scanned GitHub repos |

## Candidate repositories and archives

- `xanat` — archived conversation exports and the located character/story prompts above. Its repository README describes orchid cultivation, so treat the conversation archive as a separate embedded record set, not as a character-production project.
- `ai-music-provenance` — persona schema and artist/music provenance; no explainer-presenter records found in the recursive tree.
- `10COgraphie`, `Blue-Sea-Print`, `Blue-Sea-Print-Core`, `Francois-Essaie`, `Elbaph-OS`, `Louis`, `Marani`, and `editor` — recursive path scan did not reveal dedicated character sheets, audio files, or standalone character images in the inspected default-branch trees.
- MKC — contains two research SVG diagrams, not character artwork; it references My Voice Lab TTS and “Down by the Shore” as separate workstreams.
- `Ultimate-Nano-Banana-Pro-Collection.-Fr` — third-party prompt reference library, not a source of the established cast.

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
- Do not assume every located character belongs in the explainer cast.
- Do not substitute generic prompt-library characters for the existing cast.
- Do not move, overwrite, or duplicate original media.
- Treat filename matches as leads, not proof of identity.
- Keep private family information and confidential source material out of this public register.

## Next action

Recover the standalone Meiling sheet and its reference assets from the original source, identify which of the located characters were intended for the fast explainer format, and map only those approved characters to the recent man/woman cutouts. Then build a small reusable 2D/3D preview. No new character design is needed until that source comparison is complete.
