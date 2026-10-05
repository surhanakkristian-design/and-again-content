import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); b, code = sys.argv[1], sys.argv[2]
src = json.load(open(f'{HERE}/tr/{b}/source.json')); t = json.load(open(f'{HERE}/tr/{b}/{code}.json')); bad = []
for i, s in src.items():
    x = t.get(i)
    if not x: bad.append(f'{i}: missing'); continue
    if len(x.get('phrases', [])) != 3 or len(x.get('nouns', [])) != len(s['nouns']) or not x.get('question') or not x.get('answer') or not all(x['phrases']) or not all(x['nouns']): bad.append(f'{i}: counts or empty text')
extra = [i for i in t if i not in src]
print('ok' if not bad and not extra else 'ERRORS: ' + '; '.join(bad[:20]) + (f' extra ids {extra[:5]}' if extra else ''), len(src), 'videos')
sys.exit(1 if bad or extra else 0)
