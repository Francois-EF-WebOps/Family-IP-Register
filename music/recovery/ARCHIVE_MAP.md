# Music Archive Map

Status: first reconciliation pass; not a claim of complete recovery.
Canonical destination: this module. Original sources remain preserved at their original locations.
Recovery principle: collect first, classify second, deduplicate relationships third. Never discard source evidence.

## Recovery layers

1. **Source snapshots** — original conversation exports, archive versions, notebook exports, PDFs, audio files, platform exports, artwork collections. Keep source identity, date, location and checksum.
2. **Extracted evidence** — verbatim lyric blocks, prompts, comments, generation events, metadata and asset descriptions. Each extraction points to one or more source snapshots and preserves exact wording.
3. **Canonical entities** — songs, composition versions, recordings, releases, identities and production assets. Titles are labels, not keys.
4. **Relationships** — version-of, translation-of, adaptation-of, derived-from, duplicate-of, same-work-candidate, used-in-release, depicts-character, generated-from.
5. **Recovery state** — confirmed, partial, title-only, concept-only, inaccessible, not-yet-searched, disputed. "Not recovered" never means "never existed".

## Chronological source baseline

| Date | Source/work | Current evidence | Classification |
|---|---|---|---|
| 2026-08-20 | Down By The Shore — Version 1 | Six-line fragment; island lullaby, ~60 BPM, steel pan, Mama→Papa movement, animal/scene sequence | One composition candidate; partial |
| 2026-08-20 | Down By The Shore — Babel Creole Midday | Hook/chorus fragments, "Did you ever see…" pattern, scene sequence, ~108 BPM, steel pan + hand drums | Separate arrangement/lyric version under same song candidate; partial |
| 2026-09-07 | Late Registration localization | 23 referenced track/skit entries; two Haitian Creole karaoke adaptation drafts identified | External source collection; adaptations kept separate from original works |
| 2026-09-23 | Nation the Moor | Title and morning-beat request | Title-only |
| 2026-09-27 | Ten-persona discography architecture | Ten personas; album-based plan; 18 unique songs per album/persona discussed | Architecture, not ten verified artists or a completed catalogue |
| 2026-09-30 | Best Behavior / Worst Behavior | Transformation concept and revision comments | Draft history; full lyrics not recovered |
| 2026-10-01–06 | Family Saturday Chores | Song, actions and video scenes referenced | Project reference; exact text not recovered |
| 2026-10-05 | Lullaby / toddler-motion adaptation | Request and motion follow-up referenced; familiar-song phrase appears in title | Adaptation/reference unresolved; exact output not recovered |
| 2026-10-08 | The Sun / Sun Through the Hood | Two user-supplied phrases and detailed production/narrative direction | Fragment + direction; full lyric not recovered |
| Date unknown | Switching Skills Rap | Project title reference | Title-only |
| 2026-11-06 onward | Fin & Nik — Album 01 / ZERO (P01) | ZERO lyrics and storyboard; Tide Pool & Sand lyrics; A Friend Called Nik continuity milestone | Two lyric compositions; one title/continuity reference |
| 2026-11-24 | Tsunami | Music-generation and storyboard prompt reference | Unassigned concept/prompt; not a confirmed completed song |
| 2026-11-22 file timestamp | Heartbeats in the Streets | One user-described MP3 metadata record | One recording; artist/project attribution unresolved |

Dates above are source/conversation dates, not automatically creation, recording or release dates.

## Existing archive sources and duplicate handling

- `Master_Lyrics_Archive_Recovery_2026-10-02.md` is Version 1 of the recovery archive.
- `Master_Lyrics_Archive_Recovery_2026-10-09.md` is Version 2. It explicitly references Version 1 and adds later projects. They are sequential snapshots, not duplicate files.
- The Library exposes two entries for the 2026-10-09 archive with the same filename, size and content. Treat them as duplicate storage entries for one logical source; retain both source handles in provenance until Library-level cleanup is separately authorized.
- The two uploaded 8-page PDFs are different files and have materially different contents. They overlap heavily in Fin & Nik material but are sibling recovery reports, not exact duplicates and not a clean V1→V2 sequence.
- Repeated lyric blocks across reports are repeated evidence of the same composition unless wording, section order or provenance establishes a distinct version.
- The report's 21 Dropbox character references are a collection count, not 21 verified unique canonical assets. Inventory each file before deciding duplicates.

## Current canonical work groups

### Earlier music work
- Down By The Shore: Version 1 and Babel Creole Midday remain separate composition versions under one song candidate.
- Nation the Moor.
- Best Behavior / Worst Behavior.
- Family Saturday Chores.
- Lullaby / toddler-motion adaptation.
- The Sun / Sun Through the Hood.
- Switching Skills Rap.
- Ten-persona discography architecture (identity list still incomplete).

### Fin & Nik
- Release concept: Album 01 / ZERO (P01), planned 18 tracks.
- P01-T01: ZERO — full lyric and six-panel storyboard recovered; no recording verified by the reports.
- P01-T02: Tide Pool & Sand — full lyric recovered in the uploaded reports; assistant-drafted from canon, not user-authored original.
- P01-T09: A Friend Called Nik — continuity milestone/title only; no lyric or recording recovered.
- Tsunami — unassigned prompt/storyboard concept; do not assign a track number.
- Fin and Nik are fictional character identities, not automatically artist credits.

### External adaptation work
- Late Registration is a third-party album reference. Keep its track metadata and the user's translation/localization workflow in an external-work collection.
- Haitian Creole adaptations are derivative drafts, not original songs by the user. Do not reproduce third-party source lyrics in the public repository.

## Duplicate review queue

1. Compare exact file hashes for every audio, image, document and prompt export.
2. Compare normalized text hashes for lyric blocks while retaining original raw text.
3. Use near-duplicate matching only to propose candidates; human review decides whether items are duplicates, revisions, translations, arrangements or independent works.
4. For audio, combine file hash, duration, codec/format, acoustic fingerprint and listening review. Different encodings or masters may be the same performance but remain separate files/recordings.
5. For images, combine file hash, dimensions, perceptual hash and visual review. Character sheets with changed canon are revisions, not duplicates.
6. Never deduplicate by title, filename, artist tag, upload account or similar-looking artwork alone.

## Next recovery order

1. Search earliest available music conversations and recover complete original message sequences, starting before 2026-08-20 if accessible.
2. Reconcile the 2026-10-02 and 2026-10-09 archives against their originating conversations; preserve both as immutable source snapshots.
3. Recover the full 2026-10-08 Sun conversation, all earlier song drafts, and all ten persona names/identities.
4. Recover the complete Fin & Nik conversation sequence and original notebook attachment `retardé`.
5. Inventory all Android audio and Suno exports; then inspect Dropbox's 21 character-reference files.
6. Reconcile source records and canonical IDs; only then consider metadata/tag repair.
