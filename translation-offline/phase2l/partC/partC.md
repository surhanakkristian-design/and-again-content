# Phase 2L Part C: the configuration, and the stop

**CLOSED-SET, IN-SAMPLE** (both Slovak sets pooled, existing judge labels, 0 extra calls). Part B failed calls keep the L3 verdict.

| configuration | set | level | coverage | FA |
|---|---|---|---|---|
| reference-based stack (2I tonly / 2J fixed) | 2I | all | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| reference-based stack (2I tonly / 2J fixed) | 2J | all | 450/498 = 90.36 % [87.42, 92.81] | 24/402 = 5.97 % [3.86, 8.75] |
| reference-based stack (2I tonly / 2J fixed) | pooled | all | 893/995 = 89.75 % [87.69, 91.56] | 43/805 = 5.34 % [3.89, 7.13] |
| reference-based stack (2I tonly / 2J fixed) | pooled | A1 | 229/248 = 92.34 % [88.29, 95.32] | 5/202 = 2.48 % [0.81, 5.68] |
| reference-based stack (2I tonly / 2J fixed) | pooled | A2 | 236/250 = 94.40 % [90.78, 96.90] | 15/200 = 7.50 % [4.26, 12.07] |
| reference-based stack (2I tonly / 2J fixed) | pooled | B1 | 206/247 = 83.40 % [78.16, 87.82] | 13/203 = 6.40 % [3.45, 10.70] |
| reference-based stack (2I tonly / 2J fixed) | pooled | B2 | 222/250 = 88.80 % [84.22, 92.43] | 10/200 = 5.00 % [2.42, 9.00] |
| 2K SOURCE-ONLY, TIP rejected | 2I | all | 477/497 = 95.98 % [93.85, 97.52] | 37/403 = 9.18 % [6.55, 12.43] |
| 2K SOURCE-ONLY, TIP rejected | 2J | all | 474/498 = 95.18 % [92.91, 96.89] | 36/402 = 8.96 % [6.35, 12.18] |
| 2K SOURCE-ONLY, TIP rejected | pooled | all | 951/995 = 95.58 % [94.11, 96.77] | 73/805 = 9.07 % [7.18, 11.27] |
| 2K SOURCE-ONLY, TIP rejected | pooled | A1 | 231/248 = 93.15 % [89.25, 95.96] | 7/202 = 3.47 % [1.40, 7.01] |
| 2K SOURCE-ONLY, TIP rejected | pooled | A2 | 240/250 = 96.00 % [92.77, 98.07] | 16/200 = 8.00 % [4.64, 12.67] |
| 2K SOURCE-ONLY, TIP rejected | pooled | B1 | 237/247 = 95.95 % [92.68, 98.04] | 25/203 = 12.32 % [8.13, 17.64] |
| 2K SOURCE-ONLY, TIP rejected | pooled | B2 | 243/250 = 97.20 % [94.32, 98.87] | 25/200 = 12.50 % [8.26, 17.90] |
| 2K SOURCE-ONLY, TIP accepted (Part A) | 2I | all | 490/497 = 98.59 % [97.12, 99.43] | 164/403 = 40.69 % [35.86, 45.67] |
| 2K SOURCE-ONLY, TIP accepted (Part A) | 2J | all | 485/498 = 97.39 % [95.58, 98.60] | 148/402 = 36.82 % [32.09, 41.74] |
| 2K SOURCE-ONLY, TIP accepted (Part A) | pooled | all | 975/995 = 97.99 % [96.91, 98.77] | 312/805 = 38.76 % [35.38, 42.22] |
| 2K SOURCE-ONLY, TIP accepted (Part A) | pooled | A1 | 243/248 = 97.98 % [95.36, 99.34] | 63/202 = 31.19 % [24.87, 38.07] |
| 2K SOURCE-ONLY, TIP accepted (Part A) | pooled | A2 | 248/250 = 99.20 % [97.14, 99.90] | 78/200 = 39.00 % [32.20, 46.13] |
| 2K SOURCE-ONLY, TIP accepted (Part A) | pooled | B1 | 241/247 = 97.57 % [94.79, 99.10] | 86/203 = 42.36 % [35.48, 49.48] |
| 2K SOURCE-ONLY, TIP accepted (Part A) | pooled | B2 | 243/250 = 97.20 % [94.32, 98.87] | 85/200 = 42.50 % [35.56, 49.67] |
| SOURCE-ONLY + B, TIP rejected | 2I | all | 463/497 = 93.16 % [90.57, 95.22] | 19/403 = 4.71 % [2.86, 7.26] |
| SOURCE-ONLY + B, TIP rejected | 2J | all | 457/498 = 91.77 % [89.00, 94.03] | 18/402 = 4.48 % [2.67, 6.98] |
| SOURCE-ONLY + B, TIP rejected | pooled | all | 920/995 = 92.46 % [90.64, 94.03] | 37/805 = 4.60 % [3.26, 6.28] |
| SOURCE-ONLY + B, TIP rejected | pooled | A1 | 227/248 = 91.53 % [87.35, 94.68] | 3/202 = 1.49 % [0.31, 4.28] |
| SOURCE-ONLY + B, TIP rejected | pooled | A2 | 235/250 = 94.00 % [90.30, 96.60] | 13/200 = 6.50 % [3.51, 10.86] |
| SOURCE-ONLY + B, TIP rejected | pooled | B1 | 227/247 = 91.90 % [87.77, 94.98] | 11/203 = 5.42 % [2.74, 9.49] |
| SOURCE-ONLY + B, TIP rejected | pooled | B2 | 231/250 = 92.40 % [88.39, 95.36] | 10/200 = 5.00 % [2.42, 9.00] |
| SOURCE-ONLY + B, TIP accepted | 2I | all | 469/497 = 94.37 % [91.96, 96.22] | 68/403 = 16.87 % [13.35, 20.89] |
| SOURCE-ONLY + B, TIP accepted | 2J | all | 462/498 = 92.77 % [90.13, 94.89] | 63/402 = 15.67 % [12.26, 19.60] |
| SOURCE-ONLY + B, TIP accepted | pooled | all | 931/995 = 93.57 % [91.86, 95.01] | 131/805 = 16.27 % [13.79, 19.01] |
| SOURCE-ONLY + B, TIP accepted | pooled | A1 | 231/248 = 93.15 % [89.25, 95.96] | 21/202 = 10.40 % [6.55, 15.45] |
| SOURCE-ONLY + B, TIP accepted | pooled | A2 | 240/250 = 96.00 % [92.77, 98.07] | 40/200 = 20.00 % [14.69, 26.22] |
| SOURCE-ONLY + B, TIP accepted | pooled | B1 | 229/247 = 92.71 % [88.73, 95.62] | 37/203 = 18.23 % [13.17, 24.24] |
| SOURCE-ONLY + B, TIP accepted | pooled | B2 | 231/250 = 92.40 % [88.39, 95.36] | 33/200 = 16.50 % [11.64, 22.38] |

Rule: among SOURCE-ONLY + B with TIP rejected / TIP accepted, pick the higher pooled coverage among those with pooled FA < 5 % on the point; SAFETY STOP if none has pooled coverage >= 90 % AND FA < 5 % on the point.

FA < 5 % on the point: ['SOURCE-ONLY + B, TIP rejected']. Both targets on the point: ['SOURCE-ONLY + B, TIP rejected'].

- SOURCE-ONLY + B, TIP rejected: coverage 920/995 = 92.46 % [90.64, 94.03] (interval target MET), FA 37/805 = 4.60 % [3.26, 6.28] (interval target missed)
- SOURCE-ONLY + B, TIP accepted: coverage 931/995 = 93.57 % [91.86, 95.01] (interval target MET), FA 131/805 = 16.27 % [13.79, 19.01] (interval target missed)

**Chosen: SOURCE-ONLY + B, TIP rejected.** Frozen as stack_2l.py (TIP_ACCEPT = False); FROZEN_SHA_C.txt; commit in FREEZE_COMMIT_C.txt.
