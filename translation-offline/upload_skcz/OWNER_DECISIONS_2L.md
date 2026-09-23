# Owner decisions after Phase 2L (22 Sept 2026)

Recorded at the start of the SK/CZ upload session, as given in the upload brief.

1. **Czech accepted on the point estimate** (coverage 95.17 %, FA 3.23 %). The FA interval (upper bound 5.45 %) is waived. No re-measurement.
2. **Content-check line** "tense, articles and word order are not part of this question" (2L defect 1): **KEPT**.
3. **Judge line replaced by "- Added content is wrong."** (2L defect 3): **CONFIRMED** as intended.
4. **Upload of the SK and CZ files: APPROVED.** The only write allowed is an UPDATE of existing `exercise_localizations` rows for the exercises and languages in the two files. No INSERT, DELETE, schema change, migration, deploy or push.
5. **Frozen checker configuration for both languages:** SOURCE-ONLY + content check, TIP rejected (2L Part C freeze 0042aaa, Czech freeze f9f794c).

## Decisions after the SK/CZ upload stop (22 Sept 2026, Phase 3A brief)

6. **The 54 disputed English references:** KEEP the live English. No write.
7. **structure_json:** WAITS until app integration. No column is created now.
8. **The SK/CZ upload is a no-op** (`src` already live on 8,128/8,128 rows). **Closed.**
9. **Next step:** integrate the SK + CZ checker into the app (Phase 3A).

## Decisions after the Phase 3A Part A stop (22 Sept 2026, Phase 3A continued brief)

10. **AG is DROPPED from the app checker** (option C). App stack = F4v2 -> F4v3 -> L3 -> content check. The 14 AG-decided items are re-measured first (Part A2).
11. **Scope option C:** for learners whose native language is `sk` or `cz`, the translate format shows ONLY the 4,064 selected exercises (the exercise_ids of upload_sk_final.xlsx / upload_cz_final.xlsx, same ids in both), all checked by the new checker. Every other native language keeps today's behaviour and today's check.
12. **ONE additive database change approved:** a new small table listing the 4,064 selected exercise_ids (Part A3). No change to existing tables.

## Decisions before the Phase 3B deploy (22 Sept 2026, Phase 3B brief)

13. **Production Gemini spend for the sk/cz check approved** (projected about $0.14 per 1,000 checks).
14. **Cache stays OFF on the sk/cz path.** No database change for it.
15. **The exact-reference match stays for sk/cz.**
16. **No feedback text for sk/cz:** a wrong answer shows only the correct English sentence, then advances. The MISSING word is not shown.
17. **sk/cz learners of German, Spanish or French keep today's check** (the new checker judges English only).
18. **The 23 concepts without a selected exercise stay as they are.** No change.
19. **No backward compatibility for old app versions is needed** (almost no active users). Deploy as built.
20. **Deploy approved** as in the Phase 3B brief.

## Decision after the Phase 3B deploy (22 Sept 2026, Phase 3C-prep brief)

21. **Warm-up for check-translation:** add a warm-up ping so the learner does not wait for a cold start (built and tested in Phase 3C-prep, deployed separately).

## Decisions for the new languages (22 Sept 2026, Wave 1 brief)

22. **Genderless sources:** when the source does not mark gender (e.g. Turkish/Hungarian 3rd person, Spanish "su", French "son/sa/ses"), BOTH he/she and his/her are correct. This rule is added only to the new languages' prompts.
23. **Explicit-subject rewrite** (arm B, as for sk/cz) for es, ua, tr, hu, on the 4,064 selected exercises only.
24. **Gemini budget for all six new languages:** up to $3.00 in total.
25. **Two waves:** wave 1 = de, ua, es (Wave 1 brief); wave 2 = fr, tr, hu (later).

## Decisions for the data pass (22 Sept 2026, Data pass brief)

26. **Headless CLI sessions are NOT used.** All Claude work runs as Opus subagents in the main session (the headless OAuth token belongs to an old account).
27. **Rewritten/translated native sentences go DIRECTLY into exercise_localizations.** The owner confirmed that the gap-fill fields and chunks of non-English languages are not used by the app.
28. **Translate ALL 10,283 exercises into de/ua/es/fr/tr/hu:** the 2,015 selected first, then the rest.
29. **Check the 4,064 selected SK and CZ sentences for grammar errors and FIX them at once**, with backup.
30. **Fix the punctuation defects found in Wave 1 Part A.**

## Decisions for the Spanish re-measurement (22 Sept 2026, Wave 1 es brief)

31. **Spanish is re-measured with the packet-level fix:** 8 shuffled judge packets instead of 4 (still ONE judge prompt, shuffled across levels, 80 hidden duplicates in different sessions); after each session the returned jid set is checked and a deterministic follow-up session judges the MISSING jids only, with the same prompt, merged; cap 2 follow-ups per packet. Every packet is an Opus subagent (decision 26).
32. **Grammatical gender decides:** a grammatically masculine source noun (e.g. "спортсмен", "el atleta") is "he"; "she" is wrong. Decision 22 covers only sources that mark no gender at all.
33. **An ADDED interjection (e.g. "Wow", "Bro") is NOT an error**, mirroring the rule that a dropped interjection is not an error. Added content of any other kind stays an error. This changes the JUDGE prompt only; the checker prompts stay byte-identical (the checker already accepts these, so no re-measurement is needed).

## Decisions for the overnight deploy (22 Sept 2026, overnight deploy brief)

34. **The fast-start, reference-data cache, icon line weight, exercise-mix and typed-input fixes are deployed to the web.**
35. **Exercise mix:** a chosen exercise type may be mixed with other types so the 3-in-a-row rule and the build/typed opening can hold. Approved as built.
36. **Storage caching:** Words and Thumbnails get `max-age=31536000, immutable`; user-media gets `max-age=86400`.
37. **The scope restriction to the 4,064 selected exercises also applies to native de, ua and es learners of English.**
38. **Decision 32 (grammatical gender) stays in the JUDGE prompt only.** The checker prompts stay byte-identical and nothing is re-measured.
39. **The last 2 untranslated cells (40497 tr, 39286 hu) are fixed.**

## Decisions for the CDN / ua check / translate mix brief (23 Sept 2026)

40. **Purge the Cloudflare CDN copies of the Words and Thumbnails buckets** so the new Cache-Control takes effect now.
41. **The Ukrainian checker is sanity-checked offline** after the two live false rejections on exercise 1067.
42. **The translate format must appear more often for the routed natives** (sk, cz, de, ua, es learning English), while the "at most 3 of the same exercise in a row" rule keeps holding.
43. **Signed-URL caching for user-media is deliberately left unsolved for now.**

## Decisions for the cadence deploy / mismatch scan brief (23 Sept 2026)

44. **The CDN purge was run by the owner on 23 Sept 2026; verified on 10 files.**
45. **The translate cadence (at least 1 translate card in 6, rule "max 3 of the same kind in a row" intact) is deployed.**
46. **The selected 4,064 exercises are scanned in all six non-English natives for source/reference mismatches.** Report only, no fix in this run.

## Decisions for the mismatch fix brief (23 Sept 2026)

47. **All 303 confirmed mismatches are fixed:** the 174 Spanish pronouns, the 123 other native rows, and the 6 rows where the English is wrong.
48. **Spanish keeps the explicit subject;** only the wrong pronoun is corrected (not a restore from the Part 4 backup).
49. **Where the native sentence says something entirely different** (most of the Hungarian A1 series), it is re-translated from the English, not patched.
50. **The 440 native rows with an empty gap word stay as they are for now.**

## Decisions for the pronoun sweep / wave 2 brief (23 Sept 2026)

51. **A deterministic pronoun/person sweep runs over all 4,064 selected exercises in de, ua, es, fr, tr and hu;** what it finds is fixed with the same two-pass rule (one judge, an independent verifier, only rows both call wrong are fixed).
52. **Wave 2 (fr, tr, hu) is measured with the same method and the same targets as wave 1.**

## Decisions for the fr deploy / punctuation / tr-hu retry brief (23 Sept 2026)

53. **French is routed and deployed;** fr learners of English get the translate format only on the 4,064 selected exercises.
54. **Missing sentence-final punctuation is repaired in ALL nine languages, across the whole table,** not only the selection.
55. **Turkish and Hungarian are fixed and re-measured on NEW sets:** vocatives droppable, the genderless rule made effective, punctuation repaired.
56. **Rows where a native distractor equals the correct answer are NOT an issue:** the options are shown to the learner in English. No action, and this is not to be raised again.

## Decisions for the tr/hu deploy / 5 source fixes brief (23 Sept 2026)

57. **Turkish and Hungarian are routed and deployed.** All eight non-English natives (sk, cz, de, ua, es, fr, tr, hu) now use the SOURCE-ONLY checker, each restricted to the 4,064 selected exercises.
58. **Type-69 definition rows keep NO sentence-final mark, in every language, as the English rows do.** apply_type69.py is not run and the convention in validate_part.stem_sentence stays.
59. **Five broken source sentences are fixed:** tr 27060, tr 31993, tr 13301, hu 31482, hu 36905.

## Decisions for the new-exercises data groundwork brief (23 Sept 2026)

60. **Three new exercise types are being built:** Tinder (images, all learning languages), Listening and Speaking (videos only, English as the learning language only).
61. **Video voiceover transcripts go into the database;** they drive Speaking (which sentences are acceptable, subtitles) and Listening (eligibility and answer checking).
62. **Listening questions and their correct answers are pre-generated and stored,** so the runtime check is a fast comparison by Gemini.
63. **Speech recognition for Speaking uses Gemini** (the key already exists); pronunciation is judged leniently; audio is never stored.
64. **Tinder: no pair table.** At runtime one correct sentence for the image, or one sentence taken from a DIFFERENT word of the SAME level. Correct/incorrect ratio 50:50. Images: all styles. 30 s to start, +5 s per correct answer, no penalty for a wrong one, no upper limit, counts towards the streak.
65. **Background music for Tinder: royalty-free tracks from Pixabay,** several, played at random.

## Decisions for the widen-eligibility / more listening questions / music brief (23 Sept 2026)

66. **Eligibility is widened: a spoken line qualifies if it contains a FINITE VERB.** An explicit subject is no longer required, so imperatives and set phrases count ("Take me to the tower.", "Hold them like this, slowly."). A line with no verb at all ("Awesome!", "Two coffees.", sound markers) still does not qualify.
67. **Listening may have MORE THAN ONE question per video** where the transcript carries them (up to 3).
68. **Music: tracks 01 (upbeat electro), 02 (disco funk) and 05 (dance pop) are kept.** Tracks 03 and 04 are dropped.

## Decisions for the finish-the-three-new-exercises brief (23 Sept 2026)

69. **Tinder keeps +5 s per correct answer, with no upper limit and no XP cap.** Accepted as built.
70. **Listening and Speaking filter their videos by the learner's level (A/B),** the way Tinder does.
71. **The free listening check forgives ONE wrong letter in a word of 5+ letters (the speaking rule),** and the stored correct spelling is shown in green above the learner's answer whenever the two differ.
72. **Tinder, Listening and Speaking go live on the web.**

## Decisions for the UI fixes (bubbles) + cadence brief (23 Sept 2026)

73. **The new exercises appear much more often:** Tinder about once every 6 cards, Listening/Speaking about once every 4 cards, and the first of them inside the opening 5 cards.
74. **Bubble rule for the whole app:** text in the learner's NATIVE language sits in a WHITE bubble, text in the LEARNING language sits in a BLACK glass bubble, per the Figma designs.
75. **The translate input follows Figma 1623-1722:** a compact field, not the oversized bubble that was live.

## Decisions for the overnight brief: comment questions, exercise rebuild, translations (23 Sept 2026)

76. **The exercise set is rebuilt.** Choice, build, typed and translate stop being shown; their DATA STAYS untouched and the code paths stay behind one switch. Multiplayer is out of scope for now.
77. **Remaining exercises:** Tinder (images AND videos, all learning languages), Speaking-repeat, Comment (all learning languages, typed or spoken), Listening (English only, because the audio is English).
78. **Comment questions:** one OPEN question per media per level (A and B), from the asset description, max 70 characters, written in English and translated into the other 8 languages.
79. **Tinder has NO timer, NO rounds and NO music:** one sentence per card. The music files and the audio bucket stay, unused.
80. **Tinder may appear in runs of up to 8 cards;** the max-3 rule no longer applies to it. Other kinds keep it.
81. **Comment answers are stored from the start** (not shown to anyone yet) and are checked for grammar AND for whether they fit the media. Limit 60 words.
