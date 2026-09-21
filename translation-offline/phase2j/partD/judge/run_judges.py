#!/usr/bin/env python3
"""Phase 2J S7: 4 headless judge sessions over partD/judge/packet_s1..4.jsonl.
Adapted from phase2i/judge/run_judges.py. The judge prompt is READ from phase2i/judge/judge_prompt.txt and asserted
byte-identical (sha d3760e49...) - same text as 2I (owner's rules verbatim, practised structure out of scope, no reference).
Spawner = run_2j.run_session (tested: usage-limit envelope -> STOP_usage_limit.md hard stop; rate limit only from
api_error_status 429/529 / error type in the envelope; resume of finished sessions at 0 cost). opus, --max-turns 2 as 2I.
Headless token cap 450,000 for the stage by reservation (spent + in-flight estimates + est <= cap). One retry per session
(<sid>_r1) only on invalid output. Absolute paths only; relative -> REFUSED. --mock = scripted fake spawner (scratch only)."""
import argparse, json, os, re, sys, hashlib, threading, glob, types, math
P2J = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2j'
HERE = P2J + '/partD/judge'
P2I_PROMPT = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2i/judge/judge_prompt.txt'
P2I_SUMMARY = '/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase2i/judge/JUDGES_SUMMARY.json'
P2I_SHA = 'd3760e49e5f9451aa4a881c0b39825bce494eb1230ffd5386c9230f8890a1936'
sys.path.insert(0, P2J)
import run_2j as R
MODEL = 'opus'
PROMPT = open(P2I_PROMPT, encoding='utf-8').read()
assert hashlib.sha256(PROMPT.encode()).hexdigest() == P2I_SHA, 'judge prompt differs from 2I'

def packet(s):
    return [json.loads(l) for l in open(os.path.join(HERE, 'packet_s%d.jsonl' % s), encoding='utf-8')]

def full_prompt(items):
    return PROMPT + '\n'.join(json.dumps(it, ensure_ascii=False) for it in items) + '\n'

def extract_array(text):
    t = (text or '').strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', t, re.S)
    if m: t = m.group(1).strip()
    i, j = t.find('['), t.rfind(']')
    if i < 0 or j < i: raise ValueError('no array')
    return json.loads(t[i:j + 1])

def validate(arr, items):
    if not isinstance(arr, list): return 'not a list'
    want = [it['jid'] for it in items]
    got = [o.get('jid') if isinstance(o, dict) else None for o in arr]
    if len(got) != len(set(got)): return 'duplicate jid'
    if set(got) != set(want): return 'jid set mismatch (missing %d, extra %d)' % (len(set(want) - set(got)), len(set(got) - set(want)))
    for o in arr:
        if o.get('label') not in ('correct', 'wrong'): return 'bad label at %s' % o.get('jid')
        if not isinstance(o.get('reason'), str): return 'bad reason at %s' % o.get('jid')
    return None

def selftest():
    items = packet(1)
    for s in range(1, 5):
        for it in packet(s): assert set(it) == {'jid', 'slovak', 'level', 'answer', 'topic'}, it
    good = [{'jid': it['jid'], 'label': 'correct' if i % 2 else 'wrong', 'reason': 'Same meaning as the Slovak.'} for i, it in enumerate(items)]
    txt = 'Here you go:\n```json\n' + json.dumps(list(reversed(good)), ensure_ascii=False) + '\n```'
    assert validate(extract_array(txt), items) is None
    assert validate(extract_array(json.dumps(good)), items) is None
    assert 'mismatch' in validate(good[:-1], items)
    assert validate(good + [good[0]], items) == 'duplicate jid'
    bad = [dict(o) for o in good]; bad[3]['label'] = 'Correct'; assert validate(bad, items).startswith('bad label')
    bad = [dict(o) for o in good]; bad[5]['jid'] = 'jzzzzz'; assert 'mismatch' in validate(bad, items)
    try: extract_array('no json here'); raise SystemExit('selftest: extract should fail')
    except ValueError: pass
    shas = {hashlib.sha256(full_prompt(packet(s))[:len(PROMPT)].encode()).hexdigest() for s in range(1, 5)}
    assert shas == {P2I_SHA}
    assert R.USAGE_RE.search('Claude AI usage limit reached') and not R.USAGE_RE.search('[{"jid":"j00429"}]')
    print('selftest PASS (validator 7 cases, packet fields jid/slovak/level/answer/topic only, prompt sha == 2I %s)' % P2I_SHA[:8])

def spent(work):
    return sum(int(v.get('tokens') or 0) for p in glob.glob(os.path.join(work, 'sessions', '*', 'headless_ledger.json'))
               for v in json.load(open(p)).values())

def run_one(s, a, results, lock, inflight):
    items = packet(s); prompt = full_prompt(items)
    open(os.path.join(a.work_dir, 'prompt_s%d.txt' % s), 'w', encoding='utf-8').write(prompt)
    atts = []
    for sid in ('s%d' % s, 's%d_r1' % s):
        sd = os.path.join(a.work_dir, 'sessions', sid)
        d0 = R.read_json(os.path.join(sd, '%s.json' % sid), None)
        done = bool(d0 and d0.get('status') == 'ok')
        with lock:
            if not done and spent(a.work_dir) + sum(inflight.values()) + a.est > a.token_cap:
                results[s] = {'ok': False, 'why': 'token_cap reservation', 'attempts': atts}; return
            inflight[sid] = 0 if done else a.est
        try:
            d = R.run_session(sid, prompt, sd, stop_dir=a.stop_dir, model=MODEL, max_turns=2, wall=2400)
        except R.Stop as e:
            results[s] = {'ok': False, 'why': '%s: %s' % (e.kind, e.why), 'attempts': atts}; return
        finally:
            with lock: inflight.pop(sid, None)
        try:
            arr = extract_array(d.get('result')); why = validate(arr, items)
        except Exception as ex:
            arr, why = None, 'parse: %s' % ex
        atts.append({'sid': sid, 'tokens': d.get('tokens'), 'resumed': bool(d.get('resumed')), 'spawns': d.get('spawns'),
                     'num_turns': d.get('num_turns'), 'why': why})
        if not why:
            results[s] = {'ok': True, 'arr': arr, 'attempts': atts}; return
    results[s] = {'ok': False, 'why': atts[-1]['why'], 'attempts': atts}

def mock_install(mode):
    calls = {'n': 0, 'seen': set()}
    sess_of = {it['jid']: s for s in range(1, 5) for it in packet(s)}
    def fake(argv, timeout):
        calls['n'] += 1
        pr = argv[argv.index('-p') + 1]
        its = [json.loads(l) for l in pr.split('Items:\n', 1)[1].splitlines() if l.strip()]
        s = sess_of[its[0]['jid']]
        first = s not in calls['seen']; calls['seen'].add(s)
        if mode == 'usage':
            env = {'type': 'result', 'is_error': True, 'subtype': 'error', 'result': 'Claude AI usage limit reached|resets at 5pm', 'usage': {'input_tokens': 3}}
            return types.SimpleNamespace(returncode=1, stdout=json.dumps(env), stderr='')
        if s == 1 and first:
            env = {'type': 'result', 'is_error': True, 'subtype': 'error', 'api_error_status': 429, 'result': 'rate limited', 'usage': {'input_tokens': 5}}
            return types.SimpleNamespace(returncode=1, stdout=json.dumps(env), stderr='')
        arr = [{'jid': it['jid'], 'label': 'correct', 'reason': 'row 429 ok' if s == 3 else 'ok'} for it in its]
        if s == 2 and first: arr = arr[:-1]
        env = {'type': 'result', 'is_error': False, 'subtype': 'success', 'result': '```json\n%s\n```' % json.dumps(arr),
               'usage': {'input_tokens': 1000, 'output_tokens': 500}}
        return types.SimpleNamespace(returncode=0, stdout=json.dumps(env), stderr='429 in stderr is ignored')
    R.SPAWN[0] = fake; R.SLEEP_H[0] = lambda x: None; R.ENV[0] = dict(os.environ)
    return calls

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--work-dir', required=True); ap.add_argument('--stop-dir', default=P2J)
    ap.add_argument('--token-cap', type=int, default=450000); ap.add_argument('--est', type=int, default=0)
    ap.add_argument('--mock', choices=['normal', 'usage'])
    a = ap.parse_args()
    for p in (a.work_dir, a.stop_dir):
        if not os.path.isabs(p):
            print('REFUSED: relative path %r (absolute paths only)' % p); return 2
    selftest()
    if not a.est:
        S = json.load(open(P2I_SUMMARY))
        mx = max(v['tokens']['total'] for v in S['sessions'].values())
        a.est = min(int(math.ceil(mx * 1.1)), a.token_cap // 4)
    print('reservation est per session', a.est, 'cap', a.token_cap, flush=True)
    os.makedirs(a.work_dir, exist_ok=True)
    if a.mock:
        if a.work_dir.startswith(P2J) or a.stop_dir.startswith(P2J): print('REFUSED: mock into phase2j'); return 2
        calls = mock_install(a.mock)
    else:
        if a.work_dir != HERE or a.stop_dir != P2J: print('REFUSED: real run outside partD/judge'); return 2
        if os.path.exists(os.path.join(P2J, 'STOP_usage_limit.md')): print('REFUSED: STOP_usage_limit.md present'); return 2
        try: R.load_token()
        except R.Stop as e:
            open(os.path.join(P2J, 'STOP_S7.md'), 'w').write('# STOP S7\nOAuth token absent; 0 sessions spawned.\n'); return 2
    results, lock, inflight, th = {}, threading.Lock(), {}, []
    for s in range(1, 5):
        t = threading.Thread(target=run_one, args=(s, a, results, lock, inflight)); t.start(); th.append(t)
    for t in th: t.join()
    for s in range(1, 5):
        assert open(os.path.join(a.work_dir, 'prompt_s%d.txt' % s), encoding='utf-8').read()[:len(PROMPT)] == PROMPT
    open(os.path.join(a.work_dir, 'judge_prompt.txt'), 'w', encoding='utf-8').write(PROMPT)
    open(os.path.join(a.work_dir, 'PROMPT.sha256'), 'w').write('%s  judge_prompt.txt (identical prefix of prompt_s1..s4.txt; == phase2i/judge/PROMPT.sha256: %s)\n' % (P2I_SHA, 'yes'))
    summ = {'prompt_sha': P2I_SHA, 'prompt_sha_2i': P2I_SHA, 'identical_to_2i': True, 'model': MODEL, 'token_cap': a.token_cap,
            'est': a.est, 'mock': a.mock, 'headless_tokens_total_ledger': spent(a.work_dir), 'sessions': {}}
    for s in range(1, 5):
        R_ = results[s]
        summ['sessions'][s] = {'ok': R_['ok'], 'why': R_.get('why'), 'attempts': R_['attempts'],
                               'tokens_new': sum(int(x.get('tokens') or 0) for x in R_['attempts'] if not x['resumed'])}
        if R_['ok']:
            json.dump(R_['arr'], open(os.path.join(a.work_dir, 'verdicts_s%d.json' % s), 'w'), ensure_ascii=False, indent=0)
    if a.mock: summ['mock_spawns'] = calls['n']
    json.dump(summ, open(os.path.join(a.work_dir, 'JUDGES_SUMMARY.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({'ok': {s: results[s]['ok'] for s in range(1, 5)}, 'why': {s: results[s].get('why') for s in range(1, 5)},
                      'tokens_ledger': summ['headless_tokens_total_ledger'], 'mock_spawns': summ.get('mock_spawns')}), flush=True)
    return 0 if all(results[s]['ok'] for s in range(1, 5)) else 3

if __name__ == '__main__':
    sys.exit(main())
