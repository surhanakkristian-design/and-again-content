# A45: writes A45_PROGRESS.md (run folder + Drive reports folder) from data/*.result.json and batches/*.json.
import json, glob, os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
D = '/Users/kristiansurhanak/Library/CloudStorage/GoogleDrive-surhanak.kristian@gmail.com/Meine Ablage/AndAgain_reports'
V = {int(x['id']): x for x in json.load(open(f'{HERE}/data/videos.json'))}
rows, done, failed, audio = [], [], {}, 0
b = json.load(open(f'{HERE}/batches/lab10.json')); done += b['ids']; audio += len(b['objects'])
rows.append(f"| lab10 | 10 | 10 | 0 | {len(b['objects'])} | {'yes' if os.path.exists(HERE + '/applied/lab10') else 'waits for the owner script'} |")
for f in sorted(glob.glob(f'{HERE}/data/b*.result.json')):
    r = json.load(open(f)); name = r['batch']; bb = json.load(open(f'{HERE}/batches/{name}.json'))
    done += r['done']; failed.update(r['failed']); audio += len(bb['objects'])
    rows.append(f"| {name} | {len(r['done']) + len(r['failed'])} | {len(r['done'])} | {len(r['failed'])} | {len(bb['objects'])} | {'yes' if os.path.exists(HERE + '/applied/' + name) else 'waits for the owner script'} |")
a = sum(1 for i in done if V[i]['level'] == 'A'); bl = len(done) - a
ta = sum(1 for x in V.values() if x['level'] == 'A'); tb = len(V) - ta
applied = len(glob.glob(f'{HERE}/applied/*'))
note = sys.argv[1] if len(sys.argv) > 1 else ''
s = f"""# A45 progress

Updated: {datetime.datetime.now().strftime('%-d %b %Y %H:%M')}. {note}

**Videos with content: {len(done)} / {len(V)} (A {a} / {ta}, B {bl} / {tb}); failed: {len(failed)}; audio files recorded: {audio} (Samantha female, Daniel male); batches in the database: {applied} of {len(rows)}.**

## Owner script to run
`bash ~/Projects/and-again-content/runs/a45_20261004/apply_a45.sh`
The migration (table `media_exercise_sets`; the bucket `audio` also takes audio/mp4) if it is missing, then every batch that is not in the database yet: audio upload, read-back, guarded rows. `--check` only checks the files. Safe to run again after every new batch; a batch already written is skipped.

## Batches
| batch | videos | done | failed | audio files | in the database |
|---|---|---|---|---|---|
""" + '\n'.join(rows) + """

## Failed videos
""" + ('\n'.join(f'- {k} ({V[int(k)]["word"]}): {v}' for k, v in failed.items()) or 'none') + """

## Voices
Samantha (female), Daniel (male): no Premium / Enhanced English voice is installed. Better: download Ava (Premium) or Zoe (Premium), and Evan (Enhanced) or Nathan (Enhanced) in System Settings > Accessibility > Spoken Content > System voice > Manage voices, then say so.
"""
open(f'{HERE}/A45_PROGRESS.md', 'w').write(s); open(f'{D}/A45_PROGRESS.md', 'w').write(s)
print(s.split('\n')[4])
