#!/usr/bin/env python3
"""Wave 1 test suite over the REAL code path (stack_w1 -> run_2i_base.call_one -> HTTP), model MOCKED, 0 real calls.
Brief: a row number containing "429", a real 429 envelope, a usage-limit envelope, resume at 0 cost, relative path
refused, poison test (no English reference read); plus parser tests, the dropped-word lists and decision 22 in every
prompt, prompt derivation byte-exact against the frozen sk/cz texts, the layer order, the caps.
    python3 -B /abs/wave1/common/test_w1.py   (exit 0 = all PASS)"""
import hashlib, json, os, shutil, sys, traceback, types
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import stack_w1 as S     # noqa: E402
import prompts_w1 as P   # noqa: E402
import run_2j as H       # noqa: E402  headless spawner (byte copy of phase2j/run_2j.py)
B, CC = S.B, S.CC
T = os.path.join(S.W1, '_test')
CALLS, BODIES, SCRIPT = [0], [], []
EN_REF = 'The big dog is sleeping in the garden right now.'
RESULTS = []


def fake_http(url, body, key):
    """SCRIPT: list of (code, reply_text | envelope dict) consumed in order; default = 200 'SAME' / 'NONE'."""
    CALLS[0] += 1
    BODIES.append(json.dumps(body, ensure_ascii=False))
    if SCRIPT:
        code, x = SCRIPT.pop(0)
    else:
        sysx = body['systemInstruction']['parts'][0]['text']
        code, x = 200, ('NONE' if 'NONE or MISSING' in body['contents'][0]['parts'][0]['text'] else 'SAME')
        _ = sysx
    if code == 200:
        js = {'candidates': [{'content': {'parts': [{'text': x}]}, 'finishReason': 'STOP'}],
              'usageMetadata': {'promptTokenCount': 300, 'candidatesTokenCount': 1}}
        return 200, js, json.dumps(js)
    return code, x, json.dumps(x)


def reset(name):
    d = os.path.join(T, name)
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    CALLS[0] = 0
    del BODIES[:]
    del SCRIPT[:]
    return d


def items(lang='de', n=3, extra=None):
    src = {'de': 'Der große Hund schläft jetzt im Garten.', 'ua': 'Великий пес зараз спить у саду.',
           'es': 'El perro grande duerme ahora en el jardín.'}[lang]
    out = []
    for i in range(n):
        it = {'jid': 'A:%d:c%d' % (7 + i, i + 1), 'sid': 7 + i, 'level': 'A1', 'src': src,
              'answer': 'The big dog sleeps in the garden %d.' % i}
        if extra:
            it.update(extra)
        out.append(it)
    return out


def run(name, fn):
    try:
        fn()
        RESULTS.append((name, 'PASS', ''))
    except BaseException as e:  # noqa
        RESULTS.append((name, 'FAIL', '%s: %s\n%s' % (type(e).__name__, e, traceback.format_exc()[-1500:])))


B.HTTP[0] = fake_http
B.SLEEP[0] = lambda s: None
B.MIN_INTERVAL = 0.0


def full(d, its, lang='de'):
    root = d
    return S.run_full(its, os.path.join(d, lang, 'run', 'x'), 'T', lang, S.lang_ledger(lang, root), key='MOCK', root=root)


# ---------------------------------------------------------------------------------------------------------------- tests
def t01_prompt_derivation():
    frozen_l3 = open(P.SRC['l3_sys'], encoding='utf-8').read()
    frozen_cc = CC.sys_text('cz')
    frozen_j = open(P.SRC['judge'], encoding='utf-8').read()
    frozen_w = open(P.SRC['writer'], encoding='utf-8').read()
    for lang, L in P.LANG.items():
        for name, txt, frozen, g22line in (
                ('l3', P.l3_sys(lang), frozen_l3, '- %s\n' % P.g22(lang)),
                ('cc', P.cc_sys(lang), frozen_cc, '- %s\n' % P.g22(lang)),
                ('judge', P.judge_prompt(lang), frozen_j, '- %s\n' % P.g22(lang)),
                ('writer', P.writer_template(lang), frozen_w,
                 "\n\nThe owner's rule for genderless sources: %s" % P.g22(lang)[len('Genderless source: '):])):
            if name == 'judge' and lang in P.JUDGE_D3233:      # decisions 32 + 33: judge prompt only, es only
                assert txt.count('- %s\n' % P.d32(lang)) == 1 and txt.count(P.D33_NEW) == 1, (lang, 'd32/d33')
                txt = txt.replace('- %s\n' % P.d32(lang), '').replace(P.D33_NEW, P.D33_OLD)
            elif name == 'judge':
                assert 'Grammatical gender decides' not in txt and 'ADDED interjection' not in txt, (lang, 'd32/d33 leaked')
            if name != 'judge':
                assert 'Grammatical gender decides' not in txt and 'ADDED interjection' not in txt, (lang, name, 'checker changed')
            assert txt.count(g22line) == 1, (lang, name, 'decision 22 line')
            assert P.DROP[lang] in txt, (lang, name, 'drop list')
            assert 'Slovak' not in txt and 'Czech' not in txt, (lang, name)
            back = txt.replace(g22line, '').replace(L, 'Czech')
            if name == 'cc':
                back = back.replace('Look!; Czech ' + P.DROP[lang], 'Look!; ' + P.SKCZ_CC.split('Look!; ', 1)[1])
            else:
                back = back.replace('(Czech: %s)' % P.DROP[lang], P.SKCZ_PAREN)
            assert back == frozen, (lang, name, 'not a pure substitution of the frozen text')
        assert P.l3_user(lang, 'X', 'Y') == '%s sentence: X\nLearner answer: Y\nSAME, TIP or DIFF?' % L
        assert P.cc_user(lang, 'X', 'Y') == '%s sentence: X\nLearner answer: Y\nNONE or MISSING?' % L
    assert P.GCFG_L3 == {'temperature': 0, 'maxOutputTokens': 24, 'thinkingConfig': {'thinkingBudget': 0}}
    assert P.GCFG_CC == CC.GCFG and P.MODEL == CC.MODEL == B.MODEL == 'gemini-3.1-flash-lite'


def t02_spec_files_match():
    for lang in P.LANG:
        for f, txt in (('l3_system_%s.txt', P.l3_sys(lang)), ('content_check_system_%s.txt', P.cc_sys(lang)),
                       ('judge_prompt_%s.txt', P.judge_prompt(lang)), ('writer_template_%s.txt', P.writer_template(lang))):
            p = os.path.join(S.W1, 'spec', f % lang)
            assert open(p, encoding='utf-8').read() == txt, p


def t03_parsers():
    assert [B.parse_reply(x) for x in ('SAME', 'same.', ' DIFF\n', '**TIP**', 'SAME DIFF', '', 'OK')] == \
        ['SAME', 'SAME', 'DIFF', 'TIP', None, None, None]
    assert CC.parse('NONE') == 'NONE' and CC.parse('NONE.') == 'NONE' and CC.parse(' NONE \n') == 'NONE'
    assert CC.parse('MISSING: Hund') == 'MISSING: Hund' and CC.parse('MISSING: en el jardín.') == 'MISSING: en el jardín'
    assert CC.parse('MISSING: саду') == 'MISSING: саду'
    for bad in ('none', 'MISSING:', 'MISSING Hund', 'NONE\nMISSING: x', 'Missing: x', '', None, 'NONE, nothing'):
        assert CC.parse(bad) is None, bad
    assert CC.word_of('MISSING: en el jardín') == 'en el jardín' and CC.word_of('NONE') is None


def t04_row_number_429_is_not_a_rate_limit():
    d = reset('t04')
    its = items('de', 2)
    its[0]['jid'] = 'A:429:c1'; its[0]['sid'] = 429; its[0]['answer'] = 'Room 429 is free, error 429 RESOURCE_EXHAUSTED.'
    SCRIPT.extend([(200, 'SAME'), (200, 'SAME'), (200, 'NONE'), (200, 'MISSING: 429')])
    out = full(d, its)
    assert out['status'] == 'COMPLETE', out
    assert out['l3']['uncounted_attempts'] == 0 and out['cc']['uncounted_attempts'] == 0
    led = B.jl_read(os.path.join(d, 'de/run/x/l3/ledger.jsonl'))
    assert all(r['http'] == 200 and r['counted'] for r in led) and len(led) == 2
    # a 200 reply whose TEXT says 429 is a counted FAILED call, never a rate limit
    d2 = reset('t04b')
    SCRIPT.extend([(200, 'HTTP 429 RESOURCE_EXHAUSTED quota exceeded per day')])
    out = full(d2, items('de', 1))
    led = B.jl_read(os.path.join(d2, 'de/run/x/l3/ledger.jsonl'))
    assert len(led) == 1 and led[0]['counted'] and led[0]['failed'] and out['status'] == 'COMPLETE'
    fin = B.jl_read(os.path.join(d2, 'de/run/x/final_tiprej.jsonl'))
    assert fin[0]['layer'] == 'L3:failed' and fin[0]['accept'] is False
    assert not os.path.exists(os.path.join(d2, 'de/run/x/l3/STOP_quota.md'))


def t05_real_429_envelope_retries_uncounted():
    d = reset('t05')
    env = {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'Resource has been exhausted (e.g. check quota).',
                     'details': [{'@type': 'type.googleapis.com/google.rpc.QuotaFailure',
                                  'violations': [{'quotaMetric': 'generate_content_free_tier_requests',
                                                  'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel'}]}]}}
    SCRIPT.extend([(429, env), (503, {'error': {'code': 503, 'status': 'UNAVAILABLE'}}), (200, 'DIFF')])
    out = full(d, items('ua', 1), 'ua')
    led = B.jl_read(os.path.join(d, 'ua/run/x/l3/ledger.jsonl'))
    assert [r['http'] for r in led] == [429, 503, 200] and [r['counted'] for r in led] == [False, False, True]
    assert out['l3']['counted_total'] == 1 and out['l3']['uncounted_attempts'] == 2 and out['cc']['needed'] == 0
    assert S.read_json(S.lang_ledger('ua', d), {}) == {'T_L3': 1, 'T_CC': 0}


def t06_usage_limit_envelopes_stop():
    d = reset('t06')
    env = {'error': {'code': 429, 'status': 'RESOURCE_EXHAUSTED', 'message': 'You exceeded your current quota.',
                     'details': [{'@type': 'type.googleapis.com/google.rpc.QuotaFailure',
                                  'violations': [{'quotaMetric': 'generate_content_requests',
                                                  'quotaId': 'GenerateRequestsPerDayPerProjectPerModel'}]}]}}
    SCRIPT.extend([(429, env)])
    out = full(d, items('es', 2), 'es')
    assert out['status'] == 'STOPPED' and out['l3']['stop']['kind'] == 'quota', out
    assert out['l3']['counted_total'] == 0 and CALLS[0] == 1
    assert os.path.exists(os.path.join(d, 'es/run/x/l3/STOP_quota.md'))
    # headless Claude: a usage-limit ERROR envelope -> hard stop + STOP_usage_limit.md; '429' in an OK result is not
    envu = {'type': 'result', 'is_error': True, 'subtype': 'error', 'result': "Claude AI usage limit reached|1760000000",
            'usage': {'input_tokens': 5, 'output_tokens': 0}}
    assert H.classify_headless(1, json.dumps(envu), '')[0] == 'usage'
    envok = {'type': 'result', 'is_error': False, 'subtype': 'success', 'result': '[{"jid": "j429", "reason": "429 limit"}]',
             'usage': {'input_tokens': 5, 'output_tokens': 7}}
    assert H.classify_headless(0, json.dumps(envok), 'rate limit 429 usage limit in stderr')[0] == 'ok'
    envr = {'type': 'result', 'is_error': True, 'subtype': 'error', 'api_error_status': 429, 'result': 'rate limited'}
    assert H.classify_headless(1, json.dumps(envr), '')[0] == 'rate'
    H.SPAWN[0] = lambda argv, timeout: types.SimpleNamespace(returncode=1, stdout=json.dumps(envu), stderr='')
    H.ENV[0] = dict(os.environ)
    sd = os.path.join(d, 'hl')
    try:
        H.run_session('s1', 'prompt', sd, stop_dir=d, model='opus', max_turns=2)
        raise AssertionError('no stop')
    except H.Stop as e:
        assert e.kind == 'usage_limit'
    assert os.path.exists(os.path.join(d, 'STOP_usage_limit.md'))
    try:
        H.run_session('s2', 'prompt', os.path.join(d, 'hl2'), stop_dir=d)
        raise AssertionError('no stop on STOP file')
    except H.Stop as e:
        assert e.kind == 'usage_limit'


def t07_resume_at_zero_cost():
    d = reset('t07')
    its = items('de', 4)
    its[1]['answer'] = its[0]['answer']          # identical request -> called once
    SCRIPT.extend([(200, 'SAME'), (200, 'TIP'), (200, 'DIFF'), (200, 'NONE'), (200, 'MISSING: Garten')])
    o1 = full(d, its)
    n1 = CALLS[0]
    f1 = open(os.path.join(d, 'de/run/x/final_tiprej.jsonl'), 'rb').read()
    o2 = full(d, its)
    assert CALLS[0] == n1 and n1 in (4, 5), (CALLS[0], n1)
    assert o2['l3']['calls_made'] == 0 and o2['cc']['calls_made'] == 0 and o2['status'] == 'COMPLETE'
    assert open(os.path.join(d, 'de/run/x/final_tiprej.jsonl'), 'rb').read() == f1
    # a stopped run resumes and makes only the missing calls
    d2 = reset('t07b')
    SCRIPT.extend([(200, 'SAME'), (400, {'error': {'code': 400, 'status': 'INVALID_ARGUMENT'}})])
    o = full(d2, items('de', 3))
    assert o['status'] == 'STOPPED' and CALLS[0] == 2
    o = full(d2, items('de', 3))
    assert o['status'] == 'COMPLETE' and CALLS[0] == 2 + 2 + 3, CALLS[0]   # 2 L3 left + 3 CC (all SAME)
    led = [r for r in B.jl_read(os.path.join(d2, 'de/run/x/l3/ledger.jsonl')) if r['http'] == 200]
    assert len(led) == len({r['req_key'] for r in led}) == 3      # no request answered twice


def t08_relative_path_refused():
    d = reset('t08')
    for args in (('l3', items(), 'rel/run', 'T', 'de', os.path.join(d, 'de/GEMINI_LEDGER.json')),
                 ('l3', items(), os.path.join(d, 'x'), 'T', 'de', 'de/GEMINI_LEDGER.json'),
                 ('l3', items(), '/tmp/outside_wave1', 'T', 'de', os.path.join(d, 'de/GEMINI_LEDGER.json'))):
        try:
            S.run_calls(*args, key='MOCK')
            raise AssertionError('not refused: %r' % (args[2:],))
        except S.Refused:
            pass
    assert CALLS[0] == 0 and not os.path.exists('rel') and not os.path.exists(os.path.join(d, 'x'))
    try:
        S.run_calls('l3', items('fr'.replace('fr', 'de')), os.path.join(d, 'y'), 'T', 'fr', os.path.join(d, 'de/L.json'), key='MOCK')
        raise AssertionError('language fr not refused')
    except S.Refused:
        pass


class PoisonVal(object):
    def __getattribute__(self, n):
        raise S.PoisonHit('value.' + n)


for _n in ('__str__', '__repr__', '__len__', '__iter__', '__eq__', '__hash__', '__bool__', '__format__', '__add__',
           '__radd__', '__contains__', '__getitem__', '__mod__'):
    setattr(PoisonVal, _n, (lambda n: lambda self, *a, **k: (_ for _ in ()).throw(S.PoisonHit('value.' + n)))(_n))


def t09_poison_no_reference_read():
    d = reset('t09')
    extra = {'en': PoisonVal(), 'v': PoisonVal(), 'alt': PoisonVal(), 'lk': PoisonVal(), 'lk_verdict': PoisonVal(),
             'reference': PoisonVal(), 'english': PoisonVal(), 'full_sentence_en': PoisonVal()}
    its = [S.PoisonDict(x) for x in items('es', 3, extra)]
    SCRIPT.extend([(200, 'SAME'), (200, 'SAME'), (200, 'SAME'), (200, 'NONE'), (200, 'NONE'), (200, 'NONE')])
    out = full(d, its, 'es')
    assert out['status'] == 'COMPLETE'
    assert BODIES and all(EN_REF not in b and 'big dog' not in b.split('Learner answer')[0] for b in BODIES)
    # an honest reference string never reaches a request body either
    d2 = reset('t09b')
    its2 = items('ua', 2, {'en': EN_REF, 'v': [EN_REF], 'alt': {'dog': ['hound']}, 'lk': ['is sleeping']})
    full(d2, its2, 'ua')
    assert BODIES and all(EN_REF not in b and 'hound' not in b and 'is sleeping' not in b for b in BODIES)
    for b in BODIES:
        body = json.loads(b)
        assert set(body) == {'systemInstruction', 'contents', 'generationConfig'}
        u = body['contents'][0]['parts'][0]['text']
        assert u.startswith('Ukrainian sentence: Великий пес зараз спить у саду.\nLearner answer: The big dog sleeps')
    # a direct read of a reference key raises
    for k in ('en', 'v', 'alt', 'lk', 'lk_x', 'reference', 'english'):
        try:
            S.PoisonDict({k: 1})[k]
            raise AssertionError('no poison for %s' % k)
        except S.PoisonHit:
            pass


def t10_layer_order():
    d = reset('t10')
    its = items('de', 6)
    for i, it in enumerate(its):
        it['answer'] = 'answer %d' % i
    # sorted request order = sorted req_key; script by content instead
    rep = {'answer 0': 'SAME', 'answer 1': 'TIP', 'answer 2': 'DIFF', 'answer 3': 'garbage reply', 'answer 4': 'SAME',
           'answer 5': 'SAME'}
    ccrep = {'answer 0': 'NONE', 'answer 4': 'MISSING: Hund', 'answer 5': 'I think NONE'}

    def http(url, body, key):
        CALLS[0] += 1
        u = body['contents'][0]['parts'][0]['text']
        a = u.split('Learner answer: ', 1)[1].split('\n', 1)[0]
        x = ccrep[a] if u.endswith('NONE or MISSING?') else rep[a]
        js = {'candidates': [{'content': {'parts': [{'text': x}]}}], 'usageMetadata': {'promptTokenCount': 10, 'candidatesTokenCount': 1}}
        return 200, js, json.dumps(js)
    B.HTTP[0] = http
    try:
        out = full(d, its)
    finally:
        B.HTTP[0] = fake_http
    fin = {r['jid']: r for r in B.jl_read(os.path.join(d, 'de/run/x/final_tiprej.jsonl'))}
    got = [(fin[it['jid']]['accept'], fin[it['jid']]['layer']) for it in its]
    assert got == [(True, 'L3+CC:NONE'), (False, 'L3:TIPrej'), (False, 'L3'), (False, 'L3:failed'),
                   (False, 'CC:MISSING'), (True, 'L3+CC:failed')], got
    assert out['cc']['requests'] == 3 and CALLS[0] == 9
    assert fin[its[4]['jid']]['cc_word'] == 'Hund'


def t11_caps():
    def setup(name, led):
        d = reset(name)
        for lg, v in led.items():
            os.makedirs(os.path.join(d, lg), exist_ok=True)
            S.write_json(S.lang_ledger(lg, d), v)
        return d
    # language cap: needed > cap -> STOP before any call
    out = full(setup('t11', {'ua': {'X': S.LANG_CAP - 1}}), items('ua', 2), 'ua')
    assert out['status'] == 'STOPPED' and out['l3']['stop']['kind'] == 'cap' and CALLS[0] == 0, out
    # wave cap: other languages 3,400 + ua 1,599 -> exactly one call left in the wave
    out = full(setup('t11b', {'de': {'X': 1700}, 'es': {'X': 1700}, 'ua': {'Y': 1599}}), items('ua', 1), 'ua')
    assert out['status'] == 'STOPPED' and out['l3']['calls_made'] == 1 and out['cc']['stop']['kind'] == 'cap', out
    assert CALLS[0] == 1 and S.wave_counted(os.path.join(T, 't11b')) == 5000
    # wave full -> 0 calls
    out = full(setup('t11c', {'de': {'X': 1700}, 'es': {'X': 1700}, 'ua': {'Y': 1600}}), items('ua', 1), 'ua')
    assert out['status'] == 'STOPPED' and CALLS[0] == 0
    # the per-call wave re-read: another language spends the last calls while this one runs
    d = setup('t11d', {'de': {'X': 1700}, 'es': {'X': 1697}, 'ua': {'Y': 1600}})
    orig = B.HTTP[0]

    def http(url, body, key):         # es calls concurrently, honouring the same lock + cap
        with S.wave_lock(d):
            if S.wave_counted(d) < S.WAVE_CAP:
                S.write_json(S.lang_ledger('es', d), {'X': S.read_json(S.lang_ledger('es', d), {})['X'] + 1})
        return orig(url, body, key)
    B.HTTP[0] = http
    try:
        out = full(d, items('ua', 3), 'ua')
    finally:
        B.HTTP[0] = orig
    assert out['status'] == 'STOPPED' and out['l3']['stop']['kind'] == 'wave_cap' and S.wave_counted(d) == 5000, (out, S.wave_counted(d))
    assert abs(S.LANG_SPEND * 3 - S.WAVE_SPEND) < 1e-9 and S.WAVE_CAP == 5000


def t12_drop_lists_and_g22_everywhere():
    for lang in P.LANG:
        for txt in (P.l3_sys(lang), P.cc_sys(lang), P.judge_prompt(lang), P.writer_template(lang)):
            for w in P.DROP[lang].split(', '):
                assert w in txt, (lang, w)
            assert 'BOTH he/she and his/her are correct' in txt
            assert 'now, today, already, still, finally, then, totally, completely, just, Look!' in txt
    assert set(P.DROP) == set(P.LANG) == {'de', 'ua', 'es'}


def t13_frozen_sources_untouched():
    before = {l.rstrip('\n').split('  ', 1)[1]: l.split('  ', 1)[0] for l in open(os.path.join(S.W1, 'SHA_before.txt'), encoding='utf-8') if l.strip()}
    for p in list(P.SRC.values()) + [os.path.join(S.W1, '..', 'phase2l', 'run_2i_base.py'),
                                      os.path.join(S.W1, '..', 'phase2j', 'run_2j.py')]:
        p = os.path.normpath(p)
        rel = os.path.relpath(p, os.path.dirname(S.W1))
        assert hashlib.sha256(open(p, 'rb').read()).hexdigest() == before[rel], rel
    for mine, theirs in (('run_2i_base.py', 'phase2l/run_2i_base.py'), ('content_check.py', 'phase2l/content_check.py'),
                         ('run_2j.py', 'phase2j/run_2j.py')):
        assert open(os.path.join(HERE, mine), 'rb').read() == open(os.path.join(os.path.dirname(S.W1), theirs), 'rb').read(), mine


def t14_subagent_transport():
    """Decision 26: sub_session writes prompt.txt + PENDING and stops 'pending' (0 tokens); a reply + tokens.json is
    ingested once into the ledger; a finished session resumes at 0 cost; an invalid reply goes to ONE retry `_r1`."""
    import pipeline_w1 as W
    d = reset('t14')
    W.SUB_FAKE[0] = None
    W.L.update(lang='de', dir=d)
    ok_v = lambda arr: None if isinstance(arr, list) and arr and arr[0].get('x') == 1 else 'bad'
    r = W.run_group('writers', {'A1': ('PROMPT A1', ok_v)}, d, d, est=10, max_turns=2, cap_session=None, spent_base=d)
    assert r['A1']['stop'] == 'pending' and W.handle_fail(r, d, 'writers') == 6
    sd = os.path.join(d, 'writers/sessions/A1')
    assert open(os.path.join(sd, 'prompt.txt')).read() == 'PROMPT A1' and os.path.exists(os.path.join(sd, 'PENDING.json'))
    open(os.path.join(sd, 'reply.txt'), 'w').write('```json\n[{"x": 2}]\n```')          # invalid -> retry _r1
    json.dump({'total_tokens': 1234}, open(os.path.join(sd, 'tokens.json'), 'w'))
    r = W.run_group('writers', {'A1': ('PROMPT A1', ok_v)}, d, d, est=10, max_turns=2, cap_session=None, spent_base=d)
    assert r['A1']['stop'] == 'pending' and 'A1_r1' in r['A1']['why'], r
    assert W.spent(d) == 1234
    s1 = os.path.join(d, 'writers/sessions/A1_r1')
    open(os.path.join(s1, 'reply.txt'), 'w').write('[{"x": 1}]')
    json.dump({'total_tokens': 100}, open(os.path.join(s1, 'tokens.json'), 'w'))
    r = W.run_group('writers', {'A1': ('PROMPT A1', ok_v)}, d, d, est=10, max_turns=2, cap_session=None, spent_base=d)
    assert r['A1']['ok'] and r['A1']['arr'] == [{'x': 1}] and W.spent(d) == 1334
    r = W.run_group('writers', {'A1': ('PROMPT A1', ok_v)}, d, d, est=10, max_turns=2, cap_session=None, spent_base=d)
    assert r['A1']['ok'] and all(a['resumed'] for a in r['A1']['attempts']) and W.spent(d) == 1334   # 0 cost
    r = W.run_group('writers', {'A1': ('CHANGED PROMPT', ok_v)}, d, d, est=10, max_turns=2, cap_session=None, spent_base=d)
    assert r['A1']['ok']                                     # finished sessions are never re-asked
    jv = lambda arr: None if arr == [1] else 'jid set mismatch (missing 1, extra 0)'
    for sid in ('J', 'J_r1'):
        sd_ = os.path.join(d, 'judge/sessions', sid); os.makedirs(sd_, exist_ok=True)
        open(os.path.join(sd_, 'prompt.txt'), 'w').write('PJ'); open(os.path.join(sd_, 'reply.txt'), 'w').write('[2]')
        json.dump({'total_tokens': 1}, open(os.path.join(sd_, 'tokens.json'), 'w'))
    r = W.run_group('judge', {'J': ('PJ', jv)}, d, d, est=1, max_turns=2, cap_session=None, spent_base=d)
    assert r['J']['stop'] == 'pending' and 'J_r2' in r['J']['why'], r      # 2 jid-set misses -> ONE more attempt
    for sid in ('K', 'K_r1'):
        sd_ = os.path.join(d, 'judge/sessions', sid); os.makedirs(sd_, exist_ok=True)
        open(os.path.join(sd_, 'prompt.txt'), 'w').write('PK'); open(os.path.join(sd_, 'reply.txt'), 'w').write('not json')
        json.dump({'total_tokens': 1}, open(os.path.join(sd_, 'tokens.json'), 'w'))
    r = W.run_group('judge', {'K': ('PK', jv)}, d, d, est=1, max_turns=2, cap_session=None, spent_base=d)
    assert not r['K']['ok'] and r['K'].get('stop') is None, r                # other failures: no third attempt
    d2 = os.path.join(d, 'cap')
    r = W.run_group('judge', {'s1': ('P', ok_v)}, d2, d2, est=500, max_turns=2, cap_session=400, spent_base=d2)
    assert r['s1']['stop'] == 'token_cap'                    # the per-session cap still holds


def t15_es_eight_packets_and_followups():
    """Decision 31: 8 shuffled packets (originals 112-113, all levels), 80 controls in a different packet; a judge
    reply that drops / duplicates / invents jids gets a follow-up session over the MISSING jids only, with the same
    prompt, merged; at most 2 follow-ups, then STOP."""
    import pipeline_w1 as W
    d = reset('t15')
    W.L.update(lang='es', dir=d, D=d)
    lv = ['A1', 'A2', 'B1', 'B2']
    ans = []
    for sid in range(100):
        for suf, intent, typ in [('c%d' % i, 'correct', None) for i in range(1, 6)] + [(x.lower(), 'wrong', x) for x in 'TWMS']:
            ans.append({'aid': 'A:%d:%s' % (sid, suf), 'sid': sid, 'level': lv[sid % 4], 'source': 'S%d' % sid, 'topic': 't',
                        'answer': '%s %d' % (suf, sid), 'writer_intent': intent, 'writer_type': typ, 'writer_agent_drop': False})
    W.wjl(d + '/set/answers.jsonl', ans)
    assert W.packets(d) == 0
    key = W.jl(d + '/judge/key.jsonl')
    meta = json.load(open(d + '/judge/PACKETS_META.json'))
    assert meta['packets'] == 8 and sorted(meta['sessions']) == [str(i) for i in range(1, 9)]
    assert all(v['originals'] in (112, 113) and len(v['levels']) == 4 for v in meta['sessions'].values())
    cl = [k for k in key if k['is_control']]
    assert len(cl) == 80 and all(k['session'] != k['orig_session'] for k in cl) and meta['controls_by_intent'] == {'correct': 40, 'wrong': 40}
    assert len({k['aid'] for k in key if not k['is_control']}) == 900
    # judge_rows: missing / duplicate / invented / bad rows -> missing, deterministic packet order
    rows, miss, notes = W.judge_rows([{'jid': 'a', 'label': 'correct', 'reason': ''}, {'jid': 'b', 'label': 'x', 'reason': ''},
                                      {'jid': 'c', 'label': 'wrong', 'reason': ''}, {'jid': 'c', 'label': 'wrong', 'reason': ''},
                                      {'jid': 'zz', 'label': 'wrong', 'reason': ''}], ['a', 'b', 'c', 'd'])
    assert set(rows) == {'a'} and miss == ['b', 'c', 'd'] and notes['extra'] == ['zz'] and notes['duplicate'] == ['c']
    assert W.judge_rows(None, ['a', 'b'])[1] == ['a', 'b']
    # judges8 with a fake subagent: s1 drops 2 jids, its f1 drops 1 again, f2 returns it; s2 always drops 1 -> STOP
    asked = {}

    def fake(pr):
        its = [json.loads(l) for l in pr.split('Items:\n', 1)[1].splitlines() if l.strip()]
        assert pr.split('Items:\n', 1)[0] + 'Items:\n' == P.judge_prompt('es') + ('' if P.judge_prompt('es').endswith('\n') else '\n') or pr.startswith(P.judge_prompt('es'))
        asked.setdefault(its[0]['jid'], []).append(len(its))
        arr = [{'jid': it['jid'], 'label': 'correct', 'reason': 'r'} for it in its]
        pk = [p for p in range(1, 9) if its[0]['jid'] in {x['jid'] for x in W.jl(d + '/judge/packet_s%d.jsonl' % p)}]
        if pk == [1] and len(its) > 5: arr = arr[2:]
        elif pk == [1] and len(its) == 2: arr = arr[1:]
        elif pk == [2]: arr = arr[1:]
        return json.dumps(arr), 1000
    W.SUB_FAKE[0] = fake
    try:
        rc = W.judges(d, d, mock=True)
    finally:
        W.SUB_FAKE[0] = None
    summ = json.load(open(d + '/judge/JUDGES_SUMMARY.json'))
    s1 = summ['sessions']['s1']
    assert s1['ok'] and [a['sid'] for a in s1['attempts']] == ['s1', 's1_f1', 's1_f2'] and [a['asked'] for a in s1['attempts']][1:] == [2, 1]
    s2 = summ['sessions']['s2']
    assert not s2['ok'] and [a['sid'] for a in s2['attempts']] == ['s2', 's2_f1', 's2_f2'] and 'after 2 follow-ups' in s2['why']
    assert all(summ['sessions']['s%d' % i]['ok'] and len(summ['sessions']['s%d' % i]['attempts']) == 1 for i in range(3, 9))
    assert rc == 3 and os.path.exists(d + '/STOP_invalid_judges.md')
    f1 = open(d + '/judge/sessions/s1_f1/prompt.txt', encoding='utf-8').read()
    assert f1.startswith(P.judge_prompt('es')) and len([l for l in f1.split('Items:\n', 1)[1].splitlines() if l.strip()]) == 2


TESTS = [t01_prompt_derivation, t02_spec_files_match, t03_parsers, t04_row_number_429_is_not_a_rate_limit,
         t05_real_429_envelope_retries_uncounted, t06_usage_limit_envelopes_stop, t07_resume_at_zero_cost,
         t08_relative_path_refused, t09_poison_no_reference_read, t10_layer_order, t11_caps,
         t12_drop_lists_and_g22_everywhere, t13_frozen_sources_untouched, t14_subagent_transport,
         t15_es_eight_packets_and_followups]

if __name__ == '__main__':
    real = [0]
    for t in TESTS:
        run(t.__name__, t)
    for n, s, why in RESULTS:
        print('%-45s %s %s' % (n, s, why))
    npass = sum(1 for r in RESULTS if r[1] == 'PASS')
    print('RESULT %d/%d PASS; real Gemini calls: 0 (HTTP mocked); real headless sessions: 0 (spawner mocked)' % (npass, len(RESULTS)))
    sys.exit(0 if npass == len(RESULTS) else 1)
