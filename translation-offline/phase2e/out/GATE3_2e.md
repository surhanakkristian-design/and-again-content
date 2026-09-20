# GATE 3 - phase 2D (lk re-judge at PAR = 2)

Random 250 of 1900 merged sk rows, seed 20260920. 0 model calls; 2C gate-3 code path (AG v4, reader_nom), ERROR-of-decided, bar 12 %.

| check | AGREE | ERROR | UNDEC/CONS | decided | ERROR-of-decided | 95 % CP | bar | verdict |
|---|---|---|---|---|---|---|---|---|
| AG v4 | 219 | 31 | 0 | 250 | 12.4 % | [8.58, 17.14] | 12 % | FAIL |
| reader_nom | 153 | 18 | 79 | 171 | 10.53 % | [6.36, 16.13] | 12 % | PASS |
| g4 (diagnostic only) | 187 | 63 | 0 | 250 | 25.2 % | [19.94, 31.06] | 12 % | FAIL |

2C pooled reference: AG v4 7.20 %% [4.32, 11.14], reader_nom 2.86 %%.
g4 never gates (built over AG v2/v3).
