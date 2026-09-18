# Phase 1i — CONTEXT for every following agent (read this first, it replaces exploration)

Written by agent S (18 Sept 2026) after building the split. Everything below was verified by running it.
Paths are relative to `~/Projects/and-again-content/translation-offline/`.

**Ground rules of the phase.** Design on DEV only. The HOLDOUT is measured ONCE, by Task F, through
`phase1i/loader.py`. Never open `phase1i/holdout/*` any other way, never open `phase1h/fresh/*` to look at
answers (it is the union of both sides). `phase1c/ phase1e/ phase1f/ phase1g/ phase1h/` are chmod `a-w`
(every regular file); `phase1i/holdout/` is `a-w` as well (readable, not writable). Work in `phase1i/`.

---

## 1 What exists in `phase1i/`

| path | what |
|---|---|
| `make_split.py` | built the split + all working data. Re-runnable, zero model calls, asserts the 1h headline |
| `split/SPLIT.md` | the rule, all counts, the leakage caveat |
| `split/dev_ids.json`, `split/holdout_ids.json`, `split/split_counts.json` | id lists / counts |
| `dev/items.jsonl`, `holdout/items.jsonl` | one JSON line per item, schema in §2 |
| `dev/annotations.json`, `holdout/annotations.json` | `{"<sid>": {"hygienised": {...}, "raw": {...}}}` |
| `dev/l2_false_rejections.json` | **15** ids: DEV row-7 L2-lock false rejections (whole set 27) |
| `dev/false_acceptances.json` | **30** ids: DEV row-7 real false acceptances (whole set 66) |
| `holdout/…` same four files | produced by the same script, never printed, never inspected |
| `loader.py` | `load_items(side)`, `load_annotations(side)`; the only sanctioned reader; logs every load |
| `access_log.jsonl` | UTC time, side, caller, n items — the evidence that the holdout was read once |
| `taskA/scoring_rows.jsonl` | verdict-only rows, both sides (no Slovak, no answer) — safe to aggregate over |
| `taskA/TASK_A.md`, `taskA/TASK_A.json` | Task A result (L3 TIP = rejection) |
| `checker_1i.py` | byte copy of the frozen `phase1h/checker_1h.py` — **this is the file you may modify** |
| `lib_prev.py`, `reference_hygiene.py` | byte copies of the phase1h ones, so `import checker_1i` works |

Split: **DEV 467** items (203 correct all judged really correct, 264 wrong of which **260** judged really
wrong), **HOLDOUT 513** (217 correct, 296 wrong of which **290** judged really wrong).
Rule `side = int(sha256(item_id.utf-8).hexdigest(),16) % 2`, 0 = DEV.
**Leakage caveat: 138 of the 140 sids have items on both sides** — per-sentence changes (a hand-edited
annotation, a reference rewrite, a list keyed to a sid) are NOT measurable on this holdout. Say so if you
make one.

### Rule of use

```python
import sys, os
P1I = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1i')
sys.path.insert(0, P1I)
from loader import load_items, load_annotations
items = load_items('dev')             # 467 dicts
ann   = load_annotations('dev')       # sid(str) -> {'hygienised':…, 'raw':…}
```
`load_items('holdout')` raises `PermissionError` unless `PHASE1I_TASK_F=1` **and**
`phase1i/HOLDOUT_RUN_DONE` does not exist. Task F must `touch phase1i/HOLDOUT_RUN_DONE` when finished.
*Disclosure: `access_log.jsonl` already contains one `holdout` line from agent S's guard smoke test
(`caller "<string>"`, 513 items). No holdout item was printed or read; the guard test only counted lines.*

---

## 2 `items.jsonl` schema (one line per judged answer)

```
item_id   "C:20298:610089844" | "W:20298:1595880954"   frozen 1h id = kind:sid:int(md5(answer)[:8],16)
side      "dev" | "holdout"
kind      "C" (writer aimed at a correct answer) | "W" (writer aimed at a wrong answer)
sid       int Slovak sentence / exercise id      n     1-3 (C) or 1-4 (W), the writer's slot
level     "A1".."B2"      topic  the practised grammar topic string used in the P-B prompt
sk        the Slovak sentence (ground truth)     band  "1-6"|"7-9"|"10-12"|"13-16"|"17+"
reference the English reference the checker/prompt uses (annotation v[0] for fresh sids)
refs      list: checker_1h.refs_of() = [reference] + annotation v[] + hygiene gender variants
answer    the learner answer under test
judged    "correct" | "wrong"   the BLIND gold judgement (fresh/judgements.jsonl). THE ONLY TRUTH.
wrong_type "T"|"W"|"M"|"S" for kind W (tense / word / meaning-add-drop / small-slip family), null for C
half      "OLD" (one of the 80 in-sample sentences) | "NEW" (one of the 60 fresh sentences)
chk       {"verdict":"correct"|"correct_with_tip"|"wrong","step":"auto"|"match"|"mistake","feedback":…}
          = the APP's own offline checker verdict (produced by phase1h/chk_fresh.ts); this is what routes
          the item to L1 / L2 / L3. chk_missing is false everywhere in this set.
locks     the annotation's `lk` list (the grammar the exercise locks)   lock_ok bool
lock_released_2_1  null or {"lock":…,"equivalent":…} when §2.1 released the lock
rows      {"row7": {...}, "row8": {...}}   the Phase 1h per-item verdicts, see below
```

`rows.row7` (= flags F1 F2 F3 F4v2 F5 F2B × prompt **P-B**, the headline row that produced 82.1 % coverage
and 12.0 % false acceptance) and `rows.row8` (same flags × **P-C**, VOID — 311 empty replies, 1h §5 D3):

```
layer       "L1"|"L2"|"L3"|"F3"|"F5"|"F4v2"|"F2B"   the DECIDING layer
accepted    bool                                    verdict "correct"|"correct_with_tip"|"wrong"|"failed"
tip         tip text or null       why  the frozen one-line explanation
model       "SAME"|"TIP"|"DIFF"|null   the model's parsed label (null = no call reached this item)
reply       the model's raw reply string (always 1 word in this run)
call_made   bool        failed_call  bool  (an unparsable/empty reply: counted, never retried, never guessed)
```

Denominators, whole set: coverage 345/420, real FA 66/550 (row 7). Per side, row 7: DEV coverage 160/203
= 78.8 %, FA 30/260 = 11.5 %; HOLDOUT coverage 185/217 = 85.3 %, FA 36/290 = 12.4 % (aggregates only, from
`taskA/TASK_A.json`). The two sides are 6.5 pp apart on coverage by chance alone — remember that when you
read a holdout number later: the sides were never balanced, only hashed.

---

## 3 Running the OFFLINE layers on an item from python, with NO side effects

`checker_1i.py` is import-safe (its `main_1h()` runs only under `__main__`) but **not side-effect-free at
import**: it mutates the `lib_prev` module object (`base.LEDGER`, `base.LOG`, `base.CALL_CAP`,
`base.ATTEMPT_CAP`, `base.MODEL_CFG`, `base.prompt`, `base.ledger_append`), inserts two `sys.path` entries
and asserts that `lib_prev.py` sits in its own directory. It writes no file at import and makes no call.
Because its `HERE` is now `phase1i/`, its own path constants point at `phase1i/` — `base.LEDGER` =
`phase1i/calls.jsonl`, `FRESH` = `phase1i/fresh` (does not exist), `ANN_DIRS[0]` =
`phase1i/fresh/annotations_new_60` (does not exist). **Do not repoint them at phase1h to re-load the fresh
set.** Seed the checker from the DEV files instead — that reproduces the frozen behaviour exactly and reads
nothing from `phase1h/`:

```python
import os, sys, json
P1I = os.path.expanduser('~/Projects/and-again-content/translation-offline/phase1i')
sys.path.insert(0, P1I)
import checker_1i as C                      # imports the phase1i copies of lib_prev / reference_hygiene
from loader import load_items, load_annotations

recs, ann = load_items('dev'), load_annotations('dev')
for s, a in ann.items():                    # bypass hygiene: use the stored hygienised annotation
    C._ANN[int(s)] = a['hygienised']
for r in recs:
    C.SK_OF[r['sid']] = r['sk']

def to_item(r):                             # the exact dict shape the layers expect
    return {'item_id': r['item_id'], 'kind': r['kind'], 'exercise_id': r['sid'], 'set': 'NEW',
            'level': r['level'], 'topic': r['topic'], 'sk': r['sk'], 'reference': r['reference'],
            'answer': r['answer'], 'verdict': r['chk']['verdict'], 'step': r['chk']['step'],
            'feedback': r['chk']['feedback'], 'chk_missing': r['chk_missing'],
            'wrong_type': r['wrong_type'], 'wrong_why': '', 'locks': r['locks'],
            'lock_ok': r['lock_ok'], 'lock_released_2_1': r['lock_released_2_1'],
            'fa_class': None, 'fa_judgement': None, 'n': r['n']}

ROW7 = {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 1}
vm = {r['item_id']: r['rows']['row7']['model'] for r in recs if r['rows']['row7']['model']}
d = C.decide(to_item(recs[0]), ROW7, vm)    # 0 model calls: vm replays the frozen ledger verdicts
```

`C.decide(it, flags, verdicts)` is the whole pipeline (`checker_1i.py:802`). Order and signatures
(line numbers are the same in `checker_1h.py`):

| # | layer | function | returns | what it does |
|---|---|---|---|---|
| 1 | **F3** | `f3_deletion(it)` :442 | `(hit, missing_tokens)` | content word of the reference dropped (word-class table) → reject |
| 2 | **F5** | `f5_adjunct_deletion(it)` :705 | `(hit, trace)` | any-position adjunct/particle deletion that carries meaning → reject |
| 3 | **F4v2** | `f4v2_subject_mismatch(it)` :608 | `(hit, trace)` | subject person/number/gender read ONLY from Slovak morphology (`sk_features` :536), abstains when underdetermined → reject. `F4` (:512, the older EN-side version) runs only when `F4v2` is off |
| 4 | **route** | `lib_prev.route(it)` :121 | `(layer, why)` | uses the app checker's `chk`: → `L1` accept, `L2` grammar veto, else `L3` |
| 5 | **L2** | the lock | — | `it['step']=='mistake'` → reject at once; otherwise `f1_lock_ok(it)` (:299, `parse_lock` :194 + `pattern_match` :253) may release it, else `f2_equivalent(it)` (:319) may release it **with a tip** (`f2_tip` :371). Not released → reject. `lock_equivalent_ok(it)` (:1504, §2.1) already ran at load time and is reflected in `lock_ok` / `lock_released_2_1` |
| 6 | **L3** | the model | — | `verdicts[item_id]`: missing → `verdict='failed'`, not accepted; `DIFF` → reject; `SAME` → `correct`; `TIP` → `correct_with_tip`, **accepted** (lines 846-855; this is the switch Task A flips) |
| 7 | **F2B** | `f2_boundary_violation(it)` :773 | `(hit, trace)` | runs only on an accepted `correct_with_tip`: withdraws the tip when the span/ongoingness meaning did not survive (`en_span_tokens` :1548, `EN_SPAN` :758, `SK_SPAN` :742, `SK_ONGOING` :757) |

Supporting data and where it lives:

- **annotation fields** (`phase1c/annotated_after/<sid>.json` for the 80, `phase1h/fresh/annotations_new_60/<sid>.json`
  for the 60; both already inlined in `dev/annotations.json`): `id, t, lv, v` (accepted references),
  `lk` (locks), **`s`** (ids of the shared synonym groups — the fresh 60 have NONE, 1h §5 D4: all their
  alternatives sit in `alt`), `d` (OPTIONAL tokens, also what hygiene (a) writes into), **`g`** (the gender
  chain, e.g. `[["she"]]`, consumed by `reference_hygiene.gender_variants()` through `refs_of()` :402 —
  it reaches F3/F5/F2B but **never the prompt**, a known false-rejection cause), `p` (`"+word"` insertions /
  `"-span"` removals), `m` (mistake patterns), `alt` (per-word alternatives), `o`.
- **the synonym table on disk**: `phase1c/synonyms/table.json`, `ng_phase1c.json`, `review_added.json`,
  each `{"groups":[{"m":[members…]}]}`; read by `syn_groups()` :1461 and `syn_equivalents(phrase)` :1477.
  These files are `a-w`; a new word table is out of scope by the standing rule of the whole feature.
- `optional_tokens(it)` :415 (articles + `d` + parenthesised optionals), `subseq_missing()` :428,
  `toks/expand/form_of` :141-194, `annot(eid)` :392 (hygienises in memory), `raw_annot(eid)` :384.
- `C.band(sk)` :1715, `C.BANDS` :1711.

---

## 4 The model layer as it was actually called (row 7 = P-B, row 8 = P-C)

- **System instruction** `lib_prev.SYS` :225-228 — "You judge English translations. Reply with exactly one
  word: SAME, TIP or DIFF. SAME = … TIP = same meaning and acceptable, but with a small slip. DIFF = …
  No explanation."
- **User prompt** `lib_prev.prompt(it, variant)` :231-237 — four or five lines:
  `Slovak: …` / `Reference English: …` / `Learner: …` / *(P-B only, inserted at index 3)*
  `Practised grammar: <topic> — ALREADY VERIFIED as correct in this answer; judge meaning and vocabulary
  only.` / `SAME, TIP or DIFF?`
  **P-C** = `checker_1i.prompt()` :57-63, which rebuilds the P-B text and inserts `PC_LINE` (:52-53, "The
  SLOVAK sentence is the ground truth and the English reference is only one valid rendering of it; judge the
  learner against the Slovak, not against the reference wording.") immediately before the last line.
  `checker_1i` overwrites `base.prompt` at import (:66), so `lib_prev.prompt` is the P-B builder and
  `checker_1i.prompt` is the dispatcher. **The prompt contains no annotation, no synonym group and no
  gender chain.**
- **Call** `lib_prev.call_model(bud, model, variant, it, cfg, max_out)` :268 →
  `POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent`
  (`API` :26, `MODEL = 'gemini-3.1-flash-lite'` :46 of the checker).
  Body: `{"systemInstruction":{"parts":[{"text":SYS}]}, "contents":[{"role":"user","parts":[{"text":prompt}]}],
  "generationConfig":{"temperature":0,"maxOutputTokens":24,"thinkingConfig":{"thinkingBudget":0}}}` —
  **thinking off**, `MAX_OUT = 24` (:45), `thinkingConfig` comes from `phase1e/model_config.json` via
  `cfg_1h()` :916.
- **Key**: `lib_prev.load_key()` :39 parses `GEMINI_API_KEY` from `~/Projects/and-again/.env.local` at call
  time and sends it only in the `x-goog-api-key` header (`http()` :168). Never print it, never read that
  file yourself, never put a key on a command line.
- **Parsing**: `parse_verdict(js)` :243 concatenates the candidate parts and regexes
  `\b(SAME|TIP|DIFF)\b` on the upper-cased text; no match → `'PARSE_FAIL'`, which is a **FAILED call** —
  counted, never guessed, never retried (an item with no verdict is not accepted). `429`/`5xx` are logged
  with `counted:false` and retried up to 4 times with the server's `retryDelay`.
- **Cost**: `lib_prev.PRICE['lite']` = $0.25 in / $1.50 out per 1M tokens; measured $0.000030 per L3 call;
  148,235 in / 934 out tokens for the whole 1h run; median latency 768 ms, p95 1061 ms.

### `calls.jsonl` ledger format (one JSON object per attempt, `phase1h/calls.jsonl`, 1246 rows)

```
ts (unix float) · model · variant ("P-B"|"P-C") · item_id · http (200|429|5xx|0)
counted (bool: did it consume budget) · verdict ("SAME"|"TIP"|"DIFF"|"PARSE_FAIL") · reply (raw text)
finish (finishReason) · cold · latency_ms · thinking ("{\"thinkingBudget\": 0}") · max_output
prompt_tokens · candidates_tokens · thoughts_tokens · cached_tokens · empty_due_to_thinking
```
Cache key everywhere in the code is the triple `(model, variant, item_id)`; `Bud1h` (:903) loads
`phase1i/calls.jsonl` as its own ledger and the 1e/1f/1g ledgers as read-only seeds, and
`verdict_map_own(variant, bud)` (:1672) is the fresh-set map that may use **only** the own ledger.
A ledger row is the evidence for a verdict: if you make calls, keep writing them there.

---

## 5 The two DEV error lists (row 7)

- `dev/l2_false_rejections.json` — **15** ids (whole set 27, so 12 sit in the holdout): correct answers
  vetoed by the L2 lock and released by neither F1 nor F2. Known cause for at least one of them
  (`C:6265:241916334`, 1h §5 D4): "No one" is absent from `alt` because the annotation prompt forbids
  someone/somebody-type pairs.
- `dev/false_acceptances.json` — **30** ids (whole set 66, so 36 sit in the holdout): wrong answers judged
  really wrong that the row-7 stack accepted. On the whole set 65 of 66 come from L3 (42 TIP, 23 SAME) and
  exactly 1 from an offline layer (L1); 47 of 66 are wrong-type M or S. One of them
  (`W:9907:1778280655`) is a writer artefact — byte-identical to the reference (1h §5 D5).

---

## 6 Task A, already done (`taskA/TASK_A.md`)

Counting an L3 `TIP` as a rejection — **a flip of an existing switch, not a new rule** — moves row 7 from
coverage 345/420 = 82.1 % [78.1–85.7] and real FA 66/550 = 12.0 % [9.4–15.0] to coverage 324/420 = 77.1 %
[72.8–81.1] and real FA 24/550 = 4.4 % [2.8–6.4]: **-42 false acceptances for -21 accepted correct
answers**. That is the cheapest single lever in the stack and it is measured on DEV+HOLDOUT together
(legitimate: it re-scores an existing measurement, it designs nothing). Every following design decision
must be taken on DEV only and must state whether it is additive to this switch or an alternative to it.
