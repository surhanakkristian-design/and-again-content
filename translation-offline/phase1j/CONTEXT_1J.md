# Phase 1j — CONTEXT for every following agent (read this first; it replaces exploration)

Written by agent S (18 Sept 2026). Everything below was verified by running it, zero model calls.
Paths are relative to `~/Projects/and-again-content/translation-offline/`.
Agents: **A** p-chain · **B** Slovak rewrite + re-labelling · **J** blind judge · **R** DEV runs · **F** final run + report.

## 0 Rules of the phase

- **DEV only** until the single final run. The HOLDOUT is read exactly twice in the phase's life:
  by **B** for the sentence rewrite / re-labelling (`PHASE1J_LABEL_PREP=1`, produces no checker output,
  no verdicts, no measurement) and by **F** for the one measurement (`PHASE1J_FINAL=1`).
- Every read of either side goes through `phase1j/loader_1j.py`; it appends
  `{ts, side, what, caller, n, purpose}` to `phase1j/access_log.jsonl`. Never open `phase1j/holdout/*`
  any other way. `phase1j/holdout/` and the whole of `phase1i/` are `chmod a-w` (readable, not writable).
- **Hard cap: 1,400 counted model calls for the entire phase**, through ONE shared ledger
  `phase1j/ledger.jsonl` (same row format as §5). *Counted* = an HTTP-200 row. Before calling, check the
  ledger; before a batch, check `sum(1 for row if row['http']==200) + len(todo) <= 1400`.
  Price `gemini-3.1-flash-lite`: **$0.25 / 1M input, $1.50 / 1M output** (~$0.00003 per L3 call).
- Run python with `PYTHONDONTWRITEBYTECODE=1` (phase1i is read-only; imports must not write `__pycache__`).
- Never read, print or log `~/Projects/and-again/.env.local`.

## 1 What exists in `phase1j/`

| path | what |
|---|---|
| `make_split_1j.py` | built the split; re-runnable, 0 calls (would need phase1j/holdout unlocked) |
| `split/SPLIT.md`, `split/split_counts.json`, `split/dev_sids.json`, `split/holdout_sids.json` | the rule + all counts |
| `dev/items.jsonl`, `holdout/items.jsonl` | 490 + 490 items, schema §2 |
| `dev/annotations.json`, `holdout/annotations.json` | `{"<sid>": {"hygienised": {...}, "raw": {...}}}`, 70 sids each |
| `dev/sentences.jsonl` (70), `sentences_all.jsonl` (140, has `side`) | **answer-free, verdict-free** sentence exports for agent B |
| `loader_1j.py` | `load_items(side, purpose)`, `load_annotations(side, purpose)`, `load_sentences(side, purpose)` |
| `access_log.jsonl` | the evidence |
| `baseline_dev_1j.py`, `split/baseline_dev.json` | the apparatus check of §7 |

**Split rule (BY SENTENCE):** `order = sorted(sids, key=lambda s: sha256(("phase1j|%s" % s).encode()).hexdigest())`,
`DEV = order[:70]`, `HOLDOUT = order[70:]`. **No sid is on both sides** — the Phase 1i leakage caveat is
closed: a per-sentence change (annotation edit, reference rewrite, rewritten Slovak, a list keyed to a sid)
is now measurable on the holdout. Leakage that remains: 238 DEV and **229 HOLDOUT items were on the
Phase 1i DEV side**, i.e. the frozen 1i config was chosen while their answers were visible. So the 1j
holdout is clean for anything designed in Phase 1j and an optimistic bound for the inherited 1i config.

Counts (both sides identical by luck of the hash): 490 items, 70 sentences, 215 judged correct,
275 judged wrong; coverage denominator 210, FA denominator 275.
Really-wrong per type — DEV T 69 / W 70 / M 66 / S 70, HOLDOUT T 68 / W 68 / M 69 / S 70.
OLD/NEW items: DEV 266/224, HOLDOUT 294/196.
**No cell is genuinely too small**: the exact CP 95 % half-width of a 5 % rate is 5.6–6.2 pp on every cell,
which resolves 5 % vs ~15 % but not 5 % vs 8 %. Per-type cells are diagnostic only; decisions ride on the
275-item side denominator (half-width ±2.9 pp at 5 %).

### Rule of use

```python
import os, sys
P1J = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1j')
sys.path.insert(0, P1J)
from loader_1j import load_items, load_annotations
recs = load_items('dev', purpose='row 4 DEV run')       # 490 dicts
ann  = load_annotations('dev', purpose='row 4 DEV run') # '<sid>' -> {'hygienised':…, 'raw':…}
```

## 2 Schemas

`items.jsonl`, one line per judged answer — keys exactly:

```
item_id "C:20298:610089844" | "W:…"   side "dev"|"holdout" (PHASE 1J side)   side_1i "dev"|"holdout"
kind "C"|"W"   sid int   n slot   level "A1".."B2"   topic grammar topic string (goes into the prompt)
sk Slovak sentence   band "1-6"|"7-9"|"10-12"|"13-16"|"17+"   reference English reference used by prompt
refs list = checker refs_of() (reference + annotation v[] + hygiene gender variants)
answer learner answer   judged "correct"|"wrong"  <- the BLIND gold judgement, THE ONLY TRUTH
wrong_type "T"|"W"|"M"|"S" for kind W, null for C     half "OLD"|"NEW"
chk {"verdict","step","feedback"} = the app's own offline checker (routes to L1/L2/L3)   chk_missing false
locks / lock_ok / lock_released_2_1     rows {"row7":…, "row8":…}  (frozen Phase 1h P-B / P-C per-item
  results: layer, accepted, verdict, tip, why, model, reply, call_made, failed_call)
```

Annotation (`hygienised` and `raw`, same shape): `id, t, lv, v` (accepted references), `lk` (grammar locks),
`alt` (per-word alternatives), `m` (mistake patterns), optional `d` (OPTIONAL tokens), `p`
(`"+word"` / `"-span"`), `s` (synonym-group ids), `o`, and optional **`g` — the gender chain**.

**`g` lives in the annotation** (`ann['<sid>']['hygienised']['g']`), a list of lists of reference words:
2 DEV examples — sid `1452` → `[["he", "he#2", "his"]]`, sid `3937` → `[["She", "she"]]`.
18 of the 70 DEV sids have a `g`. `g` reaches F3/F5/F2B through `refs_of()` and, since Phase 1i, the
**prompt** through the gender licence line (§3). `sentences.jsonl` exposes it as `g` (+ `g_raw`).

`sentences.jsonl` / `sentences_all.jsonl` keys: `sid, side, level, band, topic, half, sk, reference, refs,
annotation_v, annotation_alt, annotation_d, annotation_p, g, g_raw, locks, n_items`. No answers, no verdicts.

## 3 The frozen Phase 1i configuration (inherited baseline)

`phase1i/FROZEN_CONFIG.json`: variant **P-E4b**, `tip_scoring = "tip_reject"` (an L3 `TIP` is a REJECTION),
Task B fixes on (`backfill_s_ids`, `lock_fix` syn+gender+contraction), Task C guards `["F4v3"]`,
model `gemini-3.1-flash-lite`, `generationConfig = {"temperature":0,"maxOutputTokens":24,
"thinkingConfig":{"thinkingBudget":0}}` (thinking OFF).

**System instruction** (`lib_prev.SYS`, unchanged for P-E4b), verbatim:

> You judge English translations. Reply with exactly one word: SAME, TIP or DIFF. SAME = the learner
> sentence means the same as the reference and is correct English. TIP = same meaning and acceptable, but
> with a small slip. DIFF = different meaning, or not correct English. No explanation.

**User prompt P-E4b** = the frozen P-B lines, then the extra lines **inserted before the last (question)
line**, in this order: gender line (only when the annotation has `g`), ground-truth line, wording line.
Verbatim, as built by `pipeline_1i.build_prompt` (`phase1i/pipeline_1i.py:214`):

```
Slovak: <sk>
Reference English: <reference>
Learner: <answer>
Practised grammar: <topic> — ALREADY VERIFIED as correct in this answer; judge meaning and vocabulary only.
Gender: the Slovak does not fix the gender here — the reference's "he" may equally be the other gender (he/she, him/her, his/her, himself/herself). An answer that keeps the meaning but picks the other gender is SAME on that point.
The SLOVAK sentence is the ground truth and the English reference is only one valid rendering of it; judge the learner against the Slovak, not against the reference wording.
A synonym, a different word order or a different phrasing that keeps the Slovak meaning is SAME; a word that changes which thing, person, place, time or quantity the Slovak names is DIFF.
SAME, TIP or DIFF?
```

The gender licence line is `GENDER_TMPL` (`pipeline_1i.py:40-42`); `{words}` is the flattened `g` chain
rendered as `", ".join('"%s"' % w)` (e.g. `"he", "he#2", "his"`). Ground line `GROUND_LINE` :46-47,
wording line `WORDING_LINE` :49-51. The prompt contains **no annotation, no synonym group, no alternates**
(the `Also accepted English:` line belongs to P-E4a, not to the frozen variant).

### `phase1i/pipeline_1i.py` — functions you will reuse (line numbers)

| function | line | role |
|---|---|---|
| `setup(side)` | 60 | imports `checker_1i`, seeds `C._ANN` / `C.SK_OF` from the loader (1i loader — see §7 for the 1j way) |
| `configure(b_fix, guards, side)` | 80 | applies Task B (`backfill_s_ids.apply_to_checker`, `lock_fix.apply`) and Task C (`guards_c.apply`); returns the state dict `st` |
| `to_item(r)` | 100 | item dict → the shape the checker layers expect |
| `run_pipeline(st, verdict_map, tip_reject)` | 130 | decides every item, 0 calls; row has `accepted, layer, model, tip, model_tip, reached_l3` |
| `pb_lines` / `sys_text` | 154 / 168 | the frozen P-B lines; the system instruction per variant |
| `gender_chain(st, sid)` | 182 | flattens `g` into the word list of the gender line |
| `alt_refs` | 200 | P-E4a only |
| `build_prompt(st, r, variant)` | 214 | → `(user_text, has_gender, equals_pb)` |
| `parse_reply(txt, variant)` | 245 | `\b(SAME|TIP|DIFF)\b` on the upper-cased text; `None` = parse failure |
| `load_key()` | 256 | reads `GEMINI_API_KEY` from `~/Projects/and-again/.env.local` **at call time**; sent only in the `x-goog-api-key` header; NEVER print it, never put it on a command line, `_redact()` :267 scrubs errors |
| `_http(url, body, key)` | 274 | returns `(status, json, raw)`; any exception → status `0` |
| `ledger_append(path, row)` | 294 | thread-safe one-line append |
| `call_variant(st, r, variant, ledger, key, tries=5)` | 300 | the whole call with the transport rules of §5 |
| `ledger_verdicts(path)` | 343 | `({(variant,item_id): verdict}, fails, retries)` from **HTTP-200 rows only**, last row wins |
| `cp(k, n)` / `rate` / `metrics(st, res)` | 387 / 415 / 419 | exact Clopper-Pearson, and coverage / FA / FA by type / layer / half / FR lists |

`phase1i/run_config.py` is the driver: it reads `FROZEN_CONFIG.json`, calls `configure()`, computes the L3
set from `run_pipeline(st, {})`, reuses stored verdicts **only when variant + prompt text are identical**
(`prompt_key()` = `build_prompt(...)[0]`), refuses when `len(todo) > cap`, then scores with
`run_pipeline(..., tip_reject=…)` + `metrics()` and writes `taskF/<side>_{verdicts.jsonl,summary.json}`.
Copy that structure for Phase 1j, but point the ledger at `phase1j/ledger.jsonl` and the loader at
`loader_1j`.

## 4 F4 (the Slovak-morphology subject guard)

- `phase1i/checker_1i.py:468 sk_subject(sk)`, `:512 f4_subject_mismatch(it)` (old EN-side version, runs
  only when F4v2 is off), `:536 sk_features(sk)`, `:608 f4v2_subject_mismatch(it)`.
- `phase1i/taskC/guards_c.py:291 sk_number_extra(sk)`, `:323 sk_features_v3(sk)`, `:339
  f4v3_subject_mismatch(it)`, registry `GUARDS`/`ORDER` :370-371, installer `apply()` :388.

What it already derives from Slovak morphology: `sk_features` walks the Slovak tokens and collects
(person, number, gender) signals from subject pronouns, past-tense `-l` participle endings, `byť`-future
forms and verb agreement endings, keeping a feature **only when all signals agree** — otherwise the feature
stays `None` ("underdetermined"). The English reference is never consulted. F4v2 then reads the answer's
subject pronouns (`en_subjects` / `EN_SUBJ`) and fires only when **every** answer pronoun clashes with a
feature the Slovak determines (person, number — `you` exempt — or gender m/f). F4v3 is a strict superset:
when F4v2 found *no* signal at all it adds a number signal from plural/singular verb endings
(`SK_PRESENT_NUM`, clause splitting via `SK_CLAUSE`) and decides with the same clash + abstention logic.

## 5 Stored P-E4b replies — reuse them, do not re-call

| ledger | rows with `http==200` and a parsed verdict | which items |
|---|---|---|
| `phase1i/taskE/calls.jsonl` | 270 P-E4b (plus P-E1 71, P-E2 270, P-E3 270) | the Phase 1i **DEV** items that reached L3 |
| `phase1i/taskF/holdout_calls.jsonl` | 306 P-E4b | the Phase 1i **HOLDOUT** items that reached L3 |
| `phase1i/taskB/calls.jsonl` (4 P-B), `phase1i/taskD/calls.jsonl` (30 transport probes) | — | not useful for scoring |

Keyed by `(variant, item_id)`; `item_id` is stable across phases. Together they cover **every** L3 item of
the Phase 1j DEV side with 0 misses (§7). Lookup:

```python
import sys, os
P1I = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1i')
sys.path.insert(0, P1I)
import pipeline_1i as P
have = {}
for p in ('taskE/calls.jsonl', 'taskF/holdout_calls.jsonl'):
    h, fails, _ = P.ledger_verdicts(os.path.join(P1I, p))
    have.update({i: v for (var, i), v in h.items() if var == 'P-E4b'})
have['W:20298:1595880954']          # -> 'SAME' | 'TIP' | 'DIFF'
```

Reuse is legitimate **only while the prompt text is byte-identical**: same variant, same `sk`, `reference`,
`answer`, `topic` and same gender chain. Agent B's rewrite of a Slovak sentence invalidates every stored
verdict for that sid — those items must be re-called and counted against the 1,400 cap.

Ledger row format (also the format for `phase1j/ledger.jsonl`): `ts, model, variant, item_id, http,
counted, verdict ("SAME"|"TIP"|"DIFF"|"PARSE_FAIL"), reply, finish, empty, latency_ms, try,
prompt_tokens, candidates_tokens, thoughts_tokens, cached_tokens, thinking, max_output` — and on a
transport failure `counted:false, error (redacted), transport_retry:true`.

### Transport rules as implemented (`call_variant` :300)

- **counted = HTTP 200 only.** A 200 row is written with `counted:true` and is never re-called.
- **http 0 / 429 / 5xx** (anything not 200) → row with `counted:false`, exponential backoff
  `1 s → ×2 → cap 16 s` with ±30 % jitter, up to `tries=5`; after the last attempt it returns `None`
  and the item simply has no verdict. Retries never consume budget.
- **Empty or unparsable 200** → `verdict:"PARSE_FAIL"`, `counted:true`, **never retried, never guessed**.
  `ledger_verdicts` returns it in `fails`; an item with no verdict is scored `failed` and **not accepted**.

## 6 T/W/M/S and the blind-judge protocol

Type letters are written by the wrong-answer writer into `phase1h/fresh/wrong_part*.jsonl`
(`{sid, n (1–4), type ("T"|"W"|"M"|"S"), en}`, `phase1h/FRESH_SCHEMA.md:12`) and carried on every item as
`wrong_type`. Definitions as used since Phase 1c and restated in `phase1i/CONTEXT.md` §2:

- **T** — tense / aspect: the right words, the wrong time reference.
- **W** — wrong word: a lexical substitution that changes which thing, person, place, time or quantity.
- **M** — meaning added or dropped: information in the answer that is not in the Slovak, or Slovak
  information missing from the answer (a single adverb, particle, place or time word counts).
- **S** — small slip family: article, preposition, agreement, word form / spelling slips that are still
  wrong English or change the meaning slightly.

**Blind-judge protocol** (`phase1h/REPORT_PHASE1H.md` §7, commit `65e1c1a`): the judge sees the Slovak, the
reference and the answer **only**, never any checker verdict, and records
`{set ("C"|"W"), sid, n, real ("correct"|"wrong"), note}` into `phase1h/fresh/judgements.jsonl`; doubts are
marked and resolved explicitly (21 doubts in 1h, all resolved as real). The pass must be recorded **before
any checker verdict for those items exists**. Result carried into `items.jsonl` as `judged`: of the 420
correct 0 were judged really wrong; of the 560 wrong 10 were judged really correct (T 3, W 2, M 5, S 0).
No standalone verbatim judge-instruction file exists on disk — this paragraph plus the type list above is
the protocol; agent J must reproduce it (blind, per item, doubts noted) and write the same record shape.

## 7 Apparatus check — the frozen 1i config replayed on the NEW DEV side (0 model calls)

`baseline_dev_1j.py` → `split/baseline_dev.json`. It seeds `checker_1i` from the 1j DEV files, injects the
state into `pipeline_1i` (`P._ST = {...; 'side': 'dev1j'}`) so `configure()` never touches the 1i loader,
applies the frozen config and replays the stored P-E4b verdicts:

```
items 490   reached L3 294   cache misses 0   failed-call items 0   model calls 0
coverage 191/210 = 90.95 %  CI [86.23, 94.46]
FA        15/275 =  5.45 %  CI [3.08, 8.84]
FA by type  T 0/69   W 2/70   M 5/66   S 8/70        FA by layer: L3 15
FR by layer L2 7, L3 6, F4v2 3, L3:TIPrej 2, F5 1
```

For comparison, the same config on the Phase 1i DEV side was coverage 86.21 % / FA 3.85 %, and on the
Phase 1i HOLDOUT 90.8 % / 7.9 %. The new DEV sits between them — the sides were only hashed, never
balanced, so treat a 3–5 pp difference between splits as noise, not as a change.

**Nothing has been computed on the Phase 1j HOLDOUT beyond the label counts in `split/split_counts.json`.**
