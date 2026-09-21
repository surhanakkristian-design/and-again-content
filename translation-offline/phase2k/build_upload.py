#!/usr/bin/env python3
"""Phase 2K Part 1.2 + 1.3 (0 model calls). Restores the 4 references B3 truncated (ex 927, 22385, 35040, 41408) to their
pre-B3 value (B3_diff 'before' == phase2i/upload value), writes upload/annotations_sk_final.jsonl + upload_sk_final.xlsx +
UPLOAD_README.md + RESTORE_4.json, and scans BOTH files (SK final, CZ phase2i/upload) for references ending in a
preposition or an article -> analysis/ref_endings.json."""
import json, os, re, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
P2I_UP, P2J_UP, OUT = os.path.join(TOFF, 'phase2i', 'upload'), os.path.join(TOFF, 'phase2j', 'upload'), os.path.join(HERE, 'upload')
SK_FINAL = os.path.join(OUT, 'annotations_sk_final.jsonl')
CZ_FILE = os.path.join(P2I_UP, 'annotations_cz_fixed.jsonl')
EXS = (927, 22385, 35040, 41408)
ARTICLES = {'a', 'an', 'the'}
PREPS = set('''about above across after against along among around at before behind below beneath beside besides between
beyond by despite down during except for from in inside into like near of off on onto out outside over past since than
through throughout till to toward towards under underneath until up upon via with within without'''.split())
# STRICT = articles + prepositions that cannot close an English clause as a particle (the TEST fails on these);
# the broad PREPS hits (particles / stranded prepositions: up, in, on, for, before ...) are listed for review only.
STRICT = ARTICLES | {'of', 'onto', 'into', 'upon', 'among', 'between', 'beneath', 'via', 'despite', 'during', 'than',
                     'toward', 'towards', 'to', 'from', 'with', 'at', 'by'}
COLS = ('exercise_id', 'language_code', 'level', 'src', 'en', 'structure_json')


def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


def last_word(s):
    t = re.findall(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?", s or '')
    return t[-1].lower() if t else ''


def scan_endings(path, lang):
    hits = []
    for r in jl(path):
        for i, s in enumerate(r.get('v') or []):
            w = last_word(s)
            if w in ARTICLES or w in PREPS:
                hits.append({'lang': lang, 'exercise_id': r['exercise_id'], 'ref_index': i, 'last': w,
                             'kind': 'article' if w in ARTICLES else 'preposition', 'strict': w in STRICT, 'ref': s, 'src': r.get('src')})
    return hits


def build():
    rows = jl(os.path.join(P2J_UP, 'annotations_sk_fixed.jsonl'))
    base = {r['exercise_id']: r for r in jl(os.path.join(P2I_UP, 'annotations_sk_fixed.jsonl'))}
    diff = jl(os.path.join(P2J_UP, 'B3_diff.jsonl'))
    rest = []
    for r in rows:
        if r['exercise_id'] not in EXS:
            continue
        ds = [d for d in diff if d.get('lang') == 'sk' and d.get('exercise_id') == r['exercise_id'] and d.get('action') == 'replaced']
        assert ds, ('no B3 replacement for', r['exercise_id'])
        v = list(r['v'])
        for d in ds:
            idx = [i for i, s in enumerate(v) if s == d['after']]
            assert len(idx) == 1, (r['exercise_id'], d, v)
            assert d['before'] in base[r['exercise_id']]['v'], ('before not in pre-B3 row', r['exercise_id'])
            v[idx[0]] = d['before']
            rest.append({'exercise_id': r['exercise_id'], 'ref_index': idx[0], 'b3_value': d['after'], 'restored': d['before'],
                         'pre_b3_v': base[r['exercise_id']]['v'], 'final_v': v, 'src': r['src']})
        r['v'] = v
        r['en'] = v[0]
    assert len(rows) == 4064 and len({r['exercise_id'] for r in rows}) == 4064
    assert all(isinstance(r['exercise_id'], int) and r['v'] and r['v'][0] == r['en'] for r in rows)
    assert sorted({x['exercise_id'] for x in rest}) == sorted(EXS)
    os.makedirs(OUT, exist_ok=True)
    with open(SK_FINAL, 'w', encoding='utf-8') as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    import openpyxl
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = 'sk'; ws.append(list(COLS))
    for r in rows:
        ws.append([r['exercise_id'], r['language_code'], r['level'], r['src'], r['en'], json.dumps(r, ensure_ascii=False)])
    wb.save(os.path.join(OUT, 'upload_sk_final.xlsx'))
    json.dump(rest, open(os.path.join(OUT, 'RESTORE_4.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    hits = scan_endings(SK_FINAL, 'sk') + scan_endings(CZ_FILE, 'cz')
    os.makedirs(os.path.join(HERE, 'analysis'), exist_ok=True)
    json.dump(hits, open(os.path.join(HERE, 'analysis', 'ref_endings.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(os.path.join(OUT, 'UPLOAD_README.md'), 'w', encoding='utf-8').write(
        '# Phase 2K - final Slovak upload\n\n'
        'Files: `upload_sk_final.xlsx` (sheet `sk`; columns %s) + `annotations_sk_final.jsonl` (structure_json = the jsonl row).\n'
        '4,064 rows; `exercise_id` is an integer on every row; `v[0] == en` on every row.\n\n'
        'Source: `phase2j/upload/annotations_sk_fixed.jsonl` (B3-corrected) with the 4 references B3 truncated '
        '(exercise_id 927, 22385, 35040, 41408) restored to their value before B3 (`phase2i/upload`); detail in `RESTORE_4.json`.\n\n'
        '**`v` is display-only and no longer grades.** Since Phase 2K the checker is SOURCE-ONLY: it judges the answer '
        'against the Slovak sentence. The stored English reference (`en`, `v`) stays in the data and is shown to the '
        'learner as the correct answer when they are wrong; it is never used to grade.\n\n'
        'Reference-ending scan (preposition or article, SK final + CZ): `../analysis/ref_endings.json` (%d hits: SK %d, CZ %d).\n'
        % (', '.join(COLS), len(hits), sum(h['lang'] == 'sk' for h in hits), sum(h['lang'] == 'cz' for h in hits)))
    return rest, hits


if __name__ == '__main__':
    rest, hits = build()
    for x in rest:
        print('RESTORED ex %d [%d]: %r -> %r' % (x['exercise_id'], x['ref_index'], x['b3_value'], x['restored']))
    print('ENDING HITS broad', len(hits), 'strict', sum(h['strict'] for h in hits))
    for h in hits:
        if not h['strict']:
            continue
        print('  %s ex %s [%d] %s %r: %s' % (h['lang'], h['exercise_id'], h['ref_index'], h['kind'], h['last'], h['ref']))
