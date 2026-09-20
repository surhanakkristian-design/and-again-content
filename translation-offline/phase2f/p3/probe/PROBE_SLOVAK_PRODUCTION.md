# PROBE - Slovak PRODUCTION sentences, Phase 2F PART 3.1

**THIS IS A PROBE, NOT A MEASUREMENT THAT SETTLES ANYTHING.** At n is about 180 judged-correct items the exact 95 % interval is roughly +/- 5 points. That is enough to show whether production sentences sit in the SAME REGION as the test sets, and not enough to settle it. No target is settled here on either side.

- Status: completed
- Run started: 2026-09-21T00:30:10; report written: 2026-09-21T00:30:11
- Set: 60 Slovak sentences read READ-ONLY from `phase2d/out/annotations_sk_final.jsonl` (the real uploaded production material, 4064 usable rows), seed 20260921, sids 220001-220060 (fresh: 1W used 200001-200100, Part 2 uses 210001-210100).
- Stratification: {"A1": 15, "B2": 15, "B1": 15, "A2": 15} (pool by level: {"A1": 1174, "A2": 1220, "B1": 885, "B2": 785})
- `topic` in the judge packet = the production row's `type_title` (the exercise type). The production rows carry NO `topic` field; this is stated so the 1N defect (topic dropped from the packet) cannot recur silently.
- Stack, unchanged: `phase1w/stack_1w.py` (AG v4 full + v5 `rs_nom` + TIP determiner rule) with `reader_nom`; L3 = gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, prompt P-FROZEN-1U. The 1U runner/loader/scorer were COPIED into `phase2f/p3/probe/run/`; only the SET changed. Nothing was tuned.

## Headline

| | this probe (production) | 1W blind test (Slovak) |
|---|---|---|
| coverage | 168/180 = 93.33 % [0.00, 0.00] | 218/223 = 97.76 % [95.78, 98.97] |
| false accepts | 106/180 = 58.89 % [0.00, 0.00] | 16/498 = 3.21 % [1.84, 5.15] |

- Coverage intervals DO NOT overlap. Points differ by -4.43 points (probe 93.33 % vs 1W 97.76 %).
- FA intervals DO NOT overlap. Points differ by 55.68 points (probe 58.89 % vs 1W 3.21 %).
- Target coverage >= 90 %: on the POINT MET; on the INTERVAL (lower bound >= 90) MISSED.
- Target FA < 5 %: on the POINT MISSED; on the INTERVAL (upper bound < 5) MET.
- **Neither target is settled by a probe of this size.** The statement above is the arithmetic, not a verdict.

## Phase 2B beside it

- Phase 2B (`phase2b/TRANSLATION_PRODUCTION_PHASE2B_REPORT.md`) measured the AGENT READER erring on **50 %** of raw production text against **1.67 %** on blind-test Slovak (1W).
- 2B measured a DIFFERENT quantity from this probe: 2B scored the reader's derived field (agent_nom and the voice path) against a gold annotation. This probe scores the WHOLE stack's accept/reject decision against a blind judge. A reader that errs often can still be overruled by the later layers, and a reader that is right can still be followed by a bad L3 call. The two numbers are not the same measurement and cannot be subtracted.
- Consistency: this probe IS consistent with production behaving materially worse than the test sets - the coverage point falls well below 1W's and the intervals are far apart.
- The AG/reader cells below say how often the deterministic agent path fired on production at all; that is the cell to read next to 2B, and at this n it is thin.

## Judge

- Judge noise (hidden duplicate controls, same item judged twice under different jids in different packets): **0 of 36 pairs disagreed on correct/wrong = 0.0 %** [0.00, 100.00].
- Type-only disagreements (same correct/wrong, different type): 0
- Labels: {"correct": 180, "wrong": 180} ; wrong-types {"M": 180} ; borderline 0 ; items labelled 360
- The judge received the acceptance rules VERBATIM and every packet item carried `jid / slovak / level / answer / topic`.

## Every cell (exact Clopper-Pearson 95 %); thin cells are left as n = ...

- agent drops (writer drop-*) - FA among judged wrong: 31/60 = 51.67 % [100.00, 0.00]
- by-passive (writer by-passive*) - coverage among judged correct: n = 0 (no item of this kind in the production sample)
- by-passive (writer by-passive*) - FA among judged wrong: n = 0 (no item of this kind in the production sample)
- time-frame (writer time-frame) - FA among judged wrong: 29/60 = 48.33 % [100.00, 0.00]
- missing-article (writer missing-article) - FA among judged wrong: 46/60 = 76.67 % [0.00, 0.00]
- judge type T - FA among judged wrong: n = 0 (no item of this kind in the production sample)
- judge type W - FA among judged wrong: n = 0 (no item of this kind in the production sample)
- judge type M - FA among judged wrong: 106/180 = 58.89 % [0.00, 0.00]
- judge type S - FA among judged wrong: n = 0 (no item of this kind in the production sample)
- level A1 - coverage: 45/45 = 100.00 % [0.00, 100.00]
- level A1 - FA: 29/45 = 64.44 % [100.00, 0.00]
- level A2 - coverage: 45/45 = 100.00 % [0.00, 100.00]
- level A2 - FA: 33/45 = 73.33 % [0.00, 0.00]
- level B1 - coverage: 39/45 = 86.67 % [0.00, 0.00]
- level B1 - FA: 23/45 = 51.11 % [100.00, 0.00]
- level B2 - coverage: 39/45 = 86.67 % [0.00, 0.00]
- level B2 - FA: 21/45 = 46.67 % [100.00, 0.00]
- fa_by_layer: {"L3": 86, "L1": 20}
- accept_layer_all: {"L1/accept": 188, "F4v2/reject": 24, "L3/reject": 34, "L3/accept": 86, "L3:TIPrej/reject": 24, "F4v3/reject": 3, "F2B/reject": 1}
- l3_verdicts: {"DIFF": 34, "SAME": 89, "TIP": 25}
- l3_verdicts_by_label: {"DIFF/wrong": 34, "SAME/wrong": 89, "TIP/wrong": 25}
- ag_rejected_before_l3: 0
- ag_fired_by_label: {}

## Provenance

- FREEZE hash: SELFTEST (no commit)
- RUN commit: None
- FINAL_RUN_DONE: {"status": "DONE", "written_utc": "2026-09-20T22:30:11Z", "pid": 6415, "meta": {"phase": "1U", "freeze_commit": null, "coverage": [168, 180], "fa": [106, 180], "counted_calls": 148, "stub_model": true}}
- Runner exit: 0; preflight: {"n_items": 360, "l2_firings": 1, "l3_eligible": 148, "ag_rejected_before_l3": 0, "reach_l3_planned_calls": 148, "unique_requests": 148, "PLANNED_CALLS": 148, "counted_ledger_dev": 0, "cap": 250}
- Gemini budget gate: None
- calls lines: 148
- calls counted_http200: 148
- calls uncounted_retries: 0
- calls uncounted_by_http: {}
- calls failed_empty_or_unparsable_200: 0
- calls tokens_in: 1628
- calls tokens_out: 296
- calls spend_usd_list_price: 0.00028
- calls failure_rate_pct: 0.0
- Headless (Claude Opus, bundled binary, --output-format json): {"sessions": 0, "input_tokens": 0, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0, "output_tokens": 0, "total_incl_cache": 0, "reported_cost_usd": 0}

## Defects recorded, NOT fixed

- none recorded

## Access log (verbatim)

```
{"ts": "2026-09-20T22:30:10Z", "side": "1u:fresh1u", "what": "data/sentences.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:30:10Z", "side": "1u:fresh1u", "what": "data/annotations.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:30:10Z", "side": "1u:fresh1u", "what": "data/items.json", "caller": "runner_1p.py", "n": 360, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:30:10Z", "side": "1u:fresh1u", "what": "data/sentences.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:30:10Z", "side": "1u:fresh1u", "what": "data/annotations.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:30:10Z", "side": "1u:fresh1u", "what": "data/items.json", "caller": "runner_1p.py", "n": 360, "purpose": "Phase 1U preflight (0 calls)"}
{"ts": "2026-09-20T22:30:11Z", "side": "1u:fresh1u", "what": "data/sentences.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U final (labels are read last)"}
{"ts": "2026-09-20T22:30:11Z", "side": "1u:fresh1u", "what": "data/annotations.json", "caller": "runner_1p.py", "n": 60, "purpose": "Phase 1U final (labels are read last)"}
{"ts": "2026-09-20T22:30:11Z", "side": "1u:fresh1u", "what": "data/items.json", "caller": "runner_1p.py", "n": 360, "purpose": "Phase 1U final (labels are read last)"}
{"ts": "2026-09-20T22:30:11Z", "side": "1u:labels:fresh1u", "what": "data/labels.json", "caller": "runner_1u.py", "n": 360, "purpose": "Phase 1U final scoring"}
```
