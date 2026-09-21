#!/usr/bin/env python3
"""Phase 2J S6: Part D 100-sentence set (25 per level), adapted from phase2i/make_set.py.
Source = CORRECTED sk upload (phase2j/upload/annotations_sk_fixed.jsonl) restricted to B2-audited exercise_ids
(partB/audit/COVERAGE.json). Excludes the 60 2F-probe sentences (Slovak text) and the 100 2I sentences (Slovak text AND
exercise_id). Candidates per level = unique src (also unique across levels, levels in order A1..B2), sorted by n,
random.Random(SEED+level_index).sample(25)."""
import json, hashlib, random, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); P2J = os.path.dirname(HERE); ROOT = os.path.dirname(P2J)
SEED = 20260922
LEVELS = ['A1', 'A2', 'B1', 'B2']
PER_LEVEL = 25
ANN = os.path.join(P2J, 'upload', 'annotations_sk_fixed.jsonl')
COV = os.path.join(P2J, 'partB', 'audit', 'COVERAGE.json')
PROBE = os.path.join(ROOT, 'phase2f', 'p3', 'probe', 'data', 'sentences.json')
SET2I = os.path.join(ROOT, 'phase2i', 'set', 'sentences.jsonl')

def main():
    rows = [json.loads(l) for l in open(ANN, encoding='utf-8') if l.strip()]
    assert len(rows) == 4064
    aud = {str(x) for x in json.load(open(COV, encoding='utf-8'))['audited_exercise_ids']}
    probe = {s['slovak'] for s in json.load(open(PROBE, encoding='utf-8'))}
    s2i = [json.loads(l) for l in open(SET2I, encoding='utf-8') if l.strip()]
    ex_src = probe | {s['slovak'] for s in s2i}
    ex_eid = {str(s['exercise_id']) for s in s2i}
    assert len(probe) == 60 and len(s2i) == 100
    out, stats, gseen = [], {}, set()
    for li, lv in enumerate(LEVELS):
        lvrows = [r for r in rows if r['level'] == lv]
        st = {'rows': len(lvrows), 'audited': 0, 'excl_probe': 0, 'excl_2i': 0, 'dup_src': 0}
        cand = []
        for r in sorted(lvrows, key=lambda r: int(r['n'])):
            if str(r['exercise_id']) not in aud:
                continue
            st['audited'] += 1
            if r['src'] in probe:
                st['excl_probe'] += 1; continue
            if r['src'] in ex_src or str(r['exercise_id']) in ex_eid:
                st['excl_2i'] += 1; continue
            if r['src'] in gseen:
                st['dup_src'] += 1; continue
            gseen.add(r['src']); cand.append(r)
        st['eligible'] = len(cand)
        pick = sorted(random.Random(SEED + li).sample(cand, PER_LEVEL), key=lambda r: int(r['n']))
        st['picked'] = len(pick); stats[lv] = st
        for k, r in enumerate(pick, 1):
            out.append({'sid': int(r['n']), 'wid': 'w%s%02d' % (lv, k), 'level': lv, 'slovak': r['src'],
                        'topic': r['type_title'], 'exercise_id': r['exercise_id'], 'n': r['n'], 'annotation': r})
    assert len(out) == 100 and len({o['slovak'] for o in out}) == 100 and len({o['sid'] for o in out}) == 100
    assert not any(o['slovak'] in ex_src or str(o['exercise_id']) in ex_eid for o in out)
    assert all(str(o['exercise_id']) in aud for o in out)
    p = os.path.join(HERE, 'set', 'sentences.jsonl')
    with open(p, 'w', encoding='utf-8') as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + '\n')
    sha = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    open(p + '.sha256', 'w').write('%s  sentences.jsonl\n' % sha)
    meta = {'seed': SEED, 'per_level_seed': {lv: SEED + i for i, lv in enumerate(LEVELS)}, 'stats': stats,
            'audited_ids': len(aud), 'excluded_src': len(ex_src), 'excluded_2i_eids': len(ex_eid), 'sha256': sha,
            'source': ANN, 'method': __doc__}
    json.dump(meta, open(os.path.join(HERE, 'set', 'SET_META.json'), 'w'), indent=1)
    print(json.dumps({k: meta[k] for k in ('stats', 'sha256', 'audited_ids', 'excluded_src')}))

if __name__ == '__main__':
    main()
