# Phase 2K progress

## Plan (orchestrator, 21.9.2026)
Stages S1 setup+Part1+Part2 (0 calls) -> S2 Part3 closed-set re-score (<=1,800 Gemini, safety stop FA>8%) -> S3 Part4 Czech stack (0 calls) -> S4 Part5 set+writers+judge (headless) -> S5 run+analysis -> S6 report.
Token projection (2,200,000 budget): S1 ~250k, S2 ~150k, S3 ~200k, S4 ~250k agent + ~800k headless, S5 ~150k, S6 ~120k, orchestrator ~100k = ~2.02M.

## S1 - setup + Part 1 + Part 2 (21.9.2026; 0 Gemini calls, 0 headless tokens)
- SHA_before.txt: 3,744 files, generator phase2k/sha_tree_2k.sh = phase2i/sha_tree.sh's pipeline with the prune moved to
  phase2k (so phase2i AND phase2j are covered; phase1p dirty pair + untracked phase2d/run_2d_cz.stdout.txt are baseline).
- Byte copies from phase2j: run_2i_base.py (transport), write_guard.py, adapter_2f.py, f4fix.py. Ledger GEMINI_LEDGER.json {"S1": 0}.
- §1.1 ruling verbatim (stack_source.RULING, asserted == BRIEF_2K.md 1.1 text in T10) in spec/: judge_prompt_{sk,cz}.txt (2I/2J
  judge prompt + ruling bullet after the dropped-word rule), writer_template_{sk,cz}.txt (2J TEMPLATE + ruling before
  "Sentences:"), l3_system_{sk,cz}.txt + l3_user_{sk,cz}.txt. CZ = Slovak->Czech / slovak->czech BEFORE inserting the ruling.
  NOTE for S4: the judge prompt still has "a dropped function word is correct, a dropped content word is wrong"; the ruling follows it.
- §1.2 restored (upload/RESTORE_4.json, B3 'before' == phase2i value): 41408 "...slumped onto desk." -> "...onto her desk.";
  927 "...before a." -> "...before a trust fall."; 35040 "He shares his ice cream with." -> "...with his friend.";
  22385 "...in front of." -> "...in front of the happy man." (all v[0]; en updated).
  Ending test (build_upload.scan_endings, T8) over SK final + CZ phase2i/upload: STRICT list = articles + of/onto/into/upon/among/
  between/beneath/via/despite/during/than/toward(s)/to/from/with/at/by -> 2 hits, both ex 4146 (sk+cz) "...every move she is
  thinking of." = legitimate stranded preposition, recorded in analysis/ref_endings_reviewed.json (T8 fails on any other hit).
  Broad list (particles/stranded: up, in, on, for, before, out ...) 219 hits (SK 117, CZ 102), all in analysis/ref_endings.json,
  NOT asserted (e.g. "the sun went down", "what the room is for") - orchestrator may overrule this split.
- §1.3 upload/upload_sk_final.xlsx (sheet sk, 2I columns) + annotations_sk_final.jsonl + UPLOAD_README.md: 4,064 rows,
  exercise_id int, v[0]==en, "v is display-only and no longer grades" (T9).
- Part 2 stack_source.py (SOURCE-ONLY, in-process): guards AG -> F4v2 -> F4v3 pre-L3, everything else -> L3 with ONLY
  {language, source, answer}; SAME accept, TIP reject, DIFF reject; gemini-3.1-flash-lite, temp 0, thinkingBudget 0, maxOutputTokens 24.
  Removed layers (file:line in the 2J stack; full grep with line numbers: analysis/REMOVED_LAYERS_GREP.md):
  | layer | where (2J path) | reads |
  |---|---|---|
  | L1 exact-reference accept | phase1i/checker_1i.py:822-824 (base.route -> phase2j/tonly/lib_prev.py route) | v / refs |
  | F3 deletion | checker_1i.py:799-803 | reference |
  | F5 adjunct deletion / subsequence | checker_1i.py:804-809 (_subseq_positions :669, loop :719) | v |
  | L2 mistake / F1 / F2 + LOCKTIP | checker_1i.py:827-840, 299-300, 319-372; phase1k/runner_1k.py:248-268 | locks (lk; already stripped in 2I) |
  | L3 verdict map | checker_1i.py:841-850 (replaced by stack_source.finish) | - |
  | F2B | checker_1i.py:851-858 (f2_boundary_violation 773-795; en_span_tokens 1548-1568) | alt |
  | P-FROZEN L3 body | phase2j/tonly/lib_prev.py:223 SYS "same as the reference", :230 "Reference English:"; GROUND/WORDING/VOICE/lever2/3/ARTICLE lines | reference, v[0] |
  | records reference=v[0], refs=v | phase2j/tonly/runner_1p.py build_side (CONTEXT 1.2: :153) | v |
  | AGv5 refsubj rs_nom | phase1v/trackA_loop/stack_1v.py:43-99 (call :99), final_accept :137-144 | reference |
  | TIPdet rule | stack_1v.py:122-134, applied :144 | reference |
  | AG v4 clause alignment | runner_1u ag_map_1u passes r['reference'] -> agent_drop_v4.py:290 -> agent_drop_v3.py:386/:442/:269 split_en(reference) | reference |
  AG / F4 reference check: AG READS the reference on every call (probe with reference=PoisonVal: 900/900 reads per set, at
  agent_drop_v3.py:269 split_en). REMOVED: AG = stack_1w.decide called directly with reference='' and extra=() (runner_1u's
  AG_CFG['primary'] object forwards to it but has no extra=), annotation stripped of v/alt/en/lk*/headword/rewrite.
  Effect vs the 2J stack's own AG on the same items: 2I set 892/900 agree, 2J set 895/900 (list: analysis/s1_prep.json ag_disagree;
  e.g. A:250:c3, A:1033:c3, A:3147:c5 no longer AG-rejected; A:262:c2, A:352:m newly fire).
  F4v2/F4v3 (2J-fixed via f4fix.build_fixed_v3) read only {sk, answer}: fed a PoisonDict with only those keys, 0 errors,
  0 hits on 1,800 items; 0 F4 fires on either set (2J stack also 0). F4v3 moved pre-L3 (2J ran it after L3; label-only effect).
- run_2k.py: 2J transport (run_2i_base copy), --lang sk|cz, cap 3,000 - other stages, spend $1.00, resume, --seed-ledger,
  --expect-needed, relative paths REFUSED (exit 2); claude spawner = phase2j/run_2j.py:154-265 verbatim. Czech: load('cz')
  is REFUSED until S3 assembles cz_reader + f4fix cz (L3 text for Czech already exists: S.sys_text('cz')).
- test_2k.py (real path, HTTP / spawn mocked): RESULT 13/13 PASS; mocked calls 71; real model calls 0. T1 jid 429 + 200-reply "429", T2 real 429
  envelope, T3 per-day usage envelope STOP, T4 resume 0 cost, T5 relative refused, T6 poison v/alt/lk/en + body = source+answer
  only, T7 cap, T8 endings, T9 upload, T10 ruling, T11 headless 429/usage, T12 routing, T13 SHA. (First run 11/13: T6 was an
  apparatus bug - it compared one item's reference against ALL bodies, where another item's answer equals it; fixed per body.)
- Freeze: FROZEN_SHA_S1.txt, FREEZE_COMMIT_S1.txt = e394bc2417e8b54f81396c27e57092288c61a5b5.
- Gemini calls: S1 0, cumulative 0 of 3,000. Headless tokens 0. SHA check S1: SHA_diff_S1.txt 0 lines.
- NEXT (S2), 0-call prep in analysis/s1_prep.json. Items reaching L3: 2I set 896 (4 AG-rejected: 3 correct, 1 wrong),
  2J set 892 (8 AG: 3 correct, 5 wrong); unique requests 896 / 892 = 1,788 calls. Commands (absolute, nohup, sequential):
  PYTHONDONTWRITEBYTECODE=1 nohup python3 -B /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2k/run_2k.py gemini --lang sk --set /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2i/set/items.jsonl --run-dir /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2k/run_S2_2i --stage S2_2i --expect-needed 896 --purpose "Phase 2K S2 closed-set re-score 2I" > /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2k/run_S2_2i.stdout.txt 2>&1
  PYTHONDONTWRITEBYTECODE=1 nohup python3 -B /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2k/run_2k.py gemini --lang sk --set /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j/partD/set/items.jsonl --run-dir /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2k/run_S2_2j --stage S2_2j --expect-needed 892 --spend-dirs /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2k/run_S2_2i --purpose "Phase 2K S2 closed-set re-score 2J" > /Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2k/run_S2_2j.stdout.txt 2>&1
  Labels: items carry judge_label (2I 497 correct / 403 wrong; 2J 498 / 402); label files phase2i/judge/labels.jsonl and
  phase2j/partD/judge/labels.jsonl (key aid == item jid; their 'jid' is the judge packet id). Reference-based comparison rows:
  2I 89.13/4.71 = phase2i/run/results.jsonl rows with stack=='tonly'; 2J 90.36/5.97 = phase2j/partD/run/results.jsonl;
  2J fixed stack on the 2I set = phase2j/run_S2c/results.jsonl. 2J's 25 reference-caused FRs: phase2j/analysis/numbers.json / ANALYSIS.md.
  Results: <run-dir>/results.jsonl (accept, layer AG|F4v2|F4v3|L3|L3:TIPrej|L3:failed, guard fields, l3_reply).

## S2 - Part 3 closed-set re-score (21.9.2026; Gemini 1,788 calls, 0 headless tokens)
- FROZEN_SHA_S1 verified OK before running; test_2k.py re-run 13/13 PASS (test_2k_output_S2.txt). Runs via run_S2.sh (nohup, sequential):
  run_S2_2i/ (896 calls, COMPLETE), run_S2_2j/ (892 calls, COMPLETE), 0 uncounted attempts, 0 poison hits. Spend $0.1816 (S2).
  New-stack layers: {"2I": {"L3": 756, "AG": 4, "L3:TIPrej": 140}, "2J": {"L3": 769, "L3:TIPrej": 123, "AG": 8}}.
- Reference-based rows reproduce exactly: 2I 443/497 = 89.13 % / 19/403 = 4.71 %; 2J 450/498 = 90.36 % / 24/402 = 5.97 %.
- SOURCE-ONLY: 2I cov 477/497 = 95.98 % [93.85, 97.52], FA 37/403 = 9.18 % [6.55, 12.43];
  2J cov 474/498 = 95.18 % [92.91, 96.89], FA 36/402 = 8.96 % [6.35, 12.18];
  POOLED cov 951/995 = 95.58 % [94.11, 96.77], FA 73/805 = 9.07 % [7.18, 11.27] (ref-based pooled 89.75 % / 5.34 %).
  Pooled per level: A1 cov 231/248 = 93.15 % [89.25, 95.96] FA 7/202 = 3.47 % [1.40, 7.01] ; A2 cov 240/250 = 96.00 % [92.77, 98.07] FA 16/200 = 8.00 % [4.64, 12.67] ; B1 cov 237/247 = 95.95 % [92.68, 98.04] FA 25/203 = 12.32 % [8.13, 17.64] ; B2 cov 243/250 = 97.20 % [94.32, 98.87] FA 25/200 = 12.50 % [8.26, 17.90].
- 182 verdicts changed: FR removed 2I 51 / 2J 40, FR added 17 / 16,
  FA removed 7 / 7, FA added 25 / 19 (net FA +30). 2J's 25 reference-caused FRs: 25/25 now accepted.
  FA added by writer type: {'M': 35, 'T': 5, 'S': 3, 'W': 1}. Every changed item with mechanical cause + earlier cause label: analysis/part3.md.
- SAFETY STOP FIRED: pooled FA 9.07 % > 8.0 % -> STOP_part3.md written. Per the brief: no Czech (S3-S5 not run); the orchestrator writes the report.
- Files: run_S2.sh, analyze_part3.py, analysis/part3.md, analysis/part3.json, run_S2_2i/, run_S2_2j/, run_S2_*.stdout.txt, STOP_part3.md,
  SHA_after_S2.txt, SHA_diff_S2.txt.
- Gemini calls: S2 1,788; cumulative 1,788 of 3,000. Headless tokens 0. SHA check S2: SHA_diff_S2.txt 0 lines.

## S6 - report (21.9.2026; 0 Gemini calls, 0 headless tokens)
- Report written: /Users/kristiansurhanak/Projects/and-again/docs/features/reports/TRANSLATION_PRODUCTION_PHASE2K_REPORT.md
  (and-again commit c61be3c, not pushed); copy at phase2k/TRANSLATION_PRODUCTION_PHASE2K_REPORT.md.
- Headline: Czech NOT measured (Part 3 safety stop, pooled FA 9.07 % > 8.0 %); Parts 4 and 5 not run; no Czech upload; 0 Claude tokens on Czech.
- FA-rise diagnosis in the report: 44 FA added (M 35), 9 formerly caught by removed F3 (6) / F5 (3), 3 by ref-reading AG, 2 by F4v2 path,
  30 by the reference comparison inside L3; mostly dropped content words the §1.1 ruling calls WRONG. Judgement: SK file fit as display
  data; grading should not switch to SOURCE-ONLY until a source-side dropped-content guard exists.
- Gemini calls: S6 0; cumulative 1,788 of 3,000 ($0.1816). Claude tokens (harness): S1 201,462, S2 56,806, S6 ~75,000 est,
  orchestrator ~60,000 est = ~393,000 of 2,200,000; headless 0. (TOKENS.jsonl S1/S2 rows are pre-harness estimates.)
- SHA check S6: SHA_diff_S6.txt 0 lines.
