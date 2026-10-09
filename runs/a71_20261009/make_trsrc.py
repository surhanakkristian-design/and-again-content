# A71: tr/tr71_source.json for the translators - per item and field the English, the current translations and what changed
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
APP = '/Users/kristiansurhanak/Projects/and-again/lib'
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
before = {c['mediaId']: c for c in json.load(open(f'{HERE}/content/lab58_before.json'))}
xbefore = json.load(open(f'{HERE}/content/labExtras_before.json'))
now = {c['mediaId']: c for c in json.load(open(f'{APP}/lab58.json'))}
joined = lambda ps: ' '.join(p['text'] for p in ps)
out = {}
for vid in [8055, 236, 7071, 8056, 62, 8039, 900001, 900002]:
    b, c = before[vid], now[vid]
    en = {'phrases': [t['phrase'] for t in c['taps']], 'nouns': [n['word'] for n in c['nouns']], 'story': c['story'], 'rows': [joined(r) for r in c['rows']]}
    old_en = {'phrases': [t['phrase'] for t in b['taps']], 'nouns': [n['word'] for n in b['nouns']], 'story': b['story'], 'rows': [joined(r) for r in b['rows']]}
    item = {'level': c['level'], 'scenes': [s['scene'] for s in c['scenes']], 'en': en, 'changed': {}, 'old': {}}
    for f in en:
        if f == 'rows':
            # a row keeps its old translation only when the same English row existed before
            item['changed'][f] = [i for i, t in enumerate(en[f]) if t not in old_en[f]]
        else:
            item['changed'][f] = [i for i, t in enumerate(en[f]) if i >= len(old_en[f]) or old_en[f][i] != t]
    if c.get('ownRow'):
        en['ownRow'] = joined(c['ownRow'])
        item['changed']['ownRow'] = not b.get('ownRow') or joined(b['ownRow']) != en['ownRow']
    en['captions'] = c['captions']
    old_caps = b['captions']
    item['changed']['captions'] = [cap for cap in c['captions'] if cap not in old_caps]
    for lang in LANGS:
        t = b['tr'][lang]
        o = {'phrases': t['phrases'], 'nouns': t['nouns'], 'story': t['story']}
        rows_old = t.get('rows') or t['phrases']
        o['rows'] = [rows_old[old_en['rows'].index(r)] if r in old_en['rows'] else None for r in en['rows']]
        if c.get('ownRow'): o['ownRow'] = t.get('ownRow') if not item['changed']['ownRow'] else None
        caps = b['item']['captionsTr'][lang] if vid in (900001, 900002) else xbefore[str(vid)]['tr'][lang]['captions']
        o['captions'] = {cap: caps.get(cap) for cap in c['captions']}
        item['old'][lang] = o
    out[str(vid)] = item
os.makedirs(f'{HERE}/tr', exist_ok=True)
json.dump(out, open(f'{HERE}/tr/tr71_source.json', 'w'), ensure_ascii=False, indent=1)
n = sum(len(v) if isinstance(v, list) else int(bool(v)) for item in out.values() for v in item['changed'].values())
print(f'{n} changed English entries x {len(LANGS)} languages')
