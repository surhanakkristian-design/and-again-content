# A65: puts the new recordings (audio/<id>/manifest.json, uploaded) and the verified help translations (tr/<lang>.json)
# into content/a65_lab58.json + content/a65_labExtras.json, then copies both into the app worktree.
import json, glob, os, shutil
H = os.path.dirname(os.path.abspath(__file__))
PUB = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/'
lab = json.load(open(f'{H}/content/a65_lab58.json')); ex = json.load(open(f'{H}/content/a65_labExtras.json'))
old = {e['mediaId']: e for e in json.load(open(f'{H}/upload/lab58_before_a65.json'))}
by = {e['mediaId']: e for e in lab}
row = lambda r: ' '.join(p['text'] for p in r)
for mf in glob.glob(f'{H}/audio/*/manifest.json'):
    man = json.load(open(mf)); e = by[man['mediaId']]; v = e['voices']
    for it in man['items']:
        url = PUB + it['object']; i = it['i'] - 1; k = it['kind']
        if k == 'phrase': assert e['taps'][i]['phrase'] == it['text']; v['phrases'][i] = url
        elif k == 'noun': assert e['nouns'][i]['word'] == it['text']; v['nouns'][i] = url
        elif k == 'story': assert e['story'][i] == it['text']; v['story'][i] = url
        elif k == 'row': assert row(e['rows'][i]) == it['text']; v['rows'][i] = url
        elif k == 'caption':
            v['captions'][it['text']] = url
            pics = e['item']['carousel']['pictures'] if e.get('item') else ex[str(e['mediaId'])]['carousel']['pictures']
            for p in pics:
                if p['caption'] == it['text']: p['voice'] = url
for lang in ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']:
    t = json.load(open(f'{H}/tr/{lang}.json'))
    for sid, parts in t['stories'].items(): assert len(parts) == 3; by[int(sid)]['tr'][lang]['story'] = parts
    for sid, e in by.items():
        if sid == 461: continue
        o = old[sid]; n = e['tr'][lang]
        oph = [x['phrase'] for x in o['taps']]
        for i, tap in enumerate(e['taps']):
            if tap['phrase'] not in oph: n['phrases'][i] = t['phrases'][str(sid)][tap['phrase']]
        onn = [x['word'] for x in o['nouns']]
        for i, nn in enumerate(e['nouns']):
            if nn['word'] not in onn: n['nouns'][i] = t['nouns'][str(sid)][nn['word']]
        orw = [row(r) for r in o['rows']]
        if n.get('rows') is not None:
            for i, r in enumerate(e['rows']):
                if row(r) not in orw: n['rows'][i] = t['rows'][str(sid)][row(r).replace('[', '').replace(']', '')] if row(r) in t['rows'].get(str(sid), {}) or True else None
        for cap, tx in t.get('captions', {}).get(str(sid), {}).items():
            if e.get('item'): e['item']['captionsTr'].setdefault(lang, {})[cap] = tx
            else: ex[str(sid)]['tr'][lang]['captions'][cap] = tx
    for sid, m in t.get('recall', {}).items():
        x = ex[sid]; orc = [row(r['parts']) for r in json.load(open(f'{H}/upload/labExtras_before_a65.json'))[sid]['recall']]
        for i, r in enumerate(x['recall']):
            if row(r['parts']) not in orc: x['tr'][lang]['recall'][i] = m[row(r['parts'])]
json.dump(lab, open(f'{H}/content/a65_lab58.json', 'w'), ensure_ascii=False, indent=1)
json.dump(ex, open(f'{H}/content/a65_labExtras.json', 'w'), ensure_ascii=False, indent=1)
for f, g in [('a65_lab58.json', 'lab58.json'), ('a65_labExtras.json', 'labExtras.json')]:
    shutil.copy(f'{H}/content/{f}', os.path.expanduser(f'~/Projects/and-again-a65/lib/{g}'))
print('merged')
