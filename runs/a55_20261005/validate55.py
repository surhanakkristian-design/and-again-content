# A55: checks content/<lang>/<id>.json against the English source (counts, forms, chips, recall rules) and, with --full, the
# help translations (tr/<lang>/<id>.json) and the audio manifest (audio/<lang>/<id>/manifest.json).
#   python3 validate55.py <lang> <id> [...] [--full]       exit 1 when any error
import json, os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
NATIVES = ['sk', 'cz', 'en', 'de', 'es', 'fr', 'hu', 'tr', 'ua']
ART = {'de': ('der ', 'die ', 'das '), 'es': ('el ', 'la ', 'los ', 'las '), 'fr': ('le ', 'la ', "l'", 'les ')}
TYPES = ('past', 'present', 'future', 'verb coll.', 'noun coll.')
def recall_problems(rows):
    p = []
    if not (4 <= len(rows) <= 10): p.append(f'{len(rows)} recall rows, not 4-10')
    if len([r for r in rows if r.get('from') != 'carousel']) < 4: p.append('fewer than 4 recall rows without the carousel')
    seen = set()
    for r in rows:
        parts = r.get('parts', []); text = ' '.join(x.get('text', '') for x in parts)
        if text in seen: p.append(f'recall "{text}" twice')
        seen.add(text)
        gaps = [x for x in parts if x.get('gap')]
        if len(gaps) != 1: p.append(f'recall "{text}": {len(gaps)} gaps')
        if len(parts) < 2: p.append(f'recall "{text}": fewer than 2 parts')
        for x in parts:
            if not x.get('text') or x['text'] != x['text'].strip(): p.append(f'recall "{text}": empty or padded part')
            if x.get('plain'): p.append(f'recall "{text}": plain part')
            if x.get('gap') and (x.get('accept') or [x['text']])[0] != x['text']: p.append(f'recall "{text}": gap text not first accepted')
    # A55 follow-up: rows that look the same with the gap blanked must accept each other's word (as English "beach / sports bag")
    blank = [' '.join('___' if x.get('gap') else x.get('text', '') for x in r.get('parts', [])) for r in rows]
    for a in range(len(rows)):
        for b in range(len(rows)):
            if a != b and blank[a] == blank[b]:
                ga = [x for x in rows[a]['parts'] if x.get('gap')]; gb = [x for x in rows[b]['parts'] if x.get('gap')]
                if ga and gb and gb[0]['text'] not in (ga[0].get('accept') or [ga[0]['text']]): p.append(f'recall rows look the same with the gap blanked ("{blank[a]}") and do not accept each other')
    return p
def check(lang, vid, full=False):
    e = []
    src = json.load(open(f'{HERE}/src/{vid}.json')); en = src['en']
    try: c = json.load(open(f'{HERE}/content/{lang}/{vid}.json'))
    except Exception as x: return [f'content file: {x}']
    if c.get('mediaId') != vid or c.get('lang') != lang or c.get('level') != src['level']: e.append('mediaId / lang / level')
    if c.get('keyWord') != src['keyWord'][lang]: e.append(f'keyWord {c.get("keyWord")!r} is not the database word {src["keyWord"][lang]!r}')
    taps = c.get('taps', [])
    if len(taps) != len(en['taps']): e.append(f'{len(taps)} phrases, English has {len(en["taps"])}')
    for i, (t, s) in enumerate(zip(taps, en['taps'])):
        ph = t.get('phrase', '')
        if not (2 <= len(ph.split()) <= 7) or ph != ph.strip() or ph.endswith('.') or ph[:1].isupper() and lang != 'de': e.append(f'phrase {i+1}: "{ph}"')
        if ph.lower().startswith('to '): e.append(f'phrase {i+1}: English "to"')
        if not t.get('target'): e.append(f'phrase {i+1}: no target')
        if t.get('voice') != s['voice']: e.append(f'phrase {i+1}: voice {t.get("voice")} != English {s["voice"]}')
    if len({t.get('phrase') for t in taps}) != len(taps): e.append('two phrases the same')
    nouns = c.get('nouns', [])
    if len(nouns) != len(en['nouns']): e.append(f'{len(nouns)} nouns, English has {len(en["nouns"])}')
    for n, s in zip(nouns, en['nouns']):
        w = n.get('word', '')
        if not w.startswith(ART[lang]): e.append(f'noun "{w}": no definite article')
        if lang == 'de' and len(w.split()) > 1 and not w.split()[1][:1].isupper(): e.append(f'noun "{w}": German noun not capitalised')
        if n.get('voice') != s['voice']: e.append(f'noun "{w}": voice')
    if len({n.get('word') for n in nouns}) != len(nouns): e.append('a noun twice')
    q, ans = c.get('question', ''), c.get('answer', [])
    if not q.endswith('?') or len(q.split()) > 9: e.append(f'question "{q}"')
    if lang == 'es' and not q.startswith('¿'): e.append('question: Spanish without ¿')
    if lang == 'fr' and not re.search(r'[\s  ]\?$', q): e.append('question: French without a space before ?')
    if not ans or not all(isinstance(x, str) and x and ' ' not in x for x in ans) or not ans[-1].endswith('.') or not ans[0][:1].isupper() or not (3 <= len(ans) <= 11): e.append(f'answer chips {ans}')
    if c.get('answerVoice') not in ('female', 'male'): e.append('answerVoice')
    car = c.get('carousel', [])
    if len(car) != len(en['carousel']): e.append(f'{len(car)} captions, English has {len(en["carousel"])}')
    for x, s in zip(car, en['carousel']):
        if x.get('en') != s['caption']: e.append(f'caption: en {x.get("en")!r} != {s["caption"]!r}')
        if not x.get('caption') or x.get('type') not in TYPES or not isinstance(x.get('hasKeyWord'), bool): e.append(f'caption {x.get("en")!r}: caption / type / hasKeyWord')
        if x.get('hasKeyWord') is False and not x.get('note'): e.append(f'caption {x.get("caption")!r}: no note why the key word is missing')
    tenses = [x.get('type') for x in car if x.get('type') in ('past', 'present', 'future')]
    if len(tenses) != len(set(tenses)): e.append('two captions of the same tense')
    if len({x.get('caption') for x in car}) != len(car): e.append('a caption twice')
    rec = c.get('recall', [])
    if [r.get('from') for r in rec] != [r['from'] for r in en['recall']]: e.append('recall rows: not the English sources in the English order')
    e += recall_problems(rec)
    if full:
        try: tr = json.load(open(f'{HERE}/tr/{lang}/{vid}.json'))
        except Exception as x: tr = None; e.append(f'tr file: {x}')
        if tr is not None:
            for l in NATIVES:
                if l == lang: continue
                x = tr.get(l)
                if not x: e.append(f'tr {l}: missing'); continue
                if len(x.get('phrases', [])) != len(taps) or not all(x['phrases']): e.append(f'tr {l}: phrases')
                if len(x.get('nouns', [])) != len(nouns) or not all(x['nouns']): e.append(f'tr {l}: nouns')
                if not x.get('question') or not x.get('answer'): e.append(f'tr {l}: question / answer')
                if set((x.get('captions') or {}).keys()) != {y['caption'] for y in car} or not all((x.get('captions') or {}).values()): e.append(f'tr {l}: captions')
                if len(x.get('recall', [])) != len(rec) or not all(x['recall']): e.append(f'tr {l}: recall')
            if lang in tr: e.append(f'tr: the learning language {lang} itself')
        mp = f'{HERE}/audio/{lang}/{vid}/manifest.json'
        if not os.path.exists(mp): e.append('audio: no manifest')
        else:
            m = json.load(open(mp))
            want = [(t['phrase'], t['voice']) for t in taps] + [(n['word'], n['voice']) for n in nouns] + [(' '.join(ans), c.get('answerVoice'))] + [(x['caption'], src['defaultVoice']) for x in car]
            if want != [(x['text'], x['voice']) for x in m['items']]: e.append('audio: manifest does not match the texts / voices')
            for x in m['items']:
                f = f'{HERE}/audio/{lang}/{vid}/{x["file"]}'
                if not os.path.exists(f) or os.path.getsize(f) < 1500: e.append(f'audio: {x["file"]} missing or empty')
    return e
if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]; full = '--full' in sys.argv
    lang, ids = args[0], [int(a) for a in args[1:]]
    bad = 0
    for vid in ids:
        e = check(lang, vid, full)
        if e: bad += 1; print(lang, vid, 'ERRORS:', '; '.join(e[:15]))
    print(f'{lang}: {len(ids) - bad} ok, {bad} with errors'); sys.exit(1 if bad else 0)
