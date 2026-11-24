# Music Asset Catalogue

Status: initial implementation; missing source evidence remains explicitly unknown.
Canonical home: music/ in Family-IP-Register.

## Canonical entities
- Song: the creative work/title-level concept (MUS-0001).
- Composition: a specific lyric/music version (CMP-0001).
- Recording: one exact audio file/render (REC-0001).
- Release: an album, EP, single, compilation, or planned package (REL-0001).
- Identity: artist, persona, collaborator, platform account, or character (IDN-0001).
- Source: file, archive, conversation, platform record, or external source (SRC-0001).

A song may have many compositions, recordings, and releases. Never collapse them into one record or overwrite an earlier version.

## Operating workflow
1. Inventory files without renaming, editing, transcoding, or deleting originals.
2. Match or create a song record; uncertain matches remain candidates.
3. Create one recording record per distinct audio file or generation.
4. Link composition versions only when text or other evidence exists; preserve fragments verbatim.
5. Attribute artist/persona only when supported. Uploader usernames are not automatic artist credits.
6. Keep planned releases separate from published releases.
7. Record provenance and rights status; unknown is valid.
8. Synchronize embedded tags only after review, writing a derivative copy.

## Storage
GitHub stores text catalogue records, lyrics, schemas, and documentation. Do not commit MP3/WAV binaries here. Keep audio at its original location and record its URI/path, observed properties, and checksum when available. Git LFS is not required.

## Formats and IDs
Catalogue files use UTF-8 JSONL: one JSON object per line. IDs are permanent and never recycled: MUS, CMP, REC, REL, IDN, SRC, EVD followed by four digits. Titles are labels, not identifiers.

See CATALOGUE_RULES.md and RECOVERY_QUEUE.md. This first seed reflects only known archive notes and one user-described MP3 metadata screen; it does not claim full recovery.

## Archive organization and duplicate control

The recovery workspace is organized chronologically and by canonical entity. Read `recovery/ARCHIVE_MAP.md` first, then `recovery/DUPLICATE_POLICY.md` and `recovery/duplicate-register.jsonl`. Production assets are tracked in `catalog/assets.jsonl`; external reference works and adaptations are kept in `catalog/external-works.jsonl`; failed generation attempts are events in `recovery/generation-events.jsonl`, never recordings.

Recovered Fin & Nik lyric texts are preserved in `archive/fin-nik/` and linked to evidence records. Their transcription from reports is not a substitute for checking the original messages.
