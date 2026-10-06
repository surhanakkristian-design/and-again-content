# A57: writes A57_PROGRESS.md (here and in the Drive reports folder) from the run folder's state.  python3 progress57.py ["note"]
import json, os, sys, glob, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
NAT = ['sk', 'cz', 'en', 'de', 'es', 'fr', 'hu', 'tr', 'ua']
batches = sorted(os.path.basename(p)[:-5] for p in glob.glob(f'{HERE}/data/b[0-9][0-9][0-9].json'))
ids = {b: json.load(open(f'{HERE}/data/{b}.json'))['ids'] for b in batches}
TOTAL = sum(len(v) for v in ids.values())
skip = json.load(open(f'{HERE}/data/skipped.json')) if os.path.exists(f'{HERE}/data/skipped.json') else []
L = ['# A57 progress (the remaining 3,034 videos x German / Spanish / French)', '', f'Updated {datetime.datetime.now():%Y-%m-%d %H:%M}.', '']
for lang in ('de', 'es', 'fr'):
    written = verified = 0; v = {'PASS': 0, 'FIXED': 0, 'FAIL': 0}
    for b in batches:
        for i in ids[b]:
            if os.path.exists(f'{HERE}/content/{lang}/{i}.json'): written += 1
            p = f'{HERE}/verify/{lang}/{i}.md'
            if os.path.exists(p):
                x = open(p).readline().strip().replace('VERDICT: ', '')
                if x in v: v[x] += 1; verified += 1
    trb = [b for b in batches if all(os.path.exists(f'{HERE}/tr/{b}/{lang}/verify_{n}.md') for n in NAT if n != lang)]
    built = [b for b in batches if os.path.exists(f'{HERE}/batches/{b}_{lang}.json')]
    rows = sum(len(json.load(open(f'{HERE}/batches/{b}_{lang}.json'))['ids']) for b in batches if os.path.exists(f'{HERE}/applied/{b}_{lang}'))
    audio = len(glob.glob(f'{HERE}/audio/{lang}/*/manifest.json'))
    L.append(f'- **{lang}**: written {written}/{TOTAL}, verified {verified} (PASS {v["PASS"]}, FIXED {v["FIXED"]}, FAIL {v["FAIL"]}), '
             f'batches translated {len(trb)}/{len(batches)}, built {len(built)}/{len(batches)}, audio {audio} videos, '
             f'rows in the database {rows} (+10 lab rows from A55), skipped {len([s for s in skip if s.startswith(lang + ":")])}')
L.append('')
L.append('Batches applied: ' + (', '.join(sorted(os.path.basename(p) for p in glob.glob(f'{HERE}/applied/*'))) or 'none'))
if os.path.exists(f'{HERE}/applied/fix8039'): L.append('8039 fix (der Weg / el camino): applied')
if len(sys.argv) > 1: L += ['', 'Note: ' + sys.argv[1]]
L += ['', 'Resume: say "Continue A57" (run folder `and-again-content/runs/a57_20261006`, `README.md`). Owner script: `bash ~/Projects/and-again-content/runs/a57_20261006/apply_a57.sh`.']
open(f'{HERE}/A57_PROGRESS.md', 'w').write('\n'.join(L) + '\n')
D = os.path.expanduser('~/Library/CloudStorage/GoogleDrive-surhanak.kristian@gmail.com/Meine Ablage/AndAgain_reports')
if os.path.isdir(D): shutil.copy(f'{HERE}/A57_PROGRESS.md', D)
print('\n'.join(L))
