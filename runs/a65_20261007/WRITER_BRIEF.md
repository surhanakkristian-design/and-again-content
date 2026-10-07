# A65 writer brief (lab content, 8 items)

Folder: `~/Projects/and-again-content/runs/a65_20261007`. Input: `content/source.json` (the 8 lab items as they are live
now), the stills `stills/<id>.png` and the carousel pictures `carousel/<id>_<n>.png` (n = 1, 2, 3 = the carousel's order).
LOOK at every picture with the Read tool before writing about it. Write the result to `content/writer.json`.
Learners are 15-25, levels A (A1-A2) and B (B1-B2). English only (US spelling). No chat output; when done, reply with
one line: the file path and the number of items.

## 1. Exercise 3 "Choose and write the caption." - scene + model captions for EVERY carousel picture

The carousel has 3 pictures. Pictures 1 and 2 keep their tap captions (the caption in source.json). Picture 3 has NO
caption on screen: the learner writes (or speaks) their own caption for it, and an AI checker judges it against a
TEXT description of the picture (it never sees the picture). So for every picture (all 3 of every item) write:

- `scene`: 1-3 plain sentences, what is VISIBLY there (who, doing what, where, the key objects, colors only when they
  help). Concrete, no interpretation, no jokes. 15-45 words. It must let a checker decide whether a learner's caption
  describes this picture and not one of the other two.
- `models`: 2-3 model captions a native speaker would naturally write for the picture, each using the key word
  correctly. Model 1 = the existing caption for pictures 1 and 2 (unchanged, unless it is unnatural - then flag it in
  `notes`). For picture 3 the existing caption is one of the models too.
  - noun / adjective items: SHORT captions (2-6 words, no final full stop), the key word inside ("a beach bag",
    "to feed a dolphin", "classical music"); a verb collocation may start with "to".
  - verb item (900001 "select"): FULL SENTENCES in the tense the picture shows (picture 1 = past, 2 = present
    continuous / question, 3 = future with "will" or "going to"), different subjects allowed.
- `tense` (verb item only): "past" | "present" | "future".

## 2. Exercise 5 "Make a story." - the gap b)

New rule: parts a) and c) are shown in place; the learner writes part b) so that the story makes sense. The ordering
task is gone. Max length of b): level A 10 words, level B 15 words.

For each item:
- Keep the current story if a) and c) already leave a CLEAR gap that b) must fill (c) depends on something only b)
  says), and b) fits the word limit. Otherwise rewrite the story (about the item's picture, names the key word, a light
  funny point at the end, natural English a native speaker would say).
- a) = the opening (a full sentence or the first part of one), b) = the middle, c) = the end. Each part keeps its
  capitals and punctuation from its place in the story. Prefer b) as one complete sentence (easier to write).
- The whole story: level A at most 20 words, level B at most 25 words.
- `bModels`: exactly 2 model answers for b): model 1 = the story's own b); model 2 = a different natural b) that
  connects a) and c) just as well. Both within the word limit, both grammatical, both use simple everyday words.
- Avoid a b) the learner can only guess by mind-reading: a) and c) must make the content of b) inferable (c) refers to
  something b) introduced: a thing, an action, a reason).

## 3. Rules that apply to everything you write

- Would a native speaker say exactly this? If not, rephrase. ("to impress with self-confidence" is not natural; "got her
  a drink" not "went to bring her a drink").
- No literal picture jokes for fixed expressions.
- Never change pictures; never invent things that are not in the picture.

## Output `content/writer.json`

```json
{
  "8055": {
    "ex3": [ {"scene": "...", "models": ["...", "..."]}, {...}, {...} ],
    "ex5": {"story": ["a)", "b)", "c)"], "bModels": ["...", "..."], "changed": true, "why": "..."},
    "notes": ["anything else you noticed that looks unnatural in the source (do NOT change it, only list it)"]
  },
  ...
}
```
(`tense` inside each ex3 entry for 900001.)
