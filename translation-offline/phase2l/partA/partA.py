#!/usr/bin/env python3
"""Phase 2L Part A (0 calls): TIP under SOURCE-ONLY, from the STORED 2K replies. CLOSED-SET, IN-SAMPLE re-score."""
import collections, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P2L = os.path.dirname(HERE); sys.path.insert(0, P2L)
import score_2l as SC
data = SC.load()
rej = SC.table(data, lambda r: SC.acc_2k(r, False)); acc = SC.table(data, lambda r: SC.acc_2k(r, True))
p3 = json.load(open(SC.TOFF + '/phase2k/analysis/part3.json', encoding='utf-8'))
exact = all(rej[g][L] == p3['res'][g][L]['new'] for g in SC.GROUPS for L in ('all',) + SC.LEVELS)
want = {'2I': ([477, 497], [37, 403]), '2J': ([474, 498], [36, 402]), 'pooled': ([951, 995], [73, 805])}
for g, (c, f) in want.items():
    assert rej[g]['all']['cov'][:2] == c and rej[g]['all']['fa'][:2] == f, (g, rej[g]['all'])
tips = {g: dict(collections.Counter(r['label'] for r in v if r['r'].get('layer') == 'L3:TIPrej')) for g, v in SC.groups(data).items()}
out = {'label': 'CLOSED-SET, IN-SAMPLE re-score, 0 Gemini calls', 'tip_rejected': rej, 'tip_accepted': acc,
       'reproduces_2k_exactly': exact, 'tip_items_by_label': tips}
json.dump(out, open(os.path.join(HERE, 'partA.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
L = ['# Phase 2L Part A: TIP under SOURCE-ONLY (0 calls)', '',
     'CLOSED-SET, IN-SAMPLE re-score of the STORED 2K SOURCE-ONLY replies (phase2k/run_S2_2i, run_S2_2j) against the '
     'existing judge labels (2I, 2J Part D). TIP accepted = an L3 TIP reply counts as accept; nothing else changes. '
     'Not adopted here; it feeds Part C.', '',
     'TIP-rejected reproduces 2K part3.json exactly (every set, every level, CP bounds): **%s**.' % ('YES' if exact else 'NO'), '',
     'L3 TIP items by judge label: %s' % json.dumps(tips), '',
     '| set | level | coverage TIP rejected | coverage TIP accepted | FA TIP rejected | FA TIP accepted |', '|---|---|---|---|---|---|']
for g in SC.GROUPS:
    for lv in ('all',) + SC.LEVELS:
        L.append('| %s | %s | %s | %s | %s | %s |' % (g, lv, SC.fmt(rej[g][lv]['cov']), SC.fmt(acc[g][lv]['cov']),
                                                    SC.fmt(rej[g][lv]['fa']), SC.fmt(acc[g][lv]['fa'])))
open(os.path.join(HERE, 'partA.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('PARTA exact=%s' % exact)
for g in SC.GROUPS:
    print(g, 'rej', SC.fmt(rej[g]['all']['cov']), SC.fmt(rej[g]['all']['fa']), '| acc', SC.fmt(acc[g]['all']['cov']), SC.fmt(acc[g]['all']['fa']))
