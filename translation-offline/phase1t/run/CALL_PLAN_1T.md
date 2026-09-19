# CALL_PLAN_1T — counted by a 0-call pass on the real set, 19 Sept 2026

`python3 runner_1t.py --preflight` (0 model calls, PREFLIGHT_1T.json):

| quantity | n |
|---|---:|
| items in `phase1t/set/data/items.json` | 900 |
| sentences | 100 |
| L2 lock firings under BASE (apparatus check, must be > 0) | 120 |
| L3-eligible under LOCKTIP | 698 |
| — of them rejected by AG v3 **before** L3 (0 calls) | 128 |
| **items that reach L3 = planned model calls** | **570** |
| unique requests / reusable stored verdicts | 570 / 0 |
| lever-1 calls (1P had a second request set) | 0 — lever 1 is removed |

**Planned counted calls for `--final`: 570.**  There is no dev spend in 1T and no ablation.

`call_cap` in `FROZEN_CONFIG_1T.json` is **null**, so `--final` refuses.  The owner has to write a
number; anything below 580 makes `--preflight` write `STOP_PLAN.txt` (the threshold is cap − 10).
A cap of 640 leaves the run 70 spare calls for retries after a transport outage.

AG v3 on the real set (0 calls, source-side inputs only): fires on 128 of 900 items; AG v2 would
fire on 67 (76 v3-only firings, 15 v2-only); single flags: clause 125, subj 94, by 67; 161 answers
are agentless passives on which v3 abstains (the SKP / no-nominative-agent path).
