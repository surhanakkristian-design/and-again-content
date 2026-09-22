#!/usr/bin/env python3
"""Phase 2L B2 readout (0 calls). CLOSED-SET, IN-SAMPLE."""
import collections, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P2L = os.path.dirname(HERE); sys.path.insert(0, P2L)
import score_2l as SC
CC = SC.CC
data = SC.load(); cc = SC.load_cc(); G = SC.groups(data); allrows = G['pooled']
cand_any = [r for r in allrows if CC.l3_ok(r['r'], True)]
pend = [r['key'] for r in cand_any if r['key'] not in cc]
assert not pend, 'replies missing: %d' % len(pend)
def cs(r):
    c = cc[r['key']]
    return 'failed' if c['failed'] else ('missing' if c['verdict'].startswith('MISSING: ') else 'none')
res = {}
for tip, name in ((False, 'tip_rejected'), (True, 'tip_accepted')):
    res[name] = {}
    for g, rows in G.items():
        for lv in ('all',) + SC.LEVELS:
            rr = [r for r in rows if lv == 'all' or r['level'] == lv]
            cand = [r for r in rr if CC.l3_ok(r['r'], tip)]
            miss = [r for r in cand if cs(r) == 'missing']; fail = [r for r in cand if cs(r) == 'failed']
            res[name].setdefault(g, {})[lv] = {
                'checked': len(cand), 'checked_wrong': sum(r['label'] == 'wrong' for r in cand),
                'checked_correct': sum(r['label'] == 'correct' for r in cand),
                'catches': sum(r['label'] == 'wrong' for r in miss), 'cost': sum(r['label'] == 'correct' for r in miss),
                'failed_items': len(fail), 'failed_rate_pct': round(100.0 * len(fail) / max(1, len(cand)), 2)}
m35 = [r for r in allrows if r['label'] == 'wrong' and r['r']['accept'] and not r['old_acc'] and r['wtype'] == 'M']
fa44 = [r for r in allrows if r['label'] == 'wrong' and r['r']['accept'] and not r['old_acc']]
led = SC.jl(os.path.join(HERE, 'ledger.jsonl')) if os.path.exists(os.path.join(HERE, 'ledger.jsonl')) else []
c200 = [x for x in led if x.get('http') == 200]
st = json.load(open(os.path.join(HERE, 'RUN_STATUS.json')))
calls = {'counted_http200': len(c200), 'failed_calls': sum(1 for x in c200 if x.get('failed')),
         'failed_call_rate_pct': round(100.0 * sum(1 for x in c200 if x.get('failed')) / max(1, len(c200)), 2),
         'uncounted_attempts': sum(1 for x in led if x.get('http') != 200), 'spend_usd': round(sum(x.get('cost_usd') or 0 for x in c200), 6),
         'items_checked': len(cand_any), 'unique_requests': st.get('unique_requests'),
         'phase_ledger': json.load(open(os.path.join(P2L, 'GEMINI_LEDGER.json')))}
verd = collections.Counter(cs(r) for r in cand_any)
listed = sorted([r for r in cand_any if cs(r) in ('missing', 'failed')], key=lambda r: (cs(r), r['set'], r['jid']))
def eff(r, tip):
    if not CC.l3_ok(r['r'], tip): return '-'
    if cs(r) == 'failed': return 'failed (L3 verdict kept)'
    return 'catch' if r['label'] == 'wrong' else 'COST'
items = [{'set': r['set'], 'jid': r['jid'], 'level': r['level'], 'writer_type': r['wtype'], 'label': r['label'],
          'l3': r['r']['l3_reply'], 'source': r['src'], 'answer': r['answer'], 'word': cc[r['key']]['word'],
          'raw': cc[r['key']]['raw'], 'state': cs(r), 'effect_tip_rejected': eff(r, False), 'effect_tip_accepted': eff(r, True),
          'm35': r in m35} for r in listed]
out = {'label': 'CLOSED-SET, IN-SAMPLE re-score (the sets were read while SOURCE-ONLY and this check were designed)',
       'results': res, 'verdicts_over_checked_items': dict(verd), 'calls': calls,
       'm35': {'n': len(m35), 'caught': sum(cs(r) == 'missing' for r in m35), 'failed': sum(cs(r) == 'failed' for r in m35)},
       'fa44': {'n': len(fa44), 'caught': sum(cs(r) == 'missing' for r in fa44)}, 'items': items}
json.dump(out, open(os.path.join(HERE, 'partB.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
L = ['# Phase 2L Part B: SOURCE-SIDE content check - CLOSED-SET, IN-SAMPLE', '',
     '**CLOSED-SET, IN-SAMPLE re-score.** Both Slovak sets (2I, 2J Part D) were read while SOURCE-ONLY and this check were '
     'designed; these are not fresh-set numbers. Existing judge labels; 2K SOURCE-ONLY L3 replies are the STORED ones.', '',
     'Check: content_check.py, prompt spec/content_check_prompt.txt, gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, '
     'input = Slovak sentence + language name + answer only. Run on every item L3 accepted under either TIP variant '
     '(L3 SAME or L3 TIP), one call per unique request.', '',
     'Gemini: %s counted (HTTP 200) calls, %s uncounted attempts, spend $%.4f; failed (unparsable) calls %d = %.2f %%. '
     'Verdicts over the %d checked items: %s.' % (calls['counted_http200'], calls['uncounted_attempts'], calls['spend_usd'],
     calls['failed_calls'], calls['failed_call_rate_pct'], len(cand_any), json.dumps(dict(verd))), '',
     "2K's 35 added writer-type M false acceptances: **%d caught**, %d failed calls. All 44 added FAs: %d caught." % (
         out['m35']['caught'], out['m35']['failed'], len(fa44) and out['fa44']['caught']), '',
     '## Catches (judge-wrong newly rejected) and cost (judge-correct newly rejected)', '',
     '| TIP handling | set | level | checked (wrong/correct) | catches | cost | failed calls (rate) |', '|---|---|---|---|---|---|---|']
for name in ('tip_rejected', 'tip_accepted'):
    for g in SC.GROUPS:
        for lv in ('all',) + SC.LEVELS:
            x = res[name][g][lv]
            L.append('| %s | %s | %s | %d (%d/%d) | %d | %d | %d (%.2f %%) |' % (name.replace('_', ' '), g, lv, x['checked'], x['checked_wrong'],
                     x['checked_correct'], x['catches'], x['cost'], x['failed_items'], x['failed_rate_pct']))
L += ['', '## Every item the check rejected or failed on (%d)' % len(items), '',
      'effect columns: catch = judge-wrong newly rejected; COST = judge-correct newly rejected; - = not checked in that '
      'variant (L3 TIP is already a rejection when TIP is rejected). M35 = one of 2K\'s 35 added M false acceptances.', '',
      '| # | set | id | level | writer | judge | L3 | Slovak | answer | word named / raw | TIP rej | TIP acc | M35 |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
for i, x in enumerate(items, 1):
    L.append('| %d | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (i, x['set'], x['jid'], x['level'], x['writer_type'], x['label'],
             x['l3'], SC.esc(x['source']), SC.esc(x['answer']), SC.esc(x['word'] if x['state'] == 'missing' else 'FAILED: %r' % x['raw']),
             x['effect_tip_rejected'], x['effect_tip_accepted'], 'yes' if x['m35'] else ''))
L += ['', "## 2K's 35 added M false acceptances", '', '| set | id | Slovak | answer | check |', '|---|---|---|---|---|']
for r in m35:
    c = cc[r['key']]
    L.append('| %s | %s | %s | %s | %s |' % (r['set'], r['jid'], SC.esc(r['src']), SC.esc(r['answer']), SC.esc(c['verdict'] or 'FAILED: %r' % c['raw'])))
open(os.path.join(HERE, 'partB.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('PARTB', json.dumps({k: out[k] for k in ('verdicts_over_checked_items', 'calls', 'm35', 'fa44')}))
for name in res:
    for g in SC.GROUPS:
        x = res[name][g]['all']; print(name, g, 'catches', x['catches'], 'cost', x['cost'], 'failed', x['failed_items'])
