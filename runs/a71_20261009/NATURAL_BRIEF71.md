# A71 naturalness review (decision 450 - every content run)

You did not write these texts. For EVERY English phrase and sentence of the 8 lab items (files `audit/after1_<id>.json`:
ex1 phrases, ex2 nouns, ex3 captions + model captions, ex4 map phrases / rows / own row, ex5 story parts, story models,
phrase list) ask: **would a native (US) speaker say exactly this?** Mark each `ok` or `rewrite` with a better version.

Hard limits for every rewrite (the texts were written to them; a rewrite that breaks one is useless):
- **Level A items (8055, 236, 7071, 8056, 62):** every word at most A2; present simple / continuous, past simple, going to,
  can only (no will / would / could / have + participle); sentences of at most 12 words. Notably these words are ABOVE A2 in
  the owner's Excel and must not be used: hang, suddenly, feed, sail, collar, puddle, gym, lift, bow, look at, put in,
  stare, picnic, hot-air balloon, striped, huge, giant, round.
- **Level B items (8039, 900001, 900002):** the practised words (ex1 phrases, ex2 nouns, ex3 captions, ex4 box answers,
  ex5 phrase list) must be B1 or higher - no A1 words (woman, man, window, snow, glass, cake, play-a-game, music, piano,
  sit, wear, give...), at most one A2 word per item (8039: lose; 900001: doughnut; 900002: violin).
- **Rule A71-5 (nouns):** the mind map of a noun item holds only ONE adjective / noun in front of the key word ("a park
  bench"); a row with the key word is "to [verb] ... key word" with the verb as the white box; the key word is never a box.
- **Rule A71-4:** exercise 4's own row is exactly the caption of picture `ex3_writeAt` (one box); for the verb (900001) and
  the adjective (900002) that caption stands in the timeline / map instead.
- Every text must be true of the video / picture (do not add details). Captions of nouns / adjectives are SHORT phrases;
  a verb's captions are full sentences in their tense (past / present / future).
- Exercise 5's story: one story in 3 parts (a, b, c), level A at most 20 words, B at most 25 (b at most 10 / 15 words),
  exactly one sensible order of the parts.

Write `review/natural71.json`: `{ "<id>": [{ "where": "...", "text": "...", "verdict": "ok"|"rewrite", "better": "...",
"why": "..." }] }` - one entry per text. Reply with the count of rewrites per item and the 5 most important ones.
