#!/usr/bin/env python3
"""Phase 2I stage 4: 4 headless judge sessions (2H recipe: zsh -ic OAuth, never printed; opus; -p single shot,
--output-format json, --max-turns 2, no tools). ONE prompt, byte-identical across sessions; packet appended as data.
Cap 400,000 tokens per session (reservation before spawn; a session over cap -> STOP, no retry).
Usage-limit/quota (envelope error only) -> STOP_stage4.md at once. Rate limit only from api_error_status 429/529 or
error type. A failed/unparsable session is retried at most once, only if cumulative + 400k stays <= 3,000,000.
`python3 run_judges.py selftest` tests the validator on synthetic replies (must pass before any spawn)."""
import json, os, re, sys, time, random, hashlib, subprocess, threading
HERE = os.path.dirname(os.path.abspath(__file__))
P2I = os.path.dirname(HERE)
BIN = os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude')
MODEL = 'opus'
WALL_CAP_S = 2400
SESSION_CAP = 400000
BUDGET = 3000000
CUM_BEFORE = 829126 + 60000   # stages 1-3 + this stage's agent (estimate)
SESS = os.path.join(HERE, 'sessions'); os.makedirs(SESS, exist_ok=True)
STOP = os.path.join(P2I, 'STOP_stage4.md')
USAGE_RE = re.compile(r'usage limit|hit your limit|weekly limit|5-hour limit|out of extra usage|credit balance is too low|limit will reset|resets at|quota', re.I)

PROMPT = """You are the judge for a translation-checking test set. Do not use any tools. Reply with JSON only.

Each line below is one learner answer, as JSON: an item id (jid), a Slovak sentence, its CEFR level, the exercise topic, and the learner's English translation (answer). For every item decide ONE question: is this correct English that means what the Slovak means?

The owner's rules (apply them exactly):
- The Slovak is the ground truth, not the English reference.
- Any correct English with the same meaning is correct regardless of the grammar structure used.
- A passive is acceptable.
- A passive that drops an agent the Slovak names is WRONG.
- A missing obligatory English article is an ERROR while the CHOICE of article is free.
- The time frame must match the Slovak while the English tense inside it is free.
- A dropped function word is correct, a dropped content word is wrong, added content is wrong.

OUT OF SCOPE: the practised structure. The topic tells you which grammar the exercise practises; it does NOT matter whether the answer uses that grammar. Never mark an answer wrong because it does not use the practised structure. There is no English reference; judge against the Slovak only.

Label each item "correct" or "wrong", with a reason of at most 12 words. Judge every item independently.

Output: one JSON array with exactly one object per item, every jid exactly once, exactly this shape:
[{"jid": "...", "label": "correct", "reason": "..."}]

Items:
"""

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
    """None if valid; else the reason. Every jid exactly once, labels in {correct, wrong}."""
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
    good = [{'jid': it['jid'], 'label': 'correct' if i % 2 else 'wrong', 'reason': 'Same meaning as the Slovak.'} for i, it in enumerate(items)]
    txt = 'Here you go:\n```json\n' + json.dumps(list(reversed(good)), ensure_ascii=False) + '\n```'
    assert validate(extract_array(txt), items) is None, validate(extract_array(txt), items)
    assert validate(extract_array(json.dumps(good)), items) is None
    assert validate(good[:-1], items) and 'mismatch' in validate(good[:-1], items)
    assert validate(good + [good[0]], items) == 'duplicate jid'
    bad = [dict(o) for o in good]; bad[3]['label'] = 'Correct'
    assert validate(bad, items).startswith('bad label')
    bad = [dict(o) for o in good]; bad[5]['jid'] = 'jzzzzz'
    assert 'mismatch' in validate(bad, items)
    try: extract_array('no json here'); raise SystemExit('selftest: extract should fail')
    except ValueError: pass
    # prompt identity: prefix of each full prompt is PROMPT, byte-identical
    shas = {hashlib.sha256(full_prompt(packet(s))[:len(PROMPT)].encode()).hexdigest() for s in range(1, 5)}
    assert len(shas) == 1 and shas == {hashlib.sha256(PROMPT.encode()).hexdigest()}
    # usage classifier: usage text only in envelope error counts; a '429' in result text is never a rate limit
    assert USAGE_RE.search('Claude AI usage limit reached') and not USAGE_RE.search('[{"jid":"j00429"}]')
    print('selftest PASS (7 validator cases, prompt sha identical)')

def load_token():
    r = subprocess.run(['zsh', '-ic', 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True, timeout=60)
    tok = r.stdout.strip(); env = dict(os.environ)
    if tok: env['CLAUDE_CODE_OAUTH_TOKEN'] = tok
    print('token', 'present' if tok else 'ABSENT', flush=True)
    return env, bool(tok)

def redact(s): return re.sub(r'sk-ant-[A-Za-z0-9_\-]+', 'sk-ant-REDACTED', s or '')

def usage_parts(e):
    u = (e or {}).get('usage') or {}
    d = {k: int(u.get(k) or 0) for k in ('input_tokens', 'output_tokens', 'cache_read_input_tokens', 'cache_creation_input_tokens')}
    d['total'] = sum(d.values()); return d

def parse_env(out):
    try: return json.loads(out)
    except Exception:
        for line in reversed((out or '').splitlines()):
            try: return json.loads(line)
            except Exception: pass
    return None

LOCK = threading.Lock()
USED = {'tokens': 0}

def run_session(s, env, results):
    items = packet(s); prompt = full_prompt(items)
    open(os.path.join(HERE, 'prompt_s%d.txt' % s), 'w', encoding='utf-8').write(prompt)
    attempts, rate_retries = [], 0
    while True:
        if os.path.exists(STOP):
            results[s] = {'ok': False, 'why': 'global stop', 'attempts': attempts}; return
        with LOCK:
            if attempts and CUM_BEFORE + USED['tokens'] + SESSION_CAP > BUDGET:
                results[s] = {'ok': False, 'why': 'retry would exceed budget', 'attempts': attempts}; return
        t0 = time.time()
        try:
            r = subprocess.run([BIN, '-p', prompt, '--output-format', 'json', '--max-turns', '2', '--model', MODEL],
                               env=env, capture_output=True, text=True, timeout=WALL_CAP_S, stdin=subprocess.DEVNULL, cwd=SESS)
            rc, out, err = r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired as e:
            rc, out, err = -9, (e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or '')), 'timeout'
        envl = parse_env(out); u = usage_parts(envl)
        with LOCK: USED['tokens'] += u['total']
        att = {'n': len(attempts) + 1, 'rc': rc, 'secs': round(time.time() - t0, 1), 'usage': u,
               'is_error': (envl or {}).get('is_error'), 'subtype': (envl or {}).get('subtype'),
               'num_turns': (envl or {}).get('num_turns'), 'stderr_tail': redact(err)[-400:]}
        attempts.append(att)
        json.dump({'session': s, 'attempt': att['n'], 'envelope': envl, 'stdout_if_unparsed': None if envl else redact(out)[-4000:]},
                  open(os.path.join(SESS, 's%d_attempt%d.json' % (s, att['n'])), 'w'), ensure_ascii=False, indent=1)
        errmsg = ''
        if envl and (envl.get('is_error') or rc != 0):
            errmsg = json.dumps({k: envl.get(k) for k in ('result', 'error', 'subtype', 'api_error_status')}, ensure_ascii=False)
        if errmsg and USAGE_RE.search(errmsg):
            open(STOP, 'w').write('# STOP stage 4\nUsage-limit/quota error on judge session %d (attempt %d):\n\n%s\n' % (s, att['n'], redact(errmsg)[:2000]))
            results[s] = {'ok': False, 'why': 'usage limit', 'attempts': attempts}; return
        if u['total'] > SESSION_CAP:
            open(STOP, 'w').write('# STOP stage 4\nJudge session %d used %d tokens > cap %d. No retry.\n' % (s, u['total'], SESSION_CAP))
            results[s] = {'ok': False, 'why': 'session cap exceeded', 'attempts': attempts}; return
        status = (envl or {}).get('api_error_status')
        if errmsg and (status in (429, 529) or re.search(r'"(rate_limit_error|overloaded_error)"', errmsg)) and rate_retries < 3:
            rate_retries += 1; attempts.pop(); time.sleep(min(600, 30 * 2 ** rate_retries) * random.uniform(0.8, 1.2)); continue
        why = errmsg or ('rc %d' % rc if rc != 0 else None) or (None if envl else 'no envelope')
        arr = None
        if not why:
            try:
                arr = extract_array(envl.get('result')); why = validate(arr, items)
            except Exception as e:
                why = 'parse: %s' % e
        att['why'] = why
        if not why:
            results[s] = {'ok': True, 'arr': arr, 'attempts': attempts}; return
        if len(attempts) >= 2:
            results[s] = {'ok': False, 'why': why, 'attempts': attempts}; return

def main():
    selftest()
    env, ok = load_token()
    if not ok:
        open(STOP, 'w').write('# STOP stage 4\nOAuth token absent; 0 sessions spawned.\n'); sys.exit(2)
    assert CUM_BEFORE + 4 * SESSION_CAP <= BUDGET, 'reservation exceeds budget'
    results, th = {}, []
    for s in range(1, 5):
        t = threading.Thread(target=run_session, args=(s, env, results)); t.start(); th.append(t)
    for t in th: t.join()
    psha = hashlib.sha256(PROMPT.encode()).hexdigest()
    for s in range(1, 5):
        assert open(os.path.join(HERE, 'prompt_s%d.txt' % s), encoding='utf-8').read()[:len(PROMPT)] == PROMPT
    open(os.path.join(HERE, 'judge_prompt.txt'), 'w', encoding='utf-8').write(PROMPT)
    open(os.path.join(HERE, 'PROMPT.sha256'), 'w').write('%s  judge_prompt.txt (identical prefix of prompt_s1..s4.txt)\n' % psha)
    summ = {'prompt_sha': psha, 'model': MODEL, 'sessions': {}}
    for s in range(1, 5):
        R = results[s]
        tok = {k: sum(a['usage'][k] for a in R['attempts']) for k in ('input_tokens', 'output_tokens', 'cache_read_input_tokens', 'cache_creation_input_tokens', 'total')}
        summ['sessions'][s] = {'ok': R['ok'], 'why': R.get('why'), 'attempts': R['attempts'], 'tokens': tok}
        if R['ok']:
            json.dump(R['arr'], open(os.path.join(HERE, 'verdicts_s%d.json' % s), 'w'), ensure_ascii=False, indent=0)
        with open(os.path.join(P2I, 'TOKENS.jsonl'), 'a') as f:
            f.write(json.dumps({'stage': '4', 'what': 'judge s%d' % s, 'model': MODEL, 'attempts': len(R['attempts']), **tok, 'gemini_calls': 0, 'ts': '2026-09-21'}) + '\n')
    summ['judge_tokens_total'] = sum(summ['sessions'][s]['tokens']['total'] for s in range(1, 5))
    json.dump(summ, open(os.path.join(HERE, 'JUDGES_SUMMARY.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({'prompt_sha': psha, 'tok': {s: summ['sessions'][s]['tokens']['total'] for s in range(1, 5)},
                      'ok': {s: summ['sessions'][s]['ok'] for s in range(1, 5)}, 'why': {s: summ['sessions'][s]['why'] for s in range(1, 5)}}))
    if not all(results[s]['ok'] for s in range(1, 5)):
        if not os.path.exists(STOP):
            open(STOP, 'w').write('# STOP stage 4\nJudge session(s) failed: %s\n' % {s: results[s].get('why') for s in range(1, 5) if not results[s]['ok']})
        sys.exit(3)

if __name__ == '__main__':
    selftest() if sys.argv[1:] == ['selftest'] else main()
