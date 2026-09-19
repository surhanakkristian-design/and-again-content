# Phase 1m — new set: items, cells and checks

Built by `assemble_1m.py` (seed 20260919). Generated 2026-09-19T06:59:13.795021+00:00.

## Set

| quantity | value |
|---|---|
| sentences | 140 |
| sids | 150001–150140 |
| correct items | 560 |
| wrong items | 700 |
| total items | 1260 |
| unique item ids | 1260 |

## Levels

| level | count | 1k-proportion target | delta |
|---|---|---|---|
| A1 | 18 | 12 | +6 |
| A2 | 29 | 32 | -3 |
| B1 | 50 | 50 | +0 |
| B2 | 43 | 46 | -3 |

## Sentence tags (true count of 140)

| tag | count |
|---|---|
| nom_agent | 88 |
| reported_speech | 28 |
| perfective_future | 14 |
| impersonal_or_passive | 16 |

## Writer intent cells (wrong items)

| intent | count | floor | ok |
|---|---|---|---|
| V | 220 | 195 | yes |
| TF | 192 | 165 | yes |
| T | 61 | – | – |
| W | 83 | – | – |
| M | 61 | – | – |
| S | 83 | – | – |

## V by form

| form | count | share of V | floor 30 |
|---|---|---|---|
| passive | 66 | 30.0 % | yes |
| cleft | 54 | 24.5 % | yes |
| reported | 32 | 14.5 % | yes |
| dropped | 68 | 30.9 % | yes |

Passive share of V = **30.0 %** (cap 35 %: ok).

## Overlap with the existing 210

- identical Slovak sentences: 0
- max token-Jaccard new vs existing: 0.33 (150062, 22427) (threshold 0.80)
- max token-Jaccard new vs new: 0.31 (150037, 150099)

## Judge packets

- `judge/in_part1..6.json`: 6 x 210 = 1260 rows, jids J0001–J1260, fields jid/slovak/level/topic/answer only
- `judge/blind_map.json`: 1260 jid -> item id
- `judge/in_controls.json`: 100 duplicate items, jids K001–K100
- `judge/controls_map.json`: 100 kid -> item id

## Problems

- none
