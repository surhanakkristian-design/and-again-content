# Phase 1R — Task D1: the 1Q runner crash, fixed; results regenerated from stored verdicts

Date 2026-09-19. **0 new model calls** (hard requirement, proven below).

## 1. The crash

`phase1q/run_final_stdout.log`, attempt 1 (rc=1):

```
File ".../phase1p/runner_1p.py", line 568, in run_final
    json.dump(out, open(os.path.join(HERE, 'results_1p.json'), 'w', encoding='utf-8'), indent=1,
...
TypeError: Object of type set is not JSON serializable
```

**Cause.** Every one of the 1,157 calls had already been made and stored; the run died only while
writing its results. `out['rows']` carries, per row, an F9 readout whose Slovak verdict field is a
**Python `set`** — the regeneration located it exactly at

```
$.rows[*].f9_readout.sk.verdict   e.g. {"future", "present"}
```

`json.dump` has no encoder for `set`, so the writer aborted after ~6 KB, leaving the fragment
`phase1p/results_1p.json` (6,042 bytes) and no `FINAL_RUN_DONE` marker. Verdicts, prompts, layers
and thresholds were never involved.

## 2. The fix (serialisation only)

Frozen file `phase1p/runner_1p.py` (freeze commit `255ef142625a14434f82758ea733cc5cf7c2fe79`),
edited post-run. Diff, in full:

```diff
+def _json_default(o):
+    """Phase 1R serialisation fix (results writing only; no verdict logic touched):
+    sets/frozensets are written as sorted lists, every other unsupported type still raises."""
+    if isinstance(o, (set, frozenset)):
+        return sorted(o)
+    raise TypeError('Object of type %s is not JSON serializable' % o.__class__.__name__)
+
+
 def run_final(a):
     if os.path.exists(DONE):
@@
     json.dump(out, open(os.path.join(HERE, 'results_1p.json'), 'w', encoding='utf-8'), indent=1,
-              ensure_ascii=False)
+              ensure_ascii=False, default=_json_default)
```

Nothing else changed: no lever, prompt, layer, threshold, cap or label path. Unknown types still
raise, so the fix cannot silently swallow a different serialisation bug.

**sha256 of `phase1p/runner_1p.py`**

| | sha256 |
|---|---|
| before (as it ran in 1Q) | `d444891a210ff98947aa12affdd58fb96433641f3a25c6375f570363c058e28f` |
| after (Phase 1R) | `b82562d57e8e15aa8c77585e2a80a9c3025466a859986592809a1d3ad00ee1da` |

Consequence: `check_freeze()` would now refuse, because the file no longer hashes to the freeze
commit. That is expected and post-run; the freeze hash is still recorded inside the results.

## 3. Regeneration from the STORED verdicts

`phase1r/taskD/regenerate_results.py` imports the (fixed) runner and calls its own `run_final`,
i.e. the runner's own assembling functions — `preflight` → `lever1_side` → `decide` → `score` →
`cells`. Two guards make a model call impossible:

1. every `*GEMINI*` / `*GOOGLE*` / `*API_KEY*` env var is popped before the runner is imported, and
   the process was additionally started under `env -u GEMINI_API_KEY -u GOOGLE_API_KEY …`;
2. `runner_1n.make_calls` — the single place an HTTP request is issued — is replaced by a raiser,
   so a non-empty `need` list would **abort** the regeneration instead of calling the model.

`check_freeze` is stubbed (it would refuse over the serialisation fix); the freeze hash is read
from `phase1p/FREEZE_HASH` and written into the results unchanged.

Runner output during the regeneration:

```
[PREFLIGHT] unique requests 925   reusable 925   PLANNED NEW CALLS 0   counted so far 1382
[FINAL] lever 1: 239 rewritten records, 239 L3-eligible, 0 NEW calls
```

### Zero-call proof

| | lines | sha256 of `phase1p/calls.jsonl` |
|---|---|---|
| before | 1384 | `e08b2c3bfff6e860dfd15850e1979ec253244cd90bf925c91ef65273b989f436` |
| after | 1384 | `e08b2c3bfff6e860dfd15850e1979ec253244cd90bf925c91ef65273b989f436` |

Byte-identical; the raiser was never triggered. Raw record in `regenerate_check.json`.

`phase1p/results_1p.json` is now complete (1,879,443 bytes, 1,080 rows). The broken fragment is
kept as **`phase1p/results_1p.fragment.json`** (6,042 bytes), not deleted. `results_1p.md` was
written by the runner as part of the same path.

## 4. Headline vs. the 1Q offline replay

| | regenerated `results_1p.json` | `phase1q/RESULTS_1Q.json` replay | match |
|---|---|---|---|
| coverage | 436/599 = 72.79 % | 436/599 = 72.79 % | yes |
| false accepts | 8/481 = 1.66 % | 8/481 = 1.66 % | yes |
| items / rows | 1,080 / 1,080 | 1,080 | yes |

**Exact match.** (The `[MATCH]` line in the script log shows `coverage_kn`/`fa_kn` as `false` only
because the runner stores `[436, 599]` as a list and the replay file stores `"436/599"` as a
string — same numbers, different type. The percentages, which are compared as values, match.)

## 5. Marker

`phase1p/FINAL_RUN_DONE` (the path `run_final`/`run_final_1q.sh` both look for) now exists and
says honestly: written in Phase 1R on 2026-09-19 after an offline regeneration; all 1,157 calls
were made in the 1Q run (1,382 counted incl. dev); 0 new calls in 1R; original RUN commit
`d7505d0a8b36b20384bff8ce289bea1579e0b456`; freeze commit `255ef142…`.

Note: with the marker present, `--final` now refuses (measured once) and `--ablation` is unblocked.

---

# Task D2 — what a proper lever ablation would cost (no run, arithmetic only)

## Assumptions (stated, not hidden)

* **Design**: leave-one-out over the full final set — three arms, each with one lever off and the
  other two on, on the same 1,080 items / 120 sentences. (The *pre-declared* 1Q ablation in
  `PREDECLARED_1Q.md` §"Ablation" is something else: all levers off, leftover calls only, cap−10.)
* A call is needed per **unique request hash**; the hash covers the prompt text, so any lever that
  changes the prompt for an item invalidates the cache for that item.
* Reference point from the 1Q run: main set **925** unique requests (L3-eligible under LOCKTIP),
  lever-1 side set **232** new (239 rewritten records) → **1,157** calls, all cached.
* Lever firing counts from the build line: `l2:definiteness 1000`, `l2:aspect 828`, `l2:number 207`
  (union ≈ all 1,080); `l3:items_with_a_variant 1026` of 1,080 (≈ 95 %); `l1:fired 239`.

## Arm A — lever 1 OFF (levers 2, 3 on)

Lever 1 does not touch the main prompt; it only *adds* the rewritten side set. So the 925 main
requests keep their hashes → **925 cached, 0 new**, and the 232 side calls simply do not happen.

**New calls: 0.**

## Arm B — lever 2 OFF (levers 1, 3 on)

The per-item lever-2 lines are removed from the prompt, so nearly every hash changes. At most
1,080 − 1,000 = **80** items carry no definiteness line, and some of those still carry an
aspect/number line, so realistically ≈ 40–80 requests stay cached. The eligible set also grows:
272 L2 lock firings under BASE no longer pre-reject, so up to ~155 extra items reach a call
(925 → at most 1,080).

Main ≈ 925–1,080 new (minus ~40–80 cached) ≈ **870–1,040**; lever-1 side ≈ **232**.

**New calls ≈ 1,100–1,270** (point estimate **≈ 1,160**).

## Arm C — lever 3 OFF (levers 1, 2 on)

The "Also accepted English" line disappears for the 1,026 items that had a variant (95 %); the
~54 without one keep their hash. Removing lever 3 does not change L3 *eligibility* (that is the
LOCKTIP gate), so the request counts stay 925 + 232.

Main ≈ 925 × 0.95 ≈ **879** new (≈ 46 cached); side ≈ 232 × 0.95 ≈ **220** new (≈ 12 cached).

**New calls ≈ 1,099.**

## Total

| arm | nominal requests | already in cache | NEW calls |
|---|---|---|---|
| A (L1 off) | 925 | 925 | **0** |
| B (L2 off) | ~1,157–1,312 | ~40–80 | **~1,100–1,270** |
| C (L3 off) | 1,157 | ~58 | **~1,099** |
| **total** | **~3,239–3,394** | **~1,023–1,063** | **≈ 2,200–2,370** (point **≈ 2,260**) |

So the cache pays for roughly **1,030 of ~3,300** requests (≈ 31 %), essentially all of it arm A.

## Cost at gemini-3.1-flash-lite

From `calls.jsonl` (1,384 rows, all variant `L-1P`): mean **396.6 prompt tokens** per call,
**1.0 output token** per call (`max_output: 24`, thinkingBudget 0, verdict is a single word).

* input ≈ 2,260 × 397 ≈ **0.90 M tokens**; output ≈ 2,260 × 1 ≈ **2.3 k tokens**.
* At the Flash-Lite tier assumed here — $0.10 / 1 M input, $0.40 / 1 M output (no separate public
  price sheet for "3.1-flash-lite" was available offline; substitute the real rate if it differs) —
  input ≈ **$0.090**, output ≈ **$0.001**.

**≈ $0.09, i.e. under ten cents** for the whole three-arm ablation. Money is not the constraint;
the **call cap is**: 1,382 of the 1,400-call phase cap are spent, leaving **18** (and the
pre-declared ablation floor is cap−10 = 1,390, i.e. **8 usable calls**). A proper leave-one-out
ablation therefore needs a new, explicitly granted budget of ≈ 2,300 calls — it cannot be squeezed
out of the 1P leftovers.
