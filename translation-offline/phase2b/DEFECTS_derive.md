# Phase 2B DERIVE - defects found in frozen code (RECORDED ONLY, nothing changed)

1. **f9 Czech tokenizer drops ř and ů** (phase1n/f9.py `WORD`, reused unpatched by phase1v/trackC/cz_reader.build()).
   `cz f9.tok('Řekne mu domů, že přijde.')` -> `['ekne','mu','dom','že','p','ijde']`. Every Czech word with ř/ů is
   split/truncated before tense, aspect (CZ_PERF `řekne`, `přijde`...) and l-participle reading. Likely cause of the low
   Czech `tf` yield (46/100 cz vs 75/100 sk). Affects cz g1 and reader_nom `_lpset` on Czech.
2. **reader_nom `_verbish` accepts nouns as finite verbs**: VEND `-ete` matches the locative `ceste` (n 44
   "po pobrežnej ceste" -> read as 2pl); checker_1i.sk_features `-š` rule makes the Czech noun `Kámoš` 2sg (n 164).
   Short verbs (`ide`, len<4) are never verbish. derive_2b guards this with an EN-pronoun cross-check (-> ABSTAIN).
3. **reader_nom full returns non-nominatives as agents** (noun-preverbal step): adverbs/particles `Zvyčajne`, `Takto`,
   `vraj`, `prý`; subordinators `kdybych`, `což`, `Nejenže`; oblique `touhle`, `zábere`; bare adjectives `široké`,
   `úžasný`. Harmless for the rewrite (row goes U = untouched), but they count as `active_agent` in voice_sk and as
   agent_nom values - the scorer must not trust agent_nom as gold-quality.
4. **reader_nom.read abstains on every clause without person/number feats** (e.g. 3sg present: checker_1i.sk_features
   emits no 3sg-present signal), returning `no main clause with a finite verb` before the noun-agreement step runs.
   derive_2b adds a fallback clause and runs the frozen `_decide_clause` on it with the table's feats (labelled in
   `derived.agent_nom.source`); raw reader output is kept separately in `voice_paths.reader_nom_full_agent`.
5. **g4 cannot classify without a gold dict** (cz_validate.g4 indexes `g["voice"]`); derive_2b calls it with a dummy
   gold and keeps only the raw readings `sk_reflex` (v2) and `v3_passive_or_reflex` (v3). g4 has a Czech path only via
   the cz_reader-built V2/V3 (the `se` patch); `czech_se_missed_by_SK_REFLEX` = 0/100 on cz with that path.
