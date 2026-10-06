# A59 (from A58 + owner rule 1 of A59: the key-word phrase first): rule check of content/<id>.json (the English lab set). python3 validate58.py <id>... ; exit 1 on any error.
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LIVE = {r['media_id']: r for r in json.load(open(f'{HERE}/data/live_rows.json'))}
SC = json.load(open(f'{HERE}/data/scenes.json'))
def keys_of(vid, k):
    if isinstance(k, str):
        m = re.fullmatch(r'live:([123])', k)
        return LIVE[vid]['taps'][int(m.group(1)) - 1]['keys'] if m else None
    return k
def region(keys, t):
    before, after = keys[0], None
    for k in keys:
        if k['t'] <= t: before = k
        else: after = k; break
    if before.get('off'): return None
    b = dict(x=before['x'], y=before['y'], w=before['w'], h=before['h'])
    if not after or after.get('off') or t <= before['t']: return b
    s = (t - before['t']) / (after['t'] - before['t'])
    return {q: b[q] + (after[q] - b[q]) * s for q in b}
def check(vid):
    e = []; c = json.load(open(f'{HERE}/content/{vid}.json')); src = json.load(open(f'{HERE}/data/{vid}.json'))
    dur = SC[str(vid)]['duration']
    if c.get('mediaId') != vid: e.append('mediaId')
    taps = c.get('taps', [])
    if len(taps) != 3: e.append(f'{len(taps)} taps, not 3')
    words = lambda s: s.lower().split()
    for i, t in enumerate(taps):
        p = t.get('phrase', '')
        if not re.fullmatch(r"to( [A-Za-z'-]+){2,7}", p): e.append(f'tap {i+1} "{p}": not "to" + 2-7 words')
        if not t.get('target', '').startswith('the '): e.append(f'tap {i+1}: target "{t.get("target")}" without "the"')
        for part in ('verb', 'noun'):
            v = t.get(part, '')
            if not v or not re.search(r'(^| )' + re.escape(v) + r'( |$)', p): e.append(f'tap {i+1}: {part} "{v}" is not a whole part of "{p}"')
        if t.get('verb') and t.get('noun') and p.find(t['verb']) > p.find(t['noun']): e.append(f'tap {i+1}: the verb stands after the noun')
        ks = keys_of(vid, t.get('keys'))
        if not ks: e.append(f'tap {i+1}: keys missing'); continue
        if ks[0]['t'] > 0.26 + float(src.get('startS') or 0): e.append(f'tap {i+1}: first key late')
        if ks[-1]['t'] < dur - 0.8: e.append(f'tap {i+1}: last key at {ks[-1]["t"]} early (clip {dur} s)')
        for a, b in zip(ks, ks[1:]):
            if not b['t'] > a['t']: e.append(f'tap {i+1}: keys not in time order at {b["t"]}')
            if b['t'] - a['t'] > 0.75: e.append(f'tap {i+1}: gap before {b["t"]}')
        for k in ks:
            if k.get('off'): continue
            if not (k['x'] >= 0 and k['y'] >= 0 and k['x'] + k['w'] <= 1.0001 and k['y'] + k['h'] <= 1.0001): e.append(f'tap {i+1}: box outside at {k["t"]}')
            if k['w'] < 0.04 or k['h'] < 0.04: e.append(f'tap {i+1}: box too small at {k["t"]}')
        if all(k.get('off') for k in ks): e.append(f'tap {i+1}: never in the picture')
    for i in range(len(taps)):
        for j in range(i + 1, len(taps)):
            if taps[i]['target'] == taps[j]['target']: continue
            a_k, b_k = keys_of(vid, taps[i]['keys']), keys_of(vid, taps[j]['keys'])
            if not a_k or not b_k: continue
            for t in sorted({k['t'] for k in a_k + b_k}):
                a, b = region(a_k, t), region(b_k, t)
                if a and b and a['x'] < b['x'] + b['w'] and b['x'] < a['x'] + a['w'] and a['y'] < b['y'] + b['h'] and b['y'] < a['y'] + a['h']:
                    e.append(f'regions of "{taps[i]["target"]}" and "{taps[j]["target"]}" overlap at {t}'); break
    if len({t['phrase'] for t in taps}) != len(taps): e.append('a phrase twice')
    # A59 rule 1: phrase 1 holds the key word as its noun; that phrase (inflected) is in the story
    kwb = re.sub(r'^(a|an|the|to) ', '', c.get('keyWord', ''))
    if taps:
        t1 = taps[0]
        if not re.search(r'(^| )' + re.escape(kwb) + r"( |$|'s)", t1.get('phrase', '')): e.append(f'rule 1: phrase 1 "{t1.get("phrase")}" lacks the key word "{kwb}"')
        if re.sub(r'^(a|an|the) ', '', t1.get('noun', '')) != kwb: e.append(f'rule 1: the noun of phrase 1 is "{t1.get("noun")}", not the key word "{kwb}"')
        if not any(re.search(r'\b' + re.escape(kwb), s_, re.I) for s_ in c.get('story', [])): e.append('rule 1: the story never names the key word')
    for i, t in enumerate(taps):
        if 'alsoKeys' in t:
            ak = keys_of(vid, t['alsoKeys'])
            if not ak: e.append(f'tap {i+1}: alsoKeys invalid')
            for j, u in enumerate(taps):
                if u['target'] == t['target'] or j == i: continue
                bk = keys_of(vid, u['keys'])
                for tt in sorted({k['t'] for k in ak + bk}):
                    a, b = region(ak, tt), region(bk, tt)
                    if a and b and a['x'] < b['x'] + b['w'] and b['x'] < a['x'] + a['w'] and a['y'] < b['y'] + b['h'] and b['y'] < a['y'] + a['h']:
                        e.append(f'the second doer of "{t["phrase"]}" overlaps "{u["target"]}" at {tt}'); break
    nouns = c.get('nouns', [])
    if len(nouns) != 3: e.append(f'{len(nouns)} nouns, not 3')
    for i, (n, t) in enumerate(zip(nouns, taps)):
        w = n.get('word', '')
        if not re.fullmatch(r"(an? )?[a-z][a-z'-]*( [a-z][a-z'-]*){0,3}", w): e.append(f'noun "{w}": form')
        base = re.sub(r'^(a|an|the) ', '', t.get('noun', '')); wb = re.sub(r'^(a|an) ', '', w)
        if base != wb: e.append(f'noun {i+1} "{w}" is not the noun of phrase {i+1} ("{t.get("noun")}")')
        if not (0.08 <= n.get('x', -1) <= 0.92 and 0.08 <= n.get('y', -1) <= 0.92): e.append(f'noun "{w}": slot outside 0.08-0.92')
        if n.get('x', 0) > 0.85 and 0.35 <= n.get('y', 0) <= 0.70: e.append(f'noun "{w}": slot on the rail strip')
    if len({n.get('word') for n in nouns}) != len(nouns): e.append('a noun twice')
    for i in range(len(nouns)):
        for j in range(i + 1, len(nouns)):
            a, b = nouns[i], nouns[j]
            if abs(a['x'] - b['x']) < 0.35 and abs(a['y'] - b['y']) < 0.12: e.append(f'slots of "{a["word"]}" and "{b["word"]}" too close')
    fill = c.get('fill', [])
    if len(fill) != 3 or any(f.get('gap') not in ('verb', 'noun') for f in fill): e.append('fill: 3 entries with gap verb|noun')
    elif {f['gap'] for f in fill} != {'verb', 'noun'}: e.append('fill: needs at least one verb and one noun gap')
    car = [x['caption'] for x in src['en']['carousel']]
    mm = c.get('mindMap', [])
    if [m.get('caption') for m in mm] != car: e.append(f'mindMap captions are not the carousel captions in order: {car}')
    kw = re.sub(r'^(a|an|the|to) ', '', c.get('keyWord', ''))
    for m in mm:
        p = m.get('partner', '')
        if not p or p not in m.get('caption', ''): e.append(f'partner "{p}" not in "{m.get("caption")}"')
        if kw and kw in p.split(): e.append(f'partner "{p}" holds the key word')
        if re.match(r'^(to|a|an|the) ', p) or p in ('to', 'a', 'the'): e.append(f'partner "{p}" starts with to / an article')
    pieces = [m.get('partner', '') for m in mm] + [t.get(f.get('gap', ''), '') for t, f in zip(taps, fill)]
    if len({p.lower() for p in pieces}) != len(pieces): e.append(f'the bank pieces are not all different: {pieces}')
    story = c.get('story', [])
    limit = 12 if src['level'] == 'A' else 16
    if len(story) != 3: e.append(f'{len(story)} story sentences, not 3')
    for s in story:
        if not re.fullmatch(r"[A-Z].*[.!]", s or ''): e.append(f'story "{s}": capital + . or !')
        if len(s.split()) > limit: e.append(f'story "{s}": {len(s.split())} words > {limit}')
        if re.search(r'\blaugh(s|ed|ing)? about\b', s or ''): e.append('laugh about -> laugh at')
    for t in taps:
        if re.search(r'\blaugh about\b', t['phrase']): e.append('laugh about -> laugh at')
    if not c.get('cutVerdict'): e.append('cutVerdict missing')
    return e
bad = 0
for vid in map(int, sys.argv[1:]):
    try: errs = check(vid)
    except Exception as x: errs = [f'cannot check: {x!r}']
    print(f'{vid}: ' + ('OK' if not errs else f'{len(errs)} errors\n  ' + '\n  '.join(errs))); bad += bool(errs)
sys.exit(1 if bad else 0)
