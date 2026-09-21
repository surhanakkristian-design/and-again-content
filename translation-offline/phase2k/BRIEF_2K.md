# Phase 2K — orchestration file (owner's brief verbatim in §B, stage plan in §S)

All paths absolute. ROOT = /Users/kristiansurhanak/Projects/and-again-content/translation-offline
P2K = ROOT/phase2k   P2J = ROOT/phase2j   P2I = ROOT/phase2i   P2H = ROOT/phase2h   P1V = ROOT/phase1v   P1T = ROOT/phase1t
Content repo: /Users/kristiansurhanak/Projects/and-again-content (commit everything under P2K there, with a literal `git -C /Users/kristiansurhanak/Projects/and-again-content ...`;
zsh `$G`-style git variables silently skipped commits in 2J — never use them).
Report: /Users/kristiansurhanak/Projects/and-again/docs/features/reports/TRANSLATION_PRODUCTION_PHASE2K_REPORT.md
(commit it in the and-again repo with `git -C /Users/kristiansurhanak/Projects/and-again`, copy to P2K/ and commit there). Never push.

## §R Common rules for every stage agent
- Allowed reading: this file, P2K/PROGRESS.md, P2K files of earlier stages, and the owner's allowed sources ONLY:
  P2J/TRANSLATION_PRODUCTION_PHASE2J_REPORT.md, P2I/TRANSLATION_PRODUCTION_PHASE2I_REPORT.md, P2J/ (upload/, f4fix.py, test_2j.py, set/,
  run/, analysis/, and the 2J stack/runner files it imports: stack_tonly.py, run_2j.py, adapter_2f.py, write_guard.py, PROGRESS.md),
  P2I/ (TRANSLATION-ONLY stack, runner, set, run, judge brief; P2I/CONTEXT.md is the technical map — use it instead of re-reading the chain),
  P1V/trackC/cz_reader.py, P2H/out/annotations_cz_final.jsonl. The chain modules named by P2I/CONTEXT.md may be read only as needed for the
  code path in question. Stage S3 may additionally locate and read 1T's Czech gold-validation file(s) under P1T (one `find`).
  Read each source once; record what you learned in PROGRESS.md so later stages do not re-read.
- Nothing written to the DATABASE (SELECT only). No deploy, no migration, no push, no rebase. Write only under P2K (plus the report file).
- Earlier phase directories stay byte-identical: S1 writes P2K/SHA_before.txt with the same generator 2J used (P2I/sha_tree.sh, all phase*/
  except phase2k; the pre-existing dirty phase1p/access_log.jsonl + run_1p.log pair is part of the baseline). Every stage ends by
  re-running it into P2K/SHA_after_S<n>.txt and diffing against SHA_before (must be empty; if not, STOP and write P2K/STOP_sha.md).
- python via `python3 -B` / PYTHONDONTWRITEBYTECODE=1; copy chain modules into P2K, never run earlier-phase code in place; use the
  write_guard.py pattern so nothing can write outside P2K. Absolute paths in every invocation. Long jobs under `nohup` (NEVER setsid).
  Commit every file immediately after writing it.
- TEST FIRST: no model call (Gemini or headless Claude) before P2K/test_2k.py passes over the REAL code path with the model mocked, including:
  a row/item number containing "429" (must not be read as a rate limit), a real 429 envelope (retried, not counted), a usage-limit envelope
  (hard STOP), resume at 0 cost, a relative path refused cleanly (never a crash mid-run), and a test asserting the SOURCE-ONLY verdict path
  reads no reference field (`v`, `alt`, `lk`, `en`) anywhere — e.g. items whose v/alt/lk/en are poison objects that raise on any access,
  plus an assertion that no reference string appears in any L3 request body. Plus the §1.2 reference-ending test. If a test cannot pass:
  STOP at 0 cost, write P2K/STOP_<stage>.md.
- Gemini: L3 = gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, replies SAME / TIP / DIFF, TIP-as-rejection ON (2I/2J transport:
  counted = HTTP 200 only; rate limit detected ONLY from HTTP status or error envelope, never output text).
  HARD CAP 3,000 counted calls for the whole phase; spend cap $1.00. Keep P2K/GEMINI_LEDGER.json {stage: counted} and check it before any call.
- Headless Claude (only S4/S5 need it): 2J recipe (P2I/CONTEXT.md §2, P2J/run_2j.py spawner; OAuth token loaded via `zsh -ic`, NEVER printed;
  --output-format json; usage from the envelope). A usage-limit/quota error in ANY headless session -> STOP at once, write
  P2K/STOP_usage_limit.md; the orchestrator then writes the report. If headless spawning fails -> STOP at 0 cost.
- Claude token budget for the WHOLE phase: 2,200,000 (harness-counted, all agents + headless sessions). Append to P2K/TOKENS.jsonl
  {stage, headless_tokens, agent_est}. Before any headless spend, project the remaining stages; if the projection exceeds the budget, STOP.
- Tool calls: at most 12 per agent (you), counted by the harness. Batch work into scripts and heredocs.
- At the end of your stage append a section to P2K/PROGRESS.md: what was built, numbers, files (with line numbers where the brief asks),
  Gemini calls (stage + cumulative), headless tokens, SHA check result, and what the next stage must know. Reply to the orchestrator in
  <= 15 lines. Write nothing else anywhere.

## §S Stage plan (order Part 1 -> 2 -> 3 (safety stop) -> 4 -> 5)
S1  Setup + Part 1 + Part 2 (0 model calls). SHA_before. Copy 2J's FIXED translation-only stack (with f4fix bound in) into P2K.
    Part 1: §1.1 ruling verbatim into P2K copies of the judge brief, the writer spec and the L3 prompt (SK and CZ versions);
    §1.2 restore the 4 truncated SK references (ex 927, 22385, 35040, 41408) from the pre-B3 value (P2I/upload vs P2J/upload), plus the
    reference-ending test over BOTH files (SK final, CZ from P2I/upload) — ending in a preposition or article; list every hit;
    §1.3 P2K/upload/upload_sk_final.xlsx + UPLOAD_README.md (4,064 rows, v[0]==en, exercise_id int, `v` display-only / no longer grades).
    Part 2: build P2K/stack_source.py (SOURCE-ONLY) per §2.1-2.3; a table of EVERY removed layer with the file and line numbers in the
    2J stack (L1 exact-reference accept, F3, F5, every other read of v/alt/lk/en), and whether AG / F4v2 / F4v3 read a reference (remove it,
    say so). Build P2K/run_2k.py (2J transport + ledger + resume + headless spawner, language-parametrised sk|cz) and P2K/test_2k.py (§R list).
    Tests must pass. Freeze: P2K/FROZEN_SHA_S1.txt + commit hash in P2K/FREEZE_COMMIT_S1.txt.
S2  Part 3 (Gemini only, <= ~1,800 calls). Closed-set re-score of SOURCE-ONLY over 2I's 900 and 2J's 900 items vs their EXISTING judge
    labels. Coverage + FA with exact 95 % CP per set, pooled, per level, beside the reference-based results (2I 89.13 %/4.71 %,
    2J 90.36 %/5.97 %), every changed verdict with cause, how many of 2J's 25 reference-caused FRs are now accepted, FAs added/removed.
    Write P2K/analysis/part3.md. SAFETY STOP: pooled FA > 8.0 % -> write P2K/STOP_part3.md and stop (no Czech).
S3  Part 4 (0 model calls). Czech SOURCE-ONLY stack mirroring Slovak exactly: P1V/trackC/cz_reader.py (4 fixes: -em, se, jestli, aspect
    lexicon) + f4fix.build_fixed(CK,'cz') bound into AG and F4v2/F4v3; L3 source = the Czech sentence, language named Czech. Port every
    Slovak test + the Czech misreads (-em as 1sg, missing `se`, `jestli` as participle, `příliš` as 2sg). Run 1T's Czech gold validation once:
    agree / conservative / ERROR per guard beside Slovak. Czech upload P2K/upload/upload_cz_final.xlsx (from the 2H/2I Czech file: 4,064 rows,
    exercise_id int, v[0]==en; truncation scan only, report hits; no other reference correction). Tests pass; freeze (FROZEN_SHA_S3.txt,
    FREEZE_COMMIT_S3.txt).
S4  Part 5 set + writers + judge (headless Claude). 100 Czech sentences from P2H/out/annotations_cz_final.jsonl, 25 per level, not
    overlapping ANY exercise used in any earlier phase set (scan all phase*/ set files for cz exercise ids / sentences); 4 blind writers
    (one per level, seeing only the Czech sentence, level, topic), 5 correct + 4 wrong per sentence (500/400), T/W/M/S balanced, no
    agent-drop floor; ONE judge prompt across 4 sessions, items shuffled across levels, 80 hidden duplicates in different sessions, each
    session capped at 400,000 tokens, packets `jid / czech / level / answer / topic`, owner's rules verbatim incl. §1.1. Do NOT open the
    stack on the set. Freeze + commit before opening: P2K/FROZEN_SHA.txt, FREEZE_COMMIT.txt, then RUN_COMMIT.txt.
S5  Part 5 run + analysis. Open ONCE with the Czech SOURCE-ONLY stack; FINAL_RUN_DONE; access log verbatim. Coverage/FA pooled and per
    level, exact 95 % CP, both targets (cov >= 90 %, FA < 5 %) on point and interval; every Czech FR and FA by cause; judge noise from the
    80 duplicates. Write P2K/analysis/part5.md.
S6  Report (orchestrator or a report agent): the §B report structure.

## §B The owner's brief, verbatim

# Brief: Phase 2K — the checker judges against the SOURCE sentence only; close Slovak; build and measure Czech

Work in ~/Projects/and-again-content/translation-offline/phase2k/.
Read ONLY, once at the start: TRANSLATION_PRODUCTION_PHASE2J_REPORT.md, TRANSLATION_PRODUCTION_PHASE2I_REPORT.md,
phase2j/ (upload/, f4fix.py, test_2j.py, set/, run/, analysis/), phase2i/ (TRANSLATION-ONLY stack, runner, set, run,
judge brief), phase1v/trackC/cz_reader.py, phase2h/out/annotations_cz_final.jsonl.

## 0. THE OWNER'S DECISION — the English reference no longer grades anything
The learner is given a sentence to translate. The only thing that matters is whether their answer is a correct
translation OF THAT SENTENCE. The stored English reference is irrelevant to grading; the owner's words: judge the
answer against the translation the learner was given — that is the most important thing.
So the checker becomes SOURCE-ONLY: the model sees the SOURCE sentence and the ANSWER, never a reference, and answers
one question — is this a correct English translation of this sentence?
Why it matters: in 2J, references that were wrong or too narrow were the largest false-rejection cause (25 of 48),
and 2I defect 2 already noted the L3 system text said "SAME = same as the reference" while another line said "judge
against the Slovak". SOURCE-ONLY removes both.
The reference STAYS in the data: the app shows it as the correct answer when the learner is wrong. It stops grading.

Rules: nothing is written to the DATABASE — SELECT only. No deploy, no migration, no push, no rebase. Earlier phase
directories stay byte-identical; verify SHA-256 before and after. Write only under phase2k/. Commit every file
immediately. `nohup`, never `setsid`. Absolute paths everywhere.
Test first: a suite over the real code path, model mocked, must pass before any model call — a row number containing
"429", a real 429 envelope, a usage-limit envelope, resume at 0 cost, a relative path refused, and a test asserting the
SOURCE-ONLY verdict path reads no reference field (`v`, `alt`, `lk`, `en`) anywhere. If a test cannot pass, STOP at 0 cost.
**If a headless session fails with a Claude usage-limit or quota error, STOP at once and write the report.**
**Minimise Claude tokens.** Parts 1–3 need no headless writers or judges; only Part 5 does.

## PART 1 — close Slovak (no measurement)
1.1 Write the owner's dropped-word ruling VERBATIM into the judge brief, the writer spec and the L3 prompt, both
    languages: Dropping a word is judged by its KIND. ACCEPTABLE to drop: time adverbs, degree adverbs and interjections
    — now, today, already, still, finally, then, totally, completely, just, Look! (Slovak: teraz, dnes, už, ešte,
    konečne, vtedy, úplne, práve, Pozri!; Czech: teď, dnes, už, ještě, konečně, tehdy, úplně, právě, Podívej!). WRONG to
    drop: nouns, adjectives, main verbs, and place or direction phrases — hot, in the room, off the plant. The owner's
    reason: where even the model does not treat it as a serious error, it is not counted as one.
1.2 Repair the 4 truncated references B3 produced in the Slovak file (ex 927, 22385, 35040, 41408) by restoring them as
    they were before B3 — the learner sees them as the correct answer. Add a test that fails on any reference, in either
    file, ending in a preposition or an article.
1.3 Write the final Slovak upload `phase2k/upload/upload_sk_final.xlsx` + `UPLOAD_README.md`, 4,064 rows, `v[0] == en`,
    exercise_id an integer. State in the README that `v` is display-only and no longer grades.

## PART 2 — build SOURCE-ONLY from 2J's fixed TRANSLATION-ONLY stack
2.1 The L3 request carries ONLY the source sentence, its language, and the answer. No reference, no `v`, no `alt`, no
    `lk`, no English sentence. The system text asks whether the answer is a correct English translation of the source,
    and carries the owner's rules: the time frame must match the source while the English tense inside it is free; a
    passive is acceptable, but a passive that drops an agent the source names is WRONG; a missing obligatory English
    article is an ERROR while the choice of article is free; the §1.1 dropped-word ruling; added content is WRONG; any
    correct English with the same meaning is correct, whatever grammar structure it uses. Same model and settings:
    gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, replies SAME / TIP / DIFF, TIP-as-rejection ON.
2.2 Remove from the verdict path EVERY layer that compares the answer with a stored reference — the L1 exact-reference
    accept, F3 and F5 (subsequence and deletion against the reference), and any other read of `v`, `alt`, `lk` or `en`.
    Name every file and line removed. Every answer that is not rejected by a source-side guard goes to L3.
2.3 KEEP the deterministic guards that read the SOURCE: AG (agent ruling) and the fixed F4v2/F4v3 (person, number,
    gender). If either reads a reference anywhere, remove that read and say so.

## PART 3 — test SOURCE-ONLY on the Slovak data we already have (Gemini only, ~1,800 calls, ~$0.25)
Re-run L3 with SOURCE-ONLY over BOTH closed Slovak sets — 2I's 900 items and 2J's 900 items — against their EXISTING
judge labels. **No new writers, no new judges, no headless Claude sessions.** Label it a closed-set re-score.
Report, for each set and pooled: coverage and FA with exact 95 % CP intervals, beside the reference-based results on the
same items (2I 89.13 % / 4.71 %, 2J 90.36 % / 5.97 %), per level, and every item whose verdict changed with its cause.
Specifically: how many of 2J's 25 reference-caused false rejections are now accepted, and how many false acceptances
SOURCE-ONLY adds or removes.
**SAFETY STOP:** if pooled FA over the two sets exceeds 8.0 %, STOP here and write the report — do not spend Claude tokens
on Czech. Otherwise continue with SOURCE-ONLY; it is the owner's decision.

## PART 4 — build the Czech SOURCE-ONLY checker
2J §3 A5: a Czech checker has never been assembled or run. Assemble it by mirroring the Slovak SOURCE-ONLY stack exactly,
with the Czech reader (1V Track C's four fixes: -em, se, jestli, aspect lexicon) and `f4fix.build_fixed(CK, 'cz')` bound
into AG and F4v2/F4v3. The L3 source is the CZECH sentence. Port every Slovak test and add the Czech misreads 1T and 2J
found (-em as 1sg, missing `se`, `jestli` as a participle, `příliš` as 2sg). Run 1T's Czech gold validation once on the
assembled readers and report agree / conservative / ERROR per guard beside Slovak's. 0 model calls.
No reference audit for Czech, and no reference correction beyond scanning for truncation — SOURCE-ONLY does not read them.

## PART 5 — measure Czech ONCE on fresh production
The method of 2I and 2J, only the language changes: 100 Czech sentences from `phase2h/out/annotations_cz_final.jsonl`,
25 per level, not overlapping anything used before; 5 correct + 4 wrong each (500 / 400); 4 blind writers, one per
level, seeing only the Czech sentence, its level and topic; T / W / M / S balanced, no agent-drop floor; ONE judge prompt
across 4 sessions, items shuffled across levels, 80 hidden duplicates in different sessions, each session capped at
400,000 tokens, packets `jid / czech / level / answer / topic`, the owner's rules verbatim including §1.1.
One stack: Czech SOURCE-ONLY. Freeze and commit before opening; freeze hash and RUN commit; FINAL_RUN_DONE; access log
verbatim. Opened ONCE. Gemini: counted = HTTP 200 only; rate limit detected ONLY from the status or error envelope,
never from output text; HARD CAP 3,000 calls across the phase; spend pre-approved to $1.00.

## Constraints
Claude token budget: **2,200,000** from the harness. Print the plan; after every stage print cumulative tokens and the
projection; STOP rather than exceed. Stage order: Part 1 → 2 → 3 (safety stop) → 4 → 5.
Your own tool calls: main session at most 24 with 4 in reserve; each agent at most 12, from the HARNESS.
Load the OAuth token as 2J did (`zsh -ic`); never print it. If headless spawning fails, STOP at 0 cost.

## Report
`docs/features/reports/TRANSLATION_PRODUCTION_PHASE2K_REPORT.md`. FIRST: Czech coverage and FA pooled and per level with
exact 95 % CP intervals, both targets (coverage ≥ 90 %, FA < 5 %) on the point and the interval. Then Part 3's Slovak
re-score beside the reference-based results, with how many reference-caused rejections disappeared and what happened to
FA. Then every Czech false rejection and false acceptance by cause. Then Part 1 (ruling, repairs, final Slovak file),
Part 2 (every removed layer, file and line), Part 4 (Czech stack and gold validation beside Slovak), the Czech upload
file, Gemini calls and spend, Claude tokens against the budget, judge noise, defects recorded not fixed, and a 5-line
judgement: whether judging against the source works, whether Czech meets the targets, and whether both files are fit to
upload.

## Chat output
Write NOTHING to the chat while working. At the very end, one line only: the report path.
