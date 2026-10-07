# A64 independent verifier (Opus 5.5) - ambiguity check (exercise 4), 6-order check (exercise 5), exercise 2 points

RUN = ~/Projects/and-again-content/runs/a64_20261007/. Input: RUN/verify/blind.json (the writer's content WITHOUT the
writer's reasons; the parts of each story are given in a SHUFFLED order labelled a / b / c). You have not seen the
writer's notes - do not open RUN/content/. Look at the pictures:
- videos: ~/Projects/and-again-content/runs/a59_20261006/verify/<id>/box_0*.jpg (fallback a58_20261006/verify/<id>/)
- pilots: ~/Projects/and-again-content/runs/a60_20261007/verify/select_boxes.jpg, classical_boxes.jpg
- exercise 2 with the zones drawn AFTER the writer's changes: RUN/zones/after/<id>.jpg (left 390x844, right 375x667;
  red = protected zones, yellow = object points, cyan = slots)

## 1. Exercise 4 ambiguity check (every item except 900001)
The learner sees: the key word in the centre of a mind map with N empty bubbles (ANY mind-map chip may go in ANY
bubble), the box of chips, and rows "to ..." each with one empty space. For EVERY chip of the box decide, as a careful
learner would, every place it could sensibly fill:
- (a) FAIL if a chip fits both a mind-map bubble and a row. A chip "fits a bubble" when chip + key word (or key word +
  chip) is a natural English collocation (e.g. "wooden" + bench, "to look at" + bench). A chip "fits a row" when the row
  with that chip is a natural phrase.
- (b) FAIL if a chip fits two different rows.
- Also FAIL: a row that contains the key word; a mind-map phrase without it; a row that does not match the picture;
  any grammar error.
Write one line per chip: the chip, the places it fits, PASS / FAIL.

## 2. Exercise 5 order check (all 8 items)
For each story you get three parts a / b / c. Without knowing the writer's order, test all 6 orders (abc, acb, bac,
bca, cab, cba) and say for each whether a careful reader would accept it as a sensible story (grammar across the joins,
capital letters and punctuation as given, pronouns after their names, cause before effect, a clear beginning / end).
PASS only when EXACTLY ONE order makes sense. Then judge the story: meaningful and good, fits the picture, level A at
most 20 words / level B at most 25 and close to it, no forced connector (a "But" / "Then" / "So" that connects nothing
is a FAIL), each part keeps its capitals / punctuation from its place, 100 % grammar, A1-A2 words at level A.

## 3. Exercise 2 points (items in blind.json "ex2")
Each moved point must lie ON its object (visibly) and outside every red zone at both sizes; a replacement noun must be
visible and outside the zones, and its phrase must match the picture.

## Output
RUN/verify/VERDICT.md (per item: the chip lines, the 6 order lines with the one order you found, the story verdict, the
exercise-2 verdict; PASS / FAIL per part and a final list of everything that must change) and RUN/verify/verdict.json:
{"<id>": {"ex4": "PASS|FAIL", "ex4_notes": "...", "story_order_found": "bca", "story": "PASS|FAIL", "story_notes": "...",
"ex2": "PASS|FAIL|-", "ex2_notes": "..."}}. Reply with one line.
