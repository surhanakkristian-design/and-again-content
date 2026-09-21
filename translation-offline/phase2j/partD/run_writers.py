#!/usr/bin/env python3
"""Phase 2J S6: 4 blind writer headless Claude sessions (one per level), adapted from phase2i/writers/run_writers.py.
Same TEMPLATE byte-for-byte (sha asserted against phase2i/writers/PROMPTS.sha256). Writers see ONLY wid/slovak/level/topic.
Spawner = run_2j.run_session (tested: usage-limit envelope -> STOP_usage_limit.md hard stop; rate limit only from the
envelope; resume of finished sessions at 0 cost). Validator = 2I's with DEFECTS 14 fixed (sorted(TYPES)); an invalid
output gets ONE retry (sid <lv>_r1). Token cap by reservation (spent + in-flight + est <= cap). No labels.
  python3 -B /abs/partD/run_writers.py --set-dir /abs/partD/set --work-dir /abs/partD/writers [--mock]"""
import argparse, json, os, re, sys, hashlib, threading, glob, types
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); P2J = os.path.dirname(HERE); ROOT = os.path.dirname(P2J)
sys.path.insert(0, P2J)
import run_2j as R
MODEL = 'opus'
LEVELS = ['A1', 'A2', 'B1', 'B2']
TYPES = ['T', 'W', 'M', 'S']
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
T2I_SHA = open(os.path.join(ROOT, 'phase2i', 'writers', 'PROMPTS.sha256')).readline().split()[1]

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
        if not (isinstance(w, list) and len(w) == 4 and all(isinstance(x, dict) for x in w)
                and sorted(x.get('type') or '' for x in w) == sorted(TYPES)
                and all(isinstance(x.get('answer'), str) and x['answer'].strip() for x in w)):
            return 'wrong != T/W/M/S at %s' % o.get('wid')
    return None

def spent(work):
    return sum(int(v.get('tokens') or 0) for p in glob.glob(os.path.join(work, 'sessions', '*', 'headless_ledger.json'))
               for v in json.load(open(p)).values())

def run_level(lv, sents, a, results, lock, inflight):
    prompt = TEMPLATE.replace('{SENTENCES}', '\n'.join(json.dumps({'wid': s['wid'], 'slovak': s['slovak'], 'level': s['level'],
                                                                   'topic': s['topic']}, ensure_ascii=False) for s in sents))
    open(os.path.join(a.work_dir, 'prompt_%s.txt' % lv), 'w', encoding='utf-8').write(prompt)
    atts = []
    for sid in (lv, lv + '_r1'):
        sd = os.path.join(a.work_dir, 'sessions', sid)
        done = os.path.exists(os.path.join(sd, '%s.json' % sid))
        with lock:
            if not done and spent(a.work_dir) + sum(inflight.values()) + a.est > a.token_cap:
                results[lv] = {'ok': False, 'why': 'token_cap reservation', 'attempts': atts}; return
            inflight[sid] = 0 if done else a.est
        try:
            d = R.run_session(sid, prompt, sd, stop_dir=a.stop_dir, model=MODEL, max_turns=12, wall=2400)
        except R.Stop as e:
            results[lv] = {'ok': False, 'why': '%s: %s' % (e.kind, e.why), 'attempts': atts}; return
        finally:
            with lock: inflight.pop(sid, None)
        try:
            arr = extract_array(d.get('result')); why = validate(arr, sents)
        except Exception as ex:
            arr, why = None, 'parse: %s' % ex
        atts.append({'sid': sid, 'tokens': d.get('tokens'), 'resumed': bool(d.get('resumed')), 'spawns': d.get('spawns'), 'why': why})
        if not why:
            results[lv] = {'ok': True, 'arr': arr, 'attempts': atts}; return
    results[lv] = {'ok': False, 'why': atts[-1]['why'], 'attempts': atts}

def mock_install():
    calls = {'n': 0, 'bad': set(), 'rate': set()}
    def fake(argv, timeout):
        calls['n'] += 1
        pr = argv[argv.index('-p') + 1]
        lines = [json.loads(l) for l in pr.split('Sentences:\n', 1)[1].splitlines() if l.strip()]
        lv = lines[0]['level']
        if lv == 'B2' and lv not in calls['rate']:
            calls['rate'].add(lv)
            env = {'type': 'result', 'is_error': True, 'subtype': 'error', 'api_error_status': 429, 'result': 'rate limited row 429',
                   'usage': {'input_tokens': 5}}
            return types.SimpleNamespace(returncode=1, stdout=json.dumps(env), stderr='')
        arr = [{'wid': s['wid'], 'correct': ['c%d %s' % (i, s['wid']) for i in range(1, 6)],
                'wrong': [{'type': t, 'answer': '%s %s' % (t, s['wid']), 'agent_drop': t == 'M'} for t in TYPES]} for s in lines]
        if lv == 'A1' and lv not in calls['bad']:
            calls['bad'].add(lv); arr[0]['wrong'] = arr[0]['wrong'][:3]
        if lv == 'A2': arr[0]['correct'][4] = arr[0]['correct'][0]
        env = {'type': 'result', 'is_error': False, 'subtype': 'success', 'result': '```json\n%s\n```' % json.dumps(arr),
               'usage': {'input_tokens': 1000, 'output_tokens': 500}}
        return types.SimpleNamespace(returncode=0, stdout=json.dumps(env), stderr='')
    R.SPAWN[0] = fake; R.SLEEP_H[0] = lambda s: None; R.ENV[0] = dict(os.environ)
    return calls

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--set-dir', required=True); ap.add_argument('--work-dir', required=True)
    ap.add_argument('--stop-dir', default=P2J); ap.add_argument('--token-cap', type=int, default=500000)
    ap.add_argument('--est', type=int, default=110000); ap.add_argument('--mock', action='store_true')
    a = ap.parse_args()
    for p in (a.set_dir, a.work_dir, a.stop_dir):
        if not os.path.isabs(p):
            print('REFUSED: relative path %r (absolute paths only)' % p); return 2
    tsha = hashlib.sha256(TEMPLATE.encode()).hexdigest()
    assert tsha == T2I_SHA, 'template differs from 2I'
    os.makedirs(a.work_dir, exist_ok=True)
    real = not a.mock
    if real and (a.work_dir.startswith('/private/tmp') or a.stop_dir != P2J):
        print('REFUSED: real run outside phase2j'); return 2
    if a.mock:
        if a.work_dir.startswith(P2J): print('REFUSED: mock into phase2j'); return 2
        calls = mock_install()
    else:
        R.load_token(); e = R.ENV[0]
        if not (isinstance(e, dict) and e.get('CLAUDE_CODE_OAUTH_TOKEN')):
            open(os.path.join(P2J, 'STOP_S6.md'), 'w').write('# STOP S6\nOAuth token absent; 0 sessions spawned.\n'); return 2
    sents = [json.loads(l) for l in open(os.path.join(a.set_dir, 'sentences.jsonl'), encoding='utf-8')]
    ssha = hashlib.sha256(open(os.path.join(a.set_dir, 'sentences.jsonl'), 'rb').read()).hexdigest()
    results, lock, inflight, th = {}, threading.Lock(), {}, []
    for lv in LEVELS:
        t = threading.Thread(target=run_level, args=(lv, [s for s in sents if s['level'] == lv], a, results, lock, inflight)); t.start(); th.append(t)
    for t in th: t.join()
    for lv in LEVELS:
        p = open(os.path.join(a.work_dir, 'prompt_%s.txt' % lv), encoding='utf-8').read()
        assert p.split('Sentences:\n')[0] == TEMPLATE.split('Sentences:\n')[0]
    shas = {lv: hashlib.sha256(open(os.path.join(a.work_dir, 'prompt_%s.txt' % lv), 'rb').read()).hexdigest() for lv in LEVELS}
    open(os.path.join(a.work_dir, 'PROMPTS.sha256'), 'w').write('template %s\n' % tsha + ''.join('prompt_%s.txt %s\n' % (lv, shas[lv]) for lv in LEVELS))
    tok = {lv: sum(int(x.get('tokens') or 0) for x in results[lv]['attempts'] if not x['resumed']) for lv in LEVELS}
    summary = {'template_sha': tsha, 'template_sha_2i': T2I_SHA, 'prompt_sha': shas, 'model': MODEL, 'sentences_sha': ssha,
               'headless_tokens_total_ledger': spent(a.work_dir),
               'sessions': {lv: {k: results[lv].get(k) for k in ('ok', 'why', 'attempts')} for lv in LEVELS}}
    if a.mock: summary['mock_spawns'] = calls['n']
    if not all(results[lv]['ok'] for lv in LEVELS):
        json.dump(summary, open(os.path.join(a.work_dir, 'WRITERS_SUMMARY.json'), 'w'), indent=1)
        if real and not os.path.exists(os.path.join(P2J, 'STOP_usage_limit.md')):
            open(os.path.join(P2J, 'STOP_S6.md'), 'w').write('# STOP S6\nWriter session(s) failed: %s\n' % {lv: results[lv].get('why') for lv in LEVELS if not results[lv]['ok']})
        print(json.dumps(summary)[:3000]); return 3
    by_wid = {s['wid']: s for s in sents}
    answers, dedup, agent_drop, tcount = [], [], 0, {t: 0 for t in TYPES}
    for lv in LEVELS:
        for o in results[lv]['arr']:
            s = by_wid[o['wid']]; seen = set()
            items = [('correct', None, x, False, 'c%d' % i) for i, x in enumerate(o['correct'], 1)] + \
                    [('wrong', w['type'], w['answer'], bool(w.get('agent_drop')), w['type'].lower()) for w in o['wrong']]
            for intent, typ, x, ad, suf in items:
                x = x.strip()
                if x in seen:
                    dedup.append({'sid': s['sid'], 'intent': intent, 'type': typ, 'answer': x}); continue
                seen.add(x)
                if typ: tcount[typ] += 1
                agent_drop += ad
                answers.append({'aid': 'A:%d:%s' % (s['sid'], suf), 'sid': s['sid'], 'level': s['level'], 'slovak': s['slovak'],
                                'topic': s['topic'], 'answer': x, 'writer_intent': intent, 'writer_type': typ, 'writer_agent_drop': ad})
    assert len({x['aid'] for x in answers}) == len(answers)
    ap_ = os.path.join(a.set_dir, 'answers.jsonl')
    with open(ap_, 'w', encoding='utf-8') as f:
        for x in answers: f.write(json.dumps(x, ensure_ascii=False) + '\n')
    asha = hashlib.sha256(open(ap_, 'rb').read()).hexdigest()
    open(ap_ + '.sha256', 'w').write('%s  answers.jsonl\n' % asha)
    summary.update({'answers': len(answers), 'correct': sum(x['writer_intent'] == 'correct' for x in answers),
                    'wrong': sum(x['writer_intent'] == 'wrong' for x in answers), 'wrong_by_type': tcount,
                    'dedupes': len(dedup), 'dedupe_list': dedup, 'agent_drop_natural': agent_drop, 'answers_sha': asha,
                    'tokens_this_run': tok})
    json.dump(summary, open(os.path.join(a.work_dir, 'WRITERS_SUMMARY.json'), 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in summary.items() if k not in ('dedupe_list', 'sessions')}))
    return 0

if __name__ == '__main__':
    sys.exit(main())
