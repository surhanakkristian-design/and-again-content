#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F9 hand-check validation, Phase 1k report format, over the 140 existing arm-B sentences.

Read-only inputs from phase1k/taskB: sentences_140.jsonl + gold_tf.jsonl (agent G's hand gold,
written before any script output existed). Compares the FROZEN phase1k f9 with the phase1l copy
carrying the 2.2 fix. No answers, no labels, no model call, no fresh data.
AGREE = script set == gold; CONSERVATIVE = script abstains or asserts a superset; ERROR = the
script forbids a frame the gold allows (it would reject correct answers).
"""
import importlib.util, json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.join(os.path.dirname(HERE), 'phase1k')
sys.path.insert(0, HERE)
import f9 as f9_new                                                        # noqa: E402
_s = importlib.util.spec_from_file_location('f9_old', os.path.join(K, 'taskB', 'f9.py'))
f9_old = importlib.util.module_from_spec(_s); _s.loader.exec_module(f9_old)


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


def run(mod, tag, sents, gold, out):
    rows = []
    for sid, g in gold.items():
        s = sents[sid]
        got = mod.sk_frame(s['sk'])
        S, G = set(got['frames']), set(g['gold_frames'])
        cls = 'CONSERVATIVE' if not S else ('AGREE' if S == G else ('CONSERVATIVE' if G <= S else 'ERROR'))
        rows.append({'sid': sid, 'side': s['side'], 'sk': s['sk'], 'gold': sorted(G),
                     'script': sorted(S), 'cls': cls, 'why': got['reason']})
    out += ['', '### %s' % tag, '', '| side | n | agree | conservative | error | rate | CP 95 % |',
            '|---|---|---|---|---|---|---|']
    for name, rs in (('DEV', [r for r in rows if r['side'] == 'dev']),
                     ('HOLDOUT', [r for r in rows if r['side'] == 'holdout']), ('ALL', rows)):
        n = len(rs); a = sum(1 for r in rs if r['cls'] == 'AGREE')
        c = sum(1 for r in rs if r['cls'] == 'CONSERVATIVE'); e = sum(1 for r in rs if r['cls'] == 'ERROR')
        lo, hi = cp(e, n)
        out.append('| %s | %d | %d | %d | %d | %.2f %% | [%.2f, %.2f] |'
                   % (name, n, a, c, e, 100.0*e/n if n else 0.0, lo, hi))
    errs = [r for r in rows if r['cls'] == 'ERROR']
    out += ['', 'errors: %d' % len(errs)]
    for r in errs:
        out.append('- **%s** (%s) `%s` gold=%s script=%s — %s'
                   % (r['sid'], r['side'], r['sk'], r['gold'], r['script'], r['why']))
    return rows, errs


def main():
    sents = {json.loads(l)['sid']: json.loads(l) for l in
             open(os.path.join(K, 'taskB', 'sentences_140.jsonl'), encoding='utf-8') if l.strip()}
    gold = {json.loads(l)['sid']: json.loads(l) for l in
            open(os.path.join(K, 'taskB', 'gold_tf.jsonl'), encoding='utf-8') if l.strip()}
    out = ['# Phase 1L — F9 hand-check re-validation over the 140 existing sentences', '',
           'Method and format of Phase 1k report §4. No answers, no labels, 0 model calls.']
    S = 'Ona nikdy neposiela e-maily po desiatej večer'
    o, n = f9_old.sk_frame(S), f9_new.sk_frame(S)
    out += ['', '## Unit test of the 2.2 fix (sentence quoted from the brief, not read from fresh data)',
            '', '```', 'sentence  : %s' % S, 'phase1k f9: %s  (%s)' % (o['frames'], o['reason']),
            'phase1l f9: %s  (%s)' % (n['frames'], n['reason']), '```']
    assert n['frames'] == ['present'], 'FIX FAILED: %r' % (n['frames'],)
    assert o['frames'] != ['present'], 'phase1k f9 no longer shows the bug?'
    ro, eo = run(f9_old, 'phase1k f9 (frozen — reference)', sents, gold, out)
    rn, en = run(f9_new, 'phase1l f9 WITH the 2.2 fix — THE re-validation', sents, gold, out)
    moved = [(a['sid'], a['script'], b['script']) for a, b in zip(ro, rn) if a['script'] != b['script']]
    out += ['', '## Sentences whose F9 frame moved because of the 2.2 fix', '',
            ('none' if not moved else '\n'.join('- %s: %s -> %s' % m for m in moved))]
    open(os.path.join(HERE, 'F9_REVALIDATION_1L.md'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump({'old': ro, 'new': rn}, open(os.path.join(HERE, 'f9_revalidation_1l.json'), 'w'),
              ensure_ascii=False, indent=1)
    print('\n'.join(out))
    print('\nERRORS old %d  new %d  moved %d' % (len(eo), len(en), len(moved)))


if __name__ == '__main__':
    main()
