#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare F9 sk_frame / F8 sk_agent against the hand gold on all 140 arm-B Slovak sentences."""
import json, math, os, sys
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
import f9, f8

def _tail_ge(k, n, p):
    return sum(math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(k, n+1))
def _tail_le(k, n, p):
    return sum(math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(0, k+1))
def cp(k, n, a=0.05):
    if n == 0: return (0.0, 100.0)
    lo, hi = 0.0, 1.0
    if k > 0:
        x, y = 0.0, 1.0
        for _ in range(200):
            m = (x+y)/2
            if _tail_ge(k, n, m) > a/2: y = m
            else: x = m
        lo = (x+y)/2
    if k < n:
        x, y = 0.0, 1.0
        for _ in range(200):
            m = (x+y)/2
            if _tail_le(k, n, m) < a/2: y = m
            else: x = m
        hi = (x+y)/2
    return (round(lo*100, 2), round(hi*100, 2))

sents = {json.loads(l)['sid']: json.loads(l) for l in open(os.path.join(H,'sentences_140.jsonl'), encoding='utf-8')}
gold  = {json.loads(l)['sid']: json.loads(l) for l in open(os.path.join(H,'gold_tf.jsonl'), encoding='utf-8')}
rows = []
for sid, g in gold.items():
    s = sents[sid]
    got = f9.sk_frame(s['sk'])
    S, G = set(got['frames']), set(g['gold_frames'])
    if not S: cls = 'CONSERVATIVE'
    elif S == G: cls = 'AGREE'
    elif G <= S: cls = 'CONSERVATIVE'
    else: cls = 'ERROR'
    ag = f8.sk_agent(s['sk'])
    gv = g['gold_voice']
    want = (gv == 'active')
    got_nom = ag['agent_nom']
    if got_nom is True and want: v = 'AGREE'
    elif got_nom is True and not want: v = 'ERROR'
    elif got_nom is None: v = 'CONSERVATIVE'
    elif got_nom is False and not want: v = 'AGREE'
    else: v = 'CONSERVATIVE'
    rows.append({'sid': sid, 'side': s['side'], 'sk': s['sk'], 'gold': sorted(G), 'script': sorted(S),
                 'cls': cls, 'why': got['reason'], 'main': got['main'],
                 'gold_voice': gv, 'agent_nom': got_nom, 'v_cls': v, 'v_why': ag['reason'], 'agent': ag['agent']})
def table(rs, tag):
    n = len(rs); a = sum(1 for r in rs if r['cls']=='AGREE'); c = sum(1 for r in rs if r['cls']=='CONSERVATIVE')
    e = sum(1 for r in rs if r['cls']=='ERROR')
    lo, hi = cp(e, n)
    print('F9 %-9s n=%3d  AGREE %3d  CONSERVATIVE %3d  ERROR %2d  err=%5.2f%%  CP95 [%.2f, %.2f]' % (tag, n, a, c, e, 100.0*e/n, lo, hi))
    return e, n
for tag, rs in (('DEV', [r for r in rows if r['side']=='dev']), ('HOLDOUT', [r for r in rows if r['side']=='holdout']), ('ALL 140', rows)):
    table(rs, tag)
print('\nF9 ERRORS:')
for r in rows:
    if r['cls']=='ERROR':
        print('  %-6s %-7s gold=%-22s script=%-22s | %s\n         main=%s | why=%s' % (r['sid'], r['side'], r['gold'], r['script'], r['sk'][:88], r['main'], r['why']))
print('\nF8 sk_agent:')
for tag, rs in (('DEV', [r for r in rows if r['side']=='dev']), ('HOLDOUT', [r for r in rows if r['side']=='holdout']), ('ALL 140', rows)):
    n=len(rs); a=sum(1 for r in rs if r['v_cls']=='AGREE'); c=sum(1 for r in rs if r['v_cls']=='CONSERVATIVE'); e=sum(1 for r in rs if r['v_cls']=='ERROR')
    lo,hi = cp(e,n)
    print('F8 %-9s n=%3d  AGREE %3d  CONSERVATIVE %3d  ERROR %2d  err=%5.2f%%  CP95 [%.2f, %.2f]' % (tag,n,a,c,e,100.0*e/n,lo,hi))
from collections import Counter
print('gold voice classes:', dict(Counter(r['gold_voice'] for r in rows)))
print('\nF8 ERRORS:')
for r in rows:
    if r['v_cls']=='ERROR':
        print('  %-6s %-7s gold_voice=%-11s agent=%-12s | %s\n         why=%s' % (r['sid'], r['side'], r['gold_voice'], r['agent'], r['sk'][:88], r['v_why']))
json.dump(rows, open(os.path.join(H, sys.argv[1] if len(sys.argv)>1 else 'validation_rows.json'),'w'), ensure_ascii=False, indent=1)
