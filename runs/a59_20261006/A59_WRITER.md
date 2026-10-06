# A59 writer brief - REWRITE one noun video's lab set under the owner's new rule 1

Read `WRITER_BRIEF.md` in this folder (RUN = `~/Projects/and-again-content/runs/a59_20261006/`) - every rule there still holds -
then this file; where they differ, THIS file wins. Your current content is `RUN/content/<id>.json` (A58, verified); change it.

## Owner rule 1 (A59, 6 Oct 2026): the key-word phrase first, always
- The FIRST phrase (`taps[0]`) always contains the KEY WORD as its placeable noun (`taps[0].noun` = the key word, e.g. "a king",
  "the king", "a bag"; `nouns[0]` = its display form = the key word "a king"). Examples: "to have a date", "to sit on a bench".
- It has a CLEAR DOER visible in the clip (`target`). When two people/things do it TOGETHER, either may be tapped: give the
  first doer in `keys` and the second in `"alsoKeys"` (same format: `"live:N"` or your own box list), and write the target as
  "the man and the woman". Regions of different targets (incl. the second doer) must never overlap.
- This phrase then appears again: exercise 2 (its noun, automatic), exercise 4 (its row, automatic) and the STORY (the phrase,
  inflected, in one of the three sentences - ideally the first).
- This holds even when exercise 1 is not shown (one actor, or a cut).
- Keep the other two phrases, nouns, gaps and story as they are wherever they still work; change only what the rule needs (the
  chain must hold: phrases -> nouns in the same order -> rows/gaps -> story). The mind map partners come from the carousel
  captions and do not change. The 6 bank pieces stay all different (watch a gap equal to a partner, e.g. gap "bow to" vs partner).
- Grammar 100 %, everything visible in the clip (muted), humour welcome, "laugh at" never "laugh about".
- Write in `notes` exactly what you changed and why.

Check: `python3 validate59.py <id>` (has the rule-1 checks) and `python3 draw59.py <id>`, LOOK at the box sheets and slots.jpg.
Reply with ONE short paragraph: the new phrases (targets), nouns, gaps, story, exercise 1 shown or not, and what changed.
