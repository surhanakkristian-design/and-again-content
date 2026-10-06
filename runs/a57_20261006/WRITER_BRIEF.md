# A57 writer brief (the A55 brief; A57 changes marked A57) - the lab exercises for learners of German, Spanish (Spain) or French (France)

A language-learning app teaches with short videos. Each video has five exercises, today written for learners of ENGLISH. You write
the same exercises for learners of ONE other language (named to you: `de` German, `es` Spanish from Spain, `fr` French from France),
as a native-speaker teacher of that language writes them: NATIVELY, not word for word from the English. Work only inside
`~/Projects/and-again-content/runs/a57_20261006/` (called RUN). Touch no other file. No external model or service, no network.

## Look (for each of your videos)
- `RUN/src/<id>.json`: the English source: `level` (A or B), the key word per language (`keyWord.de/es/fr` = the database word the
  app teaches in that language), `definition`, `description`, `transcript` (context only; the learner may have the sound off),
  `defaultVoice`, `en` = the English exercises (`taps`, `nouns`, `question`, `answer`, `answerVoice`), and
  `oldHelpTranslations` (earlier word-for-word helper translations of the English texts: a reference, never copy them blindly).
- `RUN/verify/en/<id>/box_NN.jpg`: every frame (one per 0.5 s) with the three English tap regions drawn (red = phrase 1, green = 2,
  blue = 3; phrase and target printed at the top). Read EVERY one. `RUN/verify/en/<id>/slots.jpg`: the still picture with the
  English noun pills at their slots. Clean frames with a grid: `RUN/frames/<id>/sheet_NN.jpg`, `RUN/frames/<id>/f_<tt.tt>.jpg`.
  First run `cd RUN && python3 draw57.py en <id>` (it makes these English pictures).
- A57: these videos have NO carousel (`en.carousel` is empty) and NO English recall rows (`en.recall` is empty): write
  `"carousel": []` and build the recall rows by the A57 rule below.

## The fixed frame (do not change it)
The tap regions, the noun slots, the still moment and the voices' genders stay exactly as in English. So:
phrase n is about the SAME target as English phrase n; noun n names the SAME thing at the SAME slot as English noun n; caption n
describes carousel picture n. Same counts and order as the English.
A57: the video was made for its word and is never rejected: if something does not fit, write the best content the clip allows and
say it in `notes`. When the clip only allows a word above the video's level (e.g. "der Thron" on a level A video), use the
plain right word and note it. When an English tap box also covers moments where the phrase is not happening, write the phrase
for what the target does in most boxed frames and note it.

## Language and level (all texts)
- Model grammar 100 %, natural for a native speaker of that country (es = Spain, fr = France), standard spelling with every accent.
- Level A video: only A1-A2 words of that language. Level B video: B1-B2 vocabulary - each phrase and the model answer contain at
  least one B1/B2 word or collocation of that language (never an artificial one).
- Everything answerable from the clip; tense matching the clip; nothing invented (no names, reasons, places that are not shown).
- The same thing gets the same word in all exercises of one video.

## Write `RUN/content/<lang>/<id>.json`
```json
{
  "mediaId": 624, "lang": "de", "level": "A",
  "keyWord": "rennen",
  "taps": [ { "phrase": "einem Hut hinterherrennen", "target": "das Mädchen", "voice": "female" }, {..}, {..} ],
  "nouns": [ { "word": "die Bäume", "voice": "female" }, { "word": "der Hut", "voice": "female" }, .. ],
  "question": "Was macht das Mädchen?",
  "answer": ["Sie", "rennt", "einem", "Hut", "hinterher."],
  "answerVoice": "female",
  "carousel": [],
  "recall": [ { "from": "taps", "parts": [ { "text": "einem Hut" }, { "text": "hinterherrennen", "gap": true, "accept": ["hinterherrennen"] } ] }, ..,
              { "from": "answer", "parts": [ { "text": "rennt", "gap": true, "accept": ["rennt", "läuft"] }, { "text": "einem Hut hinterher" } ] } ],
  "notes": "doubts, anything the verifier should look at"
}
```

### keyWord
Copy `keyWord.<lang>` of the source unchanged (nouns with their article). If it does not fit what the video shows, or two English
words would map to one word of your language (or one to two), keep it and explain in `notes` with a proposal (the owner decides;
never restructure).

### 1. "Tap who does it." - the 3 phrases
- The natural infinitive phrase of a vocabulary entry in your language: de "einen Hut fangen", "durch den Schlamm fahren"
  (verb last); es "atrapar un sombrero"; fr "attraper un chapeau". Correct collocation, 2-6 words, no subject.
- True of its target in the clip, visible without sound, and fits ONLY that target (another visible person / animal / thing must
  not do it too). It need not be a literal translation of the English phrase: say what the target does, the way a native says it.
  The three phrases must not mean the same.
- `target`: the target's name in your language with the definite article ("das Mädchen", "la chica", "la fille") - for the
  verifier only. `voice`: copy the English phrase's voice.

### 2. "Place the nouns." - the nouns
- Noun n = English noun n's thing, with its DEFINITE article: de der/die/das (plural die), es el/la/los/las, fr le/la/l'/les.
  Plural where the clip shows several (English "trees" -> "die Bäume", "los árboles", "les arbres"; "wings" -> "die Flügel").
  Mass nouns with the definite article too ("das Gras", "la hierba", "l'herbe"). German nouns capitalised, everything else lower case.
- A noun stays a noun in your language (never a verb or an adjective). The usual everyday word for that thing in your country and
  of the video's level. If the English noun is the key word, use the database word (`keyWord`) when it names the thing naturally;
  else the natural word and a note.
- `voice`: copy the English noun's voice.

### 3. Question + model answer
- ONE question about what the clip SHOWS, at most 8 words, with the punctuation of the language (es "¿...?", fr a space before
  "?"). Present tense for something going on (de "Was macht das Mädchen?", es "¿Qué hace la chica?" or "¿Qué está haciendo
  la chica?", fr "Que fait la fille ?"): the natural form of your language, matching the English tense type.
- The model answer: ONE full sentence, 3-10 words, natural, grammatically perfect (es may drop the subject pronoun, as natives do).
  Pronouns agree with the grammatical gender in your language (das Mädchen -> "es" in careful German, but "sie" is what natives say:
  choose the form a native teacher writes and stay consistent; le dauphin -> il, la mouette -> elle).
- `answer` = the sentence as word chips in order: first chip capitalised, the full stop attached to the last chip, one word per chip
  (French elisions stay in one chip: "l'eau", "s'envole"). Exactly one natural word order with these chips if you can (avoid
  adverbials that could stand in two places; if German allows two orders, say so in `notes`).
- `answerVoice`: copy the English one, unless your sentence's subject has the other natural gender (then say so in notes).

### 4. Carousel captions
A57: none (`"carousel": []`). (The rules for captions are only in the lab's 10 videos.)

### 5. "Fill in what you remember." - the recall rows (A57 rule: these videos have no English rows)
- In this order: one row per tap phrase (`"from": "taps"`, the row text = your phrase exactly); then, ONLY when the key word is a
  noun of the set and none of the other rows contains it, one row of that noun (`"from": "nouns"`, the row text = your noun with
  its article, e.g. "der Hut"; the gap = the noun, never the article); then one row of the model answer (`"from": "answer"`) = your
  model answer without its subject (pronoun or noun phrase) and without the full stop, i.e. a tail of the answer
  ("Sie rennt einem Hut hinterher." -> "rennt einem Hut hinterher"; es without a subject already: the whole sentence without
  the full stop). So write the model answer subject first.
- `parts`: the row's text cut into 2-5 parts that, joined with single spaces, give the row text exactly. Exactly ONE part is the
  gap (`"gap": true`): a content word the learner can remember from the exercises (the verb or the noun, not an article, not a
  pronoun). `accept` = the gap's own text first, then other answers that are equally right in that row (a synonym the picture
  shows; keep it short). Never cut inside an elided French word ("l'herbe" stays one part; choose a gap that is not elided).
  No "to" or plain parts (those are English only). The same row text must not appear twice.
- Vary the gaps: across the rows of a video gap different words (not always the verb), and prefer the key word in at least one row.
- If two rows look the same once the gap is blanked, move a gap (or make both rows accept each other's word).

### Voices
All voices are copied from English (target / subject gender, else `defaultVoice`).

## Check your file (required)
`cd RUN && python3 validate57.py <lang> <id>` (rule errors; fix and run again), then `python3 draw57.py <lang> <id>` and LOOK at
`RUN/verify/<lang>/<id>/box_NN.jpg` (at least first, middle, last) and `slots.jpg` (your pills at the English slots: each pill on
its thing).

Reply with ONE short line per video: id, "written", and a key-word note only if there is one. Nothing else.

## Helper files
Other agents work in parallel. Any helper script or temporary file you create must carry your language and one of YOUR media ids
in its name (e.g. `tmp_de_624.py`); never run or edit a file that does not.

## A57 owner decisions
- 404: a German compound counts as containing the key word (die Sporttasche, die Hantelbank, die Strandtasche).
- The same key word may be used inside the phrases, nouns and answer where natural (it helps the learner); never force it.
