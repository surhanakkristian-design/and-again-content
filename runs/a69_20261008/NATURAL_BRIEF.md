# A69 naturalness review — lab exercise 3 captions (articles) and exercise 4 own rows

You did NOT write this content. Review it as an independent native (US) English reviewer.
Input: `content/draft.json` (8 items). Each item has its 3 carousel pictures (`scenes_new[i].picture`, relative to this
folder — LOOK at every picture with the Read tool), the scene text, the captions, the model captions, the mind map,
the rows and the new own row.

## What the learner sees
- **Exercise 3** ("Choose and write the caption."): 3 pictures, one caption each. The captions are SHORT for nouns /
  adjectives ("a beach bag", "to drop a bag"), full sentences for verbs. The owner wants captions with the article
  English needs: "a beach bag", "a gym bag", NOT "beach bag". A "to …" phrase stays a "to …" phrase. Uncountable /
  genre uses ("classical music", "classical piano" as a style) may stay without an article if that is what a native
  writes under such a picture.
- `scenes_new[i].models` = 2-3 model captions of picture i (the first = its caption); they are examples a checker uses.
- **Exercise 4** ("Fill white boxes."): a mind map (the key word in the centre, each bubble = `chip`, the phrase it
  makes = `caption`), the rows (`[x]` = the white box to fill), and the own row = a model caption (or a contiguous part
  of one) of picture `writeAt` with ONE white box.
  With Tips on the learner gets exactly the answer chips (one per white box, NO distractors) and places them.

## Check, for every item
1. **Captions:** would a native (US) speaker write exactly this caption under this picture? Is the article right
   (a / the / none)? Is it TRUE of the picture? Return a better caption only if needed.
2. **Model captions:** natural, true of their picture, correct articles.
3. **Own row (`own_row_new`):** natural as a caption fragment, true of picture `writeAt`, and:
   - it must NOT repeat a phrase that is already in the mind map or a row: no word of another box's answer may be
     visible in it, its answer may not be another box's answer, and it may not be the same collocation as a map
     phrase (e.g. map "gym" + own row "gym [bag]" is forbidden; "people bowing to the king" next to the map's
     "to bow to" is forbidden);
   - unambiguous with Tips on: list ALL answer chips of the item (map chips, row answers, own answer) and test every
     chip in every white box — no other chip may fit the own row's box naturally, and the own row's chip may not fit any
     other box. Report every pair that fits.
   - the blank should be a meaningful word (not "a" / "the").
4. If you change something, give the full new text and say why in one line.

## Output
Write `content/review.json`: a list of 8 objects
`{ "mediaId", "captions": [3 final captions], "models": [[...],[...],[...]], "own_row": "text with [box]", "verdict":
"ok" | "changed", "notes": ["one line each"] , "ambiguous_pairs": [] }` and nothing else. Keep a caption / model /
own row as it is when it is fine. Do not touch anything not listed here.
