#!/usr/bin/env python3
"""Phase 1T blind judge packets — 0 model calls.

    python3 phase1t/set/build_packets_1t.py [--data-dir ...] [--judge-dir ...]

900 real items + 80 hidden duplicate controls (20 per level, the same item under a second jid),
shuffled ACROSS levels with seed 20260919 and split into 4 packets of 245:

    judge/packet_P1.json .. packet_P4.json   [{jid, slovak, answer, level}]  and nothing else
    judge/_private/_key.json                 {jid: {item, duplicate_of, sid, level}}

The key lives under judge/_private/ so that the judge's reading list (JUDGE_BRIEF_1T.md +
its packet file) can never reach it.
"""
import argparse, collections, json, os, random, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(TOFF, 'phase1s'))
from safe_json import safe_dump                                # noqa: E402

SEED = 20260919
N_ITEMS, N_DUPS, N_PACKETS, PER_LEVEL_DUPS = 900, 80, 4, 20


def build(data_dir=None, judge_dir=None, allow_partial=False):
    data_dir = data_dir or os.path.join(HERE, 'data')
    judge_dir = judge_dir or os.path.join(os.path.dirname(data_dir.rstrip(os.sep)), 'judge')
    priv = os.path.join(judge_dir, '_private')
    items = json.load(open(os.path.join(data_dir, 'items.json'), encoding='utf-8'))
    sents = {int(s['sid']): s for s in
             json.load(open(os.path.join(data_dir, 'sentences.json'), encoding='utf-8'))}
    if len(items) != N_ITEMS and not allow_partial:
        print('REFUSED: %d items, %d expected (use --allow-partial to override)'
              % (len(items), N_ITEMS))
        return 2
    by_level = collections.defaultdict(list)
    for it in items:
        by_level[sents[int(it['sid'])]['level']].append(it['id'])
    rng = random.Random(SEED)
    dups = []
    for lvl in sorted(by_level):
        pool = sorted(by_level[lvl])
        k = min(PER_LEVEL_DUPS, len(pool))
        dups += rng.sample(pool, k)
    entries = [(it['id'], False) for it in items] + [(iid, True) for iid in dups]
    rng.shuffle(entries)

    ans = {it['id']: it['answer'] for it in items}
    key, packet_rows, first = {}, [], {}
    for n, (iid, is_dup) in enumerate(entries, 1):
        if not is_dup:
            first[iid] = 'J%04d' % n
    for n, (iid, is_dup) in enumerate(entries, 1):
        jid = 'J%04d' % n
        sid = int(iid.split(':')[1])
        s = sents[sid]
        key[jid] = {'item': iid, 'duplicate_of': first[iid] if is_dup else None,
                    'sid': sid, 'level': s['level']}
        packet_rows.append({'jid': jid, 'slovak': s['slovak'], 'answer': ans[iid],
                            'level': s['level']})

    os.makedirs(judge_dir, exist_ok=True)
    os.makedirs(priv, exist_ok=True)
    size = len(packet_rows) // N_PACKETS
    rest = len(packet_rows) - size * N_PACKETS
    out, i = [], 0
    for p in range(N_PACKETS):
        n = size + (1 if p < rest else 0)
        chunk = packet_rows[i:i + n]
        i += n
        safe_dump(chunk, os.path.join(judge_dir, 'packet_P%d.json' % (p + 1)))
        out.append(len(chunk))
    safe_dump(key, os.path.join(priv, '_key.json'))

    clean = all(set(r) == {'jid', 'slovak', 'answer', 'level'} for r in packet_rows)
    rep = {'items': len(items), 'duplicate_controls': len(dups),
           'duplicates_per_level': {lvl: sum(1 for d in dups if sents[int(d.split(':')[1])]['level'] == lvl)
                                    for lvl in sorted(by_level)},
           'packet_sizes': out, 'total_jids': len(packet_rows), 'seed': SEED,
           'packet_keys_clean': clean,
           'levels_per_packet': [dict(collections.Counter(
               r['level'] for r in packet_rows[sum(out[:p]):sum(out[:p + 1])]))
               for p in range(N_PACKETS)],
           'key_path': os.path.relpath(os.path.join(priv, '_key.json'), HERE)}
    safe_dump(rep, os.path.join(os.path.dirname(judge_dir.rstrip(os.sep)), 'build_packets_1t.json'))
    print(json.dumps(rep, indent=1, sort_keys=True))
    return 0 if clean else 2


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--data-dir')
    ap.add_argument('--judge-dir')
    ap.add_argument('--allow-partial', action='store_true')
    a = ap.parse_args()
    raise SystemExit(build(a.data_dir, a.judge_dir, a.allow_partial))
