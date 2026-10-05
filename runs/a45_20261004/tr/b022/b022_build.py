import json, sys, os
d = os.path.dirname(os.path.abspath(__file__)); code = sys.argv[1]
src = json.load(open(f'{d}/source.json')); rows = {}
for line in open(f'{d}/b022_{code}_lines.txt', encoding='utf-8'):
    line = line.strip()
    if not line: continue
    i, p, n, q, a = line.split('|')
    rows[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: rows[i] for i in src if i in rows}
json.dump(out, open(f'{d}/{code}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'written', [i for i in src if i not in rows])
