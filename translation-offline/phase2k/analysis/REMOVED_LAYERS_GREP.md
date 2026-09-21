# Phase 2K - every reference-reading layer of the 2J stack (grep, line numbers as of 21.9.2026)

Removed from the SOURCE-ONLY verdict path unless marked KEPT. stack_source.py never imports the verdict code
below (it calls only AG and the fixed F4v2/F4v3 functions), so every reference read listed here is outside the path.

| layer | file:line | text |
|---|---|---|
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:121 | `def route(it):` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:124 | `return 'L1', 'checker verdict %s' % it['verdict']` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:398 | `l1 = len(rc['L1'])` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:399 | `real_fa = sum(1 for it in rw['L1'] if (it.get('fa_class') or '') not in ('tip-accept', 'valid reading'))` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:401 | `if l1 != 100 or len(rc['L1']) + len(rc['L2']) + len(rc['L3']) != 235:` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:408 | `% (l1, len(rc['L1']) + len(rc['L2']) + len(rc['L3']), real_fa))` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:440 | `print('  correct set (235): L1 %d / L2 %d / L3 %d' % (len(rc['L1']), len(rc['L2']), len(rc['L3'])))` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:442 | `% (len(rw['L1']), len(rw['L2']), len(rw['L3'])))` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:444 | `ba = Counter(it['wrong_type'] or '?' for it in rw['L1'] + rw['L2'] + rw['L3'])` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:446 | `b1 = Counter(it['wrong_type'] or '?' for it in rw['L1'])` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:502 | `l1 = len(rc['L1'])` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:512 | `m['fa_total_end_to_end'] = len(rw['L1']) + m['wrong_accepted']` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:551 | `% len(rw['L1']))` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:557 | `len(rc['L1']) + len(rw['L1']), 100 * (len(rc['L1']) + len(rw['L1'])) / tot,` |
| L1 exact-reference accept: route | phase2j/tonly/lib_prev.py:561 | `len(rc['L1']), 100 * len(rc['L1']) / 235, len(rc['L2']), 100 * len(rc['L2']) / 235,` |
| L1 accept inside decide | phase1i/checker_1i.py:827 | `lay, why = base.route(it)` |
| L1 accept inside decide | phase1i/checker_1i.py:828 | `if lay == 'L1':` |
| F3 deletion vs reference | phase1i/checker_1i.py:442 | `def f3_deletion(it):` |
| F3 deletion vs reference | phase1i/checker_1i.py:804 | `if flags.get('F3'):` |
| F5 adjunct deletion / subsequence vs reference | phase1i/checker_1i.py:658 | `def _subseq_positions(learner, ref, opt):` |
| F5 adjunct deletion / subsequence vs reference | phase1i/checker_1i.py:705 | `def f5_adjunct_deletion(it):` |
| F5 adjunct deletion / subsequence vs reference | phase1i/checker_1i.py:809 | `if flags.get('F5'):` |
| L2 mistake / F1 / F2 (locks from lk) | phase1i/checker_1i.py:299 | `def f1_lock_ok(it):` |
| L2 mistake / F1 / F2 (locks from lk) | phase1i/checker_1i.py:319 | `def f2_equivalent(it):` |
| L2 mistake / F1 / F2 (locks from lk) | phase1i/checker_1i.py:371 | `def f2_tip(it):` |
| L2 mistake / F1 / F2 (locks from lk) | phase1i/checker_1i.py:833 | `if it['step'] == 'mistake':` |
| L2 mistake / F1 / F2 (locks from lk) | phase1i/checker_1i.py:837 | `if flags.get('F1') and f1_lock_ok(it):` |
| L2 mistake / F1 / F2 (locks from lk) | phase1i/checker_1i.py:839 | `if not released and flags.get('F2'):` |
| F2B (reads alt en_span_tokens) | phase1i/checker_1i.py:773 | `def f2_boundary_violation(it):` |
| F2B (reads alt en_span_tokens) | phase1i/checker_1i.py:856 | `if flags.get('F2B') and out['accepted'] and out['verdict'] == 'correct_with_tip':` |
| F2B (reads alt en_span_tokens) | phase1i/checker_1i.py:1548 | `def en_span_tokens(it):` |
| ROW7 flags (F1,F2,F3,F4v2,F5,F2B) | phase2j/tonly/pipeline_1i.py:31 | `ROW7_FLAGS = {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 0}` |
| ROW7 flags (F1,F2,F3,F4v2,F5,F2B) | phase2j/tonly/pipeline_1i.py:135 | `d = st['decide'](it, dict(ROW7_FLAGS), vm)` |
| reference / refs into records | phase2j/tonly/runner_1p.py:112 | `ls, fired = lever2.open_points(r['sk'], a, r['reference'], r['answer'])` |
| reference / refs into records | phase2j/tonly/runner_1p.py:118 | `ln, shown, removed = lever3.line(r['reference'], r.get('refs'))` |
| reference / refs into records | phase2j/tonly/runner_1p.py:126 | `d = lever1.detect(r['sk'], a, r['answer'], r['reference'])` |
| reference / refs into records | phase2j/tonly/runner_1p.py:153 | `'band': R1N._band(s['slovak']), 'reference': refs[0], 'refs': list(refs),` |
| reference / refs into records | phase2j/tonly/runner_1p.py:719 | `r['reference'])['fired']}` |
| reference into checker item | phase2j/tonly/pipeline_1i.py:102 | `'level': r['level'], 'topic': r['topic'], 'sk': r['sk'], 'reference': r['reference'],` |
| reference into checker item | phase2j/tonly/pipeline_1i.py:207 | `if isinstance(r, str) and r.strip() and r.strip() != (it['reference'] or '').strip():` |
| P-FROZEN L3 prompt: SYS + Reference English line | phase2j/tonly/lib_prev.py:223 | `SYS = ("You judge English translations. Reply with exactly one word: SAME, TIP or DIFF. "` |
| P-FROZEN L3 prompt: SYS + Reference English line | phase2j/tonly/lib_prev.py:224 | `"SAME = the learner sentence means the same as the reference and is correct English. "` |
| P-FROZEN L3 prompt: SYS + Reference English line | phase2j/tonly/lib_prev.py:230 | `lines = ['Slovak: ' + it['sk'], 'Reference English: ' + it['reference'], 'Learner: ' + it['answer']]` |
| GROUND_LINE / WORDING_LINE | phase2j/tonly/pipeline_1i.py:40 | `GENDER_TMPL = ('Gender: the Slovak does not fix the gender here — the reference\'s {words} may equally be '` |
| GROUND_LINE / WORDING_LINE | phase2j/tonly/pipeline_1i.py:46 | `GROUND_LINE = ('The SLOVAK sentence is the ground truth and the English reference is only one valid '` |
| GROUND_LINE / WORDING_LINE | phase2j/tonly/pipeline_1i.py:49 | `WORDING_LINE = ('A synonym, a different word order or a different phrasing that keeps the Slovak meaning '` |
| LOCKTIP | phase1k/runner_1k.py:248 | `def locktip_decide(base_decide):` |
| L1 offline checker (chk) | phase1n/runner_1l.py:92 | `def compute_chk(r):` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:2 | `"""Phase 1P — LEVER 3: stored reference variants with a deterministic TIME-FRAME filter.` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:5 | `English rendering (checker_1i.prompt(it,'P-B') interpolates it['reference'] only; runner_1k.build_req` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:9 | `The lever shows the main reference plus up to 'CAP' further STORED renderings (annotation key 'v'),` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:10 | `equally ranked, and removes any variant whose time frame differs from the main reference's.` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:15 | `CAP = 2                                  # extra variants shown beside the main reference` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:60 | `def pick(reference, refs, cap=CAP):` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:61 | `"""(shown, removed) — stored renderings other than the main reference, tense-filtered."""` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:62 | `main = (reference or '').strip()` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:80 | `def line(reference, refs, cap=CAP):` |
| lever 3 prompt line (reads v[0]) | phase1p/lever3.py:82 | `shown, removed = pick(reference, refs, cap)` |
| lever 2 prompt line | phase1p/lever2.py:66 | `def open_points(sk, ann, reference, answer=None, cfg=None):` |
| lever 2 prompt line | phase1p/lever2.py:70 | `text = ' '.join(filter(None, [reference or '', answer or '']))` |
| lever 2 prompt line | phase1p/lever2.py:80 | `for w in toks(reference):` |
| AG gets r[reference]; build_rows / final_accept | phase1w/a4/run/runner_1u.py:201 | `dec = mod.decide(r['sk'], a, wt, r['answer'], r['reference'], 'primary', flags)` |
| AG gets r[reference]; build_rows / final_accept | phase1w/a4/run/runner_1u.py:449 | `def build_rows(recs, res, ag, planned, labels, hmap, failed):` |
| AG gets r[reference]; build_rows / final_accept | phase1w/a4/run/runner_1u.py:464 | `'sk': r['sk'], 'answer': r['answer'], 'reference': r['reference'],` |
| AG gets r[reference]; build_rows / final_accept | phase1w/a4/run/runner_1u.py:712 | `# built, stack_1w.final_accept(row) is applied to every row (TIPdet / AGv5), 0 calls.` |
| AG gets r[reference]; build_rows / final_accept | phase1w/a4/run/runner_1u.py:733 | `def build_rows(recs, res, ag, planned, labels, hmap, failed):` |
| AG gets r[reference]; build_rows / final_accept | phase1w/a4/run/runner_1u.py:738 | `acc, lay = SW1W.final_accept(r, ('rs_nom',), True)` |
| AGv5 refsubj rs_nom + TIPdet | phase1v/trackA_loop/stack_1v.py:43 | `def ref_subject_heads(sk, reference):` |
| AGv5 refsubj rs_nom + TIPdet | phase1v/trackA_loop/stack_1v.py:70 | `def refsubj(sk, answer, reference, extra=V5_EXTRA):` |
| AGv5 refsubj rs_nom + TIPdet | phase1v/trackA_loop/stack_1v.py:99 | `r = refsubj(sk, answer, reference, extra)` |
| AGv5 refsubj rs_nom + TIPdet | phase1v/trackA_loop/stack_1v.py:130 | `def tip_det_rule(sk, answer, reference, layer):` |
| AGv5 refsubj rs_nom + TIPdet | phase1v/trackA_loop/stack_1v.py:137 | `def final_accept(row, extra=V5_EXTRA, tip=True):` |
| AGv5 refsubj rs_nom + TIPdet | phase1v/trackA_loop/stack_1v.py:142 | `if refsubj(row['sk'], row['answer'], row['reference'], extra):` |
| AGv5 refsubj rs_nom + TIPdet | phase1v/trackA_loop/stack_1v.py:144 | `if not acc and tip and tip_det_rule(row['sk'], row['answer'], row['reference'], layer):` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:26 | `pass, guarded by the reference having a finite relative clause with an overt` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:30 | `'align'   CLAUSE MATCHER, class B.  v3 let ANY reference clause's subject count as "the agent is` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:31 | `rendered as that clause's own subject".  v4 admits the reference-clause subject as a` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:39 | `Guards: equal clause counts, the Slovak clause active and non-reflexive, the reference` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:40 | `clause active, and - for a PRONOUN reference subject - an overt Slovak pronoun in that` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:41 | `clause (this keeps Slovak pro-drop / 3pl impersonal clauses, whose reference reads` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:44 | `Public interface is v3's:  decide(sk, ann, wtags, answer, reference, variant='primary',` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:47 | `writer_tags, reference, answer); item tags of the measured set are never read.` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:163 | `def _reduced_relative(sk, ann, wtags, answer, reference, variant):` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:187 | `rt = toks(reference)` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:206 | `'reason': ('LEX/reduced-relative: %r renders the reference relative clause %r '` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:212 | `def _align_patch(sk, ann, wtags, answer, reference):` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:236 | `def _local_agent(sk, ann, wtags, answer, reference, variant):` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:242 | `skc, ansc, refc = V3.split_sk(sk), V3.split_en(answer), V3.split_en(reference)` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:260 | `continue                                   # the reference itself is agentless: licensed` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:277 | `'%r whose own agent the reference renders as %r' % (idx, skcl, head))}` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:282 | `def decide(sk, ann, wtags, answer, reference, variant='primary', flags=ALL_FLAGS):` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:285 | `return V3.decide(sk, ann, wtags, answer, reference, variant, V3_BASE)` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:288 | `al = _align_patch(sk, ann, wtags, answer, reference) if 'align' in flags else _Patch([])` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:290 | `d = V3.decide(sk, ann, wtags, answer, reference, variant, V3_BASE)` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:298 | `f = V3.decide(sk, ann, wtags, answer, reference, variant, ('subj', 'by'))` |
| AG v4 reference reads | phase1u/taskA/agent_drop_v4.py:305 | `r = fn(sk, ann, wtags, answer, reference, variant)` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:7 | `with an agent that lives in clause Y, and it read the reference's MAIN-clause subject as` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:8 | `"the agent rendered".  v3 splits the Slovak (commas), the answer and the reference` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:9 | `(commas + subordinators/coordinators), matches answer clause -> reference clause (token` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:13 | `multi-clause reference.  v3 reads the subject as the tokens before the FIRST unambiguous` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:22 | `Inputs stay SOURCE-SIDE only (Slovak, phase1p annotation, writer_tags, reference, answer).  The` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:188 | `- object renders the Slovak agent (PRON_EQ / reference subject head / proper name) -> agent` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:295 | `"""answer clause -> Slovak clause index. Order first; lexical anchors via the reference split."""` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:339 | `def v2_candidates(agent, reference):` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:340 | `"""v2's own candidate set (last token of the agent + PRON_EQ + last token of the reference` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:343 | `rs = V2.subject_tokens(reference)` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:382 | `def decide(sk, ann, wtags, answer, reference, variant='primary', flags=ALL_FLAGS):` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:385 | `return _decide_flat(sk, ann, wtags, answer, reference, variant, flags)` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:386 | `return _decide_clauses(sk, ann, wtags, answer, reference, variant, flags)` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:389 | `def _decide_flat(sk, ann, wtags, answer, reference, variant, flags):` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:392 | `return V2.decide(sk, ann, wtags, answer, reference, variant)` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:399 | `cands0 = (candidates(atoks, reference, True) if 'subj' in flags` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:400 | `else v2_candidates(agent, reference))` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:419 | `cands = cands0 or (candidates(atoks, reference, True) if 'subj' in flags` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:420 | `else v2_candidates(agent, reference))` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:431 | `def _decide_clauses(sk, ann, wtags, answer, reference, variant, flags):` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:442 | `skc, ansc, refc = split_sk(sk), split_en(answer), split_en(reference)` |
| AG v3 reference reads | phase1t/taskA/agent_drop_v3.py:452 | `for rc in (refc or [reference or '']):` |
| AG v2 reference reads | phase1s/taskC/agent_drop_v2.py:13 | `the sentence's writer_tags (nom_agent / agent), the reference and the answer. The writer's ITEM` |
| AG v2 reference reads | phase1s/taskC/agent_drop_v2.py:154 | `def decide(sk, ann, wtags, answer, reference, variant='primary'):` |
| AG v2 reference reads | phase1s/taskC/agent_drop_v2.py:182 | `rs = subject_tokens(reference)` |
| AG v2 reference reads | phase1s/taskC/agent_drop_v2.py:205 | `# name, sk, ann, wtags, answer, reference, expect_primary, expect_noun` |
| reader_nom | phase1w/reader_nom.py | 0 hits |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:55 | `"""Every English token the annotation sanctions for this sentence: all accepted references (incl. the` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:57 | `answers, the synonym group of each reference token.  STRUCTURAL: nothing is hand-listed here."""` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:59 | `key = (it['exercise_id'], it['reference'])` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:176 | `back as a separate delete and insert.  A deletion and an insertion within 'window' reference positions` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:257 | `# reference words differently ('private property', 'right now', 'the guard regrets it'), and F6` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:323 | `def sk_features_v3(sk):` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:339 | `def f4v3_subject_mismatch(it):` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:430 | `'set': 'NEW', 'level': 'A2', 'topic': topic, 'sk': sk, 'reference': ref, 'answer': ans,` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:440 | `# (guard, expect, sk, reference, answer, label)` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:508 | `'level': r['level'], 'topic': r['topic'], 'sk': r['sk'], 'reference': r['reference'],` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:580 | `lost.append({'id': iid, 'guard': g, 'answer': r['answer'], 'reference': r['reference'],` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:612 | `ref = _eff(it['reference'], opt)` |
| F4v3 (guards_c) | phase1i/taskC/guards_c.py:622 | `why = 'no diff against the reference (tense/form or writer artefact)'` |
| F4v2 (checker_1i) | phase1i/checker_1i.py:494 | `def en_subjects(text):` |
| F4v2 (checker_1i) | phase1i/checker_1i.py:536 | `def sk_features(sk):` |
| F4v2 (checker_1i) | phase1i/checker_1i.py:608 | `def f4v2_subject_mismatch(it):` |
| F9 readout (lk) | phase1n/f9.py | 0 hits |
| 2F adapter | phase2j/adapter_2f.py:32 | `for a in (ann.get('alt') or []):` |
| 2F adapter | phase2j/adapter_2f.py:57 | `hy = {'v': [x for x in (d.get('v') or []) if isinstance(x, str) and x.strip()],` |
| 2F adapter | phase2j/adapter_2f.py:58 | `'lk': [x for x in (d.get('lk') or []) if isinstance(x, str) and x.strip()],` |
| 2F adapter | phase2j/adapter_2f.py:59 | `'alt': alt_dict(d), 'id': sid, 'lv': r['level']}` |
