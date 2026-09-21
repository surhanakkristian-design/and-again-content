# Translation production — Phase 2G report

Date: 21 Sept 2026. Sources: `and-again-content/translation-offline/phase2g/` (partA/, partB/). Every number
below comes from those files. Intervals are exact 95 % Clopper–Pearson. "Not measured" means no file holds it.
Nothing was uploaded, no DB writes, nothing pushed.

## 1. Part A — enriched references: REJECTED

The single variable was richer Czech references (mean refs/sentence 1.10 -> 2.85; 114 variants added,
9 dropped by the tense filter). It made the checker worse, so it is rejected.

| metric | before (2F refs) | after (enriched) |
|---|---|---|
| coverage | 154/182 = 84.62 % [78.54, 89.53] | 149/182 = 81.87 % [75.49, 87.18] |
| false accepts (FA) | 11/178 = 6.18 % [3.12, 10.79] | 10/178 = 5.62 % [2.73, 10.09] |
| 1W arm (after) | coverage 97.76 % [95.78, 98.97] | FA 3.21 % [1.84, 5.15] |

- Item level: 45 items changed verdict. 3 of the 28 false rejections were rescued, 8 new false rejections
  appeared (28 -> 33). 3 FAs removed, 2 FAs added (11 -> 10).
- Cost: 295 Gemini calls, 0 failed, at most $0.016. Headless Claude 87,237 tokens, about 1,454 tokens per sentence.
- A5 (pricing the full enrichment) was **not done** because the variable was rejected. The only rate measured is
  about 1,454 tok/sentence.

### Part A defects (recorded, not fixed)
1. 220060: the main reference uses "he", but the Slovak is 2nd person ("by you"). The reference is wrong, so
   the correct candidate was rejected at L3.
2. 220027: the enriched reference drops "ich" (the object "them"), so the reference is thinner than the source.
3. It was not strictly one variable at L3. The enriched `v` also changed the deterministic layers: exact-match
   hits 14 -> 26, L2 lock firings 96 -> 92, items that reached L3 312 -> 295. No code changed, but L3 saw a
   different population.
4. L3 TIP rejections doubled, 5 -> 10. These account for most of the new false rejections.

## 2. Part B — Czech production completion: STOPPED

The chain started 07:51:08 and ended 08:07:09 with `CHAIN DONE STOPPED: STOP_rows_missing.md`.
Rows present 2,980 of 4,064; only **130 new** rows. Annotation used 724,487 tokens and lk used 244,152
(Part B 968,639 of the 2,900,000 Part B cap). 0 Gemini calls.

Builder deviations, as stated by the builder: 73 finished 2F sessions reused at 0 tokens; GATE 3 samples only
new rows (the all-rows score is logged as DIAGNOSTIC); the projection gate runs per session; lk needed
judgement on 1,364 rows (2F left 150 unjudged, n 5365–5414 and 6165–6264); lk sessions log only end events in
the timeline.

### B1. Why annotation stopped at 130 new rows, and why lk exited 1

**It was not a Claude usage limit or quota.** No session output, timeline entry or lk session contains a
usage-limit, weekly-limit, reset or quota string. Every flagged attempt has `exit 0` and `is_error false`.
The owner's weekly limit was **not** hit.

It was also not the token cap (724,487 of 2,900,000), not the projection gate (it projected 933,588 tokens and
0.39 h, which passed), and not the circuit breaker (floors 900 s / 200,000 tok / x3, never tripped). No real
HTTP 429 happened either: lk ledger `http_429_seen 0`, and every annotation "429" is exit 0.

Two things stopped it:

1. **STOP at GATE 3 (the actual stop).** In batch cz_0003, reader_nom scored 7/33 = 21.21 % [8.98, 38.91]
   ERROR-of-decided against the 12 % bar (counts AGREE 26, CONSERVATIVE 17, ERROR 7). The run stops after a
   gate fails. So cz_0004 and cz_0005 never ran, and that is where the 1,064 missing rows 7065–8128 are. 700 of
   those (cz_0004, 7 v sessions + 7 rw sessions) are **already annotated in adopted 2F sessions** but were never
   merged, because the merge happens per batch after the gate. Only 300 + 64 rows would cost tokens.
   The sample was 50 of cz_0003's 90 new rows, and the point estimate sits above the bar. But the interval's
   lower end (8.98 %) is under 12 %, so the failure is not statistically settled.
2. **Runner bug: false 429s (cost 20 rows and about 255k tokens).** `should_retry` treats a literal `"429"`
   anywhere in the CLI stdout/stderr as a rate limit (`run_2g_cz.py` l. 405–407, 653). The annotation output
   echoes each row's `"n"`. Piece p07 of chunk s04 holds n 5425–5434 and 6425–6434, so its output always
   contains **5429 / 6429**. All 3 attempts of each p07 piece were successful results (the logged "error"
   is a `"type":"result"` JSON) that were flagged as 429, retried with back-off, and then given up:
   cz_0002_s04_v_p07 used 107,555 tok, cz_0003_s04_v_p07 used 110,779 tok, 0 rows written.
   cz_0003_s04_v_p09 (n 6445–6454) was also flagged once and passed on attempt 2 (72,466 tok, twice the normal
   ~36k). Its first-attempt output was not kept, so the source of that "429" is not measured. It was most
   likely an incidental digit string. cz_0004_s04_v_p07 (n 7425–7434, which contains 7429) would have
   failed the same way.
3. **lk exit 1 = runner bug, after the work was done.** `run_2g_lk.py` l. 17 defines
   `def _samp(rnd, pop, k): return _samp(rnd, pop, min(k, len(pop)))`, which calls itself.
   `gate3(merged)` raised `RecursionError` after MERGE had finished (280 of 280 corrected rows written), so the
   lk GATE 3 report is null (`lk_report: null`). The lk rows are usable; the lk gate was never computed.

Other defects: `annotation_tok_per_new_row 5,573` and `projected_annotation_tokens_all_4064 6,765,593` in
DONE are misleading. Both are inflated by the ~255k wasted tokens, and the second multiplies by rows that cost 0.
A clean v piece costs 469,581 / 13 = 36,121.6 tok per 10 rows (≈ 3,612 tok/row, against the plan's 1,379).
`UPLOAD_README.md` still has the heading "Phase 2D".

### B2. 10-row pieces

25 pieces: 13 SUCCESS, 2 FAILURE, 10 NOT_RUN (cz_0004_s04_v_p01–p10, n 7365–7464).

| piece | n | status | tokens |
|---|---|---|---|
| cz_0002_s04_v_p06 | 5415–5424 | SUCCESS | 36,160 |
| cz_0002_s04_v_p07 | 5425–5434 | **FAILURE** (false 429) | 107,555 |
| cz_0002_s04_v_p08 | 5435–5444 | SUCCESS | 35,880 |
| cz_0002_s04_v_p09 | 5445–5454 | SUCCESS | 36,270 |
| cz_0002_s04_v_p10 | 5455–5464 | SUCCESS | 36,923 |
| cz_0003_s04_v_p01 | 6365–6374 | SUCCESS | 36,609 |
| cz_0003_s04_v_p02 | 6375–6384 | SUCCESS | 35,638 |
| cz_0003_s04_v_p03 | 6385–6394 | SUCCESS | 35,624 |
| cz_0003_s04_v_p04 | 6395–6404 | SUCCESS | 36,198 |
| cz_0003_s04_v_p05 | 6405–6414 | SUCCESS | 36,148 |
| cz_0003_s04_v_p06 | 6415–6424 | SUCCESS | 36,639 |
| cz_0003_s04_v_p07 | 6425–6434 | **FAILURE** (false 429) | 110,779 |
| cz_0003_s04_v_p08 | 6435–6444 | SUCCESS | 35,668 |
| cz_0003_s04_v_p09 | 6445–6454 | SUCCESS (2nd attempt) | 72,466 |
| cz_0003_s04_v_p10 | 6455–6464 | SUCCESS | 35,930 |

The failing pieces are **not refused content**. Their text is ordinary (full Slovak/Czech table in
`phase2g/partB/REFUSED_PIECES.md`):

- cz_0002_s04_v_p07, n 5425–5434: e.g. 5425 "On ide o barlách po nemocničnej chodbe." / "On jde o berlích po
  nemocniční chodbě."; 5429 "Chce si dať urobiť fotku na mramorovom schodisku." / "Chce si nechat udělat fotku na
  mramorovém schodišti."; 5434 "Stojí bosý na teplom piesku." / "Stojí bosý na teplém písku." (crutches, railings,
  a lake, gloves, a marble staircase, a runway model, pigeons with jewellery, sand).
- cz_0003_s04_v_p07, n 6425–6434: e.g. 6428 "On otvára okná každé ráno." / "On otevírá okna každé ráno.";
  6429 "Pravidlo majiteľa bytu: on musí otvárať okná každý deň." / "Pravidlo majitele bytu: on musí otevírat okna
  každý den."; 6434 "Je ráno, takže on práve teraz robí zdravý ranný nápoj." / "Je ráno, takže on právě teď dělá
  zdravý ranní nápoj." (sliding, scars, windows, a spade, soil, coffee, spinach).

### B3. s04 timing vs 429 clusters (session_timeline.jsonl)

| launch idx | piece | launched | "429" events | outcome |
|---|---|---|---|---|
| 2 | cz_0002_s04_v_p07 | 07:51:09 (with p06 in flight) | 07:51:35, 07:53:29, 07:56:28 | GIVEUP |
| 12 | cz_0003_s04_v_p07 | 07:58:05 (with p06 in flight) | 07:58:53, 08:00:48, 08:03:57 | GIVEUP |
| 14 | cz_0003_s04_v_p09 | 07:58:48 | 07:59:26 | OK on retry 08:01:20 |

The "429s" do not follow launch position, concurrency or time. While p07 was retrying, the other slot ran p08,
p09 and p10 (cz_0002) and p08–p10 (cz_0003) cleanly at ~32–41 s each. p07 was flagged at launch index 2 and at
launch index 12, 7 minutes apart, both times with only one other session in flight. That pattern fits a
content trigger (the n value) and not a server rate limit.

### B4. Rows per batch and what is missing

| batch | n range | rows | present | missing |
|---|---|---|---|---|
| cz_0001 | 4065–5064 | 1,000 | 1,000 | — |
| cz_0002 | 5065–6064 | 1,000 | 990 | 5425–5434 |
| cz_0003 | 6065–7064 | 1,000 | 990 | 6425–6434 |
| cz_0004 | 7065–8064 | 1,000 | 0 | all (700 in adopted 2F sessions, not merged) |
| cz_0005 | 8065–8128 | 64 | 0 | all |

Missing: 1,084 of 4,064 = 5425–5434, 6425–6434, 7065–8128.

GATE 3 per batch (AG v4, reader_nom, bar 12 %; g4 diagnostic only, never gates):

| batch | sample | AG v4 ERROR-of-decided | reader_nom ERROR-of-decided | g4 (diag) | result |
|---|---|---|---|---|---|
| cz_0001 | all rows, DIAGNOSTIC (0 new) | 5/50 = 10.00 % [3.33, 21.81] | 3/25 = 12.00 % [2.55, 31.22] | 11/50 = 22.00 % [11.53, 35.96] | skipped (no new rows) |
| cz_0002 all-rows diag | 50 | 4/48 = 8.33 % [2.32, 19.98] | 2/29 = 6.90 % [0.85, 22.77] | 9/48 = 18.75 % [8.95, 32.63] | diagnostic |
| cz_0002 new rows | 40 | 4/40 = 10.00 % [2.79, 23.66] | 2/26 = 7.69 % [0.95, 25.13] | 9/40 = 22.50 % [10.84, 38.45] | PASS |
| cz_0003 all-rows diag | 50 | 5/50 = 10.00 % [3.33, 21.81] | 2/32 = 6.25 % [0.77, 20.81] | 14/50 = 28.00 % [16.23, 42.49] | diagnostic |
| cz_0003 new rows | 50 of 90 | 5/50 = 10.00 % [3.33, 21.81] | **7/33 = 21.21 % [8.98, 38.91]** | 12/50 = 24.00 % [13.06, 38.17] | **FAIL -> STOP** |
| cz_0004, cz_0005 | — | not measured | not measured | not measured | not run |

### B5. lk (dedicated pass over the 280 rows still needing judgement)

The 280 rows are n 5365–5424, 5435–5464, 6165–6264, 6365–6424 and 6435–6464: 130 new plus the 150 from 2F.
There were 3 sessions at PAR 2 with 0 real 429s. All 3 came in under 30 % non-exact on attempt 1
(cz_0002_s01_lk 0/90 = 0.00 % [0.00, 4.02]; cz_0003_s01_lk 26/100 = 26.00 % [17.74, 35.73];
cz_0003_s02_lk 21/90 = 23.33 % [15.06, 33.43]). Each was re-run once:

| session | attempt 2 non-exact | still < 30 %? |
|---|---|---|
| cz_0002_s01_lk | 45/90 = 50.00 % [39.27, 60.73] (32 unusable, 13 adjust) | no |
| cz_0003_s01_lk | 15/100 = 15.00 % [8.65, 23.53] | yes |
| cz_0003_s02_lk | 21/90 = 23.33 % [15.06, 33.43] | yes |

- Merged 2G lk non-exact: 81/280 = **28.93 % [23.69, 34.62]** (exact 199, adjust 49, unusable 32). On attempt 1
  it was 47/280 = 16.79 % [12.60, 21.69].
- This is far below Czech 2F's pooled 52.44 % [50.54, 54.34] and Slovak's 51.13 %. The intervals do not overlap.
- cz_0002_s01_lk swung from 0 % to 50 % between two runs of the same prompt. That is a stability defect: one
  run judged every row exact, the next called 32/90 unusable.
- All 2,980 final rows: lk_verdict adjusted 1,392/2,980 = 46.71 % [44.91, 48.52].
- Rows that still lack a dedicated lk: **0 of the 2,980 present**. The 1,084 missing rows have no lk at all.
- lk GATE 3 was not measured (the RecursionError above).

### B6. Output files

- `partB/out/annotations_cz_final.jsonl`: 2,980 rows, unique n 4065–7064 (minus the two gaps).
- `partB/out/upload_cz_final.xlsx`: sheet `cz`, 2,980 data rows, columns exercise_id, language_code, level, src, en,
  structure_json. The largest structure_json cell is 2,936 chars (exercise 36878), against Excel's 32,767 limit.
- `partB/UPLOAD_README.md` is present (heading still says Phase 2D).
- The input SHA check inside final_merge: 767 checked, 0 mismatches.

### Input integrity (re-hash)

`find` + `shasum -a 256` over phase2c/out, phase2d/out, phase2e/out and phase2f, written to
`phase2g/SHA_inputs_after.txt`: 767 files, **identical** to `SHA_inputs_before.txt` (empty diff).

## 3. Not in this phase

- The Czech coverage measurement set from 2F is still **closed** and can be opened once. It was not opened here.
- F1 (≥ 120 agent drops) is probably unreachable on unselected production Czech: 52 of 100 sentences have no
  named doer. The target must be re-declared before the set is opened.

## 4. Tokens, Gemini, spend

| item | tokens |
|---|---|
| headless Part A | 87,237 |
| headless Part B (annotation 724,487 + lk 244,152) | 968,639 |
| subagent Part A | 73,643 |
| subagent Part B builder | 176,899 |
| this analysis subagent (estimate) | ~80,000 |
| main session (estimate) | ~60,000 |
| **total** | **≈ 1,446,000 of 3,500,000 (≈ 41 %)** |

About 255k of Part B (218,334 on the two given-up p07 pieces plus ~36k on the p09 retry) went on the false-429 bug.
Gemini: 295 of 450 calls, all in Part A, 0 failed, ≤ $0.016. Part B used 0 of its 150.

## 5. Defects recorded (none fixed)

1. `run_2g_cz.py` `should_retry`: a literal `"429"` substring in the output counts as a rate limit, so row
   numbers like 5429/6429/7429 trigger it. The retry should key on the error envelope (is_error/exit/API error
   type), not a substring.
2. `run_2g_lk.py` l. 17: `_samp` calls itself -> RecursionError, so lk GATE 3 was never computed and lk exited 1.
3. The GATE 3 STOP stranded 700 already-annotated cz_0004 rows, because merging happens only after the gate.
4. The DONE projections are inflated by wasted tokens and by rows that cost 0.
5. The lk re-run is unstable (cz_0002_s01_lk 0 % -> 50 %).
6. The `UPLOAD_README.md` heading is stale (Phase 2D).
7. Part A: the 220060 person error in the reference, the 220027 reference missing "ich", the enrichment also
   moving L1/L2/L3 reach, and TIP rejections doubling from 5 to 10.

## 6. Judgement

1. Thin references do **not** explain the production gap. More references made coverage worse (84.62 -> 81.87 %), so enrichment is rejected.
2. Czech is **not complete**: 2,980/4,064. 1,084 rows are missing (5425–5434, 6425–6434, 7065–8128).
3. There is no refused content. Both "refused" pieces are ordinary sentences that failed on a false 429 caused by n = 5429/6429.
4. There was no usage limit or quota. The stops were a GATE 3 reader_nom fail (7/33, lower bound 8.98 % < 12 %) and two runner bugs.
5. The next run should fix the 429 detector and `_samp` first (replay the stub tests), then decide the reader_nom bar on cz_0003.
6. After that, merge cz_0004's 700 adopted rows and annotate the remaining 20 + 300 + 64 rows. At ~3.6k tok/row that is about 1.4 M headless tokens. The 2F coverage set stays closed until F1 is re-declared.
