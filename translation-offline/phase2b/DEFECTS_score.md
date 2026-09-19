# Phase 2B RUN+SCORE defects (recorded, not fixed) — 19 Sept 2026

1. **Headless hard cap breached: 505,884 vs 330,000.** v_cz was refused by the in-flight pre-check (100,646 + 4 x 60,000 > 330,000;
   the plan's 6 sessions x EST 60k = 360k never fit the cap at 4 parallel). The resume patch failed its own assertion (`for k in ORDER}`
   also matched the PROMPT_SHA line); the chained shell command then ran the UNPATCHED runner, which ignores argv and re-ran all five
   finished sessions (+253,410). v_cz refused again. Run 1 session files are in git history (8c4dec5 gold_sk, 4b16b70 gold_cz,
   be45947 lk_judge, 1299914 rewrite_fallback, 8b386f9 v_sk); run_2b_results.json / results_2b.json hold run 2. retest_2b.json compares both.
2. Derived tf emits "conditional"; the gold schema (past/present/future) never does -> counted ERROR (n30, n34).
3. tense_open: script = f9 frame-set size, gold = "more than one English tense acceptable"; gold itself flips on 13/100 sk, 4/100 cz rows.
4. agent_nom: demonstrative `ty rybky` read as pronoun `ty` (n106); adverbs/particles as agents (Zvyčajne, vraj, Takto, zábere). cz ERROR of decided 34.9 %.
5. The v prompt copies lk[0] from the supplied value 100/100, including the 41 rows the judge marks adjust: lk correction is not free inside v.
6. score_2b cause classifier counts "reflexive" only with an overt gold subject; pro-drop reflexives (AG v4 n34, n53, n58, n63) land in "other".
7. AG v4 voice path read on raw text only (derive_2b); no after-rewrite figure.
8. reader_nom full on Czech after rewrite: 11/100 = 11.0 % [5.62, 18.83], over the 10 % bar on the point.
9. v_cz never measured: Czech v cost assumed = Slovak in every extrapolation (ESTIMATE).
