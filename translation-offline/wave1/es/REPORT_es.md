# Wave 1 Spanish (es) - report part

## Status: STOPPED for good at Part B rewrite pass 1 (headless Claude weekly usage limit)

The chain was launched once (2026-09-22 12:39:08 UTC). Preflight passed 13/13 (0 real Gemini calls, 0 real headless
sessions). Rewrite pass 1 then started its three chunk sessions (c1, c2, c3; 2,049 rows), and all three returned at once
with `usage_limit`: "You've hit your weekly limit · resets 11am (Europe/Vienna)". The chain wrote `STOP_quota.md` and
`STOP_usage_limit.md` and stopped (`CHAIN_FAIL.txt`: "rewrite pass 1", 12:39:12 UTC). Under the task rules a quota or
usage-limit stop is final, so the chain was **not relaunched**.

## Headline: no measurement exists

| metric | value |
|---|---|
| coverage (pooled / per level) | not measured (Part D never started) |
| false acceptance (pooled / per level) | not measured |
| coverage >= 90 % on the point / on the interval | n/a |
| FA < 5 % on the point / on the interval | n/a |
| L3-only diagnostic, content-check catches / cost | n/a |

`partD/` is empty. The fresh set was never built, never frozen and never opened, so it is still unopened and available.

## Part A data findings (SELECT only, from `partA/partA.json`)

4,064 rows = DB count 4,064 (d and n). Per level: A1 1,174, A2 1,220, B1 885, B2 785. rows sha256
`7cd97c5779a674b951a200682d36063f13e184148ce247a608f8485cf0d3f791`. Duplicate text groups: 0. Nothing was fixed.

| finding | rows |
|---|---:|
| empty | 2,015 |
| foreign_letters | 2 |
| ellipsis_or_gap_or_trailing_comma | 1 |
| unbalanced_question_marks | 1 |

**empty (2,015 rows, no Spanish full_sentence):** A1 395 of 1,174, A2 431 of 1,220, B1 645 of 885, B2 544 of 785.
Exercise ids 32611 to 44906. So only 2,049 Spanish rows carry text, which is the row count Part B was going to rewrite.

Every other flagged row:

| finding | exercise_id | src |
|---|---:|---|
| ellipsis_or_gap_or_trailing_comma | 720 | ¿Forraste la bandeja con papel de horno, ¿verdad?? |
| unbalanced_question_marks | 10819 | ¿Estaba pasadísimo de ácido, ¿verdad? |
| foreign_letters | 20126 | Otros dos pingüinos caminan cerca del hielo. |
| foreign_letters | 20142 | Hay dos pingüinos en el hielo blanco. |

Reading: 720 and 10819 are real defects (a doubled opening mark before the tag question "¿verdad?"; 720 also ends in "??").
The two foreign_letters hits are false positives: "ü" in "pingüinos" is correct Spanish.

## Part B explicit-subject rewrite

Not produced. Pass 1 made 0 successful sessions (c1, c2, c3 all `usage_limit`, no attempts recorded), so there is no
pass 2, no final, and no `partB/partB.json`. Changed / unchanged / flagged / machine-check failures / second-pass
disagreements / pronoun counts and examples: none exist. What exists: `partB/PASS1_SUMMARY.json` (prompt sha
`2a6cf5914e854e965925f7d6960329962f4323a8b668438d7a89a3ca007eb133`), the three prompts `prompt1_c{1,2,3}.txt`
(67 kB, 53 kB, 59 kB) and the per-session headless ledgers.

## False acceptances / false rejections, judge noise

None: no writers, no judges, no items, no Gemini open.

## Gemini

0 calls (0 HTTP 200, 0 failed-but-counted), spend 0. No `GEMINI_LEDGER.json` was written.

## Claude tokens

| session | tokens | note |
|---|---:|---|
| pass1 c1#1 | 0 | usage limit, 4.0 s |
| pass1 c2#1 | 0 | usage limit, 3.5 s |
| pass1 c3#1 | 0 | usage limit, 3.5 s |
| cumulative headless (es) | 0 | from `TOKENS.md` |

Writers and judges: not started. This language agent's own use: roughly 40-60k tokens (task file, logs, Part A summary,
this report).

## Freeze and access

No freeze hash, no FREEZE_COMMIT, no RUN_COMMIT. Access log: the set was opened 0 times. Earlier commit for this language:
`5ccc39f Wave 1 es: chain stopped: rewrite pass 1` (written by the chain).

## Defects noticed, recorded, NOT fixed

1. Part A `foreign_letters` treats "ü" as foreign; it is a valid Spanish letter (güe/güi). Rows 20126 and 20142 are false
   positives.
2. Rows 720 and 10819: tag-question punctuation broken ("..., ¿verdad??" and "..., ¿verdad?" with an unmatched outer "¿").
   Only 720 is caught by the ellipsis/gap check; the outer unmatched "¿" in 720 is not flagged as unbalanced.
3. The chain launches all three pass-1 chunk sessions in parallel without a cheap quota probe first; with an exhausted
   weekly limit it fails fast (0 tokens), so no harm this time, but a probe before Part B would give the clearer stop.
4. 2,015 of 4,064 selected exercises (49.6 %) have no Spanish sentence at all; B1 (73 %) and B2 (69 %) are the worst.

## To resume

After the weekly limit resets (11am Europe/Vienna), the main session can remove the STOP files and relaunch the chain;
pass 1 has no finished sessions, so it restarts from zero Part B cost. The fresh set is untouched.
