import json, subprocess, os
P2J='/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'
R=json.load(open(P2J+'/partA/partA_result.json'))
a3=R['A3']; b=a3['before_2I']; a=a3['after_det']; A4=R['A4']; A5=R['A5']
f=lambda r:'%d/%d = %.2f %% [%.2f, %.2f]'%(r['x'],r['n'],r['pct'],r['cp95'][0],r['cp95'][1])
L=['# Phase 2J Part A — F4v2 subject-guard misfire (stage S1, 0 model calls)','',
'## A1 Diagnosis','Code path: `pipeline_1i.run_pipeline` -> `checker_1i.decide` (phase1i/checker_1i.py:815-820, flag F4v2 on via ROW7_FLAGS pipeline_1i.py:31) -> `f4v2_subject_mismatch` (checker_1i.py:608) -> `sk_features` (checker_1i.py:536). The misreading is in the present-tense ENDING heuristics of `sk_features`, checker_1i.py:552-563 (`-š` -> 2sg, `-me` -> 1pl, `-te` -> 2pl), whose only non-verb guards are `after_prep` = previous token is a preposition (checker_1i.py:542-544, one token back) and `SK_NOT_VERB` (checker_1i.py:526-527).',
'It is NOT reported speech, multi-clause structure or the wrong clause. In all 5 sentences a NOUN or ADVERB is read as a finite verb, the false feature is the only (or the agreeing) signal, and every 3rd-person answer pronoun then "clashes":','',
'| sid | false signal (2I) | why it is not a verb | features 2I -> fixed |','|---|---|---|---|']
why={250:'locative noun, `po vidieckej ceste` (adjective between preposition and noun)',1038:'adverb `príliš` (too)',1214:'locative noun, `v celom jeho živote` (two modifiers)',2461:'locative noun, `pri tomto plote` (demonstrative)',2989:'adverb `samozrejme` (of course)'}
for sid,v in sorted(R['A1'].items(), key=lambda x:int(x[0])):
    L.append('| %s | %s | %s | %s -> %s |'%(sid,', '.join(v['old_signals']),why.get(int(sid),''),v['old'],v['new']))
n44=sum(len(v['items']) for v in R['A1'].values()); nc=sum(1 for v in R['A1'].values() for i in v['items'] if i['judge']=='correct')
L+=['',"All %d F4v2 rejections of 2I sit on these 5 sentences (%d judge-correct = the 24 FRs, %d judge-wrong). None of the wrong ones is wrong because of its subject: they are m (dropped word), s (grammar), t (tense), w (word) variants whose pronoun is the same correct `he/she/it`. So F4v2 caught 0 real subject errors in 2I; the 20 'catches' were accidental."%(n44,nc,n44-nc),'',
'## A2 Fix (phase2j/f4fix.py; applied by phase2j/stack_tonly.py, P2J_F4FIX=1 default)','Two source patches of `sk_features`, bound only into `f4v2_subject_mismatch` (reader_nom / rs_nom keep the original reader):',
'- PP: a preposition followed by 1-3 modifiers (closed determiner/possessive list or adjective ending -ej/-ých/-ého/-ému/-ým/-ovom/-skom/-ckom/-nom/-ém) shadows those modifiers AND the head noun after them, exactly as `after_prep` already shadows the first word.',
'- NV: closed non-verb list ending like a verb: príliš/příliš, samozrejme, proste, okrem, first names in -š (Tomáš, Lukáš, Matúš, ...).',
'No abstain rule, no threshold; a real finite verb is still read (unit checks: `Chodíte po starej ceste`, `Robíte to príliš často`, `sme` still fire; the 5 sentences no longer do): %d/%d unit checks pass.'%(sum(u['ok'] for u in R['unit']),len(R['unit'])),'',
'Catches vs cost on the closed 2I set (F4v2 layer only):','- catches: %d judge-correct items no longer F4v2-rejected (the 24 FRs); they now go to L3.'%a3['catch_cost']['correct_no_longer_F4v2'],
'- cost: %d judge-WRONG items no longer F4v2-rejected; they now go to L3 (FA risk, decided only by the S2 calls). Deterministic layers before L3 (F3/F5 run before F4v2) did not catch them.'%a3['catch_cost']['wrong_no_longer_F4v2'],
'- items newly rejected / otherwise changed by the fix: %d.'%len(a3['catch_cost']['newly_rejected_other']),'',
'Production scan (sk_features signals, fixed vs 2I, every upload row): SK %d/%d rows change signals, CZ %d/%d. Removed signals (top): %s.'%(A5['sk_upload']['signal_changes'],A5['sk_upload']['rows'],A5['cz_upload']['signal_changes'],A5['cz_upload']['rows'],'; '.join('%s x%d'%(w,c) for w,c in A5['sk_upload']['removed_signals_top'][:20])),'',
'## A3 CLOSED-SET RE-SCORE (2I set, 900 items, TRANSLATION-ONLY stack through the real code path, stored 2I L3 replies by request hash, 0 calls)',
'Replay check (fix OFF): %d items reach L3, %d without a stored reply, %d decisions differ from 2I results.jsonl.'%(a3['replay_check_fix0']['reach_l3'],a3['replay_check_fix0']['missing_replies'],len(a3['replay_check_fix0']['decisions_differing_from_2I'])),
'','| | coverage | FA |','|---|---|---|','| 2I (before) | %s | %s |'%(f(b['coverage_det']),f(b['fa_det'])),
'| fixed, deterministic part (pending counted as reject) | %s | %s |'%(f(a['coverage_det']),f(a['fa_det'])),
'| fixed, bound: all pending accepted | %s | %s |'%(f(a['coverage_if_pending_accepted']),f(a['fa_if_pending_accepted'])),'',
'With the fix %d items reach L3; **%d new L3 calls are needed** (no stored 2I reply; the 2I run never planned a call for F4v2-rejected items): %d judge-correct, %d judge-wrong. Final A3 numbers come in S2 after exactly these calls.'%(a3['reach_l3_fix1'],len(a3['new_l3_calls_needed']),a['pending_correct'],a['pending_wrong']),'',
'Every item whose verdict changed or is pending:','','| jid | judge | 2I layer, accept | fixed |','|---|---|---|---|']
L+=['| %s | %s | %s, %s | %s |'%(c['jid'],c['judge'],c['before'][0],c['before'][1],c['after'] if isinstance(c['after'],str) else '%s, %s'%tuple(c['after'])) for c in a3['changed']]
w=A4['1W_test']
L+=['','## A4 Regression gate (deterministic, 0 calls)','F4v2 runs after AG/F3/F5 and before L1/L2/L3 (checker_1i.decide 802-820), so a changed F4v2 decision is the only way the fix can move a verdict; every item is checked old vs fixed F4v2.',
'- 1W test set (phase1w/a4/run/results_1u.json, %d rows): F4v2 final-layer rows %d; F4v2 fire changes %d; verdict flips %d; new calls needed %d. Coverage 392/401 = 97.76 %% and FA 16/499 = 3.21 %% unchanged.'%(w['n'],w['F4v2_layer_rows'],len(w['fire_changes']),len(w['verdict_flips']),len(w['new_calls']))]
for k,v in A4['packets'].items():
    L.append('- %s (%d items): F4v2 fire changes %d%s'%(k,v['n'],len(v['fire_changes']),(' - '+'; '.join('%s %s %s->%s'%(c['id'],c['judged'],c['old_fire'],c['new_fire']) for c in v['fire_changes'][:10])) if v['fire_changes'] else ''))
tot=sum(len(v['fire_changes']) for v in A4['packets'].values())
L+=['Verdict: %s'%('PASS — no F4v2 decision changes on the 1W set or any 1Q/1S/1T/1U/1W item file (the 1S packet = the closed 1Q set re-scored in 1S); coverage and FA cannot get worse; 0 new calls.' if not w['fire_changes'] and tot==0 else 'CHANGES — see list; the item files above need review (fire changes %d).'%tot),'',
'## A5 Czech reader','phase1v/trackC/cz_reader.py builds its Czech CK by executing checker_1i.py with only the `em` patch, so `sk_features` has the SAME ending heuristics and the same one-token `after_prep`. Unit (old -> fixed): '+'; '.join('`%s` %s -> %s'%(s,o[0],n[0]) for (s,o),(_,n) in zip(A5['cz_unit_old'],A5['cz_unit_new'])),
'Czech upload scan: %d/%d rows change signals with the Czech variant (Slovak + Czech prepositions při/přes/ve/ze/ke/podle/kolem/…, same NV list). Removed (top): %s.'%(A5['cz_upload']['signal_changes'],A5['cz_upload']['rows'],'; '.join('%s x%d'%(x,c) for x,c in A5['cz_upload']['removed_signals_top'][:15])),
'Fix available as `f4fix.build_fixed(CZ_CK, "cz")`. Note: the 2I decide path for Czech items would call the Slovak checker_1i F4v2 (no Czech decide path is wired); the Czech CK is used by reader_nom (lang cz).','',
'Files: phase2j/f4fix.py, phase2j/stack_tonly.py (hook), phase2j/partA/partA.py, partA_result.json, partA_stdout.txt, _run/ (requests, reqkeys_fix0/1.json incl. the missing list, prepare/finish outputs).']
open(P2J+'/partA/PART_A.md','w').write('\n'.join(L)+'\n')
json.dump({'jids':a3['new_l3_calls_needed'],'n':len(a3['new_l3_calls_needed']),'a4_new':w['new_calls']},open(P2J+'/partA/NEW_L3_CALLS_S2.json','w'),indent=1)
print(len(a3['new_l3_calls_needed']), f(b['coverage_det']), f(b['fa_det']), f(a['coverage_det']), f(a['fa_det']), f(a['coverage_if_pending_accepted']), f(a['fa_if_pending_accepted']), 'A4 1W changes', len(w['fire_changes']), 'packets', tot, 'cz', A5['cz_upload']['signal_changes'], 'sk', A5['sk_upload']['signal_changes'], 'other', len(a3['catch_cost']['newly_rejected_other']))
