# Translation production — Phase 2H report

Date: 21 Sept 2026. Source: `and-again-content/translation-offline/phase2h/` (P). Every number below was re-read
or re-computed from the files in P (python, 0 model calls). Intervals are exact two-sided 95 % Clopper–Pearson.
"Not measured" means no file holds it. Nothing was uploaded, no DB writes, nothing pushed.

The chain ran 08:46:56–09:09:43 and ended `CHAIN DONE OK` (`DONE`: `OK | 2026-09-21 09:09:43 CHAIN inputs unchanged`).

## 0. Test suite, rows present, xlsx

`chain_2h.log` line 2: `2026-09-21 08:47:00 CHAIN tests: SUMMARY: 15/15 PASS`. `test_2h_output.txt` verbatim:

```
PASS T1 success with 429 in row numbers is not retried - n=5429: 1 call, SUCCESS; n=6429: 1 call, SUCCESS; n=7429: 1 call, SUCCESS (fixture tail = stored p07 fragment, 400 chars)
PASS T2 rate limit only from the envelope - real 429 envelope retried (2 calls); 429 only in text/stderr -> 1 call
PASS T3 _samp no recursion - k=250 over 3 -> 3 items; k=50 over 100 -> 50
PASS T4 GATE 3 7/33 and 7/45 FLAG, not STOP - 7/33 CP [8.98, 38.91] -> FLAG file, no STOP; 7/45 CP [6.49, 29.46] -> FLAG
PASS T4b GATE 3 <40 decided only FLAGS - 30/35 (CP lower 69.74) -> FLAG only; 30/45 -> STOP
PASS T5 GATE 3 STOP stops only its batch - cz_t5a STOP (rows written, marked, excluded from xlsx); cz_t5b FLAG, in xlsx; 2 model calls
PASS T6 700 adopted cz_0004 rows written before a failing gate - 700 adopted cz_0004 rows written before the (forced) STOP: ['7065-7364', '7465-7864']
PASS T7 stop-file scoping between stages - gate STOP/FLAG files never block the other stage (lk 1 calls, annotate 1 calls); STOP_token_cap blocks (0 calls)
PASS T9 end to end 10 real rows annotate->lk->merge->upload - 10 rows: 2 model calls; final 2980 rows ({'lk_2h_dedicated': 10, 'phase2g_final': 2970}); xlsx 2980 rows; lk status ['accepted']
PASS T8 resume spawns 0 sessions - second invocation: 0 sessions planned, 0 spawns (first run made 2)
PASS T10 apply_lk reproduces 2G lk merge - apply_lk reproduces 2G's lk-merged rows on all 280 rows 2G judged
PASS T11 lk prompt byte-identical to 2G - lk prompt byte-identical to 2G's stored prompts (3 sessions), sha16 5fa910459c078539
PASS T12 first session failure stops at 0 cost - first session exit 1 -> STOP_first_session_failed.md, 1 call, 0 tokens
PASS T13 usage limit stops everything - usage-limit envelope -> STOP_usage_limit.md, no retry, lk then spawns 0
PASS T14 token cap reservation - reservation 0 + 0 + 5000 > cap 1000 -> STOP_token_cap.md before spawning
SUMMARY: 15/15 PASS
```

- `out/annotations_cz_final.jsonl`: **4,064 of 4,064 rows**, 4,064 unique n, n 4065–8128, **0 missing** (no gap
  ranges). 4,064 unique exercise_id. `merge_2h.json` agrees: `rows_missing_of_4064 {"count": 0, "ranges": []}`.
- `out/upload_cz_final.xlsx`: sheet `cz`, **4,064 data rows**, columns exercise_id, language_code, level, src, en,
  structure_json; every language_code `cz`; the exercise_id set equals the jsonl's; `structure_json.exercise_id`
  equals the column on 4,064/4,064. **0 rows excluded** (no batch was GATE 3 STOPPED; `UPLOAD 4064 rows, 0 excluded`).
  Largest structure_json cell 2,936 chars.
- No `STOP_*.md` file exists in P. Four `FLAG_*.md` files exist (section 2).

## 1. Rows per batch

| batch | n range | expected | present | source |
|---|---|---|---|---|
| cz_0001 | 4065–5064 | 1,000 | 1,000 | adopted 2G (2G's file, built from 20 adopted 2F sessions) |
| cz_0002 | 5065–6064 | 1,000 | 990 + 10 | 990 adopted 2G; the 10 gap rows 5425–5434 new 2H (cz_gap) |
| cz_0003 | 6065–7064 | 1,000 | 990 + 10 | 990 adopted 2G; the 10 gap rows 6425–6434 new 2H (cz_gap) |
| cz_gap | 5425–5434, 6425–6434 | 20 | 20 | new 2H: one v session `cz_gap_s04_v`; rw rows from the adopted cz_0002/0003 s04_rw sessions |
| cz_0004 | 7065–8064 | 1,000 | 1,000 | 700 adopted 2F sessions (s01, s02, s03, s05, s06, s07, s08) + 300 new 2H (s04, s09, s10: 3 v + 3 rw sessions) |
| cz_0005 | 8065–8128 | 64 | 64 | new 2H (s01_v, s01_rw) |
| **total** | 4065–8128 | **4,064** | **4,064** | |

- Adoption (`run_2h.log`): 86 sessions adopted, 73 from 2F and 13 from 2G, 0 rejected. They cost 0 tokens in 2H
  (ledger `tokens_spent_earlier`: 6,260,831 for the 2F ones and 469,581 for the 2G ones, spent in earlier phases).
- `merge_2h.json` sources: `phase2g_final` 2,700 rows (byte-equal to 2G's final rows; checked 2,700/2,700) and
  `lk_2h_dedicated` 1,364 rows (the 280 rows 2G judged + the 1,084 rows new to the final file). The source label
  names where `lk` came from, not where the annotation came from.
- Still missing: **nothing**.

## 2. GATE 3 per batch (annotate stage)

Sample: 50 random rows per batch of the rows in scope (cz_gap: its 20). Bar 12 %. Rule: decided < 40 -> FLAG only;
CP lower > 12 % -> STOP; point > 12 % -> FLAG; else PASS. g4 is recorded only. Numbers from `gates_2h.json`.

| batch | scored | AG v4 ERROR/decided | AG v4 result | reader_nom ERROR/decided | reader_nom result | g4 (recorded) | batch |
|---|---|---|---|---|---|---|---|
| cz_gap | 20 of 20 | 0/20 = 0.00 % [0.00, 16.84] | FLAG (decided < 40) | 1/15 = 6.67 % [0.17, 31.95] (CONSERVATIVE 5) | FLAG (decided < 40) | 4/20 = 20.0 % | FLAG |
| cz_0004 | 50 of 1,000 | 6/50 = 12.00 % [4.53, 24.31] | PASS (point = bar) | 3/30 = 10.00 % [2.11, 26.53] (CONSERVATIVE 20) | FLAG (decided < 40) | 14/50 = 28.0 % | FLAG |
| cz_0005 | 50 of 64 | 5/50 = 10.00 % [3.33, 21.81] | PASS | 3/28 = 10.71 % [2.27, 28.23] (CONSERVATIVE 22) | FLAG (decided < 40) | 11/50 = 22.0 % | FLAG |
| cz_0001–0003 | — | not re-gated in 2H (adopted) | — | not re-gated in 2H | — | — | — |

FLAG files, all "decided < 40: FLAG only, never STOP", nothing stopped or excluded:

- `FLAG_gate3_agv4_cz_gap.md` — 20 decided (the batch has only 20 rows).
- `FLAG_gate3_reader_nom_cz_gap.md` — 15 decided.
- `FLAG_gate3_reader_nom_cz_0004.md` — 30 decided (20 of 50 CONSERVATIVE).
- `FLAG_gate3_reader_nom_cz_0005.md` — 28 decided (22 of 50 CONSERVATIVE).

No batch reached STOP. No CP lower bound exceeds 12 % (highest lower bound: AG v4 cz_0004, 4.53 %).

lk-stage GATE 3 (250 rows of the 1,364, seed 20260920, blocks nothing): AG v4 14/245 = 5.71 % [3.16, 9.40] PASS;
reader_nom 16/152 = 10.53 % [6.14, 16.53] PASS; g4 53/245 = 21.63 % recorded.

## 3. lk

Prompt sha16 `5fa910459c078539`. Acceptance rule (`lk_sessions_2h.json`): run 1 ≥ 30 % non-exact -> accepted;
else run 2; runs differing by > 15 points -> run 3 and per-row majority (tie -> unusable > adjust > exact); else
run 2 is used (`accepted_below_bar` when still < 30 %).

| session | n range | rows | run 1 non-exact | run 2 | run 3 | status (used) |
|---|---|---|---|---|---|---|
| lk2h_s01 | 5365–5464 | 100 | 2/100 = 2.00 % [0.24, 7.04] | 0/100 = 0.00 % [0.00, 3.62] | — | accepted_below_bar (r2) |
| lk2h_s02 | 6165–6264 | 100 | 30/100 = 30.00 % [21.24, 39.98] | — | — | accepted (r1) |
| lk2h_s03 | 6365–6464 | 100 | 4/100 = 4.00 % [1.10, 9.93] | 7/100 = 7.00 % [2.86, 13.89] | — | accepted_below_bar (r2) |
| lk2h_s04 | 7065–7164 | 100 | 19/100 = 19.00 % [11.84, 28.07] | 10/100 = 10.00 % [4.90, 17.62] | — | accepted_below_bar (r2) |
| lk2h_s05 | 7165–7264 | 100 | 9/100 = 9.00 % [4.20, 16.40] | 53/100 = 53.00 % [42.76, 63.06] | 24/100 = 24.00 % [16.02, 33.57] | majority_of_3 |
| lk2h_s06 | 7265–7364 | 100 | 20/100 = 20.00 % [12.67, 29.18] | 18/100 = 18.00 % [11.03, 26.95] | — | accepted_below_bar (r2) |
| lk2h_s07 | 7365–7464 | 100 | 14/100 = 14.00 % [7.87, 22.37] | 19/100 = 19.00 % [11.84, 28.07] | — | accepted_below_bar (r2) |
| lk2h_s08 | 7465–7564 | 100 | 3/100 = 3.00 % [0.62, 8.52] | 3/100 = 3.00 % [0.62, 8.52] | — | accepted_below_bar (r2) |
| lk2h_s09 | 7565–7664 | 100 | 6/100 = 6.00 % [2.23, 12.60] | 16/100 = 16.00 % [9.43, 24.68] | — | accepted_below_bar (r2) |
| lk2h_s10 | 7665–7764 | 100 | 14/100 = 14.00 % [7.87, 22.37] | 12/100 = 12.00 % [6.36, 20.02] | — | accepted_below_bar (r2) |
| lk2h_s11 | 7765–7864 | 100 | 10/100 = 10.00 % [4.90, 17.62] | 19/100 = 19.00 % [11.84, 28.07] | — | accepted_below_bar (r2) |
| lk2h_s12 | 7865–7964 | 100 | 14/100 = 14.00 % [7.87, 22.37] | 14/100 = 14.00 % [7.87, 22.37] | — | accepted_below_bar (r2) |
| lk2h_s13 | 7965–8064 | 100 | 8/100 = 8.00 % [3.52, 15.16] | 16/100 = 16.00 % [9.43, 24.68] | — | accepted_below_bar (r2) |
| lk2h_s14 | 8065–8128 | 64 | 13/64 = 20.31 % [11.28, 32.23] | 35/64 = 54.69 % [41.75, 67.18] | 11/64 = 17.19 % [8.90, 28.68] | majority_of_3 |

All 29 runs had status OK and returned every row; every interval in the file was reproduced by my own CP code.

- **Second run needed: 13 of 14 sessions** (all except lk2h_s02, which sat exactly on the 30.0 % bar).
  **Third run: lk2h_s05 and lk2h_s14.** Only lk2h_s02 was `accepted` in the plain sense; 11 are
  `accepted_below_bar`, 2 are `majority_of_3`.
- **Final non-exact over all 1,364 lk-judged rows: 206/1,364 = 15.10 % [13.24, 17.11]** (exact 1,158, adjust 195,
  unusable 11). Against Czech 2F pooled 52.44 % [50.54, 54.34]: **no overlap**. Against Slovak 51.13 %: far
  outside the interval (no Slovak interval is given in the 2G report; not recomputed).
- The 280 rows 2G judged, re-judged: **36/280 = 12.86 % [9.17, 17.35]** (exact 244, adjust 36) vs 2G's
  28.93 % [23.69, 34.62]: **no overlap**. Row by row: 2G adjusted -> 2H exact 60, 2G exact -> 2H adjust 15,
  adjusted both times 21, exact both times 184.
- The 1,084 other rows: 170/1,084 = 15.68 % [13.57, 17.99].
- **Does the 30 % rule bias the rate upward? Yes, by design.** Only sessions under 30 % get another draw; a
  session over 30 % keeps its first draw. On top of that, a majority tie resolves to the more severe class.
  Measured: run 1 pooled 166/1,364 = 12.17 % [10.48, 14.02] -> final 15.10 %, +2.93 points. The final is about
  equal to the mean of all 2,792 row-runs (423/2,792 = 15.15 % [13.84, 16.53]), so here the shift is the
  second-run draws, not an inflation beyond what repeated runs show. The rule did not pull the rate toward 30 %.
  No session reached 30 % after run 1 except s02.
- **Run-to-run swings persisted.** Max swing 44.0 points (lk2h_s05: 9 % -> 53 % -> 24 %); next lk2h_s14 37.5
  points (20.31 % -> 54.69 % -> 17.19 %). The rows 5365–5464 (lk2h_s01; 90 of them are 2G's
  cz_0002_s01_lk rows) scored 0 % and 50 % in 2G and 2 % and 0 % in 2H with the same prompt.
- lk_verdict over all 4,064 final rows: adjusted 1,517/4,064 = 37.33 % [35.84, 38.84] (2G: 1,392/2,980 = 46.71 %).
  The 2,700 rows not re-judged keep their earlier lk: 1,311/2,700 = 48.56 % adjusted (point only), against
  15.10 % on the 1,364 judged in 2H. The file mixes two lk regimes.
- `lk[0]` is a verbatim substring of `en` on 4,064/4,064 rows.

## 4. lk invocation comparison (`LK_INVOCATION_COMPARE.md`, static, 0 tokens)

- Prompt sha16 `5fa910459c078539` in 2D, 2G and 2H (asserted); LK_2D length 1,066 chars in all three.
- Identical: binary (claude-code 2.1.275), model `opus`, argv (`-p prompt --output-format json --max-turns 12
  --model opus`), env (`os.environ` + zsh-loaded OAuth token), capture_output, text, no stdin, prompt assembly.
- **Different (2):**
  1. `cwd`: `H` (own script dir) in 2D/2G, `SCRIPT_DIR` (phase2h) in 2H — three directories in the same repo.
  2. `timeout`: absent in the 2D/2G lk call, `WALL_CAP_S = 1800` s in 2H (one call function serves both stages).
- 2H reads `en`/`correct_answer_en` from selection_2c.jsonl, 2G from the annotation rows; T11 shows the assembled
  prompts are byte-identical to 2G's three stored ones.

## 5. Tokens

| item | tokens |
|---|---|
| headless annotation (9 sessions) | 468,550 |
| headless lk (29 runs: run 1 573,909 + re-runs 610,067) | 1,183,976 |
| **headless total** (`ledger_2h.json` spent) | **1,652,526 of 2,000,000 (82.63 %)** |
| builder subagent (given) | ~252,000 |
| this report subagent (estimate) | ~130,000 |
| main session (estimate) | ~40,000 |
| **all (estimate)** | **≈ 2,074,000** |

- Annotation: 468,550 / 384 paid v rows = **1,220 tok/row**, against the plan's 654,980 (2F means v 1,147.4,
  rw 1,257.0 tok/row; 1,379 tok/row reference 529,536). Actual was 71.5 % of the plan.
- lk: 1,183,976 / 2,792 row-runs = **424 tok/row-run** against the plan's 440; per judged row 868 tok, because
  of the re-runs. Plan run 1 600,160, actual run 1 573,909.
- Plan both stages 1,255,140 (before re-runs) vs actual 1,652,526: +397,386 (+31.7 %), all of it lk re-runs.
- All 38 launches ended with a `success` envelope; no retries, no 429, no usage limit.
- Gemini: **0 calls**.

## 6. Input integrity

`SHA_inputs_before.txt` and `SHA_inputs_after.txt`: 957 lines each, byte-identical (`cmp`), `SHA_inputs_diff.txt`
0 bytes; chain log `CHAIN inputs unchanged`. `FROZEN_SHA.txt`: run_2h.py `ad74237e2abd…19911c0`.

## 7. Defects recorded, not fixed

1. **T1 fixture is a reconstruction.** 2G never stored p07's full stdout, only the redacted last 400 characters;
   T1 builds its fixture around that 400-char fragment. It proves the classifier on that tail, not on p07's real
   full output.
2. **lk call is not byte-identical to 2D/2G:** `timeout=1800` added and `cwd` changed (section 4). No run hit the
   timeout (all 29 lk runs OK).
3. **Verdict mapping hides "unusable".** An `unusable` judgement whose `lk_fixed` is a verbatim span of `en` is
   applied and written as `adjusted` (2G's mapping, reproduced by T10). All 11 unusable rows had such a span, so
   the final file has 0 `unusable` verdicts; the three-way class survives only in `lk_sessions_2h.json` decisions.
4. **The < 40-decided rule makes some gates unable to fail.** cz_gap has 20 rows, so it is always FLAG. reader_nom
   excludes CONSERVATIVE, so a 50-row sample gave 28–30 decided: reader_nom cannot STOP any batch at this sample size.
5. **cz_0004 AG v4 passed on the boundary:** point 12.00 % = bar, PASS by `<=`.
6. **cz_0001–0003 were not re-gated.** cz_0003 was STOPPED in 2G on reader_nom 7/33 = 21.21 % [8.98, 38.91];
   under 2H's rule that result is a FLAG (T4), and those rows are now in the upload file with no new gate.
7. **exercise_id is stored as text in the xlsx**, not as an integer. The README's own check 8 asks the owner to
   confirm it is an integer.
8. **50 rows have an empty `v`** (starting at n 5365), carried unchanged from 2G's final file (which has the same
   50). The invariant `v[0] == en` holds on 4,014/4,064 only. The exact n range was not listed here.
9. **lk instability** (section 3): 13/14 sessions re-run, two third runs, swings up to 44 points.
10. **lk-stage GATE 3 measures fields lk does not touch** (AG v4, reader_nom). Its PASS says nothing about lk.
11. **Re-runs cost more than run 1** (610,067 vs 573,909); the plan's projection left them out.
12. **The file mixes lk regimes**: 2,700 rows carry the earlier lk (48.56 % adjusted), 1,364 carry 2H's (15.10 %
    non-exact).

## 8. Judgement

1. Czech is complete: 4,064/4,064 rows, 4,064 in the xlsx, 0 excluded, 0 STOP. It is fit to upload once the owner has checked the text-typed exercise_id, the 50 empty-`v` rows and the still-open lk-on-the-English-row decision.
2. lk is not stable: 13 of 14 sessions needed a second run, two needed a third, runs swung up to 44 points, and the final 15.10 % [13.24, 17.11] does not overlap 2F's 52.44 % or 2G's 28.93 % on the same prompt.
3. The runner can be reused (15/15 tests, 0 retries, cap held at 82.63 %), but it is Czech-only. Parametrise the language code and sheet, batch ids and n ranges, the v prompt (`v_cz`), the adoption sources and the 2G base file, the cz-specific g4/reader checks and the SHA input list.
4. Annotation cost 1,220 tok/row against a 1,147–1,257 plan. The whole overrun (+397,386 tokens) is lk re-runs driven by the 30 % rule, which moved the rate only from 12.17 % to 15.10 %.
5. Before the next language, the reader_nom gate needs a bigger sample or a different decided rule. At 50 rows it gets 28–30 decided and can never STOP.
