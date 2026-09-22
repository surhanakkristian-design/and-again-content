#!/usr/bin/env python3
"""Phase 2J runner (stage S2).  Two transports, both tested by test_2j.py with the model mocked.

gemini  L3 transport = Phase 2I's (run_2i_base.py is a byte copy of phase2i/run_2i.py: http_post, classify,
        call_one - counted = HTTP 200 only; rate limit ONLY from HTTP status / error envelope; daily/usage quota
        envelope -> STOP; empty/unparsable 200 = counted failure, never retried), ONE stack: the fixed
        TRANSLATION-ONLY stack (phase2j/stack_tonly.py, P2J_F4FIX=1 enforced).  Phase ledger GEMINI_LEDGER.json
        {stage: counted}: the cap for a stage = 1,200 - every OTHER stage's counted calls; checked before any call
        (counted + needed > cap -> STOP, 0 calls) and before every call.  Spend cap $1.00 minus the other stages'
        spend (--spend-dirs).  --seed-ledger: stored 200 replies of an earlier run reused by request hash at
        0 cost (not counted).  --expect-needed N: STOP at 0 calls unless exactly N requests are new.
        Every path is made absolute first (2I's first set open crashed on a relative --run-dir).
claude  headless-Claude spawner, 2H/2I recipe: bundled binary, token via `zsh -ic` (never printed), -p PROMPT
        --output-format json --max-turns N --model M; usage from the envelope; usage-limit/quota ERROR envelope ->
        STOP_usage_limit.md + hard stop; rate limit only from api_error_status 429/529 or error type
        rate_limit_error/overloaded_error (a '429' in the result text or stderr is never looked at); resume skips
        finished sessions at 0 cost; per-out-dir token ledger with a reservation check.
  PYTHONDONTWRITEBYTECODE=1 nohup python3 -B /abs/phase2j/run_2j.py gemini --set /abs/SET.jsonl --run-dir /abs/DIR --stage S2
  python3 -B /abs/phase2j/run_2j.py claude --sid ID --prompt-file /abs/P.txt --out-dir /abs/DIR [--model opus]
"""
import argparse, json, os, random, re, subprocess, sys, time
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import run_2i_base as B                                                           # noqa: E402
B.STACKS = ('tonly',)
B.STACK_FILE = {'tonly': os.path.join(HERE, 'stack_tonly.py')}
PHASE_CAP, PHASE_SPEND = 1200, 1.00
LEDGER = os.path.join(HERE, 'GEMINI_LEDGER.json')
Stop = B.Stop
VERD = B.VERDICTS


def read_json(p, d):
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else d


def write_json(p, obj):
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, indent=1, sort_keys=True, ensure_ascii=False); fh.flush(); os.fsync(fh.fileno())
    os.replace(tmp, p)


def spend_of(d):
    return sum(r.get('cost_usd') or 0.0 for r in B.jl_read(os.path.join(d, 'ledger.jsonl')) if r.get('http') == 200)


def run_gemini(set_path, run_dir, stage, seed_ledger=None, ledger_path=LEDGER, key=None, purpose='Phase 2J',
               expect_needed=None, spend_dirs=()):
    set_path, run_dir, ledger_path = (os.path.abspath(x) for x in (set_path, run_dir, ledger_path))
    if os.environ.get('P2J_F4FIX', '1') != '1':
        raise SystemExit('REFUSED: the 2J stack runs with the A2 fix (P2J_F4FIX=1)')
    os.environ['P2J_F4FIX'] = '1'
    os.makedirs(run_dir, exist_ok=True)
    P = B.paths(run_dir)
    items = B.open_set(set_path, P, purpose)
    jids = [it['jid'] for it in items]
    if len(set(jids)) != len(jids):
        raise SystemExit('REFUSED: duplicate jid in %s' % set_path)
    done = {r['jid'] for r in B.jl_read(P['results'])}
    todo = [it for it in items if it['jid'] not in done]
    ledger = B.jl_read(P['ledger'])
    got = {}
    for row in ledger:
        if row.get('http') == 200 and row.get('req_key') and row['req_key'] not in got:
            got[row['req_key']] = row
    if seed_ledger:
        for x in B.jl_read(os.path.abspath(seed_ledger)):
            k = x.get('req_key')
            if x.get('http') == 200 and x.get('counted') and k and k not in got:
                got[k] = {'verdict': x.get('verdict'), 'failed': bool(x.get('failed')), 'reply': x.get('reply'),
                          'seeded': True}
    phase = read_json(ledger_path, {})
    others = sum(int(v) for k, v in phase.items() if k != stage)
    cap = PHASE_CAP - others
    ctx = {'P': P, 'cap': cap, 'spend_cap': PHASE_SPEND - sum(spend_of(os.path.abspath(d)) for d in spend_dirs
                                                               if os.path.abspath(d) != run_dir),
           'key': None, 'last': 0.0, 'made': 0, 'uncounted': 0,
           'counted': sum(1 for r in ledger if r.get('http') == 200), 'spent': spend_of(run_dir), 'est': B.EST_CALL_USD}

    def sync():
        phase[stage] = ctx['counted']; write_json(ledger_path, phase)
    st = {'status': 'COMPLETE', 'stage': stage, 'items': len(items), 'todo_items': len(todo), 'requests': 0,
          'needed': 0, 'calls_made': 0, 'stop': None, 'phase_cap_for_stage': cap, 'other_stages_counted': others,
          'mock': bool(os.environ.get('P2J_MOCK'))}
    if todo:
        clean = [B.clean_item(it, 'tonly') for it in todo]
        reqs = B.stack_call('tonly', 'prepare', clean, P)
        rq, users = {}, {}
        for j, q in sorted(reqs.items()):
            k = q['k'] = B.req_key(q)
            rq[k] = q
            users.setdefault(k, []).append('tonly:%s' % j)
        need = [k for k in sorted(rq) if k not in got]
        st.update(requests=len(rq), needed=len(need), seeded_used=sum(1 for k in rq if (got.get(k) or {}).get('seeded')),
                  needed_jids=sorted(j for j, q in reqs.items() if q['k'] in set(need)))
        stop = None
        if expect_needed is not None and len(need) != expect_needed:
            stop = Stop('expect', 'needed %d != expected %d; NO call was made' % (len(need), expect_needed))
        elif ctx['counted'] + len(need) > cap:
            stop = Stop('cap', 'counted %d + needed %d > phase cap for this stage %d (1,200 - other stages %d); NO call '
                        'was made' % (ctx['counted'], len(need), cap, others))
        elif need:
            try:
                ctx['key'] = key or B.load_key()
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
        rep = {'replies': {}, 'failed': []}
        for j, q in reqs.items():
            row = got.get(q['k'])
            if row is not None:
                if row.get('failed'):
                    rep['failed'].append(j)
                else:
                    rep['replies'][j] = row['verdict']
        out = B.stack_call('tonly', 'finish', clean, P, rep)
        for c in clean:
            r = out.get(c['jid'])
            if r is None:
                continue
            q = reqs.get(c['jid'])
            row = got.get(q['k']) if q else None
            B.jl_append(P['results'], dict(r, jid=c['jid'], sid=c['sid'], level=c['level'], stack='tonly',
                                           req_key=q['k'] if q else None, seeded_reply=bool(row and row.get('seeded')),
                                           l3_raw=row.get('reply') if row else None, ts=B.now()))
    sync()
    fin = {r['jid'] for r in B.jl_read(P['results'])}
    missing = sum(1 for j in jids if j not in fin)
    if missing and st['status'] == 'COMPLETE':
        st['status'] = 'INCOMPLETE'
    st.update(calls_made=ctx['made'], uncounted_attempts=ctx['uncounted'], counted_total=ctx['counted'],
              spend_usd=round(ctx['spent'], 6), results_missing=missing, ts=B.now(), phase_ledger=dict(phase))
    write_json(P['status'], st)
    return st


def _mock_http(url, body, key):
    js = {'candidates': [{'content': {'parts': [{'text': 'SAME'}]}, 'finishReason': 'STOP'}],
          'usageMetadata': {'promptTokenCount': 100, 'candidatesTokenCount': 1}}
    return 200, js, json.dumps(js)


# ---------------------------------------------------------------- headless Claude (2H recipe)
BIN = os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude')
USAGE_RE = re.compile(r'usage limit|hit your limit|weekly limit|5-hour limit|out of extra usage|credit balance is too low|'
                      r'limit will reset|resets at|quota', re.I)
ENV, SLEEP_H = [None], [time.sleep]


def redact(s):
    return re.sub(r'sk-ant-[A-Za-z0-9_\-]+', '[REDACTED]', '' if s is None else str(s))


def load_token():
    p = subprocess.run(['zsh', '-ic', 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True,
                       timeout=60, stdin=subprocess.DEVNULL)
    tok = (p.stdout or '').strip()
    if not tok.startswith('sk-ant-'):
        raise Stop('headless_auth', 'CLAUDE_CODE_OAUTH_TOKEN ABSENT')
    ENV[0] = dict(os.environ, CLAUDE_CODE_OAUTH_TOKEN=tok)
    return 'present'


def build_argv(prompt, model, max_turns):
    return [BIN, '-p', prompt, '--output-format', 'json', '--max-turns', str(int(max_turns)), '--model', model]


def _spawn(argv, timeout):
    return subprocess.run(argv, env=ENV[0], capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)


SPAWN = [_spawn]


def parse_envelope(stdout):
    s = (stdout or '').strip()
    for cand in [s] + s.splitlines()[::-1]:
        try:
            js = json.loads(cand)
            if isinstance(js, dict):
                return js
        except Exception:
            pass
    return None


def usage_total(env):
    u = (env or {}).get('usage') or {}
    return sum(int(u.get(k) or 0) for k in ('input_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens',
                                            'output_tokens'))


def classify_headless(rc, stdout, stderr):
    """From the JSON envelope only; stdout text outside the envelope and stderr are never searched."""
    env = parse_envelope(stdout)
    if env is None:
        return 'fail', None, 'no JSON envelope (rc=%s)' % rc
    is_err = bool(env.get('is_error')) or str(env.get('subtype') or '').startswith('error') or rc != 0
    if not is_err:
        return 'ok', env, ''
    err = env.get('error')
    errd = err if isinstance(err, dict) else {}
    msg = ' '.join(str(x) for x in ((errd.get('message') if errd else err), env.get('result')) if x)
    if USAGE_RE.search(msg):
        return 'usage', env, msg
    try:
        status = int(env.get('api_error_status') or errd.get('status') or 0)
    except Exception:
        status = 0
    if status in (429, 529) or (errd.get('type') or '') in ('rate_limit_error', 'overloaded_error'):
        return 'rate', env, msg
    return 'fail', env, msg


def run_session(sid, prompt, out_dir, stop_dir=HERE, model='opus', max_turns=12, wall=1800, token_cap=None,
                est=100000, tries=5):
    out_dir, stop_dir = os.path.abspath(out_dir), os.path.abspath(stop_dir)
    os.makedirs(out_dir, exist_ok=True)
    f = os.path.join(out_dir, '%s.json' % sid)
    d = read_json(f, None)
    if d and d.get('status') == 'ok':
        return dict(d, resumed=True, spawns=0)
    if os.path.exists(os.path.join(stop_dir, 'STOP_usage_limit.md')):
        raise Stop('usage_limit', 'STOP_usage_limit.md present')
    led = os.path.join(out_dir, 'headless_ledger.json')
    L = read_json(led, {})
    used = sum(int(v.get('tokens') or 0) for v in L.values())
    if token_cap is not None and used + est > token_cap:
        raise Stop('token_cap', 'used %d + reservation %d > cap %d' % (used, est, token_cap))
    if ENV[0] is None:
        load_token()
    for attempt in range(1, tries + 1):
        t0 = time.time()
        try:
            p = SPAWN[0](build_argv(prompt, model, max_turns), wall)
        except subprocess.TimeoutExpired:
            raise Stop('headless_timeout', 'session %s exceeded %ss' % (sid, wall))
        kind, env, msg = classify_headless(p.returncode, p.stdout, p.stderr)
        tok = usage_total(env)
        L['%s#%d' % (sid, attempt)] = {'tokens': tok, 'kind': kind, 'ts': B.now(), 'secs': round(time.time() - t0, 1)}
        write_json(led, L)
        if kind == 'ok':
            d = {'sid': sid, 'status': 'ok', 'result': env.get('result'), 'tokens': tok, 'usage': env.get('usage'),
                 'num_turns': env.get('num_turns'), 'attempts': attempt, 'model': model, 'ts': B.now()}
            write_json(f, d)
            return dict(d, spawns=attempt)
        if kind == 'usage':
            open(os.path.join(stop_dir, 'STOP_usage_limit.md'), 'w', encoding='utf-8').write(
                '# STOP usage limit\n\n%s session %s: %s\n' % (B.now(), sid, redact(msg)[:500]))
            raise Stop('usage_limit', redact(msg)[:300])
        if kind == 'rate' and attempt < tries:
            SLEEP_H[0](min(600.0, 30.0 * 2 ** (attempt - 1)) * (1.0 + random.random() * 0.3))
            continue
        raise Stop('headless_failed', 'session %s %s: %s' % (sid, kind, redact(msg)[:300]))


def main(argv=None):
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    g = sp.add_parser('gemini')
    g.add_argument('--set', required=True); g.add_argument('--run-dir', required=True)
    g.add_argument('--stage', required=True); g.add_argument('--seed-ledger'); g.add_argument('--ledger', default=LEDGER)
    g.add_argument('--expect-needed', type=int); g.add_argument('--spend-dirs', nargs='*', default=[])
    g.add_argument('--purpose', default='Phase 2J run')
    c = sp.add_parser('claude')
    c.add_argument('--sid', required=True); c.add_argument('--prompt-file', required=True)
    c.add_argument('--out-dir', required=True); c.add_argument('--model', default='opus')
    c.add_argument('--max-turns', type=int, default=12); c.add_argument('--wall', type=int, default=1800)
    c.add_argument('--token-cap', type=int); c.add_argument('--est', type=int, default=100000)
    a = ap.parse_args(argv)
    try:
        if a.cmd == 'gemini':
            rd = os.path.abspath(a.run_dir)
            key = None
            if os.environ.get('P2J_MOCK') == '1':
                if rd.startswith(os.path.join(HERE, 'run_')):
                    raise SystemExit('REFUSED: mock transport on a real run dir')
                B.HTTP[0], B.SLEEP[0], B.MIN_INTERVAL, key = _mock_http, (lambda s: None), 0, 'MOCK'
            st = run_gemini(a.set, rd, a.stage, a.seed_ledger, a.ledger, key, a.purpose, a.expect_needed, a.spend_dirs)
            print(json.dumps(st, sort_keys=True))
            return 0 if st['status'] == 'COMPLETE' else 3
        prompt = open(os.path.abspath(a.prompt_file), encoding='utf-8').read()
        d = run_session(a.sid, prompt, a.out_dir, model=a.model, max_turns=a.max_turns, wall=a.wall,
                        token_cap=a.token_cap, est=a.est)
        print(json.dumps({k: d.get(k) for k in ('sid', 'status', 'tokens', 'attempts', 'resumed')}))
        return 0
    except Stop as e:
        print(json.dumps({'status': 'STOPPED', 'kind': e.kind, 'why': e.why}))
        return 4


if __name__ == '__main__':
    sys.exit(main())
