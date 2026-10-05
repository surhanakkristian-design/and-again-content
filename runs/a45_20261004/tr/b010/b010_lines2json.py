import json, sys
code = sys.argv[1]
out = {}
for line in open(f'b010_{code}_lines.txt', encoding='utf-8'):
    line = line.rstrip('\n')
    if not line: continue
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
json.dump(out, open(f'{code}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out))
