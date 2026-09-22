#!/usr/bin/env python3
"""Phase 2L S1 test suite over the REAL code path (run_2l.run_check / run_full -> run_2k.run_items -> stack_source ->
run_2i_base.call_one, content_check) with only the HTTP function mocked. 0 model calls. Output test_2l_output_S1.txt."""
import contextlib, hashlib, io, json, os, re, shutil, sys, traceback
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); TOFF = os.path.dirname(HERE)
T = os.path.join(HERE, '_test'); RES = []
_RAW_OPEN = open


def sha_check():
    bad, n = [], 0
    for ln in _RAW_OPEN(os.path.join(HERE, 'SHA_before.txt'), encoding='utf-8'):
        ln = ln.rstrip('\n')
        if not ln:
            continue
        h, p = ln.split('  ', 1); n += 1
        try:
            with io.FileIO(os.path.join(TOFF, p), 'r') as fh:
                hh = hashlib.sha256(fh.readall()).hexdigest()
        except Exception:
            hh = 'MISSING'
        if hh != h:
            bad.append(p)
    return n, bad


N0, BAD0 = sha_check()
shutil.rmtree(T, ignore_errors=True); os.makedirs(T)
os.environ['P2I_RUN_DIR'] = T
sys.path.insert(0, HERE)
import run_2l as R  # noqa: E402
K, B, S, CC = R.K, R.B, R.S, R.CC
import write_guard as WG  # noqa: E402
B.SLEEP[0] = lambda s: None
B.MIN_INTERVAL = 0
CALLS = []


def test(name):
    def deco(fn):
        try:
            fn(); RES.append((name, 'PASS', ''))
        except BaseException as e:
            RES.append((name, 'FAIL', '%r\n%s' % (e, traceback.format_exc()[-1500:])))
        return fn
    return deco


def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


I2 = jl(os.path.join(TOFF, 'phase2i', 'set', 'items.jsonl'))
J2 = jl(os.path.join(TOFF, 'phase2j', 'partD', 'set', 'items.jsonl'))
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
            text = ('NONE', 'MISSING: huba', 'The answer drops nothing')[int(hashlib.md5(u.encode('utf-8')).hexdigest(), 16) % 3]
        else:
            text = ('SAME', 'TIP', 'DIFF')[len(u) % 3]
        return 200, ok_js(text), json.dumps(ok_js(text))
    return f


def cc_items(src):
    return [{'jid': x['jid'], 'src': x['slovak'], 'answer': x['answer'], 'level': x['level']} for x in src]


def runc(its, name, **kw):
    os.makedirs(rd(name), exist_ok=True)
    return R.run_check(its, rd(name), name, 'sk', ledger_path=kw.pop('ledger', led(name)), key='MOCK', **kw)


@test('T1 content check: item ids containing "429" are not a rate limit; a 200 reply "429" = counted FAILED call, never retried')
def t1():
    its = cc_items(I2[:12]); its[0]['jid'] = 'A:4290:c1'; its[1]['jid'] = 'A:429:c2'
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
    assert {r['jid'] for r in rows} == {x['jid'] for x in its}
    assert sum(1 for r in rows if r['failed']) == sum(len(r['users']) for r in bad) and st['failed_calls'] == len(bad)
    assert all(r['verdict'] is None and r['word'] is None for r in rows if r['failed'])
    assert json.load(open(led('t1')))['t1'] == st['counted_total']


@test('T2 real HTTP 429 envelope (per-minute RESOURCE_EXHAUSTED): detected, retried, not counted')
def t2():
    env = {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'Resource has been exhausted (e.g. check quota).',
                     'details': [{'violations': [{'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel', 'quotaMetric': 'generate_requests'}]}]}}
    B.HTTP[0] = http(script=[(429, env)])
    st = runc(cc_items(I2[12:24]), 't2')
    assert st['status'] == 'COMPLETE' and st['uncounted_attempts'] == 1 and st['counted_total'] == st['needed'], st
    L = jl(os.path.join(rd('t2'), 'ledger.jsonl'))
    assert [r['http'] for r in L].count(429) == 1 and not [r for r in L if r['http'] == 429][0]['counted']


@test('T3 usage-limit / per-day quota envelope: hard STOP, 0 counted, STOP file')
def t3():
    env = {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'Quota exceeded.',
                     'details': [{'violations': [{'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier'}]}]}}
    B.HTTP[0] = http(script=[(429, env)])
    st = runc(cc_items(I2[24:36]), 't3')
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'quota' and st['counted_total'] == 0, st
    assert os.path.exists(os.path.join(rd('t3'), 'STOP_quota.md'))


@test('T4 resume at 0 cost (replies kept; and replies deleted -> cached ledger replies reused, zero new calls)')
def t4():
    n0 = len(CALLS); B.HTTP[0] = http()
    its = cc_items(I2[:12]); its[0]['jid'] = 'A:4290:c1'; its[1]['jid'] = 'A:429:c2'
    st = runc(its, 't1')
    assert st['calls_made'] == 0 and st['todo_items'] == 0 and st['status'] == 'COMPLETE', st
    before = {r['jid']: (r['verdict'], r['failed']) for r in jl(os.path.join(rd('t1'), 'replies.jsonl'))}
    os.rename(os.path.join(rd('t1'), 'replies.jsonl'), os.path.join(rd('t1'), 'replies_first.jsonl'))
    st = runc(its, 't1')
    assert st['calls_made'] == 0 and st['status'] == 'COMPLETE' and st['needed'] == 0, st
    after = {r['jid']: (r['verdict'], r['failed']) for r in jl(os.path.join(rd('t1'), 'replies.jsonl'))}
    assert after == before and len(CALLS) == n0


@test('T5 relative path REFUSED (CLI exit 2, run_check, run_full), path outside phase2l refused; write guard redirects a write outside phase2l')
def t5():
    items = os.path.join(TOFF, 'phase2i/set/items.jsonl')
    for argv in (['check', '--items', 'partB/items_b2.jsonl', '--run-dir', rd('t5'), '--stage', 'T5', '--lang', 'sk'],
                 ['check', '--items', items, '--run-dir', 'rel/dir', '--stage', 'T5', '--lang', 'sk'],
                 ['check', '--items', items, '--run-dir', rd('t5'), '--stage', 'T5', '--lang', 'sk', '--ledger', 'L.json'],
                 ['check', '--items', items, '--run-dir', os.path.join(TOFF, 'phase2k', 'x_t5'), '--stage', 'T5', '--lang', 'sk']):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = R.main(argv)
        assert rc == 2 and 'REFUSED' in buf.getvalue(), (rc, buf.getvalue())
    assert not os.path.exists(rd('t5')) and not os.path.exists('rel') and not os.path.exists(os.path.join(TOFF, 'phase2k', 'x_t5'))
    for fn in (lambda: R.run_check([], 'relative/run', 'T5', 'sk', key='MOCK'),
               lambda: R.run_full([], 'relative/run', 'T5', 'sk', True, key='MOCK'),
               lambda: R.run_check([], rd('t5b'), 'T5', 'sk', ledger_path='GEMINI_LEDGER.json', key='MOCK')):
        try:
            fn(); raise AssertionError('not refused')
        except K.Refused:
            pass
    probe = os.path.join(TOFF, 'phase2k', '_t5_probe.txt')
    with open(probe, 'w') as fh:
        fh.write('x')
    assert not os.path.exists(probe) and os.path.exists(WG._mapped(probe))


def poison(it):
    a = S.PoisonDict({k: (S.PoisonVal() if S.is_ref(k) else v) for k, v in it['annotation'].items()})
    d = {k: (S.PoisonVal() if S.is_ref(k) else v) for k, v in it.items() if k != 'annotation'}
    d['annotation'] = a
    return S.PoisonDict(d)


@test("T6 2K poison test extended to content_check: v/alt/lk/en are poison; no reference key/value read by the stack OR the check; bodies = source + answer only; both TIP variants")
def t6():
    src_items = [x for x in I2[36:60]] + [x for x in J2[:24]]
    S.HITS.clear(); n0 = len(CALLS); B.HTTP[0] = http()
    st = R.run_full([poison(x) for x in src_items], rd('t6'), 't6', 'sk', True, ledger_path=led('t6'), key='MOCK')
    assert st['status'] == 'COMPLETE' and st['cc']['status'] == 'COMPLETE', st
    assert S.HITS == [], S.HITS[:3]
    bodies = CALLS[n0:]
    ccs, l3s = CC.sys_text('sk'), S.sys_text('sk')
    ccb = [b for b in bodies if b['systemInstruction']['parts'][0]['text'] == ccs]
    l3b = [b for b in bodies if b['systemInstruction']['parts'][0]['text'] == l3s]
    assert len(ccb) + len(l3b) == len(bodies)
    assert len(l3b) == st['l3']['needed'] > 0 and len(ccb) == st['cc']['needed'] > 0, (len(l3b), len(ccb), st)
    ok_cc = {CC.user_text('sk', x['slovak'], x['answer']): x for x in src_items}
    ok_l3 = {S.user_text('sk', x['slovak'], x['answer']): x for x in src_items}
    refs = [r for x in src_items for r in [x['annotation'].get('en')] + list(x['annotation'].get('v') or []) + list(x['annotation'].get('alt') or [])
            if isinstance(r, str) and len(r) >= 15]
    assert refs
    for b, allowed, sysw, g in [(b, ok_cc, ccs, CC.GCFG) for b in ccb] + [(b, ok_l3, l3s, S.GCFG) for b in l3b]:
        assert set(b) == {'systemInstruction', 'contents', 'generationConfig'}, set(b)
        assert b['generationConfig'] == g
        u = b['contents'][0]['parts'][0]['text']
        assert u in allowed, u
        rest = sysw + u.replace(allowed[u]['answer'], '')
        for r in refs:
            assert r not in rest, r
    assert 'reference' not in ccs.replace('There is no reference translation', '').lower()
    n1 = len(CALLS)
    st2 = R.run_full([poison(x) for x in src_items], rd('t6'), 't6', 'sk', False, ledger_path=led('t6'), key='MOCK')
    assert st2['status'] == 'COMPLETE' and len(CALLS) == n1 and S.HITS == []
    res = {r['jid']: r for r in jl(os.path.join(rd('t6'), 'l3', 'results.jsonl'))}
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


@test('T7 strict parse: NONE / MISSING: <word> only (whitespace + one trailing period trimmed); failed call keeps the L3 verdict')
def t7():
    good = {'NONE': 'NONE', ' NONE \n': 'NONE', 'NONE.': 'NONE', 'MISSING: huba': 'MISSING: huba',
            'MISSING: v izbe.': 'MISSING: v izbe', ' MISSING: vzadu ': 'MISSING: vzadu'}
    for k, v in good.items():
        assert CC.parse(k) == v, (k, CC.parse(k))
    for k in ('None', 'none', 'NONE!', 'MISSING:', 'MISSING: ', 'MISSING:huba', 'MISSING: huba\nMISSING: dom', 'Answer: NONE',
              'NONE, nothing is missing', 'SAME', '', '429', '**NONE**', 'NONE..', 'missing: huba', None):
        assert CC.parse(k) is None, k
    same, tip, diff = {'accept': True, 'layer': 'L3'}, {'accept': False, 'layer': 'L3:TIPrej'}, {'accept': False, 'layer': 'L3'}
    f, n, m = {'failed': True, 'verdict': None}, {'failed': False, 'verdict': 'NONE'}, {'failed': False, 'verdict': 'MISSING: huba'}
    assert CC.decide(same, f, False)[0] is True and CC.decide(tip, f, True)[0] is True and CC.decide(tip, f, False)[0] is False
    assert CC.decide(same, m, False)[0] is False and CC.decide(same, n, False)[0] is True and CC.decide(diff, n, True)[0] is False
    assert CC.decide(tip, n, False)[0] is False and CC.decide(tip, n, True)[0] is True and CC.decide(same, None, True)[0] is None


@test('T8 phase hard cap 3,500 (and a stage cap): counted + needed > cap -> STOP before any call')
def t8():
    assert R.PHASE_CAP == 3500 and K.PHASE_CAP == 3500
    os.makedirs(rd('t8'), exist_ok=True)
    json.dump({'OTHER': 3499}, open(led('t8'), 'w'))
    n0 = len(CALLS); B.HTTP[0] = http()
    st = runc(cc_items(I2[60:72]), 't8')
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'cap' and len(CALLS) == n0 and st['needed'] > 1, st
    st = runc(cc_items(I2[60:72]), 't8b', stage_cap=3)
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'cap' and len(CALLS) == n0, st
    st = runc(cc_items(I2[60:72]), 't8c', expect_needed=999)
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'expect' and len(CALLS) == n0, st


@test("T9 prompt: the brief's question, reply format and the owner's ruling word lists verbatim (BRIEF_2L.md), SK and CZ; spec file current")
def t9():
    b = open(os.path.join(HERE, 'BRIEF_2L.md'), encoding='utf-8').read()
    m = re.search(r'do NOT count \((now, .*?Podívej!)\)', b, re.S)
    lists = ' '.join(m.group(1).split())
    assert lists == CC.RULING_LISTS, (lists, CC.RULING_LISTS)
    for lang, name in (('sk', 'Slovak'), ('cz', 'Czech')):
        s = CC.sys_text(lang)
        assert s.count(lists) == 1 and 'time adverbs, degree adverbs and interjections do NOT count' in s
        assert 'NOUN, ADJECTIVE, MAIN VERB or PLACE/DIRECTION PHRASE' in s and 'missing from the answer, or its meaning changed' in s
        assert 'A synonym or paraphrase that carries the same meaning is NOT missing.' in s
        assert 'exactly NONE, or exactly MISSING: <source word>' in s and name + ' sentence' in s
        other = 'Czech' if lang == 'sk' else 'Slovak'
        assert (other + ' sentence') not in s
    assert CC.request('sk', 'a', 'b')['gcfg'] == {'temperature': 0, 'maxOutputTokens': 48, 'thinkingConfig': {'thinkingBudget': 0}}
    assert CC.MODEL == B.MODEL == 'gemini-3.1-flash-lite'
    assert open(os.path.join(HERE, 'spec', 'content_check_prompt.txt'), encoding='utf-8').read() == CC.spec_text()


@test('T10 earlier phases byte-identical (every file in SHA_before.txt, before and after the suite)')
def t10():
    n, bad = sha_check()
    assert n > 4000 and BAD0 == [] and bad == [], (n, BAD0[:5], bad[:5])


out = ['%s  %s%s' % (st, n, ('\n      ' + e.replace('\n', '\n      ')) if e else '') for n, st, e in RES]
out.append('RESULT %d/%d PASS; mocked calls %d; real model calls 0' % (sum(1 for r in RES if r[1] == 'PASS'), len(RES), len(CALLS)))
open(os.path.join(HERE, 'test_2l_output_S1.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
sys.exit(0 if all(r[1] == 'PASS' for r in RES) else 1)
