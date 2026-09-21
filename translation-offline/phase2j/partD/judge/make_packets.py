#!/usr/bin/env python3
"""Phase 2J S7 (copied from phase2i/judge/make_packets.py, absolute paths, fresh seed 20260923): build 4 judge packets of 245 (900 originals + 80 hidden duplicate controls).
Packets carry ONLY jid / slovak / level / answer / topic. jid->aid map in judge/key.jsonl (never shown to judges).
Deterministic: seed 20260923.
- originals: shuffled, 225 per session (i % 4) -> every session mixes all four levels.
- controls: from each original session, per level 5 answers (session index even: 3 correct + 2 wrong by writer
  intent, odd: 2 + 3) -> 20 per level, 40 correct / 40 wrong intent; the duplicate goes to session
  (orig + d(level)) % 4 with d = {A1:1, A2:2, B1:3, B2:1} -> always a DIFFERENT session, 20 per session.
- jids opaque (random 5-hex, unique); each packet shuffled."""
import json, os, random, hashlib
HERE = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j/partD/judge'
P2I = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j/partD'   # set dir parent (answers at partD/set/answers.jsonl)
SEED = 20260923
LEVELS = ['A1', 'A2', 'B1', 'B2']
SHIFT = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 1}

def build():
    ans = [json.loads(l) for l in open(os.path.join(P2I, 'set', 'answers.jsonl'), encoding='utf-8')]
    assert len(ans) == 900 and len({a['aid'] for a in ans}) == 900
    rng = random.Random(SEED)
    order = ans[:]; rng.shuffle(order)
    sess_of = {a['aid']: i % 4 for i, a in enumerate(order)}
    entries = [(a, sess_of[a['aid']], False) for a in order]
    controls = []
    for s in range(4):
        for lv in LEVELS:
            nc = 3 if s % 2 == 0 else 2
            pool_c = sorted([a for a in ans if sess_of[a['aid']] == s and a['level'] == lv and a['writer_intent'] == 'correct'], key=lambda a: a['aid'])
            pool_w = sorted([a for a in ans if sess_of[a['aid']] == s and a['level'] == lv and a['writer_intent'] == 'wrong'], key=lambda a: a['aid'])
            for a in rng.sample(pool_c, nc) + rng.sample(pool_w, 5 - nc):
                t = (s + SHIFT[lv]) % 4
                assert t != s
                controls.append((a, t, True))
    assert len(controls) == 80
    entries += controls
    jids = set()
    def new_jid():
        while True:
            j = 'j%05x' % rng.randrange(16 ** 5)
            if j not in jids:
                jids.add(j); return j
    key, packets = [], {s: [] for s in range(4)}
    for a, s, dup in entries:
        j = new_jid()
        key.append({'jid': j, 'aid': a['aid'], 'session': s + 1, 'is_control': dup, 'orig_session': sess_of[a['aid']] + 1})
        packets[s].append({'jid': j, 'slovak': a['slovak'], 'level': a['level'], 'answer': a['answer'], 'topic': a['topic']})
    for s in range(4):
        rng.shuffle(packets[s])
        assert len(packets[s]) == 245
        assert {p['level'] for p in packets[s]} == set(LEVELS)
        # no aid twice within a session
        aids = [k['aid'] for k in key if k['session'] == s + 1]
        assert len(aids) == len(set(aids)) == 245
    with open(os.path.join(HERE, 'key.jsonl'), 'w', encoding='utf-8') as f:
        for k in key: f.write(json.dumps(k, ensure_ascii=False) + '\n')
    meta = {'seed': SEED, 'sessions': {}, 'controls': 80}
    for s in range(4):
        p = os.path.join(HERE, 'packet_s%d.jsonl' % (s + 1))
        with open(p, 'w', encoding='utf-8') as f:
            for it in packets[s]: f.write(json.dumps(it, ensure_ascii=False) + '\n')
        lv = {l: sum(1 for it in packets[s] if it['level'] == l) for l in LEVELS}
        meta['sessions'][s + 1] = {'items': 245, 'controls': sum(1 for k in key if k['session'] == s + 1 and k['is_control']),
                                   'levels': lv, 'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest()}
    cl = [k for k in key if k['is_control']]
    byaid = {a['aid']: a for a in ans}
    meta['controls_by_level'] = {l: sum(byaid[k['aid']]['level'] == l for k in cl) for l in LEVELS}
    meta['controls_by_intent'] = {i: sum(byaid[k['aid']]['writer_intent'] == i for k in cl) for i in ('correct', 'wrong')}
    meta['controls_session_pairs'] = {}
    for k in cl:
        pr = '%d->%d' % (k['orig_session'], k['session'])
        meta['controls_session_pairs'][pr] = meta['controls_session_pairs'].get(pr, 0) + 1
    json.dump(meta, open(os.path.join(HERE, 'PACKETS_META.json'), 'w'), indent=1)
    print(json.dumps(meta))

if __name__ == '__main__':
    build()
