# A57: finishes one batch of one learning language: merges the 8 verified help translations into tr/<lang>/<id>.json, records
# the audio that is missing (tts57.py), validates every video (validate57.py --full, PASS / FIXED verdict), and builds the
# guarded SQL in chunks of 25 rows (out/<batch>_<lang>_NN.sql + one rollback), batches/<batch>_<lang>.json (ids, files, audio
# objects), out/<batch>_<lang>.sha256 and data/<batch>_<lang>.result.json (done / failed with the reason).
#   python3 finish57.py <batch> <lang> [--no-audio] [--only id,id --name <batch>_<lang>_r2]   (a follow-up batch of videos that
#   were not built the first time, e.g. audio that failed; written under its own name)
import json, os, sys, subprocess, hashlib
from validate57 import check
HERE = os.path.dirname(os.path.abspath(__file__))
NATIVES = ['sk', 'cz', 'en', 'de', 'es', 'fr', 'hu', 'tr', 'ua']
BASE = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio'
VOICES = json.load(open(f'{HERE}/voices.json'))
CHUNK = 25
def lit(v):
    s = json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v
    assert '$a57$' not in s
    return f'$a57${s}$a57$'
def verdict(lang, vid):
    p = f'{HERE}/verify/{lang}/{vid}.md'
    return open(p).readline().strip() if os.path.exists(p) else ''
def en_row(vid): return json.load(open(f'{HERE}/src/en_rows/{vid}.json'))
batch, lang = sys.argv[1], sys.argv[2]; name = f'{batch}_{lang}'
ids = json.load(open(f'{HERE}/data/{batch}.json'))['ids']
if '--only' in sys.argv:
    only = {int(x) for x in sys.argv[sys.argv.index('--only') + 1].split(',')}; ids = [i for i in ids if i in only]
    name = sys.argv[sys.argv.index('--name') + 1]
    assert name.startswith(f'{batch}_{lang}_r'), name
    for f in os.listdir(f'{HERE}/batches'):
        if f.startswith(f'{batch}_{lang}') and f != name + '.json': assert not set(ids) & set(json.load(open(f'{HERE}/batches/{f}'))['ids']), f'{f} has these ids already'
skip = set(json.load(open(f'{HERE}/data/skipped.json'))) if os.path.exists(f'{HERE}/data/skipped.json') else set()
src_tr = json.load(open(f'{HERE}/tr/{batch}/source_{lang}.json'))
missing_tr = [n for n in NATIVES if n != lang and not (os.path.exists(f'{HERE}/tr/{batch}/{lang}/{n}.json') and os.path.exists(f'{HERE}/tr/{batch}/{lang}/verify_{n}.md'))]
if missing_tr: sys.exit(f'{name}: help translations not written + verified yet: {missing_tr}')
tr = {n: json.load(open(f'{HERE}/tr/{batch}/{lang}/{n}.json')) for n in NATIVES if n != lang}
os.makedirs(f'{HERE}/tr/{lang}', exist_ok=True)
for vid in src_tr:
    json.dump({n: tr[n][vid] for n in tr if vid in tr[n]}, open(f'{HERE}/tr/{lang}/{vid}.json', 'w'), ensure_ascii=False, indent=1)
cand = [int(v) for v in src_tr if int(v) in ids]
if '--no-audio' not in sys.argv:
    need = [v for v in cand if not os.path.exists(f'{HERE}/audio/{lang}/{v}/manifest.json') or check(lang, v, full=True) and any(x.startswith('audio') for x in check(lang, v, full=True))]
    for k in range(0, len(need), 25):
        subprocess.run([sys.executable, f'{HERE}/tts57.py', lang] + [str(v) for v in need[k:k + 25]], timeout=1800)
if '--no-audio' not in sys.argv:   # a second recording pass for videos whose audio is still incomplete (a hung `say`)
    again = [v for v in cand if any(x.startswith('audio') for x in check(lang, v, full=True))]
    if again: subprocess.run([sys.executable, f'{HERE}/tts57.py', lang] + [str(v) for v in again], timeout=1800)
done, failed = [], {}
for vid in ids:
    if f'{lang}:{vid}' in skip: failed[vid] = 'skipped (failed after a rewrite and a second verification)'; continue
    if str(vid) not in src_tr: failed[vid] = 'not verified: ' + (verdict(lang, vid) or 'no verdict'); continue
    e = check(lang, vid, full=True)
    if verdict(lang, vid) not in ('VERDICT: PASS', 'VERDICT: FIXED'): e.append('no PASS / FIXED verdict')
    if e: failed[vid] = '; '.join(e[:6])
    else: done.append(vid)
rows, objects, files = [], [], []
cols = 'media_id, learning_language, level, status, key_word, default_voice, taps, nouns, still_s, answer_s, question, answer_chips, answer_text, answer_voice, answer_audio_url, carousel, recall, tr, voice_names, width, height'
for f in os.listdir(f'{HERE}/out'):
    if f.startswith(name + '_') and f.endswith('.sql'): os.remove(f'{HERE}/out/{f}')
for k in range(0, len(done), CHUNK):
    part = done[k:k + CHUNK]; vals_all = []
    for vid in part:
        c = json.load(open(f'{HERE}/content/{lang}/{vid}.json')); s = json.load(open(f'{HERE}/src/{vid}.json')); en = en_row(vid)
        m = {(x['kind'], x['i']): x for x in json.load(open(f'{HERE}/audio/{lang}/{vid}/manifest.json'))['items']}
        url = lambda kind, i: f"{BASE}/{m[(kind, i)]['object']}"
        objects += [x['object'] for x in m.values()]
        taps = [{'phrase': t['phrase'], 'target': t['target'], 'voice': t['voice'], 'audio_url': url('tap', i + 1), 'keys': en['taps'][i]['keys']} for i, t in enumerate(c['taps'])]
        nouns = [{'word': n['word'], 'voice': n['voice'], 'audio_url': url('noun', i + 1), 'x': en['nouns'][i]['x'], 'y': en['nouns'][i]['y']} for i, n in enumerate(c['nouns'])]
        car = [{'en': x['en'], 'caption': x['caption'], 'url': s['en']['carousel'][i]['url'], 'audio_url': url('caption', i + 1), 'type': x['type'], 'has_key_word': x['hasKeyWord']} for i, x in enumerate(c.get('carousel', []))]
        rec = [{'from': r['from'], 'parts': r['parts']} for r in c['recall']]
        trv = json.load(open(f'{HERE}/tr/{lang}/{vid}.json'))
        vals = [str(vid), lit(lang), lit(c['level']), "'live'", lit(c['keyWord']), lit(s['defaultVoice']), lit(taps) + '::jsonb', lit(nouns) + '::jsonb',
                str(en['still_s']), 'null' if en['answer_s'] is None else str(en['answer_s']), lit(c['question']), lit(c['answer']) + '::jsonb',
                lit(' '.join(c['answer'])), lit(c['answerVoice']), lit(url('answer', '')), (lit(car) + '::jsonb') if car else 'null', lit(rec) + '::jsonb',
                lit(trv) + '::jsonb', lit({g: v['name'] for g, v in VOICES[lang].items()}) + '::jsonb', str(en['width']), str(en['height'])]
        vals_all.append('(' + ', '.join(vals) + ')')
    idl = ','.join(map(str, part)); fn = f'out/{name}_{k // CHUNK + 1:02d}.sql'
    sql = f"""-- A57: batch {name}, chunk {k // CHUNK + 1} ({len(part)} videos for learners of {lang}). Guarded: nothing is written when a row of
-- this chunk exists already (the whole transaction stops); English (media_exercise_sets) is not touched.
begin;
do $g$ begin
  if exists (select 1 from public.media_exercise_sets_l10n where learning_language = '{lang}' and media_id in ({idl})) then
    raise exception 'A57 {fn}: rows exist already - nothing written';
  end if;
end $g$;
insert into public.media_exercise_sets_l10n ({cols}) values
{(','+chr(10)).join(vals_all)};
do $g$ begin
  if (select count(*) from public.media_exercise_sets_l10n where learning_language = '{lang}' and media_id in ({idl})) <> {len(part)} then
    raise exception 'A57 {fn}: not {len(part)} rows after the insert';
  end if;
end $g$;
commit;
"""
    open(f'{HERE}/{fn}', 'w').write(sql); files.append(fn)
    assert os.path.getsize(f'{HERE}/{fn}') < 1_800_000, fn
rb = f'out/{name}_rollback.sql'
open(f'{HERE}/{rb}', 'w').write(f"-- A57 rollback of batch {name} (not run)\nbegin;\ndelete from public.media_exercise_sets_l10n where learning_language = '{lang}' and media_id in ({','.join(map(str, done)) or '0'});\ncommit;\n")
b = {'batch': name, 'lang': lang, 'ids': done, 'sql': files, 'rollback': rb, 'objects': objects}
json.dump(b, open(f'{HERE}/batches/{name}.json', 'w'), indent=1)
def sha(p): return hashlib.sha256(open(f'{HERE}/{p}', 'rb').read()).hexdigest()
lines = [f'{sha(p)}  {p}' for p in files + [rb, f'batches/{name}.json']] + [f"{sha('audio/' + lang + '/' + o[len('sets/'):])}  audio/{lang}/{o[len('sets/'):]}" for o in objects]
open(f'{HERE}/out/{name}.sha256', 'w').write('\n'.join(lines) + '\n')
json.dump({'batch': name, 'done': done, 'failed': {str(k): v for k, v in failed.items()}}, open(f'{HERE}/data/{name}.result.json', 'w'), ensure_ascii=False, indent=1)
print(f'{name}: {len(done)} built ({len(files)} SQL files, {len(objects)} audio objects), {len(failed)} failed' + (': ' + '; '.join(f'{k} {v[:80]}' for k, v in list(failed.items())[:8]) if failed else ''))
