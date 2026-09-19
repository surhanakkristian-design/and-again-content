# Phase 1N — new set: items, cells and checks

Built by `assemble_1n.py` (seed 20260919). Generated 2026-09-19T09:20:04.346816+00:00.

## Set

| quantity | value |
|---|---|
| sentences | 100 |
| sids | 160001–160100 |
| correct items | 400 (target 400) |
| wrong items | 500 (target 500) |
| total items | 900 (target 900) |
| base items / topup items | 900 / 0 |
| duplicates dropped | 0 |

## Levels (counted from the data)

| level | sentences | items |
|---|---|---|
| A1 | 13 | 117 |
| A2 | 21 | 189 |
| B1 | 36 | 324 |
| B2 | 30 | 270 |
| **total** | **100** | **900** |

## Sentence tags (true count of 100)

| tag | count |
|---|---|
| nom_agent | 89 |
| reported_speech | 15 |
| perfective_future | 11 |
| impersonal_or_passive | 6 |
| passivizable | 83 |

## Writer intent cells

| intent | count | expected | ok |
|---|---|---|---|
| C (correct) | 400 | 400 | yes |
| TF | 175 | 175 | yes |
| T | 25 | 25 | yes |
| W | 100 | 100 | yes |
| M | 100 | 100 | yes |
| S | 100 | 100 | yes |
| **wrong total** | **500** | **500** | yes |

## Passive sub-cases (correct items)

| sub-case | count | expected | ok |
|---|---|---|---|
| passive `by` | 83 | 83 (one per passivizable sentence) | yes |
| passive `agentless` | 22 | 22 (passivizable and sid % 4 == 0) | yes |
| no passive (null) | 295 | – | – |

Passivizable sentences: 83 of 100; of these 22 have sid % 4 == 0. Passives on non-passivizable sentences: 0.

## Quota violations by sid

- none (every sid: 4 correct rows, 5 wrong rows, 1 `by` where passivizable, 1 `agentless` where passivizable and sid % 4 == 0)

## Contamination check vs `existing_350.json`

- existing rows compared: 350
- identical Slovak sentences: 0
- pairs with token-Jaccard >= 0.80: 0
- max token-Jaccard new vs existing: 0.35 (160053, 45) (new sid, existing row index)
- max token-Jaccard new vs new: 0.25 (160005, 160083)

## Judge packets

- `judge/in_part1..5.json`: 5 x 180 = 900 rows, jids J0001–J0900; rows carry only jid/slovak/level/answer
- `judge/blind_map.json`: 900 jid -> item id
- `judge/in_controls.json`: 80 duplicated items, jids K001–K080
- `judge/controls_map.json`: 80 kid -> item id

## Problems

- none
