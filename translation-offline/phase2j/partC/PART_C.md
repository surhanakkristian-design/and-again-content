# Phase 2J Part C — false acceptances (stage S3, 0 model calls, closed-set analysis)
Stack: fixed TRANSLATION-ONLY (A2 F4v2+F4v3 fix on), results = phase2j/run_S2c (closed 2I set: coverage 464/497, FA 20/403 = 4.96 % [3.06, 7.56]).
Script: partC/partC.py (re-runs `checker_1i.f5_adjunct_deletion` on every current FA with the adapter annotation the stack sees); data: partC/partC_result.json.

## C1 — why F5 did not fire (all 20 current FAs)
Current FAs = 2I's 19 + A:250:m (new with the A2 fix). Dropped content word: **16** (2I's 15 + A:250:m); other: grammar 2 (A:1106:c4, A:2356:c5), wrong word 1 (A:3060:c5), judge doubtful 1 (A:423:m). All 20: layer L3, reply SAME, writer-M except the 3 intent-correct.

One code path for all 20, no exception. F5 (decide checker_1i.py:809 -> `f5_adjunct_deletion` :705) only fires when the answer is an ORDER-PRESERVING SUBSEQUENCE of a reference. `_subseq_positions` returns None at **checker_1i.py:669** (`if i < len(L): return None`) as soon as one answer token is not in the reference, and the loop skips that reference at **:719** (`continue`). Re-run trace for all 20: `fired False, reason "not a subsequence of any accepted variant"`. `span_information` (:683), where the content/adjunct test lives, is never reached.
Two things combine:
- **Thin references**: every one of the 20 sentences has exactly 1 reference (closed 2I set: 873/900 items one reference, 27 two). So a single paraphrased token in the answer is enough to break the subsequence.
- **The writer's M items paraphrase as well as drop**: every dropped-word answer also swaps at least one token (the "break" token, first answer token not matched in order):

| jid | lvl | dropped (judge) | break token(s) = answer tokens not in the reference |
|---|---|---|---|
| A:110:m | B1 | in one afternoon | incredible (for unbelievable) |
| A:250:m | B1 | country (vidieckej) | been, racing (reference v[0] = "had sped") |
| A:276:m | A2 | off the plant | must (for has to) |
| A:301:m | B2 | recycling | word order "so far" moved; goal (for target) |
| A:842:m | B2 | the lid | right (straight), then |
| A:1212:m | B1 | at the mirror | making (pulling), with her mouth open |
| A:1738:m | A2 | Look! | he (she), 's, heavily, right |
| A:2046:m | B2 | this morning | dude (bro), still, is |
| A:2486:m | B1 | through the door | were coming along (came up) |
| A:3285:m | B1 | of chairs | wobbling (swaying), climbing |
| A:3489:m | A2 | now | otherwise (or) |
| A:3563:m | A2 | today | put on (wore) |
| A:3573:m | A2 | totally | to go on |
| A:3672:m | A2 | hot | up (warm up) |
| A:3797:m | A2 | in the room | hey (yo), boring (dead), quite (kinda) |
| A:3957:m | A1 | raw | kind of (low-key) |
| A:423:m (doubtful) | A2 | honestly | here, seem |
| A:1106:c4, A:2356:c5, A:3060:c5 | | not a drop | many substitutions |

Secondary defect (token class), visible once subsequence is relaxed: `now`, `today`, `totally` are in checker_1i FUNCTION/INFO_FUNC, so any "content word" test built on FUNCTION misses A:3489:m, A:3563:m, A:3573:m; `Look!` is an interjection. F5's own `span_information` would count them (INFO_FUNC -> "adjunct adverb").

## C2 — deterministic fix, sized (NOT BUILT)
No bilingual SK->EN map or lemma list exists in the repo (filename search: only judge verdict files); the only lexical resource is the annotation `alt` (English token -> synonym-group names), used below as synonyms. Rules sized on the 3 labelled sets (catches = judge-wrong currently accepted newly rejected; cost = judge-correct currently accepted newly rejected):

| rule | closed 2I (20 FA) catch / cost | 1W test (16 FA) catch / cost | 1S rows_1s (8 FA) catch / cost |
|---|---|---|---|
| V1 a reference content word missing (every ref) | 15 / 297 | 11 / 65 | 5 / 158 |
| V2 net content deficit (missing > added, every ref) | 11 / 55 | 6 / 5 | 2 / 17 |
| V3 pure deletion modulo alt synonyms (some ref) | 3 / 16 | 3 / 30 | 0 / 12 |
| V4 word in ALL refs missing, answer adds no content | 3 / 16 | 3 / 0 | 0 / 12 |
| V5 F5 relaxed: F5 span_information on ref tokens absent from the answer, order ignored, answer adds only closed-class/synonym tokens | 5 / 34 | 1 / 3 | 0 / 22 |

Every variant costs judge-correct answers on the closed 2I set (minimum 16), so by the rule nothing is wired, no test added, no re-freeze. Typical cost: synonym not in `alt` (really/very, goal/target, lies/is, across/over), restructuring (It is cold in the room -> The room is cold; Every Sunday -> on Sundays). Without a Slovak-side content map the answer cannot be compared with the Slovak, and English-side comparison against ONE reference cannot tell a drop from a paraphrase. What would be needed: a Slovak content-word -> English lemma set per sentence (a reference-side annotation, e.g. from Part B's audit), then "a Slovak content word with no rendering in the answer" = wrong.
1S packet (phase1s/taskC/judge/packet.json, 183 items): carries no references or labels and none of its jids are in rows_1s -> not sizable deterministically; recorded, not faked.

## C3 — the A2-level FA 8.00 % [3.52, 15.16]
2I A2 FAs (8/100): A:276:m, A:423:m, A:1738:m, A:3489:m, A:3563:m, A:3573:m, A:3672:m, A:3797:m. Current stack: the SAME 8, 8/100 = 8.00 % [3.52, 15.16] (the A2 fix touched no A2 FA; A:250:m is B1).
Drivers: all 8 are writer-M, L3 SAME, single-reference, F5 non-subsequence (C1). 7 are dropped content (4 of them one closed-class word: now, today, totally, Look!; 3 a phrase/adjective: off the plant, hot, in the room) and 1 judge-doubtful (honestly). A2 sentences are short, so the M writer drops ONE word and paraphrases one other (must, put on, to go on, warm up) — the exact pattern that defeats F5 — and flash-lite treats a dropped time adverb / intensifier / interjection as immaterial. Per level on the current stack: A1 2/101, A2 8/100, B1 7/102 (2I 6, +A:250:m), B2 3/100.

Gemini calls S3: 0 (cumulative 43). Headless tokens 0.
