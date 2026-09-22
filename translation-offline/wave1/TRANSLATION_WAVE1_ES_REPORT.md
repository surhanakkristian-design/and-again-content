# Translation Wave 1: Spanish (es) -> English, re-measured with the packet-level judge fix (report, 22 Sept 2026)

Pipeline: `~/Projects/and-again-content/translation-offline/wave1/` (below `W1/`). App branch: `translation-wave1`, in the worktree `~/Projects/and-again-wave1-wt`. de and ua were not touched (`W1/de/`, `W1/ua/` unchanged).

## 1. Result first

| target | point | 95 % CP interval |
|---|---|---|
| coverage >= 90 %: 453/490 = **92.45 %** [89.74, 94.63] | **MET** | missed (lower bound 89.74) |
| FA < 5 %: 12/410 = **2.93 %** [1.52, 5.06] | **MET** | missed (upper bound 5.06) |

**Spanish meets both targets on the point, so it is routed** on the branch (Part F, section 6). On the interval, both targets are missed, each by a small margin.

Per level (exact Clopper-Pearson 95 %), plus the L3-only diagnostic (the decision before the content check):

| block | coverage, CP 95 % | >= 90 %: point / interval | FA, CP 95 % | < 5 %: point / interval |
|---|---|---|---|---|
| **pooled** | 453/490 = 92.45 % [89.74, 94.63] | MET / missed | 12/410 = 2.93 % [1.52, 5.06] | MET / missed |
| A1 | 105/118 = 88.98 % [81.90, 94.00] | **missed** / missed | 4/107 = 3.74 % [1.03, 9.30] | MET / missed |
| A2 | 115/122 = 94.26 % [88.54, 97.66] | MET / missed | 4/103 = 3.88 % [1.07, 9.65] | MET / missed |
| B1 | 118/124 = 95.16 % [89.77, 98.20] | MET / missed | 4/101 = 3.96 % [1.09, 9.83] | MET / missed |
| B2 | 115/126 = 91.27 % [84.92, 95.56] | MET / missed | 0/99 = 0.00 % [0.00, 3.66] | MET / MET |
| L3 only, pooled | 469/490 = 95.71 % [93.52, 97.33] | MET / MET | 30/410 = 7.32 % [4.99, 10.28] | missed / missed |
| L3 only, A1 | 110/118 = 93.22 % [87.08, 97.03] | | 6/107 = 5.61 % [2.09, 11.81] | |
| L3 only, A2 | 119/122 = 97.54 % [92.98, 99.49] | | 6/103 = 5.83 % [2.17, 12.25] | |
| L3 only, B1 | 120/124 = 96.77 % [91.95, 99.11] | | 9/101 = 8.91 % [4.16, 16.24] | |
| L3 only, B2 | 120/126 = 95.24 % [89.92, 98.23] | | 9/99 = 9.09 % [4.24, 16.56] | |

- **Per-level miss:** A1 coverage is 88.98 %, below 90 % on the point. Four of its 13 false rejections are a single sentence (24801, "Mira la luna con el telescopio"; see section 3).
- **What the content check did:** it caught 18 false acceptances (30 -> 12) at a cost of 16 correct answers (469 -> 453). Without it, FA is 7.32 %, above the 5 % target.
- **For comparison, de and ua** (frozen, not re-run): coverage 94.40 % and 94.56 %, FA 3.25 % and 2.72 %. es has lower coverage and a similar FA.

## 2. What was run

1. **Owner decisions 31-33** were appended to `translation-offline/upload_skcz/OWNER_DECISIONS_2L.md` and committed (4689148) before any other step.
2. **Judge prompt (es only).** Decisions 32 and 33 were added to the es JUDGE prompt only (`prompts_w1.py`, `JUDGE_D3233 = {'es'}`):
   - decision 32: *"Grammatical gender decides: a grammatically masculine Spanish noun (e.g. "el atleta") is "he"; "she" is wrong. The genderless rule above covers only sentences that mark no gender at all."*
   - decision 33: the rule *"Added content is wrong."* gained the exception for an ADDED interjection ("Wow", "Bro").
   - **Unchanged:** the de and ua judge prompts and every checker prompt (L3 and content check, all three languages) are byte-identical. `spec/judge_prompt_es.txt` is the only spec file that changed.
   - **Check:** `gen_prompts_ts.py` regenerates the TS checker prompts with identical texts; only the recorded source sha of `prompts_w1.py` changed.
3. **The old es judging was discarded.** It consisted of 4 packets and 7 sessions (s1, s2, s3, s3_r1, s4, s4_r1, s4_r2), all run with the prompt from before decisions 32 and 33.
   - The judge directory was archived to `W1/es/partD/_judge_4packets_20260922/`, and the stop files to `W1/es/_stop_20260922/`.
   - Their 373,446 tokens stay counted in the language ledger.
   - The es writers were reused at 0 cost: 900 answers (500 correct + 400 wrong, T/W/M/S = 100 each). The set was the same unopened set.
4. **The packet fix (decision 31)**, in `pipeline_w1.py` (`packets8`, `judge_rows`, `judges8`; de and ua keep the 4-packet path):
   - **8 packets from one seeded shuffle.** The originals were split i % 8, so every packet has all four levels mixed. Packets s1-s4 hold 113 originals + 10 controls = 123 items; packets s5-s8 hold 112 + 10 = 122.
   - **80 hidden duplicates**, each in a different packet from its original. Each (packet, level) pair gets 3 or 2 duplicates, alternating. They split 20 per level and 40 writer-correct / 40 writer-wrong. The target packet is (s + {A1 1, A2 3, B1 5, B2 7}) mod 8.
   - **One judge prompt** for every session. Each packet carries jid / source / level / answer / topic only.
   - **The jid set is checked after every session.** A row counts only if its jid was asked, its label is correct or wrong, and its reason is a string. A jid returned twice counts as MISSING, and invented jids are ignored.
   - **Follow-up for missing jids.** If any jid is missing, a follow-up session `sN_f1` (then `sN_f2`) judges the MISSING jids only, in packet order, with the same prompt, and the results are merged. The cap is 2 follow-ups per packet; after that the chain STOPs. There are no whole-packet retries.
   - **Every session was an Opus subagent** (`tx-opus`, model opus; decision 26). No headless CLI was used.
   - **Tests.** `test_w1` is now 15/15 with the new t15 (8 packets, 80 cross-packet controls, 40/40, follow-up merge, STOP after 2 follow-ups, same prompt). t01 checks that d32/d33 exist only in the es judge prompt. The mock PASSed and exercised one follow-up (s1 -> s1_f1, 1 item).
5. **Freeze and open.**
   - The freeze covered FROZEN_SHA_D (common/*.py, common/*.sh, spec/*.txt, partA_live/rows.jsonl, items.jsonl, truth.jsonl), with freeze hash `e0cef9d4…`, FREEZE_COMMIT c20e2e4 and RUN_COMMIT 0d4c36f.
   - The clean-tree check passed, and `shasum -c` found 0 non-OK lines.
   - The es set was opened **ONCE**: `run/access_log.jsonl` has 1 entry, items.jsonl sha `118f140d…`.
   - The frozen stack ran in this order: L3 SOURCE-ONLY on gemini-3.1-flash-lite, where TIP, DIFF and unparsable replies are rejected; then the content check, where NONE accepts and MISSING rejects. There was no F4 and no AG.
   - The run took 1,752 s. All es commits are on the content repo's main, and only paths under `W1/common`, `W1/spec` and `W1/es` were committed.

## 3. False acceptances and false rejections by cause

**FA 12. All come through L3 SAME + content check NONE:**
- 4 × M (dropped content, missed by both layers):
  - antigua (ancient);
  - gigante (giant);
  - de la prisión (from the prison);
  - the noun "las flores", replaced by "They".
- 2 × T (a time-frame shift):
  - present "cierran" rendered as past;
  - "puedes" rendered as "could".
- 6 writer-correct answers that the judge labelled wrong:
  - **2 × decision 32** (29399 c2, c5): "Todo un profesional. Va a llevar …", rendered with "She". The judge applied the new rule (masculine "un profesional" -> he). Both checker layers accept "she" here: the checker prompts did not get decision 32 (brief: decision 33 changes the judge only; decision 32 was not given a checker change either).
  - 35803 c3: "La profesora sostiene su bolígrafo …", rendered as "his pen … his hand". The judge: la profesora is female. This is debatable: "su" is genderless under decision 22, but the sentence clearly means her own pen.
  - 34288 c5: an added "credit" (in "credit card").
  - 36739 c4: an added "just".
  - 34651 c2: "worst day of my life" without an article. This item is also one of the three duplicate disagreements (its duplicate was labelled correct).

**FR 37: 16 content-check MISSING, 14 TIP rejections, 7 L3 DIFF.** 36 are writer-correct answers; 1 is a writer-W answer that the judge accepted ("toe" for "dedo").
- **Genderless subject (decision 22) at L3: 4 FRs on one A1 sentence.** 24801 "Mira la luna con el telescopio" -> "He looks / He is looking / She watches / He looks … through a telescope". L3 gives TIP or DIFF although the Spanish verb has no subject pronoun. This one sentence accounts for 4 of A1's 13 FRs.
- **Content-check literalism (16):**
  - paraphrases read as a lost word: Hay ("Two bowls … are on the table"), calma (soothing), pela (peeling), quieta (still), despertarte (get up), volver (again), levantado (stood up), revelan (open onto), acerca (holds … up to), cada (all), esquivó (dodged, in a passive rephrasing), montar (assembly table), solía (habitual past without "used to"), recordado (memorized);
  - mantequilla twice: "buttering" absorbs the noun.
- **TIP rejections (14)** of tense or aspect choices judged free:
  - present simple vs progressive;
  - past vs present perfect: "ha teñido", "ha rascado";
  - "will scold" vs "will be scolding";
  - a dropped "por fin" or "completamente", which are allowed drops;
  - "the finger" for "el dedo";
  - "Mate, … I really need";
  - "her friends" for "sus amigos", which is genderless.
- **L3 DIFF (7):**
  - 24801 c1 (the genderless subject);
  - 27345 c5 (perfect for a preterite);
  - 34933 c5 ("puts on" for "lleva");
  - 40144 c5 ("shouldn't have bought so many" for "debería haber comprado menos");
  - 42156 c5 ("learned by heart" for "recordado");
  - 43998 c4 (perfect for a perfect progressive);
  - 39259 w (toe).
- **Reading:** as for de and ua, FAs are mostly dropped modifiers (M) and time-frame slips. FRs come from content-check literalism and from L3 strictness on tense, aspect and genderless subjects. Nothing Spanish-specific stands out beyond the genderless-subject pattern.

Every item, with source, answer and judge reason, is in `W1/es/partD/analysis/ANALYSIS.md`.

## 4. Judge noise and intent agreement

- **80 hidden duplicates:** 77 agree and 3 disagree, **3.75 % [0.78, 10.57]**. For comparison: de 0/80, ua 1/80. The 3 disagreements:
  - A:32586:c4 (A1): "Dandelions have white seeds for the wind to carry." Labelled wrong in s1, correct in s2.
  - A:34288:c4 (A1): "Dude, can I pay with card? I absolutely need that hot dog." Labelled wrong in s5, correct in s6.
  - A:34651:c2 (A2): "…worst day of my life! …" Labelled wrong in s8, correct in s3. The original label (wrong) counts, so this item is one of the 12 FAs.
- **Writer intent vs judge label:**
  - correct -> correct: 489/500. The 11 correct -> wrong include the 2 decision-32 cases and 3 added words.
  - wrong -> wrong: 399/400. The 1 wrong -> correct is W, "toe" for "dedo".
- **Labels:** 490 correct, 410 wrong.

## 5. The packet fix: was a follow-up needed?

**No.** All 8 packets came back complete in their first session (8/8 valid jid sets), so 0 follow-up sessions ran.
- Packet sizes were 122-123 items, half the old 245.
- One subagent (s2) noticed a duplicated jid (jff952) in its own first write and removed it with one extra Edit before finishing (3 tool uses instead of the allowed Read + Write). The pipeline ingested the corrected reply.txt.
  - Had it not corrected the reply, the duplicate would have counted as MISSING and gone to a follow-up.
  - This is recorded in `s2/tokens.json`. It is a deviation from the two-tool-call wrapper, not from blindness: it touched only its own reply file.
- The follow-up path is therefore tested (t15 and the mock) but was not exercised live.

## 6. Part F: app branch `translation-wave1` (no deploy, no push, no merge)

- **Commit 79a8fca** on top of 9bf2e48, in the worktree `~/Projects/and-again-wave1-wt`. Master was not touched.
- **Routing:**
  - `supabase/functions/check-translation/sourceOnly/wave1.ts`: `WAVE1_ROUTED = ['de', 'ua', 'es']`, so `SOURCE_ONLY_NATIVE_LANGUAGES = sk, cz, de, ua, es` (learning English only).
  - `lib/translateExercise.ts`: `TRANSLATE_SCOPE_RESTRICTED_NATIVES = ['sk', 'cz', 'de', 'ua', 'es']`.
  - **Consequence:** es learners of English get the translate format ONLY on the 4,064 selected exercises, like sk/cz/de/ua. The owner should confirm this before a deploy.
- **Replay parity:** the fixture was regenerated with `gen_replay_fixture.py de ua es`. The TS stack re-decides every stored Part D reply: **2,700/2,700 = 100 %**, including **es 900/900**, matching Python on accept, layer and the content-check word.
  - A mutation check (one es accept flipped) makes the replay test fail.
- **Tests updated:**
  - `sourceOnly.wave1.test.ts`: the routed list and the 9 × 4 routing matrix;
  - `sourceOnly.stack.test.ts`: the app/function routing pairs;
  - `lib/translateExercise.test.ts`: the scope pairs.
  - `promptsWave1.ts` and `prompts_wave1_python.json`: only the source sha comment changed.
- **Results:**
  - `npm test`: **427 pass, 0 fail**.
  - `npm run typecheck` (both tsc configs): **clean**, exit 0.
  - deno check was not run (no deno on this Mac).
- **No database write of any kind.** This run read no table: the set was built earlier from the SELECT-only snapshot.

## 7. Gemini calls and spend (counted = HTTP 200 only)

| stage | counted | non-200 / uncounted | spend |
|---|---:|---:|---:|
| L3 | 900 | 0 | $0.0957 |
| content check | 499 | 0 | $0.0389 |
| **es total** | **1,399 of the 2,000 cap** | 0 | **$0.1346 of $0.50** |

- No rate limit and no quota envelope occurred.
- Wave cumulative: 4,214 counted calls; spend $0.2728 + $0.1346 = $0.4074.

## 8. Claude tokens (budget 1,500,000 for this run)

| item | tokens |
|---|---:|
| 8 judge subagents (s1-s8, as the harness reported them) | 284,990 (35,208-36,372 each) |
| follow-up sessions | 0 |
| main session (estimate, own context) | about 200,000 |
| **this run** | **about 485,000** |

The es language ledger (writers + discarded 4-packet judges + new judges) is 791,026 subagent tokens.

## 9. Defects and notes

1. **Frozen de/ua manifests no longer verify against the working tree.** The change to `common/pipeline_w1.py`, `prompts_w1.py`, `test_w1.py`, `chain_w1_sub.sh` and `spec/judge_prompt_es.txt` means a fresh `shasum -c` of de's or ua's FROZEN_SHA_D would now fail. Their measurements stand at their own freeze commits (5507135, 112ccbb), and their spec and prompt texts are byte-identical, but the files they hashed changed. Nothing in de/ua was re-run.
2. **`ANALYSIS.md` header text** says "truth = 4 opus judge sessions". This is hard-coded; es used 8. The numbers are correct.
3. **The checker does not know decision 32.** The two FAs on 29399 are "she" for "un profesional". The brief keeps the checker prompts byte-identical, so the checker and the judge now disagree on masculine nouns. It would take a checker change plus a re-measure to align them.
4. **The genderless subject is not honoured by L3 on a verb without a pronoun** (24801: 4 FRs), although decision 22 is in the L3 prompt.
5. **A per-language reservation cap was added** for es (`CAP_LANG`, 506,036 already spent + 1.5 M - 300 k main session). The old 1.05 M headless cap would have refused 8 parallel judges on top of the discarded sessions.
6. **Blindness is still by instruction**, not by tool restriction (`tx-opus` has Bash, Glob and Grep). One subagent used an extra Edit on its own reply (section 5).
7. **The per-level intervals are uninformative** at n ≈ 100: the FA upper bounds are 9-10 %.
8. **Report location:** this report is committed on branch `translation-wave1` (worktree) and copied, uncommitted, to the master checkout's `docs/features/reports/`, to `W1/`, and to Drive `AndAgain_reports/` (.md and .txt).

## 10. Judgement

1. **Spanish meets both targets on the point:** coverage 92.45 % (target >= 90 %) and FA 2.93 % (target < 5 %). Both interval targets are narrowly missed: the coverage lower bound is 89.74 % and the FA upper bound is 5.06 %.
2. **The packet-level fix worked.** Halving the packets to about 122 items gave 8/8 complete replies on the first attempt, with no follow-up needed. Before, the 245-item packet had failed in all three attempts.
3. **es is routed on the branch** with 100 % replay parity, npm test 427/427 and tsc clean. Nothing was deployed, pushed or merged, and no database row was written.
4. **Before a deploy, the owner should confirm:**
   - the 4,064-exercise scope restriction for es learners of English;
   - whether decision 32 should also reach the checker (the 2 FAs on 29399).
