# A65 naturalness check (owner rule 7) - reviewer brief

You did NOT write this content. Folder `~/Projects/and-again-content/runs/a65_20261007`.
Input: `content/source.json` (the 8 lab items as live now: ex1 tap phrases, ex2 nouns, ex3 carousel captions, ex4 mind
map + rows, ex5 story) and `content/writer.json` (NEW content of this run: ex3 `scene` + `models` per carousel picture,
ex5 new story with gap b) and `bModels`). Pictures: `stills/<id>.png`, `carousel/<id>_<n>.png` - look at them (Read).
Write `verify/natural_review.json`. No chat output; reply with one line (path + number of changes) when done.

## The question for EVERY phrase and sentence

"Would a native speaker of (US) English say exactly this?" Check: every ex1 phrase, every ex2 noun, every carousel
caption, every mind-map caption and chip, every ex4 row, every story part (live AND new), every model caption and every
b) model, and the scene descriptions (plain and accurate is enough there). Unnatural = a collocation natives do not use,
a wrong or stiff preposition, a calque, an odd article ("pod of dolphins" without "a" is fine as a caption only if natives
caption it like that), British vs US words, "went to bring her a drink" (-> "got her a drink"), "to impress with
self-confidence" (-> a natural form).

Also check:
- No literal picture jokes for fixed expressions (e.g. no blind people for "blind date"): look whether a carousel picture
  shows a fixed expression literally.
- Exercise 2 nouns: an abstract noun is allowed only if it belongs to one clear visible place in the picture.
- Facts: a phrase / caption that does not match its picture (flag it; fix it if a natural rewrite that matches exists).

## Rewrites must keep the mechanics

- ex1 phrases: "to" + 2-7 words; phrase i contains ex2 noun i (same words, article may differ); phrase 1 holds the key
  word; the tap target stays the same thing (do not move a phrase to another doer).
- ex2 nouns: visible things; noun 1 = the key word.
- ex3 captions (nouns / adjectives): short, no full stop, with the key word; verb item 900001: full sentences, one past /
  one present / one future. A changed caption also changes its mind-map node (same caption, the chip = the caption's
  part without the key word; a verb collocation's chip keeps "to": "to fly in" + balloon).
- ex4 rows: "to" + 2-7 words WITHOUT the key word, exactly one gap (the chip); no chip may fit both the map and a row
  or two rows.
- ex5: exactly 3 parts a) b) c) keeping capitals / punctuation; b) at most 10 words (level A) / 15 (level B); story at
  most 20 (A) / 25 (B) words; it names the key word; exactly one order makes sense; bModels = 2, both fit.
- Prefer the smallest change. Do not change what is natural.

## Output `verify/natural_review.json`

```json
{
  "changes": [
    {"id": 8055, "field": "ex3.caption[2]" | "ex1.phrase[0]" | "ex2.noun[1]" | "ex4.node[3].caption" | "ex4.node[3].partner" |
       "ex4.row[1]" | "ex5.story[1]" | "ex5.bModels[0]" | "ex3.models[2][1]" | "ex3.scene[0]" | ...,
     "before": "...", "after": "...", "why": "one line"}
  ],
  "flags": [ {"id": 62, "what": "a problem you could not fix by text alone (e.g. a tap phrase whose thing is not visible)"} ],
  "checked": <number of texts you judged>
}
```
For an ex4 row give the whole row text with the gap chip in [brackets]: "to carry [a man]".
