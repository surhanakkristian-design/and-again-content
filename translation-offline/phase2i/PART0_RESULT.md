# Phase 2I Part 0 result — 0 model calls
- SK: 4,064 rows xlsx + jsonl; empty v fixed 0; v[0]!=en 0; exercise_id already int.
- CZ: 4,064 rows xlsx + jsonl; empty v fixed 50 (n 5365–5414); v[0]!=en 0; exercise_id text -> int (4,064).
- Round-trip asserted; originals' SHA-256 unchanged; lk kept, documented unused (upload/UPLOAD_README.md).
- The SK annotations are unchanged by the v fix; `upload/annotations_sk_fixed.jsonl` is byte-content-equal in data to phase2d/out/annotations_sk_final.jsonl and is the input for the set stage.
- No defects.
