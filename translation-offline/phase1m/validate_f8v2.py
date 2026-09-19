#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1M - F8v2 `sk_clauses()` validated against the blind hand gold over the 210 existing
Slovak sentences.  Format of Phase 1k report S4 / Phase 1L S3 (validate_f9_1l.py).

0 model calls, 0 network, 0 DB.  Inputs: phase1m/existing_210.json (Slovak only) and
phase1m/f8gold/gold_part{1,2}.json.  `sk_clauses(slovak, annotation)` ignores its annotation
argument (it calls f9._clauses(slovak) and _clause_agent(toks) only), so no annotation is read.

AGREE        = same agents in every clause (pronoun identity, or noun head).
CONSERVATIVE = the script abstains, wholly or on some clause, where the gold names an agent,
               and asserts nothing the gold contradicts.
ERROR        = the script asserts an agent the gold does not have, or a different one, or asserts
               on an `alt_subject_ok` sentence in a way that would forbid the allowed alternative.
"""
import datetime, json, math, os, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True
import importlib  # noqa: E402
f8v2 = importlib.import_module(os.environ.get('F8V2_MOD', 'f8v2'))

TAG = sys.argv[1] if len(sys.argv) > 1 else 'after'
ACCESS = os.path.join(HERE, 'access_log.jsonl')


def alog(side, what, n, purpose):
    with open(ACCESS, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps({'ts': datetime.datetime.now(datetime.timezone.utc)
                             .strftime('%Y-%m-%dT%H:%M:%SZ'), 'side': side, 'what': what,
                             'caller': 'f8v2-validate', 'n': n, 'purpose': purpose},
                            ensure_ascii=False) + '\n')


def _ge(k, n, p): return sum(math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(k, n+1))


def _le(k, n, p): return sum(math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(0, k+1))


def cp(k, n, a=0.05):
    if n == 0: return (0.0, 100.0)
    lo, hi = 0.0, 1.0
    if k > 0:
        x, y = 0.0, 1.0
        for _ in range(120):
            m = (x+y)/2
            if _ge(k, n, m) > a/2: y = m
            else: x = m
        lo = (x+y)/2
    if k < n:
        x, y = 0.0, 1.0
        for _ in range(120):
            m = (x+y)/2
            if _le(k, n, m) < a/2: y = m
            else: x = m
        hi = (x+y)/2
    return (round(lo*100, 2), round(hi*100, 2))


# ------------------------------------------------------------------ agent normalisation
def s_val(ag):
    if ag is None: return None
    if ag['kind'] in ('pron', 'prodrop'): return ('P', (ag.get('en') or '').lower())
    return ('N', (ag.get('tok') or '').lower())


def g_val(ag):
    if ag is None: return None
    if ag.get('kind') == 'pronoun': return ('P', (ag.get('en_subject') or '').lower())
    return ('N', (ag.get('sk') or '').lower(), (ag.get('en_subject') or '').lower())


def fold(x):
    """ASCII-fold: the hand gold was written without Slovak diacritics."""
    x = (x or '').lower().replace('\u0142', 'l')
    return ''.join(c for c in unicodedata.normalize('NFKD', x) if not unicodedata.combining(c))


PRON_EN = {'i', 'you', 'he', 'she', 'it', 'we', 'they'}


def same(s, g):
    if s is None or g is None: return s == g
    # agent identity IS the English subject: a gold noun/name entry whose en_subject is a pronoun
    # ("(elided: straznik)" -> "he") names the same agent as the script's pronoun readout
    if s[0] == 'P' and g[0] == 'N' and fold(g[2]) in PRON_EN: return s[1] == fold(g[2])
    if s[0] != g[0]: return False
    if s[0] == 'P': return s[1] == g[1]
    tok = fold(s[1])
    words = {fold(w) for w in g[1].replace(',', ' ').split()}
    return tok in words or tok == fold(g[2]) \
        or any(len(tok) > 3 and (w.startswith(tok[:4]) or tok.startswith(w[:4])) for w in words)


def show_s(ag):
    if ag is None: return 'ABSTAIN'
    return '%s=%s(%s)' % (ag['kind'], ag.get('en') or ag.get('tok'), ag.get('tok'))


def show_g(ag):
    if ag is None: return 'no-agent'
    return '%s=%s("%s")' % (ag.get('kind'), ag.get('en_subject'), ag.get('sk'))


def main():
    sents = json.load(open(os.path.join(HERE, 'existing_210.json'), encoding='utf-8'))
    alog('dev+holdout1j+fresh1k', 'existing_210.json (Slovak/side only)', len(sents),
         'F8v2 sk_clauses validation against the blind hand gold')
    gold = []
    for p in ('gold_part1.json', 'gold_part2.json'):
        g = json.load(open(os.path.join(HERE, 'f8gold', p), encoding='utf-8'))
        alog('dev+holdout1j+fresh1k', 'f8gold/' + p, len(g),
             'blind hand gold: Slovak clause agents, F8v2 validation')
        gold += g
    G = {g['sid']: g for g in gold}
    by_sid = {s['sid']: s for s in sents}
    assert set(G) == set(by_sid), 'gold/sentence sid mismatch: %s' % (set(G) ^ set(by_sid))

    rows = []
    for s in sents:
        sid, sk = s['sid'], s['slovak']
        g = G[sid]
        sc = f8v2.sk_clauses(sk, None)
        gc = g['clauses']
        sv = [s_val(c['agent']) for c in sc]
        gv = [g_val(c.get('agent')) for c in gc]
        errs, cons, notes = [], False, []
        if len(sv) == len(gv):
            for k, (a, b) in enumerate(zip(sv, gv)):
                if a is None and b is None: continue
                if a is None:
                    cons = True; continue
                if b is None:
                    errs.append('clause %d: script asserts %s, gold has NO agent (%s)'
                                % (k, show_s(sc[k]['agent']), gc[k].get('no_agent_reason')))
                elif not same(a, b):
                    errs.append('clause %d: script %s vs gold %s'
                                % (k, show_s(sc[k]['agent']), show_g(gc[k].get('agent'))))
        else:
            notes.append('clause split differs (script %d, gold %d)' % (len(sv), len(gv)))
            pool = [x for x in gv if x is not None]
            for k, a in enumerate(sv):
                if a is None: continue
                hit = next((j for j, b in enumerate(pool) if same(a, b)), None)
                if hit is None:
                    errs.append('clause %d (split mismatch): script asserts %s, no gold clause has it'
                                % (k, show_s(sc[k]['agent'])))
                else:
                    pool.pop(hit)
            cons = True
        # alt_subject_ok: the script FORBIDS the allowed alternative only when it asserts an
        # agent on the very clause the alternative concerns - and every such clause is marked
        # no-agent in the gold, which the rule above already counts as an ERROR.  Asserting the
        # gold's own agent on a DIFFERENT clause forbids nothing.  All alt sentences are listed
        # below and hand-checked one by one in F8V2_VALIDATION.md.
        if g.get('alt_subject_ok'):
            notes.append('alt_subject_ok: %s' % (g.get('alt_note') or '(no note)'))
        cls = 'ERROR' if errs else ('AGREE' if not cons else 'CONSERVATIVE')
        rows.append({'sid': sid, 'side': s['side'], 'sk': sk, 'cls': cls, 'errs': errs,
                     'notes': notes, 'alt': bool(g.get('alt_subject_ok')),
                     'script': ['[%d/%s] %s - %s' % (c['i'], c['role'], show_s(c['agent']), c['reason'])
                                for c in sc],
                     'gold': ['[%d/%s] %s%s' % (c['i'], c.get('role'), show_g(c.get('agent')),
                                                '' if c.get('agent') else
                                                ' (%s)' % c.get('no_agent_reason'))
                              for c in gc]})

    out = ['| side | n | agree | conservative | error | error rate | CP 95 % |',
           '|---|---|---|---|---|---|---|']
    tbl = {}
    for name, key in (('DEV', 'dev'), ('HOLDOUT', 'holdout'), ('FRESH1K', 'fresh1k'), ('ALL', None)):
        rs = rows if key is None else [r for r in rows if r['side'] == key]
        n = len(rs); a = sum(1 for r in rs if r['cls'] == 'AGREE')
        c = sum(1 for r in rs if r['cls'] == 'CONSERVATIVE'); e = sum(1 for r in rs if r['cls'] == 'ERROR')
        lo, hi = cp(e, n)
        tbl[name] = {'n': n, 'agree': a, 'conservative': c, 'error': e,
                     'rate': round(100.0*e/n, 2) if n else 0.0, 'ci': [lo, hi]}
        out.append('| %s | %d | %d | %d | %d | %.2f %% | [%.2f, %.2f] |'
                   % (name, n, a, c, e, 100.0*e/n if n else 0.0, lo, hi))
    errs = [r for r in rows if r['cls'] == 'ERROR']
    snap = {'tag': TAG, 'table': tbl, 'rows': rows}
    json.dump(snap, open(os.path.join(HERE, 'f8v2_validation_%s.json' % TAG), 'w'),
              ensure_ascii=False, indent=1)
    print('\n'.join(out))
    print('\nERRORS: %d / %d' % (len(errs), len(rows)))
    for r in errs:
        print('\n- %s (%s) %s' % (r['sid'], r['side'], r['sk']))
        for e in r['errs']: print('    ! ' + e)
        for x in r['script']: print('    script ' + x)
        for x in r['gold']: print('    gold   ' + x)
    print('\n--- sides of the split-mismatch CONSERVATIVEs ---')
    for r in rows:
        if any('split' in x for x in r['notes']) and r['cls'] != 'ERROR':
            print('  %s %s | %s' % (r['sid'], r['notes'], r['sk'][:70]))
    print('\n--- alt_subject_ok sentences: %d ---' % sum(1 for r in rows if r['alt']))
    for r in rows:
        if r['alt']:
            print('  %s [%s] %s' % (r['sid'], r['cls'], r['sk'][:70]))
            for x in r['script']: print('       script ' + x)
            for x in r['gold']: print('       gold   ' + x)


if __name__ == '__main__':
    main()
