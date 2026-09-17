"""Part D selection: 200 pilot sentences in the Part A proportions, bench cases included."""
import json, os, random, re, collections
from allocation import TIERS, TIER_ALLOC, MAX_SHORT_WORDS, load_rows, tier_of, words
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
PILOT = 200
BENCH = os.path.expanduser('~/Projects/and-again/scripts/translation-bench/cases.json')

def toks(s):
    return set(re.findall(r"[a-z']+", s.lower()))

def near_dup(a, b):
    ta, tb = toks(a), toks(b)
    return len(ta & tb) / max(1, len(ta | tb)) >= 0.5

rows = load_rows()
types = {t['id']: t for t in json.load(open(os.path.join(ROOT, 'data', 'exercise_types.json')))}
byid = {r['id']: r for r in rows}
tiers = tier_of()
# two-step largest remainder: first the level x tier cells, then topics inside a cell
def lr(quotas, total):
    base = {k: int(q) for k, q in quotas.items()}
    for k in sorted(quotas, key=lambda k: (-(quotas[k] - int(quotas[k])), k))[: total - sum(base.values())]:
        base[k] += 1
    return base
cells = collections.defaultdict(list)
for t in tiers:
    cells[(types[t]['level'], tiers[t])].append(t)
cell_alloc = lr({c: sum(TIER_ALLOC[tiers[t]] for t in ts) * PILOT / 5895 for c, ts in cells.items()}, PILOT)
alloc = {}
for c, ts in cells.items():
    alloc.update(lr({t: cell_alloc[c] / len(ts) for t in ts}, cell_alloc[c]))
bench = json.load(open(BENCH))
chosen = collections.defaultdict(list)
for c in bench:
    r = byid[c['exercise_id']]
    assert r['en'] == c['reference'], (c['exercise_id'], r['en'], c['reference'])
    chosen[r['type_id']].append(r)
rng = random.Random(20260917)
for t in sorted(tiers):
    assert len(chosen[t]) <= alloc[t], (t, alloc[t])
    pool = [r for r in rows if r['type_id'] == t and all((r[k] or '').strip() for k in ('en', 'sk', 'cz'))]
    short = [r for r in pool if words(r['en']) <= MAX_SHORT_WORDS]
    longer = sorted([r for r in pool if words(r['en']) > MAX_SHORT_WORDS], key=lambda r: words(r['en']))
    rng.shuffle(short)
    for r in short + longer:
        if len(chosen[t]) >= alloc[t]:
            break
        if any(r['id'] == c['id'] or near_dup(r['en'], c['en']) or (r['media_id'] and r['media_id'] == c['media_id']) for c in chosen[t]):
            continue
        if '...' in r['en'] or '…' in r['en']:
            continue
        chosen[t].append(r)
    assert len(chosen[t]) == alloc[t], t
bench_ids = {c['exercise_id'] for c in bench}
out = []
for t in sorted(chosen):
    for r in chosen[t]:
        out.append(dict(exercise_id=r['id'], type_id=t, topic=types[t]['title'], level=types[t]['level'], tier=tiers[t],
                        en=r['en'], en_answer=r['en_answer'], sk=r['sk'], cz=r['cz'], words=words(r['en']),
                        bench=r['id'] in bench_ids))
json.dump(out, open(os.path.join(ROOT, 'pilot', 'selection.json'), 'w'), ensure_ascii=False, indent=1)
lv = collections.Counter(o['level'] for o in out); tr = collections.Counter(o['tier'] for o in out)
print(len(out), dict(lv), dict(tr), 'bench', sum(o['bench'] for o in out), 'over12', sum(o['words'] > 12 for o in out))
full_lv = collections.Counter(); full_tr = collections.Counter()
for t in tiers: full_lv[types[t]['level']] += TIER_ALLOC[tiers[t]]; full_tr[tiers[t]] += TIER_ALLOC[tiers[t]]
print({k: round(v * PILOT / 5895, 1) for k, v in full_lv.items()}, {k: round(v * PILOT / 5895, 1) for k, v in full_tr.items()})
print({t: alloc[t] for t in sorted(alloc)})
