# Phase 1N — re-score of the CLOSED Phase 1M verdicts (label `rescore-1m`)

> **This is a RE-SCORE of a closed set: ranking evidence, not a measurement.** No model was called (0 calls). The 1M pipeline was replayed offline over the stored verdicts with two changes: **F8 decides nothing** and the **new labels** from the re-judge (1M labels, replaced wherever an item was re-judged).

> **Caveat that limits every number below:** the stored L3 verdicts were produced by the **OLD 1M prompt, which still carried the voice line**. The re-score therefore shows what the 1M *stack* would have scored under the corrected labels — not what a run under the 1N prompt will score. A fresh measurement is still owed.

## 0. The headline in one paragraph

Under the corrected labels the 1M stack is no longer a false-accept problem — it is a
**false-reject** problem. FA falls from 10.68 % to **2.84 %** (the V class that produced 55 of the
69 false accepts is gone: those items were never wrong), while coverage falls from 89.09 % to
**82.53 %**, because 153 items the 1M judge called wrong are now correct and the stack keeps
rejecting them: L3 alone false-rejects 77/767 = 10.04 % (was 27/614 = 4.40 %). The damage is
concentrated in the agentless passive: only 12 of 65 such items survive the stack, 40 of them
killed by L3 itself — a prompt problem, not a guard problem, which is exactly what the 1N prompt
change addresses. F8 removal is confirmed on the same evidence: F8v1 rejects 69 items, **all 69
judged correct, 0 catches**; F8v2 rejects 98, of which 86 are judged correct and 12 judged wrong,
and **none of the 12 is unique** — every one is already rejected by another layer. Ranking
evidence only: see the caveat above.

## 1. Faithfulness of the replay

`--f8 f8v2` + old labels reproduces 1M exactly: **YES** (coverage 547/614, FA 69/646, by type {"E": "0/0", "M": "1/62", "S": "2/82", "T": "11/242", "V": "55/171", "W": "0/89"}).

1115 stored verdicts reused, 301 labels replaced by the re-judge.

## 2. Headline, side by side

| cell | 1M as measured (F8v2 decides, old labels) | F8 removed, old labels | **re-score: F8 removed + new labels** |
|---|---|---|---|
| coverage | 547/614 = 89.09% [86.35, 91.44] | 553/614 = 90.07% [87.42, 92.32] | **633/767 = 82.53% [79.65, 85.15]** |
| FA | 69/646 = 10.68% [8.41, 13.32] | 94/646 = 14.55% [11.92, 17.51] | **14/493 = 2.84% [1.56, 4.72]** |

## 3. FA by type, exact 95 % Clopper-Pearson

| type | 1M as measured | re-score (F8 removed + new labels) |
|---|---|---|
| T | 11/242 = 4.55% [2.29, 7.99] | 11/241 = 4.56% [2.30, 8.02] |
| W | 0/89 = 0.00% [0.00, 4.06] | 0/96 = 0.00% [0.00, 3.77] |
| M | 1/62 = 1.61% [0.04, 8.66] | 1/73 = 1.37% [0.03, 7.40] |
| S | 2/82 = 2.44% [0.30, 8.53] | 2/83 = 2.41% [0.29, 8.43] |
| V | 55/171 = 32.16% [25.24, 39.72] | — (type retired) |

Type **V** is retired in 1N: the voice class no longer exists, its items carry a T/W/M/S type or are judged correct.

## 4. FA and false rejections by layer

| layer | FA 1M | FA re-score | false rejections 1M | false rejections re-score |
|---|---|---|---|---|
| F2B | 0 | 0 | 3/614 = 0.49% [0.10, 1.42] | 3/767 = 0.39% [0.08, 1.14] |
| F4v2 | 0 | 0 | 9/614 = 1.47% [0.67, 2.76] | 28/767 = 3.65% [2.44, 5.23] |
| F5 | 0 | 0 | 5/614 = 0.81% [0.26, 1.89] | 5/767 = 0.65% [0.21, 1.51] |
| F8 | 0 | 0 | 6/614 = 0.98% [0.36, 2.11] | 0 |
| L3 | 69/646 = 10.68% [8.41, 13.32] | 14/493 = 2.84% [1.56, 4.72] | 27/614 = 4.40% [2.92, 6.33] | 77/767 = 10.04% [8.00, 12.39] |
| L3:TIPrej | 0 | 0 | 17/614 = 2.77% [1.62, 4.40] | 21/767 = 2.74% [1.70, 4.15] |

## 5. What the removed F8 would have done under the new labels

Both modules are read out and decide nothing. COST = judged-correct items the module would reject; CATCHES = judged-wrong items it would reject; UNIQUE = of those, the ones the headline stack (every other layer incl. L3) accepts.

| module | reject readouts | COST (correct rejected) | CATCHES (wrong rejected) | UNIQUE | headline under it: coverage | FA |
|---|---|---|---|---|---|---|
| F8v1 | 69 | 69 | 0 | 0 | 600/767 = 78.23% [75.14, 81.10] | 14/493 = 2.84% [1.56, 4.72] |
| F8v2 | 98 | 86 | 12 | 0 | 602/767 = 78.49% [75.41, 81.35] | 14/493 = 2.84% [1.56, 4.72] |

* **F8v1** unique catches: none
  cost ids: W:150001:2599243042, W:150004:334432156, W:150005:2236991858, W:150008:2587640877, W:150010:598363861, W:150014:3619959625, W:150016:3330974851, W:150017:1365983468, W:150017:3282275393, W:150022:1824463829, W:150022:1914778343, W:150023:3346400173, W:150026:181640577, W:150026:2435303869, W:150029:4147431312, W:150029:636390549, W:150032:3156470445, W:150037:2631626927, W:150039:1290265141, W:150039:696790370, W:150043:2981417085, W:150043:3146717365, W:150045:2207757270, W:150046:2639017536, W:150046:2758253816, W:150049:796916908, W:150051:3986601262, W:150051:754910220, W:150052:889472901, W:150055:196200580, W:150060:541897264, W:150061:3846227511, W:150064:2721351684, W:150066:2537125926, W:150066:3443590089, W:150067:1995447870, W:150067:2928349087, W:150071:3413646462, W:150072:2079221943, W:150074:1057493295

* **F8v2** unique catches: none
  cost ids: C:150054:2062420610, C:150054:3047262874, C:150054:811753297, W:150002:1328557373, W:150004:334432156, W:150008:2587640877, W:150008:658085704, W:150016:3185442775, W:150016:3330974851, W:150017:1365983468, W:150017:3128768984, W:150017:3282275393, W:150019:2296116549, W:150019:3252552891, W:150022:1824463829, W:150022:1914778343, W:150025:3429444882, W:150025:707441286, W:150026:181640577, W:150026:2435303869, W:150029:2827682207, W:150029:4147431312, W:150029:636390549, W:150032:3156470445, W:150032:3714255681, W:150037:2631626927, W:150039:1290265141, W:150039:2371300497, W:150039:696790370, W:150042:1470509509, W:150042:3907820027, W:150043:2120767092, W:150043:2981417085, W:150043:3146717365, W:150046:2639017536, W:150046:2758253816, W:150051:3161523760, W:150051:3986601262, W:150051:754910220, W:150052:889472901

## 6. The two passive sub-cases, counted separately

Tag source: the judge's `passive` key on the re-judged items. **Nothing is rejected because of the tag** — this is a count.

### (i) passive *by*

72 items — judged correct 71, judged wrong 1 {"M": 1}.

| stored verdicts under | accepted | accept rate | rejected | rejected by layer |
|---|---|---|---|---|
| stored 1M config f8v2 | 32 | 32/72 = 44.44% [32.72, 56.64] | 40 | {"F4v2": 9, "F8": 21, "L3": 8, "L3:TIPrej": 2} |
| rescore config f8 removed | 53 | 53/72 = 73.61% [61.90, 83.30] | 19 | {"F4v2": 9, "L3": 8, "L3:TIPrej": 2} |

Split by the new label:

| config | group | n | accepted | rejected by layer |
|---|---|---|---|---|
| stored 1M config f8v2 | judged_correct | 71 | 32 | {"F4v2": 8, "F8": 21, "L3": 8, "L3:TIPrej": 2} |
| stored 1M config f8v2 | judged_wrong | 1 | 0 | {"F4v2": 1} |
| rescore config f8 removed | judged_correct | 71 | 53 | {"F4v2": 8, "L3": 8, "L3:TIPrej": 2} |
| rescore config f8 removed | judged_wrong | 1 | 0 | {"F4v2": 1} |

### (ii) passive *agentless*

65 items — judged correct 63, judged wrong 2 {"M": 2}.

| stored verdicts under | accepted | accept rate | rejected | rejected by layer |
|---|---|---|---|---|
| stored 1M config f8v2 | 9 | 9/65 = 13.85% [6.53, 24.66] | 56 | {"F4v2": 10, "F8": 3, "L3": 40, "L3:TIPrej": 3} |
| rescore config f8 removed | 12 | 12/65 = 18.46% [9.92, 30.03] | 53 | {"F4v2": 10, "L3": 40, "L3:TIPrej": 3} |

Split by the new label:

| config | group | n | accepted | rejected by layer |
|---|---|---|---|---|
| stored 1M config f8v2 | judged_correct | 63 | 9 | {"F4v2": 10, "F8": 3, "L3": 38, "L3:TIPrej": 3} |
| stored 1M config f8v2 | judged_wrong | 2 | 0 | {"L3": 2} |
| rescore config f8 removed | judged_correct | 63 | 12 | {"F4v2": 10, "L3": 38, "L3:TIPrej": 3} |
| rescore config f8 removed | judged_wrong | 2 | 0 | {"L3": 2} |

Share the M machinery already surfaces as a TIP:

| config | model TIP | any TIP |
|---|---|---|
| stored 1M config f8v2 | 3/65 = 4.62% [0.96, 12.90] | 3/65 = 4.62% [0.96, 12.90] |
| rescore config f8 removed | 3/65 = 4.62% [0.96, 12.90] | 3/65 = 4.62% [0.96, 12.90] |

## 7. How to read this

* The re-score ranks configurations on a closed set; it cannot decide a target.
* Every L3 verdict inside it was taken under the old, voice-carrying prompt.
* The label change alone moves FA; the F8 removal alone moves it the other way. Column 3 of section 2 isolates the label effect, column 4 the joint effect.

