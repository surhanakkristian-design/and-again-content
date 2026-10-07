# A64 writer (Opus 5.5) - lab exercises 2, 4 and 5 under the owner's new rules

RUN = ~/Projects/and-again-content/runs/a64_20261007/. Input: RUN/content/source.json (the 8 lab items in wall order:
8055 balloon, 236 dolphin, 7071 king, 8056 bench, 62 bag, 8039 way, 900001 "to select" (verb), 900002 "classical"
(adjective); each with key word, part of speech, level, the 3 phrases + doers, the 3 nouns with their object points
(x, y = shares of the whole picture), the carousel captions, the current exercise 4 and the current story).

Look at the picture before writing anything:
- videos: ~/Projects/and-again-content/runs/a59_20261006/verify/<id>/box_0*.jpg (fallback a58_20261006/verify/<id>/)
- pilots: ~/Projects/and-again-content/runs/a60_20261007/verify/select_boxes.jpg, classical_boxes.jpg
- exercise 2 stills with the protected zones drawn: RUN/zones/before/<id>.jpg (left 390x844, right 375x667; red =
  zones, yellow dots = the nouns' object points, cyan = where the slot lands)

All English must be 100 % grammatical and natural. Level A uses A1-A2 words only; idioms only at level B.

## Part 1 - exercise 2 "Place the nouns": objects inside a protected zone
No drop target may sit in the bottom chip tray, the right rail column or the title bar (each + 16 px). Items listed with
`zoneProblems_ex2` have an object point inside a zone. For each flagged noun:
- If the SAME object is clearly visible somewhere outside the zones at BOTH sizes (e.g. the upper part of a path, the
  top of a bag, a man's torso), give a new object point (x, y as shares of the whole picture) ON that visible part of the
  object. Check it against both panels of zones/before/<id>.jpg (the panels are cover-cropped: a point near the top or
  bottom edge may be cut off at 375x667). Keep the point well inside the object (not on its edge).
- Only when no visible part of the object lies outside the zones, choose a DIFFERENT noun from the picture (its phrase
  changes with it - say so; noun 1 is the key word and cannot change, so for noun 1 only a new point is allowed).
Output per flagged noun: old point, new point, where on the object it is, or the replacement.

## Part 2 - exercise 4 "Use the words from the box." (nouns and the adjective pilot; 900001 "to select" keeps its timeline, unchanged - skip it)
Layout: a mind map (key word in the centre, empty bubbles around it), the box of chips, and "to ..." rows below.
- **Mind map = every phrase that contains the key word.** That is: the carousel captions (adjective / noun
  collocations, as before: "weight bench", "pod of dolphins") AND the key-word phrase(s) of the picture, including verb
  collocations (phrase 1 "to sit on a bench" -> the bubble's chip is "to sit on"). A verb chip in the mind map is written
  WITH "to" ("to sit on", "to paint", "to share"); a noun / adjective partner without ("weight", "basket", "young",
  "piano"). Each node = {"caption": the full phrase with the key word, "partner": the chip}. The partner must appear in
  the caption word for word. Keep every carousel caption as a node (they are exercise 3's captions); a picture phrase
  whose collocation duplicates a caption (900002: "classical music") is not added twice.
- **3-4 bubbles.** Nouns normally get 4 (3 captions + phrase 1). Fewer key-word collocations = fewer bubbles.
- **Rows = only phrases WITHOUT the key word, from the picture** ("to" + 2-7 words, things that happen or are visible in
  the picture). 2 rows with 4 bubbles, 3 rows with 3 bubbles (6 empty spaces in total). Prefer the item's existing
  phrases 2 and 3 when they lack the key word (they already have recordings and translations); a new phrase is fine
  when it is needed (it gets a recording and translations). Each row has exactly ONE gap: a verb part ("read") or a
  noun phrase ("a book"); choose the gap so the ambiguity rules below hold.
- **Mind-map slots are order-free** (any mind-map chip fits any mind-map bubble), so think of all bubbles as one pool.
- **Ambiguity rules (must hold; the verifier tests them):** (a) no box chip may fit both a mind-map bubble and a row:
  a row's chip must NOT form a sensible collocation with the key word (e.g. a row gap "wooden" or "look at" for "bench"
  is forbidden: "wooden bench", "to look at a bench" are key-word phrases), and a mind-map chip must not make sense in any
  row; (b) no chip may fit two different rows (e.g. two rows "to play [the violin]" / "to play [the cello]" share the
  verb, so their noun chips fit both - forbidden). Replace any ambiguous chip or row.
- Output for each item: `mindMap` {centre, kind "map", nodes [{caption, partner}]}, `rows` as part lists
  [{"text":"to","plain":true},{"text":"read"},{"text":"a book","gap":true}] (the parts joined by spaces = the phrase),
  and one line per chip: why it fits only its own place.

## Part 3 - exercise 5 "Make a story." (all 8 items)
- First write ONE good, meaningful story about the picture, using close to the word maximum: level A at most 20 words
  (aim 17-20), level B at most 25 (aim 21-25); count every word ("doesn't" = 1). Meaning and quality come first: a real
  little story that fits the clip / picture (events beyond it are fine when they do not contradict it), ideally with a
  funny or warm point at the end. The story names the key word (the key-word phrase or the key word itself).
- The number of sentences is free. Then split the story into EXACTLY 3 parts that clearly follow each other. A part may
  be a whole sentence, several sentences, or part of a sentence; each part keeps exactly the capitals and punctuation it
  has at its place in the story (a part that continues a sentence starts lowercase unless the word is a name / "I"; a
  part that ends mid-sentence keeps its comma or has no mark). The first part starts with a capital, the last ends with
  . ! or ?.
- **No forced connectors.** Use "But", "Then", "Finally", "So" ... only where they really connect the content. The
  current "But his dog looked at him and waited." is the example of what NOT to do (the "But" contrasts nothing).
- **Exactly one order must make sense:** test all 6 orders of the 3 parts and write one line per wrong order saying why
  it fails (grammar, a pronoun before its name, cause after effect, an obvious beginning / end). If two orders make
  sense, rewrite.

## Output
RUN/content/a64_content.json:
{"<id>": {"ex2": [{"noun": "...", "old": [x, y], "new": [x, y], "where": "...", "replacement": null}] (only flagged
items), "ex4": {"mindMap": {...}, "rows": [[...]], "chips": {"<chip>": "why only here"}} (not for 900001),
"story": {"parts": ["...", "...", "..."], "words": n, "orders": {"123": "makes sense", "132": "why not", ...}}}}
plus RUN/content/WRITER_NOTES.md (one short paragraph per item). Reply with one line.
