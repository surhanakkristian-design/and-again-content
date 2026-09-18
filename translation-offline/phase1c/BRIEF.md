# Brief: offline translation checking – Phase 1c (verbatim from Kristian, 18.9.2026)
# A COMPLETE end-to-end run on a small set, to measure what everything really costs

Repos: ~/Projects/and-again and ~/Projects/and-again-content.
Read first, and nothing else unless you need it:
docs/features/reports/TRANSLATION_OFFLINE_PHASE1B_REPORT.md (§6, §9.2, §10, Post-mortem),
~/Projects/and-again-content/translation-offline/phase1b/README.md and FORMAT_SPEC.md.

The purpose of this run is MEASUREMENT, not volume. Every step of the pipeline runs, including
the ones never run before (reviews, supplementary fixes), but on a small set. The output I want
is a per-unit cost for each step, so the size of the production run can be chosen from data.

## 0. Already built — DO NOT REBUILD
- synonyms/table.json (862 groups), the mistake library (63 topics, 1,226 items),
  FORMAT_SPEC.md, selection/sets.json, the migration SQL: reuse as is.
- measure/ blind translations and supp/translations.json: reuse. Launch NO writer agents.
- BEFORE anything else, count what exists in measure/ and supp/: how many correct translations,
  how many wrong ones, for how many distinct exercise ids. Report the counts. Use whatever
  exists that covers the 80 sentences of §2; write new translations only for sentences that
  have none, and report separately how much that cost.
- Checker v2: patch only, per §1.

## 1. Checker v2 patches (the four from Phase 1b §10.3, nothing else)
1. BrE/AmE spelling as a normal safe substitution, not only when it is the sole difference.
2. Number words in tips: "once" must not become "1".
3. "cut" multi-form anchors over-accept — restrict.
4. "her" flipping to masculine must not accept both "his" and "him".
One unit test each. Run the full suite and REPORT THE TEST COUNT (Phase 1b left it blank).
Also: `have to / have got to` stays NOT safe (the table author's reasoning is accepted; the
original brief's example was wrong) — record that in FORMAT_SPEC.md. Restore the end/finish
(verb) group lost to the id clash. Keep `safe` at ~30 groups; do not grow it.

## 2. The sentence set: 80 sentences in TWO batches of DIFFERENT SIZE
This is deliberate. One batch gives one number; two sizes let the fixed cost per batch be
separated from the variable cost per sentence:
  v = (cost60 − cost20) / 40 ;  F = cost20 − 20·v
- Batch S: 20 sentences. Batch L: 60 sentences.
- Both stratified across A1/A2/B1/B2 in the same proportion, and each containing a few of the
  30 new long (13–16 word) sentences. Do NOT make one batch all-B1 — Phase 1b measured only B1
  and that is the most expensive case, which skewed its figure upward.
- Draw them with a new seed from the existing selection sets; record exactly which ids and the
  level split. Reuse b3 sentences only where the stratification needs them.

## 3. The one design change being tested: how synonyms get annotated
Phase 1b gave the annotator an index of 832 groups and asked it to pick. It picked almost
nothing; ~30 of its 49 false rejections come from that. Invert it:
- The annotator, per content word it judges variable, writes the alternatives a learner would
  plausibly use, as FREE TEXT and short (drop → lower, reduce; spines → thorns; crop → cut).
  It does NOT search the table and does NOT see the 832-group index.
- A deterministic script maps each free-text alternative to an existing group, or records it as
  a proposed new group (`ng`). Zero model tokens for the mapping.
- Everything else in FORMAT_SPEC.md is unchanged: variants, locked spans, gender, determiners,
  optional words, library mistakes.

## 4. Run EVERY remaining step, scoped to these 80 sentences
4.1 Review of the synonym table — only the groups actually used or proposed by the 80 sentences.
    Report: groups reviewed, how many removed or changed, tokens, and TOKENS PER GROUP.
4.2 Review of the mistake library — only the topics used by the 80 sentences.
    Report: topics and items reviewed, changes, tokens, and TOKENS PER TOPIC and PER ITEM.
4.3 10 % annotation sample review: 8 sentences. Report changes, tokens, TOKENS PER SENTENCE.
4.4 Machine lint on all 80 (zero tokens). Compare the issue types against Phase 1b's 44.
4.5 Supplementary pass: apply the already-written independent translations to these 80
    sentences. Every rejection that is really correct gets fixed; state whether each fix went
    into the synonym table (preferred), an annotation, or a new variant, and COUNT BY TYPE.
    Report tokens and TOKENS PER SENTENCE.

## 5. Saturation — the number that decides how far this scales
Count how many NEW synonym groups (`ng`) the 80 sentences propose, split by batch S and batch L,
and how many of the alternatives the annotator wrote mapped to groups that ALREADY existed.
Report the ratio (new groups per 100 sentences) and, if batch L proposes proportionally fewer
than batch S, say so — that is the saturation signal. State plainly what this implies for the
second and third thousand sentences.

## 6. Measurement
On all 80 sentences, using the blind translations:
1. Coverage BEFORE the supplementary fixes, and AFTER them. Both split by level and by
   long vs short sentences. Phase 1b's comparable figure was 11/60 = 18.3 % (B1 only, before).
2. False acceptance. Phase 1b: 0 real of 63. It must stay at 0.
3. List every remaining false rejection with its cause.
4. Worst-case matching time in Node, and the per-exercise download size.

## 7. Tokens — report per UNIT, not just totals
Same unit as Phase 1b (in + cache creation + cache read + output, from transcripts), so the
comparison holds. Report:
1. cost(batch S), cost(batch L), and the derived F and v with the arithmetic shown.
2. Marginal tokens per sentence, against Phase 1b's 11,590 and Phase 1's 21,299 (derived from
   your own §9.2 raw output: batches 01–10 = 4,259,706 ÷ 200).
3. Every figure ALSO split into its four components (input, cache creation, cache read, output).
   Cache reads were 88 % of Phase 1b's total; that split matters more than the headline.
4. Per-unit costs from §4: per group, per topic, per reviewed sentence, per supplementary fix.
5. The annotation agents' startup context size and number of calls each.
6. A build-up table of the ALL-IN cost per sentence: annotation + review share + supplementary
   share + orchestration share + measurement share.
7. Extrapolation of the production run to 500, 1,000, 2,000 and 5,895 sentences, using that
   all-in figure plus the one-off full reviews still outstanding. Include the saturation effect
   from §5 if the data supports it; if it does not, say so and extrapolate linearly.
8. Total for this run, per step, against the sub-caps in §8.

## 8. Budget
Cap for this whole run: 4,000,000 tokens in the unit above. Sub-caps:
  checker patches ≤ 700 k · batch S ≤ 150 k · batch L ≤ 300 k · synonym review ≤ 400 k ·
  library review ≤ 400 k · sample review ≤ 200 k · supplementary ≤ 350 k ·
  measurement and lint ≤ 400 k · main session ≤ 800 k · report ≤ 200 k · reserve 100 k
Report each step against its cap. If a sub-cap is crossed, finish that step, note it, and
continue only if the total still fits. At 4 M stop and write the report with what exists.
Measuring a step is more valuable than finishing it perfectly — if a step must be cut short,
cut it short and report its per-unit cost from what did run.

## 9. Execution rules — this is where Phase 1b's 16.5 M went
1. Use the lean agent types tx-opus / tx-sonnet. (Do NOT fall back to general-purpose.)
2. Each batch in ONE agent, one or two calls, inputs embedded so it needs one read and one write.
3. Per-batch synonym index filtered to that batch's words (~1–2 k tokens), not the 32 KB index.
   Library index for that batch's topics only. No Phase 1 mistake input.
4. Keep the MAIN session short. Target 10 calls or fewer. The report is written by a subagent.

## 10. Report
Write docs/features/reports/TRANSLATION_OFFLINE_PHASE1C_REPORT.md (in ~/Projects/and-again):
1. Headline: coverage before/after, by level and long/short; false acceptance; F and v;
   all-in tokens per sentence; the 500/1,000/2,000/5,895 extrapolation table; unit test count.
2. Before/after table against Phase 1b for every comparable figure.
3. The §0 counts of existing blind translations.
4. The §5 saturation numbers and what they imply.
5. The per-unit cost table from §7.4.
6. Every remaining false rejection with its cause; every accepted wrong translation.
7. Whether the lean agent types loaded, and the per-call context size of each agent.
8. Judgement in 6 lines: at what number of sentences does this become affordable, is
   coverage or cost the harder problem, and what would you change next.
Do not rewrite the migration — Phase 1b's is on disk.

Nothing to the database, no app code changes, nothing deployed, no migration applied, no paid
model API. Read-only queries are fine. Commit locally in both repos. Do not push.

## Orchestration notes (main session)
- Session id: d4aa7f1b-a2b6-4747-a41a-9af6aa32ab47. Transcripts:
  ~/.claude/projects/-Users-kristiansurhanak-Meine-Ablage-And-Again/d4aa7f1b-a2b6-4747-a41a-9af6aa32ab47.jsonl (main)
  and the subagent transcripts under ~/.claude/projects/-Users-kristiansurhanak-Meine-Ablage-And-Again/d4aa7f1b-a2b6-4747-a41a-9af6aa32ab47/ (search for *.jsonl).
- Every subagent prompt starts with a tag `[STEP: <name>]` so its transcript can be attributed to a step.
  Steps: prep (= §0 counts + §1 checker patches + §2 selection + task building), batchS, batchL,
  postannot (mapping + lint + review task building), review-syn, review-lib, review-sample, supp,
  measure, report.
- Working dir for everything: ~/Projects/and-again-content/translation-offline/phase1c/ (reuse phase1b files by path; do not copy large files).
- STATE.md in phase1c/ is the handover file between agents: each agent appends a short section
  (what it did, file paths produced, numbers). Keep it terse.
