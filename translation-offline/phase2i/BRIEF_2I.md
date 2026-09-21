# Brief: Phase 2I — measure PRODUCTION Slovak with a translation-only checker, and break down every error

(Verbatim brief from the owner, 21 Sept 2026. Stage agents: read this whole file; your own stage is given in your task prompt.)

Work in ~/Projects/and-again-content/translation-offline/phase2i/.
Read ONLY, once at the start: TRANSLATION_PRODUCTION_PHASE2F_REPORT.md, TRANSLATION_PRODUCTION_PHASE2G_REPORT.md,
TRANSLATION_PRODUCTION_PHASE2H_REPORT.md, TRANSLATION_OFFLINE_PHASE1W_REPORT.md, TRANSLATION_OFFLINE_PHASE1U_REPORT.md,
TRANSLATION_OFFLINE_PHASE1S_REPORT.md (§4, §5), phase1w/ (frozen stack and runner), phase2f/p3/probe/,
phase2d/out/annotations_sk_final.jsonl, phase2h/out/.
(Reports live in ~/Projects/and-again/docs/features/reports/.)

## 0. THE OWNER'S DECISION — this changes the checker
The checker no longer checks whether the answer uses the grammar the exercise practises, and gives no tip about
it. The owner's words: whether the translated sentence matches the exercise is unnecessary; if it causes errors
the learner simply gets no tips; **the one thing that matters is whether the sentence is correctly translated,
with a high success rate.**
So the checker now answers one question: **is this correct English that means what the Slovak means?**
Build a TRANSLATION-ONLY stack from the frozen 1W stack by removing, and nothing else:
- the L2 structure lock and every tip generated from it (LOCKTIP);
- F2B, which reads the lock span;
- every read of `lk` anywhere in the verdict path;
- any line in the L3 prompt that states which grammar is practised, and **especially any line telling the model
  the practised grammar is already verified** — since 1k nothing verifies it, so such a line would tell the model
  to skip a check nobody performs. Quote the exact line if it exists.
KEEP, unchanged, everything that decides whether the translation is correct: the Slovak-anchored time frame (a
time frame that differs from the Slovak is WRONG; the English tense inside that frame is free), AG and the agent
ruling, F3, F5, F4v2, the article rules, the L3 model, TIP-as-rejection ON.
Name every file and line you remove or change. **Nothing else is tuned.** If you find a defect, RECORD it.
Nothing is written to the DATABASE — SELECT only. No deploy, no migration, no push, no rebase. Earlier phase
directories stay byte-identical; verify SHA-256 before and after. Write only under phase2i/. Commit every file
immediately. Run under `nohup`, never `setsid`.

## PART 0 — make both upload files clean (0 model calls)
Write corrected copies under `phase2i/upload/`, never touching the originals:
- 2H found **50 Czech rows with an empty `v`** (from n 5365), so the model has no reference for them. Set
  `v = [en]` for every row where `v` is empty, in BOTH languages; list the n values.
- 2H found **`exercise_id` stored as text** in the xlsx. Write it as an integer in both files.
- `lk` stays in `structure_json` but is now UNUSED; say so in `UPLOAD_README.md`.
- Assert both files round-trip, row counts 4,064 and 4,064, and `v[0] == en` on every row.

## 1. The set — production as it is
- **100 Slovak sentences from `phase2d/out/annotations_sk_final.jsonl`**, 25 per level, deterministic seed,
  **excluding the 60 sentences of the 2F probe** and anything used in any test set. Annotation used exactly as
  stored, except the Part 0 `v` fix.
- **5 correct and 4 wrong answers per sentence: 500 correct, 400 wrong.** Correct answers are weighted up because
  the false rejections are what this phase exists to categorise.
- Wrong answers balanced across T / W / M / S. **No agent-drop floor**; production has few named agents. Report
  the natural counts.
- **4 blind writers, one per level**, seeing ONLY the Slovak sentence, its level and its topic.

## 2. The judge — one rule set, bounded cost
2F's single judge session burned 1,547,186 tokens and died. So: **ONE judge prompt, byte-identical across 4
sessions**, ~245 items each, **shuffled across all four levels**; assert the prompt sha is identical. **80 hidden
duplicate controls placed in DIFFERENT sessions** from their originals. Packets carry
`jid / slovak / level / answer / topic`. Cap each session at 400,000 tokens; STOP rather than exceed.
The judge gets the owner's rules VERBATIM, with the practised structure explicitly OUT of scope: the Slovak is the
ground truth, not the English reference; any correct English with the same meaning is correct regardless of the
grammar structure used; a passive is acceptable; a passive that drops an agent the Slovak names is WRONG; a missing
obligatory English article is an ERROR while the CHOICE of article is free; the time frame must match the Slovak
while the English tense inside it is free; a dropped function word is correct, a dropped content word is wrong,
added content is wrong.

## 3. The run — two stacks on the same items
Run BOTH on every item: **TRANSLATION-ONLY (the headline, what ships)** and **FROZEN 1W (the comparison)**.
L3 **gemini-3.1-flash-lite, temperature 0, thinkingBudget 0**. Do not use the 2D–2H annotation runners.
Test first, as 2H proved works: before any model call, a suite over the real code path with the model mocked must
pass — a row number containing "429", a genuine 429 envelope, a usage-limit envelope, resume at 0 cost, and a test
asserting TRANSLATION-ONLY reads `lk` nowhere. If a test fails, fix and re-run; if it cannot pass, STOP at 0 cost.
Freeze and commit both stacks before opening the set; record the freeze hash AND the RUN commit; write
FINAL_RUN_DONE; publish the access log verbatim. The set is opened ONCE.
Gemini transport: counted = HTTP 200 only; a rate limit is detected ONLY from the HTTP status or the API error
envelope, **never from a substring of the output**. Retry http 0/429/5xx with backoff, logged counted:false; an
empty or unparsable 200 is a FAILED call, never guessed, never silently retried. HARD CAP 2,000 calls; spend
pre-approved to $1.00.

## 4. What to report
4.1 Headline: coverage and FA for TRANSLATION-ONLY, pooled and per level, each k/n with exact 95 % Clopper-Pearson
    intervals — beside FROZEN on the same items, 1W's test figures (97.76 % / 3.21 %) and 2F's probe
    (84.62 % / 6.18 %). Both targets (coverage ≥ 90 %, FA < 5 %) on the point and on the interval.
4.2 **The effect of the owner's decision**: every item whose verdict differs between the two stacks, listed, with
    which removed component caused it. Separately: correct answers newly ACCEPTED, and wrong answers newly
    ACCEPTED. The second number is the cost; state it plainly.
4.3 **EVERY false rejection of TRANSLATION-ONLY, item by item**: sid, level, the Slovak, every stored English
    reference, the answer, the rejecting layer (L1 / AG / F3 / F4v2 / F5 / L3 / L3:TIPrej), the L3 reply, and ONE
    cause: determiner or article CHOICE · dropped FUNCTION word (M1) · synonym or different word · structural
    paraphrase · English tense within the Slovak's frame · voice or passive · word order · AG misfire · reference
    wrong or too narrow · judge label doubtful · other. Extend only if nothing fits, and say why.
4.4 Tables: count per cause, per layer, cause by layer, and cause by level.
4.5 Compare with the test sets: 1U's 20 false rejections were 12 determiner; by layer AG 1, L3 7, L3:TIPrej 12.
    Say which causes are NEW to production and which are the same at a higher rate.
4.6 For each cause: reachable by (a) an offline rule, (b) the L3 prompt, (c) the annotation or reference, or
    (d) not at all — with an estimated number of items each would recover. Build nothing.
4.7 **M1**: 1S §5 found F5 never sees the Slovak and its only free class is NONINFO, so dropping *also*, *then* or
    *finally* is rejected as a content word, against the owner's rule. Count exactly how many false rejections are
    this.
4.8 Every FALSE ACCEPTANCE of TRANSLATION-ONLY, item by item, with its cause.
4.9 The 28 false rejections of the 2F probe, categorised with the same list from its stored files at 0 calls.

## 5. Constraints
Claude token budget: **3,000,000** from the harness. Print the plan before spending; after every stage print
cumulative tokens and the projection; STOP rather than exceed.
**If a headless session fails with a Claude usage-limit or quota error, STOP at once and write the report.**
Your own tool calls: main session at most 24 with 4 in reserve; each agent at most 12, from the HARNESS.
Load the OAuth token as 2H did (`zsh -ic`); never print it. If headless spawning fails, STOP at 0 cost.

## 6. Report
`docs/features/reports/TRANSLATION_PRODUCTION_PHASE2I_REPORT.md` (in ~/Projects/and-again). FIRST: the
TRANSLATION-ONLY headline beside FROZEN, 1W and 2F. Then 4.2 (what the decision changed, with its cost). Then the
cause tables, the comparison with the test sets, reachability with estimated recoveries, the M1 count, false
acceptances by cause, the 2F probe's 28, and every false rejection and false acceptance one per row. Then Part 0's
corrections, every removed file and line, Gemini calls and spend, Claude tokens against the budget, judge noise
across sessions, defects recorded not fixed, and a 6-line judgement: what production coverage really is with the
translation-only checker, what removing the structure check cost and gained, which causes dominate, and what
single change would recover the most.

## Rules for every stage agent (from the orchestrator)
- At most 12 tool calls of your own. Batch work into scripts; one Bash call can do a lot.
- Write only under phase2i/ (except the final report stage, which writes the report in ~/Projects/and-again).
  `git add` + `git commit` each file you create in the content repo (~/Projects/and-again-content) right away
  (no push, no rebase). Commit message prefix "Phase 2I:".
- Log your stage's Claude token use (headless sessions: from their JSON usage) to phase2i/TOKENS.jsonl, one line
  per session/stage, and append a stage note to phase2i/PROGRESS.md (what you did, files, cumulative tokens,
  projection vs 3,000,000).
- If something makes the stage impossible, write phase2i/STOP_<stage>.md with the reason and return.
- Return to the orchestrator a SHORT summary (≤ 15 lines): status, key numbers, files. No narration.
