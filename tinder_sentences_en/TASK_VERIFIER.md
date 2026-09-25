# Task: verify the Tinder texts of one slice (independent VERIFIER)

Working directory: ~/Projects/and-again-content/tinder_sentences_en. The slice name and the file to verify are in
your prompt (slices/<slice>_out.jsonl, or slices/<slice>_retry.jsonl on the retry round). You did not write
these texts; judge them strictly against RULES.md and the media description in slices/<slice>_in.md.

For EVERY row check all four texts:
- target word present in the TRUE sentence and the TRUE phrase, in the sense of the definition;
- TRUE sentence true for the media; tense matches reality (now = present continuous, habit/fact = present simple,
  finished = past, about to happen = future); the "tense" label matches;
- grammar flawless in all four (articles, agreement, prepositions, tense, capitalisation);
- lengths: sentences <= 60, phrases <= 30 characters and 2-5 words, phrases are labels not sentences;
- FALSE sentence: same tone and structure, grammatically perfect, wrong on ONE fact a learner sees at a glance,
  not accidentally true, not a matter of opinion;
- FALSE phrase: similar at first glance (same key word in another sense/continuation, or same object/particle),
  clearly wrong after thought, not absurd, not wrong by grammar, not trivially unrelated;
- nothing invented beyond the description (guesses about thoughts/what happens next are fine if the scene invites them);
- translatable: no pun, rhyme, English-only wordplay;
- register: no banned words, nothing sexual, nothing about bodies/looks, no mocking of nationality/religion/race/
  disability, pop-culture names widely known in Europe, no living person mocked; tone gates from RULES.md.
Minor taste differences are NOT a reason to reject. Reject only for a real rule break a reviewer would object to.

Write slices/<slice>_verdict.jsonl (or _verdict2.jsonl on the retry round), one line per row, ONE Write call:
{"id": 123, "v": "A", "r": [], "note": "", "stretched": false}
v = "A" accept or "R" reject; r = reason codes from: word_missing, not_true, tense, grammar, length,
false_sentence_unclear, false_sentence_true, false_phrase_weak, false_phrase_bad, phrase_not_label, invented,
translatability, register, tone, other. note = a few words naming the field and the problem (only for R).
stretched = true when the TRUE sentence goes past 30 characters only to fit a joke.
Budget: minimal tool calls, no commentary. Final message: one line, accepted/rejected counts.
