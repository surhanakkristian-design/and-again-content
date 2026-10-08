# A66 story phrases - naturalness + usefulness reviewer (owner rule 7)

RUN = ~/Projects/and-again-content/runs/a66_20261008/. You did NOT write these. Read RUN/PHRASES_WRITER.md (the task
and the `match` rules), RUN/content/source.json (each item's exercises) and RUN/content/phrases_writer.json (the
writer's 4 phrases per item). Pictures: ~/Projects/and-again-content/runs/a65_20261007/stills/<id>.png (all 8) and
frames/<id>_NN.png (videos 62, 236, 7071, 8039; one frame per second - a thing may be visible only in a later frame).
LOOK at the still / frames of an item before calling a phrase untrue.

For EVERY phrase ask:
1. "Would a native US speaker say exactly this?" as a phrase to use in a story (a fragment like "couldn't lift it",
   "the old king" or "to run down it first" is not a natural, reusable phrase; "to want a walk, not a story" is a quote
   of the funny line, not a building block). Natural, reusable chunks: "to have a date", "to laugh about the jokes",
   "blind, dream or double date".
2. Is it TRUE to the video (frames) and taken from this item's exercises (tap phrases, ex4 rows, mind-map / carousel
   captions, story)? Shortening is fine; new words are not (except the minimal change a natural chunk needs, e.g.
   "to pack a bag" instead of a story's "packed a picnic bag").
3. Is the set of 4 the MOST USEFUL for writing a story about THIS video (the doer, the main action, the funny point)?
   Phrase 1 should hold the key word. Grouping alternatives with "or" (at most 3, e.g. "beach or gym bag") is welcome
   where the carousel / mind map offers real alternatives a story could use - but not just to cram.
4. `match`: lemmas (lowercase, singular, infinitive; a real base form), in the order a natural retelling keeps,
   smallest set that still means THIS phrase (verb + key noun, or a distinctive verb alone), no "to"/articles/
   possessives/prepositions/pronouns, one alternative per "or" option, hyphenated words one token, multi-word nouns
   each word. Too loose (matches nearly any story about the video) or too strict (a natural retelling like "the king
   rode the quad bike" -> must match "to ride a quad bike") = fix.

Rewrite what fails; keep what is fine. Output RUN/verify/phrases_review.json:
{"<id>": {"final": [{"text": "...", "match": [[...]]}, ... exactly 4],
          "changes": [{"before": "...", "after": "...", "why": "one line"}], "notes": "..."}}
Reply with one line (number of changes).
