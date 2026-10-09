# A71: writes the new English content (content/draft71.json after review = content/final71.json) into the app's lib/lab58.json
# and lib/labExtras.json. Unchanged texts keep their recordings and translations; a changed text gets voice null (tts71.py
# records it) and its translation from tr/tr71_final.json (missing = the old one is kept and listed as STALE).
#   python3 build71.py <content json> [--tr tr/tr71_final.json] [--voices audio/voices71.json] [--report changes71.json]
import json, sys, copy, os
HERE = os.path.dirname(os.path.abspath(__file__))
APP = '/Users/kristiansurhanak/Projects/and-again/lib'
args = sys.argv[1:]
src = args[0]
opt = lambda name: args[args.index(name) + 1] if name in args else None
draft = json.load(open(src))
tr_new = json.load(open(opt('--tr'))) if opt('--tr') else {}
voices_new = json.load(open(opt('--voices'))) if opt('--voices') else {}
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
before_path = f'{HERE}/content/lab58_before.json'
xbefore_path = f'{HERE}/content/labExtras_before.json'
if not os.path.exists(before_path):
    json.dump(json.load(open(f'{APP}/lab58.json')), open(before_path, 'w'), ensure_ascii=False, indent=1)
    json.dump(json.load(open(f'{APP}/labExtras.json')), open(xbefore_path, 'w'), ensure_ascii=False, indent=1)
lab = json.load(open(before_path))
extras = json.load(open(xbefore_path))
by = {c['mediaId']: c for c in lab}

def parts(spec):
    out = []
    for k, p in enumerate(spec):
        gap = p.startswith('*')
        text = p[1:] if gap else p
        part = {'text': text}
        if gap: part['gap'] = True
        if k == 0 and text == 'to' and not gap: part['plain'] = True
        out.append(part)
    return out

def joined(ps): return ' '.join(p['text'] for p in ps)
changes = []
stale = []
def note(vid, ex, before, after, why=''):
    if before != after: changes.append({'mediaId': vid, 'exercise': ex, 'before': before, 'after': after, 'why': why})

for key, d in draft.items():
    vid = int(key)
    c = by[vid]
    old = copy.deepcopy(c)
    v = c['voices']
    pos = c.get('pos', 'noun')
    # level, sense, senses, writeAt
    note(vid, 'level', old.get('level'), d['level'])
    c['level'] = d['level']; c['sense'] = d['sense']
    if d.get('senses'): c['senses'] = d['senses']
    else: c.pop('senses', None)
    note(vid, 'writeAt', old.get('writeAt'), d['writeAt'])
    c['writeAt'] = d['writeAt']
    # ex 1
    for i, phrase in enumerate(d['taps']):
        if c['taps'][i]['phrase'] != phrase:
            note(vid, f'ex1 phrase {i + 1}', c['taps'][i]['phrase'], phrase)
            c['taps'][i]['phrase'] = phrase
            v['phrases'][i] = voices_new.get(key, {}).get(f'phrase{i + 1}')
    # ex 2
    if d.get('nouns'):
        for i, (word, x, y) in enumerate(d['nouns']):
            n = c['nouns'][i]
            if n['word'] != word:
                note(vid, f'ex2 noun {i + 1}', n['word'], word)
                n['word'] = word
                v['nouns'][i] = voices_new.get(key, {}).get(f'noun{i + 1}')
            if x is not None and (abs(n['x'] - x) > 1e-9 or abs(n['y'] - y) > 1e-9):
                note(vid, f'ex2 point {i + 1} ({word})', f"{n['x']}, {n['y']}", f'{x}, {y}')
                n['x'], n['y'] = x, y
    # ex 3 captions + scenes
    caps_old = c['captions']
    for i, cap in enumerate(d['captions']):
        note(vid, f'ex3 caption {i + 1}', caps_old[i], cap)
    c['captions'] = d['captions']
    vc = {}
    for i, cap in enumerate(d['captions']):
        vc[cap] = v['captions'].get(cap) or voices_new.get(key, {}).get(f'caption{i + 1}')
    v['captions'] = vc
    for i, s in enumerate(d['scenes']):
        note(vid, f'ex3 scene {i + 1}', old['scenes'][i]['scene'], s['scene'])
        note(vid, f'ex3 models {i + 1}', ' | '.join(old['scenes'][i]['models']), ' | '.join(s['models']))
    c['scenes'] = d['scenes']
    # ex 4
    if d.get('timeline'):
        nodes = [{'caption': t[0], 'partner': t[1], **({'form': t[2]} if len(t) > 2 else {})} for t in d['timeline']]
    else:
        nodes = [{'caption': cap, 'partner': p} for cap, p in d['map']]
    note(vid, 'ex4 map/timeline', ' | '.join(f"{n['caption']} [{n['partner']}]" for n in old['mindMap']['nodes']), ' | '.join(f"{n['caption']} [{n['partner']}]" for n in nodes))
    c['mindMap']['nodes'] = nodes
    rows = [parts(r) for r in d['rows']]
    rt = lambda ps: ' '.join(f"[{p['text']}]" if p.get('gap') else p['text'] for p in ps)
    note(vid, 'ex4 rows', ' | '.join(rt(r) for r in old['rows']), ' | '.join(rt(r) for r in rows))
    old_rows = [joined(r) for r in old['rows']]
    old_row_voices = (old['voices'].get('rows') or [None] * len(old['rows']))
    new_row_voices = []
    for i, r in enumerate(rows):
        j = old_rows.index(joined(r)) if joined(r) in old_rows else None
        new_row_voices.append(old_row_voices[j] if j is not None else voices_new.get(key, {}).get(f'row{i + 1}'))
    c['rows'] = rows
    v['rows'] = new_row_voices
    if d.get('ownRow'):
        own = parts(d['ownRow'])
        note(vid, 'ex4 own row', rt(old['ownRow']) if old.get('ownRow') else '', rt(own))
        c['ownRow'] = own
    else:
        note(vid, 'ex4 own row', rt(old['ownRow']) if old.get('ownRow') else '', '(none: the own picture\'s caption is in the ' + ('timeline' if d.get('timeline') else 'map') + ')')
        c.pop('ownRow', None)
    # ex 5
    for i, part in enumerate(d['story']):
        if c['story'][i] != part:
            note(vid, f'ex5 story {"abc"[i]})', c['story'][i], part)
            c['story'][i] = part
            v['story'][i] = voices_new.get(key, {}).get(f'story{i + 1}')
    c['storyModels'] = d['storyModels']
    sp = [{'text': t, 'match': m} for t, m in d['storyPhrases']]
    note(vid, 'ex5 phrase list', ' | '.join(p['text'] for p in old['storyPhrases']), ' | '.join(p['text'] for p in sp))
    c['storyPhrases'] = sp
    note(vid, 'ex5 connector row', old.get('storyConnectors'), d['storyConnectors'])
    c['storyConnectors'] = d['storyConnectors']
    # translations: phrases, nouns, story, rows, ownRow
    T = tr_new.get(key, {})
    for lang in LANGS:
        t = c['tr'][lang]
        def put(field, i, en_changed):
            new = T.get(lang, {}).get(field)
            if new is not None:
                if i is None: t[field] = new
                else: t[field][i] = new[i]
            elif en_changed:
                stale.append(f'{vid} {lang} {field}{"" if i is None else " " + str(i + 1)}')
        for i in range(3):
            put('phrases', i, old['taps'][i]['phrase'] != c['taps'][i]['phrase'])
            put('nouns', i, old['nouns'][i]['word'] != c['nouns'][i]['word'])
            put('story', i, old['story'][i] != c['story'][i])
        if T.get(lang, {}).get('rows') is not None: t['rows'] = T[lang]['rows']
        elif [joined(r) for r in rows] != old_rows: stale.append(f'{vid} {lang} rows')
        if c.get('ownRow'):
            if T.get(lang, {}).get('ownRow') is not None: t['ownRow'] = T[lang]['ownRow']
            elif not old.get('ownRow') or joined(old['ownRow']) != joined(c['ownRow']): stale.append(f'{vid} {lang} ownRow')
        else:
            t.pop('ownRow', None)
    # carousel captions (labExtras for videos, item for pictures) + their translations
    if vid in (900001, 900002):
        car = c['item']['carousel']['pictures']; ctr = c['item'].setdefault('captionsTr', {})
    else:
        car = extras[str(vid)]['carousel']['pictures']; ctr = {lang: extras[str(vid)]['tr'][lang]['captions'] for lang in extras[str(vid)]['tr']}
    for i, pic in enumerate(car):
        oldcap, newcap = pic['caption'], d['captions'][i]
        pic['caption'] = newcap
        pic['voice'] = vc[newcap]
        for lang in LANGS:
            m = ctr.setdefault(lang, {})
            val = m.pop(oldcap, None)
            new = T.get(lang, {}).get('captions', {}).get(newcap)
            if new is not None: m[newcap] = new
            elif oldcap == newcap and val is not None: m[newcap] = val
            else:
                stale.append(f'{vid} {lang} caption {i + 1}')
                if val is not None: m[newcap] = val
    if vid not in (900001, 900002):
        for lang in LANGS:
            extras[str(vid)]['tr'][lang]['captions'] = ctr[lang]
        # the A48 recall rows of the carousel follow the captions (one row per caption; the box = its first word that is
        # not the key word, an article or "to"); their native texts = the captions' translations
        ex = extras[str(vid)]
        keyw = c['mindMap']['centre'].lower()
        idx = [k for k, row in enumerate(ex['recall']) if row['from'] == 'carousel']
        for k, cap in zip(idx, d['captions']):
            words = cap.split(' ')
            g = next(j for j, w in enumerate(words) if w.lower().strip('.?!') not in ('a', 'an', 'the', 'to', keyw, keyw + 's'))
            prts = ([{'text': 'to', 'plain': True}] if words[0] == 'to' else []) + ([{'text': ' '.join(words[1 if words[0] == 'to' else 0:g])}] if g > (1 if words[0] == 'to' else 0) else [])
            prts += [{'text': words[g], 'gap': True, 'accept': [words[g]]}] + ([{'text': ' '.join(words[g + 1:])}] if g + 1 < len(words) else [])
            ex['recall'][k] = {'from': 'carousel', 'parts': prts}
            for lang in LANGS:
                if 'recall' in ex['tr'].get(lang, {}) and k < len(ex['tr'][lang]['recall']):
                    ex['tr'][lang]['recall'][k] = ctr[lang].get(cap, ex['tr'][lang]['recall'][k])

json.dump(lab, open(f'{APP}/lab58.json', 'w'), ensure_ascii=False, indent=1)
json.dump(extras, open(f'{APP}/labExtras.json', 'w'), ensure_ascii=False, indent=1)
rep = opt('--report') or f'{HERE}/changes71.json'
json.dump({'changes': changes, 'stale': stale}, open(rep, 'w'), ensure_ascii=False, indent=1)
missing = [f'{c["mediaId"]} {k}' for c in lab if c['mediaId'] != 461 for k in ('phrases', 'nouns', 'story', 'rows') for i, u in enumerate(c['voices'].get(k) or []) if u is None]
missing += [f'{c["mediaId"]} caption "{k}"' for c in lab if c['mediaId'] != 461 for k, u in c['voices']['captions'].items() if u is None]
print(f'{len(changes)} changes, {len(stale)} stale translations, {len(missing)} recordings missing')
