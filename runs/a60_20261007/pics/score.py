# A56: blind scores per caption from blind/<round>_answer.json against blind/<id>_<round>_key.json -> blind_scores.json
import json, glob, os, collections
P = os.path.dirname(os.path.abspath(__file__)); S = collections.defaultdict(lambda: [0, 0])
for a in sorted(glob.glob(f'{P}/blind/*_answer.json')):
    rnd = os.path.basename(a).split('_')[0]; ans = json.load(open(a))
    for vid, m in ans.items():
        kf = f'{P}/blind/{vid}_{rnd}_key.json'
        if not os.path.exists(kf): continue
        key = json.load(open(kf))
        for i, cap in key.items():
            S[f'{vid}|{cap}'][1] += 1; S[f'{vid}|{cap}'][0] += m.get(f'card_{i}') == cap
out = {k: f'{v[0]}/{v[1]}' for k, v in sorted(S.items())}
json.dump(out, open(f'{P}/blind_scores.json', 'w'), indent=1, ensure_ascii=False); print(json.dumps(out, indent=1, ensure_ascii=False))
