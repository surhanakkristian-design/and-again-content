# Phase 1h — notes on the 60 new annotations

Pipeline unchanged from Phase 1c: spec `GENERATION_SPEC.md` + `phase1c/BRIEF.md` §4, task prompts
`phase1c/tasks/batchS.md` / `batchL.md`, template `phase1c/annotated_after/10013.json`.
Nothing from `phase1g/` (report, remaining errors), the checker source or `reference_hygiene.py` was read,
so the annotations are not shaped by the checker's known errors. Hygiene was NOT pre-applied.

- **`s` (synonym-group ids) is omitted.** The batchS/batchL prompts that produced the 80 do not contain
  `s`; it was added afterwards by the §4.1 synonym review. Inventing new `ng1c_*` ids would be a new
  artefact, so every alternative is carried in `alt`, as the annotators wrote it.
- `ans` (the practised span) is not given in `new_sentences_60.jsonl`, so `lk` was chosen per topic the
  way Phase 1c locked it (aux+verb for the continuous/perfect topics, the article phrase for t6, the
  question word for t9, the if-clause verb for the 2nd/3rd conditionals, the result verb for Mixed).
- Gender chains `g` only where the Slovak leaves person/gender open: 14779, 7708, 8618, 10124, 5971,
  6790, 6883. Everywhere else an l-participle (`bola`, `premenila`, `nebola`, `Mala`, …) or a pronoun
  fixes it.
- Doubtful sentences (flagged for the judge, not resolved here):
  - **8465** `Keby ten sud nebol prevrátil…` — `sud` can be read as subject ("if that barrel had not
    tipped over") or as object of an omitted masculine subject. Read as transitive (no `sa`), hence
    "If he had not tipped that barrel over". The result clause is present-time, so 53.07/53.06 apply.
  - **31648** `vraj` rendered as "apparently" / "they say"; both are in `v`.
  - **3332** `overal` rendered "jumpsuit" with `alt` overall(s)/boiler suit/coveralls.
  - **7910** `zopnutá kopa` = a clipped/fastened pile of paper; rendered "the clipped pile" + `alt`.
  - **9584** `od chvíle, keď vyštartovala` kept literal ("since the moment she started"); the Phase 1c
    sentence of the same family used a starting gun, which the Slovak here does not mention.
  - **6265** `Nobody` — "No one" is NOT listed in `alt` because the prompt forbids someone/somebody-type
    pairs; if the matcher does not normalise them this will cost a false rejection.
