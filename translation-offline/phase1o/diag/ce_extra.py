# Task C+E extra cuts (0 model calls): CP for sub-rates, F5 exposure, DET-swap reweighting, probe cross-tab (prompt confound).
import io, contextlib, json, os, random, collections, time
with contextlib.redirect_stdout(io.StringIO()):
    import ce_analyse as A
R, S, fr = A.R, A.S, A.fr
TOFF = os.path.dirname(A.O)
open(os.path.join(A.O, 'access_log.jsonl'), 'a').write(json.dumps({'ts': time.strftime('%Y-%m-%dT%H:%M:%S'), 'side': 'taskCE', 'what': 'phase1n/calls.jsonl (L-1N:probe) + phase1m/calls.jsonl (L-1M:main) verdicts', 'caller': 'phase1o/diag/ce_extra.py', 'n': 120, 'purpose': 'prompt-confound cross-tab on the 1M items re-asked under P-FROZEN-1N'}) + '\n')
nn = lambda x: not x['passive'] and not x['cleft']
print('## sub-rates, non-passive non-cleft (1M n=571, 1N n=320) and ALL')
for lab, f in [('L3 DIFF', lambda x: x['layer'] == 'L3'), ('L3:TIPrej', lambda x: x['layer'] == 'L3:TIPrej'), ('L3+TIPrej', lambda x: x['layer'] in ('L3', 'L3:TIPrej')), ('F5', lambda x: x['layer'] == 'F5'), ('cause DET', lambda x: x['cause'] == 'DET'), ('cause DROP', lambda x: x['cause'] == 'DROP'), ('cause TENSE', lambda x: x['cause'] == 'TENSE'), ('cause LEX', lambda x: x['cause'] == 'LEX'), ('cause STRUCT', lambda x: x['cause'] == 'STRUCT'), ('L3 DIFF & DET', lambda x: x['layer'] == 'L3' and x['cause'] == 'DET'), ('L3 DIFF & not DET', lambda x: x['layer'] == 'L3' and x['cause'] != 'DET')]:
    print('  %-18s 1M %s | 1N %s || ALL 1M %s | 1N %s' % (lab, R(sum(1 for x in fr if x['set'] == '1m' and nn(x) and f(x)), 571), R(sum(1 for x in fr if x['set'] == '1n' and nn(x) and f(x)), 320), R(sum(1 for x in fr if x['set'] == '1m' and f(x)), 614), R(sum(1 for x in fr if x['set'] == '1n' and f(x)), 426)))
print('## FR by writer intent (all FR): 1M %s | 1N %s' % (dict(collections.Counter(x['intent'] for x in fr if x['set'] == '1m')), dict(collections.Counter(x['intent'] for x in fr if x['set'] == '1n'))))
print('## F5 by intent: 1M %s | 1N %s' % (dict(collections.Counter(x['intent'] for x in fr if x['set'] == '1m' and x['layer'] == 'F5')), dict(collections.Counter(x['intent'] for x in fr if x['set'] == '1n' and x['layer'] == 'F5'))))
def subseq(a, b):
    it = iter(b); return all(t in it for t in a)
for s in ('1m', '1n'):
    ex = []
    for x in S[s]:
        if x['passive'] or x['l1']: continue
        m = A.altmap(x['alt']); a = A.altnorm(A.tok(x['answer']), m); best = None
        for r in x['refs']:
            rt = A.altnorm(A.tok(r), m)
            if len(a) < len(rt) and subseq(a, rt): best = min(best or 99, len(rt) - len(a))
        if best: x['sub_del'] = best; ex.append(x)
    k = sum(x['layer'] == 'F5' for x in ex)
    print('## F5 exposure %s: answers that are a pure token subsequence of a stored variant (alt-normalised, >=1 token deleted): %d = %.1f%% of judged-correct %d ; F5 fired on %s ; by intent %s ; F5 FR not caught by this proxy %d' % (s, len(ex), 100.0 * len(ex) / len(S[s]), len(S[s]), R(k, len(ex)), dict(collections.Counter(x['intent'] for x in ex)), sum(1 for x in fr if x['set'] == s and x['layer'] == 'F5') - k))
    print('     final acceptance of the exposed answers: %s' % R(sum(x['accepted'] for x in ex), len(ex)))
print('## near bins (0,.2] non-passive non-cleft')
for s in ('1m', '1n'):
    it = [x for x in S[s] if nn(x) and 0 < x['dist'] <= 0.2]; print('  %s %s ; rejected by layer %s ; by cause %s' % (s, R(sum(x['accepted'] for x in it), len(it)), dict(collections.Counter(x['layer'] for x in it if not x['accepted'])), dict(collections.Counter(x['cause'] for x in it if not x['accepted']))))
# DET-swap x distance-bin reweighting
random.seed(1505)
def cell(x): return (x['det_swap'], min(A.binof(x), 3))
def rw(a, b):
    ca, cb = collections.defaultdict(list), collections.defaultdict(list)
    for x in a: ca[cell(x)].append(x['accepted'])
    for x in b: cb[cell(x)].append(x['accepted'])
    pool = {c: A.mean(ca.get(c, []) + cb.get(c, [])) for c in set(ca) | set(cb)}
    ra = {c: (A.mean(ca[c]) if c in ca else pool[c]) for c in pool}; rb = {c: (A.mean(cb[c]) if c in cb else pool[c]) for c in pool}
    wa = {c: len(ca.get(c, [])) / len(a) for c in pool}; wb = {c: len(cb.get(c, [])) / len(b) for c in pool}
    cova, covb = sum(wa[c] * ra[c] for c in pool), sum(wb[c] * rb[c] for c in pool)
    compA = sum(wa[c] * rb[c] for c in pool) - covb; compB = cova - sum(wb[c] * ra[c] for c in pool)
    return 100 * (cova - covb), 100 * compA, 100 * compB
for sn in ('NONPASS_NONCLEFT', 'WRITER_C_NONPASS', 'NONPASS'):
    a = [x for x in S['1m'] if A.SUB[sn](x)]; b = [x for x in S['1n'] if A.SUB[sn](x)]
    g, cA, cB = rw(a, b); cm, cn = A.clusters(a), A.clusters(b); bs = []
    for _ in range(600):
        aa = [x for c in random.choices(cm, k=len(cm)) for x in c]; bb = [x for c in random.choices(cn, k=len(cn)) for x in c]
        _, p, q = rw(aa, bb); bs.append(((p + q) / 2, p, q))
    av = sorted(z[0] for z in bs); pa = sorted(z[1] for z in bs); qb = sorted(z[2] for z in bs)
    print('## reweighting on det_swap x distance (8 cells) %s: gap %.2f ; composition A (1N rates, 1M mix) %.2f [%.2f, %.2f] ; B (1M rates, 1N mix) %.2f [%.2f, %.2f] ; avg %.2f [%.2f, %.2f]' % (sn, g, cA, pa[15], pa[584], cB, qb[15], qb[584], (cA + cB) / 2, av[15], av[584]))
print('## sole-determiner answers (nearest variant differs only in a/an/the/this/that/these/those), non-passive')
DETS = {'a', 'an', 'the', 'this', 'that', 'these', 'those'}
for s in ('1m', '1n'):
    sole = []
    for x in S[s]:
        if x['passive'] or x['l1']: continue
        m = A.altmap(x['alt']); a = [t for t in A.altnorm(A.tok(x['answer']), m) if t not in DETS]
        if any(a == [t for t in A.altnorm(A.tok(r), m) if t not in DETS] for r in x['refs']) and x['dist'] > 0: sole.append(x)
    print('  %s n=%d (%.1f%% of judged-correct) accepted %s ; model verdicts %s' % (s, len(sole), 100.0 * len(sole) / len(S[s]), R(sum(x['accepted'] for x in sole), len(sole)), dict(collections.Counter(str(x['verdict']) for x in sole))))
# probe cross-tab: the same 1M items under the old prompt (1M main) and the new prompt (1N probe)
old, new = {}, {}
for l in open(os.path.join(TOFF, 'phase1m/calls.jsonl')):
    d = json.loads(l)
    if d.get('variant') == 'L-1M:main': old[d['item_id']] = d['verdict']
for l in open(os.path.join(TOFF, 'phase1n/calls.jsonl')):
    d = json.loads(l)
    if d.get('variant') == 'L-1N:probe': new[d['item_id']] = d['verdict']
both = [i for i in new if i in old]; jc = {x['id']: x for x in S['1m']}
print('## probe: %d items asked under both prompts (%d not in the 1M ledger); kinds %s' % (len(both), len(new) - len(both), dict(collections.Counter(i.split(':')[0] + ':' + i.split(':')[1][:3] for i in new))))
print('   all: old->new %s' % dict(collections.Counter('%s->%s' % (old[i], new[i]) for i in both)))
j = [i for i in both if i in jc]
print('   judged-correct subset n=%d: old->new %s ; non-cleft %s' % (len(j), dict(collections.Counter('%s->%s' % (old[i], new[i]) for i in j)), dict(collections.Counter('%s->%s' % (old[i], new[i]) for i in j if not jc[i]['cleft']))))
