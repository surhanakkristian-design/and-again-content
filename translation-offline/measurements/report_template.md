# "Translate the sentence" – offline checking, Phase 1 report (pilot, 200 sentences)

Run 17 Sept 2026, 12:40–13:25 UTC. Nothing was written to the database, no app code changed, nothing deployed,
no migration applied, no paid model API called. The only database access was read-only (`supabase db query`
SELECTs for the counts and the sentence dump). All generation and review ran as Claude Code subagents.

Work lives in `~/Projects/and-again-content/translation-offline/` (folder proposed for the pilot output;
`README.md` there maps every file). The migration proposal is
`supabase/migrations/20260917160000_translation_offline_check.sql` in this repo.

## 0. Headline

| | |
|---|---|
| **Coverage (main risk)** | 120 fresh correct translations of 40 pilot sentences, written without seeing the stored lists: **69 accepted as `correct` (57.5 %)**, 3 `correct_with_tip`, **48 `wrong`**. By my reading, 45 of the 48 rejected ones are correct English and should have been accepted. By level: A1 19/27, A2 12/15, B1 24/45, B2 14/33 accepted as correct. |
| Why they fail | synonyms not listed (~22: stapled/clipped, motionless/still, near/beside, lifted/raised, somebody/someone…), **pronoun gender the native sentence does not show** (8: he/she, her/it), determiners (6: the/this/that/a/her), small optional words (7: ever, already, even, up, of them…), other phrasings (~5) |
| Bench vs gemini-3.7-flash | same verdict on **17 of 20**; the three disagreements are all about where `correct_with_tip` ends (§5.2) – in two of them I think Gemini is right, the third is debatable |
| Data per sentence | 5.1 prepared mistakes (10.6 stored sentences once slots expand) and 42.6 acceptable translations (median 23; B1 61, B2 45). 2.1 KB compact (slot syntax) / 11.3 KB expanded |
| Effort | generation 6.4 min wall / 48 agent-minutes / 1.03 M tokens for 200; review 4.5 min wall / 17 agent-minutes / 0.68 M tokens. 5,895 sentences ≈ 32 agent-hours, ≈ 50 M tokens, ≈ 3–4 h wall with 10 agents in parallel |
| Review pass | changed 225 things in 77 of the 200 files: 175 feedback texts, 36 acceptable lines (10 added, 26 fixed), 14 mistake changes (5 verdicts changed, 3 mistakes that were in fact correct moved to acceptable) |

**How I read it:** the checking algorithm and the prepared feedback work, and they are instant. The stored lists
do not work yet as the only gate for B-level sentences. With these lists, four in ten correct B-level answers
would be marked `wrong` with a confident, false "Namiesto X patrí Y". Before scaling, Phase 2 needs at least the
fixes in §6.2 (pronoun rule, synonym slots per content word, determiner and adverb freedom), and then the
coverage measurement again. That is a decision for you, not something I changed.

---

## 1. Part A – topic tiers and allocation

### 1.1 Verification

- All 63 listed type ids exist, all are `focus_category.en = Grammar`, none is type 69.
- **The row counts have changed since the brief was written.** The brief's 23,703 is the state before the A1
  import landed. During this run (between 14:40 and 14:43 local time) every A-level topic grew from 563 to
  774–777 rows. Live now: **29,215** grammar exercises, all with non-empty English, Slovak and Czech
  `full_sentence` (35,028 exercises in total; stable on a second count). The allocation below uses the live
  numbers. The brief's rule of about one quarter still holds: 5,895 of 23,703 is 24.9 %; of 29,215 it is 20.2 %.
- **No topic is short of eligible rows.** The lowest is 245 (every B topic) against a top allocation of 130.
- **But 24 B-level topics do not have enough sentences of up to 12 words.** Together they need **951 sentences
  of 13–16 words** (longest needed: 16 words in topic 57, 15 in 34/53/65/66). All A topics have enough short
  sentences. See the last column.

### 1.2 Allocation table (tiers fixed by Kristian)

"≤12 words" = eligible rows whose English sentence has at most 12 words.

{{ALLOC}}

Totals: A1 1,025 · A2 1,365 · B1 1,795 · B2 1,710 = **5,895**.

Topics with fewer ≤12-word rows than their allocation (topic: ≤12-word rows / allocated): 31: 68/85, 32: 60/85,
33: 101/130, 34: 71/130, 35: 45/85, 37: 15/40, 39: 77/130, 40: 76/130, 41: 100/130, 43: 54/85, 44: 122/130,
45: 120/130, 46: 72/85, 50: 17/85, 51: 76/85, 52: 16/40, 53: 43/130, 54: 26/85, 55: 96/130, 57: 41/130,
60: 110/130, 65: 51/130, 66: 80/130, 67: 47/85.

### 1.3 Pilot selection (200)

`scripts/select_pilot.py`: largest-remainder apportionment, first over the 12 level × tier cells, then over the
topics inside a cell. All 20 bench exercises are included and count inside the 200. Inside a topic the script
takes a seeded random order of the ≤12-word rows and only then longer rows. It skips a row when another chosen
row of the same topic shares its media id or ≥ 50 % of its words (near-duplicates), and it skips rows with `...` / `…`.

| | A1 | A2 | B1 | B2 | tier 1 | tier 2 | tier 3 |
|---|---|---|---|---|---|---|---|
| pilot | 35 | 46 | 61 | 58 | 110 | 72 | 18 |
| exact share of 200 | 34.8 | 46.3 | 60.9 | 58.0 | 110.3 | 72.1 | 17.6 |

Only 7 pilot sentences have more than 12 words, and all 7 are bench cases. So the pilot **under-represents** the
951 longer B sentences the full run needs. Coverage there will be lower than measured here.

---

## 2. Part B – migration (file only, NOT applied)

Three tables, one trigger and one security-definer function:

- `translation_acceptable_answers` holds one row per accepted sentence (the reference is not stored again, it
  stays `exercise_localizations.full_sentence`). It keeps `answer_text` plus `normalized_answer` =
  `normalizeBasic()`. Unique on (exercise, language, normalised form). `language_code` is limited to en/de/es/fr
  so the table can serve other learning languages later. Only `en` is planned.
- `translation_typical_mistakes` holds the mistake text + normalised form, `kind`, a `verdict` check (wrong /
  correct_with_tip), `feedback_sk`, `feedback_cz` (required, ≤ 150) and `feedback_en` (≤ 150). A trigger enforces
  "`feedback_en` present exactly for B1/B2 exercises" from `exercise_types.level`.
- Both are public read: RLS on, a `select using (true)` policy, `grant select` to anon/authenticated, writes
  revoked. This is the same shape as the catalogue migration, so only the service role writes them.
- `translation_unmatched_answers` stores exercise, learning language, native language, normalised answer,
  original text (capped at 300), what the device decided, `count`, first/last seen. No user id and no device id.
  RLS is on with no policies, and all privileges are revoked from anon/authenticated.
- `log_translation_unmatched_answer(...)` is `security definer`, `search_path = ''`, executable by anon and
  authenticated. It validates the input, only logs exercises that have offline data, increments `count` for a
  known key, and inserts new keys only while the exercise has fewer than 500 distinct unmatched answers (spam
  ceiling).

The SQL was not executed anywhere. There is no local Postgres on this Mac, and the brief says "no CLI", so there
was no rolled-back dry run either. It has been checked by reading only.

```sql
{{MIGRATION}}
```

---

## 3. Part C – the checking algorithm

Code: `translation-offline/checker/offlineCheck.ts` (pure functions), tests in `offlineCheck.test.ts`,
`slots.ts` (build-time slot expansion). `typedAnswer.ts` there is a byte-for-byte copy of this repo's
`lib/typedAnswer.ts`, and a test asserts that.

### 3.1 In plain words

"Matches" always means: both sides pass through the typed-answer normalisation of `lib/typedAnswer.ts` (case,
whitespace, punctuation, apostrophe styles, diacritics, English contractions in both directions, numbers 0–100 as
digits or words), and their sets of readings share one member.

1. **Correct.** The answer matches the reference or any acceptable translation → `correct`, no feedback.
   1b. The answer differs only in British/American spellings (colour/color, grey/gray, centre/center,
   realise/realize, travelled/traveled…; rules plus a 45-pair list, a rule result only counts when it is a real
   word) → `correct`.
2. **Prepared mistake.** The answer matches a stored mistake → that mistake's verdict and its feedback in the
   learner's feedback language.
3. **One typo.** After the words are lined up position by position against an accepted sentence of the same
   length, exactly one word differs, and that word
   - has ≥ 4 letters in the accepted sentence,
   - is one edit away (insert, delete, substitute, or swap of two neighbouring letters),
   - is **not a real English word** (so sled/sleds, give/gave, their/there, then/than are never typos), and
   - is **not another form of the same word** (the accepted word ± s, d, r, n, y – catches "childs", "womans",
     which are not in the word list either)

   → `correct_with_tip`, with an automatic tip that shows the correct spelling.
4. **Everything else** → `wrong`. The tip comes from a word-by-word alignment against the closest accepted
   sentence (smallest word edit distance with swaps). An accepted sentence that has exactly the answer's words
   in another order is always taken first. Neighbouring differences form one place. Output:
   - same words, other order → "Pozor na poradie slov: „…“" (only the span that moved; no quote when it would be
     the whole sentence);
   - otherwise up to 2 places, each one of: wrong word(s) "Namiesto „X“ patrí „Y“", missing "Chýba „Y“", extra
     "„X“ tu nepatrí";
   - more than 3 places, a quoted span over 5 words, or text over 150 characters → a generic line ("Porovnaj
     svoju vetu so správnym prekladom.");
   - Czech and English templates are the same ("Místo „X“ patří „Y“", "Write “Y” instead of “X”"…).

**Feedback language (decision 4)** applies to prepared and automatic tips alike: `sk` → Slovak, `cz` → Czech at
every level; any other native language → English at B1/B2 and **no text at A1/A2** (feedback `null`; the app
shows only the correct sentence).

Steps 3 and 4 return `unmatched: true`: these are the answers to log anonymously.

### 3.2 Additions to the shared normalisation (checker only, lib untouched)

The pilot exposed three gaps in `lib/typedAnswer.ts`, which the translate format now depends on much more than
the typed format did. I fixed them **in the offline checker, not in the app library** (no app code changes this
phase):

- typographic double quotes “ ” „ and dashes – —, and brackets, were not punctuation. Several references use
  “action”, so a learner typing "action" got `wrong`;
- `noun + 's` ("the globe's got", "the car's broken") was only ever a possessive. It now also reads as noun +
  is / has, and the possessive reading stays;
- automatic tips showed digits for number words ("Namiesto „kind“ patrí „1“" for "the same one"). They now show
  the word.

These three should move into `lib/typedAnswer.ts` in Phase 2.

### 3.3 Word list

- **Source:** the SCOWL-derived Hunspell `en_US` dictionary, version 2020.12.07 (wordlist.sourceforge.net, SCOWL
  size 60). It was taken from the copy that ships with the Adobe Photoshop Hunspell plugin on this Mac, so
  nothing was downloaded. The file header and README match the upstream release.
- **Licence:** the SCOWL copyright notice (Kevin Atkinson; use, copy, modify, distribute and sell for any purpose
  if the notice is kept; MIT-like) plus the Ispell BSD licence for the affix file. The README with the full notice
  is kept as `wordlist/SCOWL_LICENSE.txt`. (The `en_GB` dictionary in the same folder is GPL/LGPL and was **not**
  used.)
- **Build:** `wordlist/build_wordlist.py` expands the affix rules (prefixes, suffixes, cross products; the
  possessive flag is not expanded) → **99,756 lower-case word forms, 984 KB raw, 263 KB gzipped**. It removes
  capitalised entries unless the word also exists in lower case (proper names), and 247 abbreviations written
  without a full stop ("biol", "govt", "assoc"…). Those would block real typos: without the filter, "biol" for
  "boil" was not a typo.
- **Proposal for the phone:** do not ship the list. The typo step only needs the dictionary words that are one
  edit away from the words of that exercise's accepted sentences. Precomputed per exercise at build time, that is
  **0.7 KB on average (max 1.8 KB)** in the pilot (1,094 distinct target words → 5,837 neighbours in total). It
  can be stored next to the acceptable translations and gives exactly the same verdicts.

### 3.4 Raw test output

`node --test checker/*.test.ts` (Node 26.3):

```
{{TESTS}}
```

---

## 4. Ten complete pilot sentences

2 per level plus 2 more B-level; six of them are bench exercises (20435, 21510, 16034, 11348, 7845, 10330).
Everything after the review pass, exactly as stored in `pilot/generated/` (slot lines) and `pilot/expanded/`
(the sentences below). Feedback texts are verbatim.

Visible defects in these ten (left as they are, reported instead):
- 4.1, mistake 1: the feedback quotes „The plate is white…“, copied from the example in `GENERATION_SPEC.md`
  (the reference says "The big plate…"). It is harmless but shows the generator copies examples, so the spec
  example should use a neutral sentence.
- 4.1: the reference says "very", while both native sentences say "úplne/úplně" (completely). The generator
  noted this under `source_issues` and accepts both.

{{EXAMPLES}}

---

## 5. Part E – measurements

### 5.1 Coverage (the main risk)

**Method.** `measurements/coverage_input.json` holds 40 pilot sentences drawn at random (seed 4040: 9 A1, 5 A2,
15 B1, 11 B2; 4 are bench exercises). A fresh subagent received only exercise id, level, topic and the Slovak and
Czech sentences – not the reference, not the stored lists – and was told to write 3 different correct
translations each, as three different learners would, using the practised grammar. The 120 sentences went
through the Part C checker (`scripts/run_measurements.ts`, native `sk`).

**Result (after the review pass):**

| | correct | correct_with_tip | wrong |
|---|---|---|---|
| all 120 | **69** (57.5 %) | 3 | **48** |
| A1 (27) | 19 | 0 | 8 |
| A2 (15) | 12 | 1 | 2 |
| B1 (45) | 24 | 1 | 20 |
| B2 (33) | 14 | 1 | 18 |

Steps: 17 matched the reference, 52 an acceptable translation, 3 a stored `correct_with_tip` mistake, 48 went to
step 4. **No typo step:** none of the 120 had a typo.

Before the review pass (same checker): 67 / 3 / 50. The review's 10 added lines rescued only 2 of these.
Before my three normalisation additions (§3.2): 65 / 3 / 52.

**Every non-correct one, with my judgement** (C = the accepted sentence the tip was built from; the tip is what a
Slovak learner would see):

{{COVERAGE}}

**Judgement summary:** of the 48 `wrong`, **45 are correct translations that should be accepted**.
One (#33) should be `correct_with_tip` (it avoids CAN). Two are not clean: #4 is an unnatural Past Continuous
passive, and #30 "wasted" a penalty is odd. Of the 3 `correct_with_tip`, all three verdicts are defensible
(#28 could even be `wrong`, since "might have" changes the meaning).

**So of about 116 answers that deserve acceptance, 69 were accepted: ~59 %.** Each of the 45 false rejections
also shows a confident, wrong tip ("Namiesto „near“ patrí „beside“", "Namiesto „she“ patrí „he“").

### 5.2 Comparison with gemini-3.7-flash on the 20 bench answers

`measurements/bench_comparison.json` (Gemini verdicts from TRANSLATION_BENCH_REPORT.md §2).

| # | answer | offline | step | gemini-3.7 | offline feedback (sk) |
|---|---|---|---|---|---|
{{BENCH}}

**Agreement 17 / 20.** The disagreements:

| # | answer | offline | Gemini | who is right |
|---|---|---|---|---|
| 3 | He is able to find her before she **comes** home. | wrong (auto: "Namiesto „is able to“ patrí „can“.") | correct_with_tip | **Gemini.** The sentence is correct and only avoids CAN. The generator stored "is able to" as `correct_with_tip`, but only in combinations with "gets"/"she", so this combination fell to step 4. The same combinatorial gap as the coverage failures. |
| 9 | On the bench is one long bandage. | wrong (stored mistake) | correct_with_tip | **Gemini, by decision 5.** The locative inversion is grammatical and has the same meaning; it avoids *There is*. The pilot is inconsistent here: in exercise 18966 the reviewer changed exactly this pattern to `correct_with_tip`, but in 11610 it stayed `wrong`. The feedback "Chýba „there“" is fine for either verdict. |
| 20 | I wish my cat **was** as calm as that **ginger** one… | correct_with_tip ("V hovorovej reči sa „was“ používa, no po „wish“ je štandardné „were“.") | correct | **Debatable.** "was" after *wish* is standard in modern British and American usage; "were" is more formal, not clearly more natural. I lean to Gemini, but the tip is true and harmless. |

Where both agree, the prepared feedback holds up against Gemini's. It is shorter, names the tense in English, is
never gendered, and never praises. The automatic tips are weaker than Gemini's where a part is missing: case 12
says "Chýba „and cherry“" (the closest accepted variant has no "the"), and Gemini says what the missing part means.

### 5.3 Size and effort

**Per sentence, after review** (`pilot/expanded/_stats.json`; bytes = compact JSON of the acceptable + mistake
lists without the sentence metadata):

| level | n | avg words | acceptable translations mean / median | mistakes (prepared) | mistake sentences after slot expansion | compact slot JSON | expanded JSON (DB shape) |
|---|---|---|---|---|---|---|---|
| A1 | 35 | 8.3 | 32.9 / 11 | 4.8 | 7.6 | 1.39 KB | 6.74 KB |
| A2 | 46 | 9.8 | 22.8 / 13.5 | 5.4 | 8.4 | 1.66 KB | 5.97 KB |
| B1 | 61 | 11.2 | 61.1 / 35 | 4.9 | 13.4 | 2.47 KB | 16.59 KB |
| B2 | 58 | 11.2 | 44.7 / 31 | 5.3 | 11.3 | 2.58 KB | 12.55 KB |
| all | 200 | 10.2 | 42.6 / 23 | 5.1 | 10.6 | 2.12 KB | 11.25 KB |

Max acceptable translations for one sentence: 287 (A1 – slots multiply quickly). Min: 1.

**Time and tokens for the 200** (Claude Code subagents, Opus 5; 10 generation agents with 17–23 sentences each,
then 5 review agents with 40 each, all in parallel):

| phase | wall time | sum of agent run times | subagent tokens |
|---|---|---|---|
| generation | 12:48:14 → 12:54:37 UTC = **6.4 min** | 2,891 s = **48.2 min** (208–383 s per batch) | 1,026,185 |
| review | 12:55:27 → 12:59:55 UTC = **4.5 min** | 1,043 s = **17.4 min** (167–245 s per list) | 677,143 |
| coverage writer (E1) | 1.0 min | 59 s | 73,672 |
| **per sentence** | | **19.7 s** of agent time | **8,500 tokens** |

**Extrapolation to 5,895 sentences** (× 29.5, same model and batch sizes):

| | pilot 200 | 5,895 |
|---|---|---|
| agent time generation + review | 65.6 min | **≈ 32 h** (≈ 37 h adding ~15 % for the 951 longer B sentences) |
| wall time at 10 agents in parallel | 11 min | **≈ 3.5–4.5 h**, plus supervision and lint runs |
| tokens | 1.70 M | **≈ 50 M** |
| acceptable translation rows | 8,515 | **≈ 251,000** |
| mistake rows | 2,127 | **≈ 62,700** |
| JSON, compact slot form | 0.42 MB | ≈ 12.5 MB |
| JSON, expanded (DB shape) | 2.25 MB | ≈ 66 MB |
| per-exercise typo neighbour lists (§3.3) | 0.14 MB | ≈ 4 MB |

These numbers are for the current list size. The fixes in §6.2 will make the lists bigger: pronoun and synonym
slots multiply the expansions, and B1 already averages 61 sentences. If the lists grow by 3–5×, storing slot
patterns and matching them on the device (a small pattern matcher instead of full expansion) becomes the better
design. See §6.2.

---

## 6. Decisions I made myself

### 6.1 Made and applied

1. **Live row counts, not 23,703.** The A1 import landed during the run. Part A and the pilot use the 29,215 live
   grammar rows. The allocation stays exactly as decided (5,895).
2. **Pilot proportions:** two-step largest remainder (level × tier cells, then topics). Bench cases are placed in
   their own topics first.
3. **Near-duplicate rule:** same media id, or ≥ 50 % shared words, within a topic. Rows with `...`/`…` are
   skipped.
4. **Slot syntax `{a|b|}`** for generation. Every combination is expanded at build time; the database stores
   plain sentences. Max 96 combinations per line.
5. **Generation and review by subagents** with written specs (`GENERATION_SPEC.md`, `REVIEW_SPEC.md`). The review
   agents were different agents from the generators. Generators and reviewers were told not to open the bench
   file, so the 20 bench learner answers never reached them.
6. **The reviewer may also add** clearly missing common translations (counted separately: 10), not only remove
   or fix.
7. **Review lists mix levels** (every 5th file of the level-sorted list), so no reviewer only sees one level.
8. **After generation I added two rules to the review spec:** a pronoun rule (accept every subject the native
   sentence allows) and "past participle" in English. The first generator batches had used "příčestí minulé".
9. **Lint gate** (`scripts/build_pilot.ts`): copied fields unchanged, 3–6 mistakes, ≤ 96 combinations, feedback ≤
   150 characters, `feedback_en` exactly for B, gendered forms, translated grammar names, praise, whole reference
   in the feedback, a mistake equal to an acceptable sentence, and the checker must land every stored sentence in
   its step. Before review: 18 findings (16 translated grammar names, 2 gendered). After review: 2, both false
   positives in 10677, where the feedback quotes a Slovak rendering of the sentence ("„Mal si kúpiť“ … je „should
   have bought“"), not an address to the learner.
10. **Checker additions beyond the brief:** step 1b (British/American spelling), the three normalisation
    additions of §3.2, "another form of the same word" = ± s/d/r/n/y, a preference for the permutation candidate
    in step 4, and a generic tip instead of long quotes.
11. **Czech language code `cz`** (as in the database); the checker also accepts `cs`.
12. **Word list filtering:** lower-case SCOWL entries only, 247 unpunctuated abbreviations removed, no en_GB
    (licence).
13. **Migration details:** reference not duplicated into the variants table; a `language_code` column for later
    languages; a `kind` column; a `content_version` column; the level rule for `feedback_en` as a trigger;
    `device_verdict` in the log; a 500-distinct-answers-per-exercise ceiling; the log function ignores exercises
    without offline data.
14. **Coverage writer did not see the reference**, only the native sentences (a learner does not see it either).
    This makes the measurement stricter than showing the reference would.

### 6.2 Proposed, not applied (for your decision)

1. **Pronoun rule** at generation: whenever the native sentence does not fix the subject's gender, write
   `{He|She}` slots (and `{her|it}` for "ju" referring to a thing). This alone would have fixed 8 of the 45 false
   rejections.
2. **Synonym slots for every content word** that has a common synonym, instead of the ~2 slot lines per sentence
   the generators wrote. The review pass did not catch this. It checked what was there, not what was missing.
   A dedicated "missing variants" pass, where a second agent writes 5 independent translations and every
   rejected-but-correct one is added, would target exactly the failure measured in §5.1. It costs roughly the
   price of the review pass again.
3. **Determiner and small-word freedom** (the/this/that, a/the where the native has no article; already, just,
   even, ever, up) as explicit slots.
4. **Store patterns, match on the device** once lists grow, instead of 250,000+ expanded rows.
5. **Soft landing for step 4 at B level:** when the closest accepted sentence differs only in content words that
   are not the practised grammar (the aligned difference does not touch the `correct_answer` span of the
   exercise), return `correct_with_tip` with "Iné slovo, ale v poriadku: v zadaní je „clipped“" instead of
   `wrong`. That is a verdict-policy change (decision 5), so it is only a suggestion. It would have turned about
   20 of the 45 false rejections into a tip.
6. **Unmatched log review loop:** read `translation_unmatched_answers` weekly, add the correct ones as variants.
   With 59 % coverage that queue will be large at launch.
7. **Consistency sweep for correct_with_tip boundaries** (locative inversion, no backshift in reported speech,
   was/were after wish). The pilot has the same pattern with different verdicts in different exercises.
8. Fold §3.2 into `lib/typedAnswer.ts`, and change the `GENERATION_SPEC.md` example sentence (it was copied into
   one feedback).

## 7. Housekeeping

- Content repo: `translation-offline/` committed locally (`data/grammar_rows.json` is git-ignored, 10 MB,
  reproducible with `scripts/dump_rows.py`). Other uncommitted files that were already in the content repo were
  not touched and not committed.
- App repo: this report and the migration file committed locally. The untracked
  `docs/features/PROJECT_HANDOFF_CHAT.md` that was already there is not part of the commit.
- Nothing pushed, nothing applied, nothing deployed.
