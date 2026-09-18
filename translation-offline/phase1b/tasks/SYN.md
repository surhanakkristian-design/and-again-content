# Task: GLOBAL synonym table (Opus). Budget: at most ~15 tool calls.
Write `synonyms/table.json` in the FORMAT_SPEC §1 format.
Sources: (a) the Phase 1 acceptable lists — extract every {a|b|…} slot from `../pilot/generated/*.json` field `acceptable`
with ONE python one-liner that prints distinct alternations with counts (do not read the files one by one);
(b) the 45 false rejections in ~/Projects/and-again/docs/features/reports/TRANSLATION_OFFLINE_PHASE1_REPORT.md lines 1236–1290
(near/beside, stapled/clipped, motionless/still, lifted/raised, somebody/someone, demands/requests, pedestal/stand, …);
(c) your own knowledge of common A1–B2 English synonyms a Slovak/Czech learner would plausibly choose for one native word.
Rules:
- safe: interchangeable in EVERY English sentence (someone/somebody, anyone/anybody, everyone/everybody, no one/nobody,
  have to/have got to, …). Strict and short (≤ ~30 groups). If you can think of one sentence where the swap changes meaning or
  sounds wrong, it is contextual.
- contextual: aim for ~400–600 groups covering common verbs, nouns, adjectives, adverbs, prepositions and short phrases
  (near/beside, lift/raise, still/motionless, stapled/clipped, big/large, huge/enormous/gigantic, quickly/fast, shout/yell,
  put/place, look at/watch …). Every group: `ok` = one sentence where the swap is valid, `bad` = one where it is not.
- Members are lemmas; set `pos`; give `irr` for irregular verbs/nouns/adjectives; `head` for multi-word verbs if not index 0.
- Never group the grammar structures the exercises practise (can/be able to, will/going to, must/have to, who/that,
  much/many, some/any, used to/would …) — those are variants or library mistakes, not synonyms.
- A member may appear in several groups (different senses), but group ids must be unique, snake_case, descriptive.
Then run `python3 scripts/make_indexes.py`. Final message: counts by kind + file size.
