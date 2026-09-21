#!/usr/bin/env python3
"""Phase 2J S3 - Part C (0 model calls). C1 why F5 did not fire on every current FA; C2 sizing of deterministic
dropped-content-word rules on closed 2I set, 1W test set, 1S rows/packet; C3 A2-level FA drivers."""
import glob, inspect, json, os, re, sys
sys.dont_write_bytecode = True
P2J = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'; TOFF = os.path.dirname(P2J); P2I = TOFF + '/phase2i'
sys.path.insert(0, TOFF + '/phase1i')
import checker_1i as C                                                           # noqa
_ORIG_ANNOT = C.annot; CUR = {}
def _annot(eid):
    if isinstance(eid, str) and eid.startswith('__P2J__'): return CUR['a']
    return _ORIG_ANNOT(eid)
C.annot = _annot
ADP = json.load(open(P2J + '/run_S2c/_adapter_tonly/annotations.json', encoding='utf-8'))
jl = lambda p: [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
SRC = inspect.getsourcelines(C.f5_adjunct_deletion); SUB = inspect.getsourcelines(C._subseq_positions)
def lno(fnsrc, pat):
    lines, start = fnsrc
    for k, l in enumerate(lines):
        if pat in l: return start + k
LN = {'f5': SRC[1], 'subseq_none': lno(SUB, 'return None'), 'f5_continue': lno(SRC, 'continue'),
      'f5_equal': lno(SRC, 'answer equals an accepted variant'), 'span_info': inspect.getsourcelines(C.span_information)[1],
      'noninfo_return': lno(inspect.getsourcelines(C.span_information), 'all(t in NONINFO'), 'refs_of': inspect.getsourcelines(C.refs_of)[1],
      'optional_tokens': inspect.getsourcelines(C.optional_tokens)[1], 'decide_F5': 809}
SRCTXT = {'refs_of': inspect.getsource(C.refs_of), 'optional_tokens': inspect.getsource(C.optional_tokens), 'annot': inspect.getsource(_ORIG_ANNOT), 'f5_tail': ''.join(SRC[0][14:])}
def refs_list(ann):
    a = ann.get('hygienised', ann) if isinstance(ann, dict) else {}
    v = a.get('v') or ann.get('v') or []
    return [x for x in v if isinstance(x, str) and x.strip()]
def mk_it(answer, refs, ann, sk):
    a = ann.get('hygienised', ann) if isinstance(ann, dict) else {}
    return {'answer': answer, 'reference': refs[0] if refs else '', 'refs': refs, 'alt': a.get('alt', []), 'sk': sk, 'annotation': a,
            'exercise_id': '__P2J__'}
def f5_why(it):
    """re-run F5 exactly and name the failing condition per reference."""
    CUR['a'] = it.get('adp') or it['annotation']
    hit, tr = C.f5_adjunct_deletion(it)
    opt = C.optional_tokens(it); lt = C.expand(C.toks(it['answer'])); L = [t for t in lt if t not in opt]
    per = []
    for r in C.refs_of(it):
        rt = C.expand(C.toks(r)); miss = C._subseq_positions(lt, rt, opt)
        if miss is None:
            R = [t for t in rt if t not in opt]
            extra = [t for t in L if t not in R]
            i = 0; brk = None
            for t in L:
                while i < len(R) and R[i] != t: i += 1
                if i >= len(R): brk = t; break
                i += 1
            per.append({'ref': r, 'subsequence': False, 'answer_tokens_not_in_ref': extra, 'first_break': brk})
        else:
            spans = C._spans(miss); pd = C._postdash_start(r, opt)
            per.append({'ref': r, 'subsequence': True, 'spans': [[t for _p, t in s] for s in spans],
                        'span_info': [C.span_information(s, opt, pd) for s in spans]})
    return hit, tr, per
# ---------------------------------------------------------------- C2 candidate rules
FW = set(C.FUNCTION) | set(C.NONINFO)
def stem(t): t = t.lower().strip("'"); t = re.sub(r"'s$", '', t); return t[:5] if len(t) > 5 else re.sub(r'(ies|es|s|ed|ing)$', '', t) or t
def ctoks(s): return [t for t in C.expand(C.toks(s)) if t.isalpha() and len(t) > 1 and t not in FW]
def syn(it):
    S = {}
    for a in it.get('alt') or []:
        if isinstance(a, dict):
            g = set()
            for grp in a.get('groups_or_candidates') or []:
                g |= {stem(w) for w in re.split(r'[_\s]+', str(grp)) if w}
            S[stem(a.get('tok', ''))] = g
    return S
def missing_extra(it, ref):
    S = syn(it); A = {stem(t) for t in ctoks(it['answer'])}; R = [stem(t) for t in ctoks(ref)]
    Rs = set(R)
    miss = [t for t in R if t not in A and not (S.get(t, set()) & A)]
    Aall = set(); [Aall.update(S.get(t, set())) for t in Rs]
    extra = [t for t in A if t not in Rs and t not in Aall]
    return miss, extra
def rules(it):
    refs = it['refs'] or [it['reference']]
    me = [missing_extra(it, r) for r in refs]
    allref = set(); [allref.update(stem(t) for t in ctoks(r)) for r in refs]
    S = syn(it); synall = set(); [synall.update(v) for v in S.values()]
    A = {stem(t) for t in ctoks(it['answer'])}
    in_all = set.intersection(*[{stem(t) for t in ctoks(r)} for r in refs]) if refs else set()
    miss_all = [t for t in in_all if t not in A and not (S.get(t, set()) & A)]
    extra_any = [t for t in A if t not in allref and t not in synall]
    return {'V1_any_ref_content_missing_every_ref': all(m for m, _e in me),
            'V2_net_content_deficit_every_ref': all(len(m) > len(e) for m, e in me),
            'V3_pure_deletion_mod_synonyms_some_ref': any(m and not e for m, e in me),
            'V4_word_in_all_refs_missing_and_no_new_content': bool(miss_all) and not extra_any,
            '_detail': {'per_ref': [{'missing': m, 'extra': e} for m, e in me], 'missing_from_all_refs': miss_all, 'extra_vs_all_refs': extra_any}}
RN = ['V1_any_ref_content_missing_every_ref', 'V2_net_content_deficit_every_ref', 'V3_pure_deletion_mod_synonyms_some_ref', 'V4_word_in_all_refs_missing_and_no_new_content']
def size(name, recs):
    out = {'set': name, 'n': len(recs), 'n_correct': sum(r['lab'] == 'correct' for r in recs), 'n_wrong': sum(r['lab'] == 'wrong' for r in recs),
           'accepted_wrong': sum(r['lab'] == 'wrong' and r['acc'] for r in recs), 'rules': {}}
    for rn in RN:
        catch = [r['id'] for r in recs if r['acc'] and r['lab'] == 'wrong' and r['rules'][rn]]
        cost = [r['id'] for r in recs if r['acc'] and r['lab'] == 'correct' and r['rules'][rn]]
        out['rules'][rn] = {'catches': len(catch), 'cost': len(cost), 'catch_ids': catch, 'cost_ids': cost[:40],
                            'fires_on_already_rejected': sum(1 for r in recs if not r['acc'] and r['rules'][rn])}
    return out
# ---------------------------------------------------------------- closed 2I set, current stack (run_S2c)
IT = {i['jid']: i for i in jl(P2I + '/set/items.jsonl')}
PREP = {x['jid']: x for x in json.load(open(P2J + '/run_S2c/_io/tonly_prepare_items.json', encoding='utf-8'))}
NEW = {r['jid']: r for r in jl(P2J + '/run_S2c/results.jsonl')}
R2I = {r['jid']: r for r in jl(P2I + '/run/results.jsonl') if r['stack'] == 'tonly'}
recs2i = []; C1 = []
for j, x in PREP.items():
    refs = refs_list(x['annotation']); it = mk_it(x['answer'], refs, x['annotation'], x['slovak']); it['adp'] = ADP.get(str(x['sid'])) or ADP.get(x['sid'])
    rr = rules(it); lab = IT[j]['judge_label']
    recs2i.append({'id': j, 'lab': lab, 'acc': bool(NEW[j]['accept']), 'rules': rr, 'level': x['level']})
    if lab == 'wrong' and NEW[j]['accept']:
        hit, tr, per = f5_why(it)
        C1.append({'jid': j, 'level': x['level'], 'slovak': x['slovak'], 'refs': refs, 'answer': x['answer'], 'judge_type': IT[j].get('judge_type') or IT[j].get('type'),
                   'judge_reason': IT[j].get('judge_reason') or IT[j].get('reason'), 'layer': NEW[j]['layer'], 'l3': NEW[j].get('l3_reply'),
                   'in_2I_FA': bool(R2I[j]['accept']), 'f5_recomputed_fire': hit, 'f5_trace': tr, 'per_ref': per, 'c2': rr})
# ---------------------------------------------------------------- 1W test set
D1W = TOFF + '/phase1w/a4/data'; ANN = json.load(open(D1W + '/annotations.json', encoding='utf-8'))
rows = json.load(open(TOFF + '/phase1w/a4/run/results_1u.json', encoding='utf-8'))['rows']
recs1w = []
for r in rows:
    ann = ANN.get(str(r['sid'])) or ANN.get(r['sid']) or {}
    refs = refs_list(ann) or [r['reference']]
    it = mk_it(r['answer'], refs, ann, r.get('sk'))
    recs1w.append({'id': r['item_id'], 'lab': r['judged'], 'acc': bool(r['final_accept']), 'rules': rules(it), 'level': r.get('level')})
# ---------------------------------------------------------------- 1S rows + packet
Q = {}
for f in glob.glob(TOFF + '/phase1q/**/annotations.json', recursive=True):
    try:
        for k, v in json.load(open(f, encoding='utf-8')).items(): Q.setdefault(str(k), v)
    except Exception: pass
def sid_of(r):
    try: return str(r.get('sid') or str(r.get('iid') or r.get('jid') or r.get('item_id')).split(':')[1])
    except Exception: return None
s1 = {}
for name, rs in (('1S rows_1s', json.load(open(TOFF + '/phase1s/taskA/rows_1s.json', encoding='utf-8'))),
                 ('1S packet', json.load(open(TOFF + '/phase1s/taskC/judge/packet.json', encoding='utf-8'))['items'])):
    rec = []; keys = sorted(rs[0].keys()); noref = 0
    for r in rs:
        ann = Q.get(sid_of(r)) or {}
        refs = [x for x in (r.get('refs') or r.get('references') or []) if isinstance(x, str)] or refs_list(ann) or ([r['reference']] if r.get('reference') else [])
        if not refs or not r.get('answer'): noref += 1; continue
        lab = r.get('label_s2') or r.get('label') or r.get('judged')
        lab = 'correct' if str(lab).lower().startswith(('c', 'right', 'true')) else ('wrong' if lab is not None else None)
        acc = r.get('accept_1s', r.get('accept'))
        rec.append({'id': r.get('iid') or r.get('jid') or r.get('item_id'), 'lab': lab, 'acc': bool(acc), 'rules': rules(mk_it(r['answer'], refs, ann, r.get('sk'))), 'level': r.get('level')})
    s1[name] = (rec, keys, noref, sorted({str(r.get('label_s2') or r.get('label') or r.get('judged')) for r in rs})[:8])
SZ = [size('closed 2I set (current stack run_S2c)', recs2i), size('1W test set', recs1w)]
for k, (rec, keys, noref, labs) in s1.items():
    z = size(k, rec); z['rows_skipped_no_ref_or_answer'] = noref; z['keys'] = keys; z['label_values'] = labs; SZ.append(z)
# ---------------------------------------------------------------- C3 per level
lvl = {}
for r in recs2i:
    d = lvl.setdefault(r['level'], {'wrong': 0, 'fa': 0, 'fa_2I': 0}); 
    if r['lab'] == 'wrong':
        d['wrong'] += 1; d['fa'] += r['acc']; d['fa_2I'] += bool(R2I[r['id']]['accept'])
A2_2I = [j for j, r in R2I.items() if IT[j]['judge_label'] == 'wrong' and r['accept'] and PREP[j]['level'] == 'A2']
bil = [f for f in glob.glob(TOFF + '/**/*', recursive=True) if re.search(r'(lemma|bilingual|sk_en|dict|lexicon)', os.path.basename(f), re.I) and '/phase2j/' not in f][:30]
res = {'label': 'Part C, 0 model calls', 'lines': LN, 'src': SRCTXT, 'C1_current_FAs': C1, 'C2_sizing': SZ, 'C3_levels': lvl, 'C3_A2_2I_FAs': A2_2I, 'bilingual_candidates': bil}
json.dump(res, open(P2J + '/partC/partC_result.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('LINES', LN); print('BIL', bil)
for c in C1:
    print('FA', c['jid'], c['level'], 'in2I', c['in_2I_FA'], c['layer'], c['l3'], 'F5', c['f5_recomputed_fire'], c['f5_trace'].get('reason') if isinstance(c['f5_trace'], dict) else '', '| A:', c['answer'])
    for p in c['per_ref']: print('   ', 'SUB' if p['subsequence'] else 'NOSUB', p.get('first_break'), p.get('answer_tokens_not_in_ref', p.get('spans')), p.get('span_info', ''), '| R:', p['ref'][:90])
    print('    C2', {k[:2]: v for k, v in c['c2'].items() if k[0] == 'V'}, c['c2']['_detail']['per_ref'])
for z in SZ:
    print('SIZE', z['set'], 'n', z['n'], 'c', z['n_correct'], 'w', z['n_wrong'], 'accW', z['accepted_wrong'], {k[:2]: (v['catches'], v['cost']) for k, v in z['rules'].items()}, z.get('keys', '')[:30] if z.get('keys') else '', z.get('label_values', ''), z.get('rows_skipped_no_ref_or_answer', ''))
print('LVL', lvl); print('A2_2I', A2_2I)
# ---------------------------------------------------------------- C2 extension: V5 = F5 relaxed (F5's own span_information on
# reference tokens absent from the answer, order ignored; answer may add only function/closed-class tokens or alt synonyms)
def v5(it):
    opt = C.optional_tokens(it) if it.get('adp') or it.get('exercise_id') else set(C.ARTICLES)
    S = syn(it); A = [t for t in C.expand(C.toks(it['answer'])) if t not in opt]; As = {stem(t) for t in A}
    synall = set(); [synall.update(v) for v in S.values()]
    anyfire = False; hits = []
    for r in (it['refs'] or [it['reference']]):
        R = [t for t in C.expand(C.toks(r)) if t not in opt]; Rs = {stem(t) for t in R}
        extra = [t for t in A if stem(t) not in Rs and stem(t) not in synall and t not in FW and t.isalpha()]
        miss = [(p, t) for p, t in enumerate(R) if stem(t) not in As and not (S.get(stem(t), set()) & As)]
        info = [C.span_information(s, opt, C._postdash_start(r, opt)) for s in C._spans(miss)]
        info = [x for x in info if x]
        if extra or not info: return False, None
        hits.append(info)
    return True, hits
def recs_v5(pairs):
    out = []
    for rid, lab, acc, it in pairs:
        CUR['a'] = it.get('adp') or it['annotation']
        out.append({'id': rid, 'lab': lab, 'acc': acc, 'fire': v5(it)[0], 'ans': it['answer'], 'ref': it['reference']})
    return out
P2 = []
for j, x in PREP.items():
    refs = refs_list(x['annotation']); it = mk_it(x['answer'], refs, x['annotation'], x['slovak']); it['adp'] = ADP.get(str(x['sid']))
    P2.append((j, IT[j]['judge_label'], bool(NEW[j]['accept']), it))
P1 = []
for r in rows:
    ann = ANN.get(str(r['sid'])) or {}
    refs = refs_list(ann) or [r['reference']]; it = mk_it(r['answer'], refs, ann, r.get('sk')); it['adp'] = ann
    P1.append((r['item_id'], r['judged'], bool(r['final_accept']), it))
PS = []
rs1 = json.load(open(TOFF + '/phase1s/taskA/rows_1s.json', encoding='utf-8'))
for r in rs1:
    it = mk_it(r['answer'], [r['reference']], {}, r.get('slovak')); it['adp'] = {'v': [r['reference']]}
    PS.append((r['iid'], r['label_s2'], bool(r['accept_1s']), it))
pk = json.load(open(TOFF + '/phase1s/taskC/judge/packet.json', encoding='utf-8'))['items']
ids1s = {r['iid'] for r in rs1}; pk_in = sum(1 for p in pk if p['jid'] in ids1s)
V5 = {}
for name, pr in (('closed 2I', P2), ('1W test', P1), ('1S rows_1s', PS)):
    rr = recs_v5(pr)
    V5[name] = {'catches': [r['id'] for r in rr if r['acc'] and r['lab'] == 'wrong' and r['fire']],
                'cost': [[r['id'], r['ans'], r['ref']] for r in rr if r['acc'] and r['lab'] == 'correct' and r['fire']]}
    print('V5', name, 'catch', len(V5[name]['catches']), V5[name]['catches'], 'cost', len(V5[name]['cost']))
    for c in V5[name]['cost'][:4]: print('   cost', c)
V4c = [z for z in SZ if z['set'].startswith('closed')][0]['rules']['V4_word_in_all_refs_missing_and_no_new_content']
print('V4 2I catches', V4c['catch_ids'], 'cost sample', [(i, PREP[i]['answer'], refs_list(PREP[i]['annotation'])[0]) for i in V4c['cost_ids'][:5]])
print('PACKET', len(pk), 'in rows_1s', pk_in)
print('NREFS FA', sorted({len(c['refs']) for c in C1}), 'NREFS 2I all', {n: sum(1 for x in PREP.values() if len(refs_list(x['annotation'])) == n) for n in (1, 2, 3, 4)})
res['C2_V5_f5_relaxed'] = V5; res['C2_packet_overlap'] = {'packet_items': len(pk), 'in_rows_1s': pk_in}
json.dump(res, open(P2J + '/partC/partC_result.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
