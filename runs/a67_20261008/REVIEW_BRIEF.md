# A67 naturalness + ambiguity review (independent; you did not write this content)

RUN = ~/Projects/and-again-content/runs/a67_20261008/. Read WRITER_BRIEF.md (the rules), content/source.json (the items)
and content/writer.json (the writer's output). Pictures: ~/Projects/and-again-content/runs/a65_20261007/stills/<id>.png,
carousel/<id>_<n>.png (n = 1..3 = carousel picture 0..2). Look at carousel picture `writeAt` of every item and at the
still before you judge.

For each of the 8 items check, and fix what fails:
1. `ownRow`: would a native (US) speaker say exactly this as a caption of that picture? Is it TRUE of the picture? Is the
   blank guessable from the picture + the row? Are the words exactly from the caption / that picture's models?
2. Ambiguity (hard rule): build the item's full exercise 4 = every mind-map bubble (centre key word + `partner`), every
   existing row with its [gap], and the own row. Put EVERY chip (all expected answers + the distractors) into EVERY space
   and read the result. A chip other than the expected one that makes a natural, true phrase in a space = fail. Two
   spaces expecting the same answer = fail.
3. Distractors: plausible near alternatives, but each fits no space; nothing offensive; level-appropriate.
4. Connectors: natural lowercase lines, 3-4 items + "...", fit the level, no two items share the same line.
5. The mix: exactly 4 items blank the key word, 4 another part.

Write content/review.json: {"<id>": {"ok": true|false, "changes": [{"field": "...", "before": ..., "after": ...,
"why": "..."}], "chip_test": "one line: what you tested and the result"}} and content/final.json = writer.json with your
fixes applied (same shape, without "why"). Reply with one line.
