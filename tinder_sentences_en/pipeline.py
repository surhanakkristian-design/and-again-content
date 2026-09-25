"""Slice bookkeeping between the agent rounds.

python3 pipeline.py retry_in s01   -> slices/s01_retry_in.md from verifier rejects + hard check flags
python3 pipeline.py final s01      -> slices/s01_final.jsonl (agreed rows) + s01_left.json (still rejected)
python3 pipeline.py sql s01        -> slices/s01_upsert.sql (English rows of the agreed set)
"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'slices')
SOFT = {'device_repeat'}


def jl(p):
    return [json.loads(l) for l in open(p) if l.strip()] if os.path.exists(p) else []


def hard(flags, verdict_ok):
    out = [f for f in flags if f not in SOFT]
    if verdict_ok:  # the verifier read the sentence; trust it on irregular word forms
        out = [f for f in out if not f.endswith('word_missing?')]
    return out


def flags_for(rows):
    res, prev = {}, None
    for r in rows:
        res[r['id']] = check.check_row(r, prev)
        prev = r.get('device')
    return res


def round_result(rows, verdicts):
    V = {v['id']: v for v in verdicts}
    F = flags_for(rows)
    ok, bad = [], []
    for r in rows:
        v = V.get(r['id'])
        if v and v.get('v') == 'R' and v.get('r') == ['tone'] and '!' not in r['ts'] + r['fs'] and r['tone'] != 'chill':
            # only the tone LABEL was wrong on a plain sentence: relabel it chill (counted in the report)
            r['tone_was'] = r['tone']; r['tone'] = 'chill'
            v = dict(v, v='A', relabelled=True)
        vok = bool(v) and v.get('v') == 'A'
        h = hard(F[r['id']], vok)
        (ok if vok and not h else bad).append((r, v, h))
    return ok, bad


def blocks(s):
    txt = open(os.path.join(D, f'{s}_in.md')).read()
    out = {}
    for b in txt.split('### ')[1:]:
        out[int(b.split(' |')[0])] = '### ' + b.strip()
    return out


def retry_in(s):
    rows = jl(os.path.join(D, f'{s}_out.jsonl'))
    _, bad = round_result(rows, jl(os.path.join(D, f'{s}_verdict.jsonl')))
    B = blocks(s)
    L = []
    for r, v, h in bad:
        reasons = (v or {}).get('r', []) + h
        note = (v or {}).get('note', '') if v else 'no verdict'
        L.append(f"{B[r['id']]}\nPrevious: TRUE: {r['ts']} | FALSE: {r['fs']} | true phrase: {r['tp']} | false phrase: {r['fp']} | tone {r['tone']}, device {r['device']}\nReasons: {', '.join(reasons)}. {note}")
    open(os.path.join(D, f'{s}_retry_in.md'), 'w').write('\n\n'.join(L) + '\n')
    print(s, 'retry rows:', len(bad))


def final(s):
    rows = jl(os.path.join(D, f'{s}_out.jsonl'))
    ok1, bad1 = round_result(rows, jl(os.path.join(D, f'{s}_verdict.jsonl')))
    retry = jl(os.path.join(D, f'{s}_retry.jsonl'))
    ok2, bad2 = round_result(retry, jl(os.path.join(D, f'{s}_verdict2.jsonl'))) if retry else ([], [])
    done2 = {r['id'] for r, _, _ in ok2}
    fin = [dict(r, stretched=bool(v and v.get('stretched')), round=1) for r, v, _ in ok1 if r['id'] not in done2] + \
          [dict(r, stretched=bool(v and v.get('stretched')), round=2) for r, v, _ in ok2]
    retried = {r['id'] for r in retry}
    left = [{'id': r['id'], 'r1': (v or {}).get('r', []) + h, 'note1': (v or {}).get('note', '')} for r, v, h in bad1 if r['id'] not in done2]
    L2 = {r['id']: ((v or {}).get('r', []) + h, (v or {}).get('note', '')) for r, v, h in bad2}
    for x in left:
        x['retried'] = x['id'] in retried
        if x['id'] in L2:
            x['r2'], x['note2'] = L2[x['id']]
    with open(os.path.join(D, f'{s}_final.jsonl'), 'w') as f:
        for r in fin:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    json.dump({'r1_rejects': [{'id': r['id'], 'r': (v or {}).get('r', []) + h, 'note': (v or {}).get('note', ''),
                               'ts': r['ts'], 'fs': r['fs'], 'tp': r['tp'], 'fp': r['fp']} for r, v, h in bad1],
               'left': left}, open(os.path.join(D, f'{s}_left.json'), 'w'), ensure_ascii=False, indent=0)
    print(s, 'final', len(fin), 'r1 rejects', len(bad1), 'retry ok', len(ok2), 'left', len(left))


def q(x):
    return "'" + str(x).replace("'", "''") + "'"


def sql(s):
    fin = jl(os.path.join(D, f'{s}_final.jsonl'))
    vals = ',\n'.join(f"({r['id']},'en',{q(r['ts'])},{q(r['fs'])},{q(r['tp'])},{q(r['fp'])},{q(r['tone'])},{q(r['device'])})" for r in fin)
    open(os.path.join(D, f'{s}_upsert.sql'), 'w').write(
        "begin;\ninsert into public.tinder_sentences (media_id, language_code, true_sentence, false_sentence, true_phrase, false_phrase, tone, device) values\n"
        + vals + "\non conflict (media_id, language_code) do update set true_sentence=excluded.true_sentence, false_sentence=excluded.false_sentence, "
        "true_phrase=excluded.true_phrase, false_phrase=excluded.false_phrase, tone=excluded.tone, device=excluded.device, created_at=now();\ncommit;\n")
    print(s, 'sql rows', len(fin))


if __name__ == '__main__':
    {'retry_in': retry_in, 'final': final, 'sql': sql}[sys.argv[1]](sys.argv[2])
