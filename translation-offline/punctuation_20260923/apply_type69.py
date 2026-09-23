"""PREPARED, NOT RUN (pending owner): type 69 definition rows get a final '.' on full_sentence in all nine languages.
Held back because validate_part.stem_sentence documents 'no final stop is added' for type 69 (BRIEF 9.9.2026 v10 §6)
and the English rows carry no mark, so the brief's 'mark from the English row' gives none. Running it also needs
stem_sentence to append the '.' so future imports stay derive-consistent. Run: python3 apply_type69.py [--dry]"""
import json, sys, os, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import writer
rows = json.load(open(f'{H}/work/snapshot_after.json'))
per = collections.defaultdict(list)
for r in rows:
    fs = r['full_sentence'] or ''
    if r['exercise_type_id'] == 69 and fs.strip() and fs.rstrip()[-1] not in '.!?' and fs.rstrip()[-1].isalnum():
        per[r['language_code']].append(dict(id=r['id'], exercise_id=r['exercise_id'], lang=r['language_code'],
                                            new={'full_sentence': fs.rstrip() + '.'}, old={'full_sentence': fs}))
if '--count' in sys.argv:
    print({k: len(v) for k, v in sorted(per.items())}); sys.exit()
for L in sorted(per):
    res = writer.run(f'type69_{L}_full_sentence', per[L], ['full_sentence'], dry='--dry' in sys.argv)
    print(res['name'], res['n'], res['written'], len(res['skipped']), len(res['verify_bad']))
