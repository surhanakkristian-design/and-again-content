# Translation pipeline — consolidated status, 21 September 2026

Numbers and sources only. No recommendations. Every interval is exact Clopper–Pearson 95 %.

## 1. Measured headline figures

| figure | value | 95 % interval | phase |
|---|---|---|---|
| Slovak coverage, blind TEST set | 392/401 = 97.76 % | [95.78, 98.97] | 1W |
| Slovak FA, blind TEST set | 16/499 = 3.21 % | [1.84, 5.15] | 1W |
| **Slovak coverage, PRODUCTION sentences (PROBE)** | **154/182 = 84.62 %** | **[78.54, 89.53]** | **2F §3.1** |
| **Slovak FA, PRODUCTION sentences (PROBE)** | **11/178 = 6.18 %** | **[3.12, 10.79]** | **2F §3.1** |
| Czech coverage | **not measured** | — | — |
| Czech FA | **not measured** | — | — |
| Slovak coverage (previous set) | 95.02 % | [92.42, 96.93] | 1U |
| Slovak FA (previous set) | 3.21 % | [1.85, 5.17] | 1U |
| Slovak coverage | 92.40 % | [89.44, 94.74] | 1T |

Targets: coverage ≥ 90 %, FA < 5 %.

## 2. Per-guard error rates, sk vs cz

| guard | Slovak | Czech | phase |
|---|---|---|---|
| `agent_nom` | 11.63 % | **21.05 %** | 2C |
| `gender` | 11.63 % | **19.23 %** | 2C |
| AG v4, merged-file diagnostic (250 rows, 12 % bar) | 10.00 % [6.58, 14.41] | 10.40 % [6.91, 14.87] | 2E |
| agent reader on raw PRODUCTION text | 50 % | — | 2B |
| agent reader on blind TEST Slovak | 1.67 % | — | 2B |
| GATE 3 AG v4 per batch (50 rows, 12 % bar) | — | 8.00 / 8.00 / 6.00 % PASS | 2E |
| GATE 3 `reader_nom` per batch | — | 6.90 / 7.69 / 9.68 % PASS | 2E |
| g4 (diagnostic, never gates) | — | 22 / 26 / 30 % | 2E |
| deterministic agent path, production Slovak | fired 13/360, 0 coverage cost | — | 2F §3.1 |

## 3. `lk` — the dedicated pass

| language | rows | non-exact | rate | interval | phase |
|---|---|---|---|---|---|
| Slovak | 4,064 | — | 51.13 % | [49.58, 52.68] | 2D |
| Czech pooled | 2,700 | 1,416 | 52.44 % | [50.54, 54.34] | 2E |
| Czech cz_0001 | 1,000 | 526 | 52.60 % | [49.45, 55.73] | 2E |
| Czech cz_0002 | 900 | 467 | 51.89 % | [48.57, 55.20] | 2E |
| Czech cz_0003 | 900 | 423 | 52.88 % | [49.35, 56.38] | 2E |
| Czech, the 50 rows added in 2F | 50 | — | **not judged** | — | 2F |

Czech spans rejected for not being a contiguous substring of `en`: 0 (Slovak: 1). Czech `unusable` class: 742.
Cost: Czech 465.6 tok/sentence, Slovak 473.5.

## 4. Rows that exist, per language

| language | rows annotated | of scope | missing | why |
|---|---|---|---|---|
| sk | 4,064 | 4,064 | 0 | — |
| cz | **2,850** | 4,064 | **1,214** | n 5415-5464 (`cz_0002_s04_v` h2, refused 4×); n 6365-6464 (`cz_0003_s04_v`, refused); cz_0004 1,000 rows (429-limited, 875,000 tok for 0 rows in 2F); cz_0005 64 rows (never reached) |
| de, fr, es, tr, hu, ua | 0 | — | all | not started |

Czech production corpus, SELECT-only count: **39,498** (A1 9,999 / A2 13,591 / B1 8,906 / B2 7,002).
Annotated-or-excluded: 4,552 ids; remaining candidates 34,966.

## 5. Per-sentence cost

| item | Slovak | Czech |
|---|---|---|
| annotation + `lk`, both passes | ≈ 1,683 tok/row (2D: 6.84 M / 4,064) | 885 tok/row (2E, mostly pre-paid in 2D) |
| annotation alone, healthy | — | 1,379 tok/row (2F) |
| annotation alone, 429-limited chunk | — | 29,322 tok/row (2F, cz_0004) |
| `lk` pass | 473.5 tok/sentence | 465.6 tok/sentence |
| 100 sentences annotated cold, in-driver | — | 310,134 tok (2F §2) |

## 6. Ready to upload

`phase2f/out/upload_cz_final.xlsx` — sheet `cz`, **2,850 rows**, columns `exercise_id`, `language_code`,
`level`, `src`, `en`, `structure_json`. Largest `structure_json` cell **2,936** chars against Excel's
**32,767**. `phase2f/out/annotations_cz_final.jsonl` 2,850 lines. `phase2d/out/upload_sk_final.xlsx`
4,064 Slovak rows, already uploaded. **Nothing in 2F was uploaded and nothing was written to the database.**

## 7. Gemini

| phase | counted calls | failed | spend at list |
|---|---|---|---|
| 1W | 794 of 1,200 cap | 0 | $0.066 |
| 2F §3.1 | 312 | 0 | $0.0163 |
| 2F §2 | 0 (set never opened) | — | $0 |

## 8. The three decisions still open

1. **The other six languages.** 2F §3.2 prices them at 28,340,000 tokens in total (low bracket 24,818,000),
   of which 14.6 M (52 %) is engineering: ua 3,890,000 · es 4,290,000 · fr 4,490,000 · de 4,690,000 ·
   tr 5,490,000 · hu 5,490,000. 2E's condition — do not start until the refused-chunk defect is diagnosed —
   is now partly met (2F §1.2) and partly not (the cause is localised, not explained).
2. **The 771 concepts with no grammar sentence.** Unchanged; no work done in 2F.
3. **The `unusable` `lk` content question.** 742 Czech rows and the Slovak equivalent: stored answers that
   are numerals, conjunctions or relative pronouns rather than verb phrases — data defect or a judge scoped
   too narrowly. Nothing has been overwritten.
