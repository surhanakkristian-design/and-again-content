# Blind judge task — Phase 1j, Task B (re-judging the rewritten Slovak)

You are a blind human-level judge of English translations of Slovak sentences. This file is
self-contained: everything you need is here.

## Files

- You may read **only** `phase1j/taskB/JUDGE_TASK.md` (this file) and
  `phase1j/taskB/judge_input.jsonl` (or the equal split `judge_input_part1.jsonl`,
  `judge_input_part2.jsonl`, `judge_input_part3.jsonl` — same content, 233 / 233 / 231 lines).
- You must **not** open `judge_keymap.json`, any file under `phase1j/dev/`, `phase1j/holdout/`,
  `phase1i/`, any ledger, any checker output, any report or any other agent's notes. They contain the
  old labels; seeing them would destroy the measurement.
- You write exactly one file: `phase1j/taskB/judge_output.jsonl`.
- Zero model/API calls. This is your own judgement, item by item.

## Input line

```json
{"k": "j0001", "sk": "<the Slovak sentence>", "answer": "<the learner's English>", "level": "A1|A2|B1|B2"}
```

There is no id, no old label, no reference translation, no type and no side. Some items are controls;
you cannot tell which, and you must not try.

## The protocol

Judge **each answer only against the Slovak sentence**, at the stated CEFR level, one item at a time,
in the order given. You are the ground truth: the question is not "what would a checker say" but
"is this a faithful, acceptable English translation of this Slovak sentence".

- **correct** = a faithful, acceptable English translation of THIS Slovak sentence. Synonyms,
  paraphrase, a different word order, a different but equivalent phrasing, British/American variants and
  natural style differences are all free. Minor punctuation or capitalisation is not an error.
- **wrong** = anything else: a different meaning, information added or dropped, the wrong time
  reference, or English that is not correct.
- **The explicit Slovak subject pronoun is binding.** These sentences state their subject
  (`on`, `ona`, `ono`, `oni`, `ony`, `ja`, `ty`, `my`, `vy`). An answer whose subject has another
  **person, number or gender** than the Slovak subject is **wrong**, type **S**. The Slovak is the
  ground truth; there is no gender licence in this pass.
- Where the Slovak leaves something genuinely open (an unnamed object's gender, a tense that English
  can render in more than one way), keep the benefit of the doubt for the learner.
- If you doubt an item, decide anyway and put the doubt in `note` (`"doubt: …"`). Never leave a line out.

## The four wrong-types (quoted from `phase1j/CONTEXT_1J.md` §6)

- **T** — tense / aspect: the right words, the wrong time reference.
- **W** — wrong word: a lexical substitution that changes which thing, person, place, time or quantity.
- **M** — meaning added or dropped: information in the answer that is not in the Slovak, or Slovak
  information missing from the answer (a single adverb, particle, place or time word counts).
- **S** — small slip family: article, preposition, agreement, word form / spelling slips that are still
  wrong English or change the meaning slightly.

A subject that disagrees in person, number or gender with the explicit Slovak pronoun is **S**.
If several types apply, choose the one that carries the main damage to the meaning.

## Output — `phase1j/taskB/judge_output.jsonl`, one line per input line, same `k`

```json
{"k": "j0001", "label": "correct", "type": null, "subj_ok": true, "note": ""}
{"k": "j0002", "label": "wrong", "type": "S", "subj_ok": false, "note": "she for on"}
```

- `label`: `"correct"` or `"wrong"`.
- `type`: `"T" | "W" | "M" | "S"` when `label` is `"wrong"`, otherwise `null`.
- `subj_ok`: `false` **iff** the answer's subject disagrees in person, number or gender with the Slovak
  subject; `true` otherwise (also `true` when the answer has no overt subject that could disagree).
  `subj_ok` is judged independently of `label`, and a `false` here always makes the item `wrong`.
- `note`: at most 8 words, may be empty.

Every `k` of your input must appear exactly once in the output.
