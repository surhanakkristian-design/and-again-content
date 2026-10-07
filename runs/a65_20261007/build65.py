# A65: the final lab content = live lab58.json + writer.json (ex3 scenes/models, ex5 gap stories + bModels) + the
# naturalness review (natural_review.json, overridden by natural_recheck.json: fixes, real flags' fixes, more).
#   python3 build65.py plan   -> content/a65_final_changes.json (every change before -> after) + content/a65_lab58.json
# The recordings / translations of changed texts are added later by tts65.py / tr65 (voices: null = to record).
import json, os, re, sys, copy
H = os.path.dirname(os.path.abspath(__file__))
lab = json.load(open(f'{H}/upload/lab58_before_a65.json'))
extras = json.load(open(f'{H}/upload/labExtras_before_a65.json'))
writer = json.load(open(f'{H}/content/writer.json'))
review = json.load(open(f'{H}/verify/natural_review.json'))
recheck = json.load(open(f'{H}/verify/natural_recheck.json'))
IDS = [8055, 236, 7071, 8056, 62, 8039, 900001, 900002]
# the final change list: review changes with recheck verdicts, then real flag fixes, then "more"
changes = {}
for c in review['changes']: changes[(c['id'], c['field'])] = dict(c, source='review')
for c in recheck['changes']:
    if c['verdict'] == 'fix': changes[(c['id'], c['field'])]['after'] = c['after']; changes[(c['id'], c['field'])]['why'] += ' | recheck: ' + c['why']
for f in recheck['flags']:
    if f['real']:
        for x in f['fix']: changes[(f['id'], x['field'])] = dict(x, id=f['id'], why=f['why'], source='flag')
for m in recheck['more']: changes[(m['id'], m['field'])] = dict(m, source='recheck')
by = {c['mediaId']: c for c in lab}
log = []
def row_parts(text):
    m = re.match(r'^(to) (.*?)\s*\[(.+)\]$', text)
    return [{'text': 'to', 'plain': True}, {'text': m.group(2)}, {'text': m.group(3), 'gap': True}]
for (vid, field), c in sorted(changes.items(), key=lambda kv: (IDS.index(kv[0][0]), kv[0][1])):
    e = by[vid]; after = c['after']
    m = re.match(r'(ex\d)\.(\w+)(?:\[(\d+)\])?(?:\[(\d+)\])?(?:\.(\w+))?$', field)
    ex, name, i, j, sub = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
    i = int(i) if i is not None else None
    before = None
    if ex == 'ex1' and name == 'phrase': before = e['taps'][i]['phrase']; e['taps'][i]['phrase'] = after; e['voices']['phrases'][i] = None
    elif ex == 'ex1' and name == 'target': before = e['taps'][i]['target']; e['taps'][i]['target'] = after
    elif ex == 'ex2' and name == 'noun':
        before = e['nouns'][i]['word']; e['nouns'][i]['word'] = after; e['voices']['nouns'][i] = None
        if 'x' in c: e['nouns'][i]['x'], e['nouns'][i]['y'] = c['x'], c['y']
    elif ex == 'ex3' and name == 'caption':
        before = e['captions'][i]; e['captions'][i] = after
        pics = e['item']['carousel']['pictures'] if e.get('item') else extras[str(vid)]['carousel']['pictures']
        pics[i]['caption'] = after; pics[i]['voice'] = None
        e['voices']['captions'].pop(before, None)
        trs = e['item']['captionsTr'] if e.get('item') else {k: v['captions'] for k, v in extras[str(vid)]['tr'].items()}
        for lang, t in trs.items(): t.pop(before, None)  # new translation later
    elif ex == 'ex3' and name in ('models', 'scene'): continue  # applied to the writer's file below
    elif ex == 'ex4' and name == 'node':
        node = e['mindMap']['nodes'][i]; before = node[sub]; node[sub] = after
    elif ex == 'ex4' and name == 'row':
        before = ' '.join(p['text'] for p in e['rows'][i]); e['rows'][i] = row_parts(after)
        if e['voices'].get('rows'): e['voices']['rows'][i] = None
    elif ex == 'ex5': continue
    else: sys.exit(f'unknown field {field}')
    log.append({'id': vid, 'field': field, 'before': before, 'after': after, 'why': c['why'], 'source': c['source']})
# writer content (+ review changes on it)
for vid in IDS:
    w = copy.deepcopy(writer[str(vid)]); e = by[vid]
    for (cid, field), c in changes.items():
        if cid != vid: continue
        m = re.match(r'ex3\.(models|scene)\[(\d+)\](?:\[(\d+)\])?$', field)
        if m:
            k, i, j = m.group(1), int(m.group(2)), m.group(3)
            if k == 'scene': before = w['ex3'][i]['scene']; w['ex3'][i]['scene'] = c['after']
            elif j is None: before = w['ex3'][i]['models']; w['ex3'][i]['models'] = c['after']
            else: before = w['ex3'][i]['models'][int(j)]; w['ex3'][i]['models'][int(j)] = c['after']
            log.append({'id': vid, 'field': field, 'before': before, 'after': c['after'], 'why': c['why'], 'source': c['source']})
        m = re.match(r'ex5\.(story|bModels)\[(\d+)\]$', field)
        if m:
            k, i = m.group(1), int(m.group(2))
            before = w['ex5'][k][i]; w['ex5'][k][i] = c['after']
            log.append({'id': vid, 'field': field, 'before': before, 'after': c['after'], 'why': c['why'], 'source': c['source']})
    # model 1 = the (final) caption
    for i, sc in enumerate(w['ex3']):
        if sc['models'][0] != e['captions'][i]: sc['models'][0] = e['captions'][i]
    e['scenes'] = [{k: v for k, v in sc.items() if k in ('scene', 'models', 'tense')} for sc in w['ex3']]
    old_story = e['story']; new_story = w['ex5']['story']
    for i in range(3):
        if old_story[i] != new_story[i]:
            e['voices']['story'][i] = None
            log.append({'id': vid, 'field': f'ex5.story[{i}]', 'before': old_story[i], 'after': new_story[i], 'why': w['ex5'].get('why', 'writer: gap rule') if w['ex5'].get('changed') else 'review', 'source': 'writer+review'})
    e['story'] = new_story
    e['storyModels'] = w['ex5']['bModels']
    if e['storyModels'][0] != e['story'][1]: e['storyModels'][0] = e['story'][1]
# de-duplicate log entries of the same field (writer + review on a story part): keep the earliest before, latest after
seen = {}
for x in log:
    k = (x['id'], x['field'])
    if k in seen: seen[k]['after'] = x['after']; seen[k]['why'] += ' | ' + x['why']
    else: seen[k] = dict(x)
final_log = [x for x in seen.values() if x['before'] != x['after']]
json.dump(final_log, open(f'{H}/content/a65_final_changes.json', 'w'), ensure_ascii=False, indent=1)
json.dump(lab, open(f'{H}/content/a65_lab58.json', 'w'), ensure_ascii=False, indent=1)
json.dump(extras, open(f'{H}/content/a65_labExtras.json', 'w'), ensure_ascii=False, indent=1)
print(len(final_log), 'changes')
