# A66 blind order test (exercise 5 page 1 = ordering the story's 3 parts again)

RUN = ~/Projects/and-again-content/runs/a66_20261008/. You did NOT write these stories and you do not know their
order. Open ONLY RUN/verify/blind/blind.json and the pictures (do NOT open RUN/content/, RUN/before/, the app repo or
any other run folder's content files). Pictures (one still per item): ~/Projects/and-again-content/runs/a65_20261007/stills/<id>.png;
for the videos 62, 236, 7071, 8039 also one frame per second: ~/Projects/and-again-content/runs/a65_20261007/frames/<id>_NN.png.

Each item gives one short story split into three parts, shown in a SHUFFLED order labelled a / b / c. In the app the
learner sees the three parts as chips and taps them into order; capitals and punctuation are shown exactly as given.

For EVERY item write all 6 orders (abc, acb, bac, bca, cab, cba) as the full text joined with spaces, and for each say
whether a careful native reader would accept it as a sensible story: grammar across the joins (a part starting
lowercase must continue a sentence; a part ending with a comma cannot end the story), capitals and punctuation as given,
pronouns after their names, cause before effect, a clear beginning and a clear end (the funny point last).
PASS only when EXACTLY ONE order makes sense; FAIL when zero or two or more make sense (name them).
Also note anything unnatural or a story that does not fit the picture (one line), but the verdict is about the order.

Output RUN/verify/blind/blind_result.json:
{"<id>": {"orders": {"abc": {"text": "...", "sensible": true|false, "why": "short"}, ...6 entries},
 "sensible_orders": ["..."], "verdict": "PASS"|"FAIL", "notes": "..."}}
and RUN/verify/blind/BLIND_RESULT.md (a readable table). Reply with one line (counts PASS / FAIL).
