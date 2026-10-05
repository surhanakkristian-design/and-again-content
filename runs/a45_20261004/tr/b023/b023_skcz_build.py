import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
code = sys.argv[1]
src = json.load(open(f'{HERE}/source.json'))
out = {}
for line in open(f'{HERE}/b023_{code}_lines.txt', encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    i, p, n, q, a = [x.strip() for x in line.split(' | ')]
    out[i] = {'phrases': [x.strip() for x in p.split(' ; ')], 'nouns': [x.strip() for x in n.split(' ; ')], 'question': q, 'answer': a}
ordered = {i: out[i] for i in src if i in out}
ordered.update({i: v for i, v in out.items() if i not in src})
json.dump(ordered, open(f'{HERE}/{code}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(ordered))
