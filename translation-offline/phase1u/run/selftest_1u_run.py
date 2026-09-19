#!/usr/bin/env python3
"""Phase 1U run-tooling self-tests - SYNTHETIC rows only, 0 model calls, 0 network.
The measuring apparatus is suspected first: the floors gate (incl. a misspelt key), the
chk-degenerate stop, the hard-cap stop, failed-call handling, the scorer (incl. every pre-declared
sensitivity, hand-computed) and the prompt assertion.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1u/run/selftest_1u_run.py
"""
import datetime
import json
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import runner_1u as RU                                                        # noqa: E402
import score_1u as SC                                                         # noqa: E402
from safe_json import safe_dump, guarded_run, flush_log                       # noqa: E402

RU.mirror_to_dev = lambda *a, **k: 0        # the self-test NEVER touches phase1u/ledger_dev.jsonl
CHECKS = []


def ck(name, ok, detail=''):
    CHECKS.append({'check': name, 'ok': bool(ok), 'detail': str(detail)[:300]})
    print('[SELFTEST] %-46s %s  %s' % (name, 'PASS' if ok else 'FAIL', str(detail)[:160]),
          flush=True)


def refuses(fn):
    try:
        fn()
    except SystemExit as e:
        return 'SystemExit: %s' % e
    except Exception as e:
        return 'UNEXPECTED %s: %s' % (type(e).__name__, e)
    return ''


# ------------------------------------------------------------------ fixture (synthetic)
def make_fixture(d):
    os.makedirs(d, exist_ok=True)
    sents = [
        {'sid': 190001, 'slovak': 'Mama upiekla velku tortu.', 'level': 'A1', 'topic': 'synthetic',
         'tags': {'half': 'P1', 'kind': 'ACT', 'tf_gold': 'past',
                  'writer_tags': {'nom_agent': True, 'agent': 'Mama', 'emb_agent': None,
                                  'emb_type': None, 'passivizable': True,
                                  'impersonal_or_passive': False, 'kind': 'ACT', 'emb': False}}},
        {'sid': 190002, 'slovak': 'Peter kontroluje schranku kazde rano.', 'level': 'A2',
         'topic': 'synthetic',
         'tags': {'half': 'P2', 'kind': 'ACT', 'tf_gold': 'present',
                  'writer_tags': {'nom_agent': True, 'agent': 'Peter', 'emb_agent': None,
                                  'emb_type': None, 'passivizable': True,
                                  'impersonal_or_passive': False, 'kind': 'ACT', 'emb': False}}},
        {'sid': 190003, 'slovak': 'Okno bolo zatvorene pred burkou.', 'level': 'B1',
         'topic': 'synthetic',
         'tags': {'half': 'P1', 'kind': 'PAS', 'tf_gold': 'past',
                  'writer_tags': {'nom_agent': False, 'agent': None, 'emb_agent': None,
                                  'emb_type': None, 'passivizable': False,
                                  'impersonal_or_passive': True, 'kind': 'PAS', 'emb': False}}}]
    ann = {'190001': {'voice_sk': 'active_agent', 'agent_nom': True, 'tf_gold': 'past',
                      'tense_open': False, 'perfective_present': False,
                      'hygienised': {'id': 190001, 'lv': 'A1', 'lk': ['baked'],
                                     'v': ['Mum baked a big cake.',
                                           'Mother has baked a large cake.']}},
           '190002': {'voice_sk': 'active_agent', 'agent_nom': True, 'tf_gold': 'present',
                      'tense_open': True, 'perfective_present': False,
                      'hygienised': {'id': 190002, 'lv': 'A2', 'lk': ['checks'],
                                     'v': ['Peter checks the letterbox every morning.',
                                           'Every morning Peter checks the letterbox.']}},
           '190003': {'voice_sk': 'passive', 'agent_nom': False, 'tf_gold': 'past',
                      'tense_open': False, 'perfective_present': False,
                      'hygienised': {'id': 190003, 'lv': 'B1', 'lk': ['closed'],
                                     'v': ['The window was closed before the storm.']}}}
    items = [
        {'id': 'W:190001:agdrop', 'sid': 190001, 'kind': 'W', 'intent': 'M', 'form': None,
         'tags': ['drop-main'], 'passive': 'agentless', 'answer': 'A big cake was baked.'},
        {'id': 'C:190001:same', 'sid': 190001, 'kind': 'C', 'intent': 'C', 'form': None,
         'tags': ['determiner'], 'passive': None, 'answer': 'Mum baked the big cake.'},
        {'id': 'W:190001:tip', 'sid': 190001, 'kind': 'W', 'intent': 'T', 'form': None,
         'tags': ['time-frame'], 'passive': None, 'answer': 'Mum will bake a big cake.'},
        {'id': 'W:190001:diff', 'sid': 190001, 'kind': 'W', 'intent': 'M', 'form': None,
         'tags': ['missing-article'], 'passive': None, 'answer': 'Mum baked big cake.'},
        {'id': 'C:190002:same', 'sid': 190002, 'kind': 'C', 'intent': 'C', 'form': None,
         'tags': ['plain'], 'passive': None, 'answer': 'Peter checks a letterbox every morning.'},
        {'id': 'W:190002:agdrop', 'sid': 190002, 'kind': 'W', 'intent': 'M', 'form': None,
         'tags': ['drop-fronted'], 'passive': 'agentless',
         'answer': 'The letterbox is checked every morning.'},
        {'id': 'W:190002:diff', 'sid': 190002, 'kind': 'W', 'intent': 'M', 'form': None,
         'tags': ['plain'], 'passive': None, 'answer': 'Peter checks the postbox every evening.'},
        {'id': 'C:190003:same', 'sid': 190003, 'kind': 'C', 'intent': 'C', 'form': None,
         'tags': ['skp-passive'], 'passive': 'agentless',
         'answer': 'The window had been closed before the storm.'},
        {'id': 'W:190003:tip', 'sid': 190003, 'kind': 'W', 'intent': 'W', 'form': None,
         'tags': ['skp-passive'], 'passive': 'agentless',
         'answer': 'The window was shut before the storm.'}]
    labels = {}
    for k, it in enumerate(items):
        wrong = it['kind'] == 'W'
        labels[it['id']] = {'judged': 'wrong' if wrong else 'correct',
                            'type': it['intent'] if wrong else None, 'passive': it['passive'],
                            'tip': False, 'borderline': it['id'] == 'W:190002:agdrop',
                            'confidence': 3 + (k % 3), 'dropped': '', 'packet_part': 1,
                            'packet_position': k + 1, 'qid': 'Q%04d' % (k + 1)}
    safe_dump(sents, os.path.join(d, 'sentences.json'))
    safe_dump(ann, os.path.join(d, 'annotations.json'))
    safe_dump(items, os.path.join(d, 'items.json'))
    safe_dump(labels, os.path.join(d, 'labels.json'))
    return d


def stub(empty_for=(), wall_after=None):
    state = {'n': 0}

    def fn(req, need):
        st = {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
        for h in sorted(need):
            _s, _u, _g, hh, variant, iid = req[h]
            if wall_after is not None and state['n'] >= wall_after:
                st['wall'] = True
                st['skipped'] += 1
                continue
            v = ('TIP' if iid.endswith(':tip') else 'DIFF' if iid.endswith(':diff') else 'SAME')
            bad = iid in empty_for
            row = {'ts': datetime.datetime.now().isoformat(timespec='seconds'), 'req_hash': hh,
                   'item_id': iid, 'variant': variant, 'http': 200, 'counted': True,
                   'verdict': None if bad else v, 'reply': '' if bad else json.dumps({'verdict': v}),
                   'model': 'STUB', 'empty': bad, 'latency_ms': 12, 'tokens_in': 300,
                   'tokens_out': 1}
            with open(RU.CALLS, 'a', encoding='utf-8') as fh:
                fh.write(json.dumps(row, ensure_ascii=False) + '\n')
                flush_log(fh)
            state['n'] += 1
            st['ok' if not bad else 'empty'] += 1
        return st
    return fn


def fresh(root, name):
    d = os.path.join(root, name)
    if os.path.isdir(d):
        for f in os.listdir(d):
            os.remove(os.path.join(d, f))
    os.makedirs(d, exist_ok=True)
    return d


# ------------------------------------------------------------------ 1. floors gate
def floors_gate_test(root):
    good = {k: {'n': 999, 'min': 10, 'pass': True} for k in RU.FLOOR_KEYS_1U}
    good['all_pass'] = True
    p = os.path.join(root, 'floors_pass.json')
    safe_dump(good, p)
    ok1 = refuses(lambda: RU.check_floors_1u(p)) == ''
    bad = json.loads(json.dumps(good))
    bad['F5_missing_article_wrong'] = {'n': 3, 'min': 40, 'pass': False}
    bad['all_pass'] = False
    p2 = os.path.join(root, 'floors_fail.json')
    safe_dump(bad, p2)
    r2 = refuses(lambda: RU.check_floors_1u(p2))
    mis = json.loads(json.dumps(good))
    mis['F1_agentdrop_any_wrong'] = mis.pop('F1_agent_drops_wrong')      # the 1T key-spelling trap
    p3 = os.path.join(root, 'floors_misspelt.json')
    safe_dump(mis, p3)
    r3 = refuses(lambda: RU.check_floors_1u(p3))
    ck('floors gate: correct keys + all_pass -> runs', ok1)
    ck('floors gate: a failing floor REFUSES', 'REFUSED' in r2 and 'F5' in r2, r2)
    ck('floors gate: a misspelt key REFUSES (the 1T trap)',
       'REFUSED' in r3 and 'F1_agent_drops_wrong' in r3, r3)


# ------------------------------------------------------------------ 2. cap + counted
def cap_test(root):
    p = os.path.join(root, 'ledger_synth.jsonl')
    with open(p, 'w', encoding='utf-8') as fh:
        for i in range(5):
            fh.write(json.dumps({'http': 200, 'counted': True, 'verdict': 'SAME'}) + '\n')
        for h in (429, 500, 0):
            fh.write(json.dumps({'http': h, 'counted': False}) + '\n')
    ck('counted = HTTP 200 only (429/5xx/0 are not counted)', RU.counted_dev(p) == 5,
       'counted_dev=%d of 8 rows' % RU.counted_dev(p))
    orig = RU.counted_dev
    try:
        RU.counted_dev = lambda *a, **k: 895
        r = refuses(lambda: RU.cap_check(10, 'selftest:cap'))
        ck('hard cap: 895 + 10 > 900 STOPS and prints the numbers',
           'STOP' in r and '895' in r and '900' in r, r)
        RU.counted_dev = lambda *a, **k: 899
        ok = refuses(lambda: RU.cap_check(1, 'selftest:cap')) == ''
        ck('hard cap: 899 + 1 = 900 is allowed', ok)
    finally:
        RU.counted_dev = orig


# ------------------------------------------------------------------ 3. chk-degenerate
def degenerate_test(root, fixture):
    ck('chk_degenerate(): one accepting class is degenerate',
       RU.chk_degenerate({'chk_distribution': {'correct/auto': 9}})
       and not RU.chk_degenerate({'chk_distribution': {'correct/auto': 5, 'wrong/auto': 4}}))
    orig = RU.R1T.build
    try:
        def fake(data_dir, tag, purpose, loader=RU.LM):
            out = list(orig(data_dir, tag, purpose, loader))
            out[6] = dict(out[6], chk_distribution={'correct/auto': out[6]['n_items']})
            return tuple(out)
        RU.R1T.build = fake
        d = fresh(root, 'run_degenerate')
        RU.set_run_dir(d)
        r = refuses(lambda: RU.preflight(fixture, 'synthetic', 'selftest', RU.LM, cap=False))
        ck('degenerate chk STOPS with 0 calls',
           'STOP' in r and os.path.exists(os.path.join(d, 'STOP_CHK.txt'))
           and not os.path.exists(os.path.join(d, 'calls.jsonl')), r)
    finally:
        RU.R1T.build = orig
        RU.set_run_dir(HERE)


# ------------------------------------------------------------------ 4. the run paths
def run_tests(root, fixture):
    d1 = fresh(root, 'run_clean')
    out = RU.final_core(d1, fixture, 'synthetic', RU.LM, stub(), checks=False)
    rows = {r['item_id']: r for r in out['rows']}
    ag = [r for r in out['rows'] if r['ag']['fired']]
    ck('AG v4 rejects before L3 (0 calls for those items)',
       ag and all(not r['final_accept'] and not r['layers']['planned_call'] for r in ag)
       and any(r['final_layer'] == 'AG' for r in ag),
       '%d AG rejections, layers %s' % (len(ag), sorted({r['final_layer'] for r in ag})))
    l3 = [r for r in out['rows'] if r['layers']['planned_call']]
    ck('L3 reached and an item accepted there',
       any(r['final_accept'] and r['final_layer'] == 'L3' for r in l3),
       '%d planned calls' % len(l3))
    ck('TIP is a rejection',
       any(r['final_layer'] == 'L3:TIPrej' and not r['final_accept'] for r in out['rows']))
    ck('AG shadows recorded (v2 / v3 / guarded union / full v4)',
       all(set(r['ag_shadow']) == set(RU.AG_SHADOWS_1U) for r in out['rows']),
       json.dumps(out['build']['ag'], sort_keys=True))
    lines = [json.loads(x) for x in open(os.path.join(d1, 'access_log.jsonl'), encoding='utf-8')
             if x.strip()]
    lab_at = [k for k, r in enumerate(lines) if r['what'] == 'data/labels.json']
    ck('labels.json is read LAST, after every verdict',
       bool(lab_at) and lab_at[0] == len(lines) - 1, 'label read at %s of %d' % (lab_at, len(lines)))
    r1 = refuses(lambda: RU.final_core(d1, fixture, 'synthetic', RU.LM, stub(), checks=False))
    ck('a second --final on a finished dir REFUSES', 'REFUSED' in r1, r1)
    d2 = fresh(root, 'run_verdicts_exist')
    RU.set_run_dir(d2)
    open(os.path.join(d2, 'calls.jsonl'), 'a').write('')
    r2 = refuses(lambda: RU.final_core(d2, fixture, 'synthetic', RU.LM, stub(), checks=False))
    ck('--final REFUSES when a verdict file already exists',
       'REFUSED' in r2 and 'second --final' in r2, r2)
    # failed call
    d3 = fresh(root, 'run_failed')
    o3 = RU.final_core(d3, fixture, 'synthetic', RU.LM, stub(empty_for=('W:190002:diff',)),
                       checks=False)
    bad = [r for r in o3['rows'] if r['call_failed']]
    ver, failed, counted = RU.ledger_state_1u(os.path.join(d3, 'calls.jsonl'))
    ck('an empty 200 reply is a FAILED call: counted, not retried, item flagged',
       len(bad) == 1 and bad[0]['item_id'] == 'W:190002:diff' and len(failed) == 1
       and counted == o3['calls']['counted_calls'] and o3['headline']['failed_calls'] == 1
       and bad[0]['judged'] == 'wrong',
       'failed=%s counted=%d accepted=%s' % ([r['item_id'] for r in bad], counted,
                                             bad[0]['final_accept'] if bad else None))
    # crash + offline replay
    d4 = fresh(root, 'run_crash')
    try:
        guarded_run(lambda: RU.final_core(d4, fixture, 'synthetic', RU.LM, stub(), checks=False,
                                          crash_at='aggregation'),
                    os.path.join(d4, 'FINAL_RUN_DONE.attempt'),
                    meta_fn=lambda r: {'status': (r or {}).get('status')})
    except Exception:
        pass
    before = RU.ledger_state_1u(os.path.join(d4, 'calls.jsonl'))[2]
    o4 = RU.final_core(d4, fixture, 'synthetic', RU.LM, None, checks=False, offline=True)
    after = RU.ledger_state_1u(os.path.join(d4, 'calls.jsonl'))[2]
    same = (json.dumps(o4['rows'], sort_keys=True, default=str)
            == json.dumps(out['rows'], sort_keys=True, default=str))
    ck('crash -> recompute from the stored verdicts, 0 new calls, identical rows',
       o4.get('status') == 'DONE' and before == after and same,
       'calls %d/%d, rows identical %s' % (before, after, same))
    RU.set_run_dir(HERE)
    return out


# ------------------------------------------------------------------ 5. prompt assertion
def prompt_test(fixture):
    cfg, sel, st, recs, ann, by, info, ag = RU.build(fixture, 'synthetic', 'selftest prompt')
    rep = RU.assert_prompt(st, recs[0])
    ck('prompt = 1T prompt + EXACTLY one line, after the levers, before the tail',
       rep['ok'] and rep['lines_1u'] == rep['lines_1t'] + 1
       and rep['added_line'] == RU.AL.ARTICLE_LINE_1U,
       'added at line %d; before: %r; after: %r' % (rep['added_at_line'], rep['line_before'][:40],
                                                    (rep['line_after'] or '')[:30]))
    ck('the ruling text matches phase1u/RULING_ARTICLE.txt', RU.AL.CHECK['ok'],
       json.dumps(RU.AL.CHECK))
    orig = RU.AL.ARTICLE_LINE_1U
    try:
        RU.AL.ARTICLE_LINE_1U = orig + ' TAMPERED'
        r = refuses(RU.AL.check)          # the guard: the literal vs stack/L3_PROMPT_1U.txt
        r2 = refuses(lambda: RU.assert_prompt(st, dict(recs[0], _extra=[])))
        ck('a tampered line is caught (literal vs L3_PROMPT_1U.txt)',
           'REFUSED' in r and 'ARTICLE_LINE_1U differs' in r, r)
        ck('the assertion still holds shape-wise on a tampered line (one added line only)',
           r2 == '', r2)
    finally:
        RU.AL.ARTICLE_LINE_1U = orig
    return rep


# ------------------------------------------------------------------ 6. the scorer, hand-computed
def synth_rows():
    base = [('C:190001:a', 190001, 'A1', 'C', 'correct', None, True, 'L3', ['plain'], 4),
            ('C:190002:a', 190002, 'A1', 'C', 'correct', None, True, 'L3', ['by-passive'], 5),
            ('W:190003:a', 190003, 'A2', 'W', 'correct', None, False, 'L3', ['skp-passive'], 2),
            ('C:190004:a', 190004, 'A2', 'C', 'correct', None, True, 'L3', ['skp-passive'], 5),
            ('C:190005:b', 190005, 'B1', 'C', 'correct', None, True, 'L3', ['by-passive'], 3),
            ('C:190006:b', 190006, 'B1', 'C', 'correct', None, True, 'L3', ['plain'], 3),
            ('W:190007:a', 190007, 'B2', 'W', 'wrong', 'M', True, 'L3', ['missing-article'], 2),
            ('W:190008:a', 190008, 'B2', 'W', 'wrong', 'M', False, 'AG', ['drop-main'], 4),
            ('W:190009:a', 190009, 'A1', 'W', 'wrong', 'T', False, 'L3', ['time-frame'], 5),
            ('W:190010:a', 190010, 'A2', 'W', 'wrong', 'M', False, 'AG', ['drop-fronted'], 5),
            ('W:190011:a', 190011, 'B1', 'W', 'wrong', 'M', False, 'AG', ['drop-misaligned'], 4),
            ('W:190012:a', 190012, 'B2', 'W', 'wrong', 'S', False, 'L2', ['drop-other'], 3)]
    rows = []
    for k, (iid, sid, lv, kind, judged, ty, acc, layer, tags, conf) in enumerate(base):
        rows.append({'item_id': iid, 'sid': sid, 'level': lv, 'kind': kind, 'judged': judged,
                     'judged_type': ty, 'final_accept': acc, 'final_layer': layer, 'tags': tags,
                     'confidence': conf, 'packet_position': k + 1, 'borderline': iid.endswith(':b'),
                     'sk': 'SK %d' % sid, 'answer': 'EN %d' % sid, 'call_failed': False,
                     'ag': {'fired': layer == 'AG', 'reason': 'synthetic'},
                     'ag_shadow': {n: {'fired': layer == 'AG'} for n in SC.SHADOWS},
                     'layers': {'model': 'SAME' if acc else 'DIFF'}})
    return rows


def scorer_selftest():
    rows = synth_rows()
    out, empty = SC.score({'rows': rows, 'calls': {'tokens_in': 1000, 'tokens_out': 12,
                                                   'counted_calls': 4}})
    h = out['headline']
    ck('scorer: pooled coverage 5/6, FA 1/6 (hand-computed)',
       [h['pooled']['coverage']['k'], h['pooled']['coverage']['n']] == [5, 6]
       and [h['pooled']['fa']['k'], h['pooled']['fa']['n']] == [1, 6],
       'cov %s fa %s' % (SC.f(h['pooled']['coverage']), SC.f(h['pooled']['fa'])))
    ck('scorer: P1 = odd sid, P2 = even sid, never averaged',
       [h['P1']['coverage']['n'], h['P2']['coverage']['n']] == [3, 3]
       and [h['P1']['fa']['n'], h['P2']['fa']['n']] == [3, 3],
       'P1 cov %s / P2 cov %s' % (SC.f(h['P1']['coverage']), SC.f(h['P2']['coverage'])))
    ck('scorer: targets on the point AND the interval',
       h['pooled']['coverage']['target']['point'] == 'MISSED'
       and h['pooled']['coverage']['target']['interval'] == 'MISSED'
       and h['pooled']['fa']['target']['point'] == 'MISSED',
       'cov %s; fa %s' % (SC.t(h['pooled']['coverage']), SC.t(h['pooled']['fa'])))
    s1 = out['S1_writer_intent']
    ck('S1 writer intent: the mislabelled item moves (5 C / 7 W by kind)',
       s1['n_moved'] == 1 and s1['pooled']['fa']['n'] == 7 and s1['pooled']['coverage']['n'] == 5
       and s1['pooled']['coverage']['k'] == 5 and s1['pooled']['fa']['k'] == 1,
       'moved %s' % s1['moved_items'])
    s2 = out['S2_wrong_borderline_correct']
    ck('S2: judged-wrong borderline + top-up to n>=20 (toy set: all 6 wrong move)',
       s2['n_moved'] == 6 and s2['pooled']['coverage']['n'] == 12
       and s2['pooled']['coverage']['k'] == 6, 'moved %d' % s2['n_moved'])
    s3 = out['S3_correct_borderline_wrong']
    ck('S3 mirror: judged-correct borderline + top-up (toy set: all 6 correct move)',
       s3['n_moved'] == 6 and s3['pooled']['fa']['n'] == 12, 'moved %d' % s3['n_moved'])
    s4 = out['S4_exclude_S2_S3']
    ck('S4: the S2 and S3 sets excluded from the denominator',
       s4['n_moved'] == 12 and s4['n_rows'] == 0, 'excluded %d, left %d' % (s4['n_moved'],
                                                                           s4['n_rows']))
    s5 = out['S5_article_pre_ruling']
    ck('S5: missing-article judged wrong scored correct',
       s5['n_moved'] == 1 and s5['pooled']['fa']['n'] == 5
       and s5['pooled']['coverage']['n'] == 7 and s5['pooled']['coverage']['k'] == 6,
       'moved %s' % s5['moved_items'])
    s6 = out['S6_leave_out_A1']
    ck('S6: leave-one-level-out x4 (A1 dropped)',
       s6['n_rows'] == 9 and s6['n_moved'] == 3
       and all('S6_leave_out_%s' % x in out for x in ('A1', 'A2', 'B1', 'B2')),
       'left %d rows' % s6['n_rows'])
    ck('no pre-declared sensitivity is empty', not empty, empty)
    c = out['cells']
    ck('cells: missing-article FA 1/1, agent-drop split, by-passive / SKP / time-frame',
       [c['missing_article']['fa']['k'], c['missing_article']['fa']['n']] == [1, 1]
       and c['agent_drop_fa']['all']['n'] == 4 and c['agent_drop_fa']['main']['n'] == 1
       and c['agent_drop_fa']['fronted']['n'] == 1
       and c['agent_drop_fa']['misaligned']['n'] == 1 and c['agent_drop_fa']['other']['n'] == 1
       and c['by_passive_coverage']['n'] == 2 and c['skp_coverage']['n'] == 2
       and c['time_frame_fa']['n'] == 1,
       'article FA %s, drops %s' % (SC.f(c['missing_article']['fa']),
                                    {k: v['n'] for k, v in c['agent_drop_fa'].items()}))
    ck('AG cost / catches and the four offline shadows',
       out['ag']['primary_v4']['fired'] == 3
       and out['ag']['primary_v4']['catches_judged_wrong'] == 3
       and out['ag']['primary_v4']['measured_cost_judged_correct'] == 0
       and set(out['ag']['shadows_offline']) == set(SC.SHADOWS))
    ck('layers: FA / false rejections / true rejections split by layer',
       out['detail']['false_accepts_by_layer'] == {'L3': 1}
       and out['detail']['false_rejections_by_layer'] == {'L3': 1}
       and out['detail']['true_rejections_by_layer'] == {'AG': 3, 'L3': 1, 'L2': 1},
       json.dumps(out['detail']['true_rejections_by_layer'], sort_keys=True))
    ck('spend is an upper bound at the published price',
       abs(out['model']['spend_usd_upper_bound']
           - round(1000 / 1e6 * 0.10 + 12 / 1e6 * 0.40, 4)) < 1e-9,
       out['model']['price_note'])
    order = [r['item_id'] for r in SC.topup(
        [{'item_id': 'x%d' % i, 'confidence': c, 'packet_position': p}
         for i, (c, p) in enumerate([(5, 1), (1, 9), (2, 3), (1, 2), (3, 4)])], 0, 4)]
    ck('S2/S3 top-up order: lowest confidence, ties by packet position',
       order == ['x3', 'x1', 'x2', 'x4'], order)
    return out


# ------------------------------------------------------------------ main
def main():
    root = os.path.join(HERE, 'selftest')
    os.makedirs(root, exist_ok=True)
    fixture = make_fixture(os.path.join(root, 'data'))
    prompt_test(fixture)
    floors_gate_test(root)
    cap_test(root)
    degenerate_test(root, fixture)
    run_tests(root, fixture)
    scorer_selftest()
    rep = {'mode': 'self-test - synthetic rows, stubbed model, 0 model calls, 0 network',
           'ts': datetime.datetime.now().isoformat(timespec='seconds'), 'checks': CHECKS,
           'passed': sum(1 for c in CHECKS if c['ok']), 'of': len(CHECKS)}
    safe_dump(rep, os.path.join(HERE, 'SELFTEST_1U.json'))
    print('[SELFTEST] %d/%d passed - SELFTEST_1U.json written, 0 model calls'
          % (rep['passed'], rep['of']))
    if rep['passed'] != rep['of']:
        raise SystemExit(1)
    return rep


if __name__ == '__main__':
    main()
