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
