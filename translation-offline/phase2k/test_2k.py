#!/usr/bin/env python3
"""Phase 2K S1 test suite: the REAL code path (run_2k.run_items -> stack_source guards/prepare/finish -> run_2i_base.call_one)
with only the HTTP function / headless spawn mocked. 0 model calls. Output: test_2k_output.txt; exit 0 iff all pass."""
import contextlib, io, json, os, re, shutil, subprocess, sys, traceback, types
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
T = os.path.join(HERE, '_test')
RES = []


def sha_tree():
    return subprocess.run(['zsh', os.path.join(HERE, 'sha_tree_2k.sh')], capture_output=True, text=True).stdout


SHA0 = sha_tree()
shutil.rmtree(T, ignore_errors=True); os.makedirs(T)
os.environ['P2I_RUN_DIR'] = T
sys.path.insert(0, HERE)
import run_2k as K
B, S = K.B, K.S
import build_upload as BU
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
            'usageMetadata': {'promptTokenCount': 300, 'candidatesTokenCount': 1}}


def http(script=(), first_text=None):
    script = list(script); state = {'first': first_text}

    def f(url, body, key):
        CALLS.append(body)
        if script:
            code, js = script.pop(0)
            return code, js, json.dumps(js)
        u = body['contents'][0]['parts'][0]['text']
        if state['first'] is not None:
            text, state['first'] = state['first'], None
        else:
            text = ('SAME', 'TIP', 'DIFF')[len(u) % 3]
        return 200, ok_js(text), json.dumps(ok_js(text))
    return f


def run(its, name, **kw):
    os.makedirs(rd(name), exist_ok=True)
    return K.run_items(its, rd(name), name, 'sk', ledger_path=kw.pop('ledger', led(name)), key='MOCK', **kw)


@test('T1 mocked end-to-end: jid containing "429" is not a rate limit; a 200 reply "429" = counted failure, never retried')
def t1():
    its = [dict(x) for x in I2[:12]]
    its[0]['jid'] = 'A:4290:c1'; its[1]['jid'] = 'A:429:c2'
    B.HTTP[0] = http(first_text='429')
    st = run(its, 't1')
    assert st['status'] == 'COMPLETE', st
    assert st['uncounted_attempts'] == 0 and st['counted_total'] == st['needed'] == st['unique_requests'] > 0, st
    L = jl(os.path.join(rd('t1'), 'ledger.jsonl'))
    assert all(r['http'] == 200 and r['try'] == 1 for r in L), L
    bad = [r for r in L if r['failed']]
    assert len(bad) == 1 and bad[0]['reply'] == '429', bad
    rows = {r['jid']: r for r in jl(os.path.join(rd('t1'), 'results.jsonl'))}
    assert set(rows) == {x['jid'] for x in its}
    assert sum(1 for r in rows.values() if r['layer'] == 'L3:failed') == 1
    assert json.load(open(led('t1')))['t1'] == st['counted_total']


@test('T2 real 429 envelope (per-minute RESOURCE_EXHAUSTED): retried, not counted')
def t2():
    env = {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'Resource has been exhausted (e.g. check quota).',
                     'details': [{'violations': [{'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel', 'quotaMetric': 'generate_requests'}]}]}}
    B.HTTP[0] = http(script=[(429, env)])
    st = run([dict(x) for x in I2[12:24]], 't2')
    assert st['status'] == 'COMPLETE' and st['uncounted_attempts'] == 1 and st['counted_total'] == st['needed'], st
    L = jl(os.path.join(rd('t2'), 'ledger.jsonl'))
    assert [r['http'] for r in L].count(429) == 1 and not [r for r in L if r['http'] == 429][0]['counted']


@test('T3 usage-limit envelope (per-day quota): hard STOP, 0 counted, STOP file')
def t3():
    env = {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'Quota exceeded.',
                     'details': [{'violations': [{'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier'}]}]}}
    B.HTTP[0] = http(script=[(429, env)])
    st = run([dict(x) for x in I2[24:36]], 't3')
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'quota' and st['counted_total'] == 0, st
    assert os.path.exists(os.path.join(rd('t3'), 'STOP_quota.md'))


@test('T4 resume at 0 cost (results kept; and results deleted -> replies reused from the ledger)')
def t4():
    n0 = len(CALLS)
    B.HTTP[0] = http()
    its = [dict(x) for x in I2[:12]]
    its[0]['jid'] = 'A:4290:c1'; its[1]['jid'] = 'A:429:c2'
    st = run(its, 't1')
    assert st['calls_made'] == 0 and st['todo_items'] == 0 and st['status'] == 'COMPLETE', st
    before = {r['jid']: (r['accept'], r['layer']) for r in jl(os.path.join(rd('t1'), 'results.jsonl'))}
    os.rename(os.path.join(rd('t1'), 'results.jsonl'), os.path.join(rd('t1'), 'results_first.jsonl'))
    st = run(its, 't1')
    assert st['calls_made'] == 0 and st['status'] == 'COMPLETE', st
    after = {r['jid']: (r['accept'], r['layer']) for r in jl(os.path.join(rd('t1'), 'results.jsonl'))}
    assert after == before and len(CALLS) == n0


@test('T5 relative paths refused cleanly (exit 2, no traceback, nothing opened)')
def t5():
    for argv in (['gemini', '--lang', 'sk', '--set', 'phase2i/set/items.jsonl', '--run-dir', rd('t5'), '--stage', 'T5'],
                 ['gemini', '--lang', 'sk', '--set', os.path.join(TOFF, 'phase2i/set/items.jsonl'), '--run-dir', 'rel/dir', '--stage', 'T5'],
                 ['claude', '--sid', 'x', '--prompt-file', 'p.txt', '--out-dir', rd('t5c')]):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = K.main(argv)
        assert rc == 2 and 'REFUSED' in buf.getvalue(), (rc, buf.getvalue())
    assert not os.path.exists(rd('t5')) and not os.path.exists('rel')
    try:
        K.run_items([], 'relative/run', 'T5', 'sk', key='MOCK'); raise AssertionError('not refused')
    except K.Refused:
        pass


def poison(it):
    a = S.PoisonDict({k: (S.PoisonVal() if S.is_ref(k) else v) for k, v in it['annotation'].items()})
    d = {k: (S.PoisonVal() if S.is_ref(k) else v) for k, v in it.items() if k != 'annotation'}
    d['annotation'] = a
    return S.PoisonDict(d)


@test('T6 SOURCE-ONLY: items whose v/alt/lk/en are poison objects; no reference value or key is read; L3 body = source + answer only')
def t6():
    src_items = [x for x in I2[36:60]] + [x for x in J2[:24]]
    S.HITS.clear(); n0 = len(CALLS)
    B.HTTP[0] = http()
    st = run([poison(x) for x in src_items], 't6')
    assert st['status'] == 'COMPLETE', st
    assert S.HITS == [], S.HITS[:3]
    bodies = CALLS[n0:]
    assert len(bodies) == st['needed'] > 0
    sysw = S.sys_text('sk')
    allowed = {S.user_text('sk', x['slovak'], x['answer']) for x in src_items}
    for b in bodies:
        assert set(b) == {'systemInstruction', 'contents', 'generationConfig'}, set(b)
        assert b['systemInstruction']['parts'][0]['text'] == sysw
        u = b['contents'][0]['parts'][0]['text']
        assert u in allowed, u
        assert b['generationConfig'] == S.GCFG
    for x in src_items:
        body_wo_answer = sysw + '\n'.join(u.replace(x['answer'], '') for u in allowed)
        for r in [x['annotation'].get('en')] + list(x['annotation'].get('v') or []):
            if r and r != x['answer']:
                assert r not in body_wo_answer, r
    assert 'Reference' not in sysw and 'reference' not in sysw.replace('There is no reference translation', '')


@test('T7 hard cap 3,000: counted + needed > cap -> STOP before any call')
def t7():
    os.makedirs(rd('t7'), exist_ok=True)
    json.dump({'OTHER': 2999}, open(led('t7'), 'w'))
    n0 = len(CALLS); B.HTTP[0] = http()
    st = run([dict(x) for x in I2[60:72]], 't7')
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'cap' and len(CALLS) == n0 and st['needed'] > 1, st


@test('T8 reference-ending test over BOTH files (SK final, CZ phase2i/upload): no reference ends in an article or a STRICT preposition')
def t8():
    hits = BU.scan_endings(BU.SK_FINAL, 'sk') + BU.scan_endings(BU.CZ_FILE, 'cz')
    strict = [h for h in hits if h['strict']]
    assert strict == [], ['%s %s %r' % (h['lang'], h['exercise_id'], h['ref']) for h in strict]


@test('T9 upload_sk_final: 4,064 rows, exercise_id int, v[0]==en, the 4 references restored to the pre-B3 value, README')
def t9():
    rows = jl(BU.SK_FINAL)
    assert len(rows) == 4064 and all(isinstance(r['exercise_id'], int) and r['v'][0] == r['en'] for r in rows)
    pre = {r['exercise_id']: r for r in jl(os.path.join(BU.P2I_UP, 'annotations_sk_fixed.jsonl'))}
    fin = {r['exercise_id']: r for r in rows}
    for x in json.load(open(os.path.join(BU.OUT, 'RESTORE_4.json'))):
        assert x['restored'] in pre[x['exercise_id']]['v'] and x['restored'] in fin[x['exercise_id']]['v']
        assert x['b3_value'] not in fin[x['exercise_id']]['v']
    import openpyxl
    ws = openpyxl.load_workbook(os.path.join(BU.OUT, 'upload_sk_final.xlsx'), read_only=True)['sk']
    xr = list(ws.iter_rows(values_only=True))
    assert len(xr) == 4065 and all(isinstance(r[0], int) for r in xr[1:])
    assert all(json.loads(r[5])['en'] == r[4] for r in xr[1:])
    rd_ = open(os.path.join(BU.OUT, 'UPLOAD_README.md'), encoding='utf-8').read()
    assert 'display-only' in rd_ and 'no longer grades' in rd_


@test('T10 the 1.1 ruling verbatim (from BRIEF_2K.md) in judge brief, writer spec and L3 prompt, SK and CZ')
def t10():
    b = open(os.path.join(HERE, 'BRIEF_2K.md'), encoding='utf-8').read()
    m = re.search(r'languages: (Dropping a word.*?counted as one\.)', b, re.S)
    ruling = ' '.join(m.group(1).split())
    assert ruling == S.RULING, (ruling, S.RULING)
    for lang in ('sk', 'cz'):
        for f in ('judge_prompt_%s.txt', 'writer_template_%s.txt', 'l3_system_%s.txt'):
            t = open(os.path.join(HERE, 'spec', f % lang), encoding='utf-8').read()
            assert t.count(ruling) == 1, f % lang
        assert S.sys_text(lang).count(ruling) == 1
    assert 'Czech' in S.sys_text('cz') and 'Slovak sentence' not in S.sys_text('cz').replace(ruling, '')


@test('T11 headless spawner: "429" in result/stderr is not a rate limit; 429 envelope retried; usage-limit envelope = hard STOP')
def t11():
    K.ENV[0] = {'X': '1'}; K.SLEEP_H[0] = lambda s: None
    seq = []

    def spawn(argv, timeout):
        return seq.pop(0)
    K.SPAWN[0] = spawn
    ok = types.SimpleNamespace(returncode=0, stdout=json.dumps({'type': 'result', 'subtype': 'success', 'is_error': False,
                               'result': 'status 429 inside text', 'usage': {'input_tokens': 10, 'output_tokens': 5}}), stderr='HTTP 429')
    seq[:] = [ok]
    d = K.run_session('a', 'p', rd('t11'), stop_dir=rd('t11'))
    assert d['status'] == 'ok' and d['spawns'] == 1 and d['tokens'] == 15
    rate = types.SimpleNamespace(returncode=1, stdout=json.dumps({'is_error': True, 'api_error_status': 429, 'result': 'x'}), stderr='')
    seq[:] = [rate, ok]
    d = K.run_session('b', 'p', rd('t11'), stop_dir=rd('t11'))
    assert d['spawns'] == 2
    use = types.SimpleNamespace(returncode=1, stdout=json.dumps({'is_error': True, 'result': "You've hit your limit - resets 5pm"}), stderr='')
    seq[:] = [use]
    try:
        K.run_session('c', 'p', rd('t11'), stop_dir=rd('t11')); raise AssertionError('no stop')
    except K.Stop as e:
        assert e.kind == 'usage_limit'
    assert os.path.exists(os.path.join(rd('t11'), 'STOP_usage_limit.md'))
    seq[:] = [ok]
    try:
        K.run_session('d', 'p', rd('t11'), stop_dir=rd('t11')); raise AssertionError('not refused')
    except K.Stop as e:
        assert e.kind == 'usage_limit' and len(seq) == 1


@test('T12 routing: every answer not rejected by a source-side guard reaches L3')
def t12():
    rows = jl(os.path.join(rd('t6'), 'results.jsonl'))
    st = json.load(open(os.path.join(rd('t6'), 'RUN_STATUS.json')))
    assert all(r['reached_l3'] == (r['guard_layer'] is None) for r in rows)
    assert st['requests'] == sum(1 for r in rows if r['guard_layer'] is None)
    assert set(r['layer'] for r in rows) <= {'AG', 'F4v2', 'F4v3', 'L3', 'L3:TIPrej', 'L3:failed'}


@test('T13 earlier phases byte-identical (sha tree before == after suite == SHA_before.txt)')
def t13():
    now = sha_tree()
    assert now == SHA0, 'suite changed an earlier phase'
    assert now == open(os.path.join(HERE, 'SHA_before.txt')).read(), 'differs from SHA_before.txt'


out = ['%s  %s%s' % (st, n, ('\n      ' + e.replace('\n', '\n      ')) if e else '') for n, st, e in RES]
out.append('RESULT %d/%d PASS; mocked calls %d; real model calls 0' % (sum(1 for r in RES if r[1] == 'PASS'), len(RES), len(CALLS)))
open(os.path.join(HERE, 'test_2k_output.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('\n'.join(out))
sys.exit(0 if all(r[1] == 'PASS' for r in RES) else 1)
