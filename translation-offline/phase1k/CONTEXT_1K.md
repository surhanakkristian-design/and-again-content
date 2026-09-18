# Phase 1k — CONTEXT (read this first)

Written by agent **P** (18 Sept 2026). Paths relative to
`~/Projects/and-again-content/translation-offline/`. `$J = phase1j` (read-only, `chmod -R a-w`),
`$K = phase1k`.

## §0 The new acceptance rule (owner's text, verbatim)

```
OLD: the answer had to use the practised structure; the L2 lock rejected any paraphrase of it.
NEW: **the reference point is the SLOVAK sentence, not the English reference.** If the learner's
sentence is correct English on its own AND means what the Slovak means, it is ACCEPTED with points,
even if it avoids the practised structure entirely. Learners often do not know which structure is
being practised and must not be penalised for that. The practised structure becomes a TIP, not a gate.

Three boundaries the owner set explicitly:
B1 VOICE. If the Slovak names an agent in the nominative and the answer moves that agent out of subject
   position or drops it (active -> passive), that is a MISTRANSLATION: WRONG, no points. Where the
   Slovak is itself impersonal or passive, an English passive is correct.
B2 TENSE IS ANCHORED TO THE SLOVAK, and this is NOT relaxed. Where the Slovak fixes the time, the
   answer must match it: "Po dopade JE trochu šťavy" answered "there WAS a bit of juice" is WRONG.
   This is judged against the Slovak, never against the English reference — an answer whose tense
   differs from the reference but fits the Slovak is CORRECT.
B3 Where the Slovak leaves the choice genuinely open, any grammatically possible English tense in the
   right time frame is ACCEPTED WITH A TIP naming the practised structure. Slovak past imperfective
   ("On trénoval hodiny") admits "was training", "trained" and "had been training" alike.

So B2 and B3 are one rule in two cases: the TIME FRAME (past / present / future) must always match the
Slovak; the choice of English tense WITHIN that frame is free when the Slovak does not fix it.
```

## 1 Data

| path | what |
|---|---|
| `$K/loader_1k.py` | the ONLY sanctioned reader; logs to `$K/access_log.jsonl` |
| `$K/fresh/sentences_fresh.jsonl` | **70 NEW Slovak sentences** (arm-B form) + references + annotation + gold metadata |
| `$K/fresh/annotations_fresh.json` | `{"<sid>": {"hygienised": …, "raw": …}}`, same shape as `$J/*/annotations.json` |
| `$K/fresh/writer_input.jsonl` | `{wid, slovak, level, topic}` only — the answer writer sees nothing else |
| `$K/fresh/writer_output.jsonl` | written by the answer writer: `{"wid":…, "answers":[{"text":…, "intent":"C\|T\|W\|M\|S\|V\|TF"}, …]}` |
| `$K/fresh/items_fresh.jsonl` | built by the judge-input script: `{id, sid, text, intent}` |
| `$K/judge/build_judge_input.py` | blind-judge input builder (`in_1..in_4` + `in_5`, `key.jsonl`) |
| `$J/dev/items.jsonl`, `$J/holdout/items.jsonl` | 490 + 490 Phase 1j items (schema `$J/CONTEXT_1J.md` §2) |
| `$J/taskB/rewrites.jsonl` | arm-B Slovak (`new_sk`) + arm-B references (`refs_new`) for all 140 sids |
| `$J/taskB/annotations_b_{dev,holdout}.json` | arm-B annotations (`g` removed on rewritten sids) |

**Phase 1j is closed** (`$J/FINAL_RUN_DONE`). In Phase 1k its HOLDOUT is just a *labelled replay*
set (its numbers are already published); the untouched surface of Phase 1k is the 70 FRESH
sentences and their answers.

## 2 Schemas

**Phase 1j item** (unchanged, `$J/CONTEXT_1J.md` §2): `item_id "C:<sid>:<crc32>" | "W:…"`, `side`,
`kind "C"|"W"`, `sid`, `n`, `level`, `topic`, `sk`, `band`, `reference`, `refs`, `answer`,
`judged "correct"|"wrong"` (gold), `wrong_type "T"|"W"|"M"|"S"|null`, `half`, `locks`, `chk`, `rows`,
`side_1i`. `load_dev_items()` overwrites `sk` / `reference` / `refs` with the arm-B values and adds
`arm_b_rewritten`.

**Annotation** (`hygienised` and `raw`): `id` (= sid), `t` (topic id), `lv` (level), `v` (accepted
references), `lk` (grammar locks, parallel to `v`), `alt` (per-word alternatives), optional `s`
(synonym groups), `d` (optional tokens), `p`, `m` (mistake patterns), `g` (gender chain — **absent /
null everywhere in arm B and in all 70 fresh sentences**, because the pronoun is stated).

**Fresh sentence record** = the `sentences_all.jsonl` keys (`sid, side, level, band, topic, half, sk,
reference, refs, annotation_v, annotation_alt, annotation_d, annotation_p, g, g_raw, locks, n_items`)
plus `annotation` (`{hygienised, raw}`) plus **gold metadata the checker must NEVER read**:

| field | values |
|---|---|
| `tf_gold` | `present \| past \| future \| conditional \| mixed` — the time frame the Slovak fixes |
| `voice_sk` | `active_agent \| impersonal \| passive` |
| `agent_nom` | `true` = the Slovak names a nominative agent **and** the verb is transitive, so an English passive recast is possible — and per B1 **wrong** |
| `perfective_present` | `true` = perfective present form with future meaning ("dokončí") |
| `tense_open` | `true` = the Slovak leaves the English tense choice open inside the frame (B3), e.g. past imperfective |

`side` of a fresh record is `"fresh"`, `half` is `"NEW"`, `n_items` is `null` until answers exist.
`band` = Slovak word-count bucket (`1-6 / 7-9 / 10-12 / 13-16 / 17+`), same convention as 1j.
Fresh `t` (topic id) is synthetic (`9000+`) — it is **not** a live topic id and carries no `m`
patterns, so no mistake-pattern lookup can fire on a fresh sentence.

**Item id** everywhere: `C:<sid>:<crc32(text)>` for an intended-correct answer, `W:<sid>:<crc32>`
otherwise (`zlib.crc32(text.encode('utf-8')) & 0xffffffff`), identical to the 1h–1j convention.

**Intents** on fresh answers: `C` correct · `T` tense/aspect wrong · `W` wrong word · `M` meaning
added/dropped · `S` small slip · **`V` active→passive recast** (B1 probe) · **`TF` time-frame shift**
(B2 probe). `T`/`W`/`M`/`S` keep their Phase 1c–1j definitions (`$J/CONTEXT_1J.md` §6). An intent is
the writer's *design intent*, never a label: the blind judge's verdict is the only truth.

## 3 Conventions of this phase

- **Arm B is frozen**: explicit subject pronoun wherever Slovak would drop it; no `g` chain when the
  pronoun is stated. Every fresh sentence follows it (noun-subject sentences stay as they are).
- Every read of Phase 1j data, of fresh sentences, answers, items, judge key or judge labels goes
  through `loader_1k` and appends `{ts, side, what, caller, n, purpose}` to `$K/access_log.jsonl`.
- Reads of fresh **answers / items / judge key / judge labels** raise `PermissionError` unless
  `PHASE1K_OPEN_FRESH=1`. Only the judge-input build and the ONE final run set it. Fresh
  **sentences** and **writer_input** are answer-free and always readable.
- `$J` is `chmod -R a-w`. Never write there, never copy anything there. Run python with
  `PYTHONDONTWRITEBYTECODE=1` (`loader_1k` also sets `sys.dont_write_bytecode`).
- No model call without a ledger row; blind-judge protocol as in `$J/CONTEXT_1J.md` §6 (the judge
  sees Slovak + answer only — in 1k **not even the reference**, because §0 makes the Slovak the sole
  ground truth).
- Never read, print or log `~/Projects/and-again/.env.local`.

### Rule of use

```python
import os, sys
K = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1k')
sys.path.insert(0, K)
from loader_1k import load_dev_items, load_dev_annotations, load_fresh_sentences
dev  = load_dev_items(purpose='1k DEV run')            # 490, arm-B Slovak
ann  = load_dev_annotations(purpose='1k DEV run')      # arm-B annotations
frs  = load_fresh_sentences(purpose='1k fresh design') # 70, answer-free
```
