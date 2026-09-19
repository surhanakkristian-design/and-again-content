# Translation production Phase 2B: what each field really costs for sk + cz, and whether the 2A gate was the right gate

19 September 2026. Measurement only. Files: `and-again-content/translation-offline/phase2b/`. That covers `PLAN.md`, `selection_2b_*`, `sample_2b.json`,
`derived_2b.json`, `alt_map_2b.json`, `run_2b.py`, `sessions/*.json`, `run_2b_results.json`, `run_2b.log`, `score_2b.py`, `results_2b.json`,
`retest_2b.py`, `retest_2b.json` and `DEFECTS_*.md`. Every file was committed as it was produced. Nothing was pushed. 0 Gemini calls, DB SELECT only, no migration, no app code, no checker rule changed.

**Headline:**
- **Headless hard cap BREACHED:** 505,884 tokens against 330,000. A resume command failed and re-ran the five finished sessions a second time (§6, S1). The second run was not planned, but it did give a free run-1 vs run-2 retest.
- **Model-authored cost for sk + cz is about 1,033 tokens per sentence at N = 100** (v 476.7 + rewrite fallback 268.5 + lk 245.6 measured, plus 42.6 estimated for residual nulls). That is **36 % of 2A's 2,876.3** (rewrite 1,264.5 + annotation 1,611.8).
- **The derived fields are not production grade.** Error rates on the rows they decide: voice 17.2 %, agent_nom 26.1 %, tf 14.1 %, gender 14.9 %, tense_open 32.4 %. Compare 1.67 % (1W) and 3–4 % (2A).
- **The 2A gate fired on the wrong guard.** The frozen stack's own AG v4 voice path errs on 7.0 % [3.88, 11.47]. The harness guard g4 errs on 11.5–14.0 % raw and 23–26 % after the rewrite. 20 of g4's 23–28 raw errors are the known reflexive `si`/`sa`/`se` pattern.
- **v_cz was never measured.** The in-flight budget check refused it in both runs. Czech v cost is assumed equal to Slovak and marked ESTIMATE.

## 1. Per-field table: who authors each field, and at what cost

Tokens per sentence are all tokens incl. cache reads, over all sentences. M = MEASURED on the 200-row sample (100 sk + 100 cz). E = ESTIMATE.
"Script" = the frozen reader/guards + derive_2b.py, 0 tokens. The shares add up to 100 % per row.

| field | authored by model | derived by script | already in the data | note |
|---|---|---|---|---|
| rewrite | 48.5 % (97/200; sk 46, cz 51): **268.5 tok/sent** over all 200 (M, N = 97; 553.6 per fallback row). At N = 30: 628.6 (E) | 51.5 % (R 14 + U 89): 0 tok, but **12.6 % ERROR** [6.89, 20.62] vs gold | – | model fallback 4.1 % ERROR [1.13, 10.22], 0 machine-check fails |
| lk | 20.5 % need adjusting (judge); a judge pass costs **245.6 tok/sent** (M, N = 200) | – (mechanical check: 200/200 are verbatim substrings, so it cannot tell exact from adjust) | 79.5 % exact [73.23, 84.87] | the v session does NOT fix lk (lk[0] copied 100/100) |
| topic/level | – | – | **100 %**, 0 missing | 61 exercise types in the sample |
| voice_sk | 50.5 % null → rides in v (E) | 49.5 %, ERROR of decided 17.2 % | – | |
| agent_nom | 56.0 % null → rides in v (E) | 44.0 %, ERROR of decided 26.1 % | – | adverbs/demonstratives read as agents |
| person | 30.5 % → v (E) | 69.5 %, ERROR 8.6 % | – | |
| number | 29.0 % → v (E) | 71.0 %, ERROR 3.5 % | – | |
| gender | 66.5 % → v (E) | 33.5 %, ERROR 14.9 % | – | |
| tense_open | 10.5 % → v (E) | 89.5 %, ERROR 32.4 % | – | definition mismatch, gold itself unstable |
| perfective_present | 33.0 % → v (E) | 67.0 %, ERROR 6.0 % | – | |
| tf | 39.5 % → v (E) | 60.5 %, ERROR 14.1 % | – | derive emits "conditional", gold never does |
| alt | 40.4 % unmapped tokens (491/1,214), tokens not isolated (E) | 2.6 % propose_new (31) | 57.0 % mapped (692) | rough match, sense not checked |
| v | **100 %: 476.7 tok/sent** (M, N = 100, sk only); 252.1 excl. cache read; at N = 30: 1,221.9 (E) | – | – | v[0] = reference 100/100 |

Residual nulls average 3.15 fields per sentence. Riding in the v session at about 13.5 output tokens per field, that is **+42.6 tok/sent (E)**.

## 2. Measurements

The gold is a blind Opus session per language that sees only the source sentence (2A's GOLD + DEF, with the language named and the schema extended).
**Caveat:** gold and every model-authored field come from the same model family (Opus). This is **self-consistency, not independent accuracy.**

- **Retest (the unplanned second run).** Gold run 1 vs run 2, tf + person + voice + subject all identical: sk 100/100, cz 99/100.
  - Unstable fields: tense_open 87/100 (sk) and 96/100 (cz); gender 99/100 and 95/100.
- Gold meta:
  - sk: 17 multi-sentence items (6 labelled on a sentence other than the first), 0 fragments.
  - cz: 13 multi-sentence items (4), 2 fragments.
  - Voice: sk 56 active_agent / 43 prodrop / 1 impersonal; cz 60 / 35 / 2 passive / 3 impersonal.

### 2.1 lk (judge sees en + correct_answer_en only)
- Judge (run 2, scored): exact **159/200 = 79.5 % [73.23, 84.87]**, adjust 41 = 20.5 % [15.13, 26.77], unusable 0.
  - sk 81/19, cz 78/22.
  - By level, exact/adjust: A1 46/4, A2 39/11, B1 32/18, B2 42/8.
- Run 1 said exact 169 (84.5 %). The class was the same on 188/200 rows.
- Mechanical check: 200/200 are verbatim, case-sensitive substrings of en. The check cannot separate exact from adjust.
- The adjust cases are trimming or extending the span, never replacing it:
  - "is going to" → "is going to find"
  - "many" → "How many"
  - "is" → "There is"
  - trailing full stops: "her eye." → "her eye"

### 2.2 topic + level
- 200/200 rows carry type title and level. 0 missing.
- The selection hits every available topic per level (A1 11/11, A2 15/15, and so on).

### 2.3 derived fields vs blind gold (pooled; sk / cz). ERROR of all rows and of decided rows (non-null)

| field | A/C/E pooled | ERROR of all | ERROR of decided | coverage | sk ERROR dec. | cz ERROR dec. |
|---|---|---|---|---|---|---|
| voice_sk | 82/101/17 | 8.5 % [5.03, 13.26] | 17.17 % [10.33, 26.06] | 49.5 % | 17.65 % | 16.67 % |
| agent_nom | 65/112/23 | 11.5 % [7.43, 16.75] | 26.14 % [17.34, 36.59] | 44.0 % | 17.78 % | 34.88 % |
| person | 127/61/12 | 6.0 % [3.14, 10.25] | 8.63 % [4.54, 14.59] | 69.5 % | 5.63 % | 11.76 % |
| number | 137/58/5 | 2.5 % [0.82, 5.74] | 3.52 % [1.15, 8.03] | 71.0 % | 2.70 % | 4.41 % |
| gender | 57/133/10 | 5.0 % [2.42, 9.00] | 14.93 % [7.40, 25.74] | 33.5 % | 11.63 % | 20.83 % |
| tf | 104/79/17 | 8.5 % [5.03, 13.26] | 14.05 % [8.40, 21.54] | 60.5 % | 12.00 % | 17.39 % |
| tense_open | 121/21/58 | 29.0 % [22.82, 35.82] | 32.40 % [25.61, 39.79] | 89.5 % | 22.83 % | 42.53 % |
| perfective_present | 126/66/8 | 4.0 % [1.74, 7.73] | 5.97 % [2.61, 11.42] | 67.0 % | 7.41 % | 3.77 % |

- **Only number and perfective_present come near the reference bars** (1W blind Slovak 1.67 %; 2A reader_nom 3–4 %). All other fields miss them by a wide margin.
- Multi-sentence items explain few of the errors (voice 4, tf 4, tense_open 9).
- agent_nom errors come from DERIVE defect #3, which is confirmed. Non-nominatives are read as agents: `Zvyčajne`, `vraj`, `Takto`, `zábere`, and Czech `ty rybky` (a demonstrative, not the pronoun).
- tense_open is mostly a definition mismatch. The script uses the f9 frame-set size. The gold judges "more than one English tense acceptable", and is itself unstable on retest.

### 2.4 alt (from alt_map_2b.json, rough match, sense not checked)
- Mapped 692 / propose_new 31 / unmapped 491 content tokens.
  - A1: 135/3/100
  - A2: 172/9/84
  - B1: 189/8/139
  - B2: 196/11/168
- 198/200 rows have at least one mapped word. "Mapped" means a group exists for the surface word, not that the sense fits (ring → call_phone_ring in "a ring of small fish").

### 2.5 v alone (every other field supplied)
- v_sk, N = 100, MEASURED: **476.7 tok/sent**, 252.1 excl. cache read, 71.4 output. This is 29.6 % of 2A's 1,611.8 and 35.3 % of its 713.3.
  - Run 1 measured 491.7, with 86.2 output.
- Decomposition: a least-squares fit over the 5 sessions puts fixed system context at about 9.4 k cache creation + 22,462 cache read. Marginal input is 0.365 tok per character.
- The N = 30 equivalent is an **ESTIMATE**: 1,221.9 tok/sent (75.8 % of 1,611.8) and 473.2 excl. cache read (66.3 % of 713.3). At N = 30 the fixed ~32 k context dominates, so **run v at N ≥ 100.**
- Quality: v[0] = reference 100/100. Two variants given on 76/100 (run 1: 61). Only 35/100 v lists were identical across runs.
- **v_cz is not measured** (refused twice by the budget pre-check). Czech is assumed equal to Slovak.

### 2.6 rewrite
- Script handled R + U on 103/200 = 51.5 % (sk R8/U46, cz R6/U43). The model got the ABSTAIN rows: sk 46, cz 51.
- **Script accuracy vs gold: 90/103 = 87.38 % [79.38, 93.11]; ERROR 12.62 % [6.89, 20.62].** sk 7/54, cz 6/49.
  - R rows: 13/14 agree.
  - U rows: 12 errors. The script left a pro-drop sentence untouched because the reader supplied a false agent (`Zvyčajne`, `Takto`) or read an embedded/quoted subject (n42 „…ja vymením…“ rozhodne sa).
- **Model fallback (2A REWRITE, sk + cz): 93/97 = 95.88 % [89.78, 98.87].** R-main 51, R-embedded 6, U 40. 0 machine-check failures, 57 rewrites applied.
  - Retest: same action on 96/97, identical text on 93/97.
- Tokens: the fallback session cost 53,695. That is **268.5 per sentence over all 200** (21.2 % of 2A's 1,264.5) and 553.6 per fallback row at N = 97. The N = 30 ESTIMATE is 628.6 per sentence over all.

## 3. g4 verdict: the frozen AG v4 path beside g4 (same 200, 2A's exact method, reader_nom full installed)

| guard | before (raw) ERROR | sk | cz | after (rewritten) ERROR | sk | cz |
|---|---|---|---|---|---|---|
| **AG v4 voice path (frozen stack)** | **14/200 = 7.0 % [3.88, 11.47]** | 9.0 % [4.20, 16.40] | 5.0 % [1.64, 11.28] | not computed (raw only) | | |
| g4_v2 (harness) | 23/200 = 11.5 % [7.43, 16.75] | 9.0 % | 14.0 % [7.87, 22.37] | 46/200 = 23.0 % [17.36, 29.46] | 22.0 % | 24.0 % |
| g4_v3 (harness) | 28/200 = 14.0 % [9.51, 19.59] | 12.0 % | 16.0 % | 52/200 = 26.0 % [20.07, 32.66] | 26.0 % | 26.0 % |
| reader_nom full (g3cls) | 11/200 = 5.5 % [2.78, 9.63] | 3.0 % | 8.0 % [3.52, 15.16] | 16/200 = 8.0 % [4.64, 12.67] | 5.0 % | **11.0 % [5.62, 18.83]** |

- **Causes of the g4 errors:**
  - g4_v2 raw: 20 reflexive `si`/`sa`/`se` with an overt nominative, 3 other.
  - g4_v3 raw: 20 reflexive, 2 multi-sentence, 6 other.
  - After the rewrite, 43 of the 46/52 errors are reflexive: an inserted pronoun turns a pro-drop reflexive into "overt subject + `sa`".
  - Direction is almost entirely ERROR_as_passive (v3 raw 26/28).
- **AG v4 errors:** 12 read as passive, 2 read as active.
  - Causes: 3 reflexive with an overt subject, 2 multi-sentence, 9 other.
  - The "other" group is mostly **pro-drop** reflexives such as "Stan by si mal postaviť…" and "Nemohla sa dočkať…". The cause classifier only counts reflexives with an overt gold subject.
- **Should 2A's gate have fired?** By the letter of the brief ("any guard"), yes. On the substance, no. g4 is the validation harness's guard built over AG v2/v3, not the production path, and its error is one known pattern that the arm-B rewrite amplifies by construction.
  - The production path (AG v4) is at 7.0 % on the point. Its upper bound of 11.47 % does not clear the 10 % bar, so it **passes on the point only**.
- **Should the 10 % bar apply to g4 at all?** No, not as a stop gate. 1W measured the stack end to end on fresh data: SKP coverage 97.22 %, by-passive coverage 98.75 %. g4's reflexive misreading does not show up there.
  - Recommendation: gate on AG v4 + reader_nom. Record g4 as a harness defect.
- **New finding:** reader_nom full on **Czech after the rewrite is at 11.0 %**, over the bar on the point. 7 of the 11 are "other" errors from the Czech reader. The Slovak reader holds at 3.0 % / 5.0 %.

## 4. Re-extrapolations

**Per-sentence basis for sk + cz production (model-authored only), at N = 100:**

| component | tok/sent | status |
|---|---|---|
| v | 476.7 | MEASURED, sk; cz assumed equal (E) |
| rewrite fallback over all rows | 268.5 | MEASURED |
| lk judge pass | 245.6 | MEASURED, N = 200 |
| residual derived-field nulls riding in the v session | 42.6 | ESTIMATE |
| **total** | **1,033.4** | (584.2 excl. cache read) |

**Timing basis:** v 0.54 s/sent, fallback 1.14 s/row, lk 0.31 s/sent, 4 parallel. The 6 natives use 2A's measured rewrite + annotation 2,876.3 tok/sent and 4.34 s/sent, N = 30; that part is an ESTIMATE.

| scenario | sentences | tokens (all) | excl. cache read | sessions | serial | wall at 4 parallel |
|---|---|---|---|---|---|---|
| **attainable now, sk + cz** (4,109 × 2) | 8,218 | **8.49 M** | 4.80 M | 83 v + 40 fb + 42 lk = 165 | 3.2 h | **0.8 h** |
| sk + cz target (7,200 × 2) | 14,400 | **14.88 M** | 8.41 M | 144 + 70 + 72 = 286 | 5.6 h | **1.4 h** |
| variant 2: sk + cz + 1,000 concepts × 6 natives | 20,400 | **32.14 M** (14.88 + 17.26) | – | 286 + 400 = 686 | 12.8 h | **3.2 h** |
| variant 1, reference only (v for 7,200 × 8) | 57,600 | **27.46 M** (+14.15 M if lk is judged) | 14.52 M | 576 (+288) | 8.6 h | **2.1 h** |

- **Assumptions:**
  - Linear in sentences.
  - The ABSTAIN share stays at 48.5 %.
  - Czech v cost equals Slovak.
  - Residual nulls ride in the v session at marginal output cost (ESTIMATE).
  - Session start-up is not modelled.
  - At N = 30 instead of N = 100, sk + cz costs about 1,937 tok/sent (ESTIMATE), i.e. 27.9 M for 14,400.
- **What remains model-authored:**
  - sk + cz: v (with lk corrections and the residual nulls) and the rewrite for about half the rows.
  - Natives: everything. No reader, rewrite script or guard exists for them.
  - Variant 1: only v. This is the only scenario with no derived fields to trust.
- **Guards for a non-Slavic native** (ua / es / tr / hu / fr / de):
  - Each would need its own nominative/agent reader, a voice path and a tense-frame table, then a blind-gold validation like this one. 1T showed that Czech alone, a close Slavic sibling, needed its own reader to fix four named bugs, and ua has none despite being Slavic.
  - es/tr/hu are pro-drop, so they also need a rewrite rule and a pronoun table. fr/de are not pro-drop, but their passive and reflexive (se/sich) patterns would reproduce g4's failure.
  - Until then, native rows are model-only with no guard, i.e. 2A-style cost and no gate.

## 5. Selection rule for the 7,200, and its relation to 39,498 and 5,895
- **Rule:** rank concepts by md5(concept_id||'phase2b-concept'), then take 3,600 of them.
  - An A-concept gets one A1 and one A2 grammar-topic exercise. A B-concept gets one B1 and one B2.
  - Within a (concept, level), pick the lowest md5(concept_id||exercise_id||'phase2b'), ties by exercise_id.
  - Sentences come from `exercise_localizations`; no `sentence_translations` table exists live.
  - word_concepts has no level column, so the concept level is derived from the vocabulary exercise level (A 1,600 / B 1,457).
- **7,200 is unattainable.** The DB has 3,057 concepts and only 2,286 have any grammar sentence.
  - The rule yields **4,109** per language: 1,823 concepts × 2 + 463 × 1. 771 concepts get 0.
  - Shortfall: 3,091.
- **39,498** is 2A's in-scope count (1W Track B SQL: every sk + en full_sentence A1–B2). The 4,109 is a concept-balanced subset of it, at most 2 per concept: 10.4 %.
- **5,895 is still unreproducible.** 2,139 probed counts produced no exact hit. Its only origin is PROJECT_HANDOFF_CHAT.md ("about 5,895 sentences").

## 6. Defects recorded (not fixed)
**DATA** (DEFECTS_data.md):
1. No live `sentence_translations` table.
2. No concept level column.
3. 7,200 unattainable (4,109).
4. The synonym-group table is not live. It exists only as phase1b table.json with 863 groups; "862" was "862 M" tokens.
5. The Czech code is `cz`, not `cs`.
6. 5,895 is unreproducible.
7. 2A's excluded list was incomplete (488 vs 470; union 1,487).
8. B2 topic imbalance (16..106 per topic).
9. The alt map is heuristic (no lemmatizer).

**DERIVE** (DEFECTS_derive.md):
1. The f9 Czech tokenizer drops ř/ů. This is the likely cause of Czech tf coverage at 46 %.
2. `_verbish` accepts nouns as finite verbs (`ceste`, `Kámoš`).
3. reader_nom full returns non-nominatives as agents.
4. reader_nom abstains on clauses without person/number feats (3sg present).
5. g4 cannot classify without a gold dict.

**SCORE** (DEFECTS_score.md):
1. **Headless hard cap breached, 505,884 vs 330,000.**
   - v_cz was refused by the in-flight pre-check: 100,646 + 4 × 60,000 > 330,000. The plan's 6 × EST 60 k = 360 k never fit the cap with 4 parallel.
   - My resume patch failed its own assertion: the pattern `for k in ORDER}` also matched the PROMPT_SHA line.
   - The chained shell command then ran the unpatched runner, which ignores argv and re-ran all five sessions (+253,410). v_cz was refused again.
   - Run 1 is preserved in git history (8c4dec5, 4b16b70, be45947, 1299914, 8b386f9). `run_2b_results.json` and `results_2b.json` hold run 2.
2. The derived tf emits "conditional", which the gold schema (past/present/future) never produces. It is counted as ERROR (n30, n34).
3. tense_open definitions differ: the script uses the f9 frame-set size, the gold uses "more than one English tense acceptable". The gold itself flips on 13/100 sk rows.
4. agent_nom: `ty rybky` (demonstrative) is read as the pronoun `ty`, and adverbs are read as agents. Czech ERROR of decided is 34.9 %.
5. The v prompt copies lk[0] from the supplied value on 100/100 rows, including the 41 the judge says need adjusting. lk correction does not come free inside v.
6. The g4 cause classifier counts "reflexive" only with an overt gold subject, so pro-drop reflexives land in "other".
7. The AG v4 path was read on raw text only (derive_2b). There is no "after" figure.
8. reader_nom Czech after the rewrite is at 11.0 %, over the 10 % bar on the point.

## 7. Tokens, sessions, harness calls
- **Headless (runner, `claude` 2.1.275, --model opus, 4 parallel):** 10 sessions in 2 runs, 0 retries, 0 failures, 1 session (v_cz) refused twice.
  - Run 1: 252,474 tokens.
  - Run 2: 253,410 tokens. The scored run.
  - **Total 505,884** against the 330,000 hard cap: **BREACHED by 175,884**.
  - Per session (run 1 / run 2): gold_sk 52,900 / 50,888; gold_cz 49,759 / 52,031; lk_judge 49,089 / 49,126; rewrite_fallback 51,557 / 53,695; v_sk 49,169 / 47,670.
- **Sub-agents:**
  - DATA: 121,191 tokens, 9 calls.
  - DERIVE: 137,140 tokens, 11 calls.
  - RUN + SCORE + REPORT: "<filled by main session>" tokens, 11 calls of 12.
- Main session: 8 tool calls of 16.
- PHASE_TOTAL_PLACEHOLDER
- Gemini calls 0. DB SELECT only (DATA agent). Nothing pushed, no migration, no app code, no checker rule changed.

## 8. Judgement
1. The real model cost of sk + cz is about 1,033 tok/sent at N = 100. That is 8.5 M tokens and about 0.8 h for the 8,218 sentences that actually exist, or 14.9 M for the unattainable 14,400. Either way it is about 36 % of 2A's per-sentence cost.
2. Still model-authored: v on every row, the rewrite on about half, lk corrections on 20 %, and every derived field the script leaves null (3.15 per sentence).
3. The derived fields the script does decide are too error-prone to ship unreviewed. Only number (3.5 %) and perfective_present (6.0 %) are near the bar. Voice, agent_nom, tf, gender and tense_open need the model or a reader fix.
4. The 2A gate should be lifted for g4, a harness guard with one known reflexive defect. Re-gate on the frozen AG v4 path (7.0 %, passes on the point only) and on reader_nom, which is fine for Slovak but at 11.0 % for Czech after the rewrite.
5. The other six languages would each need a reader, voice path and tense table built and blind-validated, as Czech needed four fixes of its own. Until then they are model-only at about 2,876 tok/sent with no guard at all.
6. The gold is Opus judging Opus. Every rate here is self-consistency, and the budget breach (S1) must be counted against the phase total.
