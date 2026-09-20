# GATE 3 - phase 2D (lk re-judge at PAR = 2)

Random 250 of 2850 merged sk rows, seed 20260920. 0 model calls; 2C gate-3 code path (AG v4, reader_nom), ERROR-of-decided, bar 12 %.

| check | AGREE | ERROR | UNDEC/CONS | decided | ERROR-of-decided | 95 % CP | bar | verdict |
|---|---|---|---|---|---|---|---|---|
| AG v4 | 231 | 19 | 0 | 250 | 7.6 % | [4.64, 11.61] | 12 % | PASS |
| reader_nom | 141 | 12 | 97 | 153 | 7.84 % | [4.12, 13.3] | 12 % | PASS |
| g4 (diagnostic only) | 191 | 59 | 0 | 250 | 23.6 % | [18.48, 29.36] | 12 % | FAIL |

2C pooled reference: AG v4 7.20 %% [4.32, 11.14], reader_nom 2.86 %%.
g4 never gates (built over AG v2/v3).
