"""Tinder texts translation: slice inputs, checks, verifier inputs, final rows, SQL.

python3 build.py inputs <lang>          -> slices/<lang>/tNN_in.txt (12 slices of ~305 media, by media id)
python3 build.py check <lang> <tNN>     -> slices/<lang>/tNN_check.json (hard/soft flags per id) + tNN_v_in.txt
python3 build.py final <lang> <tNN>     -> slices/<lang>/tNN_final.jsonl + tNN_upsert.sql (agreed rows only)
python3 build.py retry_in <lang>        -> slices/<lang>/r1_in.txt (rows rejected in all slices, with reasons)
"""
import json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
LANG = {'sk': 'Slovak', 'cz': 'Czech', 'de': 'German', 'ua': 'Ukrainian', 'es': 'Spanish', 'fr': 'French', 'tr': 'Turkish', 'hu': 'Hungarian'}
NSLICE = 12


def load(p):
    d = json.load(open(os.path.join(H, p)))
    return d['rows'] if isinstance(d, dict) else d


def en_rows():
    return sorted(load('en_rows.json'), key=lambda r: r['media_id'])


def meta():
    idx = json.load(open(os.path.join(H, '../tinder_sentences_en/media_index.json')))
    con = {}
    for c in load('concepts_raw.json'):
        con.setdefault(c['media_id'], []).append(c)
    out = {}
    for mid, m in idx.items():
        mid = int(mid)
        words = m['words']
        w = words.split(' (')[0].strip().lower()
        cs = con.get(mid, [])
        c = next((x for x in cs if (x['word'] or '').strip().lower() == w), cs[0] if cs else None)
        out[mid] = {'words': words, 'loc': (c or {}).get('loc') or {}}
    return out


def slices():
    rows = en_rows()
    n = len(rows)
    size = -(-n // NSLICE)
    return [rows[i:i + size] for i in range(0, n, size)]


def sdir(lang):
    d = os.path.join(H, 'slices', lang)
    os.makedirs(d, exist_ok=True)
    return d


def inputs(lang):
    M = meta()
    for k, part in enumerate(slices(), 1):
        L = []
        for r in part:
            m = M.get(r['media_id'], {'words': '?', 'loc': {}})
            L.append(f"{r['media_id']} | {m['words']} | loc: {m['loc'].get(lang, '?')} | tone {r['tone']}\n  TS: {r['ts']}\n  FS: {r['fs']}\n  TP: {r['tp']}\n  FP: {r['fp']}")
        open(os.path.join(sdir(lang), f't{k:02d}_in.txt'), 'w').write('\n'.join(L) + '\n')
    print(lang, 'slices', len(slices()))


def read_out(p):
    out = {}
    if not os.path.exists(p):
        return out
    for line in open(p, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or not re.match(r'^\d+\t', line):
            continue
        parts = line.split('\t')
        out[int(parts[0])] = {'ts': parts[1].strip() if len(parts) > 1 else '', 'fs': parts[2].strip() if len(parts) > 2 else '',
                              'tp': parts[3].strip() if len(parts) > 3 else '', 'fp': parts[4].strip() if len(parts) > 4 else '',
                              'note': parts[5].strip() if len(parts) > 5 else ''}
    return out


def stem_in(loc, text):
    t = text.lower()
    words = [w for w in re.split(r"[\s/,;()]+", (loc or '').lower()) if len(w) >= 3 and w not in ('der', 'die', 'das', 'el', 'la', 'le', 'les', 'los', 'las', 'un', 'une', 'una', 'ein', 'eine', 'sich', 'se', 'si')]
    if not words:
        return True
    for w in words:
        s = w[:max(3, min(len(w) - 2, 5))] if len(w) > 4 else w[:3]
        if s in t:
            return True
    return False


def flags_of(r, en, loc):
    f = []
    for k in ('ts', 'fs', 'tp', 'fp'):
        if not r[k]:
            f.append(f'{k}_empty')
    if f:
        return f, []
    soft = []
    if r['ts'] == r['fs']:
        f.append('ts_equals_fs')
    if r['tp'] == r['fp']:
        f.append('tp_equals_fp')
    for k in ('ts', 'fs'):
        if not re.search(r'[.!?…"»“”]$', r[k]):
            f.append(f'{k}_no_end_punct')
        if len(r[k]) > 110:
            f.append(f'{k}_too_long')
    for k in ('tp', 'fp'):
        n = len(r[k].split())
        if n < 1 or n > 6:
            f.append(f'{k}_words_{n}')
        if len(r[k]) > 48:
            f.append(f'{k}_too_long')
        if r[k].endswith('.'):
            f.append(f'{k}_full_stop')
    for k in ('ts', 'fs', 'tp', 'fp'):
        if r[k] == en[k] and len(en[k].split()) > 2:
            f.append(f'{k}_untranslated')
    if not stem_in(loc, r['ts']):
        soft.append('word_missing?')
    return f, soft


def check(lang, s):
    D = sdir(lang)
    M = meta()
    EN = {r['media_id']: r for r in en_rows()}
    ids = [int(l.split(' |')[0]) for l in open(os.path.join(D, f'{s}_in.txt')) if re.match(r'^\d+ \|', l)]
    out = read_out(os.path.join(D, f'{s}_out.tsv'))
    res, V = {}, []
    for i in ids:
        en = EN[i]
        loc = M.get(i, {}).get('loc', {}).get(lang, '')
        if i not in out:
            res[i] = {'hard': ['missing'], 'soft': []}
            continue
        h, soft = flags_of(out[i], en, loc)
        res[i] = {'hard': h, 'soft': soft}
        if h:
            continue
        r = out[i]
        V.append(f"{i} | {M.get(i, {}).get('words', '?')} | loc: {loc}" + (f" | checker: {', '.join(soft)}" if soft else '') + (f" | translator note: {r['note']}" if r['note'] else '') +
                 f"\n  EN TS: {en['ts']}\n  {lang} TS: {r['ts']}\n  EN FS: {en['fs']}\n  {lang} FS: {r['fs']}\n  EN TP: {en['tp']}\n  {lang} TP: {r['tp']}\n  EN FP: {en['fp']}\n  {lang} FP: {r['fp']}")
    json.dump(res, open(os.path.join(D, f'{s}_check.json'), 'w'), ensure_ascii=False)
    open(os.path.join(D, f'{s}_v_in.txt'), 'w').write('\n'.join(V) + '\n')
    hard = sum(1 for x in res.values() if x['hard'])
    print(lang, s, 'rows', len(ids), 'translated', len(out), 'hard', hard, 'soft', sum(1 for x in res.values() if x['soft']), 'to verify', len(V))


def coverage(p):
    """last_id the verifier says it judged (None = no coverage line)"""
    last = None
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if '"last_id"' in line:
                try:
                    last = int(json.loads(line)['last_id'])
                except Exception:
                    pass
    return last


def verdicts(p):
    out = {}
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            line = line.strip()
            if line.startswith('{'):
                try:
                    v = json.loads(line)
                    out[int(v['id'])] = v
                except Exception:
                    pass
    return out


def q(x):
    return "'" + str(x).replace("'", "''") + "'"


def final(lang, s):
    D = sdir(lang)
    EN = {r['media_id']: r for r in en_rows()}
    out = read_out(os.path.join(D, f'{s}_out.tsv'))
    chk = json.load(open(os.path.join(D, f'{s}_check.json')))
    rej = verdicts(os.path.join(D, f'{s}_verdict.jsonl'))
    vp = os.path.join(D, f'{s}_verdict.jsonl')
    vdone = os.path.exists(vp)
    last = coverage(vp)
    order = [int(i) for i in chk]
    covered = set(order[:order.index(last) + 1]) if last in order else (set(order) if last is None else set())
    fin, left = [], []
    for i, c in chk.items():
        i = int(i)
        if vdone and i not in covered and not c['hard']:
            left.append({'id': i, 'stage': 'no_verdict', 'r': ['not_verified']})
        elif c['hard']:
            left.append({'id': i, 'stage': 'check', 'r': c['hard']})
        elif not vdone:
            left.append({'id': i, 'stage': 'no_verdict', 'r': []})
        elif i in rej:
            left.append({'id': i, 'stage': 'verifier', 'r': rej[i].get('r', []), 'note': rej[i].get('note', '')})
        else:
            fin.append(dict(out[i], id=i))
    with open(os.path.join(D, f'{s}_final.jsonl'), 'w') as f:
        for r in fin:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    json.dump(left, open(os.path.join(D, f'{s}_left.json'), 'w'), ensure_ascii=False, indent=0)
    sql(lang, s, fin, EN)
    print(lang, s, 'final', len(fin), 'left', len(left))


def sql(lang, s, fin, EN):
    D = sdir(lang)
    if not fin:
        open(os.path.join(D, f'{s}_upsert.sql'), 'w').write('select 1;\n')
        return
    vals = ',\n'.join(f"({r['id']},{q(lang)},{q(r['ts'])},{q(r['fs'])},{q(r['tp'])},{q(r['fp'])},{q(EN[r['id']]['tone'])},{q(EN[r['id']]['device'])})" for r in fin)
    open(os.path.join(D, f'{s}_upsert.sql'), 'w').write(
        "begin;\ninsert into public.tinder_sentences (media_id, language_code, true_sentence, false_sentence, true_phrase, false_phrase, tone, device) values\n"
        + vals + "\non conflict (media_id, language_code) do update set true_sentence=excluded.true_sentence, false_sentence=excluded.false_sentence, "
        "true_phrase=excluded.true_phrase, false_phrase=excluded.false_phrase, tone=excluded.tone, device=excluded.device, created_at=now();\ncommit;\n")


def retry_in(lang):
    D = sdir(lang)
    M = meta()
    EN = {r['media_id']: r for r in en_rows()}
    L = []
    for k in range(1, NSLICE + 1):
        s = f't{k:02d}'
        p = os.path.join(D, f'{s}_left.json')
        if not os.path.exists(p):
            continue
        out = read_out(os.path.join(D, f'{s}_out.tsv'))
        for x in json.load(open(p)):
            i = x['id']
            en = EN[i]
            m = M.get(i, {'words': '?', 'loc': {}})
            prev = out.get(i)
            L.append(f"{i} | {m['words']} | loc: {m['loc'].get(lang, '?')} | tone {en['tone']}\n  TS: {en['ts']}\n  FS: {en['fs']}\n  TP: {en['tp']}\n  FP: {en['fp']}"
                     + (f"\n  Rejected {lang}: TS: {prev['ts']} | FS: {prev['fs']} | TP: {prev['tp']} | FP: {prev['fp']}" if prev else '')
                     + f"\n  Reasons: {', '.join(x['r'])}. {x.get('note', '')}")
    open(os.path.join(D, 'r1_in.txt'), 'w').write('\n'.join(L) + '\n')
    print(lang, 'retry rows', len(L))


if __name__ == '__main__':
    cmd = sys.argv[1]
    {'inputs': lambda: inputs(sys.argv[2]), 'check': lambda: check(sys.argv[2], sys.argv[3]),
     'final': lambda: final(sys.argv[2], sys.argv[3]), 'retry_in': lambda: retry_in(sys.argv[2])}[cmd]()
