# A45: checks content/<id>.json (format, tap keys, overlaps, nouns, question, answer, native texts, audio manifest).
#   python3 validate.py <id> [...]   -> prints errors, exit 1 when any. Used by build_sql.py and by the batch runner.
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
def times_of(vid):
    p = f'{HERE}/frames/{vid}/info.json'
    return json.load(open(p))['times'] if os.path.exists(p) else None
def check(vid, need_tr=True, need_audio=True):
    e = []
    try: c = json.load(open(f'{HERE}/content/{vid}.json'))
    except Exception as x: return [f'content file: {x}']
    if c.get('mediaId') != int(vid): e.append('mediaId')
    if c.get('level') not in ('A', 'B'): e.append('level')
    if c.get('defaultVoice') not in ('female', 'male'): e.append('defaultVoice')
    taps = c.get('taps', [])
    if len(taps) != 3: e.append(f'{len(taps)} phrases, not 3')
    times = times_of(vid)
    for i, t in enumerate(taps):
        if not t.get('phrase', '').startswith('to ') or not (2 <= len(t['phrase'].split()) <= 6): e.append(f'phrase {i+1}: "{t.get("phrase")}"')
        if not t.get('target'): e.append(f'phrase {i+1}: no target')
        if t.get('voice') not in ('female', 'male'): e.append(f'phrase {i+1}: voice')
        keys = t.get('keys', [])
        if times is not None:
            miss = [x for x in times if not any(abs(x - k['t']) < 0.01 for k in keys)]
            if miss: e.append(f'phrase {i+1}: no key at t = {miss[:6]}')
        if not any(not k.get('off') for k in keys): e.append(f'phrase {i+1}: target never in the picture')
        for k in keys:
            if k.get('off'): continue
            if not all(n in k for n in 'xywh'): e.append(f'phrase {i+1} t {k.get("t")}: box incomplete'); continue
            if k['x'] < 0 or k['y'] < 0 or k['x'] + k['w'] > 1.0001 or k['y'] + k['h'] > 1.0001 or k['w'] <= 0 or k['h'] <= 0: e.append(f'phrase {i+1} t {k["t"]}: box outside the picture ')
    def key(tap, t):
        for k in tap.get('keys', []):
            if abs(k['t'] - t) < 0.01: return None if k.get('off') else k
    alltimes = sorted({k['t'] for t in taps for k in t.get('keys', [])})
    for t in alltimes:
        for i in range(len(taps)):
            for j in range(i + 1, len(taps)):
                if taps[i].get('target') == taps[j].get('target'): continue
                a, b = key(taps[i], t), key(taps[j], t)
                if a and b and all(n in a for n in 'xywh') and all(n in b for n in 'xywh') and a['x'] < b['x'] + b['w'] - 1e-6 and b['x'] < a['x'] + a['w'] - 1e-6 and a['y'] < b['y'] + b['h'] - 1e-6 and b['y'] < a['y'] + a['h'] - 1e-6:
                    e.append(f't {t}: boxes of "{taps[i]["target"]}" and "{taps[j]["target"]}" overlap')
    for i in range(len(taps)):
        for j in range(i + 1, len(taps)):
            if taps[i].get('target') == taps[j].get('target') and taps[i].get('keys') != taps[j].get('keys'): e.append(f'phrases {i+1} and {j+1}: same target, different boxes')
    nouns = c.get('nouns', [])
    if not (3 <= len(nouns) <= 4): e.append(f'{len(nouns)} nouns, not 3-4')
    if len({n.get('word') for n in nouns}) != len(nouns): e.append('nouns: a word twice')
    for n in nouns:
        if not n.get('word') or not (0.03 <= n.get('x', -1) <= 0.97 and 0.03 <= n.get('y', -1) <= 0.97) or n.get('voice') not in ('female', 'male'): e.append(f'noun {n.get("word")}: word, slot or voice')
    for a in range(len(nouns)):
        for b in range(a + 1, len(nouns)):
            if all(k in nouns[a] and k in nouns[b] for k in 'xy') and abs(nouns[a]['x'] - nouns[b]['x']) < 0.30 and abs(nouns[a]['y'] - nouns[b]['y']) < 0.07: e.append(f'nouns "{nouns[a]["word"]}" and "{nouns[b]["word"]}": slots too close')
    if not isinstance(c.get('stillS'), (int, float)): e.append('stillS')
    q, ans = c.get('question', ''), c.get('answer', [])
    if not (q.endswith('?') and len(q.split()) <= 7): e.append('question: not a question of at most 7 words')
    if not ans or not ans[-1].endswith('.') or not (3 <= len(' '.join(ans).split()) <= 10) or not ans[0][0].isupper(): e.append('answer: chips')
    if c.get('answerVoice') not in ('female', 'male'): e.append('answerVoice')
    if need_tr:
        tr = c.get('tr', {})
        for l in LANGS:
            x = tr.get(l)
            if not x or len(x.get('phrases', [])) != 3 or len(x.get('nouns', [])) != len(nouns) or not x.get('question') or not x.get('answer') or not all(x['phrases']) or not all(x['nouns']): e.append(f'tr {l}')
    if need_audio:
        mp = f'{HERE}/audio/{vid}/manifest.json'
        if not os.path.exists(mp): e.append('audio: no manifest')
        else:
            m = json.load(open(mp)); want = [(t['phrase'], t['voice']) for t in taps] + [(n['word'], n['voice']) for n in nouns] + [(' '.join(ans), c.get('answerVoice'))]
            got = [(x['text'], x['voice']) for x in m['items']]
            if want != got: e.append('audio: manifest does not match the texts / voices')
            for x in m['items']:
                f = f'{HERE}/audio/{vid}/{x["file"]}'
                if not os.path.exists(f) or os.path.getsize(f) < 1500: e.append(f'audio: {x["file"]} missing or empty')
    return e
if __name__ == '__main__':
    bad = 0
    for vid in sys.argv[1:]:
        e = check(vid)
        if e: bad += 1; print(vid, 'ERRORS:', '; '.join(e[:12]))
    print(f'{len(sys.argv) - 1 - bad} ok, {bad} with errors'); sys.exit(1 if bad else 0)
