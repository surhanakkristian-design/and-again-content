# A57 verifier brief (the A55 brief; A57 changes marked A57)

You are the independent verifier, as a strict native-speaker teacher of ONE language (`de` German from Germany, `es` Spanish from
Spain, `fr` French from France), of exercise content that another writer wrote for learners of that language. You look at the
pictures and decide. Work only inside `~/Projects/and-again-content/runs/a57_20261006/` (RUN). No external model or service, no
network. Read `RUN/WRITER_BRIEF.md` first: its rules are what you verify.

For EACH of your videos:
1. Read `RUN/src/<id>.json` (English source, key word, description) and `RUN/content/<lang>/<id>.json`.
2. Run `cd RUN && python3 draw57.py <lang> <id>` and read EVERY `RUN/verify/<lang>/<id>/box_NN.jpg` (every frame with the three tap
   regions; the native phrases and targets printed at the top: red = phrase 1, green = 2, blue = 3) and
   `RUN/verify/<lang>/<id>/slots.jpg` (the still picture with the native noun pills at their slots). Clean frames:
   `RUN/frames/<id>/f_<tt.tt>.jpg`. (A57: these videos have no carousel.)
3. Check, strictly, every text:
   - Grammar 100 % (case, gender, agreement, articles, aspect / tense, word order, reflexives, prepositions), spelling, accents,
     punctuation; natural for a native speaker of that country; vocabulary of the video's level (A: A1-A2 words; B: at least one
     B1-B2 word or collocation per phrase and in the answer, never artificial).
   - Phrases: the natural infinitive entry form; true of the boxed target in the clip, visible without sound, fits ONLY that target
     (no other visible person / animal / thing does it too), the three do not mean the same.
   - Nouns: definite article right (gender!), plural where the picture shows several, the usual word for that thing, still a noun,
     each pill on its thing, no other noun of the set would also fit that pill.
   - Question + answer: answerable from the picture, tense matching the clip, nothing invented, at most 8 words in the question, one
     natural chip order (say if a second order is equally natural), chips one word each, full stop on the last chip.
   - Recall rows (A57 rule in the writer brief section 5): the tap phrases, at most one key-word noun row, the answer's tail; one
     sensible gap each (a content word, varied across the rows), `accept` lists only answers that are really right there (and
     every answer that is equally right there: a learner typing a correct synonym should not be marked wrong).
   - The key word: does `keyWord` name what the video shows? Does it collide (two English words -> one word, or one -> two)? Note it
     in one line starting `KEYWORD:` (the owner decides; never change it). A57: the video is never rejected for it; you only flag.
4. Fix what is wrong directly in `RUN/content/<lang>/<id>.json`, run `python3 validate57.py <lang> <id>` and draw57.py again and LOOK
   again at what you changed. Keep what is right unchanged. Never change the key word (note instead).
5. Write `RUN/verify/<lang>/<id>.md`: first line exactly one of `VERDICT: PASS` (nothing changed), `VERDICT: FIXED` (you changed things
   and the result now passes every check), `VERDICT: FAIL` (cannot be made right: say why); then short notes: every change
   (field, before -> after, why), remaining doubts, key-word notes.

Reply with ONE short line per video: id, verdict, number of texts changed, and the KEYWORD note if any. Nothing else.

## Helper files
Other agents work in parallel. Any helper script or temporary file you create must carry your language and one of YOUR media ids
in its name; never run or edit a file that does not.
