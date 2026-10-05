# A45: guarded batch write of content/<id>.json (+ audio manifests) into public.media_exercise_sets.
#   python3 build_sql.py <batch> <id> [...]  -> out/<batch>_data_NN.sql (each one transaction, < 900 kB), out/<batch>_rollback.sql,
#   batches/<batch>.json (ids, files, audio objects). Stops when a video fails validate.py.
import json, os, sys
from validate import check
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/'
batch, ids = sys.argv[1], [int(x) for x in sys.argv[2:]]
bad = {i: check(i) for i in ids}; bad = {i: e for i, e in bad.items() if e}
if bad: print('ERROR', bad); sys.exit(1)
def q(s): 
    assert '$a45$' not in s; return f'$a45${s}$a45$'
def j(o): return q(json.dumps(o, ensure_ascii=False, separators=(',', ':'))) + '::jsonb'
rows, objects = [], []
for i in ids:
    c = json.load(open(f'{HERE}/content/{i}.json')); m = json.load(open(f'{HERE}/audio/{i}/manifest.json'))
    url = {(x['kind'], x['i']): BASE + x['object'] for x in m['items']}; objects += [x['object'] for x in m['items']]
    taps = [{'phrase': t['phrase'], 'target': t['target'], 'voice': t['voice'], 'audio_url': url[('tap', n + 1)], 'keys': t['keys']} for n, t in enumerate(c['taps'])]
    nouns = [{'word': x['word'], 'x': x['x'], 'y': x['y'], 'voice': x['voice'], 'audio_url': url[('noun', n + 1)]} for n, x in enumerate(c['nouns'])]
    ans_s = 'null' if c.get('answerS') is None else str(c['answerS'])
    rows.append((i, f"({i}, '{c['level']}', 'live', '{c['defaultVoice']}', {j(taps)}, {j(nouns)}, {c['stillS']}, {ans_s}, {q(c['question'])}, {j(c['answer'])}, {q(' '.join(c['answer']))}, '{c['answerVoice']}', {q(url[('answer', '')])}, {j(c['tr'])}, {j(m['voices'])})"))
parts, cur, size = [], [], 0
for r in rows:
    if cur and size + len(r[1].encode()) > 850_000: parts.append(cur); cur, size = [], 0
    cur.append(r); size += len(r[1].encode())
if cur: parts.append(cur)
files = []
for n, part in enumerate(parts, 1):
    pid = ','.join(str(i) for i, _ in part); f = f'out/{batch}_data_{n:02d}.sql'; files.append(f)
    s = f"""begin;
-- A45 batch {batch}, part {n} of {len(parts)}: {len(part)} videos. Guards: none of them has a row yet; all are videos.
do $g$ begin
  if exists (select 1 from public.media_exercise_sets where media_id in ({pid})) then raise exception 'A45 {batch}/{n}: rows exist already, nothing written'; end if;
  if (select count(*) from public.media where media_type = 'video' and id in ({pid})) <> {len(part)} then raise exception 'A45 {batch}/{n}: not all ids are videos, nothing written'; end if;
end $g$;
insert into public.media_exercise_sets (media_id, level, status, default_voice, taps, nouns, still_s, answer_s, question, answer_chips, answer_text, answer_voice, answer_audio_url, tr, voice_names) values
""" + ',\n'.join(r for _, r in part) + f""";
do $g$ begin
  if (select count(*) from public.media_exercise_sets where media_id in ({pid}) and jsonb_array_length(taps) = 3 and jsonb_array_length(nouns) between 3 and 4) <> {len(part)} then raise exception 'A45 {batch}/{n}: count after the write is wrong, rolled back'; end if;
end $g$;
commit;
"""
    open(f'{HERE}/{f}', 'w').write(s)
allid = ','.join(str(i) for i in ids)
open(f'{HERE}/out/{batch}_rollback.sql', 'w').write(f"-- A45 rollback of batch {batch} (NOT run). The rows did not exist before; the audio objects stay in storage.\nbegin;\ndelete from public.media_exercise_sets where media_id in ({allid});\ncommit;\n")
json.dump({'batch': batch, 'ids': ids, 'sql': files, 'rollback': f'out/{batch}_rollback.sql', 'objects': objects}, open(f'{HERE}/batches/{batch}.json', 'w'), indent=1)
print(batch, len(ids), 'videos', len(files), 'sql files', [os.path.getsize(f'{HERE}/{f}') for f in files], 'B;', len(objects), 'audio objects')
