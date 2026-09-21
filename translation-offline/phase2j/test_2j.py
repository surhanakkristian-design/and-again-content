#!/usr/bin/env python3
"""Phase 2J S2 test suite - real code path (stack_tonly subprocesses, run_2j transport), model MOCKED.
  python3 -B /abs/phase2j/test_2j.py   (writes only under phase2j/_test_tmp, removed at the end)"""
import collections, json, os, shutil, subprocess, sys, traceback
sys.dont_write_bytecode = True
P2J = os.path.dirname(os.path.abspath(__file__)); TOFF = os.path.dirname(P2J); P2I = TOFF + '/phase2i'
sys.path.insert(0, P2J)
import run_2j as R                                                              # noqa: E402
B = R.B
TMP = P2J + '/_test_tmp'
shutil.rmtree(TMP, ignore_errors=True); os.makedirs(TMP)
B.SLEEP[0] = lambda s: None; B.MIN_INTERVAL = 0; R.SLEEP_H[0] = lambda s: None
RES = []
ITEMS = [json.loads(l) for l in open(P2I + '/set/items.jsonl', encoding='utf-8')]
NEW44 = json.load(open(P2J + '/partA/NEW_L3_CALLS_S2.json'))['jids']


def t(name):
    def deco(fn):
        try:
            fn(); RES.append((name, 'PASS', ''))
        except BaseException as e:                                              # noqa
            RES.append((name, 'FAIL', '%r %s' % (e, traceback.format_exc()[-600:])))
        return fn
    return deco


def sid_items(*sids):
    return [dict(i) for i in ITEMS if i['sid'] in sids]


def write_set(path, items):
    with open(path, 'w', encoding='utf-8') as fh:
        for i in items:
            fh.write(json.dumps(i, ensure_ascii=False) + '\n')
    return path


def ok_js(text='SAME'):
    js = {'candidates': [{'content': {'parts': [{'text': text}]}, 'finishReason': 'STOP'}], 'modelVersion': 'mock-429',
          'usageMetadata': {'promptTokenCount': 120, 'candidatesTokenCount': 1}}
    return 200, js, json.dumps(js)


E429 = (429, {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'Resource has been exhausted (e.g. check quota).'}}, '{}')
EDAY = (429, {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'You exceeded your current quota.',
                        'details': [{'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [
                            {'quotaMetric': 'generativelanguage.googleapis.com/generate_requests_per_model_per_day',
                             'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier'}]}]}}, '{}')
CALLS = []


def utext(body):
    return body['contents'][0]['parts'][0]['text']


A_DIR, A_LED = TMP + '/run_a', TMP + '/led_a.json'
A_SET = None


@t('T1 item/row number containing "429" is NOT a rate limit + T2 real 429 envelope is retried')
def _():
    global A_SET
    its = sid_items(1214)
    x = dict(its[0], jid='A:429:c9', sid=429, answer='He said the 429 km ride was the hardest of his life!')
    A_SET = write_set(TMP + '/set_a.jsonl', its + [x])
    state = {'did': False}

    def http(url, body, key):
        u = utext(body); CALLS.append(u)
        if '429' not in u and not state['did']:
            state['did'] = True
            return E429
        return ok_js()
    B.HTTP[0] = http
    st = R.run_gemini(A_SET, A_DIR, 'T', ledger_path=A_LED, key='MOCK')
    assert st['status'] == 'COMPLETE', st
    assert st['uncounted_attempts'] == 1 and st['counted_total'] == st['needed'] >= 2, st
    led = B.jl_read(A_DIR + '/ledger.jsonl')
    rows429 = [r for r in led if r.get('http') == 429]
    assert len(rows429) == 1 and rows429[0]['counted'] is False and rows429[0]['kind'] == 'retry', rows429
    retried = [r for r in led if r['req_key'] == rows429[0]['req_key']]
    assert [r['http'] for r in retried] == [429, 200], retried
    res = {r['jid']: r for r in B.jl_read(A_DIR + '/results.jsonl')}
    assert 'A:429:c9' in res and len(res) == len(its) + 1, sorted(res)
    k429 = [q for q in CALLS if '429 km' in q]
    assert len(k429) <= 1, 'the "429" text request must never be retried'
    assert json.load(open(A_LED)) == {'T': st['counted_total']}


@t('T3 resume at 0 cost (same command, finished items skipped, stored replies reused)')
def _():
    n0 = len(CALLS)
    B.HTTP[0] = lambda *a: (_ for _ in ()).throw(AssertionError('HTTP called on resume'))
    st = R.run_gemini(A_SET, A_DIR, 'T', ledger_path=A_LED, key='MOCK')
    assert st['status'] == 'COMPLETE' and st['calls_made'] == 0 and st['todo_items'] == 0 and len(CALLS) == n0, st
    shutil.move(A_DIR + '/results.jsonl', A_DIR + '/results.moved')              # results lost -> replies reused
    st = R.run_gemini(A_SET, A_DIR, 'T', ledger_path=A_LED, key='MOCK')
    assert st['status'] == 'COMPLETE' and st['calls_made'] == 0 and st['needed'] == 0, st


@t('T4 usage-limit (per-day quota) envelope -> hard STOP, 0 counted, STOP file')
def _():
    n = []
    B.HTTP[0] = lambda *a: (n.append(1), EDAY)[1]
    d = TMP + '/run_q'
    st = R.run_gemini(write_set(TMP + '/set_q.jsonl', sid_items(2461)), d, 'Q', ledger_path=TMP + '/led_q.json', key='MOCK')
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'quota' and st['counted_total'] == 0 and len(n) == 1, st
    assert os.path.exists(d + '/STOP_quota.md') and json.load(open(TMP + '/led_q.json')) == {'Q': 0}


@t('T5 phase ledger: other stages 1,199 + needed > 1,200 -> STOP before any call')
def _():
    n = []
    B.HTTP[0] = lambda *a: (n.append(1), ok_js())[1]
    lp = TMP + '/led_c.json'; R.write_json(lp, {'OTHER': 1199})
    st = R.run_gemini(write_set(TMP + '/set_c.jsonl', sid_items(2989)), TMP + '/run_c', 'C', ledger_path=lp, key='MOCK')
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'cap' and not n and st['needed'] >= 2, st


@t('T6 --expect-needed mismatch -> STOP at 0 calls; seeded replies are reused and not counted')
def _():
    n = []
    B.HTTP[0] = lambda *a: (n.append(1), ok_js())[1]
    st = R.run_gemini(A_SET, TMP + '/run_e', 'E', ledger_path=TMP + '/led_e.json', key='MOCK', expect_needed=999)
    assert st['status'] == 'STOPPED' and st['stop']['kind'] == 'expect' and not n, st
    st = R.run_gemini(A_SET, TMP + '/run_s', 'S', seed_ledger=A_DIR + '/ledger.jsonl', ledger_path=TMP + '/led_s.json',
                      key='MOCK', expect_needed=0)
    assert st['status'] == 'COMPLETE' and not n and st['counted_total'] == 0 and st['seeded_used'] >= 2, st


@t('T7 relative-path invocation works (relative script, --set, --run-dir, --ledger; cwd = translation-offline)')
def _():
    write_set(TMP + '/set_rel.jsonl', sid_items(250))
    env = dict(os.environ, P2J_MOCK='1', PYTHONDONTWRITEBYTECODE='1')
    p = subprocess.run([sys.executable, '-B', 'phase2j/run_2j.py', 'gemini', '--set', 'phase2j/_test_tmp/set_rel.jsonl',
                        '--run-dir', 'phase2j/_test_tmp/run_rel', '--stage', 'REL', '--ledger', 'phase2j/_test_tmp/led_rel.json'],
                       cwd=TOFF, env=env, capture_output=True, text=True, timeout=1200)
    assert p.returncode == 0, p.stdout[-800:] + p.stderr[-1500:]
    st = json.load(open(TMP + '/run_rel/RUN_STATUS.json'))
    assert st['status'] == 'COMPLETE' and st['results_missing'] == 0 and st['mock'], st
    p = subprocess.run([sys.executable, '-B', 'phase2j/run_2j.py', 'gemini', '--set', 'phase2j/_test_tmp/set_rel.jsonl',
                        '--run-dir', 'phase2j/run_X', '--stage', 'X'], cwd=TOFF, env=env, capture_output=True, text=True)
    assert p.returncode != 0 and 'REFUSED' in (p.stdout + p.stderr), 'mock must be refused on a real run dir'


@t('T8 A2 hook on the REAL stack path: fix ON vs OFF prepare on the 5 sids -> exactly the 44 new L3 requests')
def _():
    its = [B.clean_item(i, 'tonly') for i in sid_items(250, 1038, 1214, 2461, 2989)]
    fin = TMP + '/hook_items.json'; json.dump(its, open(fin, 'w', encoding='utf-8'), ensure_ascii=False)
    out = {}
    for fix in (0, 1):
        o = TMP + '/hook_prep_%d.json' % fix
        env = dict(os.environ, P2J_F4FIX=str(fix), PYTHONDONTWRITEBYTECODE='1', P2I_RUN_DIR=TMP + '/hook_%d' % fix)
        p = subprocess.run([sys.executable, '-B', P2J + '/stack_tonly.py', 'prepare', fin, o], env=env, cwd=TMP,
                           capture_output=True, text=True, timeout=1200)
        assert p.returncode == 0, p.stderr[-1500:]
        out[fix] = json.load(open(o, encoding='utf-8'))
        if fix:
            assert 'F4FIX sweep' in p.stderr, 'sweep not run'
    # Compare REQUEST HASHES, not jids: identical requests are deduplicated by the stack, so which jid carries a shared
    # request depends on the subset (A:250:c3 in the 45-item subset). Full-set proof: partA/_run/reqkeys_fix{0,1}.json.
    import hashlib
    rk = lambda q: hashlib.sha256(json.dumps([q['sys'], q['user'], q['gcfg']], sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()
    H0, H1 = {rk(q) for q in out[0].values()}, {rk(q) for q in out[1].values()}
    full1 = json.load(open(P2J + '/partA/_run/reqkeys_fix1.json'))['requests']
    full0 = set(json.load(open(P2J + '/partA/_run/reqkeys_fix0.json'))['requests'].values())
    H44 = {full1[j] for j in NEW44}
    assert H44 <= H1, 'fix ON misses %d of the 44 requests' % len(H44 - H1)
    assert (H1 - H0) == (H44 - H0), ('new requests outside the 44', len((H1 - H0) - H44))
    assert H0 <= H1, 'fix ON lost a request that fix OFF made'
    assert len(H44 - full0) == 43, ('full-set new unique requests', len(H44 - full0))
    s0, s1 = set(out[0]) - set(NEW44), set(out[1]) - set(NEW44)
    assert all(rk(out[0][j]) == rk(out[1][j]) for j in s0 & s1), 'request changed outside the 44'


sys.path.insert(0, TOFF + '/phase1i')
import checker_1i as C                                                          # noqa: E402
import f4fix                                                                    # noqa: E402
FX = f4fix.build_fixed(C)
UNIT = [('Vozidlo uháňalo po vidieckej ceste predtým, než bolo zaparkované pri dunách, ako bolo pozorované.', 'The vehicle had sped along the road before it was parked by the dunes.', False),
        ('Kamarátka povedala, že náramok je príliš voľný, tak ho upravila.', 'My friend said the bracelet was too loose, so she adjusted it.', False),
        ('Povedal, že tréning bol najtvrdší v celom jeho živote! Čistá agónia!', 'He said the training was the hardest of his life!', False),
        ('Od roku 2019 fotí lietadlá pri tomto plote. Zjavne veľmi nenáročný koníček.', 'He has photographed planes at this fence since 2019.', False),
        ('Samozrejme si dala trasu nakresliť na mapu, pre prípad, že by zabudla vlastný plán.', 'Of course she had the route drawn on the map.', False),
        ('Chodíte po starej ceste každý deň?', 'Does he walk along the old road every day?', True),
        ('Včera sme boli v meste.', 'He was in town yesterday.', True),
        ('Robíte to príliš často.', 'He does it too often.', True),
        ('Išli sme po starej ceste.', 'They went along the old road.', True)]


@t('T9 A2 fix unit: the 5 misread sentences no longer fire, real verbs still do (9 cases)')
def _():
    bad = [(s, want) for s, en, want in UNIT if FX['f4v2_subject_mismatch']({'sk': s, 'answer': en})[0] != want]
    assert not bad, bad


VERBS_SK, VERBS_CZ = {'potrebuješ', 'bola'}, {'byla', 'mluvila', 'dala'}


@t('T10 A2 verb-loss (S1 cost candidates): a PP-head verb keeps its reading - synthetic SK + CZ')
def _():
    sys.path.insert(0, TOFF + '/phase1v/trackC')
    import cz_reader as CZ
    ckcz = CZ.build()['CK']; fxcz = f4fix.build_fixed(ckcz, 'cz')
    for s, en in (('Na tom potrebuješ pomoc.', 'He needs help with that.'), ('O tom bola presvedčená.', 'He was convinced of it.'),
                  ('Pri tejto práci bola veľmi rýchla.', 'He was very fast at this work.')):
        assert FX['sk_features'](s) == C.sk_features(s), (s, C.sk_features(s), FX['sk_features'](s))
        assert FX['f4v2_subject_mismatch']({'sk': s, 'answer': en})[0] == C.f4v2_subject_mismatch({'sk': s, 'answer': en})[0], s
    for s in ('O tom mluvila celý den.', 'Při tom byla klidná.', 'O tom dala vědět.', 'Na tom potřebuješ pomoc.'):
        assert fxcz['sk_features'](s) == ckcz.sk_features(s), (s, ckcz.sk_features(s), fxcz['sk_features'](s))
    globals()['CZPAIR'] = (ckcz, fxcz)


@t('T11 A2 verb-loss on both upload files: every potrebuješ/bola (SK), byla/mluvila/dala (CZ) signal is kept; '
   'every removed signal is a non-verb')
def _():
    ckcz, fxcz = CZPAIR
    rep = {}
    for lang, path, old, new, verbs in (('sk', P2I + '/upload/annotations_sk_fixed.jsonl', C.sk_features, FX['sk_features'], VERBS_SK),
                                        ('cz', P2I + '/upload/annotations_cz_fixed.jsonl', ckcz.sk_features, fxcz['sk_features'], VERBS_CZ)):
        kept = lost = chg = 0; removed = collections.Counter(); bad = []
        for l in open(path, encoding='utf-8'):
            s = json.loads(l)['src']
            so, sn = old(s)[1], new(s)[1]
            if so != sn:
                chg += 1
            for x in so:
                w = x.split()[-1]
                if w in verbs:
                    if x in sn: kept += 1
                    else: lost += 1; bad.append((s, x))
            for x in set(so) - set(sn):
                w = x.split()[-1]; removed[w] += 1
                if f4fix.is_verb_head(w):
                    bad.append((s, 'removed verb-like ' + x))
        rep[lang] = {'rows_changed': chg, 'verb_signals_kept': kept, 'lost': lost, 'removed_top': removed.most_common(12)}
        assert kept >= 1 and not bad, (lang, bad[:5])
    json.dump(rep, open(P2J + '/partA/T11_verbloss.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def fake(rc, env, stderr=''):
    import types
    return types.SimpleNamespace(returncode=rc, stdout=json.dumps(env) if env is not None else 'garbage', stderr=stderr)


OKE = {'type': 'result', 'subtype': 'success', 'is_error': False, 'result': 'done; row 429 of 4290 written',
       'num_turns': 3, 'usage': {'input_tokens': 10, 'cache_creation_input_tokens': 20, 'cache_read_input_tokens': 30, 'output_tokens': 40}}


@t('T12 headless spawner: ok envelope (usage summed; "429" in result text is not a rate limit), resume 0 spawns, argv recipe')
def _():
    R.ENV[0] = {'MOCK': '1'}
    seq = []
    R.SPAWN[0] = lambda argv, to: (seq.append(argv), fake(0, OKE, 'stderr says 429 too'))[1]
    d = R.run_session('s1', 'PROMPT', TMP + '/hl', stop_dir=TMP)
    assert d['status'] == 'ok' and d['tokens'] == 100 and d['spawns'] == 1 and len(seq) == 1, d
    a = seq[0]
    assert a[0] == R.BIN and a[1:3] == ['-p', 'PROMPT'] and a[3:5] == ['--output-format', 'json'] and '--model' in a, a
    d = R.run_session('s1', 'PROMPT', TMP + '/hl', stop_dir=TMP)
    assert d.get('resumed') and len(seq) == 1


@t('T13 headless: real 429 envelope retried; usage-limit envelope -> STOP_usage_limit.md + hard stop; stop file blocks')
def _():
    R.ENV[0] = {'MOCK': '1'}
    q = [fake(1, {'type': 'result', 'is_error': True, 'api_error_status': 429, 'result': 'API Error: 429 rate_limit_error'}), fake(0, OKE)]
    R.SPAWN[0] = lambda argv, to: q.pop(0)
    d = R.run_session('s2', 'P', TMP + '/hl', stop_dir=TMP)
    assert d['status'] == 'ok' and d['spawns'] == 2 and not q
    R.SPAWN[0] = lambda argv, to: fake(1, {'type': 'result', 'is_error': True, 'result': 'Claude AI usage limit reached|resets at 5pm'})
    try:
        R.run_session('s3', 'P', TMP + '/hl', stop_dir=TMP); raise AssertionError('no stop')
    except R.Stop as e:
        assert e.kind == 'usage_limit'
    assert os.path.exists(TMP + '/STOP_usage_limit.md')
    try:
        R.run_session('s4', 'P', TMP + '/hl', stop_dir=TMP); raise AssertionError('stop file ignored')
    except R.Stop as e:
        assert e.kind == 'usage_limit'
    os.remove(TMP + '/STOP_usage_limit.md')
    R.SPAWN[0] = lambda argv, to: fake(1, {'type': 'result', 'is_error': True, 'result': 'boom'})
    try:
        R.run_session('s5', 'P', TMP + '/hl', stop_dir=TMP, token_cap=10 ** 9); raise AssertionError('no stop')
    except R.Stop as e:
        assert e.kind == 'headless_failed'
    try:
        R.run_session('s6', 'P', TMP + '/hl', stop_dir=TMP, token_cap=150, est=100); raise AssertionError('cap ignored')
    except R.Stop as e:
        assert e.kind == 'token_cap'


npass = sum(1 for r in RES if r[1] == 'PASS')
for r in RES:
    print('%s  %s%s' % (r[1], r[0], ('\n      ' + r[2]) if r[2] else ''))
print('SUMMARY %d/%d PASS' % (npass, len(RES)))
shutil.rmtree(TMP, ignore_errors=True)
sys.exit(0 if npass == len(RES) else 1)
