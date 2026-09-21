#!/usr/bin/env python3
"""Phase 2J S7 (copied from phase2i/judge/analyze.py, absolute paths; items from the CORRECTED phase2j/upload): judge labels, duplicate-control agreement, judge vs writer intent, runner item file.
0 model calls. Judge label = ground truth; writer intent only for balancing."""
import json, os, hashlib
HERE = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j/partD/judge'
P2I = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j/partD'
UPLOAD = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j/upload/annotations_sk_fixed.jsonl'
import sys
PRECHECK = sys.argv[1:] == ['precheck']
LEVELS = ['A1', 'A2', 'B1', 'B2']

def jl(p): return [json.loads(l) for l in open(p, encoding='utf-8')]

key = jl(os.path.join(HERE, 'key.jsonl'))
ans = {a['aid']: a for a in jl(os.path.join(P2I, 'set', 'answers.jsonl'))}
verd = {}
if PRECHECK:
    verd = {k['jid']: {'jid': k['jid'], 'label': 'correct', 'reason': 'precheck'} for k in key}
else:
  for s in range(1, 5):
    for o in json.load(open(os.path.join(HERE, 'verdicts_s%d.json' % s), encoding='utf-8')):
        verd[o['jid']] = o
assert len(verd) == 980 and all(k['jid'] in verd for k in key)

labels, ctrl = [], []
orig = {k['aid']: k for k in key if not k['is_control']}
for k in key:
    v = verd[k['jid']]
    row = {'aid': k['aid'], 'label': v['label'], 'reason': v['reason'], 'session': k['session'], 'jid': k['jid']}
    (ctrl if k['is_control'] else labels).append(row)
assert len(labels) == 900 and len({r['aid'] for r in labels}) == 900
labels.sort(key=lambda r: (ans[r['aid']]['sid'], r['aid']))
if PRECHECK: HERE = '/private/tmp/claude-501/-Users-kristiansurhanak-Meine-Ablage-And-Again/6bf76dd1-92f6-4a0f-99c9-89f6fc4cd33f/scratchpad/precheck'; os.makedirs(HERE, exist_ok=True); P2I_OUT = HERE
else: P2I_OUT = os.path.join(P2I, 'set')
with open(os.path.join(HERE, 'labels.jsonl'), 'w', encoding='utf-8') as f:
    for r in labels: f.write(json.dumps(r, ensure_ascii=False) + '\n')
lab = {r['aid']: r for r in labels}

# controls
dis, pairs = [], {}
for c in ctrl:
    o = lab[c['aid']]; a = ans[c['aid']]
    pr = '%d-%d' % tuple(sorted((o['session'], c['session'])))
    p = pairs.setdefault(pr, {'n': 0, 'agree': 0})
    p['n'] += 1; ag = o['label'] == c['label']; p['agree'] += ag
    if not ag:
        dis.append({'aid': c['aid'], 'level': a['level'], 'writer_intent': a['writer_intent'], 'writer_type': a['writer_type'],
                    'slovak': a['slovak'], 'answer': a['answer'],
                    'orig': {'session': o['session'], 'label': o['label'], 'reason': o['reason']},
                    'dup': {'session': c['session'], 'label': c['label'], 'reason': c['reason']}})
agree = len(ctrl) - len(dis)
controls = {'agree': agree, 'n': len(ctrl), 'rate': round(agree / len(ctrl), 4), 'per_session_pair': pairs,
            'by_level': {l: {'n': sum(ans[c['aid']]['level'] == l for c in ctrl),
                             'agree': sum(ans[c['aid']]['level'] == l and lab[c['aid']]['label'] == c['label'] for c in ctrl)} for l in LEVELS},
            'disagreements': dis}
json.dump(controls, open(os.path.join(HERE, 'controls.json'), 'w'), indent=1, ensure_ascii=False)

# judge vs writer intent
cm = {}
jdis = []
for r in labels:
    a = ans[r['aid']]; cm.setdefault('%s->%s' % (a['writer_intent'], r['label']), 0)
    cm['%s->%s' % (a['writer_intent'], r['label'])] += 1
    if a['writer_intent'] != r['label']:
        jdis.append({'aid': r['aid'], 'level': a['level'], 'writer_intent': a['writer_intent'], 'writer_type': a['writer_type'],
                     'judge': r['label'], 'reason': r['reason'], 'slovak': a['slovak'], 'answer': a['answer']})
counts = {'correct': sum(r['label'] == 'correct' for r in labels), 'wrong': sum(r['label'] == 'wrong' for r in labels)}
per_level = {l: {x: sum(r['label'] == x and ans[r['aid']]['level'] == l for r in labels) for x in ('correct', 'wrong')} for l in LEVELS}
wr_type_kept = {}
for r in labels:
    t = ans[r['aid']]['writer_type']
    if t: wr_type_kept.setdefault(t, {'wrong': 0, 'correct': 0})[r['label']] += 1
intent = {'confusion_writer_to_judge': cm, 'agree': 900 - len(jdis), 'n': 900, 'label_counts': counts, 'per_level': per_level,
          'wrong_intent_by_type_judged': wr_type_kept, 'disagreements': jdis}
json.dump(intent, open(os.path.join(HERE, 'intent_agreement.json'), 'w'), indent=1, ensure_ascii=False)

# runner item file
ann = {}
for r in jl(UPLOAD): ann[r['n']] = r
items = []
for r in labels:
    a = ans[r['aid']]; an = ann[a['sid']]
    assert an['src'] == a['slovak'] and an['type_title'] == a['topic'] and an['level'] == a['level'] and an['v'] and an['v'][0] == an['en']
    items.append({'jid': a['aid'], 'aid': a['aid'], 'sid': a['sid'], 'level': a['level'], 'slovak': a['slovak'], 'topic': a['topic'],
                  'answer': a['answer'], 'judge_label': r['label'], 'judge_reason': r['reason'], 'judge_session': r['session'],
                  'writer_intent': a['writer_intent'], 'writer_type': a['writer_type'], 'writer_agent_drop': a['writer_agent_drop'],
                  'exercise_id': an['exercise_id'], 'n': an['n'], 'en': an['en'], 'v': an['v'], 'annotation': an})
ip = os.path.join(P2I_OUT, 'items.jsonl')
with open(ip, 'w', encoding='utf-8') as f:
    for it in items: f.write(json.dumps(it, ensure_ascii=False) + '\n')
isha = hashlib.sha256(open(ip, 'rb').read()).hexdigest()
open(ip + '.sha256', 'w').write('%s  items.jsonl\n' % isha)
out = {'controls': '%d/%d' % (agree, len(ctrl)), 'pairs': {k: '%d/%d' % (v['agree'], v['n']) for k, v in pairs.items()},
       'control_disagree_aids': [d['aid'] for d in dis], 'labels': counts, 'per_level': per_level, 'confusion': cm,
       'intent_disagree': len(jdis), 'intent_disagree_aids': [d['aid'] for d in jdis], 'by_type': wr_type_kept, 'items_sha': isha}
json.dump(out, open(os.path.join(HERE, 'STAGE4_RESULT.json'), 'w'), indent=1, ensure_ascii=False)
print(json.dumps(out, ensure_ascii=False))
