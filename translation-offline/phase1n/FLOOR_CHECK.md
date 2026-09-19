# Phase 1N — floor check (pre-run, judged counts)

Run 2026-09-19T09:26:34.243343+00:00 by `floor_check.py`, label **floor-check-1**. No model call was made on this set; the check reads the human/blind judge output only.

## 1. Judge files

| file | status | rows |
| --- | --- | --- |
| `out_part1.json` | ok | 180 |
| `out_part2.json` | ok | 180 |
| `out_part3.json` | ok | 180 |
| `out_part4.json` | ok | 180 |
| `out_part5.json` | ok | 180 |
| `out_controls.json` | ok | 80 |
| `out_part6.json` | not required (no `in_part6.json`) | – |
| `out_part7.json` | not required (no `in_part7.json`) | – |
| `out_part8.json` | not required (no `in_part8.json`) | – |
| `out_part9.json` | not required (no `in_part9.json`) | – |

- bad files: **none**
- jids in `blind_map.json`: 900; judged: 900; missing: 0
- items merged onto `data/items.json`: 900
- controls merged onto `controls_map.json`: 80 of 80

## 2. Judged totals

| verdict | n | share |
| --- | --- | --- |
| correct | 426 | 47.33 % |
| wrong | 474 | 52.67 % |
| **total** | 900 | 100 % |

## 3. Writer intent x judged verdict

| writer intent | n | judged correct | judged wrong | % wrong |
| --- | --- | --- | --- | --- |
| C | 400 | 399 | 1 | 0.25 % |
| TF | 175 | 5 | 170 | 97.14 % |
| T | 25 | 7 | 18 | 72.00 % |
| W | 100 | 7 | 93 | 93.00 % |
| M | 100 | 5 | 95 | 95.00 % |
| S | 100 | 3 | 97 | 97.00 % |

## 4. Judged type distribution (wrong rows)

| type | n | share of wrong |
| --- | --- | --- |
| T | 188 | 39.66 % |
| W | 94 | 19.83 % |
| M | 95 | 20.04 % |
| S | 97 | 20.46 % |

## 5. TIME-FRAME floor

- writer intent TF items: **175**
- of them judged WRONG: **170** (required >= 150) — **PASS**, margin 20
- of those wrong ones carrying judge type `T`: 170

## 6. PASSIVE floor

| writer passive tag | items | judged correct | judged wrong | % correct |
| --- | --- | --- | --- | --- |
| by | 83 | 83 | 0 | 100.00 % |
| agentless | 22 | 22 | 0 | 100.00 % |
| **by + agentless** | 105 | 105 | 0 | 100.00 % |

- required >= 60 judged correct — **PASS**, margin 45

### 6.1 Judge's own passive tag x writer's passive tag (all merged items)

| writer \ judge | by | agentless | null | total |
| --- | --- | --- | --- | --- |
| by | 83 | 0 | 0 | 83 |
| agentless | 0 | 22 | 0 | 22 |
| null | 1 | 0 | 794 | 795 |
| **total** | 84 | 22 | 794 | 900 |

## 7. Writer versus judge disagreements

- verdict disagreements: **28** of 900 (3.11 %)
  - writer C, judged wrong: 1
  - writer wrong, judged correct: 27
- type disagreements among rows both sides call wrong: **0**

| writer intent -> judge type | n |
| --- | --- |
| none — every wrong row got the writer's type (TF and T both map to `T`) | 0 |

## 8. Control noise (80 duplicated items, re-judged blind)

| mismatch | k / n | rate | exact 95 % CP interval |
| --- | --- | --- | --- |
| judged verdict | 3 / 80 | 3.75 % | [0.78 %, 10.57 %] |
| type field | 5 / 80 | 6.25 % | [2.06 %, 13.99 %] |
| type, both-wrong pairs only | 2 / 40 | 5.00 % | [0.61 %, 16.92 %] |

## 9. Verdict

- floors_ok: **True**
- bad judge files: **none**
- top-up request written: **False**

Files: `FLOOR_CHECK.md`, `floor_check.json`; 9 label reads appended to `access_log.jsonl`.
