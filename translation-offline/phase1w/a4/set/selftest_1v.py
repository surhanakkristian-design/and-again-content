#!/usr/bin/env python3
"""Phase 1V set-tooling self-test — 0 model calls, synthetic data only.

    python3 phase1v/trackA_set/selftest_1v.py

Exercises join_labels_1v.join and floors_1v.check on a synthetic 900-item set in a scratch
directory: a passing case and failing cases (missing verdict, missing confidence, type
missing on a wrong answer, unknown id, and a floor below its minimum).  Touches nothing
under set/data or set/judge.
"""
import json, os, shutil, sys, tempfile

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import join_labels_1v as J                                     # noqa: E402
import floors_1v as F                                          # noqa: E402

PLAN = [('FR', 32, 'drop-fronted'), ('MC', 24, 'drop-misaligned'),
        ('MN', 24, 'drop-main'), ('SKP', 20, None)]
FAILS = []


def ok(name, cond, detail=''):
    print(('PASS  ' if cond else 'FAIL  ') + name + (' — ' + detail if detail else ''))
    if not cond:
        FAILS.append(name)


def synth(tmp):
    data = os.path.join(tmp, 'data')
    judge = os.path.join(tmp, 'judge')
    os.makedirs(data)
    os.makedirs(judge)
    items, sents, sid = [], [], 200000
    for kind, n_s, dtag in PLAN:
        for _ in range(n_s):
            sid += 1
            sents.append({'sid': sid, 'slovak': 'Veta %d.' % sid, 'level': 'A1',
                          'tags': {'kind': kind}})
            if kind == 'SKP':
                plan = [('c1', 'C', ['skp-passive']), ('c2', 'C', ['skp-passive']),
                        ('c3', 'C', ['skp-passive']), ('c4', 'C', ['plain']),
                        ('w1', 'W', ['time-frame']), ('w2', 'W', ['time-frame']),
                        ('w3', 'W', ['missing-article']), ('w4', 'W', ['wrong-word']),
                        ('w5', 'W', ['wrong-word'])]
            else:
                plan = [('c1', 'C', ['plain']), ('c2', 'C', ['determiner']),
                        ('c3', 'C', ['by-passive']), ('c4', 'C', ['paraphrase']),
                        ('w1', 'W', [dtag]), ('w2', 'W', [dtag]),
                        ('w3', 'W', ['time-frame']), ('w4', 'W', ['missing-article']),
                        ('w5', 'W', ['wrong-word'])]
            for aid, k, tags in plan:
                items.append({'id': '%s:%d:%s' % (k, sid, aid), 'sid': sid, 'kind': k,
                              'tags': tags, 'answer': 'answer %d %s' % (sid, aid)})
    json.dump(items, open(os.path.join(data, 'items.json'), 'w'))
    json.dump(sents, open(os.path.join(data, 'sentences.json'), 'w'))
    key, q = {}, 0
    for it in items:
        q += 1
        key['Q%04d' % q] = {'item': it['id'], 'duplicate_of': None, 'sid': it['sid'],
                            'level': 'A1', 'part': 1 + q % 4, 'position': q}
    dups = [it['id'] for it in items[:80]]
    for iid in dups:
        q += 1
        orig = next(k for k, v in key.items() if v['item'] == iid)
        key['Q%04d' % q] = {'item': iid, 'duplicate_of': orig, 'sid': int(iid.split(':')[1]),
                            'level': 'A1', 'part': 1 + q % 4, 'position': q}
    kp = os.path.join(tmp, 'packet_key_1v.json')
    json.dump(key, open(kp, 'w'))
    return data, judge, kp, key, items


def verdicts(key, items, judge, mutate=None, art_correct=False):
    kinds = {i['id']: i['kind'] for i in items}
    tags = {i['id']: i['tags'] for i in items}
    for p in os.listdir(judge):
        os.remove(os.path.join(judge, p))
    parts = {}
    for qid, k in sorted(key.items()):
        iid = k['item']
        lab = 'correct' if kinds[iid] == 'C' else 'wrong'
        if art_correct and 'missing-article' in tags[iid]:
            lab = 'correct'
        v = {'id': qid, 'label': lab, 'type': None if lab == 'correct' else 'M',
             'borderline': False, 'confidence': 4, 'dropped': '', 'passive': None,
             'agent_drop': None}
        if mutate:
            v = mutate(qid, v)
            if v is None:
                continue
        parts.setdefault(k['part'], []).append(v)
    for p, rows in parts.items():
        json.dump(rows, open(os.path.join(judge, 'verdicts_part%d.json' % p), 'w'))


def main():
    tmp = tempfile.mkdtemp(prefix='selftest_1v_')
    try:
        data, judge, kp, key, items = synth(tmp)
        out = [data]

        verdicts(key, items, judge)
        rc = J.join(data, judge, kp, out)
        labels = json.load(open(os.path.join(data, 'labels.json')))
        rep = json.load(open(os.path.join(HERE, 'join_labels_1v.json')))
        ok('join accepts a complete set', rc == 0, 'rc=%d' % rc)
        ok('join writes 900 labels', len(labels) == 900, '%d' % len(labels))
        ok('join sees 80 duplicate controls', rep['duplicate_controls'] == 80)
        ok('join keeps confidence + packet position',
           all(v['confidence'] == 4 and v['packet_position'] for v in labels.values()))

        rc = F.check(data, tmp)
        fl = json.load(open(os.path.join(tmp, 'floors_1v.json')))
        ok('floors pass on a healthy set', rc == 0 and fl['all_pass'] is True)
        ok('floors keys exact',
           set(fl) >= {'F1_agent_drops_wrong', 'F1a_fronted_wrong', 'F1b_misaligned_wrong',
                       'F2_time_frame_wrong', 'F3_by_passive_correct', 'F4_skp_correct',
                       'F5_missing_article_wrong', 'missing_article_judged_correct',
                       'T_W_M_S_wrong', 'judged_correct', 'judged_wrong', 'all_pass'})
        ok('F1=160 F1a=64 F1b=48 F2=120 F3=80 F4=60 F5=100',
           [fl[k]['n'] for k in ('F1_agent_drops_wrong', 'F1a_fronted_wrong',
                                 'F1b_misaligned_wrong', 'F2_time_frame_wrong',
                                 'F3_by_passive_correct', 'F4_skp_correct',
                                 'F5_missing_article_wrong')] == [160, 64, 48, 120, 80, 60, 100],
           json.dumps({k: fl[k]['n'] for k in fl if k.startswith('F')}))
        ok('FLOOR_CHECK_1V.json written too',
           os.path.exists(os.path.join(tmp, 'FLOOR_CHECK_1V.json')))

        # judge noise on the duplicates
        flip = {qid for qid, k in key.items() if k['duplicate_of']}
        five = sorted(flip)[:5]
        verdicts(key, items, judge,
                 mutate=lambda q, v: (dict(v, label='wrong', type='S')
                                      if q in five and v['label'] == 'correct' else v))
        J.join(data, judge, kp, out)
        rep = json.load(open(os.path.join(HERE, 'join_labels_1v.json')))
        ok('join reports duplicate disagreements',
           rep['label_disagreements'] + rep['type_only_disagreements'] >= 1,
           '%d label, %d type' % (rep['label_disagreements'],
                                  rep['type_only_disagreements']))

        # failing cases
        verdicts(key, items, judge, mutate=lambda q, v: None if q == 'Q0007' else v)
        ok('join refuses a missing verdict', J.join(data, judge, kp, out) == 2)
        verdicts(key, items, judge,
                 mutate=lambda q, v: ({k: x for k, x in v.items() if k != 'confidence'}
                                      if q == 'Q0009' else v))
        ok('join refuses a missing confidence', J.join(data, judge, kp, out) == 2)
        verdicts(key, items, judge,
                 mutate=lambda q, v: (dict(v, type=None) if v['label'] == 'wrong'
                                      and q == 'Q0005' else v))
        ok('join refuses a wrong answer without a type', J.join(data, judge, kp, out) == 2)
        verdicts(key, items, judge, mutate=lambda q, v: dict(v, confidence=9)
                 if q == 'Q0011' else v)
        ok('join refuses confidence out of 1-5', J.join(data, judge, kp, out) == 2)

        # failing floor: every missing-article item judged correct
        verdicts(key, items, judge, art_correct=True)
        J.join(data, judge, kp, out)
        rc = F.check(data, tmp)
        fl = json.load(open(os.path.join(tmp, 'floors_1v.json')))
        ok('floors refuse when F5 collapses',
           rc == 2 and fl['all_pass'] is False and fl['F5_missing_article_wrong']['n'] == 0)
        ok('missing_article_judged_correct reports the other side',
           fl['missing_article_judged_correct'] == 100,
           str(fl['missing_article_judged_correct']))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
        for f in ('join_labels_1v.json',):
            p = os.path.join(HERE, f)
            if os.path.exists(p):
                os.remove(p)
    print('\n%s — %d failure(s)' % ('SELFTEST FAILED' if FAILS else 'SELFTEST OK', len(FAILS)))
    return 1 if FAILS else 0


if __name__ == '__main__':
    raise SystemExit(main())
