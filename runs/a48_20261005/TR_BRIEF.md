# A48 translation brief

Translate, for each of the 10 lab videos (RUN/content/<id>.json; ids 8055 236 624 7071 8056 4265 461 62 8039 432),
into the app's native languages: de (German), fr (French), es (Spanish), sk (Slovak), cz (Czech), ua (Ukrainian),
tr (Turkish), hu (Hungarian):
1. every carousel caption (vertical and horizontal sets, the original included);
2. every recall row as ONE full native text (the row's parts joined, the gap filled with its own text).
These texts are shown to the learner as the meaning of the English (the rail's translate button). Natural, correct
native language at the video's level; a collocation is translated as the natural native collocation, not word by word
("to pop a balloon" -> "einen Ballon platzen lassen"). Infinitive phrases as the native dictionary form of the phrase.
Tense captions ("was calmed by a knight", "is running after a hat") as finite native phrases in the same tense
meaning, without a subject where the language allows (else with the 3rd person pronoun the picture shows). Keep
consistent with the existing lab texts of the same video (lib/labExercises.json in ~/Projects/and-again-a48, field
tr.<lang>: phrases, nouns, answer): the same native word for the same English word.
Output one file per language: RUN/tr/<lang>.json =
{ "<mediaId>": { "captions": { "<English caption>": "<native>" , ...}, "recall": ["<native row 1>", ...] }, ... }
recall in the rows' order of the content file, as many as the file has. Write nothing else.
