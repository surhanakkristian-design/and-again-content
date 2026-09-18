# Task B — the L2 over-firing: fix and DEV measurement (18 Sept 2026)

Diagnosis with counts and ids: `taskB/DIAGNOSIS.md`. Machine-readable result: `taskB/results.json`.
Model ledger: `taskB/calls.jsonl` (4 rows). DEV only; the holdout was never opened.

## Deliverables and the exact call the integrating agent makes

```python
import sys; sys.path.insert(0, '<phase1i>'); sys.path.insert(0, '<phase1i>/taskB')
import checker_1i as C
import backfill_s_ids as B, lock_fix

B.apply_to_checker(C)                       # -> report dict; mutates C._ANN in place, 0 model tokens
lock_fix.apply(C, syn=True, gender=True, contraction=True)   # -> {'syn':…, 'releases': {item_id: trace}}
lock_fix.revert(C)                          # undo
```
* `lock_fix.apply(checker_module, syn=True, gender=True, contraction=True)` wraps `f1_lock_ok`,
  `lock_equivalent_ok` and `_has` on the module handed to it. Import is side-effect free (stdlib only).
  `checker_1i.py` is **not** edited.
* `backfill_s_ids.apply_to_checker(checker_module, annotations=None)` /
  `backfill_s_ids.backfill_annotations(annotations, checker_module) -> (new_ann, report)` /
  `python3 backfill_s_ids.py <side>`. It takes the loader's annotation dict (`{"<sid>": {"hygienised":…}}`
  or plain `{"<sid>": ann}`), works per sentence, and is byte-identical for dev and holdout.
* `run_measure.py` reproduces everything (`TASKB_CALLS=1` to call the model; cached from the ledger otherwise).

**The fix, three independently switchable parts**
1. `syn` — the locked span may be satisfied by an existing synonym-group member, reached by phrase
   (`syn_equivalents`), by the annotation's `s` id (after the backfill) **or** by its `alt`.
   Hard guard: the equivalent must have the **identical grammatical signature** as the lock
   (`parse_lock` kind, aux chain, verb form, `needs_to`); for `literal` spans the old §2.1 rule
   (preposition/linker only) still applies. A tense, aspect or voice change can never release the lock.
2. `gender` — the lock is expanded over the annotation's own `g` chain with the very function hygiene uses
   for the references (`reference_hygiene.gender_variants`).
3. `contraction` — `_has` matches a phrase token against every alternative of an `expand()` ambiguity token.

## Apparatus check

Replaying the frozen row-7 verdict map through `C.decide` reproduces the stored `rows.row7` for **467/467**
DEV items (layer, accepted, verdict): 0 mismatches. Baseline type-T false acceptance is 1/67 = **1.5 %**,
the number the task names.

## What the fix does on DEV

4 items leave L2 for L3 (`syn` 0, `gender` 3, `contraction` 1):

| item | kind / judged / type | released by | model | final |
|---|---|---|---|---|
| `C:29691:1286045143` | C / correct | gender (`his`→`her`) | DIFF | rejected at L3 |
| `C:29691:2714964500` | C / correct | gender (`his`→`her`) | DIFF | rejected at L3 |
| `C:5959:1661102304` | C / correct | contraction (`will`→`is going to`, with tip) | DIFF | rejected at L3 |
| `W:29691:3644752565` | W / wrong / S | gender (`his`→`her`) | DIFF | rejected at L3 |

**Every DEV WRONG answer whose lock outcome changes: exactly one**, `W:29691:3644752565` (type S,
*"He'll drop her guide…"*). It is released from L2 to L3 and the model rejects it — not accepted under
either scoring. No type-T wrong answer changes outcome at all, by construction (part 1's signature guard,
and parts 2-3 only swap a pronoun / read a contraction).

### Coverage and false acceptance, DEV, exact 95 % Clopper-Pearson

| scoring | metric | before | after |
|---|---|---|---|
| TIP = accept (1h baseline) | coverage | 160/203 = 78.8 % [72.55–84.23] | 160/203 = 78.8 % [72.55–84.23] |
| TIP = accept | false acceptance | 30/260 = 11.5 % [7.92–16.06] | 30/260 = 11.5 % [7.92–16.06] |
| TIP = reject (Task A switch) | coverage | 145/203 = 71.4 % [64.68–77.53] | 145/203 = 71.4 % [64.68–77.53] |
| TIP = reject | false acceptance | 8/260 = 3.1 % [1.34–5.97] | 8/260 = 3.1 % [1.34–5.97] |

False acceptance by wrong type, unchanged under both scorings — TIP = accept T 1/67 (**1.5 %**), W 10/69,
M 10/56, S 9/68; TIP = reject T 0/67, W 1/69, M 3/56, S 4/68.

**Recovered correct answers: none. Newly accepted wrong answers: none.** The fix is additive to the Task A
switch (it touches only items L2 rejected; it never converts a rejection into an acceptance by itself) and
it costs nothing, but on DEV it buys nothing either: all three correct answers it hands to L3 are called
DIFF by `gemini-3.1-flash-lite`. L2's over-firing on those three is masked by an L3 error of the same sign.

## Model calls

4 calls, frozen P-B prompt, `gemini-3.1-flash-lite`, thinking off, `maxOutputTokens` 24 — all HTTP 200,
all parsed, **0 failed**, 0 retries; 621 prompt / 4 output tokens, latency 703-1012 ms. Budget 150, used 4.
One apparatus bug of mine is worth recording: `lib_prev.parse_verdict` returns a *tuple*
`(verdict, text, usage, finish)`, and my first reader compared the tuple against `'SAME'|'TIP'|'DIFF'` and
booked all four replies as failed calls. The replies were fine (`DIFF` ×4); the reader was wrong. The four
ledger rows were rewritten in place so `verdict` holds the documented string, `reply` the raw text.
No key was printed, logged or passed on a command line.

## For the holdout run (Task F)

All three parts are general rules (annotation `g`, `expand()` tokens, existing synonym tables) — no
per-sentence list, no hand-edited annotation — so they are measurable on the holdout despite the leakage
caveat. G1 (sid 103) is a data defect that is *not* fixed here and, being per-sentence, could not be
measured there anyway. Expect the holdout effect to be of the same size as here: a handful of releases,
each of which then depends on L3.
