# A55: the guarded SQL of one learning language (batch lab10_<lang>) from content/<lang>/<id>.json + tr/<lang>/<native>.json
# + audio/<lang>/<id>/manifest.json + the English rows (src/sets_en.json: regions, slots, still, shape) + the carousel
# pictures (src/<id>.json). Every video must validate (validate55.py --full) and carry a PASS / FIXED verdict.
#   python3 build_sql55.py <lang> [...]   -> out/lab10_<lang>.sql, out/lab10_<lang>_rollback.sql, batches/lab10_<lang>.json
import json, os, sys
from validate55 import check
HERE = os.path.dirname(os.path.abspath(__file__))
IDS = [8055, 236, 624, 7071, 4265, 461, 62, 8039, 432, 8056]
NATIVES = ['sk', 'cz', 'en', 'de', 'es', 'fr', 'hu', 'tr', 'ua']
BASE = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio'
VOICES = json.load(open(f'{HERE}/voices.json'))
EN = {r['media_id']: r for r in json.load(open(f'{HERE}/src/sets_en.json'))}
def lit(v):
    s = json.dumps(v, ensure_ascii=False) if not isinstance(v, str) else v
    assert '$a55$' not in s
    return f'$a55${s}$a55$'
def verdict(lang, vid):
    p = f'{HERE}/verify/{lang}/{vid}.md'
    return open(p).readline().strip() if os.path.exists(p) else ''
for lang in sys.argv[1:]:
    tr = {n: json.load(open(f'{HERE}/tr/{lang}/{n}.json')) for n in NATIVES if n != lang}
    for vid in IDS:   # the help translations go into tr/<lang>/<id>.json first, so the full check reads them
        json.dump({n: tr[n][str(vid)] for n in tr if str(vid) in tr[n]}, open(f'{HERE}/tr/{lang}/{vid}.json', 'w'), ensure_ascii=False, indent=1)
    bad = []
    for vid in IDS:
        e = check(lang, vid, full=True)
        if verdict(lang, vid) not in ('VERDICT: PASS', 'VERDICT: FIXED'): e.append('no PASS / FIXED verdict')
        if e: bad.append(f'{vid}: ' + '; '.join(e[:6]))
    if bad: print(lang, 'NOT BUILT:\n  ' + '\n  '.join(bad)); continue
    rows, objects, plain = [], [], []
    for vid in IDS:
        c = json.load(open(f'{HERE}/content/{lang}/{vid}.json')); s = json.load(open(f'{HERE}/src/{vid}.json')); en = EN[vid]
        m = {(x['kind'], x['i']): x for x in json.load(open(f'{HERE}/audio/{lang}/{vid}/manifest.json'))['items']}
        url = lambda kind, i: f"{BASE}/{m[(kind, i)]['object']}"
        objects += [x['object'] for x in m.values()]
        taps = [{'phrase': t['phrase'], 'target': t['target'], 'voice': t['voice'], 'audio_url': url('tap', i + 1), 'keys': en['taps'][i]['keys']} for i, t in enumerate(c['taps'])]
        nouns = [{'word': n['word'], 'voice': n['voice'], 'audio_url': url('noun', i + 1), 'x': en['nouns'][i]['x'], 'y': en['nouns'][i]['y']} for i, n in enumerate(c['nouns'])]
        car = [{'en': x['en'], 'caption': x['caption'], 'url': s['en']['carousel'][i]['url'], 'audio_url': url('caption', i + 1), 'type': x['type'], 'has_key_word': x['hasKeyWord']} for i, x in enumerate(c['carousel'])]
        rec = [{'from': r['from'], 'parts': r['parts']} for r in c['recall']]
        trv = json.load(open(f'{HERE}/tr/{lang}/{vid}.json'))
        vals = [str(vid), lit(lang), lit(c['level']), "'live'", lit(c['keyWord']), lit(s['defaultVoice']), lit(taps) + '::jsonb', lit(nouns) + '::jsonb',
                str(en['still_s']), 'null' if en['answer_s'] is None else str(en['answer_s']), lit(c['question']), lit(c['answer']) + '::jsonb',
                lit(' '.join(c['answer'])), lit(c['answerVoice']), lit(url('answer', '')), (lit(car) + '::jsonb') if car else 'null', lit(rec) + '::jsonb',
                lit(trv) + '::jsonb', lit({g: v['name'] for g, v in VOICES[lang].items()}) + '::jsonb', str(en['width']), str(en['height'])]
        rows.append('(' + ', '.join(vals) + ')')
        plain.append({'media_id': vid, 'learning_language': lang, 'key_word': c['keyWord'], 'taps': taps, 'nouns': nouns, 'question': c['question'], 'answer_chips': c['answer'],
                      'answer_audio_url': url('answer', ''), 'carousel': car or None, 'recall': rec, 'tr': trv})
    cols = 'media_id, learning_language, level, status, key_word, default_voice, taps, nouns, still_s, answer_s, question, answer_chips, answer_text, answer_voice, answer_audio_url, carousel, recall, tr, voice_names, width, height'
    ids = ','.join(map(str, IDS))
    sql = f"""-- A55: the {len(IDS)} lab videos for learners of {lang} (batch lab10_{lang}). Guarded: nothing is written when a row of this
-- batch exists already (the whole transaction stops); English (media_exercise_sets) is not touched.
begin;
do $g$ begin
  if exists (select 1 from public.media_exercise_sets_l10n where learning_language = '{lang}' and media_id in ({ids})) then
    raise exception 'A55 lab10_{lang}: rows exist already - nothing written';
  end if;
end $g$;
insert into public.media_exercise_sets_l10n ({cols}) values
{(','+chr(10)).join(rows)};
do $g$ begin
  if (select count(*) from public.media_exercise_sets_l10n where learning_language = '{lang}' and media_id in ({ids})) <> {len(IDS)} then
    raise exception 'A55 lab10_{lang}: not {len(IDS)} rows after the insert';
  end if;
end $g$;
commit;
"""
    open(f'{HERE}/out/lab10_{lang}.sql', 'w').write(sql)
    json.dump(plain, open(f'{HERE}/out/rows_{lang}.json', 'w'), ensure_ascii=False, indent=1)   # what the app reads (the lab check uses it)
    open(f'{HERE}/out/lab10_{lang}_rollback.sql', 'w').write(f"-- A55 rollback of batch lab10_{lang} (not run)\nbegin;\ndelete from public.media_exercise_sets_l10n where learning_language = '{lang}' and media_id in ({ids});\ncommit;\n")
    json.dump({'batch': f'lab10_{lang}', 'lang': lang, 'ids': IDS, 'sql': [f'out/lab10_{lang}.sql'], 'rollback': f'out/lab10_{lang}_rollback.sql', 'objects': objects}, open(f'{HERE}/batches/lab10_{lang}.json', 'w'), indent=1)
    print(lang, f'built: {len(rows)} rows, {len(objects)} audio objects, {os.path.getsize(f"{HERE}/out/lab10_{lang}.sql")} bytes')
