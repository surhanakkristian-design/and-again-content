#!/usr/bin/env python3
"""Phase 1P floor check — adapted from phase1n/floor_check.py.  Run BEFORE --final.

    python3 phase1p/floor_check_1p.py
    python3 phase1p/floor_check_1p.py --make-fixture [dir]   # synthetic self-test data, 0 calls

STOPS (exit 2, writes STOP_FLOOR.txt) unless all four floors hold:
    judged-wrong time-frame                >= 120
    judged-wrong with the agentless tag    >=  60
    judged-correct agentless passives      >=  60
    judged-correct determiner-variant      >=  80
Also prints the T/W/M/S balance and lever 1's detector agreement with the writers' agentless tag.
0 model calls; the judge labels it reads are already delivered at this point.
"""
import argparse, collections, json, os, random, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import loader_1p as LM                                                         # noqa: E402
import lever1                                                                  # noqa: E402

FLOORS = {'judged_wrong_timeframe': 120, 'judged_wrong_agentless': 60,
          'judged_correct_agentless': 60, 'judged_correct_determiner': 80}
STOP = os.path.join(HERE, 'STOP_FLOOR.txt')


def run(data_dir=None, judge_dir=None, out=None):
    purpose = 'Phase 1P floor check before the final run'
    sents = {int(s['sid']): s for s in LM.load_sentences(purpose, caller='floor_check_1p.py',
                                                         data_dir=data_dir)}
    ann = LM.load_annotations(purpose, caller='floor_check_1p.py', data_dir=data_dir)
    items = LM.load_items(purpose, caller='floor_check_1p.py', data_dir=data_dir)
    labels, controls, meta = LM.load_labels(purpose, caller='floor_check_1p.py', judge_dir=judge_dir)
    got = collections.Counter()
    tw, det_agree = collections.Counter(), collections.Counter()
    for it in items:
        j, t = labels.get(it['id'], (None, None))
        tags = it.get('tags') or []
        if j == 'wrong':
            tw[t or '?'] += 1
            if 'timeframe' in tags:
                got['judged_wrong_timeframe'] += 1
            if 'agentless' in tags:
                got['judged_wrong_agentless'] += 1
        elif j == 'correct':
            if 'agentless' in tags:
                got['judged_correct_agentless'] += 1
            if 'determiner' in tags:
                got['judged_correct_determiner'] += 1
        a = ann.get(str(it['sid'])) or {}
        hy = a.get('hygienised', a)
        ref = ([v for v in (hy.get('v') or []) if isinstance(v, str)] or [''])[0]
        d = lever1.detect(sents[int(it['sid'])]['slovak'], a, it['answer'], ref)
        det_agree['%s/%s' % ('agentless' if 'agentless' in tags else 'other',
                             'fires' if d['fired'] else 'silent')] += 1
    fails = {k: [got[k], v] for k, v in FLOORS.items() if got[k] < v}
    rep = {'items': len(items), 'sentences': len(sents), 'labelled': len(labels),
           'floors_required': FLOORS, 'floors_got': dict(got), 'floors_failed': fails,
           'judged': dict(collections.Counter(v[0] for v in labels.values())),
           'TWMS_balance': dict(tw), 'halves': dict(collections.Counter(
               s['tags'].get('half') or ('P1' if int(s['sid']) % 2 else 'P2') for s in sents.values())),
           'levels': dict(collections.Counter(s['level'] for s in sents.values())),
           'lever1_detector_vs_writer_agentless_tag': dict(det_agree),
           'judge_rejected_rows': len(meta.get('rejected_rows') or []),
           'judge_hidden_duplicates': len(meta.get('hidden_duplicate_rows') or [])}
    print(json.dumps(rep, indent=1, sort_keys=True))
    p = out or os.path.join(HERE, 'floor_check_1p.json')
    json.dump(rep, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    if fails:
        open(STOP, 'w', encoding='utf-8').write(json.dumps(
            {'why': 'a floor is not met; the set may not be run', 'failed': fails}, indent=1) + '\n')
        print('STOP: floors not met %s — %s written' % (json.dumps(fails), STOP))
        return 2
    print('FLOORS PASS')
    return 0


def make_fixture(d, meet=True):
    """A synthetic writer + verdict fixture (never a measurement). Pre-flights every gate."""
    os.makedirs(d, exist_ok=True)
    rng = random.Random(3)
    A, B = [], []
    for n in range(1, 121):
        lvl = ('A1', 'A2') [0 if n <= 30 else 1] if n <= 60 else ('B1', 'B2')[0 if n <= 90 else 1]
        sk = 'Veta cislo %d o tom, ako niekto nieco robi.' % n
        v = ['Sentence number %d about how somebody does something.' % n,
             'Number %d: somebody does something.' % n]
        ansrs = []
        for k in range(4):
            tags = (['agentless'] if k == 0 and (meet or n <= 10) else
                    ['determiner'] if k == 1 else ['by-passive'] if k == 2 else ['plain'])
            ansrs.append({'aid': k + 1, 'kind': 'C', 'intent': 'C', 'form': None, 'tags': tags,
                          'answer': ('The thing is done every day.' if k == 0 else
                                     'A sentence number %d about somebody.' % n if k == 1 else
                                     'Something is done by somebody number %d.' % n if k == 2 else
                                     v[0])})
        for k in range(5):
            tags = (['timeframe'] if k < 2 else ['agentless'] if k == 2 and (meet or n <= 5)
                    else ['plain'])
            ansrs.append({'aid': 5 + k, 'kind': 'W', 'intent': 'TF' if k < 2 else 'X',
                          'form': None, 'tags': tags,
                          'answer': 'Sentence number %d will do something else %d.' % (n, k)})
        row = {'sid': '1P%03d' % n, 'level': lvl, 'topic': 'selftest', 'slovak': sk,
               'annotation': {'id': 170000 + n, 'v': v, 'lk': [], 'lv': lvl,
                              'voice_sk': 'active_agent', 'agent_nom': True, 'tf_gold': 'present',
                              'tense_open': True, 'perfective_present': False},
               'answers': ansrs}
        (A if n <= 60 else B).append(row)
    json.dump(A, open(os.path.join(d, 'writer_A.json'), 'w', encoding='utf-8'), indent=1,
              ensure_ascii=False)
    json.dump(B, open(os.path.join(d, 'writer_B.json'), 'w', encoding='utf-8'), indent=1,
              ensure_ascii=False)
    jd = os.path.join(os.path.dirname(d), 'judge')
    os.makedirs(jd, exist_ok=True)
    blind, key, rows = {}, {}, []
    j = 0
    for n in range(1, 121):
        for k in range(9):
            j += 1
            kind = 'C' if k < 4 else 'W'
            aid = k + 1
            iid = '%s:%d:%d' % (kind, 170000 + n, aid)
            jid = 'J%05d' % j
            blind[jid] = iid
            key[jid] = {'sid': '1P%03d' % n, 'aid': aid, 'kind': kind}
            rows.append({'jid': jid, 'judged': 'correct' if kind == 'C' else 'wrong',
                         'type': None if kind == 'C' else rng.choice(('T', 'W', 'M', 'S')),
                         'passive': None})
    for r in rows[:20]:                                        # hidden duplicate jids (judge noise)
        rows.append(dict(r))
    json.dump(blind, open(os.path.join(jd, 'blind_map.json'), 'w', encoding='utf-8'), indent=1)
    json.dump(key, open(os.path.join(jd, '_key.json'), 'w', encoding='utf-8'), indent=1)
    json.dump(rows, open(os.path.join(jd, 'out_part1.json'), 'w', encoding='utf-8'), indent=1)
    json.dump(rows, open(os.path.join(jd, 'verdicts_part1.json'), 'w', encoding='utf-8'), indent=1)
    print('fixture written to %s (+ judge/) — meet=%s' % (d, meet))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--make-fixture', dest='fx', nargs='?', const=os.path.join(HERE, 'selftest', 'fx', 'data'))
    ap.add_argument('--no-meet', action='store_true')
    ap.add_argument('--data-dir')
    ap.add_argument('--judge-dir')
    a = ap.parse_args()
    if a.fx:
        make_fixture(a.fx, meet=not a.no_meet)
    else:
        raise SystemExit(run(a.data_dir, a.judge_dir))
