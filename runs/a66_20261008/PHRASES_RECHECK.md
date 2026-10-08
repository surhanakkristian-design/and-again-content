# A66 story phrases - independent RE-CHECK of the rewrites

RUN = ~/Projects/and-again-content/runs/a66_20261008/. You wrote none of this. Read RUN/PHRASES_WRITER.md and
RUN/PHRASES_REVIEW.md (the rules), RUN/content/source.json, RUN/content/phrases_writer.json (first draft) and
RUN/verify/phrases_review.json (a reviewer's final lists + changes). Pictures: ~/Projects/and-again-content/runs/a65_20261007/stills/<id>.png
and frames/<id>_NN.png (62, 236, 7071, 8039) - look before calling a phrase untrue.

For EVERY change of the reviewer: is the `after` text exactly what a native US speaker would say, true to the video,
taken from the item's exercises, useful for a story, and is its `match` right (rules in the briefs; test it against two
or three natural retellings, e.g. "The king rode the quad bike through the mud.")? Verdict ok / fix (with your text and
match). Also check every UNCHANGED final phrase and match once more. Exactly 4 per item.

Write RUN/verify/phrases_recheck.json:
{"<id>": {"final": [{"text": "...", "match": [[...]]}, ... 4], "verdicts": [{"text": "...", "verdict": "ok"|"fix",
 "why": "..."}]}}
Reply with one line (number of fixes).
