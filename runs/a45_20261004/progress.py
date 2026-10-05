# A45: writes A45_PROGRESS.md (run folder + Drive reports folder) from data/*.result.json and batches/*.json.
import json, glob, os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
D = '/Users/kristiansurhanak/Library/CloudStorage/GoogleDrive-surhanak.kristian@gmail.com/Meine Ablage/AndAgain_reports'
V = {int(x['id']): x for x in json.load(open(f'{HERE}/data/videos.json'))}
DB = json.load(open(f'{HERE}/data/db_state.json')) if os.path.exists(f'{HERE}/data/db_state.json') else {'at': 'never', 'rows': 0, 'batches': {}}
VOICES = json.load(open(f'{HERE}/voices.json'))
def indb(name):
    d = DB['batches'].get(name)
    if not d or d['rows'] == 0: return 'not yet'
    return f"yes ({d['rows']} rows" + (', shape' if d['shaped'] == d['rows'] else f", shape {d['shaped']}/{d['rows']}") + ')' if d['rows'] == d['videos'] else f"PARTLY ({d['rows']} of {d['videos']} rows)"

rows, done, failed, audio = [], [], {}, 0
b = json.load(open(f'{HERE}/batches/lab10.json')); done += b['ids']; audio += len(b['objects'])
rows.append(f"| lab10 | 10 | 10 | 0 | {len(b['objects'])} | {indb('lab10')} |")
for f in sorted(glob.glob(f'{HERE}/data/b*.result.json')):
    r = json.load(open(f)); name = r['batch']; bb = json.load(open(f'{HERE}/batches/{name}.json'))
    done += r['done']; failed.update(r['failed']); audio += len(bb['objects'])
    rows.append(f"| {name} | {len(r['done']) + len(r['failed'])} | {len(r['done'])} | {len(r['failed'])} | {len(bb['objects'])} | {indb(name)} |")
a = sum(1 for i in done if V[i]['level'] == 'A'); bl = len(done) - a
ta = sum(1 for x in V.values() if x['level'] == 'A'); tb = len(V) - ta
applied = sum(1 for k, d in DB['batches'].items() if d['videos'] == d['rows'])
pending = [k for k, d in sorted(DB['batches'].items()) if d['videos'] != d['rows']]
EXTRA = open(f'{HERE}/data/progress_notes.md').read().strip() if os.path.exists(f'{HERE}/data/progress_notes.md') else ''
note = sys.argv[1] if len(sys.argv) > 1 else ''
s = f"""# A45 progress

Updated: {datetime.datetime.now().strftime('%-d %b %Y %H:%M')}. {note}

**Videos with content: {len(done)} / {len(V)} (A {a} / {ta}, B {bl} / {tb}); failed: {len(failed)}; audio files recorded: {audio} ({VOICES['female']} female, {VOICES['male']} male); batches in the database: {applied} of {len(rows)} ({DB['rows']} rows, read {DB['at']}).**

## Owner script to run
`bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh`
Batches not in the database yet: {', '.join(pending) or 'none'}. The script applies the migrations if missing (table `media_exercise_sets`; columns width / height), then per batch not in the database: audio upload (missing files are sent again up to 5 rounds with pauses after a network error), read-back of every object, guarded rows (only when all audio reads back), and the picture shape of every batch. `--check` only checks the files. Safe to run again; a batch already written is skipped.

{EXTRA}

## Batches
| batch | videos | done | failed | audio files | in the database |
|---|---|---|---|---|---|
""" + '\n'.join(rows) + """

## Failed videos
""" + ('\n'.join(f'- {k} ({V[int(k)]["word"]}): {v}' for k, v in failed.items()) or 'none') + """

## Voices
""" + VOICES['female'] + " (female), " + VOICES['male'] + """ (male). Checked 5 Oct 2026 (`say -v '?'`): no Ava / Zoe (Premium) and no Evan / Nathan (Enhanced) installed, so no re-recording. To get them: System Settings > Accessibility > Spoken Content > System voice > Manage voices.
"""
open(f'{HERE}/A45_PROGRESS.md', 'w').write(s); open(f'{D}/A45_PROGRESS.md', 'w').write(s)
print(s.split('\n')[4])
