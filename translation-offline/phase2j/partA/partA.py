#!/usr/bin/env python3
"""Phase 2J stage S1, Part A (0 model calls): A1 diagnosis, A2 fix check, A3 closed-set replay, A4 gate, A5 Czech."""
import collections, glob, hashlib, json, math, os, subprocess, sys
sys.dont_write_bytecode = True
P2J = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'
TOFF = os.path.dirname(P2J); P2I = TOFF + '/phase2i'; OUT = P2J + '/partA'; RUN = OUT + '/_run'
os.makedirs(RUN, exist_ok=True)
os.environ['P2I_RUN_DIR'] = RUN
sys.path.insert(0, P2J); import write_guard  # noqa
sys.path.insert(0, TOFF + '/phase1i'); import checker_1i as C  # noqa
import f4fix  # noqa
FX = f4fix.build_fixed(C)
VERD = ('SAME', 'TIP', 'DIFF')
res = {}

def cp(x, n):
    if n == 0: return [None, None]
    def cdf(k, p):
        if p <= 0: return 1.0
        if p >= 1: return 0.0 if k < n else 1.0
        return sum(math.exp(math.lgamma(n+1)-math.lgamma(i+1)-math.lgamma(n-i+1)+i*math.log(p)+(n-i)*math.log(1-p)) for i in range(0, k+1))
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            m = (lo+hi)/2
            if f(m): lo = m
            else: hi = m
        return (lo+hi)/2
    lo = 0.0 if x == 0 else bis(lambda p: 1-cdf(x-1, p) < 0.025)
    hi = 1.0 if x == n else bis(lambda p: cdf(x, p) > 0.025)
    return [round(100*lo, 2), round(100*hi, 2)]

def rate(x, n): return {'x': x, 'n': n, 'pct': round(100.0*x/n, 2) if n else None, 'cp95': cp(x, n)}

# ---------------- unit checks of the fix (synthetic + the 5 sentences)
UNIT = [('Vozidlo uháňalo po vidieckej ceste predtým, než bolo zaparkované pri dunách, ako bolo pozorované.', 'The vehicle had sped along the road before it was parked by the dunes.', False),
        ('Kamarátka povedala, že náramok je príliš voľný, tak ho upravila.', 'My friend said the bracelet was too loose, so she adjusted it.', False),
        ('Povedal, že tréning bol najtvrdší v celom jeho živote! Čistá agónia!', 'He said the training was the hardest of his life!', False),
        ('Od roku 2019 fotí lietadlá pri tomto plote. Zjavne veľmi nenáročný koníček.', 'He has photographed planes at this fence since 2019.', False),
        ('Samozrejme si dala trasu nakresliť na mapu, pre prípad, že by zabudla vlastný plán.', 'Of course she had the route drawn on the map.', False),
        ('Chodíte po starej ceste každý deň?', 'Does he walk along the old road every day?', True),
        ('Včera sme boli v meste.', 'He was in town yesterday.', True),
        ('Robíte to príliš často.', 'He does it too often.', True),
        ('Išli sme po starej ceste.', 'They went along the old road.', True)]
unit = []
for sk, en, want in UNIT:
    new = FX['f4v2_subject_mismatch']({'sk': sk, 'answer': en})[0]
    unit.append({'sk': sk, 'answer': en, 'old_fire': C.f4v2_subject_mismatch({'sk': sk, 'answer': en})[0], 'new_fire': new, 'want_fire': want, 'ok': new == want})
res['unit'] = unit
assert all(u['ok'] for u in unit), unit

# ---------------- A1: signals on the 5 sentences before/after
items = [json.loads(l) for l in open(P2I + '/set/items.jsonl', encoding='utf-8')]
IT = {i['jid']: i for i in items}
R2I = {r['jid']: r for r in (json.loads(l) for l in open(P2I + '/run/results.jsonl')) if r['stack'] == 'tonly'}
a1 = {}
for r in R2I.values():
    if r['layer'] == 'F4v2':
        s = IT[r['jid']]['slovak']
        if r['sid'] not in a1:
            fo, so = C.sk_features(s); fn, sn = FX['sk_features'](s)
            a1[r['sid']] = {'slovak': s, 'old': fo, 'old_signals': so, 'new': fn, 'new_signals': sn, 'items': []}
        a1[r['sid']]['items'].append({'jid': r['jid'], 'judge': IT[r['jid']]['judge_label'], 'answer': IT[r['jid']]['answer'],
                                      'pronouns': C.en_subjects(IT[r['jid']]['answer']),
                                      'new_fire': FX['f4v2_subject_mismatch']({'sk': s, 'answer': IT[r['jid']]['answer']})[0]})
res['A1'] = a1

# ---------------- A3: closed 2I set through the real stack path, stored replies by request hash
PASS = ('jid', 'sid', 'level', 'slovak', 'topic', 'answer', 'annotation')
def strip(a):
    b = {k: v for k, v in a.items() if not (k == 'lk' or str(k).startswith('lk_'))}
    for sub in ('hygienised', 'raw'):
        if isinstance(b.get(sub), dict):
            b[sub] = {k: v for k, v in b[sub].items() if not (k == 'lk' or str(k).startswith('lk_'))}
    return b
clean = []
for it in items:
    c = {k: it[k] for k in PASS if k in it}; c['annotation'] = strip(c['annotation']); clean.append(c)
FIN = RUN + '/items_tonly.json'
json.dump(clean, open(FIN, 'w', encoding='utf-8'), ensure_ascii=False)
def stack(cmd, fix, rep=None):
    out = RUN + '/%s_fix%d.json' % (cmd, fix)
    args = [sys.executable, '-B', P2J + '/stack_tonly.py', cmd, FIN] + ([rep] if rep else []) + [out]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', P2I_RUN_DIR=RUN, P2J_F4FIX=str(fix)); env.pop('TONLY_POISON', None)
    p = subprocess.run(args, env=env, capture_output=True, text=True, cwd=P2J, timeout=3000)
    open(RUN + '/stack_%s_fix%d.log' % (cmd, fix), 'w').write(p.stderr[-20000:])
    if p.returncode: raise SystemExit('stack %s fix%d rc=%s %s' % (cmd, fix, p.returncode, p.stderr[-3000:]))
    return json.load(open(out, encoding='utf-8'))
def rkey(q): return hashlib.sha256(json.dumps([q['sys'], q['user'], q['gcfg']], sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()
LED = {}
for l in open(P2I + '/run/ledger.jsonl'):
    x = json.loads(l)
    if x.get('counted') and x.get('verdict') in VERD: LED[x['req_key']] = x['verdict']
rep = {}
for fix in (0, 1):
    pr = stack('prepare', fix)
    keys = {j: rkey(q) for j, q in pr.items()}
    miss = sorted(j for j, k in keys.items() if k not in LED)
    rp = RUN + '/replies_fix%d.json' % fix
    json.dump({'replies': {j: LED[k] for j, k in keys.items() if k in LED}, 'failed': []}, open(rp, 'w'))
    fin = stack('finish', fix, rp)
    json.dump({'requests': keys, 'missing': miss}, open(RUN + '/reqkeys_fix%d.json' % fix, 'w'), indent=1)
    rep[fix] = {'reach_l3': len(pr), 'missing': miss, 'fin': fin}
lab = {j: IT[j]['judge_label'] for j in IT}
def score(dec, pending=()):
    c = [j for j in lab if lab[j] == 'correct']; w = [j for j in lab if lab[j] == 'wrong']
    acc = lambda j: j in dec and dec[j]['accept']
    pc = [j for j in c if j in pending]; pw = [j for j in w if j in pending]
    return {'coverage_det': rate(sum(acc(j) for j in c), len(c)), 'fa_det': rate(sum(acc(j) for j in w), len(w)),
            'pending_correct': len(pc), 'pending_wrong': len(pw),
            'coverage_if_pending_accepted': rate(sum(acc(j) for j in c) + len(pc), len(c)),
            'fa_if_pending_rejected': rate(sum(acc(j) for j in w), len(w)),
            'fa_if_pending_accepted': rate(sum(acc(j) for j in w) + len(pw), len(w))}
replay0 = [j for j in R2I if (rep[0]['fin'].get(j, {}).get('accept'), rep[0]['fin'].get(j, {}).get('layer')) != (R2I[j]['accept'], R2I[j]['layer'])]
changed = []
for j in sorted(R2I):
    a = rep[1]['fin'].get(j)
    if j in rep[1]['missing'] or a is None or (a['accept'], a['layer']) != (R2I[j]['accept'], R2I[j]['layer']):
        changed.append({'jid': j, 'judge': lab[j], 'before': [R2I[j]['layer'], R2I[j]['accept']],
                        'after': 'PENDING L3 (no stored reply)' if j in rep[1]['missing'] else [a['layer'], a['accept']]})
res['A3'] = {'label': 'CLOSED-SET RE-SCORE (2I set, stored 2I L3 replies, 0 calls)',
             'replay_check_fix0': {'reach_l3': rep[0]['reach_l3'], 'missing_replies': len(rep[0]['missing']), 'decisions_differing_from_2I': replay0},
             'before_2I': score(R2I), 'after_det': score(rep[1]['fin'], set(rep[1]['missing'])),
             'reach_l3_fix1': rep[1]['reach_l3'], 'new_l3_calls_needed': rep[1]['missing'], 'changed': changed,
             'catch_cost': {'correct_no_longer_F4v2': sum(1 for c in changed if c['judge'] == 'correct' and c['before'][0] == 'F4v2'),
                            'wrong_no_longer_F4v2': sum(1 for c in changed if c['judge'] == 'wrong' and c['before'][0] == 'F4v2'),
                            'newly_rejected_other': [c for c in changed if c['before'][0] != 'F4v2']}}

# ---------------- A4: 1W test set + every phase1q/1s/1t/1u/1w item file (1S packet = the closed 1Q set)
def a4_rows(rows):
    ch = []
    for r in rows:
        of = C.f4v2_subject_mismatch({'sk': r['sk'], 'answer': r['answer']})[0]
        nf = FX['f4v2_subject_mismatch']({'sk': r['sk'], 'answer': r['answer']})[0]
        if of != nf: ch.append(dict(r, old_fire=of, new_fire=nf))
    return ch
w1 = json.load(open(TOFF + '/phase1w/a4/run/results_1u.json'))['rows']
PAST = ('L1', 'L3', 'L3:TIPrej', 'TIPdet', 'F2B')
ch = a4_rows([{'id': r['item_id'], 'sk': r['sk'], 'answer': r['answer'], 'judged': r['judged'], 'layer': r['final_layer'], 'accept': r['final_accept']} for r in w1])
res['A4'] = {'1W_test': {'n': len(w1), 'F4v2_layer_rows': sum(1 for r in w1 if r['final_layer'] == 'F4v2'),
                         'fire_changes': ch,
                         'verdict_flips': [c for c in ch if (c['layer'] in PAST and c['new_fire'] and c['accept']) or (c['layer'] == 'F4v2' and not c['new_fire'])],
                         'new_calls': [c['id'] for c in ch if c['layer'] == 'F4v2' and not c['new_fire']]}, 'packets': {}}
for f in sorted(glob.glob(TOFF + '/phase1[qstuw]/**/items.json', recursive=True)):
    d = os.path.dirname(f)
    if not os.path.exists(d + '/sentences.json'): continue
    S = {s['sid']: s.get('slovak') for s in json.load(open(d + '/sentences.json'))}
    L = json.load(open(d + '/labels.json')) if os.path.exists(d + '/labels.json') else {}
    its = json.load(open(f)); rows = []
    for i in its:
        if i.get('answer') and S.get(i.get('sid')):
            rows.append({'id': i['id'], 'sk': S[i['sid']], 'answer': i['answer'], 'judged': (L.get(i['id']) or {}).get('judged')})
    res['A4']['packets'][os.path.relpath(d, TOFF)] = {'n': len(rows), 'fire_changes': a4_rows(rows)}

# ---------------- A5: Czech reader + production scan (both upload files)
sys.path.insert(0, TOFF + '/phase1v/trackC'); import cz_reader as CZ  # noqa
CKCZ = CZ.build()['CK']; FXCZ = f4fix.build_fixed(CKCZ, 'cz')
def scan(path, old, new):
    n = chg = 0; words = collections.Counter(); ex = []
    for l in open(path, encoding='utf-8'):
        s = json.loads(l)['src']; n += 1
        fo, so = old(s); fn, sn = new(s)
        if so != sn:
            chg += 1
            for x in set(so) - set(sn): words[x.split(' ', 1)[0] + ' ' + x.split()[-1]] += 1
            if len(ex) < 12: ex.append({'src': s, 'old': fo, 'new': fn, 'removed': sorted(set(so) - set(sn)), 'added': sorted(set(sn) - set(so))})
        elif fo != fn: raise AssertionError(s)
    return {'rows': n, 'signal_changes': chg, 'removed_signals_top': words.most_common(60), 'examples': ex}
cz_unit = [(s, CKCZ.sk_features(s)) for s in ('Jel po venkovské cestě příliš rychle.', 'Je příliš unavená, tak šla domů.', 'Při tomto plotě fotí letadla.')]
res['A5'] = {'cz_unit_old': cz_unit, 'cz_unit_new': [(s, FXCZ['sk_features'](s)) for s, _ in cz_unit],
             'cz_upload': scan(P2I + '/upload/annotations_cz_fixed.jsonl', CKCZ.sk_features, FXCZ['sk_features']),
             'sk_upload': scan(P2I + '/upload/annotations_sk_fixed.jsonl', C.sk_features, FX['sk_features'])}
json.dump(res, open(OUT + '/partA_result.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
a3 = res['A3']
print('unit', sum(u['ok'] for u in unit), '/', len(unit))
print('A1 new_fire on 44:', sum(i['new_fire'] for v in a1.values() for i in v['items']))
print('A3 replay fix0 reach', a3['replay_check_fix0']['reach_l3'], 'miss', a3['replay_check_fix0']['missing_replies'], 'diff', len(a3['replay_check_fix0']['decisions_differing_from_2I']))
print('A3 before', a3['before_2I']['coverage_det'], a3['before_2I']['fa_det'])
print('A3 after', json.dumps(a3['after_det']))
print('A3 reach fix1', a3['reach_l3_fix1'], 'new calls', len(a3['new_l3_calls_needed']), 'changed', len(a3['changed']), a3['catch_cost']['correct_no_longer_F4v2'], a3['catch_cost']['wrong_no_longer_F4v2'], len(a3['catch_cost']['newly_rejected_other']))
print('A4 1W', res['A4']['1W_test']['F4v2_layer_rows'], len(res['A4']['1W_test']['fire_changes']), len(res['A4']['1W_test']['verdict_flips']))
for k, v in res['A4']['packets'].items(): print('A4', k, v['n'], len(v['fire_changes']), [(c['id'], c['judged'], c['old_fire'], c['new_fire']) for c in v['fire_changes']][:6])
for k in ('cz_upload', 'sk_upload'): print('A5', k, res['A5'][k]['rows'], res['A5'][k]['signal_changes'], res['A5'][k]['removed_signals_top'][:25])
print('cz_unit', res['A5']['cz_unit_old'], res['A5']['cz_unit_new'])
