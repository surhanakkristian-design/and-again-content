# A45 writer brief

You write the exercise content for a few short videos of a language-learning app (learners of English). For EACH of your videos you
look at its frames and write ONE json file. Work only inside `~/Projects/and-again-content/runs/a45_20261004/` (called RUN below).
Touch no other file. Use no external model or service, no network. Do the videos one after another; finish each before the next.

## Look
- `RUN/frames/<id>/packet.json`: key word, its LEVEL (A or B), a description of the clip, the transcript (context only: the learner may
  have the sound off), `times` (the frame times), `sheets` (how many sheet pictures).
- `RUN/frames/<id>/sheet_NN.jpg`: 4 frames per sheet (left to right, top to bottom), one frame every 0.5 s, its time printed bottom
  left ("t = 2.5 s"). A yellow 10 x 10 grid lies on every frame: `.1` ... `.9` = share of the picture's width (x, from the left) and
  height (y, from the top). Read EVERY sheet with the Read tool. A single frame: `RUN/frames/<id>/f_<tt.tt>.jpg` (e.g. `f_02.50.jpg`).

## Level
- Level A video (A1-A2 learners): simple, frequent everyday words only in every text (phrases, nouns, question, answer).
- Level B video (B1-B2 learners): B-level vocabulary: each phrase and the model answer should contain at least one word or collocation
  that is B1/B2 rather than beginner ("to storm into the room", "to reflect the grey sky", "to adjust a strap"), nouns more specific
  ("a lantern", "a puddle", "a mannequin" rather than "a lamp", "water", "a doll") - but always true to the picture and natural.

## Write `RUN/content/<id>.json`
```json
{
  "mediaId": 123, "level": "B", "keyWord": "a lantern",
  "defaultVoice": "female",
  "taps": [
    { "phrase": "to hold a drink", "target": "the woman", "voice": "female",
      "keys": [ { "t": 0.0, "x": 0.52, "y": 0.30, "w": 0.40, "h": 0.55 }, { "t": 0.5, "off": true }, ... ] },
    { ... }, { ... }
  ],
  "stillS": 2.5,
  "nouns": [ { "word": "a lantern", "x": 0.80, "y": 0.35, "voice": "female" }, ... ],
  "question": "What is she doing?",
  "answer": ["She", "is", "laughing", "at", "his", "jokes."],
  "answerVoice": "female",
  "notes": "weak spots, doubts, anything the verifier should look at"
}
```

### 1. "Tap who does it." - exactly 3 phrases
- A phrase = "to" + verb + object or detail: "to hold a drink", "to laugh at his jokes", "to fly over the clouds". Correct
  collocations, natural model English, grammatically perfect, 3-5 words, vocabulary of the video's level.
- Each phrase is about ONE person, animal or thing (the target) that is clearly visible in the clip and really does / is that in the
  clip. Nothing invented, nothing that needs the sound. The learner sees the phrase and taps the target in the playing video.
  Prefer actions; a state ("to wear a red scarf") only when no action fits only that target.
- Prefer three different targets when the clip has several. Two phrases may share a target. A clip that shows only one possible
  target may use it for all three. A phrase must fit ONLY its target: if another visible person / animal / thing also does it, choose
  another phrase. Two phrases of one video must not mean the same.
- `target`: short name with "the" ("the man", "the dog", "the red car"). Two people of the same kind need different names
  ("the tall man", "the man in the hat").
- `keys`: the tap region of the target at EVERY frame time (one key per value in `times`, same `t`). `x`, `y` = top-left corner,
  `w`, `h` = size, shares of the whole picture (0..1, read from the grid, 2 decimals). The box holds the whole visible target and is
  generous (about 0.03-0.05 padding; a small target gets at least 0.18 x 0.14), stays inside 0..1, and NEVER overlaps the box of a
  DIFFERENT target at the same time (shrink the padding where two targets are close; if they overlap in the picture, split along the
  line between them). Phrases with the same target use exactly the same keys. If the target is not in the picture at a time (cut,
  out of frame, hidden): `{ "t": 2.5, "off": true }`. Follow the target: when it moves, the box moves. A clip with cuts: the target's
  box in every shot where it is visible.

### 2. "Place the nouns." - 3 or 4 nouns on one still picture
- `stillS`: one of the frame times, a calm moment where all your nouns are clearly visible and well apart.
- Each noun names ONE thing visible at that moment, at one clear place: with article for a singular countable noun ("a hat"),
  bare plural for a clear group standing together ("trees"), bare mass noun ("snow", "grass"), "the sky". Lower case. Vocabulary
  of the video's level. Include the key word when it is a visible noun. No two nouns that could label the same place (not "a man"
  and "a shirt" on the same small figure; not "a parrot" when there are two parrots apart, unless the slot is clearly on one and no
  other noun is the other bird). No abstract words, nothing that needs guessing.
- `x`, `y` = the centre of a small label pill ON the thing (shares of the picture, 0.10 <= x <= 0.90, 0.05 <= y <= 0.95). Pills are
  about 0.07 high and as wide as the word (about 0.25-0.40 of the width): two pills need at least 0.08 distance in y, or 0.40 in x.

### 3. Question + model answer
- ONE question about what the clip SHOWS, answerable from the picture alone, at most 7 words; the model answer uses words of your
  phrases and/or nouns (and the key word when natural).
- Tense matches the clip: something going on -> present continuous ("What is the girl doing?" -> "She is running after a hat.").
- No invented details (no names, reasons, durations, places that are not shown).
- Model answer: ONE full sentence, 4-9 words, grammatically perfect, natural, vocabulary of the level. `answer` = the sentence as
  word chips in order: first chip capitalised, the full stop attached to the last chip, one word per chip (a fixed phrase may stay
  one chip: "at night."). Exactly one natural word order with these chips (no adverb that could stand in several places).
- If two people of the same gender are shown, the question names its subject clearly ("What is the woman outside doing?").

### 4. Voices (the texts are recorded)
- `voice` of a phrase: "female" when its target is a woman or girl, "male" when a man or boy, else the video's `defaultVoice`.
- `voice` of a noun: "female" / "male" when the noun is a female / male person ("a woman", "a boy"), else `defaultVoice`.
- `answerVoice`: "female" when the answer's subject is a woman / girl / She, "male" for a man / boy / He, else `defaultVoice`.
- `defaultVoice`: the gender of the main person of the clip; if there is none (animals, things, a mixed group), "female" when
  `evenId` is true in the packet, else "male".

## Check your file (required)
Run `cd RUN && python3 draw.py <id>`. It prints rule errors (fix them and run again) or draws your boxes: then LOOK at
`RUN/verify/<id>/box_NN.jpg` (at least the first, a middle and the last picture) and `RUN/verify/<id>/slots.jpg` and fix boxes that
miss their target and pills that are not on their thing. Run draw.py again after every change.

A video you cannot write for (nothing identifiable, picture broken): write `RUN/content/<id>.skip` with one line saying why, no json.

Reply with one line per video: id, the 3 phrases, the nouns, the question and the answer (or "skip: reason").

## Helper files
Other agents work in parallel and share the scratch folders. Any helper script or temporary file you create must carry one of YOUR media ids in its name (e.g. `gen_<id>.py`); never run or edit a file that does not.
