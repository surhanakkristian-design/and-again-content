# Phase 2C GATE 1 - three reader fixes, re-validated on 2B's frozen sample

0 Gemini calls, 0 headless sessions, 0 DB access, 0 new gold. Sample = `phase2b/sample_2b.json`
(200 rows, sk 1-100 / cz 101-200); gold = 2B's blind gold `phase2b/run_2b_results.json`
`outputs.gold_sk` / `outputs.gold_cz` (run 2 - the run `results_2b.json` scored).

## Entry point (for the production runner)

    import derive_2c
    out = derive_2c.derive(row, lang=None, mode="after")

`row` = {"n": int, "lang": "sk"|"cz", "src": str, "en": str, "level": str} (`lang=` fills/overrides
`row["lang"]`). `mode`: `"after"` (all three patches, the production setting), `"before"` (byte-identical
2B behaviour), or `"tok"`/`"verbish"`/`"agent"` (single-patch ablation), or a dict
`{"tok":bool,"verbish":bool,"agent":bool}`.

Output schema = **exactly** `phase2b/derive_2b.derive()`'s, so everything `run_2b.py` consumed keeps working:

* `reader`: `agent`, `why`, `clause`, `feats`, `agent_on_fallback_clause`
* `derived`: `agent_nom`, `finite_verb`, `person`, `number`, `gender`, `tf` (+`frames`), `tense_open`,
  `perfective_present`, `voice_sk` - each `{"value": ..., "source": str}`, `value is None` = abstain
* `voice_paths`: `g4_v2_sk_reflex`, `g4_v3_passive_or_reflex`, `g4_cz_se_missed`, `agv4_sk_clause_passive`,
  `agv4_sk_clause_reflex`, `agv4_main_passive`, `agv4_main_reflex`, `agv4_en_passive`,
  `agv4_en_passive_span`, `reader_nom_full_agent` - the AG v4 + reader_nom paths
* `rewrite`: `action` (`U`/`R`/`ABSTAIN`), `new`, `pronoun`, `where`, `reason`, `check` - the arm-B script
  rewrite. `derive_2c.main()` renames `new` -> `sk_new`/`cz_new` exactly as `derive_2b.main()` did.

Frozen code is never edited: `phase1*/`, `checker/` and `phase2b/` are imported and monkeypatched in
memory by `derive_2c.patches()`; the patched `_decide_clause` copy lives in `phase2c/derive_2c.py`.

## The three fixes

1. **P3 / DERIVE #3 `agent`** - `reader_nom._decide_clause` returned non-nominatives. Patched copy:
   a pronoun form that is also a determiner and stands before a noun (adjectives skipped) is a determiner,
   not the pronoun (cz `ty rybky`); NP heads are rejected when they are closed-class adverbs, particles,
   conjunctions or subordinators (incl. the generated `kdyby-`/`aby-` conditional paradigm and the
   "stem + `ze`" conjunction rule), deictic obliques in `-hle`, preposition-governed forms, or bare
   long-form adjectives without a head noun. Nothing survives -> abstain (frozen behaviour).
2. **P1 / DERIVE #1 `tok`** - `f9.WORD` is replaced by `[a-z + the full Czech+Slovak diacritic set]`
   (adds r-hacek and u-kroucek, plus o/u-umlaut), on BOTH f9 module objects (Slovak `f9_1n` and the
   `cz_reader.build()` copy), so `tok`, `_is_l_part`, `sk_frame`, the CZ_PERF aspect lexicon and
   `reader_nom._lpset` all see whole Czech words. Verified: `Rekne mu domu` -> `['řekne','mu','domů']`.
3. **P2 / DERIVE #2 `verbish`** - `reader_nom._verbish` wrapper: a token that is not a byt-copula, a modal
   or an l-participle loses its verb reading when it is preposition-governed in the sentence
   (`po pobreznej ceste`), capitalised but not sentence-initial, or ends in `-s` without a real 2sg
   present ending (`Kamos`).

Not touched, by instruction: **`tense_open`** (2B DEFECTS_score #3 - a definition mismatch, not a reader
bug: the script reports the f9 frame-set size, the gold reports "more than one English tense acceptable",
and the gold itself flips on 13/100 sk rows). It stays a model field. The `tf` "conditional" emission
(DEFECTS_score #2 - the gold schema only has past/present/future) was also left alone; see below.

## Before / after (ERROR-of-decided = ERROR / (AGREE + ERROR), exact 95 % Clopper-Pearson)

A/C/E = AGREE / CONSERVATIVE (script abstains) / ERROR.

| field | lang | BEFORE A/C/E | BEFORE ERR-of-decided | AFTER A/C/E | AFTER ERR-of-decided | gate |
|---|---|---|---|---|---|---|
| voice_sk | sk | 42/49/9 | 17.65 % [8.4, 30.87] | 42/51/7 | 14.29 % [5.94, 27.24] | - |
| voice_sk | cz | 40/52/8 | 16.67 % [7.48, 30.22] | 39/56/5 | 11.36 % [3.79, 24.56] | - |
| voice_sk | pooled | 82/101/17 | 17.17 % [10.33, 26.06] | 81/107/12 | 12.9 % [6.85, 21.45] | - |
| agent_nom | sk | 37/55/8 | 17.78 % [8.0, 32.05] | 38/57/5 | 11.63 % [3.89, 25.08] | - |
| agent_nom | cz | 28/57/15 | 34.88 % [21.01, 50.93] | 30/62/8 | 21.05 % [9.55, 37.32] | - |
| agent_nom | pooled | 65/112/23 | 26.14 % [17.34, 36.59] | 68/119/13 | 16.05 % [8.83, 25.88] | - |
| person | sk | 67/29/4 | 5.63 % [1.56, 13.8] | 67/30/3 | 4.29 % [0.89, 12.02] | PASS |
| person | cz | 60/32/8 | 11.76 % [5.22, 21.87] | 62/32/6 | 8.82 % [3.31, 18.22] | PASS |
| person | pooled | 127/61/12 | 8.63 % [4.54, 14.59] | 129/62/9 | 6.52 % [3.03, 12.02] | PASS |
| number | sk | 72/26/2 | 2.7 % [0.33, 9.42] | 72/27/1 | 1.37 % [0.03, 7.4] | PASS |
| number | cz | 65/32/3 | 4.41 % [0.92, 12.36] | 66/32/2 | 2.94 % [0.36, 10.22] | PASS |
| number | pooled | 137/58/5 | 3.52 % [1.15, 8.03] | 138/59/3 | 2.13 % [0.44, 6.09] | PASS |
| gender | sk | 38/57/5 | 11.63 % [3.89, 25.08] | 38/57/5 | 11.63 % [3.89, 25.08] | - |
| gender | cz | 19/76/5 | 20.83 % [7.13, 42.15] | 21/74/5 | 19.23 % [6.55, 39.35] | - |
| gender | pooled | 57/133/10 | 14.93 % [7.4, 25.74] | 59/131/10 | 14.49 % [7.17, 25.04] | - |
| tense_open | sk | 71/8/21 | 22.83 % [14.72, 32.75] | 71/8/21 | 22.83 % [14.72, 32.75] | - |
| tense_open | cz | 50/13/37 | 42.53 % [31.99, 53.59] | 51/9/40 | 43.96 % [33.56, 54.75] | - |
| tense_open | pooled | 121/21/58 | 32.4 % [25.61, 39.79] | 122/17/61 | 33.33 % [26.55, 40.67] | - |
| perfective_present | sk | 75/19/6 | 7.41 % [2.77, 15.43] | 75/19/6 | 7.41 % [2.77, 15.43] | PASS |
| perfective_present | cz | 51/47/2 | 3.77 % [0.46, 12.98] | 52/45/3 | 5.45 % [1.14, 15.12] | PASS |
| perfective_present | pooled | 126/66/8 | 5.97 % [2.61, 11.42] | 127/64/9 | 6.62 % [3.07, 12.19] | PASS |
| tf | sk | 66/25/9 | 12.0 % [5.64, 21.56] | 66/25/9 | 12.0 % [5.64, 21.56] | - |
| tf | cz | 38/54/8 | 17.39 % [7.82, 31.42] | 40/53/7 | 14.89 % [6.2, 28.31] | - |
| tf | pooled | 104/79/17 | 14.05 % [8.4, 21.54] | 106/78/16 | 13.11 % [7.69, 20.42] | - |

## GATE 1

Rule: a field may be script-derived in production only if its AFTER ERROR-of-decided **point estimate is
under 10 % on BOTH sk and cz**.

**Passed: person, number, perfective_present**

## Per-fix attribution (ERROR-of-decided %, sk / cz)

| field | before | +tok | +verbish | +agent | after (all three) |
|---|---|---|---|---|---|
| voice_sk | 17.65 / 16.67 | 17.65 / 16.67 | 17.65 / 16.33 | 14.29 / 11.63 | 14.29 / 11.36 |
| agent_nom | 17.78 / 34.88 | 17.78 / 34.88 | 17.78 / 36.36 | 11.63 / 18.92 | 11.63 / 21.05 |
| person | 5.63 / 11.76 | 5.63 / 11.43 | 4.29 / 9.09 | 5.63 / 11.76 | 4.29 / 8.82 |
| number | 2.7 / 4.41 | 2.7 / 4.29 | 1.37 / 3.03 | 2.7 / 4.41 | 1.37 / 2.94 |
| gender | 11.63 / 20.83 | 11.63 / 19.23 | 11.63 / 20.83 | 11.63 / 20.83 | 11.63 / 19.23 |
| tense_open | 22.83 / 42.53 | 22.83 / 43.96 | 22.83 / 42.53 | 22.83 / 42.53 | 22.83 / 43.96 |
| perfective_present | 7.41 / 3.77 | 7.41 / 5.45 | 7.41 / 3.77 | 7.41 / 3.77 | 7.41 / 5.45 |
| tf | 12.0 / 17.39 | 12.0 / 14.89 | 12.0 / 17.39 | 12.0 / 17.39 | 12.0 / 14.89 |

Fields moved by each single fix (counts or rates changed vs before):
{"tok": ["person", "number", "gender", "tense_open", "perfective_present", "tf"], "verbish": ["voice_sk", "agent_nom", "person", "number"], "agent": ["voice_sk", "agent_nom"]}

## Caveat (important)

The three fixes were designed from the defect examples in `phase2b/DEFECTS_derive.md`, and those examples
were drawn from **this same 200-row sample**. The AFTER column is therefore an optimistic **in-sample**
number: it is a regression check that the fixes do what they claim, not a fresh-set measurement of the
patched reader. A production decision at the 10 % bar should be confirmed on rows this sample never saw.

## Defects recorded, not fixed

* `tf` emits `"conditional"`; the gold schema is past/present/future only (2B rows n30, n34) - every
  conditional reading is scored ERROR by construction. Not one of the three named fixes; left as is.
* `tense_open` definition mismatch (see above) - left to the model.
* `phase1t/taskB/cz_validate.py` has its **own** `WORD` regex inside the g1..g4 slice, independent of
  `f9.WORD`; the P1 fix does not reach it. It only feeds `voice_paths` (g4 raw readings), not a scored
  field, so it was left untouched. Recorded in `DEFECTS_gate1.md`.

## Verdict

* **Passed GATE 1 (AFTER, both languages under 10 %): `person`, `number`, `perfective_present`.**
  `person` sk 4.29 % / cz 8.82 %, `number` sk 1.37 % / cz 2.94 %, `perfective_present` sk 7.41 % / cz 5.45 %.
* The three fixes **did help** - every one of them moved something - but **none of the three target fields
  crossed the bar**: `voice_sk` 17.65 -> 14.29 sk, 16.67 -> 11.36 cz; `agent_nom` 17.78 -> 11.63 sk,
  34.88 -> 21.05 cz; `tf` 12.00 -> 12.00 sk, 17.39 -> 14.89 cz. They stay model fields.
* The one field the fixes *converted*: `person` on Czech (11.76 % -> 8.82 %, tok + verbish), which was over
  the bar before and is under it now. `number` and `perfective_present` were already under it.
* `perfective_present` on Czech got slightly **worse** in point terms (3.77 % -> 5.45 %) while its coverage
  rose (53 -> 55 decided): the tokenizer fix hands f9 Czech words it could not read before, so the aspect
  lexicon now fires on rows it used to abstain on. Same direction on `tense_open` cz (42.53 -> 43.96).
* `gender` is untouched by all three fixes (sk 11.63 %, cz 19.23 % -> 19.23 %): its residual errors come
  from somewhere else and would need a fourth, unnamed fix.
* Cell sizes are small (19-75 decided rows per field per language); the Clopper-Pearson upper bounds in the
  table above are the honest statement - e.g. `person` cz 8.82 % has CP95 [3.31, 18.22], so "under 10 %" is
  a point-estimate verdict only, and an in-sample one at that.
