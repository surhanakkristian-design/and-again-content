# A58 verifier brief - independent check of ONE video's new lab set (English)

You did NOT write this content. Check it hard against the clip and the rules, as a native English teacher and an exacting
reviewer. Work only inside `~/Projects/and-again-content/runs/a59_20261006/` (RUN); touch only files of your id.

Read first: `RUN/WRITER_BRIEF.md` (the rules the writer followed - they are your rules too), `RUN/content/<id>.json`
(the content), `RUN/data/<id>.json` (source: level, key word, definition, description, carousel captions).
Then run `python3 validate59.py <id>` and `python3 draw59.py <id>` and LOOK at EVERY `RUN/verify/<id>/box_NN.jpg` (each phrase
with its tap region drawn on every frame: red = phrase 1, green = 2, blue = 3) and `RUN/verify/<id>/slots.jpg` (the noun pills
at their slots on the still). Also `RUN/cuts/sheet_<id>.jpg` and `RUN/data/scenes.json` (automatic scene-cut detection: the 3
most likely cut moments with frames just before / at / after), and the carousel pictures
`~/Projects/and-again-content/runs/a55_20261005/src/pics/<id>_<n>.jpg`.

## Check
1. Cut: is there a real scene cut (a jump to another shot / a sudden change of framing or content between two frames), or
   only camera movement / animation? Confirm or correct `cutVerdict`. Exercise 1 is shown only with >= 2 different targets AND
   no cut.
2. Each phrase: grammar 100 %, natural collocation, level (A: A1-A2 words; B: B1-B2, idioms only at B), true in the clip and
   visible muted, ONLY its target does it, tied to the key word's situation, exactly one placeable noun visible in the still.
   Region: on its target in every frame where the target is visible (generous), `off` only when it is not in the picture;
   regions of different targets never overlap.
3. Nouns: exactly the phrases' nouns; each pill ON its thing in slots.jpg; natural display form.
4. Fill gaps + mind-map partners: sensible pieces (a learner can recall them), all six different.
5. Story: three short sentences, grammar 100 %, natural, funny, one clear order, consistent tense, uses the phrases /
   collocations, nothing that contradicts the clip (story time like "all day" is fine; a thing that is visibly NOT there is not).
   "laugh at" never "laugh about".

## Verdict
- Everything right: `PASS`.
- Something wrong that you can fix within the rules: fix it IN `RUN/content/<id>.json` yourself (keep the schema; rerun
  validate59.py and draw59.py and look again), verdict `FIXED` with a list of each change and why.
- Wrong and not fixable by you: `FAIL` with the reason.
Write `RUN/verify/<id>/VERDICT.md`: first line `PASS`, `FIXED` or `FAIL`; then the findings (short). Reply with the same.

## A59 addition (owner rule 1) - check this too
Read `A59_WRITER.md`. Phrase 1 must hold the key word as its placeable noun, with a clear doer visible in the clip (or two doers
together: `alsoKeys`, either tap right); noun 1 = the key word; the key-word phrase (inflected) is in the story. Compare with the
A58 version (`~/Projects/and-again-content/runs/a58_20261006/content/<id>.json`): every change must keep the chain phrases ->
nouns -> rows/gaps -> story intact and stay true to the clip. A phrase whose doer appears only part of the clip is fine when
its region is right in every frame and `off` elsewhere. Validate with `validate59.py`, draw with `draw59.py`.
