"""Deterministic pass (no model). A row NEEDS a mark when full_sentence (trimmed) ends without . ! ? AND does not end
legitimately (closing quote/bracket, ellipsis, emoji, abbreviation) AND is not type 69 (definition template, no stop by
the documented convention of validate_part.stem_sentence). The mark comes from the English row of the same exercise.
Rows are SURE when: the English mark is '.', the native shows no question signal, and derive(intro, answer) equals
full_sentence + '.' (the only change is the mark). Everything else is UNSURE and goes to the subagents."""
import json, collections, sys, os, re
sys.path.insert(0, os.path.expanduser('~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/scripts'))
import validate_part as vp
H = os.path.dirname(os.path.abspath(__file__))
CLOSERS = '"\'”“»«)]’›‹'
ABBR = re.compile(r'(?i)^(etc|vs|dr|mr|mrs|ms|st|jr|sr|inc|ltd|bzw|usw|vb|stb|atď|apod|tzn|tj|resp|napr|např|ok)$')
QSIG = {
    'tr': re.compile(r'(?i)(^|\s)m[ıiuü](y[ıiuü]m|s[ıiuü]n|y[ıiuü]z|s[ıiuü]n[ıiuü]z|d[ıiuü]r|yd[ıiuü]|ym[ıiuü]ş|ler)?(\s|$)|değil mi'),
    'ua': re.compile(r'(?i)(^|[\s«])(чи|хіба|невже)\s'),
    'hu': re.compile(r'(?i)\bvajon\b'),
    'de': re.compile(r'^(Wer|Was|Wo|Warum|Wieso|Weshalb|Wie|Wann|Welche[rsnm]?)\s'),
    'cz': re.compile(r'^(Kde|Proč|Kdo|Co|Jak|Kdy|Který|Která|Které)\s'),
    'sk': re.compile(r'^(Kde|Prečo|Kto|Čo|Ako|Kedy|Ktorý|Ktorá|Ktoré)\s'),
}
def en_mark(s):
    s = (s or '').rstrip().rstrip(CLOSERS + ' ')
    return s[-1:] if s[-1:] in '.!?' else None
def is_emoji(ch):
    return ord(ch) >= 0x2190 and not ch.isalnum()

def classify(rows):
    by = collections.defaultdict(dict)
    for r in rows: by[r['exercise_id']][r['language_code']] = r
    out = []
    for r in rows:
        fs = (r['full_sentence'] or '').rstrip()
        if not fs or fs[-1] in '.!?':
            continue
        L = r['language_code']; t = r['exercise_type_id']
        base = dict(id=r['id'], exercise_id=r['exercise_id'], lang=L, type=t)
        if t == 69:
            out.append({**base, 'cls': 'legit', 'why': 'type 69 definition template (no stop by convention)'}); continue
        last = fs[-1]; lastw = fs.split()[-1].strip(CLOSERS)
        if last in CLOSERS:
            out.append({**base, 'cls': 'legit', 'why': 'closing quote/bracket'}); continue
        if fs.endswith('…') or fs.endswith('...'):
            out.append({**base, 'cls': 'legit', 'why': 'ellipsis'}); continue
        if is_emoji(last):
            out.append({**base, 'cls': 'legit', 'why': 'emoji'}); continue
        if ABBR.match(lastw):
            out.append({**base, 'cls': 'unsure', 'why': 'ends on an abbreviation-like word'}); continue
        if not last.isalnum():
            out.append({**base, 'cls': 'unsure', 'why': f'ends on {last!r}'}); continue
        en = by[r['exercise_id']].get('en')
        m = en_mark(en['full_sentence'] if en else None) if L != 'en' else None
        der = vp.derive_full_sentence(r['intro_text'] or '', r['correct_answer'] or '', L, t)
        gapend = (r['intro_text'] or '').rstrip().endswith('...')
        why = []
        if m is None: why.append('no English mark')
        elif m != '.': why.append(f'English mark {m}')
        if QSIG.get(L) and QSIG[L].search(fs): why.append('native question signal')
        if not gapend: why.append('gap not sentence-final (intro would change)')
        if der != fs + '.': why.append('derive differs beyond the mark')
        if why:
            out.append({**base, 'cls': 'unsure', 'why': '; '.join(why), 'en_mark': m}); continue
        out.append({**base, 'cls': 'sure', 'mark': '.', 'field': 'full_sentence', 'old_fs': r['full_sentence'],
                    'new_fs': fs + '.', 'intro_unchanged': True})
    return out

if __name__ == '__main__':
    rows = json.load(open(f'{H}/work/snapshot_before.json'))
    out = classify(rows)
    json.dump(out, open(f'{H}/work/classified.json', 'w'), ensure_ascii=False, indent=0)
    c = collections.Counter((x['lang'], x['cls']) for x in out)
    for k in sorted(c): print(k, c[k])
    w = collections.Counter(x['why'] for x in out if x['cls'] == 'unsure'); print(w.most_common())
