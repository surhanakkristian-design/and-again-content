#!/usr/bin/env python3
"""Phase 2K runner (stage S1).  Tested by test_2k.py with the model mocked.
gemini  L3 transport = 2I/2J's (run_2i_base.py = byte copy of phase2j/run_2i_base.py: counted = HTTP 200 only; rate
        limit ONLY from the HTTP status / error envelope, never from reply text; daily/usage-limit envelope -> STOP;
        empty/unparsable 200 = counted failure, never retried), ONE stack: SOURCE-ONLY (stack_source.py, in-process),
        language --lang sk|cz.  Phase ledger GEMINI_LEDGER.json {stage: counted}: cap for a stage = 3,000 - every OTHER
        stage, checked before any call (counted + needed > cap -> STOP, 0 calls) and before every call.  Spend cap $1.00
        minus --spend-dirs.  Resume: finished jids skipped; stored 200 replies reused by request hash at 0 cost;
        --seed-ledger reuses another run's replies; --expect-needed N: STOP at 0 calls unless exactly N requests are new.
        Every path argument must be ABSOLUTE: a relative one is REFUSED (exit 2) before anything is opened.
claude  headless-Claude spawner = phase2j/run_2j.py lines 154-265 verbatim (2H recipe: token via zsh -ic, never
        printed; usage-limit ERROR envelope -> STOP_usage_limit.md + hard stop; rate limit only from the envelope).
  PYTHONDONTWRITEBYTECODE=1 nohup python3 -B /abs/phase2k/run_2k.py gemini --lang sk --set /abs/items.jsonl --run-dir /abs/DIR --stage S2_2i [--expect-needed N]
  python3 -B /abs/phase2k/run_2k.py claude --sid ID --prompt-file /abs/P.txt --out-dir /abs/DIR [--model opus]
"""
import argparse, json, os, random, re, subprocess, sys, time
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import run_2i_base as B                                                           # noqa: E402
import stack_source as S                                                          # noqa: E402
PHASE_CAP, PHASE_SPEND = 3000, 1.00
LEDGER = os.path.join(HERE, 'GEMINI_LEDGER.json')
Stop = B.Stop
SRC_FIELD = {'sk': 'slovak', 'cz': 'czech'}


class Refused(Exception):
    pass


def must_abs(p, what):
    if p is None:
        return
    if not isinstance(p, str) or not os.path.isabs(p):
        raise Refused('REFUSED: %s must be an absolute path, got %r' % (what, p))


def read_json(p, d):
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else d


def write_json(p, obj):
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, indent=1, sort_keys=True, ensure_ascii=False); fh.flush(); os.fsync(fh.fileno())
    os.replace(tmp, p)


def spend_of(d):
    return sum(r.get('cost_usd') or 0.0 for r in B.jl_read(os.path.join(d, 'ledger.jsonl')) if r.get('http') == 200)


def clean_item(it, lang):
    """-> {jid, sid, level, src, answer, ann}; ann = the annotation WITHOUT any reference key (values never touched)."""
    f = SRC_FIELD[lang]
    src = it[f] if f in it else it['src']
    ann = it['annotation'] if 'annotation' in it else None
    a = {k: ann[k] for k in ann if not S.is_ref(k)} if isinstance(ann, dict) else {}
    return {'jid': it['jid'], 'sid': it['sid'], 'level': it['level'], 'src': src, 'answer': it['answer'], 'ann': a}


def run_items(items, run_dir, stage, lang, seed_ledger=None, ledger_path=LEDGER, key=None, expect_needed=None,
              spend_dirs=()):
    for p, w in [(run_dir, '--run-dir'), (ledger_path, '--ledger'), (seed_ledger, '--seed-ledger')] + \
            [(d, '--spend-dirs') for d in spend_dirs]:
        must_abs(p, w)
    if lang not in S.LANG:
        raise Refused('REFUSED: --lang must be sk or cz')
    os.makedirs(run_dir, exist_ok=True)
    os.environ['P2I_RUN_DIR'] = run_dir
    P = B.paths(run_dir)
    jids = [it['jid'] for it in items]
    if len(set(jids)) != len(jids):
        raise Refused('REFUSED: duplicate jid')
    done = {r['jid'] for r in B.jl_read(P['results'])}
    todo = [it for it in items if it['jid'] not in done]
    ledger = B.jl_read(P['ledger'])
    got = {}
    for row in ledger:
        if row.get('http') == 200 and row.get('req_key') and row['req_key'] not in got:
            got[row['req_key']] = row
    if seed_ledger:
        for x in B.jl_read(seed_ledger):
            k = x.get('req_key')
            if x.get('http') == 200 and x.get('counted') and k and k not in got:
                got[k] = {'verdict': x.get('verdict'), 'failed': bool(x.get('failed')), 'reply': x.get('reply'),
                          'seeded': True}
    phase = read_json(ledger_path, {})
    others = sum(int(v) for k, v in phase.items() if k != stage)
    cap = PHASE_CAP - others
    ctx = {'P': P, 'cap': cap, 'spend_cap': PHASE_SPEND - sum(spend_of(d) for d in spend_dirs if d != run_dir),
           'key': None, 'last': 0.0, 'made': 0, 'uncounted': 0,
           'counted': sum(1 for r in ledger if r.get('http') == 200), 'spent': spend_of(run_dir), 'est': B.EST_CALL_USD}

    def sync():
        phase[stage] = ctx['counted']; write_json(ledger_path, phase)
    st = {'status': 'COMPLETE', 'stage': stage, 'lang': lang, 'stack': 'source', 'items': len(items),
          'todo_items': len(todo), 'requests': 0, 'needed': 0, 'calls_made': 0, 'stop': None,
          'phase_cap_for_stage': cap, 'other_stages_counted': others, 'mock': key == 'MOCK'}
    if todo:
        clean = [clean_item(it, lang) for it in todo]
        reqs = S.prepare(clean, lang)
        rq, users = {}, {}
        for j, q in sorted(reqs.items()):
            k = q['k'] = B.req_key(q)
            rq[k] = q
            users.setdefault(k, []).append('source:%s' % j)
        need = [k for k in sorted(rq) if k not in got]
        st.update(requests=len(reqs), unique_requests=len(rq), needed=len(need),
                  seeded_used=sum(1 for k in rq if (got.get(k) or {}).get('seeded')))
        stop = None
        if expect_needed is not None and len(need) != expect_needed:
            stop = Stop('expect', 'needed %d != expected %d; NO call was made' % (len(need), expect_needed))
        elif ctx['counted'] + len(need) > cap:
            stop = Stop('cap', 'counted %d + needed %d > phase cap for this stage %d (3,000 - other stages %d); NO call '
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
        out = S.finish(clean, lang, rep['replies'], rep['failed'])
        for c in clean:
            r = out.get(c['jid'])
            if r is None:
                continue
            q = reqs.get(c['jid'])
            row = got.get(q['k']) if q else None
            B.jl_append(P['results'], dict(r, jid=c['jid'], sid=c['sid'], level=c['level'], stack='source', lang=lang,
                                           req_key=q['k'] if q else None, seeded_reply=bool(row and row.get('seeded')),
                                           l3_raw=row.get('reply') if row else None, ts=B.now()))
    sync()
    fin = {r['jid'] for r in B.jl_read(P['results'])}
    missing = sum(1 for j in jids if j not in fin)
    if missing and st['status'] == 'COMPLETE':
        st['status'] = 'INCOMPLETE'
    st.update(calls_made=ctx['made'], uncounted_attempts=ctx['uncounted'], counted_total=ctx['counted'],
              spend_usd=round(ctx['spent'], 6), results_missing=missing, ts=B.now(), phase_ledger=dict(phase),
              poison_hits=len(S.HITS))
    write_json(P['status'], st)
    return st


def run_gemini(set_path, run_dir, stage, lang, seed_ledger=None, ledger_path=LEDGER, key=None, purpose='Phase 2K run',
               expect_needed=None, spend_dirs=()):
    must_abs(set_path, '--set'); must_abs(run_dir, '--run-dir')
    os.makedirs(run_dir, exist_ok=True)
    items = B.open_set(set_path, B.paths(run_dir), purpose)
    return run_items(items, run_dir, stage, lang, seed_ledger, ledger_path, key, expect_needed, spend_dirs)


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
    g.add_argument('--stage', required=True); g.add_argument('--lang', required=True, choices=sorted(S.LANG))
    g.add_argument('--seed-ledger'); g.add_argument('--ledger', default=LEDGER)
    g.add_argument('--expect-needed', type=int); g.add_argument('--spend-dirs', nargs='*', default=[])
    g.add_argument('--purpose', default='Phase 2K run')
    c = sp.add_parser('claude')
    c.add_argument('--sid', required=True); c.add_argument('--prompt-file', required=True)
    c.add_argument('--out-dir', required=True); c.add_argument('--model', default='opus')
    c.add_argument('--max-turns', type=int, default=12); c.add_argument('--wall', type=int, default=1800)
    c.add_argument('--token-cap', type=int); c.add_argument('--est', type=int, default=100000)
    a = ap.parse_args(argv)
    try:
        if a.cmd == 'gemini':
            for p, w in ((a.set, '--set'), (a.run_dir, '--run-dir'), (a.ledger, '--ledger'),
                         (a.seed_ledger, '--seed-ledger')):
                must_abs(p, w)
            for d in a.spend_dirs:
                must_abs(d, '--spend-dirs')
            key = None
            if os.environ.get('P2K_MOCK') == '1':
                if a.run_dir.startswith(os.path.join(HERE, 'run_')):
                    raise Refused('REFUSED: mock transport on a real run dir')
                B.HTTP[0], B.SLEEP[0], B.MIN_INTERVAL, key = _mock_http, (lambda s: None), 0, 'MOCK'
            st = run_gemini(a.set, a.run_dir, a.stage, a.lang, a.seed_ledger, a.ledger, key, a.purpose,
                            a.expect_needed, a.spend_dirs)
            print(json.dumps(st, sort_keys=True))
            return 0 if st['status'] == 'COMPLETE' else 3
        must_abs(a.prompt_file, '--prompt-file'); must_abs(a.out_dir, '--out-dir')
        prompt = open(a.prompt_file, encoding='utf-8').read()
        d = run_session(a.sid, prompt, a.out_dir, model=a.model, max_turns=a.max_turns, wall=a.wall,
                        token_cap=a.token_cap, est=a.est)
        print(json.dumps({k: d.get(k) for k in ('sid', 'status', 'tokens', 'attempts', 'resumed')}))
        return 0
    except Refused as e:
        print(json.dumps({'status': 'REFUSED', 'why': str(e)}))
        return 2
    except Stop as e:
        print(json.dumps({'status': 'STOPPED', 'kind': e.kind, 'why': e.why}))
        return 4


if __name__ == '__main__':
    sys.exit(main())
