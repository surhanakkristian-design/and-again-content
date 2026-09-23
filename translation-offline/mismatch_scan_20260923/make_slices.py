# Builds the scan slices: ~150 exercises each, all 8 natives next to the English row. SELECT output only.
import json, collections, re, sys
D = sys.argv[1]
rows = json.load(open(f'{D}/rows.json'))
by = collections.defaultdict(dict); lvl = {}
for r in rows:
    by[r['exercise_id']][r['l']] = r; lvl[r['exercise_id']] = r['level']
LANGS = ['de', 'ua', 'es', 'fr', 'tr', 'hu', 'sk', 'cz']
ids = sorted(by)
def line(r):
    fs = (r['fs'] or '').strip(); ca = (r['ca'] or '').strip(); it = (r['it'] or '').strip()
    s = f"{fs}  [gap: {ca}]"
    derived = fs.replace(ca, '...', 1) if ca else fs
    if it and it != derived and it != fs:
        s += f"  [intro: {it}]"
    return s
n = 27; size = -(-len(ids) // n)
stats = []
for k in range(n):
    chunk = ids[k*size:(k+1)*size]
    out = []
    for i in chunk:
        e = by[i]
        out.append(f"### {i} {lvl[i]}")
        for l in ['en'] + LANGS:
            if l in e: out.append(f"{l}: {line(e[l])}")
            else: out.append(f"{l}: <MISSING ROW>")
    txt = '\n'.join(out) + '\n'
    open(f'{D}/slices/s{k+1:02d}.txt', 'w').write(txt)
    stats.append((k+1, len(chunk), len(txt)))
print(stats[:3], sum(s[2] for s in stats))
