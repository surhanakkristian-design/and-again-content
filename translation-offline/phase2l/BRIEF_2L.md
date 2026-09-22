# Brief: Phase 2L — a source-side content check for SOURCE-ONLY; then build and measure Czech

(Verbatim copy of the owner's brief, 22.9.2026.)

Work in ~/Projects/and-again-content/translation-offline/phase2l/.
Read ONLY, once at the start: the 2K report (docs/features/reports/TRANSLATION_PRODUCTION_PHASE2K_REPORT.md),
phase2k/ (stack_source.py, spec/, analysis/part3.md + part3.json, GEMINI_LEDGER.json, stored L3 replies),
phase2j/ (partD/run, set, f4fix.py), phase2i/ (run, set, judge brief), phase1v/trackC/cz_reader.py,
phase2h/out/annotations_cz_final.jsonl.

## 0. Where we are, and the rule that stays
The owner's decision stands: the checker judges the answer against the SOURCE sentence only; the English reference does
not grade. 2K built SOURCE-ONLY and re-scored the closed Slovak sets: coverage 951/995 = 95.58 % [94.11, 96.77],
FA 73/805 = 9.07 % [7.18, 11.27]. All 25 reference-caused rejections are gone. The SAFETY STOP fired on FA.
2K's diagnosis: 44 FAs were added, 35 of them writer-type M — answers that DROP a noun, adjective or place phrase the
source carries ("A mushroom grows…" for *Veľká huba*, "…the gavel came down" for *obrovské kladivko*, "These seats are
completely empty!" without *vzadu*). The reference layers used to catch these; judging the whole sentence against the
Slovak, flash-lite says SAME. The owner's ruling was in the L3 prompt throughout and did not enforce itself.
This phase adds a SOURCE-SIDE content check. It must never read the reference.

Rules: nothing is written to the DATABASE — SELECT only. No deploy, no migration, no push, no rebase. Earlier phase
directories stay byte-identical; verify SHA-256 before and after. Write only under phase2l/. Commit every file
immediately. `nohup`, never `setsid`. Absolute paths everywhere.
Test first: a suite over the real code path, model mocked, must pass before any model call — a row number containing
"429", a real 429 envelope, a usage-limit envelope, resume at 0 cost, a relative path refused, and 2K's poison test
proving no reference field (`v`, `alt`, `lk`, `en`) is read anywhere, extended to the new check. If a test cannot pass,
STOP at 0 cost.
**If a headless session fails with a Claude usage-limit or quota error, STOP at once and write the report.**
**Parts A–C use NO headless Claude sessions** — Gemini calls on existing labelled data only.

## PART A — zero-call readout: TIP under SOURCE-ONLY
2K added 33 false rejections, 20 of them L3 TIP where the reference-based L3 said SAME. TIP-as-rejection was measured
under the reference-based prompt; under SOURCE-ONLY it may mean something else. Re-score the STORED 2K SOURCE-ONLY replies
on both closed sets with TIP accepted instead of rejected — 0 calls — and report coverage and FA beside TIP-rejected.
Do not adopt it yet; it feeds Part C.

## PART B — the second-stage content check
B1 Build it: ONLY for items SOURCE-ONLY L3 has ACCEPTED, ONE further call to the same model (gemini-3.1-flash-lite,
   temperature 0, thinkingBudget 0) given ONLY the source sentence, its language and the answer. One question: is any
   NOUN, ADJECTIVE, MAIN VERB or PLACE/DIRECTION PHRASE of the source missing from the answer, or its meaning changed?
   Reply exactly `NONE` or `MISSING: <source word>`. The prompt must state the owner's ruling explicitly: time adverbs,
   degree adverbs and interjections do NOT count (now, today, already, still, finally, then, totally, completely, just,
   Look!; Slovak teraz, dnes, už, ešte, konečne, vtedy, úplne, práve, Pozri!; Czech teď, dnes, už, ještě, konečně,
   tehdy, úplně, právě, Podívej!). A synonym or paraphrase that carries the same meaning is NOT missing. MISSING → reject.
   An unparsable reply is a FAILED call: counted, never guessed, never silently retried; report the rate.
B2 Run it on both closed Slovak sets (2I and 2J Part D), against their existing judge labels. Report, per set and pooled:
   catches (judge-wrong items newly rejected) and cost (judge-correct items newly rejected), every item listed with the
   word the model named, and how many of 2K's 35 added M false acceptances it catches.
B3 Label all of this a CLOSED-SET, IN-SAMPLE re-score: the sets were read while SOURCE-ONLY and this check were designed.

## PART C — the configuration, and the stop
Measure on both closed sets pooled: SOURCE-ONLY + B, with TIP rejected and with TIP accepted (Part A). Pick the one with
the higher coverage among those with FA below 5 % on the point.
**SAFETY STOP:** if no configuration reaches pooled coverage ≥ 90 % AND pooled FA < 5 % on the point, STOP here and write
the report. Do not spend Claude tokens on Czech. Freeze the chosen configuration and record its commit.

## PART D — build the Czech SOURCE-ONLY checker
A Czech checker has never been assembled or run. Mirror the frozen Slovak configuration exactly, with the Czech reader
(1V Track C's four fixes: -em, se, jestli, aspect lexicon) and `f4fix.build_fixed(CK, 'cz')` bound into AG and F4v2/F4v3,
reading the SOURCE only. The L3 source and the Part B check both use the CZECH sentence. Port every Slovak test and add
the Czech misreads 1T and 2J found (-em as 1sg, missing `se`, `jestli` as a participle, `příliš` as 2sg). Run 1T's Czech
gold validation once on the assembled readers and report agree / conservative / ERROR per guard beside Slovak's. 0 calls.
Write the Czech upload file `phase2l/upload/upload_cz_final.xlsx` (4,064 rows, `v[0] == en`, exercise_id integer, `v`
display-only, the reference-ending scan from 2K applied).

## PART E — measure Czech ONCE on fresh production
The method of 2I and 2J: 100 Czech sentences from `phase2h/out/annotations_cz_final.jsonl`, 25 per level, not overlapping
anything used before; 5 correct + 4 wrong each (500 / 400); 4 blind writers, one per level, seeing only the Czech sentence,
its level and topic; T / W / M / S balanced, no agent-drop floor; ONE judge prompt across 4 sessions, items shuffled across
levels, 80 hidden duplicates in different sessions, each session capped at 400,000 tokens, packets
`jid / czech / level / answer / topic`, the owner's rules verbatim including the dropped-word ruling, the practised
structure out of scope. Drop 2K defect 3's redundant older line from the judge prompt.
One stack: the Czech checker from Part D. Freeze and commit before opening; freeze hash and RUN commit; FINAL_RUN_DONE;
access log verbatim. Opened ONCE. This is the first OUT-OF-SAMPLE measurement of the SOURCE-ONLY design — say so.

## Constraints
Claude token budget: **2,000,000** from the harness. Print the plan; after every stage print cumulative tokens and the
projection; STOP rather than exceed. Stage order: A → B → C (safety stop) → D → E.
Gemini: counted = HTTP 200 only; a rate limit is detected ONLY from the status or error envelope, never from output text;
HARD CAP 3,500 calls across the phase; spend pre-approved to $1.00.
Your own tool calls: main session at most 24 with 4 in reserve; each agent at most 12, from the HARNESS.
Load the OAuth token as 2K did (`zsh -ic`); never print it. If headless spawning fails, STOP at 0 cost.

## Report
`docs/features/reports/TRANSLATION_PRODUCTION_PHASE2L_REPORT.md`. FIRST: Czech coverage and FA pooled and per level with
exact 95 % CP intervals, both targets on the point and the interval — or, if the Part C stop fired, say so first. Then
Part C's configuration table on the closed Slovak sets beside 2K (95.58 % / 9.07 %) and the reference-based stack
(89.75 % / 5.34 %). Then Part B's catches and cost item by item, Part A's TIP readout, Czech false rejections and false
acceptances by cause, Part D (the Czech stack and its gold validation beside Slovak), the Czech upload file, Gemini calls
and spend, Claude tokens against the budget, judge noise, defects recorded not fixed, and a 5-line judgement: whether the
content check fixes SOURCE-ONLY, whether Czech meets the targets, and whether Czech is fit to upload.

## Chat output
Write NOTHING to the chat while working. At the very end, one line only: the report path.
