# A58 writer brief (base rules; A59 changes in A59_WRITER.md come first) - the new five-exercise lab set of ONE noun video (English)

A language-learning app (learners aged 15-25 learn ENGLISH) teaches with short videos. For each video you write a new set of
five exercises. Work only inside `~/Projects/and-again-content/runs/a59_20261006/` (called RUN). Touch no other file. No
external model or service, no network. Helper scripts or temp files you create carry your media id in the name
(`tmp_<id>.py`); never run or edit a file of another id (other writers work in parallel).

## Look first (for your video `<id>`)
- `RUN/data/<id>.json`: the source: `level` (A or B), `keyWord.en` (the database word the app teaches), `definition` (the key
  word's database definition), `description` (what the clip shows), `transcript`, `defaultVoice`, `stillS` (the still moment
  of exercise 2), and `en` = the CURRENT exercises (`taps` phrases + targets, `nouns` with slots `x`/`y`, `carousel` captions).
- `RUN/data/live_rows.json`: the live row of your video: `taps[n].keys` = tap regions (boxes every 0.5 s, shares of the whole
  picture) of the CURRENT targets. You may reuse them (see below).
- Frames: `~/Projects/and-again-content/runs/a55_20261005/frames/<id>/f_<tt.tt>.jpg` (one per 0.5 s, 10 x 10 grid with
  .1-.9 labels = shares of width / height), `sheet_NN.jpg` (4 per sheet), `still.jpg` (the still of exercise 2), and
  `~/Projects/and-again-content/runs/a55_20261005/verify/en/<id>/box_NN.jpg` (the CURRENT regions drawn: red / green / blue).
  Read enough of them to know the whole clip (every sheet for clips under 10 s; for 30 s clips at least every second sheet).
- `RUN/cuts/sheet_<id>.jpg` + `RUN/data/scenes.json`: the moments the automatic scene-cut detection found most likely (3 frames
  around each). `~/Projects/and-again-content/runs/a55_20261005/src/pics/<id>_<n>.jpg`: carousel picture n (caption n).

## The five exercises (fixed order; the learner meets each phrase up to 4 times)
1. "Tap who does it." - one phrase at a time stands in a pill on the playing clip; the learner taps WHO or WHAT does it (a
   person, an animal, or a thing when it makes sense: "the balloon flies", "the puddle reflects the sky"). Shown only when the
   clip has at least 2 different actors (different targets among your 3 phrases) AND no scene cut.
2. "Place the nouns." - the 3 nouns = exactly the nouns of your 3 phrases; each has a slot ON that thing in the still picture.
3. "Choose the caption." - the existing carousel pictures + captions (unchanged; you do not write them).
4. "Fill the empty spaces." - a mind map: the key word in the centre, the three carousel captions around it with the key
   word's PARTNER as an empty space ("weight bench" -> partner "weight"; "to paint a bench" -> "paint"; "to fly in a balloon"
   -> "fly in"; "king and queen" -> "queen"); below, your 3 phrases with ONE empty space each (the verb part or the noun). The
   bank holds ONLY the 6 correct pieces (no distractors); the learner taps them into the spaces.
5. "Make a story." - your 3 short sentences that form a funny little story, shown shuffled; the learner taps them into the
   right order (or tells an own story).

## Rules for every text
- Grammar 100 %, natural English a native teacher writes. Level A video: A1-A2 words only. Level B: B1-B2 words; idioms ONLY at
  level B (a common one, never forced). Humour and puns are welcome (e.g. a "blind date" with a blind man), never mean.
- Everything is visible / answerable in the clip (muted): no names, no invented reasons or places.
- Collocations exactly as natives say them: "laugh at jokes" (never "laugh about"), "impress her with his self-confidence"
  (the verb's object where it needs one).

## Your content: write `RUN/content/<id>.json`
```json
{
  "mediaId": 8056, "level": "A", "keyWord": "a bench",
  "cutVerdict": "no cut",                      // your look at cuts/sheet_<id>.jpg: "no cut" or "cut at <t> s"
  "taps": [
    { "phrase": "to sit on a bench", "target": "the man", "verb": "sit on", "noun": "a bench", "keys": "live:3" },
    { "phrase": "to read a book",    "target": "the man", "verb": "read",   "noun": "a book",  "keys": "live:1" },
    { "phrase": "to look at the man", "target": "the dog", "verb": "look at", "noun": "the man", "keys": "live:2" }
  ],
  "nouns": [ { "word": "a bench", "x": 0.58, "y": 0.54 }, { "word": "a book", "x": 0.18, "y": 0.5 }, { "word": "a man", "x": 0.4, "y": 0.4 } ],
  "fill": [ { "gap": "verb" }, { "gap": "verb" }, { "gap": "noun" } ],
  "mindMap": [ { "caption": "weight bench", "partner": "weight" }, { "caption": "to paint a bench", "partner": "paint" }, { "caption": "to share a bench", "partner": "share" } ],
  "story": ["...", "...", "..."],
  "notes": "doubts for the verifier"
}
```

### taps (3 phrases)
- Infinitive phrase: `to` + verb (+ particle / preposition) + the placeable noun (+ at most a short detail), 3-7 words, lower
  case except proper words; level B may use the passive (`to be pulled by a dog`). Each phrase is TIED TO THE KEY WORD'S
  SITUATION (what the video is about) and contains exactly ONE placeable noun: a thing / person / animal clearly visible in the
  still picture (`still.jpg`). `verb` = the phrase's verb part exactly as written in the phrase (e.g. "look at", "hang from",
  "be pulled by"); `noun` = the placeable noun exactly as written in the phrase. Prefer the key word as one of the nouns.
- `target` = who / what does it, with "the" ("the man", "the balloon"). True in the clip, visible without sound, and ONLY that
  target does it (no other visible actor does the same). The three phrases mean different things.
- `keys`: reuse the live regions when your target is the SAME target as a current phrase: `"live:N"` (N = 1-3, the current
  phrase whose target it is; its region follows that target through the clip). Only when you need a target that has no live
  region, write the boxes yourself: a list `[{ "t": 0.0, "x": .., "y": .., "w": .., "h": .. }, ...]` at EVERY frame time
  (0.5 s apart, from the first frame to the last), shares of the whole picture (top-left corner + size, read off the grid),
  generous (a finger hits it; at least 0.04 wide and high), `{ "t": .., "off": true }` when the target is not in the picture.
  Regions of different targets must never overlap at the same moment.
- Exercise 1 is shown only with >= 2 different targets AND no cut. If the clip really has one actor (e.g. only a dolphin),
  keep one target - exercise 1 is then skipped automatically; say so in `notes`. Do not force a second actor that does not
  make sense.

### nouns (3)
- Exactly the 3 `noun`s of your phrases, in the phrase order, written the same way BUT as a display form with an indefinite
  article or none (`a man`, `clouds`, `water`) - if the phrase says "the man", the noun is "a man".
- `x`, `y` = the pill's centre on that thing in `still.jpg` (shares of the whole picture, read off the grid). Between 0.08 and
  0.92; keep pills apart (at least 0.12 vertically when they are less than 0.35 apart horizontally); avoid the right 15 % strip
  at heights 0.35-0.70 (the rail of icons stands there). Reuse the current slot when the noun is a current noun and its slot is
  on the thing.

### fill (one entry per phrase)
`"gap": "verb"` or `"noun"`: which part of that phrase is the empty space in exercise 4. At least one verb and one noun gap.
The 6 pieces of the bank (3 partners + 3 gaps) must all be different texts.

### mindMap
The three carousel captions of `en.carousel` in their order, each with its `partner` = the caption's words that go with the key
word, without the key word, without "to" and without the article (exact substring of the caption).

### story (3 sentences)
- A funny little story in THREE short sentences (level A: at most 12 words each; level B: at most 16), in the clip's situation,
  that uses as many of your 3 phrases and of the 3 carousel collocations as possible (inflected forms are fine; the key word is
  not required). Each sentence ends with . or !; only ONE order makes sense (sentence 1 sets the scene, 2 develops, 3 ends with
  the joke). Present or past tense, consistent. Grammar 100 %.

## Check your file (required)
`cd RUN && python3 validate59.py <id>` (fix every error, run again), then `python3 draw59.py <id>` and LOOK at
`RUN/verify/<id>/box_NN.jpg` (first, middle, last at least: your phrases and targets with their regions) and
`RUN/verify/<id>/slots.jpg` (each noun pill ON its thing).

Reply with ONE short paragraph: phrases (targets), nouns, gaps, partners, the story, exercise 1 shown or not (why), notes.
