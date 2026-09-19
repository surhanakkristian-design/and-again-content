# Phase 1P — DEV readout (design on CLOSED sets only, 225 counted calls)

The new 1P set was never read: `phase1p/data/` and `phase1p/judge/` were empty for the whole of
this work (the only files this agent ever put there were a synthetic self-test fixture, now moved
to `selftest/fx/`).  Everything below is measured on the CLOSED `fresh1n` side, which is fair for
design and never for a headline.

## 0. The measuring apparatus was checked first

`runner_1p.py --dev` rebuilds the 1N side through `loader_1p` (logging into `phase1p/`, never into
`phase1n/`), computes `chk` with `runner_1l.compute_chk` (never asserts it), and re-scores the
frozen stack under prompt `P-FROZEN-1N` with **0 new calls** — all 834 L3 verdicts are reused from
`phase1n/calls.jsonl` by request hash.  It reproduces the 1N headline **exactly**:

    coverage [350, 426]   FA [14, 474]      (1N: 350/426 = 82.16 %, 14/474 = 2.95 %)

and the run **asserts** it (`APPARATUS: the 1N baseline is not reproduced`).  Every lever number
below is a delta against that identical baseline, so an apparatus drift cannot be read as a gain.

## 1. How many references did the model see before?  **Exactly ONE.**

Confirmed in code, not by inference: `runner_1k.build_req` (the only request builder, wrapped by
`runner_1n.build_req_1n` and now by `runner_1p.build_req_1p`) assembles
`pipeline_1i.pb_lines(st, it)` = `checker_1i.prompt(it, 'P-B')`, which interpolates
**`it['reference']`** and nothing else, and then appends only the gender line (when the annotation
has `g`), `GROUND_LINE` and `WORDING_LINE`.  `pipeline_1i.ALT_TMPL` / `alt_refs()` exist but are
reachable only from the retired probe variant `P-E4a`, which no frozen prompt uses.  Lever 3 is
therefore live, and it is the first time the model is shown more than one rendering.
(Side note found on the way: on all 100 1N sentences the annotation carries **no `g` key at all**,
so the gender line fired 0 times — lever 2's insertion point was exercised with no competing line.)

## 2. Per lever, separately.  No row combines levers.

### Lever 1 — agentless passive accepted WITH A TIP (deterministic rewrite)

`lever1.detect()` fires when the ANSWER is an English be-passive with no `by` anywhere after the
participle **and** the annotation says the Slovak is active with an explicit nominative agent
(`voice_sk == 'active_agent'` / `agent_nom`).  It then inserts `by <agent>` directly after the
participle, the agent being the subject NP of the main reference in the object case, and the
REWRITTEN answer goes through the normal stack with F4v2/F4 suppressed for that record only (the
F4v2 fix: in a passive the answer's subject is the patient, so the guard's premise is false).

| | |
|---|---|
| detector fires on the 1N side | **35 / 900** answers |
| of those judged correct / judged wrong | 26 / **9** (the honest exposure count; the writers tagged **0** judged-wrong answers agentless, so all 9 come from the detector) |
| writer `agentless` tag | 22 items, the detector reads **21** of them as an agentless passive (1 miss: no by-agentless be-passive pattern) |
| already accepted by the frozen stack (shadow, unrewritten) | 10 of the 26 |
| **GAIN** (judged correct, baseline REJECTS, lever 1 accepts) | **5** |
| **FA COST** (judged wrong, baseline rejects, lever 1 accepts) | **0 / 9** |
| calls | 33 |

So on this side lever 1 converts 5 of the ~21 false rejections it targets and costs nothing on the
9 judged-wrong answers it touches.  The 2 items the 1N run lost at F4v2 are in the fired set and the
suppression removes that stop; they do not all convert, because the rewritten answer still has to
survive L3.  Gain and cost are separable on the new set because the runner stores
`lever1.shadow_unrewritten_accept` / `shadow_unrewritten_layer` per item.

### Lever 2 — "the Slovak does not fix X"

Three script-built lines (definiteness, aspect inside the named frame, number on mass/collective
nouns), inserted exactly where the gender chain is inserted.  On the 1N side they fire
**definiteness 874 / aspect 720 / number 81** of 900 items.  The aspect line names the frame and
says a different frame is DIFF, and it never fires on a Slovak perfective present.

| | |
|---|---|
| gain set: non-agentless false rejections decided at L3 / L3:TIPrej | 41 |
| **GAIN** | **12 / 41** |
| FA set: 55 judged-wrong (38 time-frame, 17 other), seeded | 55 |
| **FA COST** | **0 / 55**, of which time-frame **0** |
| calls | 96 |

### Lever 3 — stored reference variants with a mandatory tense filter

Up to 2 further stored renderings (`v[1:]`), equally ranked, any variant whose time frame differs
from the main reference's removed by `lever3.time_frame()`.

| | |
|---|---|
| variants shown over the 900 1N items | **1170** (891 items get at least one) |
| **variants REMOVED by the tense filter** | **63** |
| gain set (same 41 items) | 41 |
| **GAIN** | **11 / 41** |
| **FA COST** | **1 / 55**, of which time-frame **1** |
| calls | 96 |

Lever 3 is the only lever with a measured FA cost on this side: one time-frame item. It is inside
the noise of a 55-item sample, but it is reported as it stands and it is the reason the runner
records `variants_shown` / `variants_removed` per item, so the new set can price it again.

## 3. What was NOT done

* **No lever was measured in combination with another**, by instruction; the interaction of 2 and 3
  (both add prompt lines) is unknown, and the final run uses all three at once.
* The FA samples were **cut to 55 per lever** (suggested ~70) and the lever-1 exposure cap to 40, to
  stay inside the 300-call dev budget. 225 of 300 were used; the rest is left for the final run.
* Nothing was measured on a fresh set. Every number here is a closed-set design number.
* `assemble_1p.py` / `floor_check_1p.py` are written to the 1P input contract rather than line-edited
  from the 1N files: the writer schema changed (string SIDs `1Pnnn`, a per-answer `tags` list), and
  a tolerant reader plus an explicit REFUSE list was the smaller risk. The 1N behaviour they keep is
  the overlap / duplicate / floor / judge-noise logic.
* The model was never asked to obey a passive rule: lever 1 is deterministic on purpose, because the
  1N prompt line aimed at exactly this class did not work (6/22).
* No DB write, no app code, nothing deployed; the prompt was not reverted, the Slovak was not made
  more explicit, the TIME FRAME rule was not touched, TIP-as-rejection stays ON.
