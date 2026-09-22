# Translation Wave 1: SOURCE-ONLY checker for native German (de), Ukrainian (ua) and Spanish (es) -> English. Report (22 Sept 2026)

Working directory: `~/Projects/and-again-content/translation-offline/wave1/` (below: `W1/`). App branch: `translation-wave1` in `~/Projects/and-again` (local, not pushed).

## 0. Headline: NO language was measured, so no DB write was made

Every language stopped at its **first headless Claude session**. The CLI answered: "You've hit your weekly limit · resets 11am (Europe/Vienna)". That was 12:39:08-12:39:12Z, 10 sessions, 0 tokens each. The brief says a usage-limit error stops the language, so none was relaunched.

| language | coverage (pooled / per level, CP 95 %) | FA (pooled / per level, CP 95 %) | >= 90 % / < 5 %, point | same, interval | DB write | stopped at |
|---|---|---|---|---|---|---|
| de | not measured | not measured | not assessed | not assessed | none (de has no rewrite) | Part D writers (4 sessions) |
| ua | not measured | not measured | not assessed | not assessed | **NO** | Part B rewrite pass 1 (3 sessions) |
| es | not measured | not measured | not assessed | not assessed | **NO** | Part B rewrite pass 1 (3 sessions) |

- **Test set:** no Part D set was ever opened. The de set of 100 sentences was built and committed, but it was never frozen or opened, so it can be reused. For ua and es no set was built.
- **Gemini:** 0 calls, $0.00.
- **Claude:** headless tokens 0, total about 450k of the 4,000,000 budget.
- **Earlier phase directories:** byte-identical. SHA-256 over 5,016 files before and after: 0 differences (`W1/SHA_before.txt`, `SHA_after.txt`, `SHA_diff.txt`).

**Everything before the first headless session ran and passed:**
- decisions 22-25 recorded;
- Part A (SELECT only) for all three languages;
- the shared stack and prompts;
- the test suite, 13/13 with the model mocked;
- the token projection for de: 953,619 of 1,300,000;
- the Part D mock for de.

**To resume after the reset:**
1. Delete `STOP_quota.md`, `STOP_usage_limit.md` and `CHAIN_FAIL.txt` in `W1/de`, `W1/ua` and `W1/es`. The spawner refuses to start while `STOP_usage_limit.md` exists.
2. Relaunch `nohup bash W1/common/chain_w1.sh <lang> > W1/<lang>/chain.log 2>&1 &` for each language.

Nothing is spent twice.

## 1. Owner decisions recorded

Decisions 22-25 are appended to `translation-offline/upload_skcz/OWNER_DECISIONS_2L.md` (and-again-content commit **808d1f2**):
- 22: genderless sources, both he/she and his/her are correct, new languages only;
- 23: explicit-subject rewrite for es / ua / tr / hu on the 4,064;
- 24: $3.00 Gemini for the six new languages;
- 25: two waves.

## 2. Part A: data (SELECT only), per language

- **Source:** `W1/<lang>/partA/partA.md`, `partA.json`, `rows.jsonl` (with SHA-256).
- **Rows:** 4,064 per language, one localization row per exercise. Per level: A1 1,174 / A2 1,220 / B1 885 / B2 785.

**Main finding: 2,015 of the 4,064 selected exercises have NO full_sentence (and no intro_text) in de, ua and es.**
- By level: A1 395, A2 431, B1 645, B2 544.
- fr, tr and hu have exactly the same gap. sk, cz and en have 0 empty rows.
- Only **2,049** exercises per language carry a native sentence: A1 779, A2 789, B1 240, B2 241. Only these can be shown in the translate format to de/ua/es learners, or rewritten.
- Nothing was fixed.

| finding | de | ua | es |
|---|---:|---:|---:|
| empty full_sentence | 2,015 | 2,015 | 2,015 |
| duplicated text | 0 | 0 | 0 |
| identical to English / looks English | 0 / 0 | 0 / 0 | 0 / 0 |
| wrong language (Russian letters / no Cyrillic) | - | 0 / 0 | - |
| no final punctuation | 2 | 138 | 0 |
| "??", "…", gap or trailing comma | 0 | 1 | 1 |
| unbalanced ¿ ? | - | - | 1 |
| "foreign" letters (heuristic) | 2 | - | 2 |
| Latin word in Ukrainian | - | 1 | - |

**Every flagged row other than the empty ones:**

**de:**
- 29171 "…Dieses Café ist ein Albtraum!" and 29183 "…Cafétisch…": "foreign letters". Both are **false positives**: é in a loanword.
- 1228 „Ich könnte hier keine Stunde ohne Handy sitzen.“ - „Er auch nicht, offenbar.“: "no final punctuation". **False positive**: the closing “ is not in the check's list.
- 3046 "Sein Hemd ist durchgeschwitzt, … gegen den Karren stemmt": a real missing period.

**ua:**
- 720 "Ти вистелила деко пергаментом, правда ж??": doubled "??".
- 32236 "Він щовечора сідає у червоне Ferrari.": Latin word, legitimate (a brand name).
- **138 rows without a final period.** Mostly short A1/A2 sentences, e.g.:
  - 2454 "Половину тарілок вони вже склали, коли стельова лампа без жодного попередження згасла"
  - 12434 "На кухні надто багато диму"
  - 26685 "Важке тренування потребує багато сили"
  - The full list is in `W1/ua/partA/partA.md`.
  - None is truncated in meaning. It is a formatting gap only.

**es:**
- 720 "¿Forraste la bandeja con papel de horno, ¿verdad??": two ¿ and a doubled "??".
- 10819 "¿Estaba pasadísimo de ácido, ¿verdad?": two ¿ and one ?.
- 20126 "Otros dos pingüinos…" and 20142 "Hay dos pingüinos…": "foreign letters". Both are **false positives**: ü is Spanish.

Wrong-language checks found nothing: no English text, no Russian letters, no Cyrillic in de/es, no rows much shorter than the English. The same row 720 is malformed in ua and es.

## 3. Part B: explicit-subject rewrite (ua, es)

**Not run.** All 3 pass-1 sessions per language were refused with the weekly limit before producing output.

| | ua | es |
|---|---:|---:|
| rows to rewrite (non-empty) | 2,049 | 2,049 |
| changed | 0 | 0 |
| unchanged | not run | not run |
| flagged ambiguous | 0 | 0 |
| machine-check failures | 0 | 0 |
| second-pass disagreements | 0 | 0 |

There are no examples to show: 0 of each category exists.

The rewrite is built and tested (`W1/common/pipeline_w1.py` rw_pass1 / rw_pass2 / rw_final):
- **Pass 1:** three headless opus sessions of about 683 sentences each. They return only the changed sentences, following the 1J / 2A arm-B rule: ONE nominative pronoun in the main clause, or else in a subordinate clause.
  - Allowed pronouns for ua: я/ти/він/вона/воно/ми/ви/вони.
  - Allowed pronouns for es: yo/tú/él/ella/usted/nosotros/nosotras/vosotros/vosotras/ellos/ellas/ustedes. The feminine plurals nosotras/vosotras were added to the brief's list because a feminine-plural verb needs them.
  - An ambiguous subject gets the natural reading plus a flag.
- **Machine check:** the new tokens must equal the old tokens plus exactly one allowed pronoun. Punctuation, word order and case must be unchanged, except the first word's capital. This was unit-checked on 10 hand cases.
- **Pass 2:** independent sessions judge every changed sentence on four points:
  - only the pronoun was added;
  - the pronoun agrees with the verb;
  - the meaning is unchanged;
  - the sentence is grammatical.
- **Final rule:** a change is kept only if the machine check AND pass 2 agree; otherwise the original stays.

## 4. Part C: the checker (built, 0 calls, tests pass)

**Stack** (`W1/common/stack_w1.py`):
- **L3 SOURCE-ONLY:** gemini-3.1-flash-lite, temperature 0, thinkingBudget 0.
  - SAME goes on to the content check.
  - TIP is REJECTED.
  - DIFF and an unparsable reply are rejected.
- **Content check:** NONE accepts, MISSING rejects, a failed call keeps the accept.
- **No F4, no AG, no exact-reference layer.**
- **Transport:** byte copy of `phase2l/run_2i_base.py`. The parser and decide come from a byte copy of `phase2l/content_check.py`. The headless spawner is a byte copy of `phase2j/run_2j.py`.

**Prompts** (`W1/common/prompts_w1.py` generates `W1/spec/*.txt`) are derived by exact substitution from the frozen texts:
- L3 from `phase2k/spec/l3_system_cz.txt` / `l3_user_cz.txt`;
- the content check from `phase2l/content_check.py`, with the decision-2 line kept;
- the judge from `phase2l/partE/judge/judge_prompt.txt`;
- the writer from `phase2k/spec/writer_template_cz.txt`.

Only three things change:
1. **The language name.**
2. **The droppable-word list**, written from the owner's list:
   - de: jetzt, heute, schon, noch, endlich, dann, damals, total, völlig, gerade, eben, Schau!
   - ua: зараз, тепер, сьогодні, вже, ще, нарешті, тоді, зовсім, цілком, повністю, щойно, Дивись!
   - es: ahora, hoy, ya, todavía, aún, por fin, finalmente, entonces, totalmente, completamente, justo, ¡Mira!
3. **Decision 22**, added as one rule line: "Genderless source: when the <L> sentence does not mark gender (e.g. …), BOTH he/she and his/her are correct." The examples per language:
   - de: "sich", or a neuter noun for a person such as "das Kind";
   - ua: "свій", "себе", or a verb form without a subject pronoun;
   - es: "su", "sus", "se", or a verb without a subject pronoun.

The sk/cz prompts and code were not changed. Test t13 proves the frozen sources are untouched.

**Test suite** `W1/common/test_w1.py`: **13/13 PASS**, with Gemini HTTP and the headless spawner mocked (0 real calls). It covers:
- **Prompt derivation:** byte-exact back-substitution to the frozen cz text for L3, content check, judge and writer.
- **Spec files:** equal to the generator.
- **Parsers:** L3 and content check.
- **"429" in a row number / answer / reply text:** counted, not a rate limit.
- **A real 429 and a 503 envelope:** retried and not counted.
- **Usage-limit envelopes:** a Gemini per-day quota causes a STOP with 0 counted calls. A headless "usage limit" error envelope causes a hard stop plus `STOP_usage_limit.md`. This is the path that fired today.
- **Resume at 0 cost:** 0 new calls, identical output.
- **Relative / outside paths refused.**
- **Poison:** throwing reference values, and no English reference text in any request body.
- **Layer order.**
- **Caps:** the language cap, the wave cap, and a concurrent-language race held by a lock with a per-call reservation.
- **The drop lists and decision 22** in every prompt.
- **The frozen sources byte-identical.**

The chain re-ran the suite as preflight for each language: 13/13 each time.

## 5. Part D: measurement

**Not reached for any language.** The machinery is built and committed:
- set, mock, writers, packets, judges, labels, items;
- freeze (`FROZEN_SHA_D`, `FREEZE_HASH`, `FREEZE_COMMIT`, `RUN_COMMIT`, clean tree, shasum -c before open);
- one open with an access log;
- post (CP 95 %, FINAL_RUN_DONE).

**The set method:**
- 25 per level from the language's non-empty rows (the rewritten versions for ua/es).
- exercise_ids from earlier measurement sets are excluded: 460 ids from every `set/` directory under phase1*/phase2*.
- The three wave-1 sets are disjoint by construction: one shared seeded order, positions mod 3.

**The judge** uses the owner's rules verbatim, including decision 22. Packets are jid / source / level / answer / topic, with 80 hidden duplicates and a 400k cap per session.

**de only, run and passed:**
- The token projection: 953,619 of 1,300,000 (2L actual writers 219,767 + judges 313,058, x1.15, plus one judge retry and the agent reserve).
- The set build: 25 per level, 0 used-before ids needed.
- The mock of the whole headless path plus the real stack (poison-wrapped, HTTP mocked): MOCK PASS.

**False acceptances / false rejections by cause:** none exist (nothing was judged or checked).
**Judge noise:** not measured.

## 6. Part E: database write

**No write was made for any language.** Part E runs only for ua/es languages that met both targets, and none was measured.
- **Backup, rollback.sql, dry run, verification:** none were executed.
- **The tooling is prepared** in `W1/partE_tools/partE_db.py` (commit f29e7d8) but was **never run**, so it is untested against the live DB:
  - gate on HEADLINE.json;
  - backup of the 4,064 rows (jsonl + SHA-256) and whole-table checksums per language;
  - rollback.sql (not run);
  - a dry run inside begin/rollback with counts per batch;
  - batches of at most 500 as `update … from (values …) where full_sentence = old`, each in its own begin/commit and idempotent;
  - verify: re-select equals the file, other languages and non-selected rows unchanged, target rows unchanged apart from full_sentence.

## 7. Part F: app branch (no deploy, no push)

- **Branch:** `translation-wave1`, from `master` (941f487). Commit **2ba2b1b**, not pushed.
- **No language is routed:** none met both targets (none was measured). So `WAVE1_ROUTED = []` and the routing for all 9 native languages is unchanged: only sk>en and cz>en take the SOURCE-ONLY path.

What is on the branch:
- `sourceOnly/promptsWave1.ts`: **generated** by `scripts/translation-wave1/gen_prompts_ts.py` from the frozen wave-1 Python (`prompts_w1.py`, sha256 6ea9e978…).
- `sourceOnly/wave1.ts`: the wave-1 stack, L3 then content check with no F4. It reuses the unchanged sk/cz parsers and `decide`.
- `route.ts`: `CheckerLang` = sk | cz plus the routed wave-1 languages.
- `handler.ts`: dispatches a wave-1 language to the wave-1 stack; sk/cz go through the unchanged 3A2 stack. The metrics name the checker.
- **Nothing else changed:** `prompts.ts`, `stack.ts`, `f4.ts`, `replies.ts`, `index.ts` and `lib/translateExercise.ts` are untouched.

**Tests** (`sourceOnly.wave1.test.ts`, 6 tests):
- **Prompts byte-identical to Python**, including the request key, recomputed in TS with Python's json.dumps format.
- **Drop lists and decision 22** in every prompt.
- **Routing:** 9 natives x 4 learning languages, app copy equal.
- **Layer order**, and a subject clash that F4 would catch still reaches L3.
- **A rate-limited L3 call** gives not_verified and releases the reservation.
- **Poison:** throwing reference getters, and no English reference in any request.

**Replay parity against Part D stored replies: NOT DONE.** There are no stored replies.

**Checks:**
- `npm test`: **425 pass, 0 fail** (419 before plus 6).
- `npm run typecheck` (both tsc configs): **clean**.
- `deno check` on check-translation: only the known `_shared/gemini.ts` BodyInit error.

## 8. Gemini calls and spend

| language | calls (HTTP 200) | failed | spend |
|---|---:|---:|---:|
| de | 0 | 0 | $0.00 |
| ua | 0 | 0 | $0.00 |
| es | 0 | 0 | $0.00 |
| **wave** | **0 of 5,000** | 0 | **$0.00 of $1.50** |

The only Gemini traffic was mocked (the tests and the mock).

## 9. Claude tokens

| session | tokens |
|---|---:|
| main session (estimate, own context) | ≈ 365,000 |
| de agent | 26,400 |
| ua agent | 29,214 |
| es agent | 28,279 |
| headless sessions (10 spawned, all refused by the weekly limit) | 0 |
| **total** | **≈ 449,000 of 4,000,000** |

Per language (agent plus headless): de 26,400, ua 29,214, es 28,279. The shared build cost is in the main session.

## 10. Defects recorded, NOT fixed

1. **No quota pre-check before spawning headless sessions.** The token projection checks only the language budget, not the account's weekly limit. Ten sessions were spawned into a limit that a cheap 1-turn probe would have caught. All three agents flagged this.
2. **2,015 of the 4,064 selected exercises have no full_sentence (or intro_text)** in de/ua/es/fr/tr/hu. Only 2,049 per language can ever be translate-eligible for these natives, and B1/B2 have only 240/241. This is a data gap, not fixed.
3. **The Part A heuristics have false positives:**
   - é in "Café" (de) and ü in "pingüinos" (es) are flagged as foreign letters;
   - a German closing quote “ is flagged as missing punctuation (de 1228).
   - Real defects found: de 3046 (no period), ua 720 / es 720 (malformed "??" and double ¿), es 10819 (¿…, ¿verdad? with one ?), and 138 ua rows without a final period.
4. **A Part E rewrite of full_sentence would not update intro_text or chunks.** For es, 1,594 of the 4,064 rows have `chunks`, and the data contract in `lib/sentenceBuild.ts` says the chunks, joined, equal full_sentence. An inserted pronoun breaks that contract for every rewritten es row that has chunks. The brief orders full_sentence only; the owner should rule before an es write. For ua (no chunks) and es, intro_text (the gap sentence) would also no longer match the rewritten full_sentence.
5. **Part E tooling was never executed**, so it is untested against the live DB.
6. **Part F replay parity was not done** (no Part D replies).
7. **Gemini cap design differs from a static split.** The per-language cap is 1,800, not a static 1,650, because the Part D mock showed a worst case of 900 L3 + 900 CC calls. The 5,000 wave cap is held strictly by a lock with a one-call reservation instead.
8. **`lib/translateExercise.ts` still hard-codes ['sk', 'cz'].** When a wave-1 language is routed, it must be added there too; the routing test catches a mismatch.
9. **Pronoun list widened.** nosotras/vosotras were added to the es pronoun list beyond the brief's list.
10. **The main-session token figure is an estimate.**
11. **The de Part D set is built** (`W1/de/partD/set/sentences.jsonl`) but was never frozen or opened. make_set is deterministic, so a resume rebuilds the same set.

## 11. Judgement

1. Wave 1 produced no measurement: the Claude account's weekly limit stopped all three languages at their first headless session, at 0 tokens and $0.
2. So no language met, or missed, the coverage >= 90 % / FA < 5 % targets. Nothing was written to the database and nothing is routed in the app.
3. The whole pipeline (prompts, stack, rewrite, measurement, DB write, app port) is built, committed and tested with mocks. After the reset it can resume from the first headless session with no rework.
4. The biggest real finding is the data: only 2,049 of the 4,064 selected exercises have a de/ua/es sentence at all, which caps the scope of the translate format for these learners.
5. Before any ua/es write, the owner should rule on the divergence from intro_text (both) and chunks (es, 1,594 rows) that a full_sentence-only rewrite creates (defect 4).
