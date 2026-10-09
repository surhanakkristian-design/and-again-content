# A71 exercise 4 ambiguity test + exercise 5 blind order test

You did not write these texts. Files: `audit/after1_<id>.json` for the 8 lab items.

**Part 1 - exercise 4 (the white boxes):** the learner sees the map / timeline (centre + bubbles, each bubble = one white
box; on a MAP the bubbles are order-free: any bubble's word fits any bubble), the rows (`ex4_rows`, `[x]` = the white box,
its answer x) and the own row (`ex4_ownRow`). The word box holds exactly the answers. For EVERY answer chip, try it in EVERY
other box: does it make a correct, natural English phrase there that a teacher would have to accept? (On a map, a bubble
word in another bubble is fine - that is order-free; a bubble word in a row or the own row, or a row's word in a bubble or
another row, is the problem.) List every such case as `ambiguous` with the phrase it makes. Also flag a box whose answer is
VISIBLE elsewhere in exercise 4 (gives it away).

**Part 2 - exercise 5 (BLIND):** for each item take the 3 story parts, write out all 6 orders and say for each whether it
makes a sensible story. Exactly ONE order may make sense (the given one, a-b-c). List any other sensible order.

Write `review/ambig71.json`: `{ "<id>": { "ex4": [{ "chip": "...", "box": "...", "makes": "...", "verdict": "ok"|"ambiguous"|"visible" }],
"ex5": { "sensible_orders": ["abc", ...], "notes": "..." } } }`. Reply with the problems only.
