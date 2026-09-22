#!/usr/bin/env python3
"""Phase 2L runner.  Reuses 2K's transport and stack unchanged (byte copies in phase2l/: run_2k.py, run_2i_base.py,
stack_source.py, adapter_2f.py, write_guard.py, f4fix.py): Gemini key loading, call_one wrapper, counted = HTTP 200 only,
rate limit ONLY from status / error envelope, per-day/usage-limit envelope -> STOP, resume from the ledger at 0 cost.
Phase ledger phase2l/GEMINI_LEDGER.json {stage: counted}; phase hard cap 3,500 (K.PHASE_CAP overridden), spend $1.00.
  run_check  the Part B content check over {jid, src, answer, level} items -> replies.jsonl (one row per jid)
  run_full   SOURCE-ONLY stack (K.run_items, run_dir/l3) + content check on its accepted items (run_dir/cc)
Every path must be ABSOLUTE and (run dir / ledger) under phase2l/; anything else is REFUSED before anything is opened.
  PYTHONDONTWRITEBYTECODE=1 nohup python3 -B /abs/phase2l/run_2l.py check --items /abs/X.jsonl --run-dir /abs/phase2l/D --stage S --lang sk
"""
import argparse, json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import write_guard  # noqa: E402,F401  phase2l copy: every write outside phase2l/ is redirected
import run_2k as K  # noqa: E402
import content_check as CC  # noqa: E402
B, S = K.B, K.S
PHASE_CAP, PHASE_SPEND = 3500, 1.00
K.PHASE_CAP = PHASE_CAP
LEDGER = os.path.join(HERE, 'GEMINI_LEDGER.json')
Refused, Stop = K.Refused, K.Stop
assert K.LEDGER == LEDGER and os.path.dirname(os.path.abspath(S.__file__)) == HERE


def guard_path(p, what):
    if p is None:
        return
    K.must_abs(p, what)
    ap = os.path.normpath(p)
    if not (ap == HERE or ap.startswith(HERE + os.sep)):
        raise Refused('REFUSED: %s must lie under %s, got %r' % (what, HERE, p))


def run_check(items, run_dir, stage, lang, ledger_path=LEDGER, key=None, spend_dirs=(), stage_cap=None,
              expect_needed=None):
    for p, w in [(run_dir, '--run-dir'), (ledger_path, '--ledger')] + [(d, '--spend-dirs') for d in spend_dirs]:
        guard_path(p, w)
    if lang not in CC.LANG:
        raise Refused('REFUSED: --lang must be sk or cz')
    os.makedirs(run_dir, exist_ok=True)
    P = B.paths(run_dir)
    RP = os.path.join(run_dir, 'replies.jsonl')
    jids = [it['jid'] for it in items]
    if len(set(jids)) != len(jids):
        raise Refused('REFUSED: duplicate jid')
    done = {r['jid'] for r in B.jl_read(RP)}
    todo = [it for it in items if it['jid'] not in done]
    ledger = B.jl_read(P['ledger'])
    got = {}
    for row in ledger:
        if row.get('http') == 200 and row.get('req_key') and row['req_key'] not in got:
            got[row['req_key']] = row
    phase = K.read_json(ledger_path, {})
    others = sum(int(v) for k, v in phase.items() if k != stage)
    cap = PHASE_CAP - others
    if stage_cap is not None:
        cap = min(cap, int(stage_cap))
    spent_other = sum(K.spend_of(d) for d in spend_dirs if os.path.abspath(d) != os.path.abspath(run_dir))
    ctx = {'P': P, 'cap': cap, 'spend_cap': PHASE_SPEND - spent_other, 'key': None, 'last': 0.0, 'made': 0,
           'uncounted': 0, 'counted': sum(1 for r in ledger if r.get('http') == 200), 'spent': K.spend_of(run_dir),
           'est': B.EST_CALL_USD}

    def sync():
        phase[stage] = ctx['counted']
        K.write_json(ledger_path, phase)
    st = {'status': 'COMPLETE', 'stage': stage, 'lang': lang, 'check': 'content', 'items': len(items),
          'todo_items': len(todo), 'requests': 0, 'unique_requests': 0, 'needed': 0, 'calls_made': 0, 'stop': None,
          'phase_cap_for_stage': cap, 'other_stages_counted': others, 'mock': key == 'MOCK'}
    if todo:
        reqs = {it['jid']: CC.request(lang, it['src'], it['answer']) for it in todo}
        rq, users = {}, {}
        for j, q in sorted(reqs.items()):
            k = q['k'] = B.req_key(q)
            rq[k] = q
            users.setdefault(k, []).append('cc:%s' % j)
        need = [k for k in sorted(rq) if k not in got]
        st.update(requests=len(reqs), unique_requests=len(rq), needed=len(need))
        stop = None
        if expect_needed is not None and len(need) != int(expect_needed):
            stop = Stop('expect', 'needed %d != expected %d; NO call was made' % (len(need), int(expect_needed)))
        elif ctx['counted'] + len(need) > cap:
            stop = Stop('cap', 'counted %d + needed %d > cap for this stage %d (3,500 - other stages %d, stage cap %s); '
                        'NO call was made' % (ctx['counted'], len(need), cap, others, stage_cap))
        elif need:
            try:
                ctx['key'] = key or B.load_key()
                with CC.transport(B):
                    for k in need:
                        got[k] = B.call_one(ctx, k, rq[k], users[k])
                        sync()
            except Stop as e:
                stop = e
        sync()
        if stop:
            st.update(status='STOPPED', stop={'kind': stop.kind, 'why': stop.why})
            open(os.path.join(run_dir, 'STOP_%s.md' % stop.kind), 'w', encoding='utf-8').write(
                '# STOP (%s)\n\n%s\n\n%s. Counted calls %d, spend $%.6f. Resume with the same command.\n'
                % (stop.kind, stop.why, B.now(), ctx['counted'], ctx['spent']))
        for it in todo:
            q = reqs[it['jid']]
            row = got.get(q['k'])
            if row is None:
                continue
            v = None if row.get('failed') else row.get('verdict')
            B.jl_append(RP, {'jid': it['jid'], 'level': it.get('level'), 'req_key': q['k'], 'verdict': v,
                             'word': CC.word_of(v), 'failed': bool(row.get('failed')), 'raw': row.get('reply'),
                             'lang': lang, 'ts': B.now()})
    sync()
    rows = B.jl_read(RP)
    fin = {r['jid'] for r in rows}
    missing = sum(1 for j in jids if j not in fin)
    if missing and st['status'] == 'COMPLETE':
        st['status'] = 'INCOMPLETE'
    st.update(calls_made=ctx['made'], uncounted_attempts=ctx['uncounted'], counted_total=ctx['counted'],
              spend_usd=round(ctx['spent'], 6), results_missing=missing, ts=B.now(), phase_ledger=dict(phase),
              failed_items=sum(1 for r in rows if r.get('failed')),
              failed_calls=sum(1 for r in B.jl_read(P['ledger']) if r.get('http') == 200 and r.get('failed')))
    K.write_json(P['status'], st)
    return st


def run_full(items, run_dir, stage, lang, tip_accept, ledger_path=LEDGER, key=None, spend_dirs=()):
    guard_path(run_dir, '--run-dir'); guard_path(ledger_path, '--ledger')
    l3d, ccd = os.path.join(run_dir, 'l3'), os.path.join(run_dir, 'cc')
    st1 = K.run_items(items, l3d, stage + '_L3', lang, ledger_path=ledger_path, key=key, spend_dirs=list(spend_dirs))
    out = {'status': st1['status'], 'l3': st1, 'cc': None, 'tip_accept': bool(tip_accept)}
    if st1['status'] != 'COMPLETE':
        return out
    res = {r['jid']: r for r in B.jl_read(os.path.join(l3d, 'results.jsonl'))}
    clean = [K.clean_item(it, lang) for it in items]
    cand = [{'jid': c['jid'], 'src': c['src'], 'answer': c['answer'], 'level': c['level']} for c in clean
            if CC.l3_ok(res[c['jid']], tip_accept)]
    st2 = run_check(cand, ccd, stage + '_CC', lang, ledger_path, key, spend_dirs=list(spend_dirs) + [l3d])
    out.update(cc=st2, status=st2['status'])
    cc = {r['jid']: r for r in B.jl_read(os.path.join(ccd, 'replies.jsonl'))}
    fp = os.path.join(run_dir, 'final_%s.jsonl' % ('tipacc' if tip_accept else 'tiprej'))
    with open(fp, 'w', encoding='utf-8') as fh:
        for c in clean:
            r = res[c['jid']]
            a, layer, s = CC.decide(r, cc.get(c['jid']), tip_accept)
            x = cc.get(c['jid']) or {}
            fh.write(json.dumps({'jid': c['jid'], 'sid': c['sid'], 'level': c['level'], 'accept': a, 'layer': layer,
                                 'cc_state': s, 'cc_word': x.get('word'), 'l3_layer': r.get('layer'),
                                 'l3_reply': r.get('l3_reply'), 'tip_accept': bool(tip_accept)},
                                ensure_ascii=False, sort_keys=True) + '\n')
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    c = sp.add_parser('check')
    c.add_argument('--items', required=True); c.add_argument('--run-dir', required=True)
    c.add_argument('--stage', required=True); c.add_argument('--lang', required=True, choices=sorted(CC.LANG))
    c.add_argument('--ledger', default=LEDGER); c.add_argument('--stage-cap', type=int)
    c.add_argument('--expect-needed', type=int); c.add_argument('--spend-dirs', nargs='*', default=[])
    c.add_argument('--purpose', default='Phase 2L content check')
    a = ap.parse_args(argv)
    try:
        for p, w in ((a.items, '--items'), (a.run_dir, '--run-dir'), (a.ledger, '--ledger')):
            K.must_abs(p, w)
        guard_path(a.run_dir, '--run-dir'); guard_path(a.ledger, '--ledger')
        for d in a.spend_dirs:
            guard_path(d, '--spend-dirs')
        os.makedirs(a.run_dir, exist_ok=True)
        items = B.open_set(a.items, B.paths(a.run_dir), a.purpose)
        st = run_check(items, a.run_dir, a.stage, a.lang, a.ledger, None, a.spend_dirs, a.stage_cap, a.expect_needed)
        print(json.dumps(st, sort_keys=True))
        return 0 if st['status'] == 'COMPLETE' else 3
    except Refused as e:
        print(json.dumps({'status': 'REFUSED', 'why': str(e)}))
        return 2
    except Stop as e:
        print(json.dumps({'status': 'STOPPED', 'kind': e.kind, 'why': e.why}))
        return 4


if __name__ == '__main__':
    sys.exit(main())
