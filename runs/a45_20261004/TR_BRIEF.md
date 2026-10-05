# A45 translations brief

A language-learning app teaches English with short videos. A "translate" button shows the learner the NATIVE-language version of the
English exercise texts. Work only inside `~/Projects/and-again-content/runs/a45_20261004/` (RUN). No external model or service.

Source: `RUN/tr/<batch>/source.json`: per video id: `about` (what the clip shows, context only), `level`, `phrases` (3, each with
`en` and `target` = who or what the phrase is about, context only), `nouns` (3-4 labels of things in the picture), `question`, `answer`.

Write, for each language asked of you, `RUN/tr/<batch>/<code>.json`:
```json
{ "123": { "phrases": ["...", "...", "..."], "nouns": ["...", ...], "question": "...", "answer": "..." }, "124": { ... } }
```
Every video of the source, same order and count of phrases and nouns. Codes: de German, fr French, es Spanish, sk Slovak, cz Czech,
ua Ukrainian, tr Turkish, hu Hungarian.

Rules
- Natural, grammatically perfect, as a native teacher would write it; meaning identical to the English; nothing added or left out.
- Phrases: the infinitive form natural for a vocabulary entry (de "ein Getränk halten", fr "tenir un verre", es "sostener una bebida",
  sk "držať nápoj", cz "držet nápoj", ua "тримати напій", tr "bir içecek tutmak", hu "egy italt tartani"). No English "to".
- Nouns: the dictionary-style equivalent of the English form: where English has "a/an" use the indefinite article in languages that
  have one (de ein/eine, fr un/une, es un/una); languages without articles: the bare noun; Hungarian and Turkish: bare noun (no
  "egy" / "bir"). "the sky" -> definite form where natural (de "der Himmel", fr "le ciel", es "el cielo"). English bare plurals and
  mass nouns: de bare ("Bäume", "Schnee"), fr "des arbres" / "de la neige", es bare ("árboles", "nieve"). Plurals stay plural.
  Lower case except German nouns.
- Question and answer: full sentences with the punctuation of the language (es "¿...?", fr space before "?"), tense as in English
  (ongoing action: the form that language uses for something happening now). Pronouns agree with the noun's grammatical gender in
  that language (the dolphin, the girl / das Mädchen ...). The same thing gets the same word in phrases, nouns, question and answer
  of one video.
- Use `about` and `target` to pick the right sense (a bat, a glass, a pitcher ...).
Write the file with a script or in pieces if it is long, then check that it is valid JSON with every id
(`python3 RUN/tr_check.py <batch> <code>`). Reply with one line per language: file written, ids count.
