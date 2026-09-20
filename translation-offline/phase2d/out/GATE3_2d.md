# GATE 3 - phase 2D (lk re-judge at PAR = 2)

Random 250 of 4064 merged sk rows, seed 20260920. 0 model calls; 2C gate-3 code path (AG v4, reader_nom), ERROR-of-decided, bar 12 %.

| check | AGREE | ERROR | UNDEC/CONS | decided | ERROR-of-decided | 95 % CP | bar | verdict |
|---|---|---|---|---|---|---|---|---|
| AG v4 | 225 | 25 | 0 | 250 | 10.0 % | [6.58, 14.41] | 12 % | PASS |
| reader_nom | 150 | 6 | 94 | 156 | 3.85 % | [1.42, 8.18] | 12 % | PASS |
| g4 (diagnostic only) | 186 | 64 | 0 | 250 | 25.6 % | [20.31, 31.48] | 12 % | FAIL |

2C pooled reference: AG v4 7.20 %% [4.32, 11.14], reader_nom 2.86 %%.
g4 never gates (built over AG v2/v3).
