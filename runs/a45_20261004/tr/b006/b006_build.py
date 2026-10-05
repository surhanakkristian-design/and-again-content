import json, sys
code = sys.argv[1]
src = json.load(open('source.json')); out = {}
for line in open(f'b006_{code}_data.txt', encoding='utf-8'):
    line = line.rstrip('\n')
    if not line: continue
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
assert list(out) == list(src), set(src) ^ set(out)
for i in src: assert len(out[i]['nouns']) == len(src[i]['nouns']) and len(out[i]['phrases']) == 3, i
json.dump(out, open(f'{code}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
