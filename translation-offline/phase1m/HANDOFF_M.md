# Phase 1M — code handoff (label `recon-code`)

Everything below is recon so that **no build agent ever has to open `runner_1l.py` again**.
All line numbers are into **`phase1m/runner_1l.py`** (a byte-identical copy of `phase1l/runner_1l.py`,
959 lines; `f8.py`, `f9.py`, `loader_1l.py`, `validate_f9_1l.py`, `export_hygiene.py` were copied too).
`phase1b…phase1l` are `chmod a-w`: read-only, never edit.

Model is decided: `gemini-3.1-flash-lite`, temperature 0, `thinkingBudget 0`. Do not test another.

---

## (a) Module graph + sys.path

```
phase1m/runner_1m.py (yours)
 └─ phase1m/runner_1l.py            ← import it; HERE = phase1m (see the path warning in (e))
     ├─ phase1m/loader_1l.py  as L  ← imports phase1k/loader_1k.py and REBINDS its _log
     │                                so every logged read lands in phase1m/access_log.jsonl
     ├─ phase1k/runner_1k.py  as R1K
     │   ├─ R1K.R  = phase1j/taskC/runner_1j.py   (load_side, prep_arm, make_state, ledger_rows)
     │   ├─ R1K.P  = phase1i/pipeline_1i.py       (run_pipeline, to_item, rate, ledger_append,
     │   │                                         load_key, _http, parse_reply, MODEL, API, ENV)
     │   └─ R1K.R._C = phase1i/checker_1i.py  (exposed in runner_1l as `C`)
     ├─ phase1m/f9.py  → rebound onto R1K.f9   (the 1L negated-present fix)
     └─ phase1m/f8.py  → rebound onto R1K.f8   (f8 does `import f9`, so f9 must be imported first)
```

`runner_1l.py:40-47` sets `HERE / TOFF / P1J / P1K / REPO` and prepends
`HERE, P1K, P1K/taskB, P1J/taskC` to `sys.path`; `:49-50` imports `loader_1l` and `runner_1k`;
`:52-63` re-prepends `HERE`, drops the phase1k `f8`/`f9` from `sys.modules`, imports the phase1m
copies and asserts the rebind; `:65-68` aliases `R`, `P`, `C`.
**From a script living in `phase1m/`, this is the whole setup you need:**

```python
import sys, os
sys.dont_write_bytecode = True                 # phase1i…phase1l are read-only: no __pycache__
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import loader_1l as L                          # logs into phase1m/access_log.jsonl
import runner_1l as RL                         # does the R1K / f8 / f9 wiring for you
R1K, R, P, C = RL.R1K, RL.R, RL.P, RL.C
```
Run everything as `PYTHONDONTWRITEBYTECODE=1 python3 -B phase1m/<script>.py`.
Module import of `runner_1l` reads **no data** (`main()` is guarded by `__main__`), so it is safe.

Constants worth knowing (`:69-84`): `LEDGERS_RO` (phase1j + phase1k ledgers, read-only),
`CALLS`, `ACCESS`, `HYG`, `FREEZE_HASH`, `DONE`, `STOP_PRE`, `STOP_PLAN`, `FROZEN`
(= `phase1k/FROZEN_CONFIG_1K.json`), `TYPES` (= `R1K.TYPES`, the FA type list T/W/M/S/V/E),
`PRICE_IN=0.25/1e6`, `PRICE_OUT=1.50/1e6`, `PLAN_CAP=1200`, `PHASE_CAP=2000`,
`EXCLUDE_SID=140006` (1k-specific), `DEV_TARGET`, `REPLAY_TARGET`.

---

## (b) Schemas

### record ("rec"), built at `:251-257`, one per ITEM (not per sentence)

```python
{'item_id': 'C:140012:1a2b3c4d',   # or 'W:...'; kind = item_id.split(':')[0]
 'kind': 'C'|'W', 'sid': int, 'n': 1,
 'level': 'A1|A2|B1|B2', 'topic': str, 'sk': str,      # sk = the arm-B Slovak actually measured
 'band': str|None,
 'reference': str,                  # the DISPLAYED reference = first member of the accepted set
 'refs': [str, ...],                # accepted set = [reference] + annotation 'v'
 'answer': str,                     # the learner answer under test
 'judged': 'correct'|'wrong',       # provisional (from the id prefix); OVERWRITTEN by judge labels
 'wrong_type': None|'T'|'W'|'M'|'S'|'V'|'E',
 'half': 'NEW', 'locks': [str, ...],            # flattened annotation 'lk'
 'intent': 'C'|'V'|'TF'|'T'|'W'|'M'|'S',        # WRITER intent, never truth
 'chk': {...}, 'chk_missing': False,
 'rows': [], 'lock_ok': bool, 'lock_released_2_1': <trace>|None}
```
`lock_ok` (`:258-266`): true when the answer contains a normalised lock string, else
`C.lock_equivalent_ok(P.to_item(r))` may release it into `lock_released_2_1`.

### annotation, `annotations.json`: `str(sid) -> obj`

The runner never assumes a flat shape: it uses `hy = a.get('hygienised', a)` (`:244`, `:157`).
Keys actually consumed:
* `v`  : list[str] — the extra accepted references (`apply_hygiene` rewrites `hy['v']` **in place**);
* `lk` : list of str **or list of list of str** (flattened at `:245-250`) — the practised structure
  locks; also read directly by `f9.check` via `_ann()`;
* `m`  : list[str] — mistake patterns, consumed by `compute_chk` through
  `C.pattern_match(C.parse_lock(pat), answer)`;
* `p`  : written onto the annotation by `runner_1j.build_pmap` for the F4p layer.

### chk (the deterministic checker's verdict carried by every record)

`{'verdict': 'correct'|'wrong'|'correct_with_tip', 'step': 'match'|'mistake'|'auto', 'feedback': str}`.
Acceptance is tested as `chk['verdict'] in ('correct','correct_with_tip')`.
`step='match'` ⇒ L1 accept; `step='mistake'` ⇒ L2 mistake rejection (unpatched bug #4);
`step='auto'` ⇒ routed to L2/L3. The production `spelling_variant` step is not reproducible offline.

### calls.jsonl / ledger rows (`call_one`, `:401-416`)

HTTP 200 row: `{ts, model, variant, item_id, req_hash, http:200, counted:true, verdict, reply,
finish, empty, latency_ms, try, prompt_tokens, candidates_tokens, thoughts_tokens, cached_tokens,
thinking, max_output}`. Non-200 row: `{ts, model, variant, item_id, req_hash, http, counted:false,
verdict:null, reply:'', latency_ms, try, error (redacted), transport_retry:true}`.
`verdict` is `P.parse_reply(txt, 'P-E4b')` or the literal `'PARSE_FAIL'`.

**Request hash → verdict.** `R1K.build_req(st, rec, prompt_id) -> (sys_text, user_text, gen_cfg, h)`;
`h` is the request hash and the ONLY key. `plan_requests` (`:481-488`) builds
`{h: (sys, user, gcfg, h, variant_tag, item_id)}`; `hashes_for` (`:491-493`) builds `{item_id: h}`.
`ledger_state()` (`:327-346`) replays all ledgers and returns `(rep, ver, failed, counted_local)`
where `ver[h] = 'SAME'|'DIFF'|'TIP'` (a `PARSE_FAIL` row removes `h` from `ver` and puts it in
`failed`). The per-item verdict map handed to the pipeline is
`vm = {i: ver[h] for i, h in hmap.items() if h in ver}` — items with no verdict are simply absent
from `vm` (tracked as `no_verdict` at `:840`). Identical prompts across variants dedupe to one call.

### judge labels

`labels, _key_rows, _v = R1K.judge_labels(src, purpose)` with `src ∈ {'dev','holdout1j','fresh'}`
(used at `:641` and `:822`). `labels: item_id -> (judged, wrong_type)`. They are the ground truth and
overwrite `r['judged'] / r['wrong_type']` (`:642-643`, `:826-828`). `src='fresh'` requires
`PHASE1K_OPEN_FRESH=1`. **Phase 1M's own labels do NOT come from here** — see (e).

---

## (c) `configure_row` and the guards

```python
R1K.configure_row(st, recs, vm, locktip, guards, f8_on, f9_on, tip_reject)   # phase1k/runner_1k.py:438
    stx = dict(st)
    if locktip: stx['decide'] = locktip_decide(st['decide'])
    res = P.run_pipeline(stx, vm, tip_reject=tip_reject)
    return apply_guards(res, guards, f8_on, f9_on)
```
* `st` — the checker/pipeline state from `R.make_state(recs, ann, ('F4v3',), side_tag=...)`;
* `recs` — **accepted but unused in the body** (state is already baked into `st`); pass the same list
  you built `st` from;
* `vm` — `{item_id: 'SAME'|'DIFF'|'TIP'}`, the L3 model verdicts (missing key = no L3 verdict);
* `locktip` — bool; wraps `st['decide']` in `locktip_decide` so the L2 structure lock becomes a TIP
  source instead of a rejector;
* `guards` — `{item_id: {'f8': {...}|None, 'f9': {...}|None}}` from
  `R1K.guard_readouts(recs, ann, f9_strict)`; each readout has `['verdict'] ∈
  {'reject','accept','tip','abstain'}` (plus `sk`, `en`, `reason`, `sk_frames` for F9);
* `f8_on`, `f9_on` — bools; `apply_guards` turns a `verdict == 'reject'` readout into a rejection;
* `tip_reject` — **TIP-as-rejection**, applied inside `P.run_pipeline(..., tip_reject=...)`, i.e. at
  the L3 decision, *not* in `apply_guards`.

Returned row: `res[item_id] = {'accepted': bool, 'layer': 'L1'|'L2'|'L3'|…, 'reached_l3': bool, …}`
(`accepted`, `layer`, `reached_l3` are the three keys the 1L code reads; `layer` is also used as a
dict key in `col_metrics`).

Guard modules (`phase1m/f8.py`, `phase1m/f9.py`, already rebound onto `R1K` by importing
`runner_1l`):
* `f8.sk_agent(slovak, annotation=None) -> {'agent_nom','agent','voice_sk','reason'}`;
  `f8.en_passive(answer)`; `f8.check(slovak, annotation, answer) -> {'verdict': 'reject'|'accept'|
  'abstain', ...}` (voice guard: Slovak nominative agent vs English passive);
* `f9.check(slovak, annotation, answer) -> {'verdict': 'reject'|'accept'|'tip'|'abstain', 'sk':
  sk_frame(...), 'en': en_frame(...), 'reason', 'sk_frames'}` (time-frame guard; `tip` is emitted
  when the practised lock `lk` is absent from the answer); module flag `f9.REPORTED_STRICT = False`
  (frozen); `f9.sk_frame(slovak, annotation=None) -> {'frames': [...], 'reported': bool, 'reason'}`
  is also used standalone by the F9 hand-check.

---

## (d) Flow, function by function

* `alog(side, what, n, purpose)` `:87-88` — one JSON line into `access_log.jsonl` via `L._log`.
* `compute_chk(r)` `:92-121` → `(chk, how)` with `how ∈ {'match','mistake','auto'}`. Needs
  `r['sid'], r['reference'], r['answer'], r['item_id'], r['sk']`, uses `C.refs_of(it)` (falls back to
  `[reference] + r['refs']`), `C.base.norm`, `C.annot(sid)`, `C.pattern_match(C.parse_lock(pat), ...)`.
* `hygiene_patches(side, purpose)` `:124-133` — globs `HYG/out_<side>_*.json`; **missing dir = no
  hygiene, silently**.
* `apply_hygiene(recs, ann, patches)` `:136-196` — in-memory `{remove, replace}` over the accepted
  set; promotes the first surviving `v` to `reference`; returns stats incl. `sids_touched`,
  `ref_kept`, `examples`.
* `build_side(side, hyg_on, purpose)` `:199-278` → `(st, recs, ann, by, info)`, `by = {item_id: rec}`.
  * DEV / replay1j branch `:204-229`: `PHASE1J_FINAL=1` → `R.load_side('dev'|'holdout', purpose)` →
    deepcopy → optional hygiene → `R.prep_arm('B', s, data)` → `(st, recs, pm)`; `ann = ann_b0`;
    if hygiene moved a reference the stored `chk` is recomputed (`:221-228`).
    `R.load_side(side, purpose) -> (recs, ann, ann_b, sk_new, rew)` (phase1j/taskC/runner_1j.py:89):
    items + annotations + `taskB/annotations_b_<side>.json` + `taskB/sk_new.json` + `rewrites.jsonl`.
  * FRESH branch `:231-278`: `PHASE1K_OPEN_FRESH=1`; `L.load_fresh_sentences/annotations/items`;
    builds the record dict `:251-257`; lock check `:258-266`; optional hygiene `:268-269`;
    `st = R.make_state(recs, ann, ('F4v3',), side_tag='fresh1k')` `:270`; **then** every `chk` is
    computed with `compute_chk` `:272-277` (this ordering matters: the annotations must already be in
    `st`). `info['chk_computed']` counts match/mistake/auto.
* `dev_chk_calibration()` `:281-295` — compute_chk vs the stored DEV verdicts, 0 calls.
* `l3_ids(st, locktip)` `:299-301`; `lock_counts(st, recs)` `:304-308` → `(L2 rejections under BASE,
  L3-eligible under LOCKTIP)`.
* `preflight(st, recs, tag)` `:311-323` — prints both counts; if either is 0 it writes
  `STOP_PREFLIGHT.txt` and `SystemExit`s with 0 calls made (the Phase 1k degenerate-side symptom).
  Reference numbers: DEV 65/318, 1j replay 310/336.
* `check_freeze()` `:743-767` — refuses unless `FREEZE_HASH` exists; `git hash-object` every `*.py`
  in `HERE` and compares with `git rev-parse <hash>:translation-offline/phase1l/<f>` —
  **the path is hard-wired to phase1l**, so 1M must replace this.
* `ledger_state()` `:327-346`, `pace()`/`MIN_INTERVAL=0.30` `:349-359`, `load_keys()` `:362-380`
  (free-tier key from `P.ENV` first, then `P.load_key()`), `call_one(req, key, tries=5)` `:383-422`.
  **Transport rules:** counted = HTTP 200 only; 0/429/5xx retried with exponential backoff
  (1 s ×2, cap 16 s, jitter) and logged `counted:false`; an **empty 200 is a FAILED call — counted,
  never retried, never guessed**; every attempt is appended to `CALLS` via `P.ledger_append`.
  6 worker threads (`:815`), `random.Random(1).shuffle` of the todo list.
* `token_spend()` `:425-441` — counts over `CALLS` only; note the hard-wired
  `PHASE_CAP - 667 - n200` remaining estimate (667 = Phase 1k's spend).
* `col_metrics(recs, res, labels, drop_sid=None)` `:445-473` — coverage, coverage kind-C, FA,
  `fa_by_type` (over `TYPES`), `fa_by_layer` / `fr_by_layer`, `fa_ids`, `fr_ids`, and `targets`
  evaluated on the point AND on the exact Clopper-Pearson interval (`P.rate(k, n) -> {k,n,pct,ci}`).
  Never average columns. `_r(d)` `:476-477` formats `k/n = pct% [lo, hi]`.
* `plan_requests` `:481-488` / `hashes_for` `:491-493` — see (b).
* `section5(...)` `:497-591` — `lock_released` `:502-516` (**`released_by_LOCKTIP_total` is the inert
  counter: it compares `configure_row(..., locktip=True, ...)` with the BASE row and on 1L's data it
  stays 0 because LOCKTIP items still fail elsewhere — report it, do not trust it as evidence**),
  `guard_cost` for F8/F9 `:518-536` (caught / uniquely caught / own cost, measured on top of LOCKTIP
  with the model layer present, reading the module-global `RES_VM[0]`), `b3_tip_abstain` `:538-548`,
  `unpatched_guard_bugs_5_4` `:550-578` (all four deliberately NOT patched), `hygiene` +
  `builder_2_1` `:580-590`.
* `f9_fresh_validation(purpose)` `:594-620` — F9 `sk_frame` vs the stored `tf_gold`
  (agree/conservative/error). **Depends on `tf_gold`, which the new set does not have.**
* `RES_VM` `:623` — module global the §5 block scores against; set it before calling `section5`.
* `run_dev(args)` `:627-740` — zero new calls: builds each side, applies judge labels, prints
  lock/L3 counts, reports cache misses without calling, scores, compares to `DEV_TARGET` /
  `REPLAY_TARGET`, runs the old-vs-new F9 diff (`_F9_OLD`, loaded in `main()` `:946-951`) and the
  DEV hygiene before/after; writes `dev_regression.json`.
* `run_fresh(args)` `:770-934` — refuses if `FINAL_RUN_DONE` exists `:771-772`; `check_freeze()`;
  builds both reference variants (before/after hygiene) `:780-788`; preflight on each; merges the two
  request dicts (dedupe by hash) `:790-791`; `need = hashes with neither verdict nor failure` `:793`;
  **STOP if `len(need) > min(PLAN_CAP, --max-calls)`** — writes `STOP_PLAN.txt`, 0 calls `:796-802`;
  makes the calls `:804-819`; re-reads the ledger; scores both variants, each rebuilding its own
  state `:822-840`; `section5` + `f9_fresh_validation` `:844-846`; the two named cells
  (ACTIVE→PASSIVE intent V, TIME-FRAME-SHIFT intent TF) `:849-856`; writes `results_fresh.json`
  `:858-869`, the markdown table `:871-912`, appends to `F9_REVALIDATION_1L.md` `:914-924`, and
  finally `FINAL_RUN_DONE` `:931-933`.

---

## (e) What `runner_1m.py` must replace, and what it may import

**Path warning.** `import runner_1l as RL` from `phase1m/` gives `RL.HERE = phase1m`, so
`RL.CALLS = phase1m/calls.jsonl`, `RL.HYG = phase1m/hygiene` (absent ⇒ hygiene silently off),
`RL.ACCESS = phase1m/access_log.jsonl`, `RL.FREEZE_HASH/DONE/STOP_* = phase1m/…`.
`RL.LEDGERS_RO` still lists only phase1j + phase1k, so **the 1L verdicts are invisible**. If you want
them, do it explicitly before any `ledger_state()` call:

```python
P1L = os.path.join(RL.TOFF, 'phase1l')
RL.LEDGERS_RO = RL.LEDGERS_RO + [os.path.join(P1L, 'calls.jsonl')]   # read-only reuse
RL.HYG = os.path.join(P1L, 'hygiene')      # only if you want 1L's hygiene patches
```

**Must be written fresh in `runner_1m.py` (the new formats differ from phase1k's fresh files):**

1. `loader_1m` — `P1M/data/sentences.json`, `annotations.json`, `items.json` are **JSON lists/dicts,
   not JSONL**; each load must append one line to `phase1m/access_log.jsonl`
   (`{ts, side, what, caller, n, purpose}`); reuse `loader_1l._log` or copy it.
2. `build_side_1m` — replaces the FRESH branch `:231-278`. Field renames: item text is
   **`answer`**, not `text`; ids are `C:<sid>:<crc32>` / `W:<sid>:<crc32>`; sentences carry `tags`
   and **no `reference` / `refs` / `band` / `tf_gold`**. ⚠ `compute_chk`, `C.refs_of`, `P.to_item`
   and the L1 match all need `r['reference']` and `r['refs']`: derive them from the annotation
   (`hy['v']`, first entry promoted to `reference`) exactly as `apply_hygiene` does, or take them
   from whatever `DATA_HANDOFF.md` fixes — this is the one real open dependency. Keep the rest of
   `:251-277` verbatim, including the `make_state(..., side_tag=…)` **before** the `compute_chk`
   loop. Also set `r['judged']` from the id prefix and carry `it['kind']/['intent']/['form']` as
   writer intent only.
3. `judge_labels_1m` — replaces `R1K.judge_labels`. Read `P1M/judge/out_part1..6.json` +
   `out_controls.json` (`{jid, judged, type}`), map `jid` through `blind_map.json` /
   `controls_map.json` to item ids, and return `{item_id: (judged, type)}`. Read it **ONCE, after
   every verdict exists**; log the read.
4. `check_freeze_1m` — copy `:743-767` with `translation-offline/phase1m/` in the `git rev-parse`
   path.
5. `f9` validation — `f9_fresh_validation` needs `tf_gold`; either drop it or feed a new gold file.
6. Constants: `EXCLUDE_SID`, `DEV_TARGET`, `REPLAY_TARGET`, `token_spend`'s `- 667` are 1k/1L-specific.

**Reusable unchanged by importing `RL` (no copy, no edit):** `compute_chk`, `apply_hygiene`,
`hygiene_patches`, `l3_ids`, `lock_counts`, `preflight`, `ledger_state`, `pace`, `load_keys`,
`call_one`, `token_spend`, `col_metrics`, `_r`, `plan_requests`, `hashes_for`, `section5`, `RES_VM`,
plus `R1K.configure_row / guard_readouts / build_req / locktip_decide / apply_guards / TYPES` and
`P.run_pipeline / to_item / rate / ledger_append / parse_reply / _http / MODEL / API / ENV`.
Frozen config: `json.load(open(RL.FROZEN))['selected']` → `{name:'LOCKTIP+F8+F9 (ALL)', prompt:
'P-FROZEN', locktip, f8, f9, f9_strict:False, tip_reject:True}` — do not re-select.

---

## (f) Zero-call readouts of the existing sides

```python
purpose = '…'                                   # always pass a real purpose: it is logged
# DEV (490 items, 70 sentences)
st, recs, ann, by, info = RL.build_side('dev', False, purpose)
labels, _k, _v = RL.R1K.judge_labels('dev', purpose)

# 1j HOLDOUT replay (490 items, 70 sentences)
st, recs, ann, by, info = RL.build_side('replay1j', False, purpose)
labels, _k, _v = RL.R1K.judge_labels('holdout1j', purpose)

# 1L FRESH (600 items, 70 sentences) — gated
os.environ['PHASE1K_OPEN_FRESH'] = '1'
RL.HYG = os.path.join(RL.TOFF, 'phase1l', 'hygiene')      # else "after hygiene" is unreproducible
st, recs, ann, by, info = RL.build_side('fresh', True, purpose)
labels, _k, _v = RL.R1K.judge_labels('fresh', purpose)

# stored verdicts (add phase1l/calls.jsonl first, see (e))
rep, ver, failed, counted = RL.ledger_state()
hm  = RL.hashes_for(st, recs, RL.l3_ids(st, True), 'P-FROZEN')
vm  = {i: ver[h] for i, h in hm.items() if h in ver}
res = RL.R1K.configure_row(st, recs, vm, True, RL.R1K.guard_readouts(recs, ann, False),
                           True, True, True)
m   = RL.col_metrics(recs, res, {i: labels[i] for i in labels})
```
Raw ledger rows: `RL.R.ledger_rows(path)`. 1L's own results are already on disk and need no code:
`phase1l/results_fresh.json`, `results_fresh.md`, `dev_regression.json`, `calls.jsonl`.

---

## Files produced by this recon

* `phase1m/existing_210.json` — 210 rows `{sid, side, slovak, level, topic}` (dev 70 / holdout 70 /
  fresh1k 70), Slovak/level/topic only, **no references, answers or labels**. `slovak` is the arm-B
  text exactly as the runner measures it (`rec['sk']` out of `build_side`; 0 drift against the
  loader's arm-B sentences). Levels: A1 27, A2 44, B1 74, B2 65.
* `phase1m/export_existing_210.py` — the script that produced it (0 model calls).
* `phase1m/CACHING_CHECK.md` — brief §4: `loader_1k.load_fresh_annotations` returns a
  **fresh object per call** (no memo; contrast `_rewrites`, which does cache).
* `phase1m/DEPENDENCY_READS.md`, `phase1m/access_log.jsonl`.
* Copied and made writable: `f8.py`, `f9.py`, `loader_1l.py`, `runner_1l.py`, `validate_f9_1l.py`,
  `export_hygiene.py`. Empty dirs `data/`, `judge/`, `f8gold/`, `tasks/`.
