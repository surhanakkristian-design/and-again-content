"""Part A: topic tiers (fixed by Kristian), eligibility check, allocation table."""
import json, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

TIERS = {
    1: [1, 3, 6, 9, 10, 12, 14, 15, 16, 21, 33, 34, 39, 40, 41, 44, 45, 47, 53, 55, 56, 57, 60, 65, 66],
    2: [2, 4, 8, 13, 17, 18, 20, 22, 23, 24, 31, 32, 35, 38, 42, 43, 46, 50, 51, 54, 59, 61, 62, 63, 67],
    3: [5, 7, 11, 19, 25, 26, 36, 37, 48, 49, 52, 58, 64],
}
TIER_ALLOC = {1: 130, 2: 85, 3: 40}
MAX_SHORT_WORDS = 12

def words(s):
    return len(s.split())

def load_rows():
    return json.load(open(os.path.join(ROOT, 'data', 'grammar_rows.json')))

def tier_of():
    return {t: tier for tier, ids in TIERS.items() for t in ids}

if __name__ == '__main__':
    rows = load_rows()
    types = json.load(open(os.path.join(ROOT, 'data', 'exercise_types.json')))
    tmap = {t['id']: t for t in types}
    by_type = collections.defaultdict(list)
    for r in rows:
        if all((r[k] or '').strip() for k in ('en', 'sk', 'cz')):
            by_type[r['type_id']].append(r)
    tiers = tier_of()
    assert len(tiers) == 63 and sum(TIER_ALLOC[t] for t in tiers.values()) == 5895
    table = []
    for tid in sorted(tiers):
        t = tmap.get(tid)
        assert t is not None, f'type {tid} missing'
        assert t['focus_en'] == 'Grammar', (tid, t)
        el = by_type[tid]
        short = [r for r in el if words(r['en']) <= MAX_SHORT_WORDS]
        alloc = TIER_ALLOC[tiers[tid]]
        table.append(dict(id=tid, title=t['title'], level=t['level'], tier=tiers[tid],
                          eligible=len(el), eligible_short=len(short), allocated=alloc,
                          short_enough=len(short) >= alloc, enough=len(el) >= alloc))
    json.dump(table, open(os.path.join(ROOT, 'measurements', 'allocation_table.json'), 'w'), indent=1)
    print('| id | title | level | tier | eligible rows | of them ≤12 words | allocated |')
    print('|---|---|---|---|---|---|---|')
    for r in table:
        print(f"| {r['id']} | {r['title']} | {r['level']} | {r['tier']} | {r['eligible']} | {r['eligible_short']} | {r['allocated']} |")
    print('total eligible', sum(r['eligible'] for r in table), 'allocated', sum(r['allocated'] for r in table))
    print('short of eligible:', [r['id'] for r in table if not r['enough']])
    print('short of <=12-word rows:', [(r['id'], r['eligible_short'], r['allocated']) for r in table if not r['short_enough']])
    lv = collections.Counter()
    for r in table: lv[r['level']] += r['allocated']
    print(dict(lv))
