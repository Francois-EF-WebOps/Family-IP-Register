# Duplicate Detection and Resolution Policy

## Core rule

A duplicate is a relationship between source objects, not permission to delete one. Preserve every original file, message, archive snapshot and version. The catalogue may select one canonical representation while retaining all source references and alternate forms.

## Duplicate classes

| Class | Definition | Action |
|---|---|---|
| D0 — Exact binary duplicate | Same cryptographic hash and byte length | One logical content object; retain every source location/reference |
| D1 — Exact text duplicate | Same normalized text hash after line-ending/Unicode normalization; raw text may differ in formatting | One composition/evidence text candidate; preserve raw source copies and formatting |
| D2 — Repeated extraction | Same lyric/prompt transcribed from multiple reports or conversation summaries | One canonical evidence item with multiple source links; do not create a new composition |
| D3 — Near duplicate / revision | Similar wording but any substantive edits, section changes, omissions or order changes | Separate composition versions; link with `revision_of` |
| D4 — Translation / adaptation | Same underlying work transformed into another language or purpose | Separate derivative composition; link with `translation_of` or `adaptation_of` |
| D5 — Arrangement / performance variant | Same song with materially different tempo, instrumentation, lead/response, structure or arrangement | Separate composition/arrangement and recording as appropriate |
| D6 — Audio duplicate candidate | Same or similar audio across encodings, bitrates, trims, remasters or exports | Preserve every file; compare hashes, acoustic fingerprints, duration and listening evidence |
| D7 — Visual derivative | Same image re-encoded/resized/cropped or a revised character design | Preserve all assets; classify exact duplicate vs derivative vs canon revision |
| D8 — Same title, unrelated work | Title collision only | Keep separate songs until positive evidence links them |
| D9 — Same source repeated in catalogue | Duplicate Library record or repeated report reference | One logical source record with multiple source handles/occurrences |

## Matching sequence

1. Exact binary SHA-256.
2. Exact text hash after safe normalization (Unicode NFC, consistent line endings, trailing whitespace handling only). Do not normalize spelling, punctuation, language or lyric wording.
3. Metadata comparison: source ID, message timestamp, filename, duration, format, dimensions, platform generation ID.
4. Near-match candidate generation.
5. Human classification with explicit reason and confidence.
6. Record relationship and preserve all source references.

## Prohibited shortcuts

- Same title does not prove same song.
- Same filename does not prove same file.
- Different filename does not prove different recording.
- Same lyrics do not prove same recording or same author.
- Same audio waveform encoded differently does not mean the source files may be discarded.
- A translation is not a duplicate lyric.
- A new arrangement is not automatically a new song.
- A prompt retry is not a recording if generation failed.
- Repeated assistant/user summaries are not independent primary evidence.
- A newer report does not automatically replace an older report.

## Required duplicate record fields

`duplicate_group_id`, `left_source_id`, `right_source_id`, `duplicate_class`, `match_method`, `match_value` (hash or comparison evidence), `decision`, `confidence`, `reviewer_note`, `canonical_target_id`, `reviewed_at`.

Decisions: `exact_duplicate`, `same_evidence_repeated`, `revision_not_duplicate`, `derivative_not_duplicate`, `distinct_work`, `candidate_needs_review`.

## Preservation and public repository handling

Do not upload private audio, personal exports, credentials, private email addresses or expiring signed image URLs to a public repository. Store non-sensitive metadata and provenance references; retain originals in their source location. Never delete or overwrite originals as part of deduplication.
