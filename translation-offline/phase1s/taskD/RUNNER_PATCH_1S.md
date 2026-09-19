# Phase 1S — Task D2: the exact patch a future run must apply to `phase1p/runner_1p.py`

Nothing was run and the frozen runner was **not modified** by this task. This file is the diff a
future run applies, plus the audit that motivates it.

## 0. Identity of the file this patch applies to

| file | sha256 (today, 2026-09-19, i.e. *after* the 1R serialisation fix) |
|---|---|
| `phase1p/runner_1p.py` | `b82562d57e8e15aa8c77585e2a80a9c3025466a859986592809a1d3ad00ee1da` |

(1R records the pre-fix hash as `d444891a210ff98947aa12affdd58fb96433641f3a25c6375f570363c058e28f`;
the freeze commit is `255ef142625a14434f82758ea733cc5cf7c2fe79` and `check_freeze()` already refuses
against it — that refusal is pre-existing and not caused by this patch.)

`phase1q/rows_1q.json` sha256 `eefa93fb8297d3140f9892b8bbbead0b69fd1d5c47a440441f77250241934dcb` (read-only input to D1).

## 1. Audit of every write site in the run path

`runner_1p.py` — 14 sites. "safe default" = an encoder for exotic types; "atomic" = tmp+fsync+replace.

| line | writes | safe default | atomic | a crash here costs |
|---|---|---|---|---|
| 62-64 `say()` | `run_1p.log`, append+close per line | n/a (str) | no (append) | nothing; the line is on disk at close |
| 189 | `STOP_CHK` degenerate-chk marker | no | no | nothing (pre-call) |
| 260 | `STOP_PLAN` cap marker | no | no | nothing (pre-call) |
| 390 | `STOP_PRE` preflight marker | no | no | nothing (pre-call) |
| 406 | `STOP_PLAN` threshold marker | no | no | nothing (pre-call) |
| 441 | `selftest/dry_run_1p.json` (rows incl. `f9_readout`) | **no** | no | the dry run only, but it is the SAME set-in-`f9_readout` bug — a dry run would have caught 1Q |
| 480/482/484 | selftest fixtures sentences/annotations/items | no | no | nothing |
| 515 | `SystemExit` message | n/a | n/a | nothing |
| 539 | `PAUSED` quota-wall note | no | no | the resume note; verdicts survive in `calls.jsonl` |
| **576** | **`results_1p.json`** | **yes (1R `_json_default`)** | **no — `open(...,'w')` truncates first** | **the whole result file → this is the 1Q fragment** |
| 581-585 | `results_1p.md` | no | no | **the DONE marker: it is written after this** |
| **586** | **`FINAL_RUN_DONE`** | no | no | **written last, on the happy path only, no try/finally → any earlier failure makes a paid-for run look unfinished** |
| 635 | `ablation_1p.json` | no | no | the ablation result |
| 784 | `dev/dev_lever%d.json` | **no** | no | a dev lever sweep (225 calls were spent on dev) |

Called modules: `lever1.py`, `lever2.py`, `lever3.py` contain **no** write site (pure computation).
`loader_1p.py:33` appends `access_log.jsonl` (str/int only, append+close — safe).
Outside the run path but same defect class: `assemble_1p.py:151,162`, `normalise_1p.py:40`,
`floor_check_1p.py:69,71,110,112,132-135`, `build_B.py:16,135-137` — no default, not atomic.
`phase1n/runner_1n.py` (imported as `R1N`, it owns the call/verdict store) repeats the pattern at
lines 261, 274, 374, 723, 841, 960, 1042, 1090, 1120 and **1144 (`DONE` written last)**; it was
grepped, not read line by line — outside the stated read scope for this task.

**Conclusion.** The 1Q crash was not one bad `json.dump`; it was a *class*: (i) no encoder for
exotic values, (ii) no encoder for exotic dict *keys* (a `default=` handler never sees keys — the
1S self-test proves the stdlib still raises `TypeError: keys must be str…`), (iii) destructive
non-atomic writes that truncate the previous file before the new bytes exist, and (iv) a DONE
marker that is the last statement of the happy path instead of a `finally`.

## 2. The patch

Apply verbatim to `phase1p/runner_1p.py`. `phase1s/safe_json.py` must be importable
(24/24 self-test checks pass, run 2026-09-19).

```diff
@@ imports (top of file, after line 15)
 import argparse, collections, json, os, random, subprocess, sys
+sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'phase1s'))
+from safe_json import safe_dump, write_done_marker, guarded_run   # noqa: E402

@@ -519,527 (the 1R shim) — keep it for reference but stop using it
-def _json_default(o):
-    if isinstance(o, (set, frozenset)):
-        return sorted(o)
-    raise TypeError('Object of type %s is not JSON serializable' % o.__class__.__name__)
+# superseded by phase1s/safe_json.json_default (handles keys, tuples, objects, NaN, cycles)

@@ line 441  --dry-run
-    json.dump(out, open(os.path.join(HERE, 'selftest', 'dry_run_1p.json'), 'w', encoding='utf-8'),
-              indent=1, ensure_ascii=False)
+    safe_dump(out, os.path.join(HERE, 'selftest', 'dry_run_1p.json'))

@@ line 576  --final results
-    json.dump(out, open(os.path.join(HERE, 'results_1p.json'), 'w', encoding='utf-8'), indent=1,
-              ensure_ascii=False, default=_json_default)
+    safe_dump(out, os.path.join(HERE, 'results_1p.json'))

@@ line 586  the marker
-    open(DONE, 'w', encoding='utf-8').write(json.dumps(
-        {'phase': '1P', 'freeze_commit': fh, 'coverage': met['coverage_kn'], 'fa': met['fa_kn'],
-         'counted_calls': counted_local()}, indent=1) + '\n')
+    write_done_marker(DONE, meta={'phase': '1P', 'freeze_commit': fh,
+                                  'coverage': met['coverage_kn'], 'fa': met['fa_kn'],
+                                  'counted_calls': counted_local()})

@@ line 635  ablation
-    json.dump(out, open(os.path.join(HERE, 'ablation_1p.json'), 'w', encoding='utf-8'), indent=1,
-              ensure_ascii=False)
+    safe_dump(out, os.path.join(HERE, 'ablation_1p.json'))

@@ line 784  dev sweep
-    json.dump(out, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
+    safe_dump(out, p)

@@ main() — wrap the paid-for entry points so a marker ALWAYS exists
-    if a.final:
-        run_final(a)
+    if a.final:
+        guarded_run(lambda: run_final(a), DONE + '.attempt',
+                    meta_fn=lambda r: {'rows': len(r['rows'])} if r else None)
```

Notes a future run must respect.

1. `run_final` refuses when `DONE` exists, so `guarded_run` writes its own
   `FINAL_RUN_DONE.attempt` marker; `run_final` still writes the real `DONE` on success. After a
   crash the `.attempt` file holds status `CRASHED` + the traceback and proves the calls were made.
2. `safe_dump` serialises to a string **before** touching the target, so a residual encoding
   problem leaves the previous complete file in place instead of a 6 KB fragment.
3. The five STOP/PAUSED markers (189, 260, 390, 406, 539) may also be switched to `safe_dump`;
   they carry only str/int today, so this is hygiene, not a fix.
4. Nothing in this patch touches a lever, the prompt, a layer, a threshold, the cap or the label
   path. It is serialisation and process bookkeeping only. Applying it changes the file hash again;
   record the new sha256 next to the run.
