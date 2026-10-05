# A45 batch steps.
#   python3 batch.py status <batch>        which videos have content / a verdict
#   python3 batch.py trsource <batch>      tr/<batch>/source.json from the videos with VERDICT PASS / FIXED
#   python3 batch.py finish <batch>        merge tr/<batch>/<code>.json into the content, record audio, validate, build the SQL
import json, os, sys, subprocess, re
HERE = os.path.dirname(os.path.abspath(__file__))
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
cmd, b = sys.argv[1], sys.argv[2]
plan = json.load(open(f'{HERE}/data/{b}.plan.json')); ids = plan['ids']
def verdict(i):
    p = f'{HERE}/verify/{i}.md'
    if not os.path.exists(p): return None
    m = re.match(r'\s*VERDICT:\s*(PASS|FIXED|FAIL)', open(p).read())
    c = f'{HERE}/content/{i}.json'
    # a content file changed after its verdict (another agent's stray script) must be verified again
    if m and m.group(1) != 'FAIL' and os.path.exists(c) and not os.path.exists(f'{HERE}/audio/{i}/manifest.json') and os.path.getmtime(c) > os.path.getmtime(p) + 2: return 'STALE'
    return m.group(1) if m else 'UNREADABLE'
def state():
    s = {}
    for i in ids:
        has = os.path.exists(f'{HERE}/content/{i}.json'); skip = os.path.exists(f'{HERE}/content/{i}.skip')
        s[i] = ('skip' if skip and not has else 'none' if not has else 'written', verdict(i))
    return s
if cmd == 'status':
    s = state(); import collections
    print(collections.Counter(s.values()))
    print('no content:', [i for i, v in s.items() if v[0] == 'none'])
    print('no verdict:', [i for i, v in s.items() if v[0] != 'none' and v[1] is None])
    print('fail:', [i for i, v in s.items() if v[1] in ('FAIL', 'UNREADABLE')])
    print('stale:', [i for i, v in s.items() if v[1] == 'STALE'])
elif cmd == 'trsource':
    V = {int(x['id']): x for x in json.load(open(f'{HERE}/data/videos.json'))}
    s = state(); src = {}
    for i in ids:
        if s[i][1] not in ('PASS', 'FIXED'): continue
        c = json.load(open(f'{HERE}/content/{i}.json'))
        src[str(i)] = {'about': V[i]['asset_description'], 'level': c['level'], 'phrases': [{'en': t['phrase'], 'target': t['target']} for t in c['taps']],
                       'nouns': [n['word'] for n in c['nouns']], 'question': c['question'], 'answer': ' '.join(c['answer'])}
    os.makedirs(f'{HERE}/tr/{b}', exist_ok=True)
    json.dump(src, open(f'{HERE}/tr/{b}/source.json', 'w'), ensure_ascii=False, indent=1)
    print(len(src), 'videos in tr source')
elif cmd == 'finish':
    src = json.load(open(f'{HERE}/tr/{b}/source.json')); tr = {l: json.load(open(f'{HERE}/tr/{b}/{l}.json')) for l in LANGS}
    done, failed = [], {}
    for i in ids:
        v = verdict(i)
        if str(i) not in src:
            failed[i] = 'no content' if v is None else f'verifier: {v}'; continue
        c = json.load(open(f'{HERE}/content/{i}.json')); s = src[str(i)]
        if [t['phrase'] for t in c['taps']] != [p['en'] for p in s['phrases']] or [n['word'] for n in c['nouns']] != s['nouns'] or c['question'] != s['question'] or ' '.join(c['answer']) != s['answer']:
            failed[i] = 'content changed after the translation source was built'; continue
        c['tr'] = {l: tr[l][str(i)] for l in LANGS if str(i) in tr[l]}
        json.dump(c, open(f'{HERE}/content/{i}.json', 'w'), ensure_ascii=False, indent=1)
        done.append(i)
    subprocess.run(['python3', f'{HERE}/tts.py'] + [str(i) for i in done], check=True)
    from validate import check
    ok = []
    for i in done:
        e = check(i)
        if e: failed[i] = 'validate: ' + '; '.join(e[:3])
        else: ok.append(i)
    subprocess.run(['python3', f'{HERE}/build_sql.py', b] + [str(i) for i in ok], check=True, cwd=HERE)
    json.dump({'batch': b, 'done': ok, 'failed': {str(k): v for k, v in failed.items()}}, open(f'{HERE}/data/{b}.result.json', 'w'), indent=1)
    print(b, len(ok), 'done;', len(failed), 'failed', failed)
