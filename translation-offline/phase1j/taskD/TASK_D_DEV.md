# Phase 1j — Task D, the DEV measurement (agent R)

Model **gemini-3.1-flash-lite**, temperature 0, thinkingBudget 0 — decided, not tested. DEV only. Every counted call is an HTTP-200 row in the one shared ledger `phase1j/ledger.jsonl`.

## 1 Label rules (declared before the results)

- **arm_A_and_BASE** — existing labels on the original Slovak (items.jsonl judged / wrong_type)
- **arms_B_A+B_C_primary** — existing label/type, overridden to (wrong, type S) exactly where the blind judge says label=wrong AND subj_ok=false, for items of REWRITTEN sentences only; every other judge disagreement counted, not adopted
- **arms_B_A+B_C_sensitivity** — judge label AND type adopted for every rewritten-sentence item
- **controls** — the 60 CONTROL items (unchanged Slovak) never change a label; they measure judge noise only
- Type **M** in CONTEXT_1J §6 is *"meaning added **or** dropped"*, so under the tag contract the expected tag for an M item is **MISS or ADD** (either counts as correct).

## 2 Relabelling counts and judge noise

DEV (rewritten-sentence items only, controls excluded): `{"n_rejudged": 357, "unchanged": 299, "correct_to_wrong_subject": 26, "wrong_to_wrong_type_change": 29, "wrong_to_correct": 3}`

Both sides together (counts only, taken from the key map; no holdout row was opened): `{"n_rejudged": 637, "unchanged": 529, "correct_to_wrong_subject": 48, "wrong_to_wrong_type_change": 49, "wrong_to_correct": 10, "correct_to_wrong_other": 1}`

Primary overrides actually applied on DEV: **41** items. Sensitivity overrides on DEV: **59**.

**Judge noise, 60 CONTROL items** (unchanged Slovak, judged blind a second time):

| direction | rate | exact 95 %% CP |
|---|---|---|
| correct_to_wrong | 0/60 = 0.00 % | [0.00, 5.96] |
| wrong_to_correct | 1/60 = 1.67 % | [0.04, 8.94] |
| any_flip | 1/60 = 1.67 % | [0.04, 8.94] |

## 3 Budget plan (printed before any call, zero calls)

| arm | items at L3 | unique prompts | already stored | NEW calls after dedupe |
|---|---|---|---|---|
| BASE | 294 | 294 | 294 | 0 |
| A | 294 | 294 | 294 | 0 |
| A:f4p-only | 294 | 294 | 294 | 0 |
| A:p_prompt-only | 294 | 294 | 294 | 0 |
| B | 256 | 256 | 250 | 6 |
| A+B | 256 | 256 | 251 | 5 |
| C | 256 | 256 | 251 | 5 |

Total NEW planned: **16** (DEV allowance 1,070 = 1,400 hard cap − 330 reserved for the final holdout run). Subsample: **none**. All (item, arm) pairs were built first, byte-identical prompts deduped, then shuffled with seed 1 so an outage damages every arm equally.

## 4 The table

*switch* = TIP-as-rejection for A / B / A+B. **For arm C there is no TIP**; its analogue is the MISS row of the tag table — switch **on** = `MISS -> rejected`, switch **off** = `MISS -> accepted`. Coverage denominators differ between arms because the B-labels move items between the correct and the wrong set; read the percentages, not the counts, across arms.

### 4.1 primary labels

| arm | switch | coverage | FA | FA T | FA W | FA M | FA S | failed calls | FR by layer |
|---|---|---|---|---|---|---|---|---|---|
| BASE | on | 191/210 = 90.95% [86.23, 94.46] | 15/275 = 5.45% [3.08, 8.84] | 0/69 = 0.00% [0.00, 5.21] | 2/70 = 2.86% [0.35, 9.94] | 5/66 = 7.58% [2.51, 16.80] | 8/70 = 11.43% [5.07, 21.28] | 0 | {"F4v2": 3, "L2": 9, "L3:TIPrej": 2, "L3": 5} |
| BASE | off | 193/210 = 91.90% [87.36, 95.21] | 29/275 = 10.55% [7.18, 14.79] | 0/69 = 0.00% [0.00, 5.21] | 6/70 = 8.57% [3.21, 17.73] | 15/66 = 22.73% [13.31, 34.70] | 8/70 = 11.43% [5.07, 21.28] | 0 | {"F4v2": 3, "L2": 9, "L3": 5} |
| A | on | 190/210 = 90.48% [85.67, 94.09] | 11/275 = 4.00% [2.01, 7.04] | 0/69 = 0.00% [0.00, 5.21] | 2/70 = 2.86% [0.35, 9.94] | 5/66 = 7.58% [2.51, 16.80] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3:TIPrej": 3, "L3": 5} |
| A | off | 193/210 = 91.90% [87.36, 95.21] | 25/275 = 9.09% [5.97, 13.13] | 1/69 = 1.45% [0.04, 7.81] | 5/70 = 7.14% [2.36, 15.89] | 15/66 = 22.73% [13.31, 34.70] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3": 5} |
| A:f4p-only | on | 191/210 = 90.95% [86.23, 94.46] | 11/275 = 4.00% [2.01, 7.04] | 0/69 = 0.00% [0.00, 5.21] | 2/70 = 2.86% [0.35, 9.94] | 5/66 = 7.58% [2.51, 16.80] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3:TIPrej": 2, "L3": 5} |
| A:f4p-only | off | 193/210 = 91.90% [87.36, 95.21] | 25/275 = 9.09% [5.97, 13.13] | 0/69 = 0.00% [0.00, 5.21] | 6/70 = 8.57% [3.21, 17.73] | 15/66 = 22.73% [13.31, 34.70] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3": 5} |
| A:p_prompt-only | on | 190/210 = 90.48% [85.67, 94.09] | 11/275 = 4.00% [2.01, 7.04] | 0/69 = 0.00% [0.00, 5.21] | 2/70 = 2.86% [0.35, 9.94] | 5/66 = 7.58% [2.51, 16.80] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3:TIPrej": 3, "L3": 5} |
| A:p_prompt-only | off | 193/210 = 91.90% [87.36, 95.21] | 25/275 = 9.09% [5.97, 13.13] | 1/69 = 1.45% [0.04, 7.81] | 5/70 = 7.14% [2.36, 15.89] | 15/66 = 22.73% [13.31, 34.70] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3": 5} |
| B | on | 171/185 = 92.43% [87.63, 95.80] | 12/301 = 3.99% [2.08, 6.86] | 0/64 = 0.00% [0.00, 5.60] | 2/64 = 3.12% [0.38, 10.84] | 4/62 = 6.45% [1.79, 15.70] | 6/111 = 5.41% [2.01, 11.39] | 0 | {"L3:TIPrej": 3, "L2": 7, "L3": 4} |
| B | off | 174/185 = 94.05% [89.61, 96.99] | 25/301 = 8.31% [5.45, 12.02] | 0/64 = 0.00% [0.00, 5.60] | 5/64 = 7.81% [2.59, 17.30] | 14/62 = 22.58% [12.93, 34.97] | 6/111 = 5.41% [2.01, 11.39] | 0 | {"L2": 7, "L3": 4} |
| A+B | on | 170/185 = 91.89% [86.98, 95.39] | 12/301 = 3.99% [2.08, 6.86] | 0/64 = 0.00% [0.00, 5.60] | 1/64 = 1.56% [0.04, 8.40] | 4/62 = 6.45% [1.79, 15.70] | 7/111 = 6.31% [2.57, 12.56] | 0 | {"L3:TIPrej": 4, "L2": 7, "L3": 4} |
| A+B | off | 174/185 = 94.05% [89.61, 96.99] | 24/301 = 7.97% [5.18, 11.63] | 0/64 = 0.00% [0.00, 5.60] | 4/64 = 6.25% [1.73, 15.24] | 13/62 = 20.97% [11.66, 33.18] | 7/111 = 6.31% [2.57, 12.56] | 0 | {"L2": 7, "L3": 4} |
| C | on | 162/185 = 87.57% [81.93, 91.95] | 4/301 = 1.33% [0.36, 3.37] | 0/64 = 0.00% [0.00, 5.60] | 0/64 = 0.00% [0.00, 5.60] | 1/62 = 1.61% [0.04, 8.66] | 3/111 = 2.70% [0.56, 7.70] | 0 | {"L3": 16, "L2": 7} |
| C | off | 165/185 = 89.19% [83.80, 93.27] | 29/301 = 9.63% [6.55, 13.54] | 1/64 = 1.56% [0.04, 8.40] | 0/64 = 0.00% [0.00, 5.60] | 25/62 = 40.32% [28.05, 53.55] | 3/111 = 2.70% [0.56, 7.70] | 0 | {"L3": 13, "L2": 7} |

### 4.2 sensitivity labels

| arm | switch | coverage | FA | FA T | FA W | FA M | FA S | failed calls | FR by layer |
|---|---|---|---|---|---|---|---|---|---|
| BASE | on | 191/210 = 90.95% [86.23, 94.46] | 15/275 = 5.45% [3.08, 8.84] | 0/69 = 0.00% [0.00, 5.21] | 2/70 = 2.86% [0.35, 9.94] | 5/66 = 7.58% [2.51, 16.80] | 8/70 = 11.43% [5.07, 21.28] | 0 | {"F4v2": 3, "L2": 9, "L3:TIPrej": 2, "L3": 5} |
| BASE | off | 193/210 = 91.90% [87.36, 95.21] | 29/275 = 10.55% [7.18, 14.79] | 0/69 = 0.00% [0.00, 5.21] | 6/70 = 8.57% [3.21, 17.73] | 15/66 = 22.73% [13.31, 34.70] | 8/70 = 11.43% [5.07, 21.28] | 0 | {"F4v2": 3, "L2": 9, "L3": 5} |
| A | on | 190/210 = 90.48% [85.67, 94.09] | 11/275 = 4.00% [2.01, 7.04] | 0/69 = 0.00% [0.00, 5.21] | 2/70 = 2.86% [0.35, 9.94] | 5/66 = 7.58% [2.51, 16.80] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3:TIPrej": 3, "L3": 5} |
| A | off | 193/210 = 91.90% [87.36, 95.21] | 25/275 = 9.09% [5.97, 13.13] | 1/69 = 1.45% [0.04, 7.81] | 5/70 = 7.14% [2.36, 15.89] | 15/66 = 22.73% [13.31, 34.70] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3": 5} |
| A:f4p-only | on | 191/210 = 90.95% [86.23, 94.46] | 11/275 = 4.00% [2.01, 7.04] | 0/69 = 0.00% [0.00, 5.21] | 2/70 = 2.86% [0.35, 9.94] | 5/66 = 7.58% [2.51, 16.80] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3:TIPrej": 2, "L3": 5} |
| A:f4p-only | off | 193/210 = 91.90% [87.36, 95.21] | 25/275 = 9.09% [5.97, 13.13] | 0/69 = 0.00% [0.00, 5.21] | 6/70 = 8.57% [3.21, 17.73] | 15/66 = 22.73% [13.31, 34.70] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3": 5} |
| A:p_prompt-only | on | 190/210 = 90.48% [85.67, 94.09] | 11/275 = 4.00% [2.01, 7.04] | 0/69 = 0.00% [0.00, 5.21] | 2/70 = 2.86% [0.35, 9.94] | 5/66 = 7.58% [2.51, 16.80] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3:TIPrej": 3, "L3": 5} |
| A:p_prompt-only | off | 193/210 = 91.90% [87.36, 95.21] | 25/275 = 9.09% [5.97, 13.13] | 1/69 = 1.45% [0.04, 7.81] | 5/70 = 7.14% [2.36, 15.89] | 15/66 = 22.73% [13.31, 34.70] | 4/70 = 5.71% [1.58, 13.99] | 0 | {"F4v2": 3, "L2": 9, "L3": 5} |
| B | on | 171/185 = 92.43% [87.63, 95.80] | 11/298 = 3.69% [1.86, 6.51] | 0/53 = 0.00% [0.00, 6.72] | 2/74 = 2.70% [0.33, 9.42] | 3/64 = 4.69% [0.98, 13.09] | 6/107 = 5.61% [2.09, 11.81] | 0 | {"L3:TIPrej": 3, "L2": 7, "L3": 4} |
| B | off | 174/185 = 94.05% [89.61, 96.99] | 24/298 = 8.05% [5.23, 11.75] | 0/53 = 0.00% [0.00, 6.72] | 5/74 = 6.76% [2.23, 15.07] | 13/64 = 20.31% [11.28, 32.23] | 6/107 = 5.61% [2.09, 11.81] | 0 | {"L2": 7, "L3": 4} |
| A+B | on | 170/185 = 91.89% [86.98, 95.39] | 11/298 = 3.69% [1.86, 6.51] | 0/53 = 0.00% [0.00, 6.72] | 1/74 = 1.35% [0.03, 7.30] | 3/64 = 4.69% [0.98, 13.09] | 7/107 = 6.54% [2.67, 13.02] | 0 | {"L3:TIPrej": 4, "L2": 7, "L3": 4} |
| A+B | off | 174/185 = 94.05% [89.61, 96.99] | 23/298 = 7.72% [4.96, 11.36] | 0/53 = 0.00% [0.00, 6.72] | 4/74 = 5.41% [1.49, 13.27] | 12/64 = 18.75% [10.08, 30.46] | 7/107 = 6.54% [2.67, 13.02] | 0 | {"L2": 7, "L3": 4} |
| C | on | 162/185 = 87.57% [81.93, 91.95] | 4/298 = 1.34% [0.37, 3.40] | 0/53 = 0.00% [0.00, 6.72] | 0/74 = 0.00% [0.00, 4.86] | 1/64 = 1.56% [0.04, 8.40] | 3/107 = 2.80% [0.58, 7.98] | 0 | {"L3": 16, "L2": 7} |
| C | off | 165/185 = 89.19% [83.80, 93.27] | 28/298 = 9.40% [6.33, 13.29] | 0/53 = 0.00% [0.00, 6.72] | 0/74 = 0.00% [0.00, 4.86] | 25/64 = 39.06% [27.10, 52.07] | 3/107 = 2.80% [0.58, 7.98] | 0 | {"L3": 13, "L2": 7} |

"failed calls" = items that reached L3 and have **no** verdict (an empty or unparsable HTTP-200 reply, counted, never retried, never guessed); they are scored as rejected.

## 5 A vs B on the subject problem

BASE has 8 type-S false acceptances on DEV. Per item, under switch **on**:

| item | A | B | A+B | C |
|---|---|---|---|---|
| `W:10574:2448666810` | REMOVED (L3) | REMOVED (F4v2) | REMOVED (F4v2) | REMOVED (F4v2) |
| `W:1452:315243162` | REMOVED (L3) | REMOVED (F4v2) | REMOVED (F4v2) | REMOVED (F4v2) |
| `W:16403:1306885234` | REMOVED (L3) | REMOVED (F4v2) | REMOVED (F4v2) | REMOVED (F4v2) |
| `W:2389:1402963517` | still accepted | still accepted | still accepted | REMOVED (L3) |
| `W:7910:2914297793` | still accepted | still accepted | still accepted | REMOVED (L3) |
| `W:8293:1283962081` | REMOVED (L3) | REMOVED (F4v2) | REMOVED (F4v2) | REMOVED (F4v2) |
| `W:8799:1222448868` | REMOVED (L3) | REMOVED (L3) | REMOVED (L3) | REMOVED (L3) |
| `W:9687:2008862971` | still accepted | still accepted | still accepted | REMOVED (L3) |

- `W:10574:2448666810` — SK: Trénoval hodiny, kým bolo svetlo konečne správne. | ref: He had been training for hours before the light was finally right. | answer: **They had been training for hours until the light was finally right.**
- `W:1452:315243162` — SK: Ak sa dotkne toho kaktusa, strávi večer vyťahovaním tŕňov z prsta. | ref: If he touches that cactus, he will spend the evening pulling spines out of his finger. | answer: **If they touch that cactus, they'll spend the evening pulling thorns out of their finger.**
- `W:16403:1306885234` — SK: Rozlúč sa a o hodinu sa vráti naspäť. | ref: Say bye now and she will come back in an hour. | answer: **Say goodbye, and in an hour they'll come back.**
- `W:2389:1402963517` — SK: Keby duriány nesmrdeli tak silno, colnica by ich asi pustila. | ref: If durians didn't smell so strongly, customs would probably let them through. | answer: **If durians didn't smell so strong, the customs officer would probably let them through.**
- `W:7910:2914297793` — SK: Napriek ventilátoru na plný výkon sa zopnutá kopa vôbec nepohla. | ref: Despite the fan at full power, the clipped pile did not move at all. | answer: **Despite the fan being at full power, the clipped piles didn't move at all.**
- `W:8293:1283962081` — SK: Jedlo nikdy nedelí, takže tento croissant musí byť výnimočný. | ref: She never shares food, so this one must be special. | answer: **They never share food, so this croissant must be special.**
- `W:8799:1222448868` — SK: Stále hádzala tú istú kombináciu, kým nešla hladko. | ref: She kept throwing the same combination until it felt smooth. | answer: **They kept throwing the same combination until it went smoothly.**
- `W:9687:2008862971` — SK: Ak oba štáty podpíšu zmluvu, hranica sa budúci mesiac otvorí. | ref: If both states sign the treaty, the border will open next month. | answer: **If both countries sign the treaty, the borders will open next month.**

**Correct answers each arm loses that BASE accepted** (label in force for that arm, switch on):

- **A** — 1 lost
  - `C:8017:1594837287` at L3:TIPrej (model TIP) — The goalkeeper was just standing on the line when the referee pointed at the white spot.

- **B** — 1 lost
  - `C:8465:1630787538` at L3 (model DIFF) — If that barrel hadn't been knocked over, the fish would still be here.

- **A+B** — 2 lost
  - `C:8017:1594837287` at L3:TIPrej (model TIP) — The goalkeeper was just standing on the line when the referee pointed at the white spot.
  - `C:8465:1630787538` at L3 (model DIFF) — If that barrel hadn't been knocked over, the fish would still be here.

- **C** — 12 lost
  - `C:14779:4064141330` at L3 (model DIFF) — She's going to wipe dust from the top of the door.
  - `C:15437:2596903784` at L3 (model DIFF) — The field is private property. We must keep to the path.
  - `C:24733:1990053738` at L3 (model DIFF) — The little glass is hot, so you must hold it carefully.
  - `C:24733:3021952467` at L3 (model DIFF) — The small glass is hot, so you must be careful holding it.
  - `C:27628:3250724313` at L3 (model DIFF) — The kids will wake up at seven a.m.
  - `C:6265:2537737113` at L3 (model DIFF) — Nobody enjoys being chased on a trip like that.
  - `C:6830:456997889` at L3 (model DIFF) — As kids, they used to buy dried herbs in jars.
  - `C:7752:397282127` at L3 (model DIFF) — The otter's poked me in the sleeve three times already this morning.
  - `C:8465:1630787538` at L3 (model DIFF) — If that barrel hadn't been knocked over, the fish would still be here.
  - `C:9602:2201109812` at L3 (model DIFF) — Before the final, she'd been sprinting each morning for months.
  - `C:9913:2883974382` at L3 (model DIFF) — Last year, she had her boots dyed a purple color.
  - `W:23878:655520666` at L3 (model DIFF) — In this huge stadium there is a green field.

## 6 Task C — tag-level accuracy of the contract

Expected tag from the label in force: correct -> `OK`, M -> `MISS` or `ADD`, W -> `SWAP`, S -> `SUBJ`. Type **T** has no tag in the contract and is reported separately. Scored on the first tag returned.

- items that reached the model: **256**, unparsable replies: **0**
- overall tag accuracy (excluding T): **207/240 = 86.25% [81.24, 90.34]**

| expected class | tag accuracy | exact 95 %% CP |
|---|---|---|
| correct | 101/118 = 85.59 % | [77.94, 91.38] |
| M | 30/33 = 90.91 % | [75.67, 98.08] |
| W | 60/62 = 96.77 % | [88.83, 99.61] |
| S | 16/27 = 59.26 % | [38.80, 77.61] |

Tags the model gave **type-T** items: `{"SWAP": 14, "SUBJ": 1, "MISS": 1}`

Confusion, expected x first tag returned: `{"M|ADD": 5, "M|MISS": 25, "M|OK": 1, "M|SUBJ": 1, "M|SWAP": 1, "S|SUBJ": 16, "S|SWAP": 11, "T|MISS": 1, "T|SUBJ": 1, "T|SWAP": 14, "W|ADD": 1, "W|SUBJ": 1, "W|SWAP": 60, "correct|ADD": 5, "correct|MISS": 4, "correct|OK": 101, "correct|SUBJ": 1, "correct|SWAP": 7}`

Confusion, expected x full tag SET: `{"M|ADD": 5, "M|MISS": 24, "M|MISS+SUBJ": 1, "M|MISS+SWAP": 1, "M|OK": 1, "M|SWAP": 1, "S|ADD+MISS+SUBJ": 2, "S|ADD+SWAP": 1, "S|MISS+SUBJ": 1, "S|SUBJ": 10, "S|SUBJ+SWAP": 4, "S|SWAP": 9, "T|MISS": 1, "T|SUBJ": 1, "T|SWAP": 14, "W|ADD+SWAP": 1, "W|SUBJ+SWAP": 2, "W|SWAP": 59, "correct|ADD": 3, "correct|ADD+SUBJ": 1, "correct|ADD+SWAP": 2, "correct|MISS": 4, "correct|OK": 101, "correct|SUBJ": 1, "correct|SWAP": 6}`

Ten example mismatches:

- `C:10116:2635817258` expected OK, returned `ADD:tightly SWAP:holding~hugging` — SK: Keď sa terapia začala, ona objímala vankúš. | ref: When the session started, she was hugging a pillow. | answer: **When the session started, she was holding a pillow tightly.**
- `C:11610:415761804` expected OK, returned `MISS:one` — SK: Na lavičke je jeden dlhý obväz. | ref: There is one long bandage on the bench. | answer: **There's a long bandage on the bench.**
- `C:14779:4064141330` expected OK, returned `MISS:edge` — SK: Ona ide utrieť prach z hornej hrany dverí. | ref: She is going to wipe the dust off the top edge of the door. | answer: **She's going to wipe dust from the top of the door.**
- `C:15437:2596903784` expected OK, returned `ADD:property` — SK: Pole je súkromné. My musíme zostať na cestičke. | ref: The field is private. We must stay on the path. | answer: **The field is private property. We must keep to the path.**
- `C:24733:1990053738` expected OK, returned `ADD:little` — SK: Pohárik je horúci, tak ty ho musíš držať opatrne. | ref: The glass is hot, so you must hold it carefully. | answer: **The little glass is hot, so you must hold it carefully.**
- `C:24733:3021952467` expected OK, returned `ADD:small SUBJ:you~you` — SK: Pohárik je horúci, tak ty ho musíš držať opatrne. | ref: The glass is hot, so you must hold it carefully. | answer: **The small glass is hot, so you must be careful holding it.**
- `C:27628:1242167241` expected OK, returned `SWAP:will wake up~awake` — SK: Deti sa zobudia o siedmej ráno. | ref: The children awake at seven in the morning. | answer: **At seven in the morning, the children will wake up.**
- `C:27628:3250724313` expected OK, returned `SWAP:will wake up~awake` — SK: Deti sa zobudia o siedmej ráno. | ref: The children awake at seven in the morning. | answer: **The kids will wake up at seven a.m.**
- `C:27628:3492027817` expected OK, returned `SWAP:will wake up~awake` — SK: Deti sa zobudia o siedmej ráno. | ref: The children awake at seven in the morning. | answer: **The children will wake up at seven in the morning.**
- `C:29691:2119858295` expected OK, returned `SWAP:let~drops ADD:going~to` — SK: On pustí svojho sprievodcu na kostolné schody! Úplná katastrofa! | ref: He drops his guidebook on the church steps! Total disaster! | answer: **He's going to let his guide onto the church steps! A complete disaster!**

## 7 Selection

| arm | switch | coverage | FA | FA type T | unique calls |
|---|---|---|---|---|---|
| A | on | 190/210 = 90.48% [85.67, 94.09] | 11/275 = 4.00% [2.01, 7.04] | 0/69 = 0.00% [0.00, 5.21] | 294 |
| A | off | 193/210 = 91.90% [87.36, 95.21] | 25/275 = 9.09% [5.97, 13.13] | 1/69 = 1.45% [0.04, 7.81] | 294 |
| B | on | 171/185 = 92.43% [87.63, 95.80] | 12/301 = 3.99% [2.08, 6.86] | 0/64 = 0.00% [0.00, 5.60] | 256 |
| B | off | 174/185 = 94.05% [89.61, 96.99] | 25/301 = 8.31% [5.45, 12.02] | 0/64 = 0.00% [0.00, 5.60] | 256 |
| A+B | on | 170/185 = 91.89% [86.98, 95.39] | 12/301 = 3.99% [2.08, 6.86] | 0/64 = 0.00% [0.00, 5.60] | 256 |
| A+B | off | 174/185 = 94.05% [89.61, 96.99] | 24/301 = 7.97% [5.18, 11.63] | 0/64 = 0.00% [0.00, 5.60] | 256 |
| C | on | 162/185 = 87.57% [81.93, 91.95] | 4/301 = 1.33% [0.36, 3.37] | 0/64 = 0.00% [0.00, 5.60] | 256 |
| C | off | 165/185 = 89.19% [83.80, 93.27] | 29/301 = 9.63% [6.55, 13.54] | 1/64 = 1.56% [0.04, 8.40] | 256 |

- type-T FA <= 1.5% gate: 7 of 8 rows pass -> ['A/on', 'A/off', 'B/on', 'B/off', 'A+B/on', 'A+B/off', 'C/on']
- rows with FA point estimate < 5%: ['B/on cov 92.43 FA 3.99', 'A+B/on cov 91.89 FA 3.99', 'A/on cov 90.48 FA 4.00', 'C/on cov 87.57 FA 1.33']
- -> highest coverage among them: B / switch on

**Frozen choice: arm `B`, switch `on`** — written to `phase1j/FROZEN_CONFIG_1J.json`; `phase1j/run_final.py` rebuilds exactly these requests.

### DEV false acceptances of the selected configuration, itemised

- `C:10167:2659945156` type S at L1 — model reply `` | SK: On má ústa také suché, že smäd musí byť skutočný. | ref: His mouth is that dry, so the thirst must be real. | answer: **Her mouth is so dry that the thirst must be real.**
- `C:10167:3007534590` type S at L1 — model reply `` | SK: On má ústa také suché, že smäd musí byť skutočný. | ref: His mouth is that dry, so the thirst must be real. | answer: **Her mouth's so dry that the thirst must be real.**
- `C:26084:39201327` type S at L1 — model reply `` | SK: On ju dokáže nájsť skôr, než ona príde domov. | ref: He can find her before she gets home. | answer: **She can find her before she comes home.**
- `W:21124:1753932823` type M at L3 — model reply `SAME` | SK: Zvyčajne ona ostáva pod strechou, ale dnes tancuje v daždi. | ref: She usually stays dry, but today she is dancing in the rain. | answer: **She stays under the roof, but today she is dancing in the rain.**
- `W:2389:1402963517` type S at L3 — model reply `` | SK: Keby duriány nesmrdeli tak silno, colnica by ich asi pustila. | ref: If durians didn't smell so strongly, customs would probably let them through. | answer: **If durians didn't smell so strong, the customs officer would probably let them through.**
- `W:2783:2540506102` type M at L3 — model reply `` | SK: Lopta, ktorú pes priniesol, je teraz úplne od blata. | ref: The ball that the dog fetched is now completely muddy. | answer: **The ball that the dog brought is covered in mud.**
- `W:31648:250135833` type W at L3 — model reply `SAME` | SK: Zlatko, on vraj opustil misku včera, nie dnes. | ref: Honey, apparently he left the bowl yesterday, not today. | answer: **Honey, apparently he left the plate yesterday, not today.**
- `W:7444:2683969038` type M at L3 — model reply `SAME` | SK: Ona si naniesla už tri vrstvy, takže jej riasy vyzerajú obrovské. | ref: She has already applied three coats, so her lashes look huge. | answer: **She has applied three layers, so her eyelashes look huge.**
- `W:7910:2914297793` type S at L3 — model reply `` | SK: Napriek ventilátoru na plný výkon sa zopnutá kopa vôbec nepohla. | ref: Despite the fan at full power, the clipped pile did not move at all. | answer: **Despite the fan being at full power, the clipped piles didn't move at all.**
- `W:8812:384802316` type M at L3 — model reply `` | SK: Tréner by si prial, aby jeho lapy boli trochu hrubšie. | ref: Her trainer wishes his pads were a bit thicker. | answer: **The coach wishes his gloves were thicker.**
- `W:9007:2829648222` type W at L3 — model reply `SAME` | SK: Dnes v noci on preveril už šesť zdrojov a kopa stále rastie. | ref: He has checked six sources tonight and the pile is still growing. | answer: **Tonight he has already checked six sources and the list is still growing.**
- `W:9687:2008862971` type S at L3 — model reply `` | SK: Ak oba štáty podpíšu zmluvu, hranica sa budúci mesiac otvorí. | ref: If both states sign the treaty, the border will open next month. | answer: **If both countries sign the treaty, the borders will open next month.**

## 8 Calls, tokens, spend

`{"counted_calls_http200": 814, "failed_calls_parse": 0, "transport_rows_not_counted": 298, "tokens_in": 241424, "tokens_out": 1795, "spend_usd": 0.06305}`

Transport retries (non-200 rows, never counted): 298. Prompts reused byte-identically from the Phase 1i ledgers: 294. Spend at $0.25 / 1M input and $1.50 / 1M output tokens: **$0.06305**. **Whether these calls were billed or served from a free tier is not detectable from the response body** — the figure is the list price of the tokens actually reported by `usageMetadata`.
