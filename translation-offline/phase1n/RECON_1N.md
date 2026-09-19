# Phase 1N — recon of the Phase 1M runner (label `recon-code`)

Purpose: a later agent builds `phase1n/loader_1n.py` + `phase1n/runner_1n.py` from **this file alone**.
Every reference is `file:line`. `M = translation-offline/phase1m` (read-only), `N = phase1n`,
`TOFF = translation-offline`. Model everywhere: `gemini-3.1-flash-lite`, temperature 0,
thinkingBudget 0 — never another.

---

## 1. Import chain — what actually executes at run time

`M/FREEZE_FILES:3-9` names the seven modules that execute under `--final`:
`runner_1m.py, runner_1l.py, loader_1m.py, loader_1l.py, f8v2.py, f8.py, f9.py`.
Everything else in `M/FREEZE_FILES:11-24` is present but not executed.

```
M/runner_1m.py                                   entry point (main guarded, :840-841)
 ├─ sys.dont_write_bytecode = True               :22   (phase1b..1l are chmod a-w)
 ├─ sys.path.insert(0, HERE)                     :23-24
 ├─ import loader_1l as L                        :25   → M/loader_1l.py:11-14 puts TOFF/phase1k on
 │                                                      sys.path, imports phase1k/loader_1k and
 │                                                      REBINDS its _log → M/access_log.jsonl
 ├─ import runner_1l as RL                       :26   ← does ALL of the deep wiring:
 │    RL:40-47  HERE/TOFF/P1J/P1K/REPO, prepends HERE, P1K, P1K/taskB, P1J/taskC to sys.path
 │    RL:49-50  import loader_1l, import runner_1k as R1K
 │    RL:52-63  re-prepend HERE, drop phase1k f8/f9 from sys.modules, import the phase1m copies
 │              (f9 BEFORE f8 — f8 does `import f9`), assert R1K.f8/R1K.f9 are the local ones
 │    RL:65-67  R = R1K.R (phase1j/taskC/runner_1j), P = R1K.P (phase1i/pipeline_1i), C = R._C
 │              (phase1i/checker_1i)
 └─ import loader_1m as LM                       :27   M-only data door, no outside reads
```

Earlier-phase modules that therefore execute: `phase1k/loader_1k.py`, `phase1k/runner_1k.py`,
`phase1j/taskC/runner_1j.py`, `phase1i/pipeline_1i.py`, `phase1i/checker_1i.py`,
`phase1i/lib_prev.py` (imported lazily inside `P.sys_text` / `P.pb_lines`).

Ledger scope is set once at `runner_1m.py:36`:
`RL.LEDGERS_RO = list(RL.LEDGERS_RO) + [phase1l/calls.jsonl]`; `RL.LEDGERS_RO` itself is
`[phase1j/ledger.jsonl, phase1k/ledger.jsonl]` (`RL:69`). Because `RL.HERE == phase1m`,
`RL.CALLS/ACCESS/HYG/FREEZE_HASH/DONE/STOP_*` all point into `phase1m` (`RL:70-76`,
`runner_1m.py:37-46`). **1N must append `phase1m/calls.jsonl` the same way if it wants the 1115
stored 1M verdicts.**

Run line: `PYTHONDONTWRITEBYTECODE=1 python3 -B phase1n/runner_1n.py --dev|--dry|--final`.

---

## 2. Where the L3 prompt (P-FROZEN) lives — and the voice rule

### 2.1 Construction

`phase1k/runner_1k.py:77-89` — the only builder:

```python
def build_req(st, r, prompt_id):
    """(system, user, generationConfig, hash). prompt_id P-FROZEN is byte-identical to Phase 1j arm B."""
    it = P.to_item(r)
    lines = P.pb_lines(st, it)            # phase1i/pipeline_1i.py:154-166
    head, tail = lines[:-1], lines[-1]
    g = P.gender_chain(st, r['sid'])      # pipeline_1i.py:182-197
    gline = P.GENDER_TMPL.format(...) if g else None
    extra = ([gline] if gline else []) + [P.GROUND_LINE, P.WORDING_LINE]
    if prompt_id == 'P-1K':
        extra = extra + list(NEW_RULES)   # <-- P-1K ONLY
    sysx, gcfg = P.sys_text(st, 'P-E4b'), P.GEN_CFG
    user = '\n'.join(head + extra + [tail])
    return sysx, user, gcfg, R.req_hash(sysx, user, gcfg)
```

* **system text** = `P.sys_text(st, 'P-E4b')` → `pipeline_1i.py:168-179`; since the variant is not
  `'P-E2'` it returns `lib_prev.SYS` unchanged, i.e. `phase1i/lib_prev.py:225-228`:
  > "You judge English translations. Reply with exactly one word: SAME, TIP or DIFF. SAME = the
  > learner sentence means the same as the reference and is correct English. TIP = same meaning and
  > acceptable, but with a small slip. DIFF = different meaning, or not correct English. No
  > explanation."
* **user body head/tail** = the frozen P-B prompt read out of the checker itself
  (`pipeline_1i.py:154-166` → `C.prompt(it,'P-B')` → `checker_1i.py:57-63` → `lib_prev.py:231-237`):
  `Slovak: …` / `Reference English: …` / `Learner: …` / `Practised grammar: <topic> — ALREADY
  VERIFIED as correct in this answer; judge meaning and vocabulary only.` / tail `SAME, TIP or DIFF?`
* **the two inserted rules**, `pipeline_1i.py:46-51`:
  * `GROUND_LINE` — "The SLOVAK sentence is the ground truth and the English reference is only one
    valid rendering of it; judge the learner against the Slovak, not against the reference wording."
  * `WORDING_LINE` — "A synonym, a different word order or a different phrasing that keeps the
    Slovak meaning is SAME; a word that changes which thing, person, place, time or quantity the
    Slovak names is DIFF."
* generation config `pipeline_1i.py:33`:
  `GEN_CFG = {'temperature': 0, 'maxOutputTokens': 24, 'thinkingConfig': {'thinkingBudget': 0}}`;
  `MODEL` `:32`, `API` `:34`, `ENV` `:35` (`~/Projects/and-again/.env.local`).

### 2.2 THE VOICE RULE — verbatim, and where it is NOT

The only voice rule in the whole stack is `NEW_RULES[1]`, `phase1k/runner_1k.py:57-59`, quoted in
full:

> 'Voice: if the Slovak names an agent in the nominative and the learner sentence moves that agent out '
> 'of subject position or drops it (an active Slovak sentence turned into an English passive), that is '
> 'DIFF. Where the Slovak is itself impersonal or passive, an English passive is SAME.'

Its two siblings, for completeness — `NEW_RULES[0]`, `runner_1k.py:54-56`:

> 'Judge the learner sentence against the SLOVAK sentence, not against the English reference. A '
> 'different structure that is correct English and means what the Slovak means is SAME, even when it '
> 'avoids the structure the reference uses.'

and `NEW_RULES[2]`, `runner_1k.py:60-63`:

> 'Time: the time frame (past, present or future) must match the Slovak — a Slovak perfective present '
> 'form ("dokonci") means the FUTURE, and an English present tense inside an if- or when-clause about '
> 'the future is fine. A different English tense inside the Slovak\'s own time frame (for a Slovak past '
> 'imperfective: "trained", "was training", "had been training") is SAME.'

**Load-bearing finding: `NEW_RULES` is appended only when `prompt_id == 'P-1K'`
(`runner_1k.py:85-86`). `FROZEN_CONFIG_1M.json` freezes `"prompt": "P-FROZEN"`, so the prompt that
produced all 1115 Phase 1M L3 verdicts contains NO voice rule at all** — the model was never told
that agent demotion / active→passive is a mistranslation. `PROMPTS = ('P-FROZEN', 'P-1K')`
(`runner_1k.py:65`). The 30.68 % agent-demotion cell of Phase 1M was measured under a prompt silent
on voice; F8/F8v2 is the only thing in the stack that encodes the rule.

### 2.3 How the prompt text binds the request hash and the ledger

`R.req_hash(sysx, user, gcfg)` (phase1j/taskC/runner_1j.py) over **system + user + generationConfig**
is the ONLY cache key. `RL.plan_requests` (`runner_1l.py:481-488`) returns `{h: (sys,user,gcfg,h,
variant,item_id)}`; `RL.hashes_for` (`:491-493`) returns `{item_id: h}`; `RL.ledger_state()`
(`:327-346`) replays every ledger and returns `(rep, ver, failed, counted_local)` with
`ver[h] ∈ {'SAME','DIFF','TIP'}` (a `PARSE_FAIL` row deletes `h` from `ver` and adds it to `failed`);
`vm = {i: ver[h] for i,h in hmap.items() if h in ver}` (`runner_1m.py:601`).

Consequences for 1N:
* Changing **one character** of `GROUND_LINE`, `WORDING_LINE`, `lib_prev.SYS`, the P-B lines, the
  topic string, the reference, the answer, or `GEN_CFG` changes `h` → **every stored verdict becomes
  a cache miss and must be paid for again**. Adding the voice rule (i.e. selecting `P-1K` or a new
  `P-1N`) invalidates all 1115 1M verdicts by construction.
* Identical prompts across variants dedupe to one call; the ledger row keeps the item_id of the
  first requester, so **map verdicts by `req_hash`, never by the row's `item_id`**.
* The 1M plan was `unique 1115 / reused 0 / new 1115` (`results_1m.json:calls`), i.e. the 1L ledger
  contributed nothing to the new side.

---

## 3. F8 / F8v2 — binding, application, and how to run with F8 deciding nothing

### 3.1 Binding

1. `runner_1l.py:52-63` imports `M/f9.py` then `M/f8.py` and rebinds `R1K.f8, R1K.f9` — so after
   `import runner_1l`, F8 **v1** is already the active module.
2. `runner_1m.py:86-104 select_f8(name)`: `'f8'` → the already-imported module; any other name →
   `importlib.util.spec_from_file_location(name, HERE/<name>.py)`, `exec_module`, require
   `hasattr(mod,'check')`, then `R1K.f8 = mod`. Called from `run_dev:434`, `run_dry:520`,
   `run_final:560`, and temporarily inside the F8v1 shadow (`:661-675`, restored in `finally`).
3. `FROZEN_CONFIG_1M.json` picks the module by name (`"f8_module": "f8v2"`); `load_cfg`
   `runner_1m.py:65-83` builds `sel` and refuses `locktip=false` (`:73-74`). CLI overrides
   `--f8/--f9/--tip` are accepted in `--dev` only (`main:823-825`).

### 3.2 Application

* `R1K.guard_readouts(recs, ann, strict)` `phase1k/runner_1k.py:271-288` — calls
  `f8.check(r['sk'], ann[str(sid)], r['answer'])` and `f9.check(...)` for **every** record,
  regardless of whether the guard decides; exceptions become `{'verdict':'abstain'}`. It flips
  `f9.REPORTED_STRICT` for the call and restores it.
* `R1K.apply_guards(res, guards, f8_on, f9_on)` `runner_1k.py:291-303` — a guard may only turn an
  acceptance into a rejection:

```python
if d['accepted']:
    if f8_on and (g.get('f8') or {}).get('verdict') == 'reject':
        d['accepted'], d['layer'] = False, 'F8'
    elif f9_on and (g.get('f9') or {}).get('verdict') == 'reject':
        d['accepted'], d['layer'] = False, 'F9'
```

* `R1K.configure_row(st, recs, vm, locktip, guards, f8_on, f9_on, tip_reject)` `runner_1k.py:438`:
  wraps `st['decide']` in `locktip_decide` when `locktip`, runs `P.run_pipeline(stx, vm,
  tip_reject=...)`, then `apply_guards(res, guards, f8_on, f9_on)`.

### 3.3 Recipe: F8 decides NOTHING, both readouts still reported as shadows

`guard_readouts` computes the readouts independently of `f8_on`, so the shadow costs 0 calls:

```python
select_f8('f8');   g_v1 = R1K.guard_readouts(recs, ann, sel['f9_strict'])   # F8 v1 readouts
select_f8('f8v2'); g_v2 = R1K.guard_readouts(recs, ann, sel['f9_strict'])   # F8 v2 readouts
guards = {i: {'f8': None, 'f9': g_v2[i]['f9']} for i in g_v2}   # or pass g_v2 with f8_on=False
res      = R1K.configure_row(st, recs, vm, True, guards, False, sel['f9'], sel['tip_reject'])  # HEADLINE
sh_v1    = R1K.configure_row(st, recs, vm, True, g_v1,  True,  sel['f9'], sel['tip_reject'])   # shadow
sh_v2    = R1K.configure_row(st, recs, vm, True, g_v2,  True,  sel['f9'], sel['tip_reject'])   # shadow
```

* `f8_on=False` is sufficient (`apply_guards` reads the readout only when `f8_on`); nulling the
  `'f8'` key as well is belt-and-braces against a later `apply_guards` edit.
* Use `runner_1m.py:366-374 guard_delta(by, lab, res_on, res_off, name)` for caught / uniquely
  caught / cost, plus `sum(1 for i in by if (g[i]['f8'] or {}).get('verdict')=='reject')` as the raw
  reject-readout count (as `runner_1m.py:658-660` does).
* Ordering caveat (`M/tip_readout_1m.py:8-11`): `phase1i/checker_1i` keeps ONE module-global
  annotation/SK map. Build the side first, compute readouts/scores for it, and do not build a second
  side in between.
* `f9.REPORTED_STRICT = False` is frozen; strict is only read out (`section5` bug 2,
  `runner_1l.py:554-555`).

---

## 4. The runner, block by block

| block | where | notes for 1N |
|---|---|---|
| `say()` / `alog()` | `runner_1m.py:54-61` | every line also appended to `run_1m.log`; `alog` → `LM._log` |
| `load_cfg` | `:65-83` | requires all 8 keys in `FROZEN_CONFIG_1M.json`; refuses `locktip=false`; builds `sel['name']` |
| `select_f8` | `:86-104` | see §3.1 |
| `_band` | `:108-110` | Slovak word-count bucket `1-6/7-9/10-12/13-16/17+` |
| **`build_side_1m`** | `:113-191` | the FRESH-branch replacement. Loads `LM.load_sentences/annotations/items`; flattens `hy['lk']` (str or list-of-list) `:135-140`; `refs = hy['v']`, `reference = refs[0]` `:141-144`; record dict `:142-150` (adds `form`, `tags`, drops `tf_gold`); lock check `:151-159` (`C.base.norm` containment, else `C.lock_equivalent_ok(P.to_item(r))` → `lock_released_2_1`); optional hygiene `:161-165`; `st = R.make_state(recs, ann, ('F4v3',), side_tag='fresh1m')` with fallback to `'fresh1k'` on an unknown tag `:166-170`; **then** `compute_chk` for every record `:171-179` (order matters); degenerate-chk abort → `STOP_CHK.txt` `:184-190` |
| `RL.compute_chk(r)` | `runner_1l.py:92-121` | `(chk, how)`, `how ∈ match/mistake/auto`; needs `sid, reference, refs, answer, item_id, sk`; uses `C.refs_of`, `C.base.norm`, `C.annot(sid)`, `C.pattern_match(C.parse_lock(pat), …)` over annotation `m`. `chk = {'verdict','step','feedback'}`; accept = verdict in `('correct','correct_with_tip')` |
| `preflight_1m` | `runner_1m.py:194-204` | `RL.lock_counts` (`runner_1l.py:304-308`) → (L2 lock rejections under BASE, L3-eligible under LOCKTIP); either 0 ⇒ `STOP_PREFLIGHT.txt` + `SystemExit`, 0 calls. 1M actuals 249 / 1115 |
| `check_freeze_1m` | `:208-240` | needs `FREEZE_HASH` **and** `FREEZE_FILES`; refuses if any `*.py` in the dir is missing from the list `:216-220`; `git hash-object <f>` vs `git rev-parse <hash>:translation-offline/phase1m/<f>`, cwd `REPO` (= `RL.REPO` = content repo root) `:227-231` |
| `plan_1m` | `:244-246` | `RL.plan_requests` + retag variant `'L-1M:<tag>'` (tag `main` / `after`) |
| `counted_local` | `:249-255` | counts `counted:true` rows in `phase1m/calls.jsonl` via `R.ledger_rows` |
| cap | `:47`, `:550-551`, `:570-576` | `PHASE_CAP_1M = 1600`; `--final` writes `STOP_PLAN.txt` and exits with 0 calls when `done + len(need) > cap`; nothing is trimmed. (`RL.PLAN_CAP=1200` / `RL.PHASE_CAP=2000` are 1L constants, unused here) |
| transport | `make_calls :258-291` + `RL.load_keys :362-380` + `RL.call_one :383-422` + `RL.pace :349-359` | key from `P.ENV` (`~/Projects/and-again/.env.local`) first, then `P.load_key()`; 6 worker threads; `random.Random(1).shuffle(todo)` so one outage damages all cells equally; `MIN_INTERVAL = 0.30`; 5 tries, exponential backoff 1 s ×2 capped 16 s + jitter; **counted = HTTP 200 only**; non-200 rows logged `counted:false, transport_retry:true`; **an empty HTTP 200 is a counted failure — never retried, never guessed** (item stays out of `vm`, lands in `no_verdict_items`); `streak >= 5` fully-retried failures ⇒ `wall`, remaining requests skipped |
| quota wall | `:578-593` | `RUN_PAUSED.txt` + `raise SystemExit(3)` **before any judge label is read**; rerun `--final` resumes by request hash |
| labels | `:596-600`, `loader_1m.py:105-151` | read ONCE, after every request has a verdict or a counted failure. `load_labels` merges `judge/out_part*.json` through `blind_map.json`, validates `judged ∈ {correct,wrong}` and `type ∈ TYPES` (`loader_1m.py:24` — **`TYPES` still contains `'V'`**), nulls the type on `correct`, records conflicts/unknown jids in `meta['rejected_rows']`; controls come from `out_controls.json` + `controls_map.json` → `{item_id: [(judged,type),…]}`. Labels overwrite `r['judged']/r['wrong_type']` `:597-599` |
| metrics | `RL.col_metrics runner_1l.py:445-473`, `_r :476-477` | coverage (all judged-correct), `coverage_kindC`, FA (all judged-wrong), `fa_by_type` over `TYPES`, `fa_by_layer` / `fr_by_layer` (denominators wrong / correct), `fa_ids`, `fr_ids`, `targets` evaluated on the point **and** on the CP interval `:469-472`. Columns are never averaged |
| CP interval | `phase1i/pipeline_1i.py:387-413 cp(k,n,alpha=0.05)`, `rate(k,n) :415-416` | exact Clopper-Pearson by 200-step bisection; `rate` → `{k,n,pct,ci}`; `_r` formats `k/n = pct% [lo, hi]` |
| cells | `runner_1m.py:344-363 cell_by_intent` + call site `:612-616` | `AGENT-DEMOTION (writer intent V, judged wrong)` with `split_by_form=True` over forms `passive/cleft/reported/dropped/None`, and `TIME-FRAME-SHIFT (intent TF)` |
| §5.1 counters | `released_fixed :377-398`, call `:619-625` | see §6 |
| shadows | `:639-677` | a) F9 had it stayed on, b) the other TIP setting, c) F8v1 in place of the selected module (rebinds F8, recomputes readouts, restores in `finally`), d) the active F8 module. They decide nothing |
| §13 builder limit | `_lev :295-304`, `l1_nearmiss :307-340`, block `:680-701` | near-miss = not an exact L1 match but within total edit distance ≤ 2 with ≤ 1 edit per token on equal token counts; unequal token counts fall back to whole-string Levenshtein ≤ 2 and are reported as `len_mismatch_subset` |
| §14 judge noise | `judge_noise :401-419`, call `:702` | controls vs part labels, judged and type disagreement rates + caveat |
| §5 continuity block | `RL.section5 runner_1l.py:497-591`, call `runner_1m.py:704-708` | wrapped in `try`; on failure the error string lands in `results['section5_1L_block']` and nothing else breaks |
| `spend` | `:422-428` + `RL.token_spend runner_1l.py:425-441` | counts over `phase1m/calls.jsonl` only; `RL.token_spend` carries a hard-wired `PHASE_CAP - 667 - n200` estimate (667 = Phase 1k's spend) — stale, 1N should drop or re-base it |
| results | `:710-723` `results_1m.json`, `:726-804` `results_1m.md` | markdown emitters: headline, FA by type (loops `TYPES`, `:737`), FA/FR by layer, targets, the two cells (+ by-form sub-table), §5.1, carried bugs, builder limit, judge noise, shadows, calls |
| `FINAL_RUN_DONE` | refuse `:556-557`, write `:806-809` | `{phase, freeze_commit, coverage, fa, counted_calls}`. 1M's: coverage `547/614 = 89.09% [86.35, 91.44]`, FA `69/646 = 10.68% [8.41, 13.32]`, 1115 counted calls, freeze `22cba45596e4df755eb42bd0b13b063aaddd7610` |
| CLI | `main :813-838` | `--dev / --dry / --final` mutually exclusive; `--f8 {f8,f8v2,f8u} --f9 {on,off} --tip {reject,accept,both}` accepted in `--dev` only |

`--dev` (`:432-507`) replays sides `dev / replay1j / fresh1l` with 0 calls, applies stored judge
labels via `R1K.judge_labels` (`phase1k/runner_1k.py:184-210`, TSV `out_*.tsv` + `key.jsonl`,
`source` filtered first), reports cache misses without calling, and compares against
`DEV_EXP = {'coverage': (182,189), 'fa': (12,301)}` / `REPLAY_EXP = {(178,196), (15,294), T (2,59)}`
(`:49-50`). `fresh1l` needs `PHASE1K_OPEN_FRESH=1` and `RL.HYG = phase1l/hygiene` (`:440-447`).

Pipeline row shape (`phase1i/pipeline_1i.py:130-152 run_pipeline`): per item
`{item_id, kind, judged, wrong_type, half, level, accepted, verdict, layer, model, tip, model_tip,
reached_l3}`; `tip_reject` flips an accepted `model == 'TIP'` to rejected with `layer = 'L3:TIPrej'`.
`locktip_decide` (`runner_1k.py:248-268`) re-decides an L2 lock rejection with the lock satisfied,
sets `lock_tip` + `released_from_lock`, and explicitly does **not** release `it['step']=='mistake'`.

---

## 5. Re-scoring the stored 1M verdicts offline, with 0 model calls

`results_1m.json` does **not** contain a per-item dump. It has only aggregate cells plus id lists
(`metrics.fa_ids` 69, `metrics.fr_ids` 67, `cells[*].accepted_ids`, `lock_released_5_1_fixed
.released_ids` 249, `builder_limit_2_1.ids` 29, `unlabelled_items` 0, `no_verdict_items` 0).
Per-item layer / L3 verdict / TIP flag must be **recomputed**, deterministically and for free:

* the raw L3 verdict lives in `M/calls.jsonl`, one row per attempt, keyed by `req_hash`:
  `{ts, model, variant:"L-1M:main", item_id, req_hash, http:200, counted:true, verdict:"SAME"|"DIFF"|
  "TIP", reply, finish, empty:false, latency_ms, try, prompt_tokens, candidates_tokens,
  thoughts_tokens, cached_tokens, thinking, max_output}`. 1115 counted rows, 0 empty, 0 non-200.
* the layer decision and the TIP flag are *derived*: `res[i]['layer']`, `res[i]['model']`,
  `res[i]['model_tip']`, `res[i]['reached_l3']` out of `run_pipeline` / `apply_guards`.

Recipe (0 calls; `FINAL_RUN_DONE` only blocks `--final`, not a scoring script):

```python
import sys, os; sys.dont_write_bytecode = True
sys.path.insert(0, '<TOFF>/phase1m')
import runner_1m as RM                       # does the whole RL/R1K/f8/f9 wiring, reads no data
RL, R1K, P, C = RM.RL, RM.R1K, RM.P, RM.C
cfg, sel = RM.load_cfg(); RM.select_f8(sel['f8_module'])
st, recs, ann, by, info = RM.build_side_1m('Phase 1N offline re-score of the stored 1M verdicts')
lock_rej, l3 = RL.lock_counts(st, recs)
rep, ver, failed, _ = RL.ledger_state()      # LEDGERS_RO already includes phase1l; phase1m/calls.jsonl is RL.CALLS
hmap = RL.hashes_for(st, recs, l3, sel['prompt'])
vm   = {i: ver[h] for i, h in hmap.items() if h in ver}     # {item_id: 'SAME'|'DIFF'|'TIP'}
guards = R1K.guard_readouts(recs, ann, sel['f9_strict'])
res  = R1K.configure_row(st, recs, vm, True, guards, sel['f8'], sel['f9'], sel['tip_reject'])
labels, controls, lmeta = RM.LM.load_labels('…same purpose…')
m = RL.col_metrics(recs, res, labels)
```

Checks that the replay is faithful: `len(vm) == 1115`, `RL._r(m['coverage']) == '547/614 = 89.09%
[86.35, 91.44]'`, `RL._r(m['fa']) == '69/646 = 10.68% [8.41, 13.32]'`.
Caveats: `build_side_1m` needs `M/data/*.json` (present) and appends access-log lines; re-reading
labels appends more; hashes only match while the prompt text and `GEN_CFG` are untouched (§2.3);
map verdicts by `req_hash`, not by the row's `item_id` (dedupe).

---

## 6. The carried bug counters (all still unpatched in 1M)

1. **`released_by_LOCKTIP_total` is inert.** `runner_1l.py:502-516` counts items where
   `lock_r[i]['accepted'] and not base_res[i]['accepted']` — an accept-flip. On the 1M set it reads
   **0** (`results_1m.json: lock_released_5_1_fixed.old_inert_counter_released_by_LOCKTIP_total = 0`,
   computed at `runner_1m.py:619-623`), because LOCKTIP-released items still fail elsewhere.
   The fix `released_fixed` (`runner_1m.py:377-398`) redefines release as **routing**:
   `set(lock_rej) & set(l3)` → **249** released of 249 L2 lock rejections; 55 accepted, 46 judged
   correct (39 accepted), wrong by type `{"T":165,"V":20,"S":9,"M":6,"W":3}`, accepted
   `{"V":10,"T":5,"M":1}`.
2. **F2B not applied to lock-released items — two disagreeing counters** (1M report §6 names both):
   * `results_1m.json: carried_bugs_counted_not_patched["F2B not applied to lock-released items"]
     .released_items_F2B_never_sees` = **249** (`runner_1m.py:628-632`), proxy "every lock-released
     item is an item F2B never sees". **This is the figure to use.**
   * `results_1m.json: section5_1L_block.unpatched_guard_bugs_5_4["3 F2B not applied to
     lock-released items"]` = `still_fires: false, count 0` (`runner_1l.py:556-558`, `bug3` reuses
     the inert accept-flip definition).
   Root cause: bug 1's definition leaked into bug 3. The 1M report calls the disagreement "itself a
   small reporting bug worth fixing before 1N". **1N fix: give `bug3` the routing definition
   (`set(lock_rej) & set(l3)`), or delete it and reference the `carried_bugs` figure.**
3. **An L2 `step == "mistake"` rejection is not released.** `locktip_decide` skips
   `it['step']=='mistake'` (`runner_1k.py:257`). Counters: `runner_1m.py:626` (`mistake_l2`, excludes
   released ids) and `runner_1l.py:559` (`bug4`, all mistake-step records). Both read **0** on the 1M
   set because `chk_distribution` was `{match 110, auto 1150}` — no record ever got step `mistake`
   (the hand-written annotations carry no `m` mistake patterns, synthetic topic ids). The bug is
   therefore **counted but untested**; 1N will only exercise it if the new annotations carry `m`.
4. **F8 fires only on an English passive main clause** — `bug1` (`runner_1l.py:552-553`) still fires:
   54 items over 39 sids. Not patched.
5. **F9 `REPORTED_STRICT` untested** — `bug2` (`runner_1l.py:554-555`): 0 items change under strict.
6. **The hygiene null was genuine** (1M report §6, `M/HYGIENE_NULL_CHECK.md`, `M/CACHING_CHECK.md`):
   `loader_1k.load_fresh_annotations` has no module memo, the two deep copies share no object, and
   0/600 items change `chk`. On the 1M set hygiene was **not applied at all** (`hygiene.files = []`,
   0 removed / 0 replaced / 0 reference changes; `chk` identical before and after). Mechanism:
   `RL.HYG = <phase dir>/hygiene`; a missing directory means **hygiene silently off**
   (`runner_1l.py:124-133`). 1N must state this explicitly rather than let it default.

---

## 7. Edit plan for `loader_1n.py` / `runner_1n.py`

### 7.1 `phase1n/loader_1n.py` — copy `M/loader_1m.py` and change

| line in `loader_1m.py` | change |
|---|---|
| `:20-23` | `HERE/DATA/JUDGE/LOG` resolve to `phase1n` automatically via `__file__` — **no edit**, but confirm `phase1n/data` and `phase1n/judge` exist |
| `:24` `TYPES = ('T','W','M','S','V','E')` | **drop `'V'`** → `('T','W','M','S','E')` if Phase 1N retires the voice type (see §7.3 for every other place `V` is wired in). Whatever is chosen must be identical in the judge instructions, `load_labels` validation and the metric loops |
| `:25` `SID_LO, SID_HI = 150001, 150140` | new sid range for the 1N set (keep the "max existing sid + >100000" convention; 1M used 150001-150140) |
| `:2-16` docstring | re-point to phase1n and to the 1N file formats |
| `:113` `out_part*.json` glob | keep, unless the 1N judge delivers a different part count |
| `:130-137` | keep the `correct ⇒ type=None`, `wrong with bad type ⇒ rejected_rows` behaviour; a `V` arriving after V is retired must land in `rejected_rows`, not be silently kept |

### 7.2 `phase1n/runner_1n.py` — copy `M/runner_1m.py` and change

| line | change |
|---|---|
| `:2-18` docstring | phase → 1N; state the F8 decision (§3.3) and the prompt decision (§2.2) explicitly |
| `:25-27` | `import loader_1n as LN` instead of `loader_1m as LM`; rename every `LM.` call site (`:61, 122-124, 596`) |
| `:32` `P1L` | add `P1M = os.path.join(TOFF, 'phase1m')` |
| `:36` | `RL.LEDGERS_RO = list(RL.LEDGERS_RO) + [P1L/calls.jsonl, P1M/calls.jsonl]` — otherwise the 1115 1M verdicts are invisible |
| `:37-46` | unchanged in form; `RL.HERE` is **phase1l's copy in phase1n**, so `runner_1l.py` must be copied into `phase1n/` (with `f8.py`, `f9.py`, `loader_1l.py`, and whichever F8 module decides) for `RL.CALLS/HYG/FREEZE_HASH/DONE/STOP_*` to point at phase1n |
| `:47` | `PHASE_CAP_1N = <new cap>`; rename `PHASE_CAP_1M`, `counted_calls_phase1m`, `remaining_under_1m_cap` (`:424-426`, `:527-528`, `:540-541`, `:568-576`, `:589`, `:797-800`) |
| `:49-50` | `DEV_EXP` / `REPLAY_EXP` stay (they are the 1L regression targets and still valid for `--dev`) |
| `:51` | `SIDE_TAG = 'fresh1n'`; verify `R.make_state` accepts the tag, else the `:166-170` fallback logs and uses `'fresh1k'` |
| `:45` | `CFG_PATH = phase1n/FROZEN_CONFIG_1N.json`; `load_cfg :69-70` key list gains whatever 1N freezes (e.g. `f8_decides`) |
| `:73-74` | keep the `locktip` refusal |
| `:86-104 select_f8` | keep; if F8 decides nothing, still call it so the shadow modules are importable and `R1K.f8` is defined |
| `:113-191 build_side_1m` → `build_side_1n` | only the field names change if the 1N data schema changes; keep `make_state` **before** the `compute_chk` loop (`:166-179`) and keep the degenerate-chk abort `:184-190` |
| `:194-204 preflight_1m` | update the reference numbers in the `say` at `:197-198` (add 1M: 249/1115) |
| `:208-240 check_freeze_1m` | `:230` path → `'%s:translation-offline/phase1n/%s'`; write `phase1n/FREEZE_FILES` listing **every** `.py` in the directory (`:216-220` refuses otherwise) |
| `:244-246 plan_1m` | variant tag `'L-1N:%s'` |
| `:258-291 make_calls` | unchanged (6 workers, seed-1 shuffle, streak-5 wall) |
| `:344-363 cell_by_intent` | if intent `V` survives as a **writer intent** (it should — the demotion cell is the headline), keep it even when the judge **type** `V` is retired; the cell selects on `by[i]['intent']`, the type only enters `fa_by_type` |
| `:422-428 spend` | re-base or drop `RL.token_spend`'s hard-wired `- 667` (`runner_1l.py:425-441`) |
| `:604` | headline call: `f8_on=False` if F8 must not decide (§3.3) |
| `:619-626` | fix the F2B counter disagreement (§6.2) before emitting |
| `:639-677 shadows` | add the F8v1 **and** F8v2 shadows side by side (1M only shadowed v1 when v2 was selected) |
| `:726-804 markdown` | `:737` loops `TYPES` — it will emit a `V` row unless `RL.TYPES` is overridden; rename every "Phase 1M" string |
| `:806-809` | `FINAL_RUN_DONE` content → phase 1N |
| `:819` | `--f8` choices to match the modules copied into phase1n |

### 7.3 Retiring judge type `V` — every place it is wired

`loader_1m.py:24` (validation), `phase1k/runner_1k.py:50 TYPES` (= `R1K.TYPES` = `RL.TYPES`,
`runner_1l.py:78`, `runner_1m.py:30`), the `fa_by_type` loop `runner_1l.py:458-460`, the markdown
table `runner_1m.py:737`, `R1K.judge_labels`'s TSV validation `runner_1k.py:207-208` (dev/replay
only), `section5` bug 1 `runner_1l.py:552-553` (selects on **intent** `'V'`, not on the type), and
`cell_by_intent(..., 'V', True)` `runner_1m.py:613-614` (**intent**, keep). Because `RL.col_metrics`
reads the module global, the cheapest correct move is `RL.TYPES = ('T','W','M','S','E')` immediately
after `import runner_1l as RL` in `runner_1n.py`, plus the same tuple in `loader_1n.py:24`; leave
`R1K.TYPES` alone (it only feeds the 1J/1K replay paths in `--dev`).

### 7.4 Files to create in `phase1n/` before `--final`

`data/sentences.json`, `data/annotations.json`, `data/items.json`, `judge/blind_map.json`,
`judge/out_part*.json` (+ `controls_map.json`, `out_controls.json`), `FROZEN_CONFIG_1N.json`,
`FREEZE_FILES`, `FREEZE_HASH`, and copies of `runner_1l.py`, `loader_1l.py`, `f8.py`, `f9.py`,
`f8v2.py` (the executing set of `M/FREEZE_FILES:3-9`). `hygiene/` deliberately absent ⇒ hygiene off,
and say so in the report rather than leaving it implicit.
