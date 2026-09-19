# Phase 1P — remedy: what the next session has to do (the set is still unopened)

1. ONE annotation agent, blind to every answer, label and packet. Input: `data/sentences.json` only (sid, slovak, level, topic).
   Format exemplar: `phase1n/data/annotations_part1.json` (closed set, read-only). Output `data/annotations_src.json`:
   `{"1P001": {"v": [>= 2 natural English renderings, v[0] = the reference], "lk": [the lock word of each rendering, parallel to v],
   "alt": {"word": ["accepted synonym", ...]}, "voice_sk": "active_agent|passive|impersonal", "agent_nom": true|false,
   "tf_gold": "past|present|future", "tense_open": bool, "perfective_present": bool}, ...}` for 1P001..1P120.
   The agent commits its file itself, immediately. `tf_gold` must equal the writer's (`sentences.json` -> `tags.tf_gold`); mismatches go to the owner, not to the runner.
2. `python3 normalise_1p.py` (exit 0 only with floors + annotations) -> `python3 floor_check_1p.py` (adds the lever-1 detector agreement).
3. Freeze (`FLOOR_CHECK_1P.md`, `FREEZE_FILES` already lists `normalise_1p.py`, `FREEZE_HASH`), commit, `RUN_COMMIT`.
4. `runner_1p.py --preflight` (225 + planned must stay <= 1,390) -> `--dry-run` -> `--final` ONCE -> `--ablation` with leftovers.
5. Headline on the judged labels with P1 / P2 / pooled exact intervals; the secondary figures are pre-declared here:
   coverage on the 480 writer-intended-correct items, and the accept rate in the cell "writer-intended wrong (M), judged correct" (n = 119).
Budget left: 1,400 - 225 = 1,175 counted calls.
