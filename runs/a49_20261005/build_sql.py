# A49: one guarded transaction for parts 1 and 3 (7071 duke -> king everywhere in the DB; 4265 model answer; 624 French
# phrase), and its rollback from the backups taken before (backup/*.json).
#   python3 build_sql.py -> out/a49_db.sql, out/a49_db_rollback.sql
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); B = f'{HERE}/backup'; os.makedirs(f'{HERE}/out', exist_ok=True)
APP = os.path.expanduser('~/Projects/and-again-a49')
K = json.load(open(f'{HERE}/content/king_7071.verified.json'))
man = {m['text']: m for m in json.load(open(f'{HERE}/audio/manifest.json'))}
AUD = 'https://abyrutykpvmzkfbesire.supabase.co/storage/v1/object/public/audio/'
rows = {r['media_id']: r for r in json.load(open(f'{B}/mes_3rows_before.json'))}
ex = json.load(open(f'{APP}/lib/labExtras.json'))
fr624 = open(f'{HERE}/verify/624_fr.md').readline().split('CHOICE:')[1].strip()
q = lambda s: "$a49$" + s + "$a49$"
J = lambda o: q(json.dumps(o, ensure_ascii=False)) + '::jsonb'
LANGS = ['de', 'fr', 'es', 'sk', 'cz', 'ua', 'tr', 'hu']

# 7071: the set
r = rows[7071]; taps = r['taps']; nouns = r['nouns']; tr = r['tr']
assert taps[0]['target'] == 'the duke' and nouns[1]['word'] == 'a duke'
taps[0]['target'] = K['taps_target'][0]
nouns[1]['word'] = 'a king'; nouns[1]['audio_url'] = AUD + man['a king']['object']
for l in LANGS:
    t = K['tr'][l]; tr[l]['nouns'] = t['nouns']; tr[l]['question'] = t['question']; assert tr[l]['answer'] == t['answer']
# 4265: the corrected answer (A48 lab file)
e = ex['4265']; r4 = rows[4265]; tr4 = r4['tr']
for l in LANGS: tr4[l]['answer'] = e['tr'][l]['answer']
# 624: French phrase 2
r6 = rows[624]; tr6 = r6['tr']; assert tr6['fr']['phrases'][1] == 'voler au vent'; tr6['fr']['phrases'][1] = fr624

TL = {'en': (K['en_tinder'], K['en_comment_question'])}
for l in LANGS: TL[l] = (K['tr'][l]['tinder'], K['tr'][l]['comment_question'])
s = ["begin;", "-- A49: 7071 teaches king (concept 2542) instead of duke (5144, kept); 4265 model answer; 624 French phrase 2.",
"do $g$ begin",
"  if (select count(*) from public.concept_media where media_id = 7071 and concept_id = 5144) <> 1 then raise exception 'A49: concept_media 7071 is not duke, nothing written'; end if;",
"  if (select title from public.media where id = 7071) <> 'duke_7071' then raise exception 'A49: media 7071 title changed, nothing written'; end if;",
"  if (select count(*) from public.media_exercise_sets where media_id in (7071, 4265, 624) and content_version = 1) <> 3 then raise exception 'A49: sets changed since the backup, nothing written'; end if;",
"  if (select answer_text from public.media_exercise_sets where media_id = 4265) <> 'It is hugging the angry parrot.' then raise exception 'A49: 4265 answer changed, nothing written'; end if;",
"  if (select count(*) from public.tinder_sentences where media_id = 7071) <> 9 or (select count(*) from public.comment_questions where media_id = 7071) <> 9 or (select count(*) from public.exercise_localizations where exercise_id = 125262) <> 9 then raise exception 'A49: 7071 text rows not as backed up, nothing written'; end if;",
"end $g$;",
"update public.concept_media set concept_id = 2542 where media_id = 7071 and concept_id = 5144;",
"update public.media set title = 'king_7071' where id = 7071 and title = 'duke_7071';",
"update public.exercises set concept_id = 2542 where id = 125262 and media_id = 7071 and concept_id = 5144;",
"update public.legacy_exercise_media set concept_id = 2542 where exercise_id = 125262 and media_id = 7071 and concept_id = 5144;",
"update public.tinder_word_distractors set concept_id = 2542 where media_id = 7071 and concept_id = 5144;",
"-- king is now the key word of a level-B video of group 1501: it takes duke's place in that group's B lists",
"update public.tinder_word_distractors set distractor_concept_ids = array_replace(distractor_concept_ids, 5144::bigint, 2542::bigint), fallback_concept_ids = array_replace(fallback_concept_ids, 5144::bigint, 2542::bigint) where concept_id <> 2542 and (5144 = any(distractor_concept_ids) or 5144 = any(fallback_concept_ids)) and not (2542 = any(distractor_concept_ids));",
]
for l, (t, cq) in TL.items():
    s.append(f"update public.tinder_sentences set true_sentence = {q(t['true_sentence'])}, false_sentence = {q(t['false_sentence'])}, true_phrase = {q(t['true_phrase'])}, false_phrase = {q(t['false_phrase'])} where media_id = 7071 and language_code = '{l}';")
    s.append(f"update public.exercise_localizations set correct_answer = {q(t['true_phrase'])}, distractor_1 = {q(t['false_phrase'])} where exercise_id = 125262 and language_code = '{l}';")
    s.append(f"update public.comment_questions set question = {q(cq)} where media_id = 7071 and language_code = '{l}';")
s.append(f"update public.media_exercise_sets set taps = {J(taps)}, nouns = {J(nouns)}, question = {q(K['question'])}, tr = {J(tr)}, content_version = 2, updated_at = now() where media_id = 7071 and content_version = 1;")
s.append(f"update public.media_exercise_sets set answer_chips = {J(e['answer'])}, answer_text = {q(' '.join(e['answer']))}, answer_audio_url = {q(e['answerVoice'])}, tr = {J(tr4)}, content_version = 2, updated_at = now() where media_id = 4265 and content_version = 1;")
s.append(f"update public.media_exercise_sets set tr = {J(tr6)}, content_version = 2, updated_at = now() where media_id = 624 and content_version = 1;")
s += ["do $g$ begin",
"  if (select count(*) from public.media_exercise_sets where media_id in (7071, 4265, 624) and content_version = 2) <> 3 then raise exception 'A49: sets not all written, rolled back'; end if;",
"  if exists (select 1 from public.concept_media where concept_id = 5144) or exists (select 1 from public.tinder_word_distractors where 5144 = any(distractor_concept_ids) or 5144 = any(fallback_concept_ids) or concept_id = 5144) then raise exception 'A49: duke still linked, rolled back'; end if;",
"  if exists (select 1 from public.tinder_sentences where media_id = 7071 and (true_sentence ilike '%duke%' or true_sentence ilike '%herzog%')) then raise exception 'A49: duke left in tinder, rolled back'; end if;",
"end $g$;", "commit;"]
open(f'{HERE}/out/a49_db.sql', 'w').write('\n'.join(s) + '\n')

# rollback from the backups
rb = ["begin;", "-- A49 rollback: every row back to its state before the A49 write (backup/*.json)."]
for x in json.load(open(f'{B}/mes_3rows_before.json')):
    rb.append(f"update public.media_exercise_sets set taps = {J(x['taps'])}, nouns = {J(x['nouns'])}, question = {q(x['question'])}, answer_chips = {J(x['answer_chips'])}, answer_text = {q(x['answer_text'])}, answer_audio_url = {q(x['answer_audio_url'])}, tr = {J(x['tr'])}, content_version = {x['content_version']}, updated_at = {q(x['updated_at'])}::timestamptz where media_id = {x['media_id']};")
rb.append("update public.concept_media set concept_id = 5144 where id = 5228 and media_id = 7071;")
rb.append("update public.media set title = 'duke_7071' where id = 7071;")
rb.append("update public.exercises set concept_id = 5144 where id = 125262;")
rb.append("update public.legacy_exercise_media set concept_id = 5144 where exercise_id = 125262 and media_id = 7071;")
for x in json.load(open(f'{B}/tinder_word_distractors_5144.json')):
    arr = lambda a: "'{" + ','.join(str(i) for i in a) + "}'::bigint[]"
    rb.append(f"update public.tinder_word_distractors set concept_id = {x['concept_id']}, distractor_concept_ids = {arr(x['distractor_concept_ids'])}, fallback_concept_ids = {arr(x['fallback_concept_ids'])} where media_id = {x['media_id']};")
for x in json.load(open(f'{B}/tinder_sentences_7071.json')):
    rb.append(f"update public.tinder_sentences set true_sentence = {q(x['true_sentence'])}, false_sentence = {q(x['false_sentence'])}, true_phrase = {q(x['true_phrase'])}, false_phrase = {q(x['false_phrase'])} where id = {x['id']};")
for x in json.load(open(f'{B}/exercise_localizations_125262.json')):
    rb.append(f"update public.exercise_localizations set correct_answer = {q(x['correct_answer'])}, distractor_1 = {q(x['distractor_1'])} where id = {x['id']};")
for x in json.load(open(f'{B}/comment_questions_7071.json')):
    rb.append(f"update public.comment_questions set question = {q(x['question'])} where id = {x['id']};")
rb.append("commit;")
open(f'{HERE}/out/a49_db_rollback.sql', 'w').write('\n'.join(rb) + '\n')
print('written', len(s), 'and', len(rb), 'lines')
