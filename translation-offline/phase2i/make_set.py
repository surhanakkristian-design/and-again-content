#!/usr/bin/env python3
"""Phase 2I stage 3: pick the 100-sentence set (25 per level) from the Part 0 SK annotations.
Excludes the 60 2F probe sentences (by Slovak text, CONTEXT 3.2; 2G Part A reused the same 60).
Deterministic: SEED below; candidates per level = unique src not excluded, sorted by n, then Random(SEED+level_index).sample."""
import json, hashlib, random, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SEED = 20260921
LEVELS = ['A1', 'A2', 'B1', 'B2']
PER_LEVEL = 25
ANN = os.path.join(HERE, 'upload', 'annotations_sk_fixed.jsonl')
PROBE = os.path.join(ROOT, 'phase2f', 'p3', 'probe', 'data', 'sentences.json')
PARTA = os.path.join(ROOT, 'phase2g', 'partA', 'data', 'sentences.json')

def main():
    rows = [json.loads(l) for l in open(ANN, encoding='utf-8') if l.strip()]
    assert len(rows) == 4064
    excl = {s['slovak'] for s in json.load(open(PROBE, encoding='utf-8'))}
    excl_a = {s['slovak'] for s in json.load(open(PARTA, encoding='utf-8'))}
    assert len(excl) == 60 and excl_a <= excl, 'exclusion set changed'
    found = sum(1 for r in rows if r['src'] in excl)
    out, stats = [], {}
    for li, lv in enumerate(LEVELS):
        seen, cand = set(), []
        for r in sorted((r for r in rows if r['level'] == lv), key=lambda r: r['n']):
            if r['src'] in excl or r['src'] in seen:
                continue
            seen.add(r['src']); cand.append(r)
        pick = sorted(random.Random(SEED + li).sample(cand, PER_LEVEL), key=lambda r: r['n'])
        stats[lv] = {'candidates': len(cand), 'picked': len(pick)}
        for k, r in enumerate(pick, 1):
            out.append({'sid': r['n'], 'wid': 'w%s%02d' % (lv, k), 'level': lv, 'slovak': r['src'],
                        'topic': r['type_title'], 'exercise_id': r['exercise_id'], 'n': r['n'],
                        'annotation': r})
    assert len(out) == 100 and len({o['slovak'] for o in out}) == 100
    assert not any(o['slovak'] in excl for o in out)
    os.makedirs(os.path.join(HERE, 'set'), exist_ok=True)
    p = os.path.join(HERE, 'set', 'sentences.jsonl')
    with open(p, 'w', encoding='utf-8') as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + '\n')
    sha = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    open(p + '.sha256', 'w').write('%s  sentences.jsonl\n' % sha)
    meta = {'seed': SEED, 'per_level_seed': {lv: SEED + i for i, lv in enumerate(LEVELS)}, 'stats': stats,
            'excluded_probe_found_in_annotations': found, 'excluded_count': len(excl), 'sha256': sha,
            'method': 'unique src per level, excluding 2F probe (=2G partA) Slovak texts, sorted by n, random.Random(seed+level_index).sample(25)'}
    json.dump(meta, open(os.path.join(HERE, 'set', 'SET_META.json'), 'w'), indent=1)
    print(json.dumps(meta))

if __name__ == '__main__':
    main()
