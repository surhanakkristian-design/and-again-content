# Phase 2J — orchestration file (owner's brief verbatim in §B, stage plan in §S)

All paths absolute. ROOT = /Users/kristiansurhanak/Projects/and-again-content/translation-offline
P2J = ROOT/phase2j   P2I = ROOT/phase2i   P1W = ROOT/phase1w
Report: /Users/kristiansurhanak/Projects/and-again/docs/features/reports/TRANSLATION_PRODUCTION_PHASE2J_REPORT.md
(commit it in the and-again repo, copy to P2J/; content repo commits for everything under P2J). Never push.

## §R Common rules for every stage agent
- Read ONLY this file, P2J/PROGRESS.md, P2J files of earlier stages, and the allowed sources: P2I/TRANSLATION_PRODUCTION_PHASE2I_REPORT.md,
  P2I/ (CONTEXT.md is the technical map — use it instead of re-reading the chain), ROOT/phase1w/TRANSLATION_OFFLINE_PHASE1W_REPORT.md
  (or wherever the 1W report lives under ROOT; find it with one `find`), P1W/. The chain modules that P2I/CONTEXT.md §1.1 names may be read
  as needed for the code path in question (they are the 2I stack's code).
- Nothing written to the database (SELECT only). No deploy, migration, push, rebase. Write only under P2J (plus the report file).
- Earlier phase directories stay byte-identical: stage 1 writes P2J/SHA_before.txt with P2I/sha_tree.sh (same generator, all phase*/
  except phase2j); every stage ends by re-running it and diffing (must be empty; phase1p dirty pair is part of the baseline).
- Run python with `python3 -B` / PYTHONDONTWRITEBYTECODE=1; copy chain modules into P2J, never run in place; use P2I/write_guard.py pattern.
- Absolute paths in every invocation. Long jobs under `nohup` (never setsid). Commit every file immediately (git -C ~/Projects/and-again-content).
- Test first: no model call (Gemini or headless Claude) before P2J/test_2j.py passes over the real code path with the model mocked, including:
  a row/item number containing "429" (not a rate limit), a real 429 envelope (retried), a usage-limit envelope (hard STOP), resume at 0 cost,
  a relative-path invocation (must work or be rejected cleanly, never crash mid-run), and one test per fix (A2, C2 if built, B3 filters).
  If a test cannot pass: STOP at 0 cost, write P2J/STOP_<stage>.md.
- Gemini: L3 = gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, TIP-as-rejection ON (2I transport: counted = HTTP 200 only; rate limit
  only from status/error envelope, never output text). HARD CAP 1,200 counted calls for the whole phase (A3 + B4 + D); spend cap $1.00.
  Keep a phase ledger P2J/GEMINI_LEDGER.json {stage: counted} and check it before any call.
- Headless Claude: 2H/2I recipe (P2I/CONTEXT.md §2; token via `zsh -ic`, never printed; --output-format json; usage from envelope).
  Usage-limit/quota error in any headless session -> STOP at once, write P2J/STOP_usage_limit.md; orchestrator then writes the report.
  If headless spawning fails -> STOP at 0 cost.
- Tool calls: at most 12 per agent (you). Batch work into scripts. Tokens: append to P2J/TOKENS.jsonl {stage, headless_tokens, agent_est}.
- At the end of your stage append a section to P2J/PROGRESS.md: what was built, numbers, files, Gemini calls (stage + cumulative), headless
  tokens, SHA check result, and anything the next stage must know. Reply to the orchestrator in <= 15 lines.

## §S Stage plan (order A -> C -> B -> D)
S1  Setup + Part A deterministic: SHA_before; copy 2I TRANSLATION-ONLY stack into P2J (stack_tonly + tonly/ + adapter + write_guard);
    A1 diagnosis of the 24 F4v2 FRs (sids 250,1038,1214,2461,2989; checker_1i.py:608, decide 815-820) naming the code path;
    A2 deterministic fix of the cause (not a broader abstain), catches vs cost separately (incl. the 20 judge-WRONG F4v2-rejected items);
    A3 deterministic part: re-score closed 2I set at 0 calls using 2I's stored L3 replies (P2I/run/ledger/results, by request hash); list
    items that newly reach L3 with NO stored reply; A4 regression gate on the 1W test set and the 1S packet (deterministic where stored replies
    exist; list any item needing a new call); A5 Czech reader check (+ fix if same defect).
S2  Runner + tests + freeze: P2J/run_2j.py (Gemini L3 transport from 2I, cap/ledger; headless Claude spawner from 2H) + P2J/test_2j.py (§R list);
    freeze (FROZEN_SHA.txt, FREEZE_COMMIT.txt); then make ONLY the A3/A4 calls that newly reach L3; finish A3 before/after table + A4 verdict.
S3  Part C: C1 per-item why F5 did not fire (15 FAs), C2 size + build only if deterministic and 0 measurable cost on closed 2I + 1W sets,
    C3 A2-level FA 8.00 % [3.52, 15.16] drivers. If C2 built, extend test_2j and re-freeze.
S4  Part B1 deterministic reference audit (sk + cz upload files, reader_nom person/number/gender vs reference subject pronoun) +
    B2 model audit of every SLOVAK reference (judge sees only the Slovak + its references; classes faithful / adds content / narrows a word /
    wrong person or gender / other, with span; N=100 per session, waves of 4 parallel sessions, one prompt, fixed sha; Czech sized only).
    BUDGET GUARD: before launching, measure the first wave and project; the whole-phase Claude budget is 4,000,000 tokens and D needs
    ~700k headless + ~400k orchestration reserved. If the full audit does not fit, audit as many complete waves as fit, record exactly which
    rows were audited, and say so; D then samples only from audited rows.
S5  B3 corrections (only flagged; remove added content, add broader word as a further variant, add the other gender where the Slovak leaves it
    open; 1P lever-3 tense filter; never enrich faithful refs) -> P2J/upload/ corrected sk (+ cz where B1 flags apply deterministically);
    B4 closed 2I set re-score with A+B(+C) — only new L3 calls.
S6  Part D set + 4 blind writers (one per level) from the CORRECTED sk upload, excluding the 60 2F-probe and the 100 2I sentences.
S7  Part D judge: ONE prompt, 4 sessions, shuffled across levels, 80 hidden duplicates across sessions, owner's rules verbatim,
    practised structure out of scope (reuse P2I/judge pattern).
S8  Part D run: freeze + commit before opening; FREEZE hash + RUN commit; opened ONCE; FINAL_RUN_DONE; access log verbatim.
S9  Analysis + report (§B "Report") + SHA after + tokens.

## §B The owner's brief (verbatim)

Work in ~/Projects/and-again-content/translation-offline/phase2j/.
Read ONLY, once at the start: TRANSLATION_PRODUCTION_PHASE2I_REPORT.md, phase2i/ (stacks, runner, tests, set,
run, analysis, upload/), TRANSLATION_OFFLINE_PHASE1W_REPORT.md, phase1w/.

### 0. Rules
The checker answers ONE question — is this correct English that means what the Slovak means. The owner removed the
structure check in 2I and it stays removed. Start from 2I's TRANSLATION-ONLY stack.
Nothing is written to the DATABASE — SELECT only. No deploy, no migration, no push, no rebase. Earlier phase
directories stay byte-identical; verify SHA-256 before and after. Write only under phase2j/. Commit every file
immediately. Run under `nohup`, never `setsid`. **Use absolute paths everywhere** — 2I's first set open crashed on
a relative `--run-dir`.
Test first, as 2H and 2I proved works: a suite over the real code path, model mocked, must pass before any model
call — including a row number containing "429", a real 429 envelope, a usage-limit envelope, resume at 0 cost, a
relative-path invocation, and every fix below. If a test cannot pass, STOP at 0 cost.

### PART A — the F4v2 subject-guard misfire (24 of 54 false rejections, 44 %)
2I: F4v2 rejected EVERY correct answer of 5 sentences (sids 250, 1038, 1214, 2461, 2989), including near-verbatim
copies of the reference, although each answer's subject agrees with the Slovak ("He said …" for "Povedal …").
A1 Diagnose from those 24 items what F4v2 misreads — reported speech, a multi-clause sentence, the subject of the
   wrong clause — and name the code path (2I cites checker_1i.py:608, decide 815–820).
A2 Fix the cause, deterministically. Do not merely make F4v2 abstain more: 2I notes 20 judge-WRONG items are also
   F4v2-rejected today, so an over-broad abstain moves them to L3 and raises FA. Report catches and cost separately.
A3 Re-score the CLOSED 2I set. Deterministic layers at 0 calls; any item that newly reaches L3 needs one call —
   make only those. Report coverage and FA before and after, and every item whose verdict changed. Label it a
   closed-set re-score.
A4 Regression gate: on the 1W test set and the 1S packet, coverage and FA must not get worse.
A5 Apply the same fix to the Czech reader if the Czech path has the same defect; say whether it does.

### PART B — the references (16 of 54 false rejections, 30 %)
2I: references that fix a gender the Slovak leaves open, invent content ("her brother"), or narrow a word ("fetch"
for *nosila*, which rejects the correct "carry").
B1 DETERMINISTIC audit, 0 model calls, on BOTH upload files (`phase2i/upload/`, sk 4,064 and cz 4,064): compare each
   reference's subject pronoun with the source's person, number and gender from `reader_nom`. Flag every mismatch.
   Report counts per language and 10 examples each.
B2 MODEL audit of every SLOVAK reference: a judge sees ONLY the Slovak sentence and its stored English references,
   never an answer or a label, and classifies each reference as faithful / adds content / narrows a word / wrong
   person or gender / other, with the span. N = 100 per session, 4 sessions in parallel, one prompt with a fixed sha.
   Czech is sized, not run.
B3 CORRECT only what is flagged: remove added content, add the broader word as a further variant, add the other
   gender where the Slovak leaves it open. Apply the tense filter from 1P lever 3 — no variant may change the time
   frame. Do NOT enrich faithful references: 2G proved blanket enrichment made coverage worse (84.62 → 81.87 %) and
   doubled TIP rejections. Report how many references changed and write corrected upload files under
   `phase2j/upload/`.
B4 Re-score the CLOSED 2I set with A and B together; report the combined effect.

### PART C — the false acceptances (15 of 19 are a dropped content word accepted by L3)
The owner's rule: a dropped content word is WRONG. F5 is meant to catch it but decided only 4 items in 2I. The
likely reason: F5 works on subsequences of the English reference, and production references are thin, so F5 rarely
matches and the item goes to L3, which accepts it.
C1 For each of the 15, show why F5 did not fire. C2 Size a deterministic fix — for instance comparing against the
Slovak's content words rather than the English reference — and BUILD it only if it is deterministic and costs
nothing measurable on the closed 2I set and the 1W set. Report catches and cost separately.
C3 Also look at A2's FA of 8.00 % [3.52, 15.16], the highest of any level, and say what drives it.

### PART D — measure on FRESH production Slovak
The same method as 2I, which worked cleanly: 100 NEW Slovak sentences from the CORRECTED upload file, 25 per level,
excluding the 60 of the 2F probe and the 100 of 2I; 5 correct + 4 wrong each (500 / 400); 4 blind writers one per
level; ONE judge prompt across 4 sessions, items shuffled across levels, 80 hidden duplicates placed in different
sessions; the owner's rules verbatim with the practised structure out of scope.
Run ONE stack — the fixed TRANSLATION-ONLY. L3 gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, TIP-as-rejection
ON. Freeze and commit before opening; record the freeze hash and RUN commit; FINAL_RUN_DONE; access log verbatim.
Opened ONCE. Gemini transport: counted = HTTP 200 only; rate limit detected ONLY from the status or error envelope,
never from output text; HARD CAP 1,200 calls (A3 and B4 included); spend pre-approved to $1.00.
Report: coverage and FA pooled and per level with exact 95 % CP, beside 2I (89.13 % / 4.71 %), both targets on the
point and the interval; then every false rejection and false acceptance with the same cause list as 2I.

### Constraints
Claude token budget: **4,000,000** from the harness. Print the plan before spending; after every stage print
cumulative tokens and the projection; STOP rather than exceed. Stage order is A → C → B → D, so the cheap
deterministic fixes land even if the budget runs short.
**If a headless session fails with a Claude usage-limit or quota error, STOP at once and write the report.**
Your own tool calls: main session at most 24 with 4 in reserve; each agent at most 12, from the HARNESS.
Load the OAuth token as 2I did (`zsh -ic`); never print it. If headless spawning fails, STOP at 0 cost.

### Report
`docs/features/reports/TRANSLATION_PRODUCTION_PHASE2J_REPORT.md`. FIRST: Part D's headline beside 2I, both targets
on the point and the interval, per level. Then the false-rejection and false-acceptance cause tables beside 2I's.
Then Part A (diagnosis, fix, closed-set effect, regression gate, Czech), Part C, Part B (audit counts per class,
references changed), the corrected upload files, Gemini calls and spend, Claude tokens against the budget, judge
noise, defects recorded not fixed, and a 6-line judgement: whether production now meets 90 % and 5 %, what each fix
recovered, and what is left.

### Chat output
Write NOTHING to the chat while working. At the very end, one line only: the report path.
