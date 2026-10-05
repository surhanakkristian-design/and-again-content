import json, sys, os
H = os.path.dirname(os.path.abspath(__file__)); code = sys.argv[1]
src = json.load(open(f'{H}/source.json')); out = {}
for ln in open(f'{H}/b025_{code}_lines.txt', encoding='utf-8'):
    ln = ln.strip()
    if not ln: continue
    i, p, n, q, a = ln.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: out[i] for i in src if i in out}
json.dump(out, open(f'{H}/{code}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
