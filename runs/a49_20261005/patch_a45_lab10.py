# A49: patches A45's FINISHED batch lab10 (written to the database 5 Oct 2026, 10:16 UTC) with the A49 content of 7071
# (king), 4265 (model answer) and 624 (French phrase 2), so that A45's sources and SQL match the database:
#   content/{7071,4265,624}.json, out/lab10_data_01.sql, out/lab10_dryrun.sql, batches/lab10.json (objects),
#   audio/7071 + audio/4265 (the new recordings + manifest.json).
# Not touched: data/videos.json (read by A45's running batches; patch after A45 finishes) and every other batch.
# Each file is backed up to backup/a45_lab10/ first and replaced atomically (os.replace). Run again = no change.
import json, os, shutil, hashlib, sys
A = os.path.expanduser('~/Projects/and-again-content/runs/a45_20261004'); H = os.path.dirname(os.path.abspath(__file__))
A48 = os.path.expanduser('~/Projects/and-again-content/runs/a48_20261005')
K = json.load(open(f'{H}/content/king_7071.verified.json'))
EX = json.load(open(os.path.expanduser('~/Projects/and-again-a49/lib/labExtras.json')))
man49 = {m['text']: m for m in json.load(open(f'{H}/audio/manifest.json'))}
fr624 = open(f'{H}/verify/624_fr.md').readline().split('CHOICE:')[1].strip()
AUD = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/'
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']
BK = f'{H}/backup/a45_lab10'; os.makedirs(BK, exist_ok=True)
noun2 = man49['a king']; ans4265 = EX['4265']['answerVoice']; ans4265_obj = ans4265.split('/public/audio/')[1]
ans4265_file = os.path.basename(ans4265_obj); ans4265_text = ' '.join(EX['4265']['answer'])

def save(rel, data):
    p = f'{A}/{rel}'; b = f'{BK}/{rel.replace("/", "__")}'
    if not os.path.exists(b): shutil.copy(p, b)
    tmp = p + '.a49tmp'; open(tmp, 'w').write(data); os.replace(tmp, p)

def fix_set(vid, taps, nouns, question, chips, text, audio, tr):
    if vid == 7071:
        assert taps[0]['target'] in ('the duke', 'the king'); taps[0]['target'] = 'the king'
        nouns[1]['word'] = 'a king'; nouns[1]['audio_url'] = AUD + noun2['object']; question = K['question']
        for l in LANGS: tr[l]['nouns'] = K['tr'][l]['nouns']; tr[l]['question'] = K['tr'][l]['question']
    if vid == 4265:
        chips = EX['4265']['answer']; text = ans4265_text; audio = ans4265
        for l in LANGS: tr[l]['answer'] = EX['4265']['tr'][l]['answer']
    if vid == 624:
        assert tr['fr']['phrases'][1] in ('voler au vent', fr624); tr['fr']['phrases'][1] = fr624
    return taps, nouns, question, chips, text, audio, tr

# 1. the SQL files: rebuild the three rows from their own JSON (A45's format kept)
D = lambda o: json.dumps(o, ensure_ascii=False, separators=(',', ':'))
for rel in ['out/lab10_data_01.sql', 'out/lab10_dryrun.sql']:
    lines = open(f'{A}/{rel}').read().split('\n'); n = 0
    for i, l in enumerate(lines):
        vid = next((v for v in (7071, 4265, 624) if l.startswith(f'({v}, ')), None)
        if vid is None: continue
        p = l.split('$a45$'); assert len(p) == 17, (rel, vid)
        taps, nouns, tr = json.loads(p[1]), json.loads(p[3]), json.loads(p[13])
        taps, nouns, q, chips, text, audio, tr = fix_set(vid, taps, nouns, p[5], json.loads(p[7]), p[9], p[11], tr)
        p[1], p[3], p[5], p[7], p[9], p[11], p[13] = D(taps), D(nouns), q, D(chips), text, audio, D(tr)
        lines[i] = '$a45$'.join(p); n += 1
    assert n == 3, (rel, n); save(rel, '\n'.join(lines))
# 2. the content files
for vid in (7071, 4265, 624):
    rel = f'content/{vid}.json'; c = json.load(open(f'{A}/{rel}'))
    tr = {l: dict(c['tr'][l]) for l in c['tr']}
    taps, nouns, q, chips, text, audio, tr = fix_set(vid, c['taps'], c['nouns'], c['question'], c['answer'], None, None, tr)
    c['taps'], c['nouns'], c['question'], c['answer'], c['tr'] = taps, nouns, q, chips, tr
    if vid == 7071: c['keyWord'] = 'a king'; c['nouns'][1].pop('audio_url', None)
    save(rel, json.dumps(c, ensure_ascii=False, indent=1))
# 3. the recordings (local copies + manifests) and the batch's object list
def put_audio(vid, kind, i, text, src, f):
    shutil.copy(src, f'{A}/audio/{vid}/{f}')
    rel = f'audio/{vid}/manifest.json'; m = json.load(open(f'{A}/{rel}'))
    it = next(x for x in m['items'] if x['kind'] == kind and (i is None or x.get('i') == i))
    old = it['object']; it.update({'text': text, 'file': f, 'object': f'sets/{vid}/{f}', 'bytes': os.path.getsize(src)})
    save(rel, json.dumps(m, ensure_ascii=False, indent=1)); return old, it['object']
swaps = [put_audio(7071, 'noun', 2, 'a king', f'{H}/audio/7071/{noun2["file"]}', noun2['file']),
         put_audio(4265, 'answer', None, ans4265_text, f'{A48}/audio/4265/{ans4265_file}', ans4265_file)]
rel = 'batches/lab10.json'; b = json.load(open(f'{A}/{rel}'))
for old, new in swaps: b['objects'] = [new if o == old else o for o in b['objects']]
save(rel, json.dumps(b, ensure_ascii=False, indent=1))
print('patched; object swaps:', swaps)
