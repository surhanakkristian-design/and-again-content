# GATE 3 - phase 2D (lk re-judge at PAR = 2)

Random 250 of 2800 merged sk rows, seed 20260920. 0 model calls; 2C gate-3 code path (AG v4, reader_nom), ERROR-of-decided, bar 12 %.

| check | AGREE | ERROR | UNDEC/CONS | decided | ERROR-of-decided | 95 % CP | bar | verdict |
|---|---|---|---|---|---|---|---|---|
| AG v4 | 224 | 26 | 0 | 250 | 10.4 % | [6.91, 14.87] | 12 % | PASS |
| reader_nom | 136 | 8 | 106 | 144 | 5.56 % | [2.43, 10.65] | 12 % | PASS |
| g4 (diagnostic only) | 189 | 61 | 0 | 250 | 24.4 % | [19.21, 30.21] | 12 % | FAIL |

2C pooled reference: AG v4 7.20 %% [4.32, 11.14], reader_nom 2.86 %%.
g4 never gates (built over AG v2/v3).
