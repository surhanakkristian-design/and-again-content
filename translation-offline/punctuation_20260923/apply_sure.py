"""Write the SURE rows of classify.py: full_sentence gains the final '.' (the gap ends the sentence, so intro_text keeps
its '...' and is not written). One backup/rollback per language; batches of <= 500; guarded on the live value."""
import json, sys, os, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import writer
dry = '--dry' in sys.argv
cl = json.load(open(f'{H}/work/classified.json'))
per = collections.defaultdict(list)
for x in cl:
    if x['cls'] == 'sure':
        assert x['new_fs'] == x['old_fs'].rstrip() + '.'
        per[x['lang']].append(dict(id=x['id'], exercise_id=x['exercise_id'], lang=x['lang'],
                                   new={'full_sentence': x['new_fs']}, old={'full_sentence': x['old_fs']}))
langs = [a for a in sys.argv[1:] if not a.startswith('--')] or sorted(per)
for L in langs:
    res = writer.run(f'sure_{L}_full_sentence', per[L], ['full_sentence'], dry=dry)
    print(json.dumps({k: (v if k != 'skipped' else v[:5]) for k, v in res.items()}, ensure_ascii=False), flush=True)
