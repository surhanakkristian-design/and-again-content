# A64: writes the verified content (content/a64_final.json), its help translations (tr/<lang>.json) and recordings
# (audio/<id>/manifest.json) into ~/Projects/and-again-a64/lib/lab58.json, starting from the backup taken before A64
# (upload/lab58_before_a64.json). Unchanged texts keep their earlier recording and translation.
#   exercise 2: a moved object point; a replaced noun (its phrase, recordings and translations change with it)
#   exercise 4 (not the verb): the mind map (every key-word phrase), the rows (phrases without the key word) + their
#              recordings (voices.rows) and translations (tr.<lang>.rows); new mind-map phrases' recordings in voices.captions
#   exercise 5: the 3 story parts, their recordings and translations
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.expanduser('~/Projects/and-again-a64/lib/lab58.json')
PUB = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/'
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
lab = json.load(open(f'{HERE}/upload/lab58_before_a64.json'))
final = json.load(open(f'{HERE}/content/a64_final.json'))
tr = {l: json.load(open(f'{HERE}/tr/{l}.json')) for l in LANGS}
row_text = lambda parts: ' '.join(p['text'] for p in parts)
for c in lab:
    k = str(c['mediaId'])
    if k not in final: continue
    f = final[k]
    man = json.load(open(f'{HERE}/audio/{k}/manifest.json'))
    rec = {(x['kind'], x['text']): PUB + x['object'] for x in man['items']}
    # exercise 2
    for x in f.get('ex2', []):
        i = [n['word'] for n in c['nouns']].index(x['noun'])
        c['nouns'][i]['x'], c['nouns'][i]['y'] = x['new']
        r = x.get('replacement')
        if r:
            c['nouns'][i]['word'] = r['noun']
            assert c['taps'][i]['target'] == r['doer'], (k, 'the doer keeps its tap region')
            c['taps'][i]['phrase'] = r['phrase']
            c['voices']['phrases'][i] = rec[('phrase', r['phrase'])]
            c['voices']['nouns'][i] = rec[('noun', r['noun'])]
            for l in LANGS:
                c['tr'][l]['phrases'][i] = tr[l]['phrases'][k][r['phrase']]
                c['tr'][l]['nouns'][i] = tr[l]['nouns'][k][r['noun']]
    phrases = [t['phrase'] for t in c['taps']]
    # exercise 4
    if 'ex4' in f:
        c['mindMap'] = f['ex4']['mindMap']
        c['rows'] = f['ex4']['rows']
        c['voices']['rows'] = [c['voices']['phrases'][phrases.index(row_text(r))] if row_text(r) in phrases else rec[('row', row_text(r))] for r in c['rows']]
        for n in c['mindMap']['nodes']:
            if n['caption'] not in c['voices']['captions'] and n['caption'] not in phrases:
                c['voices']['captions'][n['caption']] = rec[('node', n['caption'])]
        for l in LANGS:
            c['tr'][l]['rows'] = [c['tr'][l]['phrases'][phrases.index(row_text(r))] if row_text(r) in phrases else tr[l]['rows'][k][row_text(r)] for r in c['rows']]
    # exercise 5
    old = dict(zip(c['story'], c['voices']['story']))
    parts = f['story']['parts']
    c['voices']['story'] = [rec.get(('story', t)) or old[t] for t in parts]
    c['story'] = parts
    c.pop('storyOrders', None)
    for l in LANGS:
        assert len(tr[l]['stories'][k]) == len(parts), (k, l)
        c['tr'][l]['story'] = tr[l]['stories'][k]
json.dump(lab, open(LAB, 'w'), ensure_ascii=False, indent=1)
print('ok')
