## A3 FINAL (stage S2) — CLOSED-SET RE-SCORE (2I set, 900 items; 2I stored L3 replies by request hash + the new S2 calls)

Run: phase2j/run_S2 via run_2j.py (fixed TRANSLATION-ONLY stack, S2 hook fix): 843 L3 requests, 800 answered by stored 2I replies (0 cost), 43 new, 43 calls made (counted 43, uncounted 0), $0.005675.

| | coverage | FA |
|---|---|---|
| 2I (before) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |
| A2 fix (after) | 443/497 = 89.13 % [86.06, 91.73] | 19/403 = 4.71 % [2.86, 7.26] |

Catches (judge-correct, F4v2 before, now accepted): 0; judge-correct now rejected by L3: 24. Cost (judge-wrong, F4v2 before, now accepted): 0; judge-wrong still rejected (by L3): 20. Items changed outside the 44: 0. Of the 44, still F4v2: 0.

Every item whose verdict changed (layer or accept):

| jid | judge | type | before | after | L3 | answer |
|---|---|---|---|---|---|---|
| A:1038:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | My friend said that the bracelet was too loose, so she adjusted it. |
| A:1038:c2 | correct |  | F4v2 rej | F4v3 rej | SAME | The friend said the bracelet was too loose, so she adjusted it. |
| A:1038:c3 | correct |  | F4v2 rej | F4v3 rej | TIP | My friend said the bracelet is too loose, so she fixed it. |
| A:1038:c4 | correct |  | F4v2 rej | L3 rej | DIFF | My friend told me that the bracelet was too loose, so she altered it. |
| A:1038:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | The friend said that the bracelet was too loose, and so she adjusted it. |
| A:1038:m | wrong |  | F4v2 rej | L3 rej | DIFF | My friend said that it was too loose, so she adjusted it. |
| A:1038:s | wrong |  | F4v2 rej | L3 rej | DIFF | My friend said that the bracelet was too loose, so she adjust it. |
| A:1038:t | wrong |  | F4v2 rej | L3 rej | DIFF | My friend says that the bracelet is too loose, so she will adjust it. |
| A:1038:w | wrong |  | F4v2 rej | L3 rej | DIFF | My friend said that the necklace was too loose, so she adjusted it. |
| A:1214:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | He said that the training had been the hardest of his whole life! Pure agony! |
| A:1214:c2 | correct |  | F4v2 rej | F4v3 rej | SAME | He said the training was the toughest in his entire life! Pure agony! |
| A:1214:c3 | correct |  | F4v2 rej | F4v3 rej | SAME | He said that the workout had been the hardest one in his whole life! Sheer agony! |
| A:1214:c4 | correct |  | F4v2 rej | F4v3 rej | SAME | He said the practice was the hardest of his entire life! Total agony! |
| A:1214:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | He told us the training had been the toughest in his whole life! Pure agony! |
| A:1214:m | wrong |  | F4v2 rej | L3 rej | DIFF | He said that the training had been the hardest! Pure agony! |
| A:1214:s | wrong |  | F4v2 rej | F4v3 rej | TIP | He said that the training had been the most hardest in his whole life! Pure agony! |
| A:1214:t | wrong |  | F4v2 rej | L3 rej | DIFF | He says that the training will be the hardest in his whole life! Pure agony! |
| A:1214:w | wrong |  | F4v2 rej | L3 rej | DIFF | He said that the training had been the easiest in his whole life! Pure agony! |
| A:2461:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | Since 2019 he has been photographing planes by this fence. Apparently a very undemanding hobby. |
| A:2461:c2 | correct |  | F4v2 rej | F4v3 rej | SAME | He has been taking pictures of aircraft at this fence since 2019. Clearly a very low-maintenance hobby. |
| A:2461:c3 | correct |  | F4v2 rej | F4v3 rej | SAME | Since 2019, he's been photographing airplanes near this fence. Evidently a very undemanding hobby. |
| A:2461:c4 | correct |  | F4v2 rej | F4v3 rej | SAME | He has photographed planes by this fence since 2019. Apparently a very modest hobby. |
| A:2461:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | Since 2019 he has been taking photos of planes next to this fence. Obviously a very undemanding hobby. |
| A:2461:m | wrong |  | F4v2 rej | F4v3 rej | TIP | Since 2019 he has been photographing planes. Apparently a very undemanding hobby. |
| A:2461:s | wrong |  | F4v2 rej | F4v3 rej | TIP | Since 2019 he is photographing planes by this fence. Apparently a very undemanding hobby. |
| A:2461:t | wrong |  | F4v2 rej | L3 rej | DIFF | Since 2019 he had been photographing planes by this fence. Apparently a very undemanding hobby. |
| A:2461:w | wrong |  | F4v2 rej | L3 rej | DIFF | Since 2019 he has been photographing trains by this fence. Apparently a very undemanding hobby. |
| A:250:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | The vehicle had been racing along the country road before it was parked by the dunes, as was observed. |
| A:250:c3 | correct |  | F4v2 rej | AG rej |  | As was observed, the vehicle had raced along the country road before it was parked by the dunes. |
| A:250:c4 | correct |  | F4v2 rej | F4v3 rej | SAME | The car was speeding along a country road before it was parked next to the dunes, as observed. |
| A:250:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | The vehicle had sped along the country road before it got parked by the dunes, as had been observed. |
| A:250:m | wrong |  | F4v2 rej | F4v3 rej | SAME | The vehicle had been racing along the road before it was parked by the dunes, as was observed. |
| A:250:s | wrong |  | F4v2 rej | L3 rej | DIFF | The vehicle had been race along the country road before it was parked by the dunes, as was observed. |
| A:250:t | wrong |  | F4v2 rej | L3 rej | DIFF | The vehicle is racing along the country road before it is parked by the dunes, as is observed. |
| A:250:w | wrong |  | F4v2 rej | L3 rej | DIFF | The vehicle had been racing along the country road before it was parked by the lake, as was observed. |
| A:2989:c1 | correct |  | F4v2 rej | F4v3 rej | SAME | Of course she had the route drawn on the map in case she forgot her own plan. |
| A:2989:c2 | correct |  | F4v2 rej | F4v3 rej | SAME | Naturally, she had the route marked on the map, just in case she forgot her own plan. |
| A:2989:c3 | correct |  | F4v2 rej | F4v3 rej | SAME | Of course, she got the route drawn onto the map in case she should forget her own plan. |
| A:2989:c4 | correct |  | F4v2 rej | F4v3 rej | SAME | Of course she had someone draw the route on the map, in case she forgot her own plan. |
| A:2989:c5 | correct |  | F4v2 rej | F4v3 rej | SAME | Obviously she had the route drawn on a map, in case she were to forget her own plan. |
| A:2989:m | wrong |  | F4v2 rej | F4v3 rej | TIP | Of course she had the route drawn in case she forgot her own plan. |
| A:2989:s | wrong |  | F4v2 rej | L3 rej | DIFF | Of course she had the route draw on the map in case she forgot her own plan. |
| A:2989:t | wrong |  | F4v2 rej | L3 rej | DIFF | Of course she has the route drawn on the map in case she forgets her own plan. |
| A:2989:w | wrong |  | F4v2 rej | L3 rej | DIFF | Of course she had the route drawn on the map in case she lost her own plan. |
