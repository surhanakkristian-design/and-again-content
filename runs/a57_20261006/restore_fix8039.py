# A57: the rollback of fix8039_<lang>: prints the update that puts the row back as saved in backup/fix8039_<lang>_before.json.
#   python3 restore_fix8039.py <lang> > /tmp/x.sql    (then: supabase db query --linked --file /tmp/x.sql)
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); lang = sys.argv[1]
row = json.load(open(f'{HERE}/backup/fix8039_{lang}_before.json'))[0]
q = lambda v: 'null' if v is None else "$r$" + (v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)) + "$r$"
cols = ['key_word', 'taps', 'nouns', 'question', 'answer_chips', 'answer_text', 'answer_voice', 'answer_audio_url', 'carousel', 'recall', 'tr', 'content_version']
js = {'taps', 'nouns', 'answer_chips', 'carousel', 'recall', 'tr'}
sets = ', '.join(f"{c} = {q(row[c])}{'::jsonb' if c in js and row[c] is not None else ''}" if c != 'content_version' else f'content_version = {row[c]}' for c in cols)
print(f"begin;\nupdate public.media_exercise_sets_l10n set {sets}, updated_at = now() where media_id = 8039 and learning_language = '{lang}';\ncommit;")
