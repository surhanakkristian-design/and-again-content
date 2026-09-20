# PROBE - Slovak PRODUCTION sentences, Phase 2F PART 3.1

**THIS IS A PROBE, NOT A MEASUREMENT THAT SETTLES ANYTHING.** At n is about 180 judged-correct items the exact 95 % interval is roughly +/- 5 points. That is enough to show whether production sentences sit in the SAME REGION as the test sets, and not enough to settle it. No target is settled here on either side.

- Status: completed
- Run started: 2026-09-21T00:31:04; report written: 2026-09-21T00:38:56
- Set: 60 Slovak sentences read READ-ONLY from `phase2d/out/annotations_sk_final.jsonl` (the real uploaded production material, 4064 usable rows), seed 20260921, sids 220001-220060 (fresh: 1W used 200001-200100, Part 2 uses 210001-210100).
- Stratification: {"A1": 15, "B2": 15, "B1": 15, "A2": 15} (pool by level: {"A1": 1174, "A2": 1220, "B1": 885, "B2": 785})
- `topic` in the judge packet = the production row's `type_title` (the exercise type). The production rows carry NO `topic` field; this is stated so the 1N defect (topic dropped from the packet) cannot recur silently.
- Stack, unchanged: `phase1w/stack_1w.py` (AG v4 full + v5 `rs_nom` + TIP determiner rule) with `reader_nom`; L3 = gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, prompt P-FROZEN-1U. The 1U runner/loader/scorer were COPIED into `phase2f/p3/probe/run/`; only the SET changed. Nothing was tuned.

## Headline

| | this probe (production) | 1W blind test (Slovak) |
|---|---|---|
| coverage | 154/182 = 84.62 % [78.54, 89.53] | 392/401 = 97.76 % [95.78, 98.97] |
| false accepts | 11/178 = 6.18 % [3.12, 10.79] | 16/499 = 3.21 % [1.84, 5.15] |

- Coverage intervals DO NOT overlap. Points differ by -13.14 points (probe 84.62 % vs 1W 97.76 %).
- FA intervals OVERLAP. Points differ by 2.97 points (probe 6.18 % vs 1W 3.21 %).
- Target coverage >= 90 %: on the POINT MISSED; on the INTERVAL (lower bound >= 90) MISSED.
- Target FA < 5 %: on the POINT MISSED; on the INTERVAL (upper bound < 5) MISSED.
- **Neither target is settled by a probe of this size.** The statement above is the arithmetic, not a verdict.

## Phase 2B beside it

- Phase 2B (`phase2b/TRANSLATION_PRODUCTION_PHASE2B_REPORT.md`) measured the AGENT READER erring on **50 %** of raw production text against **1.67 %** on blind-test Slovak (1W).
- 2B measured a DIFFERENT quantity from this probe: 2B scored the reader's derived field (agent_nom and the voice path) against a gold annotation. This probe scores the WHOLE stack's accept/reject decision against a blind judge. A reader that errs often can still be overruled by the later layers, and a reader that is right can still be followed by a bad L3 call. The two numbers are not the same measurement and cannot be subtracted.
- Consistency: this probe IS consistent with production behaving materially worse than the test sets - the coverage point falls well below 1W's and the intervals are far apart.
- The AG/reader cells below say how often the deterministic agent path fired on production at all; that is the cell to read next to 2B, and at this n it is thin.

## The confound this probe cannot separate, stated plainly

A production sentence differs from a test sentence in TWO ways at once, and this probe changes both
together:

1. **the Slovak itself** - real uploaded material, multi-sentence items, fragments, whatever the
   pipeline produced; and
2. **the reference material the stack is allowed to match against** - which on production rows is
   much thinner than on a constructed set.

Measured on the two annotation sets (`set/reference_material_profile.json`, 0 model calls):

| | this probe (production) | 1U / 1W constructed set |
|---|---|---|
| accepted English references `v` per sentence, mean | 1.1 | 2.0 |
| sentences with only ONE accepted reference | 90.0 % | 0.0 % |
| `alt` entries (accepted token alternatives) per sentence, mean | 3.38 | 4.19 |
| sentences with an EMPTY `alt` map | 3.3 % | 0.0 % |

A blind writer's correct-but-differently-worded answer therefore has far less to match on a
production row. **The coverage gap below is consistent with the annotation being thinner, with the
sentences being harder, or with both, and this probe cannot tell those apart.** Anyone reading the
-13 point coverage difference as a property of production SENTENCES is over-reading it. Separating
the two needs a run that holds one of them fixed; that run has not been made and is not funded here.

## Judge

- Judge noise (hidden duplicate controls, same item judged twice under different jids in different packets): **0 of 36 pairs disagreed on correct/wrong = 0.0 %** [0.00, 9.74].
- Type-only disagreements (same correct/wrong, different type): 0
- Labels: {"correct": 182, "wrong": 178} ; wrong-types {"S": 31, "M": 55, "T": 52, "W": 40} ; borderline 37 ; items labelled 360
- The judge received the acceptance rules VERBATIM and every packet item carried `jid / slovak / level / answer / topic`.

## Every cell (exact Clopper-Pearson 95 %); thin cells are left as n = ...

- agent drops (writer drop-*) - FA among judged wrong: 2/22 = 9.09 % [1.12, 29.16]
- by-passive (writer by-passive*) - coverage among judged correct: 20/24 = 83.33 % [62.62, 95.26]
- by-passive (writer by-passive*) - FA among judged wrong: n = 0 (no item of this kind in the production sample)
- time-frame (writer time-frame) - FA among judged wrong: 1/52 = 1.92 % [0.05, 10.26]
- missing-article (writer missing-article) - FA among judged wrong: 3/27 = 11.11 % [2.35, 29.16]
- judge type T - FA among judged wrong: 1/52 = 1.92 % [0.05, 10.26]
- judge type W - FA among judged wrong: 1/40 = 2.50 % [0.06, 13.16]
- judge type M - FA among judged wrong: 6/55 = 10.91 % [4.11, 22.25]
- judge type S - FA among judged wrong: 3/31 = 9.68 % [2.04, 25.75]
- level A1 - coverage: 37/45 = 82.22 % [67.95, 92.00]
- level A1 - FA: 2/45 = 4.44 % [0.54, 15.15]
- level A2 - coverage: 44/45 = 97.78 % [88.23, 99.94]
- level A2 - FA: 2/45 = 4.44 % [0.54, 15.15]
- level B1 - coverage: 34/46 = 73.91 % [58.87, 85.73]
- level B1 - FA: 1/44 = 2.27 % [0.06, 12.02]
- level B2 - coverage: 39/46 = 84.78 % [71.13, 93.66]
- level B2 - FA: 6/44 = 13.64 % [5.17, 27.35]
- fa_by_layer: {"L3": 11}
- accept_layer_all: {"L3/accept": 151, "L3/reject": 131, "F4v2/reject": 13, "L1/accept": 14, "L3:TIPrej/reject": 29, "AG/reject": 13, "F3/reject": 4, "F5/reject": 4, "F2B/reject": 1}
- l3_verdicts: {"SAME": 151, "DIFF": 131, "TIP": 30, "None": 13}
- l3_verdicts_by_label: {"SAME/correct": 140, "DIFF/correct": 16, "TIP/correct": 5, "SAME/wrong": 11, "DIFF/wrong": 115, "TIP/wrong": 25, "None/wrong": 13}
- ag_rejected_before_l3: 13
- ag_fired_by_label: {"wrong": 13}

## Provenance

- FREEZE hash: 36a00a53723b05a87ee0636ca6328bb0b121cc14
- RUN commit: e99e6b9f084bd312a31527ae997f6d92ef827f54
- FINAL_RUN_DONE: {"status": "DONE", "written_utc": "2026-09-20T22:37:22Z", "pid": 7159, "meta": {"phase": "1U", "freeze_commit": "36a00a53723b05a87ee0636ca6328bb0b121cc14", "coverage": [154, 182], "fa": [11, 178], "counted_calls": 312, "stub_model": false}}
- Runner exit: 0; preflight: {"n_items": 360, "l2_firings": 96, "l3_eligible": 325, "ag_rejected_before_l3": 13, "reach_l3_planned_calls": 312, "unique_requests": 312, "PLANNED_CALLS": 312, "counted_ledger_dev": 0, "cap": 320}
- Gemini budget gate: part2_counted 0 + 250 = 250, within the 900 phase cap; this probe may spend at most 320 counted calls (declared budget 250, local ceiling 320)
- calls lines: 312
- calls counted_http200: 312
- calls uncounted_retries: 0
- calls uncounted_by_http: {}
- calls failed_empty_or_unparsable_200: 0
- calls tokens_in: 162085
- calls tokens_out: 312
- calls spend_usd_list_price: 0.01633
- calls failure_rate_pct: 0.0
- Headless (Claude Opus, bundled binary, --output-format json): {"sessions": 8, "input_tokens": 32, "cache_creation_input_tokens": 231170, "cache_read_input_tokens": 218880, "output_tokens": 97531, "total_incl_cache": 547613, "reported_cost_usd": 4.8596}
  - writer_part1_try1: exit 0, is_error False, turns 2, in 4, cache_creation 29764, cache_read 18042, out 11694, cost_usd 0.599031, denials 0
  - writer_part2_try1: exit 0, is_error False, turns 2, in 4, cache_creation 29126, cache_read 18026, out 11071, cost_usd 0.577068, denials 0
  - writer_part3_try1: exit 0, is_error False, turns 2, in 4, cache_creation 30071, cache_read 18004, out 12157, cost_usd 0.613657, denials 0
  - writer_part4_try1: exit 0, is_error False, turns 2, in 4, cache_creation 30372, cache_read 18129, out 12365, cost_usd 0.6219295, denials 0
  - judge_part1_try1: exit 0, is_error False, turns 2, in 4, cache_creation 28069, cache_read 36474, out 12860, cost_usd 0.620447, denials 0
  - judge_part2_try1: exit 0, is_error False, turns 2, in 4, cache_creation 26141, cache_read 36639, out 10773, cost_usd 0.5490745, denials 0
  - judge_part3_try1: exit 0, is_error False, turns 2, in 4, cache_creation 29581, cache_read 36654, out 14206, cost_usd 0.669307, denials 0
  - judge_part4_try1: exit 0, is_error False, turns 2, in 4, cache_creation 28046, cache_read 36912, out 12405, cost_usd 0.6090610000000001, denials 0

## Defects recorded, NOT fixed

- **planned calls above the declared ~250 budget** - 312 planned; spent anyway because the HARD constraint is the phase-wide cap of 900 shared with Part 2 (0 counted there), and the brief forbids narrowing the scope to fit. Local ceiling 320.
- **Clopper-Pearson helper in the PROBE REPORTING LAYER was wrong (found after the run, fixed, 0 model calls)** - p3_probe.cp() inverted 1 - I_p(a,b) with a bisection that assumes an increasing function, so every interval came back degenerate ([0,0] for coverage, [100,100] for FA). k/n were never affected. Fixed to the textbook form lower = BetaInv(a; k, n-k+1), upper = BetaInv(1-a; k+1, n-k); the fixed helper now reproduces the FROZEN scorer (phase1t/run/score_1t.cp) to the last digit on this run and on 1W 392/401 and 16/499. The published headline is the frozen scorer, not my helper. The measuring apparatus was wrong before the measurement was - 8th occurrence of that pattern.
- **8 of the 36 hidden duplicate controls landed in the SAME judge packet** - build_packets shuffles the item+duplicate sequence and then splits it into 4 contiguous packets, which does not force the two copies of a control into different packets. 28 of 36 pairs are cross-packet, 8 are within one packet, where the judge could in principle have anchored on its own earlier answer. The judge-noise rate is therefore an upper estimate of agreement quality / a lower estimate of noise. NOT fixed and NOT re-run: recorded.
- **the probe spent 312 counted calls against the declared ~250 budget** - the preflight planned 312 and the brief forbids narrowing the scope to fit, so the run went ahead under the HARD constraint (the phase-wide 900 shared with Part 2, which had counted 0). Local ceiling was 320. Reported, not hidden.
- **the 1U construction floors cannot hold on production material** - the seven F1-F5 floors are properties of a CONSTRUCTED set. The probe set is real uploaded production text, so the gate was kept structurally (a missing or malformed key still refuses) with every minimum set to 0 and the real counts reported as cells. A recorded DEVIATION, not a tuned gate.
- **production rows carry no topic field** - phase2d/out/annotations_sk_final.jsonl has no 'topic'; the judge packet's topic is the row's type_title (the exercise type). Stated so the 1N defect (topic dropped from the packet, 13 labels moved) cannot recur silently.

## Access log (verbatim)

```
{"ts": "2026-09-20T22:35:44Z", "side": "1u:fresh1u", "what": "data/sentences.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:35:44Z", "side": "1u:fresh1u", "what": "data/annotations.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:35:44Z", "side": "1u:fresh1u", "what": "data/items.json", "caller": "runner_1p.py", "n": 360, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:35:45Z", "side": "1u:fresh1u", "what": "data/sentences.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:35:45Z", "side": "1u:fresh1u", "what": "data/annotations.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:35:45Z", "side": "1u:fresh1u", "what": "data/items.json", "caller": "runner_1p.py", "n": 360, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:35:46Z", "side": "1u:fresh1u", "what": "data/sentences.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U final (labels are read last)"}
{"ts": "2026-09-20T22:35:46Z", "side": "1u:fresh1u", "what": "data/annotations.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U final (labels are read last)"}
{"ts": "2026-09-20T22:35:46Z", "side": "1u:fresh1u", "what": "data/items.json", "caller": "runner_1p.py", "n": 360, "purpose": "Phase 1U final (labels are read last)"}
{"ts": "2026-09-20T22:37:22Z", "side": "1u:labels:fresh1u", "what": "data/labels.json", "caller": "runner_1u.py", "n": 360, "purpose": "Phase 1U final scoring"}
```
