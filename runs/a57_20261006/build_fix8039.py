# A57 decision 403: the guarded UPDATE of the live 8039 rows (de, es) after the rewrite with der Weg / el camino. Runs finish57.py
# fix8039 <lang> first (help texts, audio, full validation, an insert file), then turns its row into an update that writes only
# while the row still holds the A55 key word.   python3 build_fix8039.py   -> out/fix8039_<lang>.sql + rollback, batches/fix8039_<lang>.json
import json, os, subprocess, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
OLD = {'de': 'der Durchgang', 'es': 'el paso'}; NEW = {'de': 'der Weg', 'es': 'el camino'}
COLS = ['key_word', 'taps', 'nouns', 'question', 'answer_chips', 'answer_text', 'answer_voice', 'answer_audio_url', 'carousel', 'recall', 'tr']
for lang in ('de', 'es'):
    r = subprocess.run([sys.executable, f'{HERE}/finish57.py', 'fix8039', lang], capture_output=True, text=True, timeout=1200); print(r.stdout.strip(), r.stderr.strip()[-300:])
    b = json.load(open(f'{HERE}/batches/fix8039_{lang}.json'))
    if b['ids'] != [8039]: sys.exit(f'{lang}: 8039 not built')
    sql = open(f'{HERE}/out/fix8039_{lang}_01.sql').read()
    vals = sql[sql.index(') values\n(') + 9: sql.rindex(');\ndo $g$')]
    # split the value tuple at top level (dollar-quoted literals contain commas)
    parts, cur, inq = [], '', False
    i = 1
    body = vals[1:-1] if vals.endswith(')') else vals[1:]
    while i <= len(body):
        if body.startswith('$a57$', i - 1): inq = not inq; cur += '$a57$'; i += 5; continue
        ch = body[i - 1]
        if ch == ',' and not inq: parts.append(cur.strip()); cur = ''
        else: cur += ch
        i += 1
    parts.append(cur.strip())
    cols = [c.strip() for c in sql[sql.index('l10n (') + 6: sql.index(') values')].split(',')]
    m = dict(zip(cols, parts))
    assert m['key_word'] == f'$a57${NEW[lang]}$a57$', m['key_word']
    sets = ',\n  '.join(f'{c} = {m[c]}' for c in COLS)
    out = f"""-- A57 decision 403: 8039 for learners of {lang} rewritten with the key word {NEW[lang]} (was {OLD[lang]}); new recordings.
-- Guarded: writes only while the row still holds the A55 key word.
begin;
do $g$ begin
  if (select count(*) from public.media_exercise_sets_l10n where media_id = 8039 and learning_language = '{lang}' and key_word = '{OLD[lang]}') <> 1 then
    raise exception 'A57 fix8039_{lang}: row not in the before-state - nothing written';
  end if;
end $g$;
update public.media_exercise_sets_l10n set
  {sets},
  content_version = content_version + 1, updated_at = now()
where media_id = 8039 and learning_language = '{lang}' and key_word = '{OLD[lang]}';
commit;
"""
    open(f'{HERE}/out/fix8039_{lang}.sql', 'w').write(out); os.remove(f'{HERE}/out/fix8039_{lang}_01.sql')
    b.update({'kind': 'update', 'sql': [f'out/fix8039_{lang}.sql'], 'rollback': f'out/fix8039_{lang}_rollback.sql',
              'verify_sql': f"select count(*) from public.media_exercise_sets_l10n where media_id = 8039 and learning_language = '{lang}' and key_word = '{NEW[lang]}'"})
    open(f'{HERE}/out/fix8039_{lang}_rollback.sql', 'w').write(f"-- A57 rollback of fix8039_{lang} (not run): restore the row from backup/fix8039_{lang}_before.json\n-- (python3 restore_fix8039.py {lang} prints the update)\nbegin;\ncommit;\n")
    json.dump(b, open(f'{HERE}/batches/fix8039_{lang}.json', 'w'), indent=1)
    sha = lambda p: hashlib.sha256(open(f'{HERE}/{p}', 'rb').read()).hexdigest()
    lines = [f'{sha(p)}  {p}' for p in b['sql'] + [b['rollback'], f'batches/fix8039_{lang}.json']] + [f"{sha('audio/' + lang + '/' + o[5:])}  audio/{lang}/{o[5:]}" for o in b['objects']]
    open(f'{HERE}/out/fix8039_{lang}.sha256', 'w').write('\n'.join(lines) + '\n')
    print(lang, 'update built:', len(b['objects']), 'audio objects')
