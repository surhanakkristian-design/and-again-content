# Phase 2I — CONTEXT (stage 1 technical map; later stages rely on this instead of re-reading sources)
Paths relative to `~/Projects/and-again-content/translation-offline/` unless stated. Line numbers verified 21.9.2026.

## 1. The frozen 1W stack
### 1.1 Files (closure = phase1w/a4/run/MODULES_1U.txt + score_1u.py; FREEZE_FILES/FREEZE_HASH/RUN_COMMIT in phase1w/a4/run/)
Entry `phase1w/stack_1w.py` (27 lines) -> `phase1v/trackA_loop/stack_1v.py` (AG v4 + v5 `rs_nom` refsubj + TIPdet rule; `final_accept` 222-231) + `phase1w/reader_nom.py` (agent reader v6; loads phase1n/f9.py, phase1i/checker_1i.py via importlib).
Runner `phase1w/a4/run/runner_1u.py` (copy of phase1u/runner_1u.py + PATCH_RUNNER at 703-746: AG primary = stack_1w.decide, build_rows wrapped by stack_1w.final_accept). Driver `phase1w/a4_driver_1w.py` (setup/copy/patch 60-160, freeze 360-400, then `runner_1u.py --final --data-dir phase1w/a4/data`).
Imported chain (all used): phase1i/{checker_1i,lib_prev,pipeline_1i,reference_hygiene}.py, phase1i/taskB/{lock_fix,backfill_s_ids}.py, phase1i/taskC/guards_c.py, phase1j/{loader_1j,taskA/p_chain,taskC/runner_1j}.py, phase1k/{loader_1k,runner_1k}.py, phase1n/{f8,f9,loader_1l,loader_1n,runner_1l,runner_1n}.py, phase1p/{lever1,lever2,lever3,loader_1p,runner_1p}.py, phase1s/{safe_json,taskC/agent_drop_v2}.py, phase1t/{run/loader_1t,run/runner_1t,taskA/agent_drop_v3}.py, phase1u/taskA/agent_drop_v4.py, phase1v/trackA_loop/stack_1v.py, phase1w/{reader_nom,stack_1w}.py, phase1w/a4/run/{runner_1u,loader_1u,article_line_1u,score_1u}.py.
WARNING: importing this chain writes loader access logs when data is loaded; always run with `python3 -B` / PYTHONDONTWRITEBYTECODE=1 and copy, never run in place, to keep earlier phases byte-identical. (phase1p/access_log.jsonl + run_1p.log were already dirty in git since 19.9, before 2I; SHA_before includes that state.)

### 1.2 Verdict pipeline (actual code order)
1. Records: `runner_1u.build` (391) -> `runner_1t.build` (186-192) -> `runner_1p.build_side` (134-197): `locks` from annotation `lk` (150-152), `reference = v[0]`, `refs = v` (153), `lock_ok` (167) + `checker_1i.lock_equivalent_ok` (169-171; patched by phase1i/taskB/lock_fix.py 154-181). `chk` computed by `runner_1l.compute_chk` (L1 offline checker; `step=='mistake'` = library-mistake L2, NOT a lock).
2. AG (pre-L3, 0 calls, final): `runner_1u.ag_map_1u` 192-213 -> PATCH `_AG1W.decide` -> `stack_1w.decide` (AG v4 all flags + rs_nom, reader_nom v6). AG-rejected items are not planned for L3 (`plan_ids` 402).
3. `runner_1p.decide` 222-229 -> `runner_1k.guard_readouts` (F8/F9 readouts; F9 READS lk, f9.py:497-501; neither decides) -> `runner_1k.configure_row(st, recs, vm, locktip=True, guards, False, False, tip_reject=True)` 438-446 -> `pipeline_1i.run_pipeline` 130-150 with ROW7_FLAGS (pipeline_1i.py:31: F1,F2,F3,F4v2,F5,F2B on).
4. Decide = `runner_1k.locktip_decide` (248-268) wrapping `checker_1i.decide` (802-865). Inside decide, order: F3 (804) -> F5 (809) -> F4v2 (815) -> `lib_prev.route` (827; lib_prev.py:122-129: L1 accept / L2 mistake / L2 lock `if not it['lock_ok']` 127-128) -> L2 branch 832-845 (mistake rejects 833; F1 `f1_lock_ok` 837 [reads locks, 299-300]; F2 `f2_equivalent` 839-842 [reads locks, 319-368; tip text `f2_tip` 372 "use the target structure"]) -> L3 verdict map 846-855 (DIFF reject; TIP/SAME accept; correct_with_tip if tip or TIP) -> F2B 856-864.
   NOTE: brief's order "L1, AG, F3, F4v2, F5" differs from code: F3, F5, F4v2 run BEFORE L1 inside decide; AG sits before all of it (separate map).
5. LOCKTIP (runner_1k.py:248-268): if decide returns L2 non-mistake reject and item has locks -> re-decide with `locks=[]`, `lock_ok=True` (259); if still L2 keep the rejection (261-262), else attach `lock_tip` (264) + `released_from_lock` (265). `lock_tip` is a label only; it does not create a TIP verdict.
6. TIP-as-rejection: pipeline_1i.py:343-346 (`tipped = acc and model=='TIP'` -> `L3:TIPrej`).
7. runner_1u PATCH build_rows (733-744) -> `stack_1w.final_accept` -> stack_1v.final_accept 222-231: AGv5 `refsubj` rs_nom rejection of accepted rows; `tip_det_rule` (215-219) overturns `L3:TIPrej` when the answer differs from the reference only by a determiner swap and the Slovak has no demonstrative.
F8/F9 do not decide (FROZEN_CONFIG_1U.json). Lever 2/3 lines (phase1p/lever2.py, lever3.py) are inserted into the prompt via `r['_extra']`.

### 1.3 Every `lk` read (verdict path of 1W)
- phase1p/runner_1p.py:150-152 (hy['lk'] -> locks), 159 (`'locks': lk`), 167 (lock_ok), 168-171 (lock_equivalent_ok) — THE source of all lock state.
- phase1i/pipeline_1i.py:105-106 (`to_item` copies locks/lock_ok/lock_released_2_1).
- phase1i/lib_prev.py:127-128 (route -> L2 lock veto).
- phase1i/checker_1i.py:299-300 (f1_lock_ok), 319-368 incl. 322-325 (f2_equivalent), 372 (f2_tip), 837 (F1 in decide), 1493-1526 (_lock_is_non_verb / lock_equivalent_ok), 1539-1542 (lock_ok patch site).
- phase1i/taskB/lock_fix.py:59-181 (lock equivalents; replaces C.f1_lock_ok / C.lock_equivalent_ok).
- phase1k/runner_1k.py:258-264 (LOCKTIP).
- phase1n/f9.py:497-501 (F9 readout: reads a['lk'] -> 'practised structure not used'; readout only, no verdict effect).
- Not in the 1W path (other phases' builders / fixtures): checker_1i.py:1601-1615 (load_fresh), lib_prev.py:98-112, runner_1k.py:368-387, runner_1l.py:245-264, runner_1n.py:206-229, runner_1p.py:287-291 (lever-1 path, lever 1 removed), fixtures runner_1p 459/465, runner_1t 554-563.
AG modules (agent_drop_v2/v3/v4, reader_nom, stack_1v, stack_1w) read NO lk (grep, 0 hits).
Count: 9 files with lk/lock reads in the live 1W path (runner_1p, pipeline_1i, lib_prev, checker_1i, lock_fix, runner_1k, f9 + F1/F2 via checker) — 1 place turns annotation `lk` into `locks` (runner_1p.py:150-152); everything else reads `locks`/`lock_ok`.

### 1.4 F2B (checker_1i.py:773-795 `f2_boundary_violation`, applied at 856-864)
Reads NOT lk but `it['topic']` (cont_topic: 'continuous'/'progressive' in topic, 784-785) plus Slovak span markers SK_SPAN/SK_ONGOING and `en_span_tokens` (annotation p/alt, 1548-1568). Fires only when out['accepted'] and verdict=='correct_with_tip'. Under LOCKTIP+TIPrej the only correct_with_tip source is model TIP (F2 tip needs L2 branch), which TIP-as-rejection rejects anyway -> removing F2B never changes accept/reject BY ITSELF, it only relabels F2B -> L3:TIPrej; BUT stack_1v.tip_det_rule overturns only layer 'L3:TIPrej', so an F2B item can become TIPdet-accepted after removal. Record this interaction.

### 1.5 The L3 prompt (P-FROZEN-1U, used by 1W unchanged)
System: phase1i/lib_prev.py:225-228 (`SYS`, via pipeline_1i.sys_text 'P-E4b'): "You judge English translations. Reply with exactly one word: SAME, TIP or DIFF. SAME = the learner sentence means the same as the reference and is correct English. TIP = same meaning and acceptable, but with a small slip. DIFF = different meaning, or not correct English. No explanation."
User body: `pipeline_1i.pb_lines` -> checker_1i.prompt(it,'P-B') (57-63) -> lib_prev.prompt (231-237): `Slovak:`, `Reference English:`, `Learner:`, then line 234-235, then [gender line phase1i/pipeline GENDER_TMPL if any] + GROUND_LINE + WORDING_LINE (runner_1k.build_req 49-61), then runner_1u.build_req_1u 81-93 inserts after WORDING_LINE: VOICE_SAME_LINE (runner_1n) + lever2/3 `_extra` + ARTICLE_LINE_1U (article_line_1u.py:18), tail `SAME, TIP or DIFF?`.
**The practised-grammar / already-verified line EXISTS** — phase1i/lib_prev.py:234-235, quoted exactly:
`'Practised grammar: %s — ALREADY VERIFIED as correct in this answer; judge meaning and vocabulary only.' % it['topic']`
(rendered e.g. "Practised grammar: Used to, Would — ALREADY VERIFIED as correct in this answer; judge meaning and vocabulary only."). `%s` = the exercise TOPIC (type_title), not lk. It is on every L3 call of 1W. This is the line the owner's decision removes. Also recorded (not changed): SYS says "means the same as the reference", while GROUND_LINE says judge against the Slovak.
Generation config (pipeline_1i GEN_CFG): `{'temperature': 0, 'maxOutputTokens': 24, 'thinkingConfig': {'thinkingBudget': 0}}`, model `gemini-3.1-flash-lite`, API base `https://generativelanguage.googleapis.com/v1beta` (lib_prev.API). Reply = bare token SAME/TIP/DIFF.
Other lines, verbatim: GROUND_LINE "The SLOVAK sentence is the ground truth and the English reference is only one valid rendering of it; judge the learner against the Slovak, not against the reference wording." WORDING_LINE "A synonym, a different word order or a different phrasing that keeps the Slovak meaning is SAME; a word that changes which thing, person, place, time or quantity the Slovak names is DIFF." VOICE_SAME_LINE "Voice: if the Slovak names an agent in the nominative and the learner sentence moves that agent out of subject position or drops it (an active Slovak sentence turned into an English passive), that is SAME, provided the meaning is preserved. Where the Slovak is itself impersonal or passive, an English passive is SAME." (AG does the agent-drop rejection before L3.)

### 1.6 Gemini transport of the 1W runner
`runner_1n.make_calls` 332-369: key = `RL.load_keys()[0]` (free tier first), per-request `RL.call_one` (phase1n/runner_1l.py); key parsed at runtime from `~/Projects/and-again/.env.local` line `GEMINI_API_KEY` (lib_prev.py:36-51), redacted in logs (64-65), 401/403 -> key invalid (190). counted = HTTP 200 only; http 0/429/5xx retried with backoff, logged counted:false; empty 200 = counted failure, never retried. ThreadPool 6 workers, shuffled Random(1); 5 consecutive failed requests = quota wall. Requests keyed by `runner_1j.req_hash(sys,user,gcfg)`; ledger `phase1w/a4/run/calls.jsonl` (+ mirror to phase1w/a4/ledger_dev.jsonl); resume = stored replies by hash are reused (0 cost). Cap 800 (PATCH).
Inputs (data dir, loader_1u): `sentences.json` [{sid, pid, slovak, level, topic, tags{...tf_gold...}}], `annotations.json` {sid: {v, lk, alt, voice/voice_sk, agent_nom, tf/tf_gold, ... (flat or under 'hygienised')}}, `items.json` [{id 'C:sid:c1'|'W:sid:w1', sid, kind, intent, form, tags, passive, answer}], `labels.json` {item_id: {judged, type, borderline, confidence, packet_part, packet_position, passive, tip, dropped, qid}}.
Outputs: run/results_1u.json `rows` (keys: ag, ag_shadow, answer, borderline, call_failed, call_failed_detail, confidence, dropped, final_accept, final_layer, form, half, intent, item_id, judge_passive, judged, judged_type, kind, layers, level, lever2_fired, lever3, packet_part, packet_position, reference, sid, sk, stack_in, tags, writer_passive), run/verdicts_1u.json (item -> SAME/TIP/DIFF = the L3 reply), run/calls.jsonl (raw lines), score_1u.json/SCORE_1U.md, FINAL_RUN_DONE, access_log.jsonl.

## 2. 2H tested-runner recipe (phase2h/run_2h.py, test_2h.py; Claude headless, not Gemini)
- Binary: `BIN = ~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude` (run_2h.py:36).
- Token: `load_token()` 590-595: `subprocess.run(["zsh","-ic",'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'])`, stored in ENV (copy of os.environ); only "present/ABSENT" logged; `_redact` 495 strips `sk-ant-…`.
- Spawn: `spawn_claude` 597-601: `[BIN, "-p", prompt, "--output-format", "json", "--max-turns", "12", "--model", MODEL]` (MODEL = opus), env=ENV, capture_output, text, no stdin, timeout WALL_CAP_S.
- Usage: `usage_total(m)` 237 = input_tokens + cache_creation_input_tokens + cache_read_input_tokens + output_tokens from the JSON envelope `usage`; per-session ledger ledger_2h.json with reservation (inflight_est) vs CAP before spawning (run_session 626-715, TOKEN-CAP stop 646).
- Classification `classify(rc, stdout, stderr)` 557-590 from `parse_envelope` (516) + `_error_fields` (540): usage limit = USAGE_RE (511-512: usage limit|hit your limit|weekly limit|5-hour limit|out of extra usage|credit balance is too low|limit will reset|resets at|quota) applied to the envelope ERROR message -> `hard_stop` STOP_usage_limit.md (497-509, GLOBAL_STOPS 56); rate limit ONLY if HTTP status 429/529 or error type in {rate_limit_error, overloaded_error} (575) -> retry with backoff_s 603 (min(600, 30·2^n)·jitter). "A '429' inside the result text or stderr is never looked at." First session failing (non-rate) -> STOP_first_session_failed.md.
- Resume: sessions written to sessions/<sid>.json; `sess_complete` 612 / `ann_complete` 862 skip finished sessions at 0 cost; `global_stop()` 479 checks stop files.
- Tests (test_2h_output.txt): T2 "rate limit only from the envelope - real 429 envelope retried; 429 only in text/stderr -> 1 call", plus stop-file scoping, resume, end-to-end with mocked model. Reuse the pattern: mock `spawn_claude` / `call_one`, not the classifier.

## 3. Data
### 3.1 phase2d/out/annotations_sk_final.jsonl — 4,064 rows; A1 1,174 · A2 1,220 · B1 885 · B2 785
Fields: agent_nom, alt, concept_id, correct_answer_src, embedded_agents, **en** (English), **exercise_id** (int, unique), exercise_type_id, field_sources, flags, fragment, gender, headword, language_code 'sk', **level**, **lk** (list), lk_reason, lk_supplied, lk_verdict, main_sentence_index, **n** (SK 1..4064; CZ 4065..8128), number, perfective_present, person, rewrite, script_reader_agent, script_voice_paths, **src** (the Slovak text), subject, tense_open, **tf** (time frame), **type_title** (= topic), **v** (list of English references), voice.
No `sid`/`topic`/`sk` fields: sentence = `src`, topic = `type_title`. SK: every v non-empty and v[0]==en (Part 0). CZ twin: phase2h/out/annotations_cz_final.jsonl, same schema, 4,064 rows.
### 3.2 Exclusions
- 2F probe (p3.1): 60 sentences, pseudo-sids 220001-220060 (`probe_result.json` "sids": [220001, 220060], seed 20260921, 15 per level). Production identity = the Slovak text: `phase2f/p3/probe/data/sentences.json` [{sid, pid 'P31001'…, slovak, level, topic, tags}] (also set/selection.json). Exclude by `src == slovak` (all 60 found verbatim in annotations_sk_final).
- 2G Part A re-used the SAME 60 (phase2g/partA/data/sentences.json, 60 hits).
- 1T/1U/1W and every phase1* set: 0 production SK sentences found (string search of all phase*/ json/jsonl). The only other hits are Czech files where a Czech sentence equals a Slovak one (≤7 strings) — not test sets.
- So exclusion set = the 60 probe sentences only.
### 3.3 2F probe results (for §4.9)
`phase2f/p3/probe/run/results_1u.json` rows (360 = 182 judged correct + 178 wrong; fields as §1.6); false rejections = judged=='correct' and not final_accept: **28** — by layer L3 16, F4v2 7, L3:TIPrej 5. FA 11. Labels: `data/labels.json` (judged, type, borderline, confidence, dropped, …) and judge verdicts `set/judge/verdicts_part1-4.json`; items `data/items.json`; references `data/annotations.json` (60 sids, v); L3 replies `run/verdicts_1u.json`; human-readable `run/SCORE_1U.md`.

## 4. Headline facts (as quoted in the brief / reports)
- 1W test: coverage 392/401 = 97.76 % [95.78, 98.97], FA 16/499 = 3.21 % [1.84, 5.15].
- 2F probe: coverage 154/182 = 84.62 % [78.54, 89.53], FA 11/178 = 6.18 % [3.12, 10.79]; judge noise 0/36 duplicate controls; types S 31 M 55 T 52 W 40; 312 counted calls, $0.0163; 8 headless sessions 547,613 tok; freeze 36a00a5, run commit e99e6b9.
- 2F judge blow-up: Part 2 `judge_s1` ran 13 turns, exit 1, 1,547,186 tokens (2F report line 38; Part 2 headless total 2,265,574).
- 1U: 20 false rejections = 12 determiner-tagged; by layer AG 1, L3 7, L3:TIPrej 12.
- 1S §5 (M1): F5 never sees Slovak; only free class NONINFO; dropping *also* rejected as "content word" (W:170116:w4).
- 2H: CZ 4,064/4,064; 50 CZ rows had empty v (n 5365-5414, lk2h_s01 range); exercise_id stored as text in the CZ xlsx; 2H headless used opus via the recipe above.

## 5. Upload files
- SK: `phase2d/out/upload_sk_final.xlsx` sheet `sk`, 4,064 rows; + `phase2d/out/annotations_sk_final.jsonl`.
- CZ: `phase2h/out/upload_cz_final.xlsx` sheet `cz`, 4,064 rows; + `phase2h/out/annotations_cz_final.jsonl` (older: phase2f/out 2,850 rows, phase2g/partB/out — superseded).
- Columns (both): exercise_id, language_code, level, src, en, structure_json (= the full jsonl annotation row as JSON, default json.dumps style, ensure_ascii False; identical to the jsonl row for all 4,064 in both languages).
- Part 0 result (phase2i/upload/): SK exercise_id already int (4,064), 0 empty v, 0 v[0]!=en; CZ exercise_id str on all 4,064 -> int, 50 empty v fixed (n 5365-5414), 0 v[0]!=en defects. No defects found.

## 6. Stage 2b additions (21.9.2026)
- Production rows reach both stacks through `phase2i/adapter_2f.py` (verbatim 2F adapter p3_probe.alt_dict/build_data; reproduces phase2f/p3/probe/data byte-identical, 60/60). Called in stack_frozen.from_2i; TONLY strips lk from the row before it (strip_row) and from the output after it (strip_lk). Shape adapter only; see TONLY_CHANGES 15.
- `phase2i/write_guard.py` redirects every write outside phase2i/ to `$P2I_RUN_DIR/_redirected/`. test_2i (z) asserts sha_tree.sh output identical before/after the suite AND equal to SHA_before.txt (3,256 files; phase1p access_log/run_1p.log unchanged since the baseline).
- Suite: 32/32 PASS (test_2i_output.txt). Frozen: FROZEN_SHA.txt, FREEZE_COMMIT.txt.
