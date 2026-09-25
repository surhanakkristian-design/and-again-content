# Task: verify the translated Tinder texts of one slice (independent VERIFIER)

Working directory: ~/Projects/and-again-content/tinder_sentences_tx. Your prompt names the language and the
file to verify. You did not write these translations. Judge them as a strict native-speaking editor of that
language against RULES_TX.md.

1. Read RULES_TX.md and the file named in your prompt (slices/<lang>/<slice>_v_in.txt, or r1_v_in.txt on the
   retry round) in ONE turn. Each media: id | English word | loc (the app's translation) | checker flags,
   then the English and the translated TS, FS, TP, FP.
2. For EVERY media check:
   - meaning: the translation claims the same about the media as the English (who, what, where, colour,
     number, object); nothing added or lost that a learner would notice;
   - FALSE texts: wrong on exactly the same fact as the English FS/FP, not accidentally true, FP still a
     plausible similar-looking label;
   - native and alive: a 20-year-old native speaker would say/write it; a joke still works as a joke; a
     stiff literal rendering of a joke or idiom is a reject (joke_lost / unnatural);
   - grammar and spelling flawless (agreement, case, gender, aspect, diacritics, capitalisation, the
     language's punctuation);
   - the loc word (any inflected form, or a justified better equivalent) is in the TRUE sentence
     ("word_missing?" from the checker is only a hint: decide yourself);
   - phrases are 2-5 word labels, lower-case start (German nouns capitalised), no full stop;
   - register: no slurs, nothing sexual, nothing about looks, no mocking of nationality/religion/race/
     disability; swearing not stronger than the English.
   Minor taste differences are NOT a reason to reject. Reject only what a native editor would really object to.
3. Write slices/<lang>/<slice>_verdict.jsonl (or r1_verdict.jsonl) with ONE Write call, containing ONLY the
   REJECTED media, one JSON object per line:
   {"id": 123, "r": ["grammar"], "note": "FS: wrong case 'na stole' -> 'na stôl'"}
   and as the LAST line always: {"checked": <number of media you judged>, "last_id": <id of the last media>}.
   The file is long: read it in parts (offset/limit of about 600 lines) until its END, every media must be judged.
   Reason codes: meaning_changed, false_fact_changed, false_accidentally_true, joke_lost, unnatural, grammar,
   word_missing, phrase_shape, register, typography, other. Every media NOT listed counts as accepted, so
   write the file even when nothing is rejected (then it contains the single line {"none": true}).
   Budget: the reads needed to cover the whole file, then one write. Final message: one line: checked / rejected counts.
