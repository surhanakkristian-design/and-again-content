#!/usr/bin/env python3
"""Phase 2I runner: every item through BOTH stacks (tonly = TRANSLATION-ONLY, frozen = 1W), one L3 model
(gemini-3.1-flash-lite, temperature 0, thinkingBudget 0 - the stacks' own GEN_CFG, sent verbatim).

Transport (brief section 3, 2H pattern): counted = HTTP 200 only.  A rate limit is recognised ONLY from the HTTP
status or the API error envelope, never from reply text.  HTTP 0/429/5xx -> retry with backoff, logged
counted:false.  A daily/usage-limit quota envelope (QuotaFailure quotaId/metric or envelope message saying per-day /
daily / usage limit / spending cap) -> clean STOP.  An empty or unparsable 200 = FAILED call: recorded, counted,
never retried, never guessed (the item is decided with no verdict -> rejected, call_failed:true).
HARD CAP 2,000 counted calls (checked before any call: counted + needed > cap -> STOP, 0 calls; and before every
call).  Spend stop at $1.00 (0.25 $/M in, 1.50 $/M out incl. thinking, as phase1k/runner_1k.py priced the model).
Files (run dir): ledger.jsonl (every HTTP attempt), results.jsonl (one line per jid+stack; resume skips them),
access_log.jsonl (every open of the set file), RUN_STATUS.json, STOP_<kind>.md, stack_<name>.log, _io/.
Identical requests (same system+user+config) are called once and shared (shared_call:true in results).
    PYTHONDONTWRITEBYTECODE=1 nohup python3 -B phase2i/run_2i.py --set SET.jsonl [--run-dir phase2i/run]
"""
import argparse, datetime, hashlib, json, os, random, re, subprocess, sys, time, urllib.error, urllib.request
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
RUN_DIR = os.path.join(HERE, 'run')
MODEL = 'gemini-3.1-flash-lite'
API = 'https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent'
PRICE_IN, PRICE_OUT = 0.25 / 1e6, 1.50 / 1e6
CAP, SPEND_CAP, TRIES, MIN_INTERVAL, EST_CALL_USD = 2000, 1.00, 6, 0.30, 0.0005
STACKS = ('tonly', 'frozen')
STACK_FILE = {'tonly': os.path.join(HERE, 'stack_tonly.py'), 'frozen': os.path.join(HERE, 'stack_frozen.py')}
ENV_FILE = os.path.expanduser('~/Projects/and-again/.env.local')
VERDICTS = ('SAME', 'TIP', 'DIFF')
PASS_KEYS = ('jid', 'sid', 'level', 'slovak', 'topic', 'answer', 'annotation')
DAILY_RE = re.compile(r'per.?day|daily|usage.?limit|spend(ing)?.?cap', re.I)
HTTP, SLEEP = [None], [time.sleep]


class Stop(Exception):
    def __init__(self, kind, why):
        Exception.__init__(self, '%s: %s' % (kind, why))
        self.kind, self.why = kind, why


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')


def jl_append(path, row):
    with open(path, 'a', encoding='utf-8') as fh:
        fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n')
        fh.flush(); os.fsync(fh.fileno())


def jl_read(path):
    out = []
    if os.path.exists(path):
        for ln in open(path, encoding='utf-8'):
            ln = ln.strip()
            if ln:
                try:
                    out.append(json.loads(ln))
                except Exception:
                    pass
    return out


def load_key():
    """As phase1n/runner_1l.load_keys()[0]: GEMINI_API_KEY_FREE / _FREETIER first, else lib_prev.load_key()
    (first line starting GEMINI_API_KEY).  Never printed; redacted in every logged error."""
    lines = [l.strip() for l in open(ENV_FILE, encoding='utf-8')]
    val = lambda l: l.split('=', 1)[1].strip().strip('"').strip("'") if '=' in l else ''
    keys = [val(l) for l in lines for n in ('GEMINI_API_KEY_FREE', 'GEMINI_API_KEY_FREETIER')
            if l.startswith(n) and val(l)]
    d = next((val(l) for l in lines if l.startswith('GEMINI_API_KEY') and val(l)), None)
    if d and d not in keys:
        keys.append(d)
    if not keys:
        raise Stop('auth', 'no GEMINI_API_KEY in %s' % ENV_FILE)
    return keys[0]


def redact(s, key):
    s = '' if s is None else str(s)
    return s.replace(key, '[REDACTED]') if key else s


def http_post(url, body, key, timeout=60):
    req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'), method='POST',
                                 headers={'Content-Type': 'application/json', 'x-goog-api-key': key})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            code, raw = r.status, r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError as e:
        code = e.code
        try:
            raw = e.read().decode('utf-8', 'replace')
        except Exception:
            raw = ''
    except Exception as e:
        return 0, None, '%s: %s' % (type(e).__name__, e)
    try:
        js = json.loads(raw)
    except Exception:
        js = None
    return code, js, raw


HTTP[0] = http_post


def envelope_error(js):
    if isinstance(js, list) and js:
        js = js[0]
    if isinstance(js, dict) and isinstance(js.get('error'), dict):
        return js['error']
    return None


def classify(code, js):
    """From the HTTP status and the API error ENVELOPE only - reply text is never looked at."""
    if code == 200:
        return 'ok'
    err = envelope_error(js) or {}
    if code == 429 or err.get('status') == 'RESOURCE_EXHAUSTED' or err.get('code') == 429:
        ids = [str(v.get('quotaId', '')) + ' ' + str(v.get('quotaMetric', ''))
               for d in (err.get('details') or []) if isinstance(d, dict)
               for v in (d.get('violations') or []) if isinstance(v, dict)]
        if any(DAILY_RE.search(x) for x in ids) or DAILY_RE.search(str(err.get('message') or '')):
            return 'quota'
        return 'retry'
    if code == 0 or 500 <= int(code) <= 599:
        return 'retry'
    if code in (401, 403):
        return 'auth'
    return 'fatal'


def parse_reply(text):
    m = re.fullmatch(r'[\s\W_]*(SAME|TIP|DIFF)[\s\W_]*', (text or '').strip(), re.I)
    return m.group(1).upper() if m else None


def req_key(q):
    return hashlib.sha256(json.dumps([q['sys'], q['user'], q['gcfg']], sort_keys=True,
                                     ensure_ascii=False).encode('utf-8')).hexdigest()


def paths(d):
    return {'dir': d, 'ledger': os.path.join(d, 'ledger.jsonl'), 'results': os.path.join(d, 'results.jsonl'),
            'access': os.path.join(d, 'access_log.jsonl'), 'status': os.path.join(d, 'RUN_STATUS.json'),
            'io': os.path.join(d, '_io')}


def open_set(path, P, purpose):
    with open(path, 'rb') as fh:
        data = fh.read()
    jl_append(P['access'], {'ts': now(), 'path': os.path.abspath(path), 'bytes': len(data),
                            'sha256': hashlib.sha256(data).hexdigest(), 'purpose': purpose, 'pid': os.getpid(),
                            'argv': sys.argv[1:]})
    return [json.loads(l) for l in data.decode('utf-8').splitlines() if l.strip()]


def strip_lk(a):
    b = {k: v for k, v in a.items() if not (k == 'lk' or str(k).startswith('lk_'))}
    for sub in ('hygienised', 'raw'):
        if isinstance(b.get(sub), dict):
            b[sub] = {k: v for k, v in b[sub].items() if not (k == 'lk' or str(k).startswith('lk_'))}
    return b


def clean_item(it, stack):
    from_flat = 'annotation' not in it
    out = {k: it[k] for k in PASS_KEYS if k in it}
    if from_flat:
        sys.path.insert(0, HERE)
        import stack_frozen as SF                   # ANN_FIELDS only; importing it loads no chain
        out['annotation'] = {f: it[f] for f in SF.ANN_FIELDS if f in it}
    if stack == 'tonly':
        out['annotation'] = strip_lk(out['annotation'])
    return out


def stack_call(s, cmd, items, P, rep=None):
    os.makedirs(P['io'], exist_ok=True)
    fin = os.path.join(P['io'], '%s_%s_items.json' % (s, cmd))
    json.dump(items, open(fin, 'w', encoding='utf-8'), ensure_ascii=False)
    args = [sys.executable, '-B', STACK_FILE[s], cmd, fin]
    if rep is not None:
        frep = os.path.join(P['io'], '%s_replies.json' % s)
        json.dump(rep, open(frep, 'w', encoding='utf-8'), ensure_ascii=False)
        args.append(frep)
    fout = os.path.join(P['io'], '%s_%s_out.json' % (s, cmd))
    args.append(fout)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', P2I_RUN_DIR=P['dir'])
    env.pop('TONLY_POISON', None)
    p = subprocess.run(args, env=env, capture_output=True, text=True, timeout=3600, cwd=HERE)
    with open(os.path.join(P['dir'], 'stack_%s.log' % s), 'a', encoding='utf-8') as fh:
        fh.write('=== %s %s rc=%s\n%s\n' % (now(), cmd, p.returncode, p.stderr[-20000:]))
    if p.returncode != 0:
        raise RuntimeError('stack %s %s failed rc=%s: %s' % (s, cmd, p.returncode, p.stderr[-3000:]))
    return json.load(open(fout, encoding='utf-8'))


def call_one(ctx, k, q, users):
    body = {'systemInstruction': {'parts': [{'text': q['sys']}]},
            'contents': [{'role': 'user', 'parts': [{'text': q['user']}]}], 'generationConfig': q['gcfg']}
    delay, key = 2.0, ctx['key']
    for attempt in range(1, TRIES + 1):
        if ctx['counted'] >= ctx['cap']:
            raise Stop('cap', 'counted %d reached the hard cap %d' % (ctx['counted'], ctx['cap']))
        if ctx['spent'] + ctx['est'] > ctx['spend_cap']:
            raise Stop('spend', 'spent $%.6f + next ~$%.6f > $%.2f' % (ctx['spent'], ctx['est'], ctx['spend_cap']))
        wait = ctx['last'] + MIN_INTERVAL - time.time()
        if wait > 0:
            SLEEP[0](wait)
        t0 = time.time()
        code, js, raw = HTTP[0](API % MODEL, body, key)
        ctx['last'] = time.time()
        base = {'ts': now(), 'req_key': k, 'model': MODEL, 'users': users, 'try': attempt,
                'latency_ms': int((time.time() - t0) * 1000)}
        if code == 200:
            cands = (js.get('candidates') or []) if isinstance(js, dict) else []
            text = ''.join(p.get('text', '') or '' for c in cands if isinstance(c, dict)
                           for p in ((c.get('content') or {}).get('parts') or []) if isinstance(p, dict))
            um = (js.get('usageMetadata') or {}) if isinstance(js, dict) else {}
            tin = int(um.get('promptTokenCount') or 0)
            tout = int(um.get('candidatesTokenCount') or 0) + int(um.get('thoughtsTokenCount') or 0)
            cost = tin * PRICE_IN + tout * PRICE_OUT
            v = parse_reply(text)
            row = dict(base, http=200, counted=True, reply=text[:500], verdict=v or 'FAILED', failed=v is None,
                       why=None if v else ('empty 200 reply' if not text.strip() else 'unparsable 200 reply'),
                       finish=(cands[0].get('finishReason') if cands and isinstance(cands[0], dict) else None),
                       tokens_in=tin, tokens_out=tout, cost_usd=round(cost, 8))
            jl_append(ctx['P']['ledger'], row)
            ctx['counted'] += 1; ctx['made'] += 1; ctx['spent'] += cost
            ctx['est'] = max(EST_CALL_USD, 2.0 * ctx['spent'] / max(1, ctx['made']))
            return row
        kind = classify(code, js)
        err = envelope_error(js) or {}
        jl_append(ctx['P']['ledger'], dict(base, http=code, counted=False, kind=kind,
                                           error_status=err.get('status'), error=redact(raw, key)[:800],
                                           transport_retry=(kind == 'retry')))
        ctx['uncounted'] += 1
        if kind == 'quota':
            raise Stop('quota', 'HTTP %s %s: %s' % (code, err.get('status'), redact(err.get('message'), key)[:300]))
        if kind == 'auth':
            raise Stop('auth', 'HTTP %s: the key was rejected' % code)
        if kind == 'fatal':
            raise Stop('http_%s' % code, redact(raw, key)[:300])
        if attempt == TRIES:
            raise Stop('rate_wall', '%d consecutive retryable failures (last HTTP %s)' % (TRIES, code))
        SLEEP[0](min(60.0, delay) * (1.0 + random.random() * 0.3))
        delay *= 2


def run(set_path, run_dir=RUN_DIR, cap=CAP, spend_cap=SPEND_CAP, key=None, purpose='Phase 2I run'):
    os.makedirs(run_dir, exist_ok=True)
    P = paths(run_dir)
    items = open_set(set_path, P, purpose)
    jids = [it['jid'] for it in items]
    if len(set(jids)) != len(jids):
        raise SystemExit('REFUSED: duplicate jid in %s' % set_path)
    done = {(r['jid'], r['stack']) for r in jl_read(P['results'])}
    todo = [it for it in items if any((it['jid'], s) not in done for s in STACKS)]
    ledger = jl_read(P['ledger'])
    got = {}
    for row in ledger:
        if row.get('http') == 200 and row.get('req_key') and row['req_key'] not in got:
            got[row['req_key']] = row
    ctx = {'P': P, 'cap': cap, 'spend_cap': spend_cap, 'key': None, 'last': 0.0, 'made': 0, 'uncounted': 0,
           'counted': sum(1 for r in ledger if r.get('http') == 200),
           'spent': sum(r.get('cost_usd') or 0.0 for r in ledger if r.get('http') == 200), 'est': EST_CALL_USD}
    st = {'status': 'COMPLETE', 'items': len(items), 'todo_items': len(todo), 'requests': 0, 'needed': 0,
          'calls_made': 0, 'stop': None, 'shared_requests': 0}
    if todo:
        clean = {s: [clean_item(it, s) for it in todo] for s in STACKS}
        reqs = {s: stack_call(s, 'prepare', clean[s], P) for s in STACKS}
        rq, users = {}, {}
        for s in STACKS:
            for j, q in sorted(reqs[s].items()):
                k = q['k'] = req_key(q)
                rq[k] = q
                users.setdefault(k, []).append('%s:%s' % (s, j))
        shared = {k for k, u in users.items() if len({x.split(':', 1)[0] for x in u}) > 1}
        need = [k for k in sorted(rq) if k not in got]
        st.update(requests=len(rq), needed=len(need), shared_requests=len(shared))
        stop = None
        if ctx['counted'] + len(need) > cap:
            stop = Stop('cap', 'counted %d + needed %d = %d > hard cap %d; NO call was made'
                        % (ctx['counted'], len(need), ctx['counted'] + len(need), cap))
        elif need:
            try:
                ctx['key'] = key or load_key()
                for k in need:
                    got[k] = call_one(ctx, k, rq[k], users[k])
            except Stop as e:
                stop = e
        if stop:
            st.update(status='STOPPED', stop={'kind': stop.kind, 'why': stop.why})
            open(os.path.join(run_dir, 'STOP_%s.md' % stop.kind), 'w', encoding='utf-8').write(
                '# STOP (%s)\n\n%s\n\n%s. Counted calls %d, spend $%.6f. Resume with the same command: every stored '
                '200 reply is reused, finished items are skipped.\n' % (stop.kind, stop.why, now(), ctx['counted'],
                                                                        ctx['spent']))
        for s in STACKS:
            todo_s = [c for c in clean[s] if (c['jid'], s) not in done]
            rep = {'replies': {}, 'failed': []}
            for j, q in reqs[s].items():
                row = got.get(q['k'])
                if row is not None:
                    if row.get('failed'):
                        rep['failed'].append(j)
                    else:
                        rep['replies'][j] = row['verdict']
            out = stack_call(s, 'finish', todo_s, P, rep)
            for c in todo_s:
                r = out.get(c['jid'])
                if r is None:
                    continue                                  # its L3 call is still pending
                q = reqs[s].get(c['jid'])
                row = got.get(q['k']) if q else None
                jl_append(P['results'], dict(r, jid=c['jid'], sid=c['sid'], level=c['level'], stack=s,
                                             req_key=q['k'] if q else None, shared_call=bool(q and q['k'] in shared),
                                             l3_raw=row.get('reply') if row else None, ts=now()))
    fin = {(r['jid'], r['stack']) for r in jl_read(P['results'])}
    missing = sum(1 for j in jids for s in STACKS if (j, s) not in fin)
    if missing and st['status'] == 'COMPLETE':
        st['status'] = 'INCOMPLETE'
    st.update(calls_made=ctx['made'], uncounted_attempts=ctx['uncounted'], counted_total=ctx['counted'],
              spend_usd=round(ctx['spent'], 6), results_missing=missing, ts=now(),
              failed_calls_total=sum(1 for r in jl_read(P['ledger']) if r.get('http') == 200 and r.get('failed')))
    json.dump(st, open(P['status'], 'w', encoding='utf-8'), indent=1, sort_keys=True)
    return st


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--set', required=True)
    ap.add_argument('--run-dir', default=RUN_DIR)
    ap.add_argument('--cap', type=int, default=CAP)
    ap.add_argument('--spend-cap', type=float, default=SPEND_CAP)
    ap.add_argument('--purpose', default='Phase 2I final run')
    a = ap.parse_args()
    if a.cap > CAP or a.spend_cap > SPEND_CAP:
        raise SystemExit('REFUSED: caps may only be lowered')
    st = run(a.set, a.run_dir, a.cap, a.spend_cap, purpose=a.purpose)
    print(json.dumps(st, sort_keys=True))
    return 0 if st['status'] == 'COMPLETE' else 3


if __name__ == '__main__':
    sys.exit(main())
