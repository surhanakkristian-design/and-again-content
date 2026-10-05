# A51: patches A45's FINISHED batch lab10 with 4265's new French model answer (as A49 did), so its sources and SQL
# equal the database and apply_a45.sh cannot bring the old text back. Backups in backup/a45_lab10/; run again = no change.
import os, shutil
A = os.path.expanduser('~/Projects/and-again-content/runs/a45_20261004'); H = os.path.dirname(os.path.abspath(__file__))
OLD = 'Il calme le perroquet en colère en le serrant dans ses bras.'
NEW = 'Il calme le perroquet en colère en lui faisant un câlin.'
BK = f'{H}/backup/a45_lab10'; os.makedirs(BK, exist_ok=True)
for rel in ['content/4265.json', 'out/lab10_data_01.sql', 'out/lab10_dryrun.sql']:
    p = f'{A}/{rel}'; s = open(p).read(); n = s.count(OLD)
    if n == 0: assert NEW in s, rel; print(rel, 'already patched'); continue
    assert n == 1, (rel, n)
    b = f'{BK}/{rel.replace("/", "__")}'
    if not os.path.exists(b): shutil.copy(p, b)
    tmp = p + '.a51tmp'; open(tmp, 'w').write(s.replace(OLD, NEW)); os.replace(tmp, p); print(rel, 'patched')
