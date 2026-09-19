# Brief: offline translation checking – Phase 1W (fix the agent reader, then run the fresh set)

(Verbatim copy of the owner's brief, 19 Sept 2026. Main-session notes at the bottom.)

Repos: ~/Projects/and-again and ~/Projects/and-again-content.
Read ONLY: docs/features/reports/TRANSLATION_OFFLINE_PHASE1V_REPORT.md, phase1v/, phase1u/.
Model: gemini-3.1-flash-lite, temperature 0, thinkingBudget 0.

## 0. FIRST, before any other work: prove headless spawning works
1V made 0 model calls because headless Claude Code could not authenticate ("OAuth session expired",
`loggedIn: false`). The owner has now set CLAUDE_CODE_OAUTH_TOKEN. Verify it before building anything:
spawn ONE trivial throwaway agent that writes a single file and exits. If it fails, STOP immediately,
say so in the report title, and quote the exact error — do not build, do not improvise, do not fall
back to doing the writers' work yourself. Never print the token.

## 1. State after 1V
1V's fresh set A4 was built and self-tested but never opened. Everything else in 1V is DONE and stands:
- AG v5 `rs_nom`: 1U type M 5.66 % → 3.77 %, FA 16 → 13, measured cost 0 on both closed sets.
- TIP determiner rule: +8 judged-correct on 1U, +5 on 1T, cost 0. 1U coverage re-score 97.01 %.
- Czech reader: all four named bugs fixed, Slovak modules byte-identical.
All closed-set figures are IN-SAMPLE and are not results. The last real measurement stands: 1U coverage
95.02 % [92.42, 96.93] MET on the interval, FA 3.21 % [1.85, 5.17] two items short of settled.

## 2. BLOCKING BUG — fix this before the run
1V Track B found the AG agent reader **returns the sentence-initial token as the agent** (`Pod`, `Na`,
`V`, `Pozri`, `Ak`). On 60 real production sentences it errs on **50.0 %**; the arm-B rewrite only gets
it to 33.3 %, and only where the pronoun happens to land first. On Czech it still errs on 37.5 % after
the four bug fixes. Our test sets hid this because they are written subject-first. This is the one
thing that would corrupt the annotation of all 5,895 sentences.
2.1 Replace the first-word heuristic with a real nominative-subject reader: find the finite verb, then
    the nominative NP agreeing with it in person, number and gender, anywhere in the clause; abstain
    when nothing agrees. Reuse the clause splitter AG v4/v5 already has.
2.2 Validate on 1V Track B's 60 production sentences and the 1T 120 Czech/Slovak pairs, reporting
    agree / conservative / ERROR before and after, Czech control beside Slovak. Target: ERROR under
    10 % on raw production Slovak. Above 15 %, say so and do not freeze it.
2.3 REGRESSION GATE, mandatory: on the 1S packet keep ≥ 96/97 drops caught, 0/42 by-passive and 0/39
    plain controls rejected; on the closed 1U and 1T sets, coverage and FA must not be worse than the
    1V round-2 figures (1U 390/402 and 13/498; 1T 394/421 and 9/479). Select on MEASURED COST.

## 3. A2(a), the loop round 1V never ran
Build and measure the L3 prompt line for determiners: Slovak has no articles, so an article-only
difference is not a DIFF, and a demonstrative difference counts only where the Slovak has
ten/tá/tie/tieto. 1U leaves 6 plain-L3 determiner false rejections (C:190009, 028, 039, 059, 084, 094
:c2) the TIP rule cannot reach. Measure on the closed sets within a 200-call loop budget, same stop
rules as 1V's loop (a worse cell, a guard cost above 2, two rounds under 1 point, budget reached).
Report the round even if reverted.

## 4. The fresh set, finally opened
The tooling exists and is self-tested (`selftest_1v.py` OK): writer briefs, judge brief, assembly,
packets, label join, floors F1–F6 (including F6 ≥ 60 determiner-difference answers judged correct),
sensitivities S1–S7, seed 20260923, sids 200001–200100, 80 hidden duplicates, overlap reference of 770
sentences. Reuse it unchanged except for the stack, which is 1V round 2 plus §2 and, if it passes, §3.
Order: 4 blind writers (one per level) → 1 blind judge for all packets, shuffled across levels → floor
check on JUDGED counts → freeze and commit → preflight → `--final` ONCE → score.
Report pooled / P1 / P2 with exact Clopper-Pearson intervals and Fisher, both targets on the POINT and
the INTERVAL, every cell one per line, every figure under S1–S7.

## 5. Track B, done honestly (0 Gemini calls)
1V's cost figure is not usable: it counted **output bytes / 4 only**, excluding the annotating agent's
input and context, which have dominated every token measurement in this project; and the gold was
written by the same agent that wrote the annotation, so the agreement figure is circular.
5.1 Re-measure on 60 fresh production sentences using HARNESS token counts for the annotating agent —
    input, output and context. Report tokens per sentence for the rewrite and the annotation
    separately, and say plainly how far off 1V's 662,008-token extrapolation was.
5.2 A SEPARATE blind agent writes the gold, seeing only the Slovak sentence. Report annotation-versus-
    gold agreement as a real number.
5.3 Re-extrapolate to 5,895 with the honest figure, assumptions stated, plus a wall-clock and batch
    count.

## 6. Constraints
Gemini spend pre-approved up to $1.00; free tier first, paid fallback allowed without asking; report
actual spend. HARD CAP 1,200 model calls: §3's loop ≤ 200, §4's run ~600, §2 and §5 are 0.
Stop rules unchanged: preflight with L3-eligible 0 or a degenerate all-accepting `chk` STOPS with 0
calls; counted = (http 200) only; retry http 0/429/5xx logged as counted:false; an empty or unparsable
200 is a FAILED call, counted, never guessed, never retried; if the run crashes, recompute from stored
verdicts and say so in the title; no code change after the run starts.
Freeze and commit before opening the set; record the freeze hash AND the RUN commit; write
FINAL_RUN_DONE; publish the access log verbatim; chmod a-w earlier phase dirs BEFORE the run.
Your own tool calls: main session at most 16 — 1V's main session reached 10 of 12 before it could spawn
the five run agents, and that cap is what stopped the phase. Each agent at most 12, from the HARNESS.
Every numbered item appears in the report with its result or a plain statement that it was not done.

## 7. Report
docs/features/reports/TRANSLATION_OFFLINE_PHASE1W_REPORT.md. §4's fresh headline FIRST, then §2's
before/after error rates and its regression gate, then §3's loop round, then §5's honest cost figures
and the corrected extrapolation. Then model calls, failures, spend, own tokens and harness call counts,
and a 6-line judgement: whether FA now settles on the interval, whether the agent reader is fit for
production annotation, and what annotating 5,895 sentences really costs.

No DB writes (read-only SELECTs for §5 are fine), no app code changes, nothing deployed, no migration.

---
## Main-session notes (for sub-agents)
- §0 PASSED at main-session call 3: the desktop-bundled binary
  `~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude`
  ran `-p ... --allowedTools Write --max-turns 3 --model sonnet`, exit 0, wrote ok.txt = SPAWN_OK.
  (First attempt exit 127 only because macOS has no `timeout` command; not an auth failure.)
- The token is NOT in the non-interactive shell env. Load it per command WITHOUT printing it:
  `export CLAUDE_CODE_OAUTH_TOKEN="$(zsh -ic 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"' 2>/dev/null)"`
  Never echo it; redact `sk-ant-…` in any log you show.
- Headless sessions: use `--output-format json` so the harness usage (input_tokens,
  cache_creation_input_tokens, cache_read_input_tokens, output_tokens, num_turns, total_cost_usd)
  is captured; cap each with `--max-turns 12`. No `timeout` binary on macOS.
- Working dir for all 1W artefacts: ~/Projects/and-again-content/translation-offline/phase1w/
