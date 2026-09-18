# Phase 1h — fresh data input schema (FROZEN with the checker)

Every file is JSON Lines, UTF-8, one object per line. The loader is `checker_1h.load_fresh()` and is frozen;
adding a field is harmless, renaming one breaks the run.

| file | line |
|---|---|
| `phase1h/fresh/new_sentences_60.jsonl` | `{sid, sk, level, topic, source}` — written by `select_new_sentences.py` (seed 20260919) |
| `phase1h/fresh/writer_input_140.jsonl` | `{sid, sk, level, topic}` — 80 old + 60 new, the blind writers' ONLY input (no English, no annotation) |
| `phase1h/fresh/annotations_new_60/<sid>.json` | one annotation per new sentence, **same format as `phase1c/annotated_after/<id>.json`** |
| `phase1h/fresh/correct_part1.jsonl` … | `{sid, n (1–3), en}` plus the optional `chk` block below |
| `phase1h/fresh/wrong_part1.jsonl` … | `{sid, n (1–4), type ("T"|"W"|"M"|"S"), en}` plus the optional `chk` block |
| `phase1h/fresh/judgements.jsonl` | `{set ("C"|"W"), sid, n, real ("correct"|"wrong"), note}` |

Item ids follow the existing scheme: `C:<sid>:<int(md5(en)[:8],16)>` and `W:<sid>:<…>` (`checker_1h._iid`).

## The `chk` block — REQUIRED for a fair measurement

Phase 1c items carry the app checker's own verdict, which is what routes an item to L1 (offline accept),
L2 (grammar veto) or L3 (model). A fresh answer has no such verdict until the existing offline checker is
run over it. Therefore each `correct_part*` / `wrong_part*` line SHOULD carry

    "chk": {"verdict": "correct"|"correct_with_tip"|"wrong", "step": "auto"|"mistake", "feedback": "<text>"}

produced by the checker already in this repo (`translation-offline/checker/`), exactly as Phase 1c produced
`measure_after.json`. When `chk` is missing the loader sets `verdict="wrong"`, `step="auto"` and marks the
item `chk_missing: true`; such items can never be accepted at L1, so coverage would be biased downwards and
the OLD/NEW comparison would be invalid. The measuring agent must either supply `chk` or report the fresh
numbers as "L2/L3 only".

## Annotation template

Template file: `phase1c/annotated_after/10013.json` (fields `id, t, lv, v, lk, s, d, g, p, m, alt, o`).
Spec: `translation-offline/GENERATION_SPEC.md` + `phase1c/BRIEF.md` §4 and the task files
`phase1c/tasks/batchS.md` / `batchL.md` (they are the prompts that produced the 80 annotations).
Reference hygiene (§2.3) is applied to the new annotations automatically at load time — the annotator must
NOT pre-apply it.
