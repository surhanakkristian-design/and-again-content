#!/usr/bin/env python3
"""Phase 1h step 5 - mechanical selection of 60 NEW Slovak sentences. Fixed seed, no model, no DB write.

Same source as Phase 1c: the local sentence pools under translation-offline/ that carry a Slovak sentence
with a level and a topic (phase1c/inputs/*.json first - that is what phase1c/selection.json drew from).
Stratified A1/A2/B1/B2 in the Phase 1c proportion (12/16/28/24 of 80 -> 9/12/21/18 of 60), tier-1 topics
only (the topic set the frozen 80 use), at least 6 sentences of 13-16 Slovak words, zero overlap with the
80 by id AND by Slovak text.

    python3 phase1h/select_new_sentences.py            # writes fresh/new_sentences_60.jsonl + writer_input_140.jsonl
"""
import os, sys, json, glob, random, re

HERE = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(HERE)
FRESH = os.path.join(HERE, 'fresh')
SEED = 20260919
QUOTA = {'A1': 9, 'A2': 12, 'B1': 21, 'B2': 18}
LONG_MIN = 6


def words(sk):
    return len(re.findall(r'[^\s]+', sk or ''))


def candidates():
    """Every record in the Phase 1c input pools that has a Slovak sentence, a level and a topic."""
    out = {}
    pats = [os.path.join(TO, 'phase1c', 'inputs', '*.json'),
            os.path.join(TO, 'measurements', '*.json'),
            os.path.join(TO, 'pilot', '*.json'),
            os.path.join(TO, 'phase1b', '*.json')]
    for pat in pats:
        for p in sorted(glob.glob(pat)):
            try:
                js = json.load(open(p))
            except Exception:
                continue
            rows = js if isinstance(js, list) else sum([v for v in js.values() if isinstance(v, list)], [])
            for r in rows:
                if not isinstance(r, dict):
                    continue
                sid = r.get('exercise_id') or r.get('id')
                sk = r.get('sk') or r.get('slovak')
                lv = r.get('level') or r.get('lv')
                tp = r.get('topic') or r.get('t')
                if sid and sk and lv in QUOTA and tp is not None:
                    out.setdefault(int(sid), {'sid': int(sid), 'sk': sk, 'level': lv, 'topic': tp,
                                              'source': os.path.basename(p)})
    return out


def old80():
    fs = sorted(glob.glob(os.path.join(TO, 'phase1c', 'annotated_after', '*.json')))
    return [json.load(open(f)) for f in fs]


def main():
    sys.path.insert(0, HERE)
    import checker_1h as chk
    oc, ow = chk.load_items_1h()
    old = {}
    for it in oc + ow:
        old[it['exercise_id']] = {'sid': it['exercise_id'], 'sk': it['sk'], 'level': it['level'],
                                  'topic': it['topic']}
    old_sk = {(' '.join((v['sk'] or '').lower().split())) for v in old.values()}
    tier1 = {v['topic'] for v in old.values()}
    pool = [r for sid, r in candidates().items()
            if sid not in old and ' '.join(r['sk'].lower().split()) not in old_sk]
    by_topic_name = {}
    for r in pool:
        by_topic_name[r['sid']] = r
    # tier-1 topics: the topic ids / names the frozen 80 use (topic may be an id in the pool)
    t1 = [r for r in pool if r['topic'] in tier1 or str(r['topic']) in {str(x) for x in tier1}]
    use = t1 if len(t1) >= sum(QUOTA.values()) else pool
    rnd = random.Random(SEED)
    chosen, longs = [], 0
    for lv, q in QUOTA.items():
        cell = sorted([r for r in use if r['level'] == lv], key=lambda r: r['sid'])
        rnd.shuffle(cell)
        long_cell = [r for r in cell if 13 <= words(r['sk']) <= 16]
        want_long = min(len(long_cell), max(0, 2 if lv in ('B1', 'B2') else 1))
        pick = long_cell[:want_long]
        rest = [r for r in cell if r not in pick]
        pick += rest[:max(0, q - len(pick))]
        longs += sum(1 for r in pick if 13 <= words(r['sk']) <= 16)
        chosen += pick[:q]
    if longs < LONG_MIN:
        extra = [r for r in use if 13 <= words(r['sk']) <= 16 and r not in chosen]
        rnd.shuffle(extra)
        for r in extra[:LONG_MIN - longs]:
            for i, c in enumerate(chosen):
                if not (13 <= words(c['sk']) <= 16) and c['level'] == r['level']:
                    chosen[i] = r
                    break
    os.makedirs(FRESH, exist_ok=True)
    with open(os.path.join(FRESH, 'new_sentences_60.jsonl'), 'w') as f:
        for r in sorted(chosen, key=lambda r: (r['level'], r['sid'])):
            f.write(json.dumps({'sid': r['sid'], 'sk': r['sk'], 'level': r['level'], 'topic': r['topic'],
                                'source': r.get('source')}, ensure_ascii=False) + '\n')
    with open(os.path.join(FRESH, 'writer_input_140.jsonl'), 'w') as f:
        for r in sorted(old.values(), key=lambda r: (r['level'], r['sid'])) + \
                 sorted(chosen, key=lambda r: (r['level'], r['sid'])):
            f.write(json.dumps({'sid': r['sid'], 'sk': r['sk'], 'level': r['level'],
                                'topic': r['topic']}, ensure_ascii=False) + '\n')
    print(json.dumps({'seed': SEED, 'pool': len(pool), 'tier1_pool': len(t1), 'chosen': len(chosen),
                      'levels': {lv: sum(1 for r in chosen if r['level'] == lv) for lv in QUOTA},
                      'long_13_16': sum(1 for r in chosen if 13 <= words(r['sk']) <= 16),
                      'overlap_ids': len(set(r['sid'] for r in chosen) & set(old)),
                      'writer_input': len(old) + len(chosen)}, indent=1))


if __name__ == '__main__':
    main()
