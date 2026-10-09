# A71 translations: the changed lab texts (8 lab items, 8 app languages)

RUN = ~/Projects/and-again-content/runs/a71_20261009/. Input `tr/tr71_source.json`: per item and field the English texts
(`en`), the current translations (`old`, per language) and which entries CHANGED in English (`changed`: indexes / caption
texts). Fields: `phrases` (exercise 1, "to ..." infinitive phrases), `nouns` (exercise 2, with the article the language
uses), `story` (exercise 5, three parts of one story: a part may end mid-sentence - keep the split, a comma at the end of a
part where the language needs one), `rows` (exercise 4 rows, the whole phrase with the box filled), `ownRow` (exercise 4's
own row = the caption of one carousel picture), `captions` (exercise 3 captions; English text -> translation). `scene`
texts tell you what each picture shows; `level` is the item's level (A: simple everyday words; B: the precise word).

Translate ONLY the changed entries into de, fr, es, sk, cz (Czech), ua (Ukrainian), tr, hu; keep every unchanged entry
exactly as in `old`. The translation is shown in small grey type under the English so the learner understands it:
natural, short, the same meaning, no explanations, no brackets; an infinitive phrase stays an infinitive phrase; a
caption keeps the caption style (a noun phrase / a full sentence in the same tense as the English).
Write `tr/tr71_writer.json`: `{"<id>": {"<lang>": {"phrases": [3], "nouns": [3], "story": [3], "rows": [n], "ownRow": "..."
(only when the item has one), "captions": {"<English caption>": "..."}}}}` - full arrays (unchanged entries copied).
Reply with one line.
