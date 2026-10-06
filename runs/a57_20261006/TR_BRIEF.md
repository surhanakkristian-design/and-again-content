# A57 help-translation brief (the A55 brief, per batch)

A language-learning app teaches German (`de`), Spanish from Spain (`es`) and French from France (`fr`) with short videos. A "translate"
button shows the learner the texts of the exercises in the learner's NATIVE language. You translate into ONE native language
(named to you). Work only inside `~/Projects/and-again-content/runs/a57_20261006/` (RUN). No external model or service, no network.

Native language codes: `sk` Slovak, `cz` Czech, `en` English, `de` German, `es` Spanish (Spain), `fr` French (France), `hu` Hungarian,
`tr` Turkish, `ua` Ukrainian. A learning language never gets a translation into itself (no `de` for German learners).

Source: `RUN/tr/<batch>/source_<lang>.json` (batch and learning language named to you): per video id: `about` (what the clip shows, context only),
`level`, `english` (the English version of the same exercise, context only - the meaning to translate is the LEARNING-language text),
`phrases` (3, each `text` + `target`), `nouns`, `question`, `answer`, `captions` (the carousel captions; A57: empty), `recall` (the
recall rows as whole texts).

Write `RUN/tr/<batch>/<lang>/<native>.json` (all ids of the source):
```json
{ "624": { "phrases": ["..", "..", ".."], "nouns": ["..", ..], "question": "..", "answer": "..",
           "captions": {}, "recall": ["..", ..] }, .. }
```
Same counts and order as the source. `captions`: `{}` (no captions in A57).

Rules
- Translate the MEANING of the learning-language text, naturally, grammatically perfect, as a native teacher writes it; nothing added
  or left out. Use `about`, `target` and `english` to pick the right sense.
- Phrases and infinitive captions: the infinitive form natural for a vocabulary entry (en "to catch a hat", sk "chytiť klobúk",
  cz "chytit klobouk", ua "зловити капелюх", tr "bir şapka yakalamak", hu "elkapni egy kalapot" / "elkap egy kalapot" - use the
  Hungarian infinitive -ni form, de "einen Hut fangen", es "atrapar un sombrero", fr "attraper un chapeau").
- Tense captions (no subject, e.g. de "rannte einem Hut hinterher"): the same tense without a subject where the language allows it
  (en "ran after a hat", "will run after a hat"; sk "bežal za klobúkom"...); noun captions as noun phrases.
- Nouns: the source has a definite article; translate as a dictionary-style noun: en with "the" (en "the hat", "the trees"),
  de der/die/das, es el/la/los/las, fr le/la/l'/les; languages without articles (sk, cz, ua, tr, hu): the bare noun (hu and tr
  without "a/az" / "bir"). Plurals stay plural. Lower case except German nouns.
- Question and answer: full sentences with the punctuation of the language (es "¿...?", fr a space before "?"), the tense as in the
  source (an ongoing action: the form the language uses for something happening now). Pronouns agree with the grammatical gender.
- Recall rows: the whole row text translated (a verb phrase without subject stays without subject).
- The same thing gets the same word everywhere inside one video.
Write the file with a script or in pieces, then check it with `python3 RUN/tr_check57.py <batch> <lang> <native>`. Reply with ONE line:
written, ids count.

## Helper files
Other agents work in parallel. Any helper file you create must carry your native code and the learning language in its name
and the batch (e.g. `tmp_tr_sk_de_b001.py`); never run or edit a file that does not.
