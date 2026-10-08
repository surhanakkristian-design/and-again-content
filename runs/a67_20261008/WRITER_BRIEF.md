# A67 lab content - writer brief (exercise 4 own-caption row, exercise 4 distractor chips, exercise 5 connector row)

RUN = ~/Projects/and-again-content/runs/a67_20261008/. Input: RUN/content/source.json = the 8 shown lab items
(8055, 236, 7071, 8056, 62, 8039, 900001, 900002) with their key word, level (A/B), part of speech, the 3 carousel
captions + the scene of each carousel picture (`scenes[i].scene`, `scenes[i].models`), `writeAt` (the carousel picture
WITHOUT a prepared caption in exercise 3 - the learner writes it), the exercise-4 mind map (`mindMap.nodes[].caption` /
`partner` = the chip the bubble expects; for a verb `kind: timeline`), the exercise-4 rows (`[x]` = the gap), the tap
phrases, the story and the story phrases. Pictures: ~/Projects/and-again-content/runs/a65_20261007/stills/<id>.png,
carousel/<id>_<n>.png (n = 1..3 = picture 0..2), frames/. Look at the carousel picture `writeAt` of each item first.

## 1. `ownRow` - a new exercise-4 row (one per item)

Exercise 3 makes the learner write the caption of carousel picture `writeAt` in their own words. Exercise 4 then gets a
NEW row: a model caption of THAT picture with exactly ONE blank. Write it as a list of parts:
`{"parts": [{"text": "gym"}, {"text": "bag", "gap": true}], "source": "caption|models[n]", "blank": "key|other"}`.
- Use the picture's caption (`ownCaption`) itself when it works; you may use one of `ownCaptionModels` instead when the
  caption cannot satisfy the rules below (say so in `why`).
- Mix the blank across the 8 items: exactly 4 items blank the KEY WORD (or its form: for the verb "to select" the verb
  form, e.g. "will select"), 4 items blank ANOTHER part of the caption. Choose which items get which so both work well.
- AMBIGUITY RULE (hard): the blank's answer must not be the answer of any other space of the item's exercise 4 (no
  mind-map bubble `partner`, no row gap) and must not fit any other space; and no other space's answer may fit this
  blank. A blank that would repeat a bubble's partner (e.g. "[gym] bag" while the map has "gym bag | gym") is NOT allowed
  - then blank the key word, or use a model where the other part is new.
- The blank is a whole word or a short fixed chunk (1-3 words, no article alone, no punctuation). It must be
  guessable from the picture + the rest of the row.
- Keep the words exactly as in the caption / model (no new words, no "to" added). Capitals and the final full stop of
  a sentence caption stay.

## 2. `distractors` - extra chips for exercise 4's word box (Tips on)

With Tips on, the box holds every expected chip (the bubbles' partners, the rows' gaps, the own-row blank) PLUS 2-3
distractors per item: "near alternatives" a learner might confuse with a right chip - a different form ("a date" for
"date", "selects" for "selected"), a near word ("self-awareness" for "self-confidence", "pick" for "select", "swim
in" for "swim with"), or a word from the same scene that fits nowhere. Each distractor must fit NO space of the item
(test it against every bubble and every row incl. the own row: the sentence it makes must be wrong or clearly worse).
Level A: simple words. Never offensive, never a second correct answer.

## 3. `connectors` - exercise 5 page 2, the grey 5th row (a suggestion, never required)

One line of 3-4 linking words/phrases + "..." in lowercase, comma separated, e.g. "however, although,
unfortunately...", "first, then, finally...", "because, so, while...", "suddenly, luckily, in the end...". Vary them
across the 8 items (repeats of single words are fine, but no two items share the same line, and neighbours in the
order above should feel different). Fit them to the item's story / level: level A = first, then, but, so, because,
suddenly, luckily, finally, in the end, after that; level B may add however, although, unfortunately, meanwhile,
eventually, as a result, while, as soon as, instead.

## Output

RUN/content/writer.json:
{"<id>": {"ownRow": {...}, "distractors": ["...", "..."], "connectors": "...", "why": {"ownRow": "...",
"distractors": "...", "connectors": "..."}}}
Natural US English. Reply with one line.
