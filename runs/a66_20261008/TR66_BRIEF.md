# A66 help translations for 7071 "quad bike" (writer)

RUN = ~/Projects/and-again-content/runs/a66_20261008/. You are a native speaker and careful translator of each of the 8
help languages: de, fr (France), es (Spain), sk, cz (Czech), ua (Ukrainian), tr, hu. These are HELP texts of an
English-learning lab (shown under the English chips when the learner taps ⇄). Source: RUN/tr66_source.json.

The English of item 7071 changed "ATV" -> "quad bike" everywhere ("to ride a quad bike", "a quad bike", the story part
"the old king borrowed the gardener's quad bike."). For each language translate every English string in `english`
(phrases, nouns, rows, the 3-part story, the two recall texts) with the NATURAL everyday local word for a quad bike
(e.g. de "Quad", sk "štvorkolka", cz "čtyřkolka") and the matching article / case. `current.<lang>` holds the
verified translations as they are now: keep them word for word where they are already correct and natural, change only
what the new English needs (e.g. a language that still says "ATV" where natives say something else). Story: translate
the whole story and split it into the SAME 3 parts at the same places; each part keeps its capitals / punctuation as
at its place in your translation; names stay; no added connectors. Grammar and spelling 100 %.

Write RUN/tr/<lang>.json for each language exactly:
{"lang": "<lang>", "phrases": {"to ride a quad bike": "..."}, "nouns": {"a quad bike": "..."},
 "rows": {"to ride a quad bike": "..."}, "story": ["part 1", "part 2", "part 3"],
 "recall": {"a quad bike": "...", "is riding a quad bike through a puddle": "..."},
 "changed": ["which of the current texts you changed and why"]}
Reply with one line per language.
