"""Write the UNSURE rows both judges agreed on (same mark in . ! ?): full_sentence gains that mark. Every such row has
its gap at the sentence end (intro_text keeps its '...', unchanged). Rows where the judges differ are listed only."""
import json, sys, os, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import writer
m = json.load(open(f'{H}/agents/merged.json'))
per = collections.defaultdict(list)
for r in m['agree']:
    assert r['intro_text'].rstrip().endswith('...')
    old = r['full_sentence']; new = old.rstrip() + r['A'][0]
    per[r['lang']].append(dict(id=r['row_id'], exercise_id=r['exercise_id'], lang=r['lang'],
                               new={'full_sentence': new}, old={'full_sentence': old}))
for L in sorted(per):
    res = writer.run(f'judged_{L}_full_sentence', per[L], ['full_sentence'], dry='--dry' in sys.argv)
    print(res['name'], res['n'], res['written'], res['already'], len(res['skipped']), len(res['verify_bad']), res['backup_sha256'][:12])
