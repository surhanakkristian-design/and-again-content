#!/usr/bin/env python3
"""Phase 2J S2c - A1/A4/A5 for F4v3 (deterministic, 0 calls): 2I F4v3 vs fixed F4v3 on the closed 2I set (per-item
signals of the 27), the 1W test set, the 1S rows + packet, and both upload files (new extra-signal exposure)."""
import json, os, sys, collections
sys.dont_write_bytecode = True
P2J = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'; TOFF = os.path.dirname(P2J)
sys.path[:0] = [P2J, TOFF + '/phase1i', TOFF + '/phase1i/taskC', TOFF + '/phase1v/trackC']
import checker_1i as C, guards_c as G, f4fix, cz_reader as CZ                    # noqa
FX = f4fix.build_fixed_v3(G, C)
jl = lambda p: [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
out = {'label': 'S2c F4v3 gate (deterministic, 0 calls)'}
IT = {i['jid']: i for i in jl(TOFF + '/phase2i/set/items.jsonl')}
S2 = {r['jid']: r for r in jl(P2J + '/run_S2/results.jsonl')}
sk_of = lambda r: r.get('sk') or r.get('slovak') or r.get('src')
f27 = []
for j, r in sorted(S2.items()):
    if r['layer'] == 'F4v3':
        it = {'sk': sk_of(IT[j]), 'answer': IT[j]['answer']}
        o, n = G.f4v3_subject_mismatch(it), FX['f4v3_subject_mismatch'](it)
        f27.append({'jid': j, 'judge': IT[j]['judge_label'], 'old_fire': o[0], 'old_signals': o[1].get('signals'), 'old_features': o[1].get('features'),
                    'old_extra': o[1].get('extra_signal'), 'new_fire': n[0], 'new_signals': n[1].get('signals'), 'new_reason': n[1].get('reason')})
ch2i = []
for j, i in IT.items():
    it = {'sk': sk_of(i), 'answer': i['answer']}
    if G.f4v3_subject_mismatch(it)[0] != FX['f4v3_subject_mismatch'](it)[0]:
        ch2i.append(j)
out['A1_F4v3_27'] = f27; out['closed_2I_fire_changes'] = sorted(ch2i)
def gate(rows, sk, ans, layer, acc):
    ch, flips = [], []
    for r in rows:
        s, a = r.get(sk), r.get(ans)
        if not s or not a: continue
        o, n = G.f4v3_subject_mismatch({'sk': s, 'answer': a})[0], FX['f4v3_subject_mismatch']({'sk': s, 'answer': a})[0]
        if o != n:
            c = {k: r.get(k) for k in ('item_id', 'iid', 'jid', 'judged', 'label_s2', layer, acc)}; c.update(sk=s, answer=a, old=o, new=n)
            ch.append(c)
            if (n and r.get(acc)) or (o and r.get(layer) == 'F4v3'): flips.append(c)
    return {'rows': len(rows), 'F4v3_layer_rows': sum(1 for r in rows if r.get(layer) == 'F4v3'), 'fire_changes': ch, 'verdict_flips_or_new_calls': flips}
out['A4'] = {'1W_test (phase1w/a4/run/results_1u.json)': gate(json.load(open(TOFF + '/phase1w/a4/run/results_1u.json'))['rows'], 'sk', 'answer', 'final_layer', 'final_accept'),
             '1S rows (phase1s/taskA/rows_1s.json)': gate(json.load(open(TOFF + '/phase1s/taskA/rows_1s.json')), 'slovak', 'answer', 'layer_1s', 'accept_1s'),
             '1S packet (phase1s/taskC/judge/packet.json)': gate(json.load(open(TOFF + '/phase1s/taskC/judge/packet.json'))['items'], 'slovak', 'answer', 'layer', 'accept')}
ckcz = CZ.build()['CK']; FXC = f4fix.build_fixed_v3(G, ckcz, 'cz')
def v3old(sf, s):
    f, src = sf(s)
    if src: return f, src, False
    num, ex = G.sk_number_extra(s)
    return (dict(f, number=num), ex, True) if num else (f, src, False)
up = {}
for lang, path, osf, nfx in (('sk', TOFF + '/phase2i/upload/annotations_sk_fixed.jsonl', C.sk_features, FX), ('cz', TOFF + '/phase2i/upload/annotations_cz_fixed.jsonl', ckcz.sk_features, FXC)):
    chg = newx = 0; ex = []
    for r in jl(path):
        s = r['src']; o = v3old(osf, s); n = nfx['sk_features_v3'](s)
        if (o[0], o[1]) != (n[0], n[1]): chg += 1
        if n[2] and not o[2]:
            newx += 1; ex.append({'src': s, 'extra': n[1], 'old_signals': o[1]})
    up[lang] = {'rows_v3_features_changed': chg, 'rows_new_extra_number_signal': newx, 'examples': ex[:10]}
out['upload_scan'] = up
out['A5'] = {'cz_reader_mentions_guards_c_or_decide': any(k in open(TOFF + '/phase1v/trackC/cz_reader.py', encoding='utf-8').read() for k in ('guards_c', 'F4v3', 'decide('))}
out['verdict'] = 'PASS' if all(not v['verdict_flips_or_new_calls'] for v in out['A4'].values()) else 'CHECK'
json.dump(out, open(P2J + '/partA/GATE_F4V3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('A1 F4v3 items', len(f27), 'old_fire', sum(x['old_fire'] for x in f27), 'new_fire', sum(x['new_fire'] for x in f27), 'old_extra', sum(bool(x['old_extra']) for x in f27))
print('A1 signals', collections.Counter(tuple(x['old_signals'] or ()) for x in f27).most_common())
print('closed 2I fire changes', len(ch2i), sorted(set(j.split(':')[1] for j in ch2i)))
for k, v in out['A4'].items(): print('A4', k, 'rows', v['rows'], 'F4v3rows', v['F4v3_layer_rows'], 'changes', len(v['fire_changes']), 'flips', len(v['verdict_flips_or_new_calls']))
print('UPLOAD', {k: (v['rows_v3_features_changed'], v['rows_new_extra_number_signal']) for k, v in up.items()}, [e['src'][:70] + ' ' + str(e['extra']) for e in up['sk']['examples'][:4]])
print('A5', out['A5'], 'VERDICT', out['verdict'])
