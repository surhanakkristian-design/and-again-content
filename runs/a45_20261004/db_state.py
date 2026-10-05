# A45: reads the live state of media_exercise_sets (read-only) per batch -> data/db_state.json, used by progress.py.
import json, glob, os, subprocess, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sql = "select media_id, (width is not null) as shaped from public.media_exercise_sets"
out = subprocess.run(['bash', '-c', f'cd ~/Projects/and-again && source supabase/scripts/_sb.sh && sb_rows "{sql}"'],
                     capture_output=True, text=True, timeout=300)
rows = {r['media_id']: r['shaped'] for r in json.loads(out.stdout)}
state = {'at': datetime.datetime.now().strftime('%-d %b %Y %H:%M'), 'rows': len(rows), 'batches': {}}
for f in sorted(glob.glob(f'{HERE}/batches/*.json')):
    b = json.load(open(f)); ids = b['ids']
    n = sum(1 for i in ids if i in rows); s = sum(1 for i in ids if rows.get(i))
    state['batches'][b['batch']] = {'videos': len(ids), 'rows': n, 'shaped': s}
    if n == len(ids): open(f'{HERE}/applied/{b["batch"]}', 'a').close()
json.dump(state, open(f'{HERE}/data/db_state.json', 'w'), indent=1)
print(state['rows'], 'rows;', {k: (v['rows'], v['shaped']) for k, v in state['batches'].items()})
