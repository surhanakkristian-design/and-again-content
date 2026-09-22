#!/usr/bin/env python3
"""Phase 2L S2 (Part D) suite for the CZECH stack over the REAL code path (stack_2l_cz.run -> run_2l.run_full ->
run_2k.run_items -> stack_source_cz (Czech reader assembled by cz_assemble) -> run_2i_base.call_one; content_check 'cz'),
only the HTTP function mocked. 0 model calls. T1-T10 = the Slovak test_2l.py ported to Czech; T11-T14 the Czech misreads
1T / 2J found; T15-T17 assembly, mirror and SOURCE-ONLY spec. Output test_2l_cz_output.txt."""
import contextlib, hashlib, io, json, os, re, shutil, sys, traceback
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); TOFF = os.path.dirname(HERE)
T = os.path.join(HERE, '_test_cz'); RES = []; INFO = {}
_RAW_OPEN = open


def _sha(p):
    try:
        with io.FileIO(p, 'r') as fh:
            return hashlib.sha256(fh.readall()).hexdigest()
    except Exception:
        return 'MISSING'


def sha_check():
    bad, n = [], 0
    for ln in _RAW_OPEN(os.path.join(HERE, 'SHA_before.txt'), encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln:
            continue
        h, p = ln.split('  ', 1); n += 1
        if _sha(os.path.join(TOFF, p)) != h:
            bad.append(p)
    return n, bad


def sha_frozen_c():
    bad = []
    for ln in _RAW_OPEN(os.path.join(HERE, 'FROZEN_SHA_C.txt'), encoding='utf-8'):
        if ln.startswith('#') or not ln.strip():
            continue
        h, p = ln.rstrip('\n').split('  ', 1)
        if _sha(os.path.join(HERE, p)) != h:
            bad.append(p)
    return bad


N0, BAD0 = sha_check(); FC0 = sha_frozen_c()
shutil.rmtree(T, ignore_errors=True); os.makedirs(T)
os.environ['P2I_RUN_DIR'] = T
sys.path.insert(0, HERE)
import stack_2l_cz as SZ  # noqa: E402
R = SZ.R; K, B, CC = R.K, R.B, R.CC; S = SZ.SCZ
import write_guard as WG  # noqa: E402
B.SLEEP[0] = lambda s: None
B.MIN_INTERVAL = 0
CALLS = []


def test(name):
    def deco(fn):
        try:
            fn(); RES.append((name, 'PASS', ''))
        except BaseException as e:
            RES.append((name, 'FAIL', '%r\n%s' % (e, traceback.format_exc()[-1800:])))
        return fn
    return deco


def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


ANN = jl(os.path.join(TOFF, 'phase2h', 'out', 'annotations_cz_final.jsonl'))


def mk(rows):
    out = []
    for i, r in enumerate(rows):
        w = r['en'].split()
        ans = r['en'] if i % 2 == 0 else ' '.join(w[:max(1, len(w) - 2)])
        out.append({'jid': 'CZ:%d:%s' % (r['exercise_id'], 'c' if i % 2 == 0 else 'w'), 'sid': r['exercise_id'],
                    'level': r['level'], 'czech': r['src'], 'answer': ans, 'annotation': r})
    return out


CZ = mk(ANN[::34][:120])
G1T = json.load(open(os.path.join(TOFF, 'phase1t', 'taskB', 'cz_validation.json'), encoding='utf-8'))
GROWS = [(r.get('n'), (r.get('cz') or {})) for r in G1T.get('rows', [])]
rd = lambda n: os.path.join(T, n)
led = lambda n: os.path.join(T, n, 'GEMINI_LEDGER.json')


def ok_js(text):
    return {'candidates': [{'content': {'parts': [{'text': text}]}, 'finishReason': 'STOP'}],
            'usageMetadata': {'promptTokenCount': 300, 'candidatesTokenCount': 3}}


def http(script=(), first_text=None):
    script = list(script); state = {'first': first_text}

    def f(url, body, key):
        CALLS.append(body)
        if script:
            code, js = script.pop(0)
            return code, js, json.dumps(js)
        sysw = body['systemInstruction']['parts'][0]['text']; u = body['contents'][0]['parts'][0]['text']
        if state['first'] is not None:
            text, state['first'] = state['first'], None
        elif sysw in (CC.sys_text('sk'), CC.sys_text('cz')):
            text = ('NONE', 'MISSING: houba', 'The answer drops nothing')[int(hashlib.md5(u.encode('utf-8')).hexdigest(), 16) % 3]
        else:
            text = ('SAME', 'TIP', 'DIFF')[len(u) % 3]
        return 200, ok_js(text), json.dumps(ok_js(text))
    return f


def cc_items(src):
    return [{'jid': x['jid'], 'src': x['czech'], 'answer': x['answer'], 'level': x['level']} for x in src]


def runc(its, name, **kw):
    os.makedirs(rd(name), exist_ok=True)
    return R.run_check(its, rd(name), name, 'cz', ledger_path=kw.pop('ledger', led(name)), key='MOCK', **kw)


@test('T1 content check (cz): item ids containing "429" are not a rate limit; a 200 reply "429" = counted FAILED call, never retried')
def t1():
    its = cc_items(CZ[:12]); its[0]['jid'] = 'A:4290:c1'; its[1]['jid'] = 'A:429:c2'
    B.HTTP[0] = http(first_text='429')
    st = runc(its, 't1')
    assert st['status'] == 'COMPLETE', st
    assert st['uncounted_attempts'] == 0 and st['counted_total'] == st['needed'] == st['unique_requests'] > 0, st
    L = jl(os.path.join(rd('t1'), 'ledger.jsonl'))
    assert all(r['http'] == 200 and r['try'] == 1 for r in L), L
    r429 = [r for r in L if r['reply'] == '429']
    assert len(r429) == 1 and r429[0]['failed'] and r429[0]['verdict'] == 'FAILED' and r429[0]['counted'], r429
    bad = [r for r in L if r['failed']]
    assert all(CC.parse(r['reply']) is None for r in bad) and all(CC.parse(r['reply']) for r in L if not r['failed'])
    rows = jl(os.path.join(rd('t1'), 'replies.jsonl'))
    assert {r['jid'] for r in rows} == {x['jid'] for x in its} and all(r['lang'] == 'cz' for r in rows)
    assert sum(1 for r in rows if r['failed']) == sum(len(r['users']) for r in bad) and st['failed_calls'] == len(bad)
    assert all(r['verdict'] is None and r['word'] is None for r in rows if r['failed'])
    assert json.load(open(led('t1')))['t1'] == st['counted_total']


@test('T1b full Czech stack: a row id containing "429" through stack_2l_cz.run is not a rate limit')
def t1b():
    its = [dict(x) for x in CZ[84:96]]; its[0]['jid'] = 'CZ:429:c'; its[1]['jid'] = 'CZ:14290:w'
    B.HTTP[0] = http()
    st = SZ.run(its, rd('t1b'), 't1b', ledger_path=led('t1b'), key='MOCK')
    assert st['status'] == 'COMPLETE' and st['l3']['uncounted_attempts'] == 0, st
    assert all(r['http'] == 200 for r in jl(os.path.join(rd('t1b'), 'l3', 'ledger.jsonl')))


@test('T2 real HTTP 429 envelope (per-minute RESOURCE_EXHAUSTED): detected, retried, not counted')
def t2():
    env = {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'Resource has been exhausted (e.g. check quota).',
                     'details': [{'violations': [{'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel', 'quotaMetric': 'generate_requests'}]}]}}
    B.HTTP[0] = http(script=[(429, env)])
    st = runc(cc_items(CZ[12:24]), 't2')
    assert st['status'] == 'COMPLETE' and st['uncounted_attempts'] == 1 and st['counted_total'] == st['needed'], st
    L = jl(os.path.join(rd('t2'), 'ledger.jsonl'))
    assert [r['http'] for r in L].count(429) == 1 and not [r for r in L if r['http'] == 429][0]['counted']


@test('T3 usage-limit / per-day quota envelope: hard STOP, 0 counted, STOP file (content check and full Czech stack)')
def t3():
    env = {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'Quota exceeded.',
                     'details': [{'violations': [{'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier'}]}]}}
    B.HTTP[0] = http(script=[(429, env)])
    st = runc(cc_items(CZ[24:36]), 't3')
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'quota' and st['counted_total'] == 0, st
    assert os.path.exists(os.path.join(rd('t3'), 'STOP_quota.md'))
    B.HTTP[0] = http(script=[(429, env)])
    st = SZ.run(CZ[96:108], rd('t3s'), 't3s', ledger_path=led('t3s'), key='MOCK')
    assert st['status'] != 'COMPLETE' and st['cc'] is None and st['l3']['counted_total'] == 0, st


@test('T4 resume at 0 cost (replies kept; replies deleted -> cached ledger replies reused; full Czech stack re-run)')
def t4():
    n0 = len(CALLS); B.HTTP[0] = http()
    its = cc_items(CZ[:12]); its[0]['jid'] = 'A:4290:c1'; its[1]['jid'] = 'A:429:c2'
    st = runc(its, 't1')
    assert st['calls_made'] == 0 and st['todo_items'] == 0 and st['status'] == 'COMPLETE', st
    before = {r['jid']: (r['verdict'], r['failed']) for r in jl(os.path.join(rd('t1'), 'replies.jsonl'))}
    os.rename(os.path.join(rd('t1'), 'replies.jsonl'), os.path.join(rd('t1'), 'replies_first.jsonl'))
    st = runc(its, 't1')
    assert st['calls_made'] == 0 and st['status'] == 'COMPLETE' and st['needed'] == 0, st
    after = {r['jid']: (r['verdict'], r['failed']) for r in jl(os.path.join(rd('t1'), 'replies.jsonl'))}
    assert after == before and len(CALLS) == n0
    its = [dict(x) for x in CZ[84:96]]; its[0]['jid'] = 'CZ:429:c'; its[1]['jid'] = 'CZ:14290:w'
    st = SZ.run(its, rd('t1b'), 't1b', ledger_path=led('t1b'), key='MOCK')
    assert st['status'] == 'COMPLETE' and len(CALLS) == n0, st


@test('T5 relative path REFUSED (CLI exit 2, run_check, run_full cz, stack_2l_cz.run), outside phase2l refused; write guard redirects')
def t5():
    items = os.path.join(TOFF, 'phase2i/set/items.jsonl')
    for argv in (['check', '--items', 'partB/items_b2.jsonl', '--run-dir', rd('t5'), '--stage', 'T5', '--lang', 'cz'],
                 ['check', '--items', items, '--run-dir', 'rel/dir', '--stage', 'T5', '--lang', 'cz'],
                 ['check', '--items', items, '--run-dir', rd('t5'), '--stage', 'T5', '--lang', 'cz', '--ledger', 'L.json'],
                 ['check', '--items', items, '--run-dir', os.path.join(TOFF, 'phase2k', 'x_t5'), '--stage', 'T5', '--lang', 'cz']):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = R.main(argv)
        assert rc == 2 and 'REFUSED' in buf.getvalue(), (rc, buf.getvalue())
    assert not os.path.exists(rd('t5')) and not os.path.exists('rel') and not os.path.exists(os.path.join(TOFF, 'phase2k', 'x_t5'))
    for fn in (lambda: R.run_check([], 'relative/run', 'T5', 'cz', key='MOCK'),
               lambda: R.run_full([], 'relative/run', 'T5', 'cz', False, key='MOCK'),
               lambda: SZ.run([], 'relative/run', 'T5', key='MOCK'),
               lambda: SZ.run([], rd('t5c'), 'T5', ledger_path='GEMINI_LEDGER.json', key='MOCK'),
               lambda: R.run_check([], rd('t5b'), 'T5', 'cz', ledger_path='GEMINI_LEDGER.json', key='MOCK')):
        try:
            fn(); raise AssertionError('not refused')
        except K.Refused:
            pass
    probe = os.path.join(TOFF, 'phase2k', '_t5_probe_cz.txt')
    with open(probe, 'w') as fh:
        fh.write('x')
    assert not os.path.exists(probe) and os.path.exists(WG._mapped(probe))


def poison(it):
    a = S.PoisonDict({k: (S.PoisonVal() if S.is_ref(k) else v) for k, v in it['annotation'].items()})
    d = {k: (S.PoisonVal() if S.is_ref(k) else v) for k, v in it.items() if k != 'annotation'}
    d['annotation'] = a
    return S.PoisonDict(d)


@test("T6 poison test on the CZECH stack + content check: v/alt/lk/en poison; no reference key/value read; bodies = Czech sentence + answer only; TIP accepted and the frozen TIP-rejected run; no AG/F4 error")
def t6():
    src_items = CZ[36:84]
    S.HITS.clear(); n0 = len(CALLS); B.HTTP[0] = http()
    st = R.run_full([poison(x) for x in src_items], rd('t6'), 't6', 'cz', True, ledger_path=led('t6'), key='MOCK')
    assert st['status'] == 'COMPLETE' and st['cc']['status'] == 'COMPLETE', st
    assert S.HITS == [], S.HITS[:3]
    bodies = CALLS[n0:]
    ccs, l3s = CC.sys_text('cz'), S.sys_text('cz')
    assert l3s == open(os.path.join(TOFF, 'phase2k', 'spec', 'l3_system_cz.txt'), encoding='utf-8').read().rstrip('\n')
    ccb = [b for b in bodies if b['systemInstruction']['parts'][0]['text'] == ccs]
    l3b = [b for b in bodies if b['systemInstruction']['parts'][0]['text'] == l3s]
    assert len(ccb) + len(l3b) == len(bodies)
    assert len(l3b) == st['l3']['needed'] > 0 and len(ccb) == st['cc']['needed'] > 0, (len(l3b), len(ccb), st)
    ok_cc = {CC.user_text('cz', x['czech'], x['answer']): x for x in src_items}
    ok_l3 = {S.user_text('cz', x['czech'], x['answer']): x for x in src_items}
    refs = [r for x in src_items for r in [x['annotation'].get('en')] + list(x['annotation'].get('v') or [])
            + [y for y in (x['annotation'].get('lk') or [])] if isinstance(r, str) and len(r) >= 15]
    assert refs
    for b, allowed, sysw, g in [(b, ok_cc, ccs, CC.GCFG) for b in ccb] + [(b, ok_l3, l3s, S.GCFG) for b in l3b]:
        assert set(b) == {'systemInstruction', 'contents', 'generationConfig'}, set(b)
        assert b['generationConfig'] == g
        u = b['contents'][0]['parts'][0]['text']
        assert u in allowed and u.startswith('Czech sentence: '), u
        rest = sysw + u.replace(allowed[u]['answer'], '')
        for r in refs:
            assert r not in rest, r
    n1 = len(CALLS)
    st2 = SZ.run([poison(x) for x in src_items], rd('t6'), 't6', ledger_path=led('t6'), key='MOCK')
    assert st2['status'] == 'COMPLETE' and len(CALLS) == n1 and S.HITS == [] and st2['tip_accept'] is False
    res = {r['jid']: r for r in jl(os.path.join(rd('t6'), 'l3', 'results.jsonl'))}
    assert all(r.get('ag_error') is None and r.get('f4_error') is None and not r.get('ag_ref_read') for r in res.values()), \
        [(j, r.get('ag_error'), r.get('f4_error')) for j, r in res.items() if r.get('ag_error') or r.get('f4_error')][:5]
    ccr = {r['jid']: r for r in jl(os.path.join(rd('t6'), 'cc', 'replies.jsonl'))}
    fa = {r['jid']: r for r in jl(os.path.join(rd('t6'), 'final_tipacc.jsonl'))}
    fr = {r['jid']: r for r in jl(os.path.join(rd('t6'), 'final_tiprej.jsonl'))}
    states = set()
    for j, r in res.items():
        c = ccr.get(j)
        if r['layer'] == 'L3:TIPrej':
            assert fr[j]['accept'] is False
        if CC.l3_ok(r, True):
            states.add('failed' if c['failed'] else c['verdict'][:7])
            assert fa[j]['accept'] == (c['failed'] or c['verdict'] == 'NONE'), (j, fa[j], c)
        else:
            assert fa[j]['accept'] is False and fr[j]['accept'] is False
    assert states == {'failed', 'NONE', 'MISSING'}, states
    lay = {}
    for r in res.values():
        lay[r['layer']] = lay.get(r['layer'], 0) + 1
    INFO['T6_layers_48_items'] = lay


@test('T7 strict parse: NONE / MISSING: <word> only (whitespace + one trailing period trimmed); failed call keeps the L3 verdict')
def t7():
    good = {'NONE': 'NONE', ' NONE \n': 'NONE', 'NONE.': 'NONE', 'MISSING: houba': 'MISSING: houba',
            'MISSING: v pokoji.': 'MISSING: v pokoji', ' MISSING: vzadu ': 'MISSING: vzadu', 'MISSING: příliš': 'MISSING: příliš'}
    for k, v in good.items():
        assert CC.parse(k) == v, (k, CC.parse(k))
    for k in ('None', 'none', 'NONE!', 'MISSING:', 'MISSING: ', 'MISSING:houba', 'MISSING: houba\nMISSING: dům', 'Answer: NONE',
              'NONE, nothing is missing', 'SAME', '', '429', '**NONE**', 'NONE..', 'missing: houba', None):
        assert CC.parse(k) is None, k
    same, tip, diff = {'accept': True, 'layer': 'L3'}, {'accept': False, 'layer': 'L3:TIPrej'}, {'accept': False, 'layer': 'L3'}
    f, n, m = {'failed': True, 'verdict': None}, {'failed': False, 'verdict': 'NONE'}, {'failed': False, 'verdict': 'MISSING: houba'}
    assert CC.decide(same, f, False)[0] is True and CC.decide(tip, f, True)[0] is True and CC.decide(tip, f, False)[0] is False
    assert CC.decide(same, m, False)[0] is False and CC.decide(same, n, False)[0] is True and CC.decide(diff, n, True)[0] is False
    assert CC.decide(tip, n, False)[0] is False and CC.decide(tip, n, True)[0] is True and CC.decide(same, None, True)[0] is None


@test('T8 phase hard cap 3,500 (and a stage cap): counted + needed > cap -> STOP before any call')
def t8():
    assert R.PHASE_CAP == 3500 and K.PHASE_CAP == 3500
    os.makedirs(rd('t8'), exist_ok=True)
    json.dump({'OTHER': 3499}, open(led('t8'), 'w'))
    n0 = len(CALLS); B.HTTP[0] = http()
    st = runc(cc_items(CZ[60:72]), 't8')
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'cap' and len(CALLS) == n0 and st['needed'] > 1, st
    st = runc(cc_items(CZ[60:72]), 't8b', stage_cap=3)
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'cap' and len(CALLS) == n0, st
    st = runc(cc_items(CZ[60:72]), 't8c', expect_needed=999)
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'expect' and len(CALLS) == n0, st


@test("T9 content-check prompt: the brief's question, reply format and ruling lists verbatim, Czech names the Czech sentence; spec current")
def t9():
    b = open(os.path.join(HERE, 'BRIEF_2L.md'), encoding='utf-8').read()
    m = re.search(r'do NOT count \((now, .*?Podívej!)\)', b, re.S)
    lists = ' '.join(m.group(1).split())
    assert lists == CC.RULING_LISTS, (lists, CC.RULING_LISTS)
    s = CC.sys_text('cz')
    assert s.count(lists) == 1 and 'time adverbs, degree adverbs and interjections do NOT count' in s
    assert 'NOUN, ADJECTIVE, MAIN VERB or PLACE/DIRECTION PHRASE' in s and 'missing from the answer, or its meaning changed' in s
    assert 'A synonym or paraphrase that carries the same meaning is NOT missing.' in s
    assert 'exactly NONE, or exactly MISSING: <source word>' in s and 'Czech sentence' in s and 'Slovak sentence' not in s
    assert CC.user_text('cz', 'Věta.', 'x').startswith('Czech sentence: Věta.')
    assert CC.request('cz', 'a', 'b')['gcfg'] == {'temperature': 0, 'maxOutputTokens': 48, 'thinkingConfig': {'thinkingBudget': 0}}
    assert CC.MODEL == B.MODEL == 'gemini-3.1-flash-lite'
    assert open(os.path.join(HERE, 'spec', 'content_check_prompt.txt'), encoding='utf-8').read() == CC.spec_text()


@test('T10 earlier phases byte-identical (every file in SHA_before.txt, before and after the suite)')
def t10():
    n, bad = sha_check()
    assert n > 4000 and BAD0 == [] and bad == [], (n, BAD0[:5], bad[:5])


ST = S.load('cz'); X = ST['CZ']; SF = ST['fx']['sk_features']; SKCK = sys.modules['checker_1i']
EMS = lambda srcs: [s for s in srcs if isinstance(s, str) and re.search(r'-m \S*em\b', s)]


@test('T11 Czech misread -em read as 1sg (1T gold): the assembled Czech readers (F4v2 fixed + CK) never read an -em word as 1sg; Slovak CK does')
def t11():
    gold = [(n, c['text']) for n, c in GROWS if EMS(((c.get('g2') or {}).get('signals')) or [])]
    cases = gold + [(None, 'Ředitelem školy je pan Novák.'), (None, 'Hercem roku se stal Petr.'), (None, 'Rozhovor s ředitelem byl dlouhý.')]
    for n, t in cases:
        assert EMS(SF(t)[1]) == [] and EMS(X['CK'].sk_features(t)[1]) == [], (n, t, SF(t))
    sk_mis = [(n, t) for n, t in cases if EMS(SKCK.sk_features(t)[1])]
    assert sk_mis, 'no Slovak -em misread reproduced'
    hit, _ = ST['f4v2']({'sk': 'Ředitelem školy je pan Novák.', 'answer': 'The headmaster of the school is Mr Novák.'})
    assert not hit
    INFO['T11_em'] = {'gold_cases_1T': gold, 'slovak_reader_misreads': len(sk_mis), 'cases': len(cases)}


SE = re.compile(r'(^|\s)se(\s|[.,!?]|$)', re.I); SASI = re.compile(r'(^|\s)(sa|si)(\s|[.,!?]|$)', re.I)


@test('T12 Czech misread missing `se` (1T gold reflex_se_missed): the AG chain (agent_drop_v4 / reader_nom) reads the Czech V2/V3 and sees `se`; the Slovak V2 does not')
def t12():
    AG4, RN = sys.modules['agent_drop_v4'], sys.modules['reader_nom']
    assert AG4.V2 is X['V2'] and AG4.V3 is X['V3'] and RN.V3 is X['V3'] and X['V3'].V2 is X['V2']
    probe = [x[0] for x in ((G1T.get('summary') or {}).get('probes', {}).get('reflex_se_missed', {}).get('cz') or [])]
    gold = [(n, c['text']) for n, c in GROWS if SE.search(c.get('text') or '') and not SASI.search(c.get('text') or '')]
    cases = gold + [(None, 'Dveře se otevřely.')]
    for n, t in cases:
        assert sys.modules['agent_drop_v2'].SK_REFLEX.search(t) is None, t
        assert AG4.V2.SK_REFLEX.search(t) and RN.V3.V2.SK_REFLEX.search(t), t
    assert set(probe) <= {n for n, _ in gold} or not probe, (probe, [n for n, _ in gold])
    INFO['T12_se'] = {'gold_cases_1T': len(gold), 'probe_rows_1T': probe}


LI = {'jestli', 'jestliže', 'zdali', 'zdalipak'}


def li_idx(tt):
    return [i for i, w in enumerate(tt) if str(w).lower().strip('.,!?;:') in LI]


@test('T13 Czech misread `jestli` read as an l-participle (1T gold): the Czech f9 never reads jestli/jestliže/zdali as a participle; the Slovak f9 does')
def t13():
    F9C, F9S = X['f9'], sys.modules['f9']
    assert F9C is not F9S and LI <= F9C.L_NONVERB and LI <= F9C.SUB_MARK
    gold = [(n, c['text']) for n, c in GROWS if li_idx(F9C.tok(c.get('text') or ''))]
    cases = gold + [(None, 'Nevím, jestli přijde.'), (None, 'Zeptal se, jestli to stihneme.'), (None, 'Nevěděla, zdali to zvládne.')]
    sk_mis = 0
    for n, t in cases:
        tc = F9C.tok(t)
        assert li_idx(tc), t
        for i in li_idx(tc):
            assert not F9C._is_l_part(tc, i), (n, t)
        ts = F9S.tok(t)
        sk_mis += sum(1 for i in li_idx(ts) if F9S._is_l_part(ts, i))
    assert sk_mis >= 1, 'no Slovak jestli misread reproduced'
    INFO['T13_jestli'] = {'gold_cases_1T': gold, 'slovak_f9_misreads': sk_mis}


@test('T14 Czech misread `příliš` read as 2sg (2J cause b): the fixed Czech F4v2/F4v3 reader never reads příliš as a verb; the unfixed CK does')
def t14():
    gold = [(n, c['text']) for n, c in GROWS if 'příliš' in (c.get('text') or '').lower()]
    prod = [(a['exercise_id'], a['src']) for a in ANN if 'příliš' in a['src'].lower()][:8]
    cases = gold + prod + [(None, 'Je to příliš drahé.')]
    for n, t in cases:
        assert not any('příliš' in s.lower() for s in SF(t)[1]), (n, t, SF(t))
    sk_mis = [(n, t) for n, t in cases if any('příliš' in s.lower() for s in SKCK.sk_features(t)[1])]
    assert sk_mis
    for nm in ('f4v2', 'f4v3'):
        hit, _ = ST[nm]({'sk': 'Je to příliš drahé.', 'answer': 'It is too expensive.'})
        assert not hit, nm
    INFO['T14_prilis'] = {'gold_cases_1T': gold, 'production_cases': [n for n, _ in prod], 'unfixed_reader_misreads': len(sk_mis)}


@test('T15 assembly: the four 1V Track C fixes present; AG/F4v2/F4v3 bound to the Czech reader; no Slovak reader object left in the chain')
def t15():
    import cz_assemble as CZA
    assert CZA.FIXES == ('em', 'se', 'jestli', 'aspect') and all(CZA.VERIFY.get(k) for k in CZA.FIXES), CZA.VERIFY
    assert ST['f4v2'].__globals__['sk_features'] is SF and ST['C'] is X['CK'] and ST['lang'] == 'cz'
    assert 2 in ST['f4v2'].__globals__['_pp_shadow'](['při', 'velkém', 'stole'])          # PREP_CZ bound (lang cz)
    assert ST['f4v3'].__globals__['sk_features_v3'].__globals__['_SF_2J'] is SF
    assert 'stack_1w' in ST['ag_how'] and ST['ag_name'] == 'primary'
    assert CZA.residual() == [], CZA.residual()[:10]
    INFO['T15_rebound'] = {'count': len(CZA.REBOUND), 'sample': [list(map(str, r)) for r in CZA.REBOUND[:12]]}


@test('T16 mirror: stack_source_cz.py == stack_source.py + cz_assemble.SUBS only; same content_check / run_2l / TIP rejected; Slovak frozen files unchanged')
def t16():
    import cz_assemble as CZA
    src = open(os.path.join(HERE, 'stack_source.py'), encoding='utf-8').read()
    assert open(os.path.join(HERE, 'stack_source_cz.py'), encoding='utf-8').read() == CZA.expected_stack_source_cz(src)
    SSK = sys.modules['stack_source']
    for a in ('GCFG', 'RULING', 'SYS_TMPL', 'STRIP_KEYS', 'VERDICTS', 'LANG'):
        assert getattr(S, a) == getattr(SSK, a), a
    import stack_2l as SK2
    assert SZ.TIP_ACCEPT is SK2.TIP_ACCEPT is False and SK2.R is R
    assert os.path.dirname(os.path.abspath(CC.__file__)) == HERE and K.S is S
    assert FC0 == [] and sha_frozen_c() == []


@test('T17 Czech L3 spec is SOURCE-ONLY: phase2k/spec/l3_system_cz.txt + l3_user_cz.txt == the prompt sent; no reference / English sentence')
def t17():
    sysf = open(os.path.join(TOFF, 'phase2k', 'spec', 'l3_system_cz.txt'), encoding='utf-8').read()
    usr = open(os.path.join(TOFF, 'phase2k', 'spec', 'l3_user_cz.txt'), encoding='utf-8').read()
    assert sysf == open(os.path.join(HERE, 'spec', 'l3_system_cz.txt'), encoding='utf-8').read()
    assert sysf.rstrip('\n') == S.sys_text('cz') and usr.rstrip('\n') == S.user_text('cz', '<SOURCE SENTENCE>', '<ANSWER>')
    low = (sysf + usr).lower().replace('there is no reference translation', '')
    assert 'reference' not in low and 'english sentence' not in low and 'slovak sentence' not in low
    assert re.findall(r'<[A-Z ]+>', usr) == ['<SOURCE SENTENCE>', '<ANSWER>']
    q = S.prepare([{'jid': 'x', 'sid': CZ[0]['sid'], 'level': 'A1', 'src': 'Kočka spí.', 'answer': 'The cat sleeps.',
                    'ann': {k: v for k, v in CZ[0]['annotation'].items() if not S.is_ref(k)}}], 'cz')
    assert all(set(v) == {'sys', 'user', 'gcfg'} for v in q.values())


test('T10b earlier phases byte-identical, re-run after T11-T17; guards_c._C is the Czech CK after a full run')(
    lambda: (t10(), [None for _ in [0] if not (sys.modules['guards_c']._C is X['CK'])] == [] or (_ for _ in ()).throw(AssertionError('guards_c._C not Czech'))))
out = ['%s  %s%s' % (st, n, ('\n      ' + e.replace('\n', '\n      ')) if e else '') for n, st, e in RES]
out.append('RESULT %d/%d PASS; mocked calls %d; real model calls 0' % (sum(1 for r in RES if r[1] == 'PASS'), len(RES), len(CALLS)))
out.append('INFO ' + json.dumps(INFO, ensure_ascii=False, default=str))
open(os.path.join(HERE, 'test_2l_cz_output.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
sys.exit(0 if all(r[1] == 'PASS' for r in RES) else 1)
