# Re-score of the closed 1Q set against corrected labels — not a new measurement

Phase 1R, Task B. 1,080 stored per-item verdicts from `phase1q/rows_1q.json` re-scored after one blind re-judge of the 119 judged-correct type-M answers. **No model, Gemini or network calls were made (0 calls); no new items were generated, judged by a model, or re-run through the stack.** The stack's accept/reject decision per item is the frozen 1Q decision; only the LABELS changed.

## 0. Pre-flight — reproduction of the old scoring from `rows_1q.json` alone

| figure | status |
| --- | --- |
| pooled | reproduced |
| P1 | reproduced |
| P2 | reproduced |
| fa_by_wrongtype | reproduced |
| layers_reject_correct | reproduced |
| layers_reject_wrong | reproduced |
| cells | reproduced |
| M_buckets | reproduced |
| ci_selftest | reproduced |
| f5_readoff | reproduced |

Clopper-Pearson self-test: 8/481 → [0.72, 3.25] (target [0.72, 3.25]).

Half rule: `phase1p/data/sentences.json` `tags.half` (present for all 120 sentences; the odd/even fallback was never needed). Cells are tag-based, exactly as in `RESULTS_1Q.json`: `<tag>_cov` = accepted among judged-correct rows carrying that tag, `<tag>_fa` = accepted among judged-wrong rows carrying that tag; tag names in the rows are `agentless`, `timeframe`, `determiner`, `by-passive`, `plain`, `aspect`, `number`. M1/M2/M3/M4 come from `phase1q/taskA/triage.json`.

## 1. The label correction

- 119 judged-correct type-M answers re-judged blind today (116 M2 + 3 M1 hidden controls).
- Owner's rule: the 3 M1 (function word dropped) stay CORRECT; the 116 M2 follow the judge.
- **Movers (M2 → wrong): 116; stayers (M2 stays correct): 0.**
- Borderline among the movers: 7.
- M1 control disagreements (judge called an M1 control wrong): 2 — reported, not applied in the primary score.

Full movement table: `phase1r/taskA/TASKA_MOVEMENT_1R.md`.

Label totals: judged-correct 599 → **483**, judged-wrong 481 → **597**.

## 2. Headline — old labels vs corrected labels (primary variant)

| metric | OLD (1Q as closed) | NEW (corrected labels) |
| --- | --- | --- |
| pooled coverage | 436/599 = 72.79 % [69.03, 76.32] | 425/483 = 87.99 % [84.75, 90.75] |
| pooled FA | 8/481 = 1.66 % [0.72, 3.25] | 19/597 = 3.18 % [1.93, 4.93] |
| P1 coverage | 221/300 = 73.67 % [68.30, 78.56] | 215/241 = 89.21 % [84.59, 92.83] |
| P1 FA | 3/240 = 1.25 % [0.26, 3.61] | 9/299 = 3.01 % [1.39, 5.64] |
| P2 coverage | 215/299 = 71.91 % [66.44, 76.93] | 210/242 = 86.78 % [81.85, 90.78] |
| P2 FA | 5/241 = 2.07 % [0.68, 4.77] | 10/298 = 3.36 % [1.62, 6.08] |

### Do the halves still agree?

| | OLD | NEW |
| --- | --- | --- |
| coverage difference P1−P2 (points) | 1.76 | 2.43 |
| coverage Fisher exact p | 0.647 | 0.4843 |
| coverage CIs overlap | True | True |
| FA difference P1−P2 (points) | -0.82 | -0.35 |
| FA Fisher exact p | 0.7243 | 0.8208 |
| FA CIs overlap | True | True |

## 3. False accepts by wrong type

| wrong type | OLD | NEW |
| --- | --- | --- |
| T | 3/224 = 1.34 % [0.28, 3.86] | 3/224 = 1.34 % [0.28, 3.86] |
| W | 1/127 = 0.79 % [0.02, 4.31] | 1/127 = 0.79 % [0.02, 4.31] |
| M | 0/10 = 0.00 % [0.00, 30.85] | 11/126 = 8.73 % [4.44, 15.08] |
| S | 4/120 = 3.33 % [0.92, 8.31] | 4/120 = 3.33 % [0.92, 8.31] |

## 4. Layers

### Which layer ACCEPTED each false accept

- OLD: L3 8
- NEW: L3 19

### Which layer REJECTED each judged-correct item (false rejections)

- OLD (163 items): F5 65, L3 53, L3:TIPrej 37, F3 5, F2B 3
- NEW (58 items): L3 30, L3:TIPrej 22, F5 4, F2B 2

### Which layer rejected judged-wrong items (true rejections)

- OLD: L3 393, L3:TIPrej 78, F5 2
- NEW: L3 416, L3:TIPrej 93, F5 63, F3 5, F2B 1

## 5. Cells

| cell | OLD | NEW |
| --- | --- | --- |
| agentless coverage | 84/116 = 72.41 % [63.34, 80.30] | 75/98 = 76.53 % [66.89, 84.50] |
| agentless FA | 2/154 = 1.30 % [0.16, 4.61] | 11/172 = 6.40 % [3.24, 11.15] |
| time-frame coverage | - (n=0) | - (n=0) |
| time-frame FA | 3/224 = 1.34 % [0.28, 3.86] | 3/224 = 1.34 % [0.28, 3.86] |
| determiner coverage | 95/120 = 79.17 % [70.80, 86.04] | 95/120 = 79.17 % [70.80, 86.04] |
| determiner FA | 0/7 = 0.00 % [0.00, 40.96] | 0/7 = 0.00 % [0.00, 40.96] |
| by-passive coverage | 42/42 = 100.00 % [91.59, 100.00] | 42/42 = 100.00 % [91.59, 100.00] |
| plain coverage | 169/271 = 62.36 % [56.30, 68.15] | 167/173 = 96.53 % [92.60, 98.72] |
| aspect coverage | 46/50 = 92.00 % [80.77, 97.78] | 46/50 = 92.00 % [80.77, 97.78] |

The 1N figure to hold for time-frame FA was 3/170 = 1.76 %; on the 1Q set it reads 3/224 = 1.34 % [0.28, 3.86] under old labels and 3/224 = 1.34 % [0.28, 3.86] under corrected labels (type-T items carry no M relabelling, so the cell is unchanged by construction).

### M buckets — accepted k/n (stack decisions are the frozen ones)

| bucket | n | accepted | rejected | rejecting layers |
| --- | --- | --- | --- | --- |
| M1 (function word dropped, stays CORRECT) | 3 | 0 | 3 | F5 2, L3 1 |
| M2 movers (now WRONG) | 116 | 11 | 105 | F5 61, L3 23, L3:TIPrej 15, F3 5, F2B 1 |
| M2 stayers (still CORRECT) | 0 | 0 | 0 | |
| M3 (already wrong) | 9 | 0 | 9 | L3 7, L3:TIPrej 2 |
| M4 (already wrong) | 1 | 0 | 1 | F5 1 |

## 6. How the stack treated the movers — the key number

- Movers: **116** (P1 59 / P2 57).
- **ACCEPTED by the stack: 11** → these are new false accepts (layers: L3 11).
- **REJECTED by the stack: 105** → these stop being false rejections (layers: F5 61, L3 23, L3:TIPrej 15, F3 5, F2B 1).

Accepted movers (the new false accepts):

| iid | half | accepting layer |
| --- | --- | --- |
| W:170039:w2 | P1 | L3 |
| W:170021:w2 | P1 | L3 |
| W:170054:w2 | P2 | L3 |
| W:170027:w2 | P1 | L3 |
| W:170036:w2 | P2 | L3 |
| W:170051:w2 | P1 | L3 |
| W:170091:w4 | P1 | L3 |
| W:170048:w2 | P2 | L3 |
| W:170080:w4 | P2 | L3 |
| W:170012:w2 | P2 | L3 |
| W:170003:w2 | P1 | L3 |

## 7. Sensitivity variants (pooled)

| variant | flipped | coverage | FA |
| --- | --- | --- | --- |
| PRIMARY (M2 follow the judge, M1 untouched) | 116 | 425/483 = 87.99 % [84.75, 90.75] | 19/597 = 3.18 % [1.93, 4.93] |
| S1: judge followed on all 119 (M1 too) | 118 | 425/481 = 88.36 % [85.15, 91.08] | 19/599 = 3.17 % [1.92, 4.91] |
| S2: borderline movers stay correct | 109 | 426/490 = 86.94 % [83.63, 89.79] | 18/590 = 3.05 % [1.82, 4.78] |

## 8. F5 and F6 under corrected labels

- F5 rejected 67 items in all: OLD read-off = costs 65 judged-correct for 2 catches.
- Of those 65 rejected-"correct" items, **61 are movers** — F5 was right about them all along.
- NEW read-off: F5 costs **4** judged-correct for **63** catches.
- Coverage with F5 on (new labels): 425/483 = 87.99 % [84.75, 90.75]; if every F5 rejection were accepted instead: 429/483 = 88.82 % [85.67, 91.49] (old-label bound was 501/599 = 83.64 %).

**F6: not recomputable.** F6 per-item verdicts are NOT stored: rows_1q.json has no F6 field, the F6 layer never appears in the `layer` column (layers seen: L1/L3/L3:TIPrej/F5/F3/F2B), and phase1p/results_1p.json rows carry only sid/item_id/half/level/judged/judged_type/tags/writer_passive/intent/layers/lever1/lever2_fired/lever3/final_accept/tip/f9_readout - no F6 readout. RESULTS_1Q f6 holds aggregates only (rej_correct_all=4, rej_wrong_all=12, m3 catches 0). Which 4 judged-correct items F6 rejected is therefore not recoverable from the read-allowed files, so the F6 recomputation under corrected labels is NOT done and NOT estimated.
