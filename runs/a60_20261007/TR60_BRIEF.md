# A60 help translations - ONE native language (writer)

You are a native speaker and careful translator of the language named to you (de, fr = France, es = Spain, sk, cz = Czech,
ua = Ukrainian, tr, hu). RUN = ~/Projects/and-again-content/runs/a60_20261007/. These are HELP texts of an English-learning lab
(the learner taps ⇄ to see them in their native language). Source: RUN/tr60_source.json.

1. `nouns.<id>.new_story` (6 noun videos): their three story sentences were rewritten. Your language's earlier verified
   translation of the OLD story and of the set's phrases is in ~/Projects/and-again-content/runs/a59_20261006/tr/<lang>.json
   (`videos.<id>`) - keep its words for the same things (the key word especially: e.g. 8055 = hot-air balloon, 8039 per that
   file). Translate the 3 new sentences.
2. `pilots.select` (verb "to select", level B) and `pilots.classical` (adjective, level B): translate `phrases` (infinitive
   phrases, as a dictionary would: de "einen Donut auswählen"), `nouns` (labels with the article your language uses for a label,
   none where it has none), `story` (3 sentences) and `captions` (full sentences; keep each caption's tense / person: past,
   present continuous question, future). The key word: select = the everyday "choose carefully" verb (de auswählen, es
   seleccionar/elegir - pick the natural one and use it in every text that has "select"); classical = classical (music) adjective.
   Each native caption should contain the translated key word; when the natural sentence does not, keep the natural one and
   say so in `notes`.
Rules: grammar and spelling 100 %; natural for a native; same meaning; story sentence 2 keeps a linking word at its start and
sentence 3 keeps its ending word ("In the end"/"Finally" -> the natural equivalent) so the order stays clear; names stay (Tom,
Mia, Leo, Ben, Sam, Anna, Max, Bruno); no added content.
Write RUN/tr/<lang>.json exactly:
{"lang": "<lang>", "nouns": {"<id>": {"story": [3]}}, "pilots": {"select": {"phrases": [3], "nouns": [3], "story": [3],
 "captions": {"<English caption>": "<native>"}}, "classical": {...}}, "notes": {"<where>": "<note>"}}
Reply with one line: language, done, anything noteworthy.
