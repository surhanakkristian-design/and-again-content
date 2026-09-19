# Phase 1U §1.1 — where the owner's ruling landed

The ruling block is byte-identical in all four places (the three stack/spec documents plus the
stand-alone copy). Source of truth: `phase1u/RULING_ARTICLE.txt`.

## 1. Judge brief
- **File:** `phase1u/set/judge/JUDGE_BRIEF_1U.md`
- **Section:** "The owner's rules, verbatim" — heading `### OWNER'S RULING ON ARTICLES (Phase 1U)`,
  placed **immediately after the OMISSION RULE (M1/M2/M3) paragraph** and before the AGENT RULE.
- **1T text changed:** the 1T brief's OMISSION RULE read `"M1, a dropped FUNCTION word or particle
  (just, already, an article, optional "that") — CORRECT…"`. In the 1U copy the list reads
  `(just, already, optional "that")` — **`an article` removed**. A parenthetical note directly under
  the ruling records the removal and points the judge to the ruling.
- **Also changed (not the ruling):** verdict fields renamed/added to the mandated set — `id`,
  `label` (was `jid`/`judged`), `type`, `borderline`, `confidence` 1–5 **mandatory on every item**,
  `dropped` as in 1T, optional `note`; `passive` and `agent_drop` kept, `agent_drop` now takes
  `fronted`/`other` instead of 1T's `embedded`; `tip` dropped. Packet format changed to
  `packet_partK.jsonl` + `verdicts_partK.json` + `JUDGE_TASK_1U.md`. The agent rule's
  "applies to EVERY clause" sentence is kept and extended with the locative/instrument `by`-phrase
  clarification.

## 2. Writer spec
- **File:** `phase1u/set/WRITER_SPEC_1U.md`
- **Section:** "The owner's rules (verbatim)" — heading `## OWNER'S RULING ON ARTICLES (Phase 1U)`,
  directly after the AGENT RULE paragraph, followed by one consequence line ("a `missing-article`
  answer is a WRONG answer of type S").
- **1T text changed:** same M1 list — `an article` removed, with an italic note under the OMISSION
  RULE pointing at the ruling. The 1T spec's `w5 type S: a small slip … missing obligatory article,
  meaning intact` is replaced by the 1U `w4` rule that makes a missing obligatory article an
  explicitly WRONG, separately tagged item.
- **Also changed (not the ruling):** 29 sentences s01–s29 in four kinds FR/MC/MN/SKP (1T had
  25 in ACT/SKP/EMB), the new answer layout (w1+w2 agent drops, w3 time-frame, w4 slip, w5 wrong
  word), the new tag vocabulary (`drop-fronted` / `drop-misaligned` / `drop-main` / `drop-other` /
  `missing-article` …), `intent` + `type` + `tags` on every answer, two output files instead of
  three. Arm-B explicit subjects, the annotation schema and the "wrong for exactly one reason" rule
  are carried over unchanged from 1T.

## 3. L3 prompt
- **File:** `phase1u/stack/L3_PROMPT_1U.txt` (prompt id `P-FROZEN-1U`), diff in
  `phase1u/stack/L3_PROMPT_DIFF.md`.
- **Where:** the ruling is rendered as **one added prompt line, `ARTICLE_LINE_1U`**, appended to the
  end of `ins` in `build_req_1p` — i.e. after `VOICE_SAME_LINE` and after the lever 2 / lever 3
  lines, immediately before the frozen tail `SAME, TIP or DIFF?`. It stands **after** lever 2's
  `DEF_LINE` on purpose, so that it qualifies "…chooses a different article is SAME on that point"
  whenever that line fires. The ruling block itself is reproduced verbatim at the foot of
  `L3_PROMPT_1U.txt` as the authority for that line.
- **Output vocabulary unchanged:** the line says a required-but-absent article is **DIFF** — the
  existing rejection verdict. No new token, no change to the system text, the P-B body, the tail or
  `GEN_CFG`.
- **1T text changed:** nothing was deleted from the prompt; the change is purely additive (the M1
  wording never appears in the prompt — lever 2's `DEF_LINE` is the only article statement and it is
  now qualified rather than edited).

## 4. Stand-alone copy
- `phase1u/RULING_ARTICLE.txt` — the ruling block and the orchestrator clarification alone.

## Files read outside `phase1t/`
Nothing outside `phase1t/` was read except the following, all needed to locate the L3 prompt text:

| file | why |
|---|---|
| `translation-offline/phase1p/runner_1p.py` (lines 40–120) | holds `PROMPT_1P` and `build_req_1p`, the assembler and the insertion point |
| `translation-offline/phase1n/runner_1n.py` (grep, lines 78–82) | `VOICE_SAME_LINE`, first element of the inserted block |
| `translation-offline/phase1k/runner_1k.py` (lines 30–120) | `build_req` head/extra/tail layout and the `P-FROZEN` body assembly |
| `translation-offline/phase1i/pipeline_1i.py` (grep, lines 40–51 and 154–193) | `GENDER_TMPL`, `GROUND_LINE`, `WORDING_LINE`, `pb_lines()`, `sys_text()` |
| `translation-offline/phase1p/lever2.py` (whole file) | `DEF_LINE` / `ASPECT_TMPL` / `NUMBER_TMPL` — the article statement the ruling has to qualify |
| `translation-offline/phase1p/lever3.py` (head) | `ALT_TMPL`, the last lever line before the insertion point |
| directory listings of `translation-offline/` via grep/find | locating the above |

**Not read** (budget): the checker / `lib_prev` module holding the frozen `P-B` body and `SYS`. Both
are carried as named placeholders `{{PB_HEAD_LINES}}` and `{{SYS}}`; the 1U change does not depend on
their content, and `L3_PROMPT_DIFF.md` §"How the 1U runner must load the new text" item 4 requires
the tooling agent to assert against a really built request before the run.

The Phase 1T report `~/Projects/and-again/docs/features/reports/TRANSLATION_OFFLINE_PHASE1T_REPORT.md`
was **not** read (budget); the rule conflict it records is restated in the task brief and is settled
by the ruling above.

No model calls, no git operations, no DB access. Nothing was written outside `phase1u/`.
