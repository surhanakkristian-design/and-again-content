# Phase 1S Task C - configuration x label set (0 model calls)

L3:TIPrej = the L3 model answered TIP (same meaning, but with a reservation); the frozen stack runs tip_reject=True, so that acceptance is turned into a rejection. The stored tip is the bare token 'TIP' - no tip text, so the tip names no word.

RDET / RDET+S2 are **CIRCULAR** (AG v2 grades itself) - a bound, not a result.

AG v1 -> v2 changes: 3 rows.

## label set 1R

| config | coverage | FA | FA crosses 5 % | agentless cov | agentless FA | P1/P2 cov p | P1/P2 FA p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| K0 | 425/483 = 87.99 % [84.75, 90.75] | 19/597 = 3.18 % [1.93, 4.93] | no | 75/98 = 76.53 % [66.89, 84.50] | 11/172 = 6.40 % [3.24, 11.15] | 0.4843 | 0.8208 |
| K1 | 401/483 = 83.02 % [79.37, 86.26] | 9/597 = 1.51 % [0.69, 2.84] | no | 51/98 = 52.04 % [41.71, 62.24] | 1/172 = 0.58 % [0.01, 3.20] | 0.5448 | 0.7518 |
| K2 | 359/483 = 74.33 % [70.19, 78.17] | 9/597 = 1.51 % [0.69, 2.84] | no | 12/98 = 12.24 % [6.49, 20.41] | 1/172 = 0.58 % [0.01, 3.20] | 0.4662 | 0.7518 |
| K3 | 358/483 = 74.12 % [69.97, 77.97] | 8/597 = 1.34 % [0.58, 2.62] | no | 11/98 = 11.22 % [5.74, 19.20] | 0/172 = 0.00 % [0.00, 2.12] | 0.4061 | 1.0000 |
| K3+TIPall | 380/483 = 78.67 % [74.75, 82.25] | 100/597 = 16.75 % [13.84, 19.99] | YES | 11/98 = 11.22 % [5.74, 19.20] | 0/172 = 0.00 % [0.00, 2.12] | 0.8243 | 0.9128 |
| K3+TIPfunc | 364/483 = 75.36 % [71.27, 79.14] | 25/597 = 4.19 % [2.73, 6.12] | YES | 11/98 = 11.22 % [5.74, 19.20] | 0/172 = 0.00 % [0.00, 2.12] | 0.6730 | 0.4143 |
| K3+TIPfunc+adv | 364/483 = 75.36 % [71.27, 79.14] | 25/597 = 4.19 % [2.73, 6.12] | YES | 11/98 = 11.22 % [5.74, 19.20] | 0/172 = 0.00 % [0.00, 2.12] | 0.6730 | 0.4143 |

| config | FA T | FA W | FA M | FA S | false rejections by layer |
| --- | --- | --- | --- | --- | --- |
| K0 | 3/224 = 1.34 % [0.28, 3.86] | 1/127 = 0.79 % [0.02, 4.31] | 11/126 = 8.73 % [4.44, 15.08] | 4/120 = 3.33 % [0.92, 8.31] | L3 30, L3:TIPrej 22, F5 4, F2B 2 |
| K1 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 2/126 = 1.59 % [0.19, 5.62] | 4/120 = 3.33 % [0.92, 8.31] | L3 52, L3:TIPrej 24, F5 4, F2B 2 |
| K2 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 2/126 = 1.59 % [0.19, 5.62] | 4/120 = 3.33 % [0.92, 8.31] | AG 81, L3:TIPrej 22, L3 15, F5 4, F2B 2 |
| K3 | 1/224 = 0.45 % [0.01, 2.46] | 1/127 = 0.79 % [0.02, 4.31] | 2/126 = 1.59 % [0.19, 5.62] | 4/120 = 3.33 % [0.92, 8.31] | AG 82, L3:TIPrej 22, L3 15, F5 4, F2B 2 |
| K3+TIPall | 6/224 = 2.68 % [0.99, 5.74] | 1/127 = 0.79 % [0.02, 4.31] | 19/126 = 15.08 % [9.33, 22.54] | 74/120 = 61.67 % [52.35, 70.39] | AG 82, L3 15, F5 4, F2B 2 |
| K3+TIPfunc | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 2/126 = 1.59 % [0.19, 5.62] | 20/120 = 16.67 % [10.49, 24.56] | AG 82, L3:TIPrej 16, L3 15, F5 4, F2B 2 |
| K3+TIPfunc+adv | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 2/126 = 1.59 % [0.19, 5.62] | 20/120 = 16.67 % [10.49, 24.56] | AG 82, L3:TIPrej 16, L3 15, F5 4, F2B 2 |

## label set S2

| config | coverage | FA | FA crosses 5 % | agentless cov | agentless FA | P1/P2 cov p | P1/P2 FA p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| K0 | 426/490 = 86.94 % [83.63, 89.79] | 18/590 = 3.05 % [1.82, 4.78] | no | 75/98 = 76.53 % [66.89, 84.50] | 11/172 = 6.40 % [3.24, 11.15] | 0.7892 | 0.8117 |
| K1 | 402/490 = 82.04 % [78.35, 85.34] | 8/590 = 1.36 % [0.59, 2.65] | no | 51/98 = 52.04 % [41.71, 62.24] | 1/172 = 0.58 % [0.01, 3.20] | 0.8141 | 0.7247 |
| K2 | 360/490 = 73.47 % [69.32, 77.33] | 8/590 = 1.36 % [0.59, 2.65] | no | 12/98 = 12.24 % [6.49, 20.41] | 1/172 = 0.58 % [0.01, 3.20] | 0.6106 | 0.7247 |
| K3 | 359/490 = 73.27 % [69.11, 77.14] | 7/590 = 1.19 % [0.48, 2.43] | no | 11/98 = 11.22 % [5.74, 19.20] | 0/172 = 0.00 % [0.00, 2.12] | 0.5421 | 1.0000 |
| K3+TIPall | 381/490 = 77.76 % [73.81, 81.36] | 99/590 = 16.78 % [13.85, 20.04] | YES | 11/98 = 11.22 % [5.74, 19.20] | 0/172 = 0.00 % [0.00, 2.12] | 1.0000 | 0.9124 |
| K3+TIPfunc | 365/490 = 74.49 % [70.39, 78.29] | 24/590 = 4.07 % [2.62, 5.99] | YES | 11/98 = 11.22 % [5.74, 19.20] | 0/172 = 0.00 % [0.00, 2.12] | 0.8367 | 0.4120 |
| K3+TIPfunc+adv | 365/490 = 74.49 % [70.39, 78.29] | 24/590 = 4.07 % [2.62, 5.99] | YES | 11/98 = 11.22 % [5.74, 19.20] | 0/172 = 0.00 % [0.00, 2.12] | 0.8367 | 0.4120 |

| config | FA T | FA W | FA M | FA S | false rejections by layer |
| --- | --- | --- | --- | --- | --- |
| K0 | 3/224 = 1.34 % [0.28, 3.86] | 1/127 = 0.79 % [0.02, 4.31] | 10/119 = 8.40 % [4.10, 14.91] | 4/120 = 3.33 % [0.92, 8.31] | L3 30, L3:TIPrej 22, F5 8, F2B 3, F3 1 |
| K1 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 1/119 = 0.84 % [0.02, 4.59] | 4/120 = 3.33 % [0.92, 8.31] | L3 52, L3:TIPrej 24, F5 8, F2B 3, F3 1 |
| K2 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 1/119 = 0.84 % [0.02, 4.59] | 4/120 = 3.33 % [0.92, 8.31] | AG 81, L3:TIPrej 22, L3 15, F5 8, F2B 3, F3 1 |
| K3 | 1/224 = 0.45 % [0.01, 2.46] | 1/127 = 0.79 % [0.02, 4.31] | 1/119 = 0.84 % [0.02, 4.59] | 4/120 = 3.33 % [0.92, 8.31] | AG 82, L3:TIPrej 22, L3 15, F5 8, F2B 3, F3 1 |
| K3+TIPall | 6/224 = 2.68 % [0.99, 5.74] | 1/127 = 0.79 % [0.02, 4.31] | 18/119 = 15.13 % [9.22, 22.85] | 74/120 = 61.67 % [52.35, 70.39] | AG 82, L3 15, F5 8, F2B 3, F3 1 |
| K3+TIPfunc | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 1/119 = 0.84 % [0.02, 4.59] | 20/120 = 16.67 % [10.49, 24.56] | AG 82, L3:TIPrej 16, L3 15, F5 8, F2B 3, F3 1 |
| K3+TIPfunc+adv | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 1/119 = 0.84 % [0.02, 4.59] | 20/120 = 16.67 % [10.49, 24.56] | AG 82, L3:TIPrej 16, L3 15, F5 8, F2B 3, F3 1 |

## label set RDET (CIRCULAR)

| config | coverage | FA | FA crosses 5 % | agentless cov | agentless FA | P1/P2 cov p | P1/P2 FA p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| K0 | 359/401 = 89.53 % [86.11, 92.35] | 85/679 = 12.52 % [10.12, 15.25] | YES | 12/19 = 63.16 % [38.36, 83.71] | 74/251 = 29.48 % [23.91, 35.54] | 0.7448 | 0.6447 |
| K1 | 358/401 = 89.28 % [85.83, 92.13] | 52/679 = 7.66 % [5.77, 9.92] | YES | 11/19 = 57.89 % [33.50, 79.75] | 41/251 = 16.33 % [11.98, 21.50] | 0.8721 | 0.6664 |
| K2 | 358/401 = 89.28 % [85.83, 92.13] | 10/679 = 1.47 % [0.71, 2.69] | no | 11/19 = 57.89 % [33.50, 79.75] | 2/251 = 0.80 % [0.10, 2.85] | 0.8721 | 0.7522 |
| K3 | 358/401 = 89.28 % [85.83, 92.13] | 8/679 = 1.18 % [0.51, 2.31] | no | 11/19 = 57.89 % [33.50, 79.75] | 0/251 = 0.00 % [0.00, 1.46] | 0.8721 | 1.0000 |
| K3+TIPall | 380/401 = 94.76 % [92.11, 96.73] | 100/679 = 14.73 % [12.15, 17.62] | YES | 11/19 = 57.89 % [33.50, 79.75] | 0/251 = 0.00 % [0.00, 1.46] | 0.3720 | 0.7467 |
| K3+TIPfunc | 364/401 = 90.77 % [87.51, 93.42] | 25/679 = 3.68 % [2.40, 5.39] | YES | 11/19 = 57.89 % [33.50, 79.75] | 0/251 = 0.00 % [0.00, 1.46] | 0.7321 | 0.3136 |
| K3+TIPfunc+adv | 364/401 = 90.77 % [87.51, 93.42] | 25/679 = 3.68 % [2.40, 5.39] | YES | 11/19 = 57.89 % [33.50, 79.75] | 0/251 = 0.00 % [0.00, 1.46] | 0.7321 | 0.3136 |

| config | FA T | FA W | FA M | FA S | false rejections by layer |
| --- | --- | --- | --- | --- | --- |
| K0 | 3/224 = 1.34 % [0.28, 3.86] | 1/127 = 0.79 % [0.02, 4.31] | 77/208 = 37.02 % [30.44, 43.97] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 14, F5 4, F2B 2 |
| K1 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 45/208 = 21.63 % [16.24, 27.86] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 15, F5 4, F2B 2 |
| K2 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 3/208 = 1.44 % [0.30, 4.16] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 15, F5 4, F2B 2 |
| K3 | 1/224 = 0.45 % [0.01, 2.46] | 1/127 = 0.79 % [0.02, 4.31] | 2/208 = 0.96 % [0.12, 3.43] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 15, F5 4, F2B 2 |
| K3+TIPall | 6/224 = 2.68 % [0.99, 5.74] | 1/127 = 0.79 % [0.02, 4.31] | 19/208 = 9.13 % [5.59, 13.90] | 74/120 = 61.67 % [52.35, 70.39] | L3 15, F5 4, F2B 2 |
| K3+TIPfunc | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 2/208 = 0.96 % [0.12, 3.43] | 20/120 = 16.67 % [10.49, 24.56] | L3:TIPrej 16, L3 15, F5 4, F2B 2 |
| K3+TIPfunc+adv | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 2/208 = 0.96 % [0.12, 3.43] | 20/120 = 16.67 % [10.49, 24.56] | L3:TIPrej 16, L3 15, F5 4, F2B 2 |

## label set RDET+S2 (CIRCULAR)

| config | coverage | FA | FA crosses 5 % | agentless cov | agentless FA | P1/P2 cov p | P1/P2 FA p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| K0 | 360/408 = 88.24 % [84.71, 91.20] | 84/672 = 12.50 % [10.09, 15.24] | YES | 12/19 = 63.16 % [38.36, 83.71] | 74/251 = 29.48 % [23.91, 35.54] | 1.0000 | 0.6416 |
| K1 | 359/408 = 87.99 % [84.43, 90.98] | 51/672 = 7.59 % [5.70, 9.86] | YES | 11/19 = 57.89 % [33.50, 79.75] | 41/251 = 16.33 % [11.98, 21.50] | 0.8794 | 0.5640 |
| K2 | 359/408 = 87.99 % [84.43, 90.98] | 9/672 = 1.34 % [0.61, 2.53] | no | 11/19 = 57.89 % [33.50, 79.75] | 2/251 = 0.80 % [0.10, 2.85] | 0.8794 | 0.5055 |
| K3 | 359/408 = 87.99 % [84.43, 90.98] | 7/672 = 1.04 % [0.42, 2.13] | no | 11/19 = 57.89 % [33.50, 79.75] | 0/251 = 0.00 % [0.00, 1.46] | 0.8794 | 1.0000 |
| K3+TIPall | 381/408 = 93.38 % [90.52, 95.59] | 99/672 = 14.73 % [12.14, 17.64] | YES | 11/19 = 57.89 % [33.50, 79.75] | 0/251 = 0.00 % [0.00, 1.46] | 0.1141 | 0.8278 |
| K3+TIPfunc | 365/408 = 89.46 % [86.07, 92.27] | 24/672 = 3.57 % [2.30, 5.27] | YES | 11/19 = 57.89 % [33.50, 79.75] | 0/251 = 0.00 % [0.00, 1.46] | 0.4207 | 0.4093 |
| K3+TIPfunc+adv | 365/408 = 89.46 % [86.07, 92.27] | 24/672 = 3.57 % [2.30, 5.27] | YES | 11/19 = 57.89 % [33.50, 79.75] | 0/251 = 0.00 % [0.00, 1.46] | 0.4207 | 0.4093 |

| config | FA T | FA W | FA M | FA S | false rejections by layer |
| --- | --- | --- | --- | --- | --- |
| K0 | 3/224 = 1.34 % [0.28, 3.86] | 1/127 = 0.79 % [0.02, 4.31] | 76/201 = 37.81 % [31.08, 44.90] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 14, F5 8, F2B 3, F3 1 |
| K1 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 44/201 = 21.89 % [16.38, 28.25] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 15, F5 8, F2B 3, F3 1 |
| K2 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 2/201 = 1.00 % [0.12, 3.55] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 15, F5 8, F2B 3, F3 1 |
| K3 | 1/224 = 0.45 % [0.01, 2.46] | 1/127 = 0.79 % [0.02, 4.31] | 1/201 = 0.50 % [0.01, 2.74] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 15, F5 8, F2B 3, F3 1 |
| K3+TIPall | 6/224 = 2.68 % [0.99, 5.74] | 1/127 = 0.79 % [0.02, 4.31] | 18/201 = 8.96 % [5.39, 13.78] | 74/120 = 61.67 % [52.35, 70.39] | L3 15, F5 8, F2B 3, F3 1 |
| K3+TIPfunc | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 1/201 = 0.50 % [0.01, 2.74] | 20/120 = 16.67 % [10.49, 24.56] | L3:TIPrej 16, L3 15, F5 8, F2B 3, F3 1 |
| K3+TIPfunc+adv | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 1/201 = 0.50 % [0.01, 2.74] | 20/120 = 16.67 % [10.49, 24.56] | L3:TIPrej 16, L3 15, F5 8, F2B 3, F3 1 |

## label set RUL

| config | coverage | FA | FA crosses 5 % | agentless cov | agentless FA | P1/P2 cov p | P1/P2 FA p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| K0 | 351/385 = 91.17 % [87.88, 93.81] | 93/695 = 13.38 % [10.94, 16.14] | YES | 1/1 = 100.00 % [2.50, 100.00] | 85/269 = 31.60 % [26.09, 37.52] | 0.7234 | 0.9118 |
| K1 | 351/385 = 91.17 % [87.88, 93.81] | 59/695 = 8.49 % [6.53, 10.81] | YES | 1/1 = 100.00 % [2.50, 100.00] | 51/269 = 18.96 % [14.45, 24.16] | 0.7234 | 0.8927 |
| K2 | 348/385 = 90.39 % [87.00, 93.14] | 20/695 = 2.88 % [1.77, 4.41] | no | 1/1 = 100.00 % [2.50, 100.00] | 12/269 = 4.46 % [2.33, 7.66] | 0.3932 | 1.0000 |
| K3 | 348/385 = 90.39 % [87.00, 93.14] | 18/695 = 2.59 % [1.54, 4.06] | no | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] | 0.3932 | 0.6430 |
| K3+TIPall | 370/385 = 96.10 % [93.66, 97.80] | 110/695 = 15.83 % [13.19, 18.76] | YES | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] | 1.0000 | 0.6789 |
| K3+TIPfunc | 354/385 = 91.95 % [88.77, 94.46] | 35/695 = 5.04 % [3.53, 6.93] | YES | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] | 0.8539 | 0.2305 |
| K3+TIPfunc+adv | 354/385 = 91.95 % [88.77, 94.46] | 35/695 = 5.04 % [3.53, 6.93] | YES | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] | 0.8539 | 0.2305 |

| config | FA T | FA W | FA M | FA S | false rejections by layer |
| --- | --- | --- | --- | --- | --- |
| K0 | 3/224 = 1.34 % [0.28, 3.86] | 1/127 = 0.79 % [0.02, 4.31] | 85/224 = 37.95 % [31.57, 44.65] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 7, F5 3, F2B 2 |
| K1 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 52/224 = 23.21 % [17.85, 29.30] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 7, F5 3, F2B 2 |
| K2 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 13/224 = 5.80 % [3.13, 9.72] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 7, F5 3, AG 3, F2B 2 |
| K3 | 1/224 = 0.45 % [0.01, 2.46] | 1/127 = 0.79 % [0.02, 4.31] | 12/224 = 5.36 % [2.80, 9.17] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 7, F5 3, AG 3, F2B 2 |
| K3+TIPall | 6/224 = 2.68 % [0.99, 5.74] | 1/127 = 0.79 % [0.02, 4.31] | 29/224 = 12.95 % [8.84, 18.06] | 74/120 = 61.67 % [52.35, 70.39] | L3 7, F5 3, AG 3, F2B 2 |
| K3+TIPfunc | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 12/224 = 5.36 % [2.80, 9.17] | 20/120 = 16.67 % [10.49, 24.56] | L3:TIPrej 16, L3 7, F5 3, AG 3, F2B 2 |
| K3+TIPfunc+adv | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 12/224 = 5.36 % [2.80, 9.17] | 20/120 = 16.67 % [10.49, 24.56] | L3:TIPrej 16, L3 7, F5 3, AG 3, F2B 2 |

## label set RUL+S2

| config | coverage | FA | FA crosses 5 % | agentless cov | agentless FA | P1/P2 cov p | P1/P2 FA p |
| --- | --- | --- | --- | --- | --- | --- | --- |
| K0 | 352/392 = 89.80 % [86.36, 92.61] | 92/688 = 13.37 % [10.92, 16.15] | YES | 1/1 = 100.00 % [2.50, 100.00] | 85/269 = 31.60 % [26.09, 37.52] | 0.8684 | 1.0000 |
| K1 | 352/392 = 89.80 % [86.36, 92.61] | 58/688 = 8.43 % [6.46, 10.76] | YES | 1/1 = 100.00 % [2.50, 100.00] | 51/269 = 18.96 % [14.45, 24.16] | 0.8684 | 1.0000 |
| K2 | 349/392 = 89.03 % [85.51, 91.95] | 19/688 = 2.76 % [1.67, 4.28] | no | 1/1 = 100.00 % [2.50, 100.00] | 12/269 = 4.46 % [2.33, 7.66] | 0.8720 | 1.0000 |
| K3 | 349/392 = 89.03 % [85.51, 91.95] | 17/688 = 2.47 % [1.45, 3.93] | no | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] | 0.8720 | 0.8108 |
| K3+TIPall | 371/392 = 94.64 % [91.93, 96.65] | 109/688 = 15.84 % [13.19, 18.79] | YES | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] | 0.3713 | 0.7542 |
| K3+TIPfunc | 355/392 = 90.56 % [87.22, 93.27] | 34/688 = 4.94 % [3.45, 6.84] | YES | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] | 0.7314 | 0.2948 |
| K3+TIPfunc+adv | 355/392 = 90.56 % [87.22, 93.27] | 34/688 = 4.94 % [3.45, 6.84] | YES | 1/1 = 100.00 % [2.50, 100.00] | 10/269 = 3.72 % [1.80, 6.73] | 0.7314 | 0.2948 |

| config | FA T | FA W | FA M | FA S | false rejections by layer |
| --- | --- | --- | --- | --- | --- |
| K0 | 3/224 = 1.34 % [0.28, 3.86] | 1/127 = 0.79 % [0.02, 4.31] | 84/217 = 38.71 % [32.19, 45.54] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 7, F5 7, F2B 3, F3 1 |
| K1 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 51/217 = 23.50 % [18.03, 29.72] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 7, F5 7, F2B 3, F3 1 |
| K2 | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 12/217 = 5.53 % [2.89, 9.46] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 7, F5 7, F2B 3, AG 3, F3 1 |
| K3 | 1/224 = 0.45 % [0.01, 2.46] | 1/127 = 0.79 % [0.02, 4.31] | 11/217 = 5.07 % [2.56, 8.89] | 4/120 = 3.33 % [0.92, 8.31] | L3:TIPrej 22, L3 7, F5 7, F2B 3, AG 3, F3 1 |
| K3+TIPall | 6/224 = 2.68 % [0.99, 5.74] | 1/127 = 0.79 % [0.02, 4.31] | 28/217 = 12.90 % [8.75, 18.11] | 74/120 = 61.67 % [52.35, 70.39] | L3 7, F5 7, F2B 3, AG 3, F3 1 |
| K3+TIPfunc | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 11/217 = 5.07 % [2.56, 8.89] | 20/120 = 16.67 % [10.49, 24.56] | L3:TIPrej 16, L3 7, F5 7, F2B 3, AG 3, F3 1 |
| K3+TIPfunc+adv | 2/224 = 0.89 % [0.11, 3.19] | 1/127 = 0.79 % [0.02, 4.31] | 11/217 = 5.07 % [2.56, 8.89] | 20/120 = 16.67 % [10.49, 24.56] | L3:TIPrej 16, L3 7, F5 7, F2B 3, AG 3, F3 1 |

## TIP variants

| variant | TIPrej rows | accepted | label set | accepted correct | accepted wrong (FA) |
| --- | --- | --- | --- | --- | --- |
| K3+TIPall | 114 | 114 | 1R | 22 | 92 |
| K3+TIPall | 114 | 114 | S2 | 22 | 92 |
| K3+TIPall | 114 | 114 | RDET (CIRCULAR) | 22 | 92 |
| K3+TIPall | 114 | 114 | RDET+S2 (CIRCULAR) | 22 | 92 |
| K3+TIPall | 114 | 114 | RUL | 22 | 92 |
| K3+TIPall | 114 | 114 | RUL+S2 | 22 | 92 |
| K3+TIPfunc | 114 | 23 | 1R | 6 | 17 |
| K3+TIPfunc | 114 | 23 | S2 | 6 | 17 |
| K3+TIPfunc | 114 | 23 | RDET (CIRCULAR) | 6 | 17 |
| K3+TIPfunc | 114 | 23 | RDET+S2 (CIRCULAR) | 6 | 17 |
| K3+TIPfunc | 114 | 23 | RUL | 6 | 17 |
| K3+TIPfunc | 114 | 23 | RUL+S2 | 6 | 17 |
| K3+TIPfunc+adv | 114 | 23 | 1R | 6 | 17 |
| K3+TIPfunc+adv | 114 | 23 | S2 | 6 | 17 |
| K3+TIPfunc+adv | 114 | 23 | RDET (CIRCULAR) | 6 | 17 |
| K3+TIPfunc+adv | 114 | 23 | RDET+S2 (CIRCULAR) | 6 | 17 |
| K3+TIPfunc+adv | 114 | 23 | RUL | 6 | 17 |
| K3+TIPfunc+adv | 114 | 23 | RUL+S2 | 6 | 17 |

### wrong rows let in (label set 1R)

| variant | iid | answer | difference |
| --- | --- | --- | --- |
| K3+TIPall | W:170002:w4 | She baked a apple pie for the neighbours yesterday. |  |
| K3+TIPall | W:170004:w3 | The teacher is correcting our tests now. | classroom correcting in marking |
| K3+TIPall | W:170004:w4 | The teacher is correcting our tests on the classroom now. | correcting in marking on |
| K3+TIPall | W:170005:w4 | I go to the park with my friend every Sundays. | every sunday sundays |
| K3+TIPall | W:170007:w4 | She make tea for the whole family every morning. | make makes |
| K3+TIPall | W:170009:w4 | The children drawed a big picture on the pavement yesterday. | drawed drew yesterday |
| K3+TIPall | W:170010:w4 | He run around the lake every day. | run runs |
| K3+TIPall | W:170011:w4 | The neighbour repaired my bike in garage. |  |
| K3+TIPall | W:170013:w4 | Mum will buys bread at the new bakery tomorrow. | buy buys tomorrow |
| K3+TIPall | W:170015:w4 | We live in small flat above a café. | caf cafe |
| K3+TIPall | W:170017:w4 | The boy is carrying a heavy bag up the stair. | stair stairs |
| K3+TIPall | W:170019:w4 | Jana drinked a whole glass of milk. | drank drinked |
| K3+TIPall | W:170021:w4 | My grandfather grow tomatoes in the greenhouse. | grow grows |
| K3+TIPall | W:170024:w3 | The hungry dog quickly ate my whole dinner off the kitchen table. | hungry kitchen quickly whole |
| K3+TIPall | W:170026:w4 | My sister is photographing the flowers in garden. |  |
| K3+TIPall | W:170027:w4 | They built a new bridge over river. |  |
| K3+TIPall | W:170028:w3 | I will bring a cake tomorrow. | school to tomorrow |
| K3+TIPall | W:170028:w4 | I will brings a cake to school tomorrow. | bring brings tomorrow |
| K3+TIPall | W:170031:w4 | My colleague translated the whole document in English yesterday. | in into yesterday |
| K3+TIPall | W:170032:w4 | She pay the rent for that small flat every month. | pay pays |
| K3+TIPall | W:170035:w4 | My parents lives in an old house on a hill. | live lives |
| K3+TIPall | W:170037:w3 | She will hand in her term paper tomorrow. | professor to tomorrow |
| K3+TIPall | W:170038:w4 | A thief stealed the neighbour's bike from the yard last night. | last night stealed stole |
| K3+TIPall | W:170039:w4 | The cook is preparing lunch for thirty guest. | guest guests |
| K3+TIPall | W:170042:w4 | The technician will replace the broken washing machine in bathroom tomorrow. | tomorrow |
| K3+TIPall | W:170044:w3 | The students studied three books last semester. | last semester thick |
| K3+TIPall | W:170044:w4 | The students studied three thick book last semester. | book books last semester |
| K3+TIPall | W:170045:w3 | I sat at the doctor's all afternoon. | at in room waiting |
| K3+TIPall | W:170046:w3 | The company will open a new branch next month. | in kosice month next |
| K3+TIPall | W:170046:w4 | The company will open a new branch in Košice next months. | ice ko kosice month months next |
| K3+TIPall | W:170047:w3 | He cleans his shoes every morning. | before every for leaving morning work |
| K3+TIPall | W:170047:w4 | He cleans his shoes every morning before leave for work. | every leave leaving morning |
| K3+TIPall | W:170048:w4 | The gardener mowed the lawn in front our house. | of |
| K3+TIPall | W:170049:w4 | She will invite the whole family on lunch tomorrow. | on to tomorrow |
| K3+TIPall | W:170050:w4 | Our cat sleep all day on an old armchair. | in on sleep sleeps |
| K3+TIPall | W:170052:w4 | The postman delivered the parcel only in Friday afternoon. | delivered in on parcel that |
| K3+TIPall | W:170053:w3 | I will pay the electricity bill tomorrow. | online tomorrow |
| K3+TIPall | W:170054:w3 | Yesterday she bought a beautiful new winter coat on sale. | beautiful herself winter yesterday |
| K3+TIPall | W:170056:w4 | The neighbours will build a small pool behind the house next years. | next swimming year years |
| K3+TIPall | W:170058:w4 | Our school organise a trip to the capital every spring. | organise organises |
| K3+TIPall | W:170059:w3 | You left your mobile phone in the kitchen. | in on phone table |
| K3+TIPall | W:170060:w4 | They will come to our new cottage on next Saturday. | next on saturday |
| K3+TIPall | W:170063:w1 | If it doesn't stop raining tomorrow, the coach cancels the whole match. | cancel cancels does doesn't not will |
| K3+TIPall | W:170063:w5 | If it doesn't stop raining tomorrow, the coach will cancel whole match. | does doesn't not |
| K3+TIPall | W:170064:w4 | When the phone rang, he was chopping onions. | chopping cutting dinner for just |
| K3+TIPall | W:170064:w5 | When the phone rang, he were just chopping onions for dinner. | chopping cutting was were |
| K3+TIPall | W:170065:w5 | You should to go to bed earlier, because you can hardly get up in the morning. | to |
| K3+TIPall | W:170067:w5 | Next month they will open new branch on the main street. |  |
| K3+TIPall | W:170068:w5 | The neighbour's son broke our kitchen window with football. |  |
| K3+TIPall | W:170071:w2 | When she gets back from Vienna, she brings us the photos from the exhibition. | bring brings comes gets those will |
| K3+TIPall | W:170071:w4 | When she gets back, she will bring us the photos from the exhibition. | comes from gets those vienna |
| K3+TIPall | W:170071:w5 | When she gets back from Vienna, she will bring us the photos of exhibition. | comes from gets of those |
| K3+TIPall | W:170072:w5 | Last year the neighbours replaced the old windows with new one. | one ones |
| K3+TIPall | W:170075:w4 | If you keep going at this pace, you will be exhausted. | by carry completely going keep on spring |
| K3+TIPall | W:170075:w5 | If you will keep going at this pace, you will be completely exhausted by spring. | carry going keep on will |
| K3+TIPall | W:170076:w4 | They lock the gate to the courtyard every evening. | at courtyard ten to yard |
| K3+TIPall | W:170076:w5 | They locks the gate to the courtyard at ten every evening. | courtyard lock locks to yard |
| K3+TIPall | W:170077:w5 | Tomorrow I will take those books to library by bike. |  |
| K3+TIPall | W:170079:w5 | Most students hands in those essays at the last minute. | hand hands |
| K3+TIPall | W:170080:w5 | Last year we moved to a more small flat near the park. | by more near small smaller |
| K3+TIPall | W:170081:w5 | If Marek will get that job, he will buy his parents a new washing machine. | get gets will |
| K3+TIPall | W:170082:w5 | The technician replaced the battery in my laptop in twenty minute. | minute minutes |
| K3+TIPall | W:170083:w5 | The coach claim that the younger players handle the training better than last year. | claim says that |
| K3+TIPall | W:170084:w5 | A policeman stopped our car just past the bridge and checked the document. | after document documents past |
| K3+TIPall | W:170085:w4 | She has been studying for her driving test for a month. | about and her is it nervous quite she |
| K3+TIPall | W:170085:w5 | She has been studying for her driving test since a month and she is quite nervous about it. | for her since |
| K3+TIPall | W:170088:w5 | The library lend these textbooks for one semester only. | lend lends |
| K3+TIPall | W:170089:w5 | You must to hand in that certificate by the end of the week. | that to |
| K3+TIPall | W:170090:w5 | Last winter the main water pipe broke in our village and there was no water for two day. | broke day days |
| K3+TIPall | W:170091:w5 | If Lucia would have read the instructions, she would not have ruined the whole spreadsheet. | had have spreadsheet table would |
| K3+TIPall | W:170092:w5 | Someone has obviously swapped those labels, because all the boxes is mixed up. | are is those |
| K3+TIPall | W:170093:w5 | It is said that the city is preparing a new parking rules in the centre. | for in |
| K3+TIPall | W:170094:w5 | The customer claimed that she had sended the complaint already on Monday. | complaint sended sent |
| K3+TIPall | W:170095:w2 | If the situation does not improve, we have to stay at home for another two weeks. | will |
| K3+TIPall | W:170095:w5 | If the situation will not improve, we will have to stay at home for another two weeks. | does will |
| K3+TIPall | W:170097:w5 | Although the company promise fast delivery, customers waits up to three weeks for their orders. | promise promises wait waits |
| K3+TIPall | W:170098:w5 | By the end of the year the team will have finish the second stage of the bridge reconstruction. | finish finished |
| K3+TIPall | W:170099:w5 | The boss regrets that he cancelled that cooperation with German partner last year. |  |
| K3+TIPall | W:170101:w5 | If the committee will approve the budget, the city will renovate the playgrounds as early as spring. | approve approves children's in will |
| K3+TIPall | W:170102:w4 | The translator delivered the finished text a day early. | colleagues earlier early recommended that to us |
| K3+TIPall | W:170102:w5 | The translator, which our colleagues recommended to us, delivered the finished text a day early. | delivered handed in which whom |
| K3+TIPall | W:170103:w2 | The editorial team will always publish corrections of mistakes at the end of the month. | mistakes of office publish publishes team will |
| K3+TIPall | W:170103:w5 | The editorial team publish corrections of mistakes always at the end of the month. | corrections mistakes of office publish publishes team |
| K3+TIPall | W:170104:w5 | While we was waiting for the verdict, the lawyer was preparing the appeal for several days. | was were |
| K3+TIPall | W:170106:w2 | The company management lays off ten employees before the end of the year. | lay lays will |
| K3+TIPall | W:170106:w5 | The company management will lay off ten employee before the end of the year. | employee employees |
| K3+TIPall | W:170109:w5 | As soon as the committee will evaluate the applications, the organisers will send the results to the applicants. | evaluate evaluates will |
| K3+TIPall | W:170110:w5 | At that time we did not even realised how much that change had helped us. | realise realised that |
| K3+TIPall | W:170112:w5 | The curator moved the most valuables paintings to the next room before the opening. | valuable valuables |
| K3+TIPall | W:170116:w5 | It is this insurance company who also cover damage caused by wind. | cover covers that who |
| K3+TIPall | W:170119:w5 | Many schools today is replacing printed textbook with tablets. | are is textbook textbooks |
| K3+TIPall | W:170120:w5 | Last week the storm damaged the roof of the gym and uprooted two tree. | tree trees |
| K3+TIPfunc | W:170002:w4 | She baked a apple pie for the neighbours yesterday. |  |
| K3+TIPfunc | W:170011:w4 | The neighbour repaired my bike in garage. |  |
| K3+TIPfunc | W:170026:w4 | My sister is photographing the flowers in garden. |  |
| K3+TIPfunc | W:170027:w4 | They built a new bridge over river. |  |
| K3+TIPfunc | W:170048:w4 | The gardener mowed the lawn in front our house. | of |
| K3+TIPfunc | W:170065:w5 | You should to go to bed earlier, because you can hardly get up in the morning. | to |
| K3+TIPfunc | W:170067:w5 | Next month they will open new branch on the main street. |  |
| K3+TIPfunc | W:170068:w5 | The neighbour's son broke our kitchen window with football. |  |
| K3+TIPfunc | W:170077:w5 | Tomorrow I will take those books to library by bike. |  |
| K3+TIPfunc | W:170085:w5 | She has been studying for her driving test since a month and she is quite nervous about it. | for her since |
| K3+TIPfunc | W:170089:w5 | You must to hand in that certificate by the end of the week. | that to |
| K3+TIPfunc | W:170092:w5 | Someone has obviously swapped those labels, because all the boxes is mixed up. | are is those |
| K3+TIPfunc | W:170093:w5 | It is said that the city is preparing a new parking rules in the centre. | for in |
| K3+TIPfunc | W:170095:w2 | If the situation does not improve, we have to stay at home for another two weeks. | will |
| K3+TIPfunc | W:170095:w5 | If the situation will not improve, we will have to stay at home for another two weeks. | does will |
| K3+TIPfunc | W:170099:w5 | The boss regrets that he cancelled that cooperation with German partner last year. |  |
| K3+TIPfunc | W:170104:w5 | While we was waiting for the verdict, the lawyer was preparing the appeal for several days. | was were |
| K3+TIPfunc+adv | W:170002:w4 | She baked a apple pie for the neighbours yesterday. |  |
| K3+TIPfunc+adv | W:170011:w4 | The neighbour repaired my bike in garage. |  |
| K3+TIPfunc+adv | W:170026:w4 | My sister is photographing the flowers in garden. |  |
| K3+TIPfunc+adv | W:170027:w4 | They built a new bridge over river. |  |
| K3+TIPfunc+adv | W:170048:w4 | The gardener mowed the lawn in front our house. | of |
| K3+TIPfunc+adv | W:170065:w5 | You should to go to bed earlier, because you can hardly get up in the morning. | to |
| K3+TIPfunc+adv | W:170067:w5 | Next month they will open new branch on the main street. |  |
| K3+TIPfunc+adv | W:170068:w5 | The neighbour's son broke our kitchen window with football. |  |
| K3+TIPfunc+adv | W:170077:w5 | Tomorrow I will take those books to library by bike. |  |
| K3+TIPfunc+adv | W:170085:w5 | She has been studying for her driving test since a month and she is quite nervous about it. | for her since |
| K3+TIPfunc+adv | W:170089:w5 | You must to hand in that certificate by the end of the week. | that to |
| K3+TIPfunc+adv | W:170092:w5 | Someone has obviously swapped those labels, because all the boxes is mixed up. | are is those |
| K3+TIPfunc+adv | W:170093:w5 | It is said that the city is preparing a new parking rules in the centre. | for in |
| K3+TIPfunc+adv | W:170095:w2 | If the situation does not improve, we have to stay at home for another two weeks. | will |
| K3+TIPfunc+adv | W:170095:w5 | If the situation will not improve, we will have to stay at home for another two weeks. | does will |
| K3+TIPfunc+adv | W:170099:w5 | The boss regrets that he cancelled that cooperation with German partner last year. |  |
| K3+TIPfunc+adv | W:170104:w5 | While we was waiting for the verdict, the lawyer was preparing the appeal for several days. | was were |
