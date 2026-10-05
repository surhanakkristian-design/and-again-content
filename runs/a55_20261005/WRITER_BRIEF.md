# A55 writer brief - the lab exercises for learners of German, Spanish (Spain) or French (France)

A language-learning app teaches with short videos. Each video has five exercises, today written for learners of ENGLISH. You write
the same exercises for learners of ONE other language (named to you: `de` German, `es` Spanish from Spain, `fr` French from France),
as a native-speaker teacher of that language writes them: NATIVELY, not word for word from the English. Work only inside
`~/Projects/and-again-content/runs/a55_20261005/` (called RUN). Touch no other file. No external model or service, no network.

## Look (for each of your videos)
- `RUN/src/<id>.json`: the English source: `level` (A or B), the key word per language (`keyWord.de/es/fr` = the database word the
  app teaches in that language), `definition`, `description`, `transcript` (context only; the learner may have the sound off),
  `defaultVoice`, `en` = the English exercises (`taps`, `nouns`, `question`, `answer`, `answerVoice`, `carousel`, `recall`), and
  `oldHelpTranslations` (earlier word-for-word helper translations of the English texts: a reference, never copy them blindly).
- `RUN/verify/en/<id>/box_NN.jpg`: every frame (one per 0.5 s) with the three English tap regions drawn (red = phrase 1, green = 2,
  blue = 3; phrase and target printed at the top). Read EVERY one. `RUN/verify/en/<id>/slots.jpg`: the still picture with the
  English noun pills at their slots. Clean frames with a grid: `RUN/frames/<id>/sheet_NN.jpg`, `RUN/frames/<id>/f_<tt.tt>.jpg`.
- `RUN/src/pics/<id>_<n>.jpg`: the carousel picture n (1-3) of the English caption n.

## The fixed frame (do not change it)
The tap regions, the noun slots, the still moment, the carousel pictures and the voices' genders stay exactly as in English. So:
phrase n is about the SAME target as English phrase n; noun n names the SAME thing at the SAME slot as English noun n; caption n
describes carousel picture n. Same counts and order as the English.

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
  "carousel": [ { "en": "ran after a hat", "caption": "rannte einem Hut hinterher", "type": "past", "hasKeyWord": true, "note": "" }, .. ],
  "recall": [ { "from": "taps", "parts": [ { "text": "einem Hut" }, { "text": "hinterherrennen", "gap": true, "accept": ["hinterherrennen"] } ] }, .. ],
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

### 4. Carousel captions (every video here has 3 pictures)
- Caption n describes picture n (`RUN/src/pics/<id>_<n>.jpg`) like English caption n: translated NATURALLY, as short as the
  English: collocations as infinitive phrases (de "einen Heißluftballon landen") or noun phrases (es "la cesta del globo"); tense captions as the same tense type without a subject
  (past "rannte einem Hut hinterher", future "wird einem Hut hinterherrennen"). At most ONE future, ONE present and ONE past per
  video, distinct in your language. Common phrases only, no idioms.
- `type`: copy the English type ("past", "present", "future", "verb coll.", "noun coll.").
- The caption's key word is the database word (`keyWord`, any inflected form). When the natural caption does not contain it, the
  natural caption wins: keep it, `hasKeyWord: false`, and say in `note` what the key word would have been and why it is unnatural.
- Look at the A56 captions in `oldHelpTranslations.<lang>.captions` (verified for the key-word rule): keep them when they are
  natural and right for the picture; improve them otherwise and say why in `note`.

### 5. "Fill in what you remember." - the recall rows
- Exactly the English rows, in the same order and from the same sources (`from`): one row per English row; a `taps` row = your
  phrase of that tap, a `nouns` row = your noun, an `answer` row = your model answer without a leading subject pronoun and without
  the full stop (es already without), a `carousel` row = your caption.
- `parts`: the row's text cut into 2-5 parts that, joined with single spaces, give the row text exactly. Exactly ONE part is the
  gap (`"gap": true`): a content word the learner can remember from the exercises (the verb or the noun, not an article, not a
  pronoun). `accept` = the gap's own text first, then other answers that are equally right in that row (a synonym the picture
  shows; keep it short). Never cut inside an elided French word ("l'herbe" stays one part; choose a gap that is not elided).
  No "to" or plain parts (those are English only). The same row text must not appear twice.

### Voices
All voices are copied from English (target / subject gender, else `defaultVoice`). Carousel captions use `defaultVoice`.

## Check your file (required)
`cd RUN && python3 validate55.py <lang> <id>` (rule errors; fix and run again), then `python3 draw55.py <lang> <id>` and LOOK at
`RUN/verify/<lang>/<id>/box_NN.jpg` (at least first, middle, last) and `slots.jpg` (your pills at the English slots: each pill on
its thing).

Reply with one line per video: id, your 3 phrases, nouns, question, answer, captions, and any key-word note.

## Helper files
Other agents work in parallel. Any helper script or temporary file you create must carry your language and one of YOUR media ids
in its name (e.g. `tmp_de_624.py`); never run or edit a file that does not.
