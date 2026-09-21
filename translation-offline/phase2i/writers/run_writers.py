#!/usr/bin/env python3
"""Phase 2I stage 3: 4 blind writer headless Claude sessions (one per level), 2H recipe.
Writers see ONLY wid / slovak / level / topic. Output: set/answers.jsonl (no labels).
Token loaded via zsh -ic, never printed. Usage limit (from envelope error only) -> STOP_stage3.md."""
import json, os, re, sys, time, random, hashlib, subprocess, threading
HERE = os.path.dirname(os.path.abspath(__file__))
P2I = os.path.dirname(HERE)
BIN = os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude')
MODEL = 'opus'
WALL_CAP_S = 2400
LEVELS = ['A1', 'A2', 'B1', 'B2']
TYPES = ['T', 'W', 'M', 'S']
SESS = os.path.join(HERE, 'sessions'); os.makedirs(SESS, exist_ok=True)
USAGE_RE = re.compile(r'usage limit|hit your limit|weekly limit|5-hour limit|out of extra usage|credit balance is too low|limit will reset|resets at|quota', re.I)

TEMPLATE = """You are a writer for a translation-checking test set. Do not use any tools. Reply with JSON only.

Below is a list of Slovak sentences from a language-learning app, one per line as JSON: a writer id (wid), the Slovak sentence, its CEFR level and the exercise topic. Imagine real learners translating each Slovak sentence into English.

For EACH sentence write:
- 5 CORRECT English translations: correct English with the same meaning as the Slovak. Make them as varied as real learners would be: different words (synonyms), different structures, different articles where the choice is free, different English tenses as long as they stay inside the Slovak's time frame (past stays past, present stays present, future stays future), a passive where it is natural, dropped optional function words. Each must be a fully acceptable translation.
- 4 WRONG translations, exactly one of each type:
  T = the time frame differs from the Slovak (e.g. past instead of present or future); otherwise correct.
  W = a wrong word or a changed meaning (a different thing, person, place, time, quantity or action).
  M = a content word of the Slovak is missing (the rest is correct).
  S = a structure or grammar error that makes it not correct English (e.g. a missing obligatory article, broken subject-verb agreement, wrong word form); the meaning is otherwise kept.
  Each wrong answer must be wrong for its tagged reason and should otherwise look like a plausible learner answer.
- If the Slovak names an agent (a person or thing doing the action), you MAY (not must) make one of the wrong answers an English passive that drops that agent; if you do, set "agent_drop": true on it (its type stays the one it is tagged with). Otherwise "agent_drop": false.

Do not repeat an answer within one sentence. Write only the English answers; no explanations.

Output: one JSON array, one object per sentence, in the input order, exactly this shape:
[{"wid": "...", "correct": ["...", "...", "...", "...", "..."], "wrong": [{"type": "T", "answer": "...", "agent_drop": false}, {"type": "W", "answer": "...", "agent_drop": false}, {"type": "M", "answer": "...", "agent_drop": false}, {"type": "S", "answer": "...", "agent_drop": false}]}]

Sentences:
{SENTENCES}
"""

def load_token():
    r = subprocess.run(['zsh', '-ic', 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True, timeout=60)
    tok = r.stdout.strip()
    env = dict(os.environ)
    if tok:
        env['CLAUDE_CODE_OAUTH_TOKEN'] = tok
    print('token', 'present' if tok else 'ABSENT', flush=True)
    return env, bool(tok)

def redact(s):
    return re.sub(r'sk-ant-[A-Za-z0-9_\-]+', 'sk-ant-REDACTED', s or '')

def usage_parts(env):
    u = (env or {}).get('usage') or {}
    return {k: int(u.get(k) or 0) for k in ('input_tokens', 'output_tokens', 'cache_read_input_tokens', 'cache_creation_input_tokens')}

def parse_env(stdout):
    try:
        return json.loads(stdout)
    except Exception:
        for line in reversed((stdout or '').splitlines()):
            try:
                return json.loads(line)
            except Exception:
                pass
    return None

def extract_array(text):
    t = (text or '').strip()
    m = re.search(r'```(?:json)?\s*(.*?)```', t, re.S)
    if m: t = m.group(1).strip()
    i, j = t.find('['), t.rfind(']')
    return json.loads(t[i:j + 1])

def validate(arr, sents):
    wids = [s['wid'] for s in sents]
    if not isinstance(arr, list) or [o.get('wid') for o in arr] != wids:
        return 'wid list mismatch'
    for o in arr:
        c, w = o.get('correct'), o.get('wrong')
        if not (isinstance(c, list) and len(c) == 5 and all(isinstance(x, str) and x.strip() for x in c)):
            return 'correct != 5 at %s' % o.get('wid')
        if not (isinstance(w, list) and len(w) == 4 and sorted(x.get('type') for x in w) == TYPES
                and all(isinstance(x.get('answer'), str) and x['answer'].strip() for x in w)):
            return 'wrong != T/W/M/S at %s' % o.get('wid')
    return None

def run_level(lv, sents, env, results):
    lines = '\n'.join(json.dumps({'wid': s['wid'], 'slovak': s['slovak'], 'level': s['level'], 'topic': s['topic']}, ensure_ascii=False) for s in sents)
    prompt = TEMPLATE.replace('{SENTENCES}', lines)
    open(os.path.join(HERE, 'prompt_%s.txt' % lv), 'w', encoding='utf-8').write(prompt)
    attempts, rate_retries, fails = [], 0, 0
    while True:
        if os.path.exists(os.path.join(P2I, 'STOP_stage3.md')):
            results[lv] = {'ok': False, 'why': 'global stop', 'attempts': attempts}; return
        t0 = time.time()
        try:
            r = subprocess.run([BIN, '-p', prompt, '--output-format', 'json', '--max-turns', '12', '--model', MODEL],
                               env=env, capture_output=True, text=True, timeout=WALL_CAP_S, stdin=subprocess.DEVNULL, cwd=HERE)
            rc, out, err = r.returncode, r.stdout, r.stderr
        except subprocess.TimeoutExpired as e:
            rc, out, err = -9, (e.stdout or b'').decode() if isinstance(e.stdout, bytes) else (e.stdout or ''), 'timeout'
        envl = parse_env(out)
        att = {'n': len(attempts) + 1, 'rc': rc, 'secs': round(time.time() - t0, 1), 'usage': usage_parts(envl),
               'is_error': (envl or {}).get('is_error'), 'subtype': (envl or {}).get('subtype'),
               'num_turns': (envl or {}).get('num_turns'), 'stderr_tail': redact(err)[-400:]}
        attempts.append(att)
        json.dump({'level': lv, 'attempt': att['n'], 'envelope': envl, 'stdout_if_unparsed': None if envl else redact(out)[-4000:]},
                  open(os.path.join(SESS, '%s_attempt%d.json' % (lv, att['n'])), 'w'), ensure_ascii=False, indent=1)
        errmsg = ''
        if envl and (envl.get('is_error') or rc != 0):
            errmsg = json.dumps({k: envl.get(k) for k in ('result', 'error', 'subtype', 'api_error_status')}, ensure_ascii=False)
        status = (envl or {}).get('api_error_status')
        if errmsg and USAGE_RE.search(errmsg):
            open(os.path.join(P2I, 'STOP_stage3.md'), 'w').write('# STOP stage 3\nUsage-limit/quota error on writer %s (attempt %d):\n\n%s\n' % (lv, att['n'], redact(errmsg)[:2000]))
            results[lv] = {'ok': False, 'why': 'usage limit', 'attempts': attempts}; return
        if errmsg and (status in (429, 529) or re.search(r'"(rate_limit_error|overloaded_error)"', errmsg)) and rate_retries < 3:
            rate_retries += 1; time.sleep(min(600, 30 * 2 ** rate_retries) * random.uniform(0.8, 1.2)); continue
        why = errmsg or ('rc %d' % rc if rc != 0 else None)
        arr = None
        if not why:
            try:
                arr = extract_array(envl.get('result'))
                why = validate(arr, sents)
            except Exception as e:
                why = 'parse: %s' % e
        att['why'] = why
        if not why:
            results[lv] = {'ok': True, 'arr': arr, 'attempts': attempts}; return
        fails += 1
        if fails >= 2:
            results[lv] = {'ok': False, 'why': why, 'attempts': attempts}; return

def main():
    sents = [json.loads(l) for l in open(os.path.join(P2I, 'set', 'sentences.jsonl'), encoding='utf-8')]
    tsha = hashlib.sha256(TEMPLATE.encode()).hexdigest()
    env, ok = load_token()
    if not ok:
        open(os.path.join(P2I, 'STOP_stage3.md'), 'w').write('# STOP stage 3\nOAuth token absent; 0 sessions spawned.\n'); sys.exit(2)
    results, th = {}, []
    for lv in LEVELS:
        t = threading.Thread(target=run_level, args=(lv, [s for s in sents if s['level'] == lv], env, results)); t.start(); th.append(t)
    for t in th: t.join()
    shas = {lv: hashlib.sha256(open(os.path.join(HERE, 'prompt_%s.txt' % lv), 'rb').read()).hexdigest() for lv in LEVELS}
    # prompt identity check: prompt minus sentence list == template for all 4
    for lv in LEVELS:
        p = open(os.path.join(HERE, 'prompt_%s.txt' % lv), encoding='utf-8').read()
        assert p.split('Sentences:\n')[0] == TEMPLATE.split('Sentences:\n')[0]
    open(os.path.join(HERE, 'PROMPTS.sha256'), 'w').write('template %s\n' % tsha + ''.join('prompt_%s.txt %s\n' % (lv, shas[lv]) for lv in LEVELS))
    tok = {lv: {k: sum(a['usage'][k] for a in results[lv]['attempts']) for k in ('input_tokens', 'output_tokens', 'cache_read_input_tokens', 'cache_creation_input_tokens')} for lv in LEVELS}
    for lv in LEVELS: tok[lv]['total'] = sum(tok[lv].values())
    summary = {'template_sha': tsha, 'prompt_sha': shas, 'model': MODEL,
               'sessions': {lv: {'ok': results[lv]['ok'], 'why': results[lv].get('why'), 'attempts': results[lv]['attempts'], 'tokens': tok[lv]} for lv in LEVELS}}
    if not all(results[lv]['ok'] for lv in LEVELS):
        json.dump(summary, open(os.path.join(HERE, 'WRITERS_SUMMARY.json'), 'w'), indent=1)
        if not os.path.exists(os.path.join(P2I, 'STOP_stage3.md')):
            open(os.path.join(P2I, 'STOP_stage3.md'), 'w').write('# STOP stage 3\nWriter session(s) failed twice: %s\n' % {lv: results[lv].get('why') for lv in LEVELS if not results[lv]['ok']})
        print(json.dumps(summary)[:3000]); sys.exit(3)
    by_wid = {s['wid']: s for s in sents}
    answers, dedup, agent_drop, tcount = [], [], 0, {t: 0 for t in TYPES}
    for lv in LEVELS:
        for o in results[lv]['arr']:
            s = by_wid[o['wid']]; seen = set()
            items = [('correct', None, a, False, 'c%d' % i) for i, a in enumerate(o['correct'], 1)] + \
                    [('wrong', w['type'], w['answer'], bool(w.get('agent_drop')), w['type'].lower()) for w in o['wrong']]
            for intent, typ, a, ad, suf in items:
                a = a.strip()
                if a in seen:
                    dedup.append({'sid': s['sid'], 'intent': intent, 'type': typ, 'answer': a}); continue
                seen.add(a)
                if typ: tcount[typ] += 1
                agent_drop += ad
                answers.append({'aid': 'A:%d:%s' % (s['sid'], suf), 'sid': s['sid'], 'level': s['level'], 'slovak': s['slovak'],
                                'topic': s['topic'], 'answer': a, 'writer_intent': intent, 'writer_type': typ, 'writer_agent_drop': ad})
    ap = os.path.join(P2I, 'set', 'answers.jsonl')
    with open(ap, 'w', encoding='utf-8') as f:
        for a in answers: f.write(json.dumps(a, ensure_ascii=False) + '\n')
    asha = hashlib.sha256(open(ap, 'rb').read()).hexdigest()
    open(ap + '.sha256', 'w').write('%s  answers.jsonl\n' % asha)
    summary.update({'answers': len(answers), 'correct': sum(a['writer_intent'] == 'correct' for a in answers),
                    'wrong': sum(a['writer_intent'] == 'wrong' for a in answers), 'wrong_by_type': tcount,
                    'dedupes': len(dedup), 'dedupe_list': dedup, 'agent_drop_natural': agent_drop, 'answers_sha': asha,
                    'tokens_total': {k: sum(tok[lv][k] for lv in LEVELS) for k in tok['A1']}})
    json.dump(summary, open(os.path.join(HERE, 'WRITERS_SUMMARY.json'), 'w'), indent=1, ensure_ascii=False)
    with open(os.path.join(P2I, 'TOKENS.jsonl'), 'a') as f:
        for lv in LEVELS:
            f.write(json.dumps({'stage': '3', 'what': 'writer %s' % lv, 'model': MODEL, 'attempts': len(results[lv]['attempts']), **tok[lv], 'gemini_calls': 0, 'ts': '2026-09-21'}) + '\n')
    print(json.dumps({k: v for k, v in summary.items() if k != 'dedupe_list'}))

if __name__ == '__main__':
    main()
