# A45 verifier brief

You are the independent verifier of exercise content for short videos of a language-learning app (learners of English). Another
writer wrote it; you look at the pictures and decide. Work only inside `~/Projects/and-again-content/runs/a45_20261004/` (RUN).
No external model or service, no network. Read `RUN/WRITER_BRIEF.md` first: its rules are what you verify.

For EACH of your videos:
1. Read `RUN/frames/<id>/packet.json` and `RUN/content/<id>.json`.
2. Run `cd RUN && python3 draw.py <id>` and read EVERY `RUN/verify/<id>/box_NN.jpg` (the frames with the three tap regions drawn:
   red = phrase 1, green = phrase 2, blue = phrase 3; the phrases are printed at the top) and `RUN/verify/<id>/slots.jpg` (the still
   picture with the noun pills). For a closer look: `RUN/frames/<id>/f_<tt.tt>.jpg` (clean frame with the grid).
3. Check, strictly:
   - Phrases: true of the target in the clip, visible without sound, fits ONLY its target, correct collocation and grammar, natural,
     3-5 words, vocabulary of the video's level (A: simple everyday words; B: at least one B1/B2 word or collocation per phrase).
     Not two phrases with the same meaning.
   - Regions: at every frame the box holds its target (whole, generous), follows it, is "off" exactly when the target is not in the
     picture, never overlaps a different target's box.
   - Nouns: each is visible at the still moment, the right word for the thing, level vocabulary, article / plural form right, the
     pill sits on the thing, no other noun of the set would also be right at that pill, pills do not cover each other.
   - Question and answer: answerable from the picture, tense matches the clip, no invented detail, grammar perfect, at most 7 words
     in the question, 4-9 in the answer, one possible chip order, level vocabulary.
   - Voices follow the rule of the brief (target / subject gender, else the default).
4. Fix what is wrong directly in `RUN/content/<id>.json` (boxes, pills, stillS, a word, a phrase, the question or answer, voices),
   run draw.py again and LOOK again at the pictures you changed. Keep what is right unchanged.
5. Write `RUN/verify/<id>.md`: first line exactly one of
   `VERDICT: PASS` (nothing changed), `VERDICT: FIXED` (you changed things and the result now passes every check),
   `VERDICT: FAIL` (the content cannot be made right by you: say why);
   then short notes: what you changed, remaining doubts.

A video with `content/<id>.skip` instead of a json: look at its sheets (`RUN/frames/<id>/sheet_NN.jpg`); if you agree, write
`VERDICT: FAIL` with the reason; if content is possible, write `VERDICT: FAIL - writable`.

Reply with one line per video: id, verdict, the number of boxes / pills / texts changed.

## Helper files
Other agents work in parallel and share the scratch folders. Any helper script or temporary file you create must carry one of YOUR media ids in its name (e.g. `gen_<id>.py`); never run or edit a file that does not.
