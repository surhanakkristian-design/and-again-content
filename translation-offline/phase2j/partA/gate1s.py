#!/usr/bin/env python3
"""Phase 2J S2 - A4 on the 1S packet (phase1s/taskA/rows_1s.json = the 1S re-score of the closed 1Q set, and the
1S taskC judge packet), deterministic, 0 calls: old vs fixed F4v2 on every row; a changed F4v2 fire is the only way
the fix can move a verdict (F4v2 sits after AG/F3/F5, before L1/L2/L3)."""
import glob, json, os, sys
sys.dont_write_bytecode = True
P2J = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'; TOFF = os.path.dirname(P2J)
sys.path.insert(0, P2J); sys.path.insert(0, TOFF + '/phase1i')
import checker_1i as C, f4fix                                                   # noqa
FX = f4fix.build_fixed(C)
S = {}
for f in glob.glob(TOFF + '/phase1q/**/sentences.json', recursive=True):
    try:
        for s in json.load(open(f, encoding='utf-8')):
            if s.get('slovak'): S.setdefault(int(s['sid']), s['slovak'])
    except Exception:
        pass
for f in ('taskD/TIPREJ_22.json', 'taskD/L3_30_GROUPED.json'):
    for r in json.load(open(TOFF + '/phase1s/' + f, encoding='utf-8')):
        S.setdefault(int(r['sid']), r['slovak'])


def sk_of(r):
    if r.get('sk') or r.get('slovak'): return r.get('sk') or r.get('slovak')
    try: return S.get(int(str(r.get('iid') or r.get('id') or r.get('item_id')).split(':')[1]))
    except Exception: return None


out = {'label': 'A4 1S packet gate (deterministic, 0 calls)', 'packets': {}}
PAST = ('L1', 'L3', 'L3:TIPrej', 'TIPdet', 'F2B', 'L2')
for name, rows in (('phase1s/taskA/rows_1s.json', json.load(open(TOFF + '/phase1s/taskA/rows_1s.json', encoding='utf-8'))),
                   ('phase1s/taskC/judge/packet.json', json.load(open(TOFF + '/phase1s/taskC/judge/packet.json', encoding='utf-8'))['items'])):
    n = nsk = 0; ch = []
    for r in rows:
        n += 1
        sk = sk_of(r); ans = r.get('answer')
        if not sk or not ans: continue
        nsk += 1
        o = C.f4v2_subject_mismatch({'sk': sk, 'answer': ans})[0]; w = FX['f4v2_subject_mismatch']({'sk': sk, 'answer': ans})[0]
        if o != w:
            ch.append({'iid': r.get('iid') or r.get('jid'), 'sk': sk, 'answer': ans, 'layer_1s': r.get('layer_1s', r.get('layer')),
                       'accept_1s': r.get('accept_1s', r.get('accept')), 'label': r.get('label_s2'), 'old': o, 'new': w})
    lay = [r.get('layer_1s', r.get('layer')) for r in rows]
    flips = [c for c in ch if (c['new'] and c['accept_1s'] and c['layer_1s'] in PAST) or (c['layer_1s'] == 'F4v2' and not c['new'])]
    out['packets'][name] = {'rows': n, 'rows_with_slovak': nsk, 'F4v2_layer_rows': sum(1 for x in lay if x == 'F4v2'),
                            'fire_changes': ch, 'verdict_changes_or_new_calls': flips}
out['verdict'] = 'PASS' if all(not v['verdict_changes_or_new_calls'] for v in out['packets'].values()) else 'CHECK'
json.dump(out, open(P2J + '/partA/GATE_1S.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in out['packets'].items():
    print('GATE1S', k, 'rows', v['rows'], 'with_sk', v['rows_with_slovak'], 'F4v2rows', v['F4v2_layer_rows'], 'fire_changes', len(v['fire_changes']), 'flips', len(v['verdict_changes_or_new_calls']))
print('GATE1S verdict', out['verdict'])
