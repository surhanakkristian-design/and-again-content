# Task D — the D3 "empty reply" failure (Phase 1i, DEV only)

**Verdict: cause FOUND, and it is not the prompt.** The 311 "empty replies" of Phase 1h row 8 were never
replies. They were **client-side transport failures** — `URLError: <urlopen error [Errno 61] Connection
refused>` — that `lib_prev.call_model` recorded as `counted: true, verdict: "PARSE_FAIL", reply: ""`.
P-C was not a fragile prompt shape; it was the variant that happened to be running when the local egress
path stopped accepting connections in the last 7.6 s of the run.

Files: `phase1i/taskD/run_d.py` (re-runnable; `--calls` makes the model calls), `taskD/calls.jsonl`
(30 counted calls, full raw response JSON per call), `taskD/timeline.json`, `taskD/conditions.json`.

---

## 1 Ledger evidence (0 model calls) — `phase1h/calls.jsonl`, 1246 rows

| field | P-C "empty" (n=311) | P-C real replies (n=312) | P-B "empty" (n=1) | P-B real replies (n=622) |
|---|---|---|---|---|
| `http` | **0** (312/312) | 200 | **0** | 200 |
| `raw` | `URLError: <urlopen error [Errno 61] Connection refused>` — **identical string in all 312** | — | same string | — |
| `finish` (finishReason) | `null` — no candidate ever arrived | `STOP` 312/312 | `null` | `STOP` 622/622 |
| `prompt_tokens` / `candidates_tokens` / `thoughts_tokens` / `cached_tokens` | `null` in **all 311** (no `usageMetadata`, no response body at all) | 181 median / 1 / null / null | null | 1 candidate token |
| `empty_due_to_thinking` | false | false | false | false |
| `latency_ms` | min 126, **median 143**, max 217 | median 794, deciles 708–1003 | 140 | median ~768 |
| `max_output` | 24 | 24 | 24 | 24 |
| `counted` | **true** (the harness charged them as failed model calls) | true | true | true |

There is **no blockReason, promptFeedback or safety field anywhere in the ledger** — not because they were
dropped, but because no HTTP response body exists for these rows. Across the whole 1h run, **every one of
the 934 HTTP-200 rows returned `finishReason STOP` and a parsable verdict: Phase 1h contains zero genuine
empty model replies.** The ~140 ms latency is a refused TCP connect, not a model turn.

### Timeline (`taskD/timeline.json`)

| quantity | value |
|---|---|
| first `http 0` | ts 1789748451.23 |
| rows before it | 925, of which `http 0`: **0** |
| rows from it to the end of the run | 321, of which `http 0`: **312** (9 survivors, interleaved) |
| length of the failure window | **7.6 s** (run ends 1789748458.85) |
| P-B call window | 1789748336.3 – 1789748458.85, last **success** 1789748417.7 |
| P-C call window | 1789748415.2 – 1789748458.85, last success 1789748458.16 |

P-B had essentially finished before the window opened; the single P-B call still in flight inside the window
also failed (1 of 1 = 100 %). P-C had 320 of its 623 calls inside the window and lost 311 of them (97 %).
The 311-vs-1 split is **exposure, not prompt shape**. Median inter-call gap in the P-C block was 31 ms and
9 successes are interleaved among the failures, so this was a burst-refusal (connection/rate limiting on the
local egress path, e.g. a proxy or ephemeral-port/connection ceiling), not a clean network outage.

### A second, worse consequence nobody has recorded yet

Of the **144 DEV items** that came back "empty" under P-C, **144 are kind `W` and 0 are kind `C`**. The
outage hit a contiguous, kind-ordered tail of the queue, so the missing verdicts are *systematically the
wrong-answer items*. An item with no verdict is not accepted, so a missing wrong-answer verdict can never be
a false acceptance: row 8's flattering **1.5 % FA is a selection artefact with a direction**, not merely a
noisy number. Confirms and sharpens 1h §5 D3 — row 8 must not be quoted at all.

### The code-level defect

`lib_prev.http()` (:168) returns status `0` on any exception; `lib_prev.call_model()` (:268) retries only
`st == 429 or st >= 500`. Status `0` falls straight through to the success path, where `parse_verdict(None)`
yields `PARSE_FAIL` and the row is written with `counted: true`. **A dead socket is therefore indistinguishable
from a model that refused to answer.** That single missing branch produced the whole of D3.

---

## 2 Prompt experiment (30 counted calls, hard cap enforced in `run_d.py`)

5 DEV items that returned "empty" under P-C in 1h (`W:10013:1594646351`, `W:10043:2003262413`,
`W:10107:1842941281`, `W:10107:2605305070`, `W:10116:603568525`), one variable changed at a time,
`gemini-3.1-flash-lite`, temperature 0, `thinkingConfig {thinkingBudget: 0}`.

| condition | what changed vs P-B | n | **empty** | finishReason | prompt tokens | verdicts |
|---|---|---|---|---|---|---|
| `B` | P-B baseline | 5 | **0** | STOP ×5 | 139–154 | SAME 1 / DIFF 4 |
| `C` | P-C: `PC_LINE` inserted before the question (the blamed shape) | 5 | **0** | STOP ×5 | 174–189 | SAME 2 / DIFF 3 |
| `C_end` | same line, **after** the question (block ordering) | 5 | **0** | STOP ×5 | 174–189 | SAME 2 / DIFF 3 |
| `B_pad` | neutral padding of the same length instead of `PC_LINE` (length only) | 5 | **0** | STOP ×5 | 174–189 | SAME 1 / DIFF 4 |
| `C_noSK` | P-C with the **Slovak line removed** | 5 | **0** | STOP ×5 | 155–162 | DIFF 5 |
| `C_mo8` | P-C with `maxOutputTokens` 8 instead of 24 | 5 | **0** | STOP ×5 | 174–189 | SAME 2 / DIFF 3 |

**30/30 counted calls returned a non-empty, one-word reply with `finishReason STOP`. 0 empty. 0 transport
retries were needed** (`_transport_retries_not_counted: 0`). Ruled out as causes: the extra P-C line itself,
its position, prompt length (`PC_LINE` costs ~35 prompt tokens; the padded P-B is the same length and is
fine), the presence/absence of the Slovak line, `maxOutputTokens`, and thinking (it was off in 1h, and
`empty_due_to_thinking` is false in every row). No `promptFeedback`/`blockReason` appeared in any of the 30
raw response bodies, so safety blocking is ruled out too.

Side note for the prompt-variant agent: `C_noSK` flipped both of the `C`-SAME items to DIFF. Dropping the
Slovak makes the model strictly reference-matching. That is a *behaviour* finding on n=5 and nothing more —
it is not power to decide anything.

---

## 3 Rules that follow

### For the prompt authors (P-E1 / P-E2 / P-E3)

1. **A prompt must not be blamed, dropped or redesigned on the basis of empty replies whose ledger row has
   `http != 200`.** Those rows carry no model evidence at all. Judge a prompt only on HTTP-200 rows.
2. **A prompt may keep the P-C "Slovak is the ground truth" line.** It is not what broke row 8. If you want
   P-C's idea, take it; just re-measure it on a clean run.
3. **A prompt must stay inside the frozen call shape** that is demonstrably stable: system instruction =
   `lib_prev.SYS`, one user part, `temperature 0`, `maxOutputTokens 24`, `thinkingConfig {thinkingBudget: 0}`,
   one-word answer, no `responseMimeType`, no stop sequences, no JSON schema. Every variation tested here
   inside that shape answered 5/5; nothing here licenses leaving it.
4. **A prompt must not grow open-ended output.** `maxOutputTokens 24` with a one-word answer never hit
   `MAX_TOKENS` in 964 HTTP-200 calls (1h 934 + Task D 30). A variant that asks for a sentence would put
   `finishReason MAX_TOKENS` into play and *that* would be a real empty/truncated-reply risk — if any P-E
   variant asks for more than one word, raise `maxOutputTokens` with it and re-check `finishReason`.
5. **Compare variants on the same items in the same run, interleaved.** In 1h the variants were run in
   blocks, so an infrastructure event hit one variant and one kind of item only. Interleave `(item, variant)`
   pairs and shuffle, so any future outage damages all variants equally and stays visible as noise.

### For the run script (how to detect an empty reply and count it)

```python
counted = (st == 200)            # ONLY a 200 is a reply at all
if not counted:                  # 0 (transport), 429, 5xx  ->  back off, retry, do NOT count
    ...
cands = (js or {}).get('candidates') or []
txt = ''.join(p.get('text','') or '' for c in cands
              for p in ((c.get('content') or {}).get('parts') or []))
empty = (not cands) or txt.strip() == ''
finish = cands[0].get('finishReason') if cands else None
```

- `empty_reply` is **only** meaningful when `http == 200`. Record it as its own boolean; never infer it from
  `reply == ''`, which is exactly the conflation that produced D3.
- Retry `http in (0, 429)` **and** `http >= 500` — status `0` must be in that set — with exponential backoff,
  max 5 tries, each attempt written to the ledger with `counted: false` and the redacted error text. These do
  not consume the call budget and are not failed model calls.
- A genuine empty reply (`http 200` + `empty`) or an unparsable one is a **failed call**: counted, logged with
  its `finishReason`, `promptFeedback` and `usageMetadata`, never retried, never guessed; the item gets no
  verdict and is not accepted. That frozen rule is right — it was just being fed the wrong input.
- After every run, **assert** `sum(http != 200 and final_try) == 0` (or at minimum print the per-status
  histogram) before quoting any coverage/FA number. A row-8-style result must be refused automatically when
  more than ~1 % of its calls never reached HTTP 200.
- Also assert the kind/variant balance of the missing verdicts: if the items without a verdict are skewed to
  `C` or to `W`, the run's coverage and FA numbers are biased in a known direction and must be discarded.

Everything above was measured on DEV items and on prompt-independent ledger aggregates only; the holdout was
not read.
