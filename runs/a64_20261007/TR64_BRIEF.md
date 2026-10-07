# A64 help translations (writer, one or more native languages)

RUN = ~/Projects/and-again-content/runs/a64_20261007/. You are a native speaker and careful translator of each language
named to you (de, fr = France, es = Spain, sk, cz = Czech, ua = Ukrainian, tr, hu). These are HELP texts of an
English-learning lab (shown under the English chips when the learner taps ⇄). Source: RUN/tr64_source.json.

1. `stories.<id>`: each story is ONE story split into exactly 3 PARTS (chips). A part may be a whole sentence, several
   sentences or part of a sentence. Translate the whole story naturally, then split it into the SAME 3 parts at the
   matching places; each part keeps the capitals and punctuation it has at its place in your translation (a part that
   continues a sentence starts lowercase unless the word is a name; a comma at the end of a part only where your
   language puts it there). Do not add connectors the English does not have. Names stay.
2. `phrases.<id>` / `nouns.<id>`: a replaced phrase of exercise 1 (infinitive form as the earlier phrases) and its noun
   (with the article / form your language's earlier nouns use).
3. `rows.<id>`: new exercise-4 phrases ("to ..." + the rest), as infinitive phrases like the earlier ones.
Use the words of your language's earlier verified texts (`earlier.<lang>.<id>`: phrases, nouns, old story) for the same
things - the key word especially. Rules: grammar and spelling 100 %; natural for a native; same meaning; no added content.
Write RUN/tr/<lang>.json exactly:
{"lang": "<lang>", "stories": {"<id>": ["part 1", "part 2", "part 3"]}, "phrases": {"<id>": {"<English phrase>": "..."}},
 "nouns": {"<id>": {"<English noun>": "..."}}, "rows": {"<id>": {"<English row>": "..."}}, "notes": {"<where>": "<note>"}}
Reply with one line per language.
