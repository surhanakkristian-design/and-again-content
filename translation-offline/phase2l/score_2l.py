#!/usr/bin/env python3
"""Phase 2L scoring library (0 calls): closed Slovak sets 2I + 2J Part D, their existing judge labels, the STORED 2K
SOURCE-ONLY results, the stored reference-based results (2I tonly / 2J fixed), the Part B replies.  Exact CP = 2K's."""
import json, math, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); TOFF = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import content_check as CC  # noqa: E402
SETS = {'2I': (TOFF + '/phase2i/set/items.jsonl', TOFF + '/phase2k/run_S2_2i/results.jsonl', TOFF + '/phase2i/run/results.jsonl'),
        '2J': (TOFF + '/phase2j/partD/set/items.jsonl', TOFF + '/phase2k/run_S2_2j/results.jsonl', TOFF + '/phase2j/partD/run/results.jsonl')}
LEVELS = ('A1', 'A2', 'B1', 'B2'); GROUPS = ('2I', '2J', 'pooled')
REPLIES = os.path.join(HERE, 'partB', 'replies.jsonl')


def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


def cp(x, n, a=0.05):
    if n == 0:
        return (float('nan'),) * 2
    def cdf(k, p):
        if p <= 0: return 1.0
        if p >= 1: return 0.0 if k < n else 1.0
        s = 0.0
        for i in range(0, k + 1):
            s += math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1) + i * math.log(p) + (n - i) * math.log1p(-p))
        return s
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(100):
            m = (lo + hi) / 2
            if f(m): hi = m
            else: lo = m
        return (lo + hi) / 2
    lo = 0.0 if x == 0 else bis(lambda p: 1 - cdf(x - 1, p) >= a / 2)
    hi = 1.0 if x == n else bis(lambda p: cdf(x, p) <= a / 2)
    return (100 * lo, 100 * hi)


def load():
    data = {}
    for s, (ip, np_, op) in SETS.items():
        items = jl(ip); new = {r['jid']: r for r in jl(np_)}
        old = {r['jid']: r for r in jl(op) if r.get('stack', 'tonly') == 'tonly'}
        data[s] = [{'set': s, 'jid': it['jid'], 'key': s + '|' + it['jid'], 'level': it['level'], 'label': it['judge_label'],
                    'wtype': it.get('writer_type'), 'src': it['slovak'], 'answer': it['answer'], 'r': new[it['jid']],
                    'old_acc': bool(old[it['jid']]['accept'])} for it in items]
        assert len(data[s]) == 900 and set(r['label'] for r in data[s]) == {'correct', 'wrong'}
    return data


def load_cc(p=REPLIES):
    return {r['jid']: r for r in jl(p)} if os.path.exists(p) else {}


def acc_2k(row, tip):
    return CC.l3_ok(row['r'], tip)


def acc_b(row, tip, cc):
    a, _, _ = CC.decide(row['r'], cc.get(row['key']), tip)
    if a is None:
        raise RuntimeError('content-check reply missing for %s' % row['key'])
    return a


def metr(rows, f):
    C = [r for r in rows if r['label'] == 'correct']; W = [r for r in rows if r['label'] == 'wrong']
    xc = sum(1 for r in C if f(r)); xw = sum(1 for r in W if f(r))
    return {'cov': [xc, len(C), round(100.0 * xc / len(C), 2), [round(v, 2) for v in cp(xc, len(C))]],
            'fa': [xw, len(W), round(100.0 * xw / len(W), 2), [round(v, 2) for v in cp(xw, len(W))]]}


def groups(data):
    return {'2I': data['2I'], '2J': data['2J'], 'pooled': data['2I'] + data['2J']}


def table(data, f):
    return {g: dict([('all', metr(v, f))] + [(L, metr([r for r in v if r['level'] == L], f)) for L in LEVELS])
            for g, v in groups(data).items()}


def fmt(m):
    return '%d/%d = %.2f %% [%.2f, %.2f]' % (m[0], m[1], m[2], m[3][0], m[3][1])


def esc(s):
    return str(s).replace('|', '/').replace('\n', ' ')
