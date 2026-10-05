# A55: writes A55_PROGRESS.md (here and in the Drive reports folder) from the run folder's state.  python3 progress.py ["note"]
import json, os, sys, glob, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
IDS = [8055, 236, 624, 7071, 4265, 461, 62, 8039, 432, 8056]
NAT = ['sk', 'cz', 'en', 'de', 'es', 'fr', 'hu', 'tr', 'ua']
L = ['# A55 progress (lab pilot: 10 videos x de / es / fr)', '', f'Updated {datetime.datetime.now():%Y-%m-%d %H:%M}.', '']
for lang in ('de', 'es', 'fr'):
    v = [open(f).readline().strip().replace('VERDICT: ', '') for f in sorted(glob.glob(f'{HERE}/verify/{lang}/*.md'))]
    written = len(glob.glob(f'{HERE}/content/{lang}/*.json'))
    trd = [n for n in NAT if n != lang and os.path.exists(f'{HERE}/tr/{lang}/{n}.json')]
    trv = [n for n in NAT if n != lang and os.path.exists(f'{HERE}/tr/{lang}/verify_{n}.md')]
    audio = len(glob.glob(f'{HERE}/audio/{lang}/*/manifest.json'))
    built = os.path.exists(f'{HERE}/batches/lab10_{lang}.json'); applied = os.path.exists(f'{HERE}/applied/lab10_{lang}')
    L.append(f'- **{lang}**: written {written}/10, verdicts {", ".join(f"{x} {v.count(x)}" for x in ("PASS", "FIXED", "FAIL") if v.count(x))}, help translations {len(trd)}/8 (verified {len(trv)}/8), audio {audio}/10, SQL built {"yes" if built else "no"}, in the database {"yes" if applied else "no"}')
if len(sys.argv) > 1: L += ['', 'Note: ' + sys.argv[1]]
L += ['', 'Resume: see `runs/a55_20261005/README.md` (order of the steps); owner script `bash ~/Projects/and-again-content/runs/a55_20261005/apply_a55.sh`.']
open(f'{HERE}/A55_PROGRESS.md', 'w').write('\n'.join(L) + '\n')
D = os.path.expanduser('~/Library/CloudStorage/GoogleDrive-surhanak.kristian@gmail.com/Meine Ablage/AndAgain_reports')
if os.path.isdir(D): shutil.copy(f'{HERE}/A55_PROGRESS.md', D)
print('\n'.join(L))
