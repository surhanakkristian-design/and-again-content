# A56 native caption verifier (one language per verifier)

App: a language-learning app. Video 624 teaches the English verb "to run" (a young woman runs after her hat that the wind
blew away). Its picture carousel has three captions; each picture is an edit of the video's still. The third picture
shows the same young woman running along a street to catch a city bus that is about to leave from a stop.

Captions of 624 and their current native versions (already verified, for context and consistency):
- "ran after a hat" (past simple) -> see `current` below
- "will run after a hat" (future) -> see `current` below
- NEW, to verify: "to run for the bus" (verb collocation, infinitive, = run to catch the bus)

Rules (owner decisions 375, 391, 392):
1. The native caption is a common, natural phrase a native speaker would say for that picture; no idiom, no calque.
2. It should contain the word the video teaches in your language = KEY (the database word, given below), in any
   inflected / infinitive form.
3. If the natural phrase does NOT contain KEY, the natural phrase wins: give it anyway and set `key_kept: false` and
   explain; do not force an unnatural phrase.
4. Infinitive form (the caption is an infinitive collocation, not a tense form), the same register and style as the
   other two captions; it must stay distinct from the two hat captions.

Write ONLY this JSON file (no other files): `out_<lang>.json`
{"lang": "<lang>", "caption": "to run for the bus", "native": "...", "key": "<KEY>", "key_kept": true|false,
 "natural": true|false, "alternatives": ["..."], "why": "one short sentence in English"}
