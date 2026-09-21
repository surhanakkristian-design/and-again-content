#!/usr/bin/env python3
"""Phase 1e — three-layer hybrid measurement (L1 offline checker / L2 grammar veto / L3 model).

Run from translation-offline/ (or anywhere; all paths are absolute-derived):
  python3 phase1e/run_phase1e.py --dry        # no network: routing counts + budget plan
  python3 phase1e/run_phase1e.py --probe      # ListModels + <=2 generate calls per model (ledgered)
  python3 phase1e/run_phase1e.py --run        # full plan, resumable; writes results.json/.md, prints results.md
  python3 phase1e/run_phase1e.py --selfcheck  # key hygiene checks (also run at the end of every action)

Phase 1c data under phase1c/ is FROZEN and only ever read.
KEY RULE: the API key is parsed from ~/Projects/and-again/.env.local at runtime, sent ONLY in the
x-goog-api-key header, never printed, never written, never on a command line. All error text is redacted.
"""
import json, os, re, sys, time, random, subprocess, hashlib, urllib.request, urllib.error
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath('/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1i/lib_prev.py'))
TO = os.path.dirname(HERE)                      # translation-offline/
P1C = os.path.join(TO, 'phase1c')               # FROZEN
APP = os.path.expanduser('~/Projects/and-again')
ENV = os.path.join(APP, '.env.local')
LEDGER = os.path.join(HERE, 'calls.jsonl')
LOG = os.path.join(HERE, 'decisions.jsonl')
MODEL_CFG = os.path.join(HERE, 'model_config.json')
CALL_CAP, ATTEMPT_CAP = 500, 650
API = 'https://generativelanguage.googleapis.com/v1beta'

# Phase 1c checker code lives in phase1c/scripts (+ checker/v2 in TypeScript). We put it on the path so any
# importable helper is reused rather than copied; the checker VERDICTS themselves are the frozen Phase 1c
# outputs in phase1c/measure/*.json (produced by checker v2 via measure.ts). We never re-run or re-implement
# the checker, and never import phase1c/scripts/measure_after.py, because importing it re-runs the Phase 1c
# measurement and would REWRITE frozen files.
sys.path.insert(0, os.path.join(P1C, 'scripts'))

# ---------------------------------------------------------------- key handling
_KEY = None


def load_key():
    global _KEY
    if _KEY:
        return _KEY
    try:
        with open(ENV) as fh:
            for line in fh:
                line = line.strip()
                if line.startswith('GEMINI_API_KEY'):
                    v = line.split('=', 1)[1].strip().strip('"').strip("'")
                    if v:
                        _KEY = v
                        return _KEY
    except Exception:
        pass
    stop_auth()


def stop_auth():
    print('STOP: GEMINI key missing or auth error')
    sys.exit(2)


def redact(s):
    s = '' if s is None else str(s)
    if _KEY:
        s = s.replace(_KEY, '[REDACTED]')
    return s


# ---------------------------------------------------------------- frozen data
rj = lambda p: json.load(open(p))
ACCEPTED = ('correct', 'correct_with_tip')


def norm(s):
    s = (s or '').lower().replace('„', ' ').replace('“', ' ').replace('’', "'")
    s = re.sub(r"[^a-z0-9' ]+", ' ', s)
    return ' ' + re.sub(r'\s+', ' ', s).strip() + ' '


def load_items():
    """235 held-out correct + 105 wrong, each with the frozen Phase 1c checker verdict and lock info."""
    before = rj(os.path.join(P1C, 'measure_before.json'))
    after = rj(os.path.join(P1C, 'measure_after.json'))
    excl = {(e['id'], e['answer']) for e in before['excluded_from_denominator']}
    cov = rj(os.path.join(P1C, 'measure', 'cov_after.json'))['rows']
    fa = rj(os.path.join(P1C, 'measure', 'fa_after.json'))['rows']
    types = {}
    for e in rj(os.path.join(P1C, 'inputs', 'fa.json')):
        for t in e['translations']:
            types[(e['exercise_id'], t['text'])] = (t['type'], t.get('why', ''))
    judged = {(x['id'], x['answer']): x for x in after['false_acceptance']['list']}

    def locks(eid):
        p = os.path.join(P1C, 'annotated_after', '%d.json' % eid)
        if not os.path.exists(p):
            return []
        a = rj(p)
        lk = a.get('lk') or []
        return [x for x in lk if isinstance(x, str) and x.strip()]

    def mk(r, kind):
        eid = r['exercise_id']
        wt, why = types.get((eid, r['answer']), (None, ''))
        lk = locks(eid)
        j = judged.get((eid, r['answer']))
        return {
            'item_id': '%s:%d:%d' % (kind, eid, int(hashlib.md5(r['answer'].encode()).hexdigest()[:8], 16)),
            'kind': kind, 'exercise_id': eid, 'level': r['level'], 'topic': r['topic'],
            'sk': r['sk'], 'reference': r['reference'], 'answer': r['answer'],
            'verdict': r['verdict'], 'step': r['step'], 'feedback': r['feedback'],
            'wrong_type': wt, 'wrong_why': why, 'locks': lk,
            'lock_ok': (not lk) or any(norm(x).strip() in norm(r['answer']) for x in lk),
            'fa_class': (j or {}).get('class'), 'fa_judgement': (j or {}).get('judgement'),
        }

    correct = [mk(r, 'C') for r in cov if (r['exercise_id'], r['answer']) not in excl]
    wrong = [mk(r, 'W') for r in fa]
    return correct, wrong


def route(it):
    """L1 offline accept / L2 grammar veto / L3 model."""
    if it['verdict'] in ACCEPTED:
        return 'L1', 'checker verdict %s' % it['verdict']
    if it['step'] == 'mistake':
        return 'L2', 'library mistake matched: %s' % (it['feedback'] or '')
    return 'L3', ''


# ---------------------------------------------------------------- ledger
def ledger_lines():
    if not os.path.exists(LEDGER):
        return []
    out = []
    for line in open(LEDGER):
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except Exception:
                pass
    return out


def ledger_state():
    ls = ledger_lines()
    spent = [x for x in ls if x.get('counted')]
    cache = {}
    for x in ls:
        if x.get('counted') and x.get('verdict') and x['verdict'] != 'PARSE_FAIL':
            cache[(x['model'], x['variant'], x['item_id'])] = x
    return ls, spent, cache


def ledger_append(rec):
    with open(LEDGER, 'a') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')


def log_decision(rec):
    with open(LOG, 'a') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')


# ---------------------------------------------------------------- HTTP
def http(url, body=None):
    """Returns (status, parsed_json_or_None, raw_text, latency_ms). Never leaks the key."""
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method='POST' if data else 'GET')
    req.add_header('x-goog-api-key', load_key())
    if data:
        req.add_header('Content-Type', 'application/json')
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read().decode('utf-8', 'replace')
            st = r.status
    except urllib.error.HTTPError as e:
        raw = e.read().decode('utf-8', 'replace') if e.fp else ''
        st = e.code
    except Exception as e:
        return 0, None, redact('%s: %s' % (type(e).__name__, e)), int((time.monotonic() - t0) * 1000)
    ms = int((time.monotonic() - t0) * 1000)
    try:
        js = json.loads(raw)
    except Exception:
        js = None
    if st in (401, 403) or 'API_KEY_INVALID' in raw or 'API key not valid' in raw:
        stop_auth()
    return st, js, redact(raw), ms


def list_models():
    ids, tok = [], ''
    while True:
        st, js, raw, _ = http(API + '/models?pageSize=200' + (('&pageToken=' + tok) if tok else ''))
        if st != 200 or not js:
            print('ListModels failed HTTP %s: %s' % (st, raw[:300]))
            sys.exit(3)
        for m in js.get('models', []):
            if 'generateContent' in (m.get('supportedGenerationMethods') or []):
                ids.append(m['name'].split('/')[-1])
        tok = js.get('nextPageToken') or ''
        if not tok:
            break

    def pick(want, banlite=False):
        c = [i for i in ids if want in i and (not banlite or 'lite' not in i)]
        if not c:
            return None
        stable = [i for i in c if 'preview' not in i and 'exp' not in i and not re.search(r'\d{2}-\d{2}$', i)]
        pool = stable or c
        return sorted(pool, key=lambda i: (len(i), i))[0]

    lite = pick('3.1-flash-lite')
    f37 = pick('3.7-flash', banlite=True)
    if not lite or not f37:
        print('Could not resolve model ids. lite=%s flash=%s' % (lite, f37))
        sys.exit(3)
    return lite, f37


SYS = ("You judge English translations. Reply with exactly one word: SAME, TIP or DIFF. "
       "SAME = the learner sentence means the same as the reference and is correct English. "
       "TIP = same meaning and acceptable, but with a small slip. "
       "DIFF = different meaning, or not correct English. No explanation.")


def prompt(it, variant):
    lines = ['Slovak: ' + it['sk'], 'Reference English: ' + it['reference'], 'Learner: ' + it['answer']]
    lines.append('SAME, TIP or DIFF?')
    return '\n'.join(lines)


THINK_LADDER = [{'thinkingBudget': 0}, {'thinkingLevel': 'minimal'}, {'thinkingLevel': 'low'}, None]


def parse_verdict(js):
    txt = ''
    try:
        for c in js['candidates'][0]['content']['parts']:
            txt += c.get('text', '')
    except Exception:
        txt = ''
    u = (js or {}).get('usageMetadata') or {}
    m = re.search(r'\b(SAME|TIP|DIFF)\b', txt.upper())
    fin = ((js or {}).get('candidates') or [{}])[0].get('finishReason')
    return (m.group(1) if m else 'PARSE_FAIL'), txt.strip(), u, fin


class Budget:
    def __init__(self):
        self.ls, self.spent, self.cache = ledger_state()
        self.attempts = len(self.ls)
        self.used = len(self.spent)
        self.r429 = sum(1 for x in self.ls if x.get('http') == 429)
        self.cold_done = set()

    def can(self):
        return self.used < CALL_CAP and self.attempts < ATTEMPT_CAP


def call_model(bud, model, variant, it, cfg, max_out=8):
    """One ledgered generateContent request set (with 429 retries). Returns record or None if capped."""
    key = (model, variant, it['item_id'])
    if key in bud.cache:
        r = dict(bud.cache[key])
        r['cached_result'] = True
        return r
    think = cfg.get('thinking', 'unset')
    mo = cfg.get('max_output', max_out)
    for attempt in range(4):
        if not bud.can():
            return None
        gc = {'temperature': 0, 'maxOutputTokens': mo}
        ti = cfg.get('thinkingConfig', 'unset')
        if ti != 'unset' and ti is not None:
            gc['thinkingConfig'] = ti
        body = {'systemInstruction': {'parts': [{'text': SYS}]},
                'contents': [{'role': 'user', 'parts': [{'text': prompt(it, variant)}]}],
                'generationConfig': gc}
        cold = model not in bud.cold_done
        st, js, raw, ms = http('%s/models/%s:generateContent' % (API, model), body)
        bud.attempts += 1
        bud.cold_done.add(model)
        if st == 429 or (st and st >= 500):
            bud.r429 += (st == 429)
            rec = {'ts': time.time(), 'model': model, 'variant': variant, 'item_id': it['item_id'], 'http': st,
                   'counted': False, 'note': 'free tier rate-limited' if st == 429 else 'server error',
                   'raw': raw[:400]}
            ledger_append(rec)
            if st != 429 or attempt == 3:
                return rec
            d = 5.0
            m = re.search(r'"retryDelay"\s*:\s*"(\d+(?:\.\d+)?)s"', raw)
            if m:
                d = min(float(m.group(1)), 65.0)
            time.sleep(min(d, 65.0))
            continue
        verdict, txt, u, fin = parse_verdict(js or {})
        rec = {'ts': time.time(), 'model': model, 'variant': variant, 'item_id': it['item_id'], 'http': st,
               'counted': True, 'verdict': verdict, 'reply': txt, 'finish': fin, 'cold': cold, 'latency_ms': ms,
               'thinking': think, 'max_output': mo,
               'prompt_tokens': u.get('promptTokenCount'), 'candidates_tokens': u.get('candidatesTokenCount'),
               'thoughts_tokens': u.get('thoughtsTokenCount'), 'cached_tokens': u.get('cachedContentTokenCount'),
               'empty_due_to_thinking': bool(verdict == 'PARSE_FAIL' and (u.get('thoughtsTokenCount') or 0) > 0)}
        if st != 200:
            rec['raw'] = raw[:400]
        ledger_append(rec)
        bud.used += 1
        if rec['counted'] and verdict != 'PARSE_FAIL':
            bud.cache[key] = rec
        return rec
    return None


# ---------------------------------------------------------------- probe
def probe_one(model, think_json, mo):
    """One extra ledgered probe call with an explicit thinking config (used to pin 3.7 Flash)."""
    bud = Budget()
    think = json.loads(think_json) if think_json != 'null' else None
    correct, wrong = load_items()
    it = [x for x in wrong if route(x)[0] == 'L3'][0]
    cfg = {'thinkingConfig': think, 'max_output': int(mo), 'thinking': think_json}
    r = call_model(bud, model, 'P-A', dict(it, item_id=it['item_id'] + '#probe-%s-%s' % (think_json, mo)), cfg)
    print('probe %s think=%s max_out=%s -> HTTP %s verdict=%s in=%s out=%s thoughts=%s cached=%s %sms' % (
        model, think_json, mo, r.get('http'), r.get('verdict'), r.get('prompt_tokens'), r.get('candidates_tokens'),
        r.get('thoughts_tokens'), r.get('cached_tokens'), r.get('latency_ms')))
    cfgs = json.load(open(MODEL_CFG)) if os.path.exists(MODEL_CFG) else {}
    if r.get('verdict') in ('SAME', 'TIP', 'DIFF'):
        cfgs[model] = {'thinkingConfig': think, 'max_output': int(mo), 'thinking': think_json}
        json.dump(cfgs, open(MODEL_CFG, 'w'), ensure_ascii=False, indent=1)
        print('config[%s] pinned = %s' % (model, json.dumps(cfgs[model])))
    else:
        print('config[%s] still UNVERIFIED' % model)
    print('ledger: %d counted calls of %d cap' % (bud.used, CALL_CAP))


def probe():
    bud = Budget()
    lite, f37 = list_models()
    print('models: flash-lite=%s   flash=%s' % (lite, f37))
    cfgs = json.load(open(MODEL_CFG)) if os.path.exists(MODEL_CFG) else {}
    cfgs['_ids'] = {'lite': lite, 'flash': f37}
    correct, wrong = load_items()
    probes = [it for it in wrong if route(it)[0] == 'L3'][:1] or [wrong[0]]
    it = probes[0]
    for model in (lite, f37):
        ok, used = None, 0
        for think in THINK_LADDER:
            if used >= 2 or not bud.can():
                break
            for mo in (8, 16, 32, 64):
                if used >= 2 or not bud.can():
                    break
                cfg = {'thinkingConfig': think, 'max_output': mo, 'thinking': json.dumps(think)}
                r = call_model(bud, model, 'P-A', dict(it, item_id=it['item_id'] + '#probe%d' % used), cfg)
                used += 1
                if r is None:
                    break
                print('probe %s think=%s max_out=%d -> HTTP %s verdict=%s in=%s out=%s thoughts=%s cached=%s %dms' % (
                    model, json.dumps(think), mo, r.get('http'), r.get('verdict'), r.get('prompt_tokens'),
                    r.get('candidates_tokens'), r.get('thoughts_tokens'), r.get('cached_tokens'),
                    r.get('latency_ms', 0)))
                if r.get('http') == 400:
                    break  # bad thinking param -> next rung of the ladder
                if r.get('verdict') in ('SAME', 'TIP', 'DIFF'):
                    ok = {'thinkingConfig': think, 'max_output': mo, 'thinking': json.dumps(think)}
                    break
                if not r.get('empty_due_to_thinking') and r.get('finish') != 'MAX_TOKENS':
                    break
            if ok:
                break
        cfgs[model] = ok or {'thinkingConfig': THINK_LADDER[0], 'max_output': 8, 'thinking': 'UNVERIFIED',
                             'note': 'probe did not confirm; verify before --run'}
        print('config[%s] = %s' % (model, json.dumps(cfgs[model])))
    json.dump(cfgs, open(MODEL_CFG, 'w'), ensure_ascii=False, indent=1)
    print('ledger: %d counted calls of %d cap, %d attempts' % (bud.used, CALL_CAP, bud.attempts))
    return cfgs


# ---------------------------------------------------------------- plan
def routing(correct, wrong):
    open(LOG, 'w').close()  # decisions.jsonl is rewritten per action
    rc, rw = defaultdict(list), defaultdict(list)
    for it in correct:
        lay, why = route(it)
        rc[lay].append(it)
        log_decision({'item_id': it['item_id'], 'set': 'correct', 'layer': lay, 'why': why})
    for it in wrong:
        lay, why = route(it)
        rw[lay].append(it)
        log_decision({'item_id': it['item_id'], 'set': 'wrong', 'type': it['wrong_type'], 'layer': lay, 'why': why})
    return rc, rw


def sanity(rc, rw):
    l1 = len(rc['L1'])
    real_fa = sum(1 for it in rw['L1'] if (it.get('fa_class') or '') not in ('tip-accept', 'valid reading'))
    ok = True
    if l1 != 100 or len(rc['L1']) + len(rc['L2']) + len(rc['L3']) != 235:
        ok = False
    if real_fa != 0:
        ok = False
    if not ok:
        print('!!! SANITY WARNING: L1 accepts on the correct set = %d (Phase 1c: 100/235 = 42.6%%), total = %d, '
              'real false acceptances = %d (Phase 1c: 0). The measuring apparatus is suspect first.'
              % (l1, len(rc['L1']) + len(rc['L2']) + len(rc['L3']), real_fa))
    else:
        print('sanity OK: L1 %d/235 = %.1f%% reproduces Phase 1c 100/235 = 42.6%%; real false acceptances 0/105'
              % (l1, 100 * l1 / 235))
    return ok


def plan(rc, rw, bud):
    N = len(rc['L3']) + len(rw['L3'])
    left = CALL_CAP - bud.used
    p = {'N': N, 'L3_correct': len(rc['L3']), 'L3_wrong': len(rw['L3']), 'ledger_used': bud.used, 'remaining': left}
    if 2 * N <= left:
        p['mode'] = 'full'
        p['stage1'] = {'items': N, 'calls': 2 * N, 'note': 'Flash-Lite x P-A and x P-B on all N'}
        rem = left - 2 * N
        p['stage2'] = {'budget': rem, 'wrong_items': len(rw['L3']),
                       'correct_sample': max(0, min(len(rc['L3']), rem - len(rw['L3']))),
                       'note': '3.7 Flash, better Stage-1 prompt only; all L3 wrong first, then seed-1 sample of '
                               'rejected-correct items'}
        p['cut'] = '4th variant (3.7 Flash x the other prompt) is CUT — not enough budget under the 500 cap.'
    else:
        fit = max(0, (left // 2) - len(rw['L3']))
        p['mode'] = 'stage1-sampled'
        p['stage1'] = {'wrong_items': len(rw['L3']), 'correct_sample': min(fit, len(rc['L3'])),
                       'calls': 2 * (len(rw['L3']) + min(fit, len(rc['L3'])))}
        p['stage2'] = None
        p['cut'] = 'Stage 2 (3.7 Flash) SKIPPED and the 4th variant CUT: 2N=%d exceeds the remaining budget.' % (2 * N)
    return p


def print_plan(rc, rw, p):
    print('\nROUTING')
    print('  correct set (235): L1 %d | L2 %d | L3 %d' % (len(rc['L1']), len(rc['L2']), len(rc['L3'])))
    print('  wrong set   (105): L1 %d (false accepts) | L2 %d (no model call) | L3 %d'
          % (len(rw['L1']), len(rw['L2']), len(rw['L3'])))
    bt = Counter(it['wrong_type'] or '?' for it in rw['L3'])
    ba = Counter(it['wrong_type'] or '?' for it in rw['L1'] + rw['L2'] + rw['L3'])
    b2 = Counter(it['wrong_type'] or '?' for it in rw['L2'])
    b1 = Counter(it['wrong_type'] or '?' for it in rw['L1'])
    for t in 'TWMS':
        print('    type %s: total %d | L1 %d | L2 %d | L3 %d' % (t, ba[t], b1[t], b2[t], bt[t]))
    print('\nBUDGET PLAN  N=%d  ledger used %d/%d' % (p['N'], p['ledger_used'], CALL_CAP))
    print('  mode: %s' % p['mode'])
    print('  stage1: %s' % json.dumps(p['stage1']))
    print('  stage2: %s' % json.dumps(p['stage2']))
    print('  %s' % p['cut'])


# ---------------------------------------------------------------- run
PRICE = {'lite': {'in': 0.25, 'out': 1.50, 'cached': 0.025, 'src': 'task brief'},
         'flash': {'in': 0.75, 'out': 3.75, 'cached': 0.075,
                   'src': 'ai.google.dev/gemini-api/docs/pricing, fetched 2026-09-18, paid tier through 2026-12-31'}}


def run_config(bud, model, variant, items, cfg, tag, out):
    fails = 0
    for it in items:
        if not bud.can():
            out[tag] = dict(out.get(tag, {}), incomplete='call cap reached')
            break
        r = call_model(bud, model, variant, it, cfg)
        while (r is not None and r.get('counted') and r.get('verdict') == 'PARSE_FAIL'
               and (r.get('empty_due_to_thinking') or r.get('finish') == 'MAX_TOKENS')
               and cfg.get('max_output', 8) < 64 and bud.can()):
            cfg['max_output'] = {8: 16, 16: 32, 32: 64}.get(cfg.get('max_output', 8), 64)
            print('  raising maxOutputTokens for %s to %d (thinking consumed the cap)' % (model, cfg['max_output']))
            r = call_model(bud, model, variant, dict(it, item_id=it['item_id'] + '@%d' % cfg['max_output']), cfg)
        if r is None or not r.get('counted'):
            fails += 1
            if fails >= 5:
                out[tag] = dict(out.get(tag, {}), incomplete='5 consecutive failed items (free tier rate limit)')
                break
            continue
        fails = 0
        rec = {'item_id': it['item_id'], 'set': ('correct' if it['kind'] == 'C' else 'wrong'),
               'type': it['wrong_type'], 'layer': 'L3', 'model': model, 'variant': variant,
               'verdict': r['verdict'], 'reply': r.get('reply'), 'latency_ms': r.get('latency_ms'),
               'cold': r.get('cold'), 'cached_result': r.get('cached_result', False)}
        log_decision(rec)
        out.setdefault(tag, {}).setdefault('rows', []).append({**rec, 'tokens': {
            'in': r.get('prompt_tokens'), 'out': r.get('candidates_tokens'),
            'thoughts': r.get('thoughts_tokens'), 'cached': r.get('cached_tokens')}, 'item': it})
    return out


def metrics(tag, res, rc, rw, n_correct_total=235):
    rows = res.get(tag, {}).get('rows', [])
    cr = [r for r in rows if r['set'] == 'correct']
    wr = [r for r in rows if r['set'] == 'wrong']
    acc = lambda r: r['verdict'] in ('SAME', 'TIP')
    m = {'tag': tag, 'sent': len(rows), 'incomplete': res.get(tag, {}).get('incomplete'),
         'n_correct_sent': len(cr), 'n_wrong_sent': len(wr),
         'correct_accepted': sum(acc(r) for r in cr), 'wrong_accepted': sum(acc(r) for r in wr),
         'parse_fail': sum(r['verdict'] == 'PARSE_FAIL' for r in rows)}
    l1 = len(rc['L1'])
    if cr:
        rate = m['correct_accepted'] / len(cr)
        m['coverage_measured'] = (l1 + m['correct_accepted']) / n_correct_total
        m['coverage_extrapolated'] = (l1 + rate * len(rc['L3'])) / n_correct_total
        m['sampled'] = len(cr) < len(rc['L3'])
    else:
        m['coverage_measured'] = m['coverage_extrapolated'] = None
        m['sampled'] = True
    m['fa_by_type'] = dict(Counter(r['type'] or '?' for r in wr if acc(r)))
    m['fa_total_end_to_end'] = len(rw['L1']) + m['wrong_accepted']
    lats = [r['latency_ms'] for r in rows if not r['cold'] and r.get('latency_ms')]
    lats.sort()
    pick = lambda q: lats[min(len(lats) - 1, int(q * len(lats)))] if lats else None
    m['lat_median'], m['lat_p95'] = pick(0.5), pick(0.95)
    m['lat_cold'] = [r['latency_ms'] for r in rows if r['cold']]
    tk = lambda k: [r['tokens'][k] or 0 for r in rows]
    m['tok'] = {k: (sum(tk(k)) / len(rows) if rows else 0) for k in ('in', 'out', 'thoughts', 'cached')}
    return m


def cost_block(m, price):
    if not price:
        return None, None
    ti, to, tc = m['tok']['in'], m['tok']['out'] + m['tok']['thoughts'], m['tok']['cached']
    per_call = ((ti - tc) * price['in'] + tc * price['cached'] + to * price['out']) / 1e6
    return per_call, price


def write_report(res, mets, rc, rw, p, bud, ids, cfgs, sane):
    L = []
    A = L.append
    A('# Phase 1e — three-layer hybrid (L1 checker / L2 grammar veto / L3 model)\n')
    A('Models: Flash-Lite `%s`, Flash `%s`. Thinking config: %s\n'
      % (ids['lite'], ids['flash'], json.dumps({k: v.get('thinking') for k, v in cfgs.items() if k != '_ids'})))
    A('Sanity: %s\n' % ('L1 100/235 = 42.6 % and 0 real false acceptances reproduced' if sane
                        else '**WARNING — Phase 1c baseline NOT reproduced, see stdout**'))
    A('\n## 1. Per model x prompt variant\n')
    A('| config | sent to L3 | end-to-end coverage /235 (baseline 42.6 %) | end-to-end FA /105 | FA by type | L2 caught (no model call) |')
    A('|---|---|---|---|---|---|')
    for m in mets:
        cov = ('%.1f %% measured on n=%d + extrapolated %.1f %%' % (100 * m['coverage_measured'], m['n_correct_sent'],
                                                                   100 * m['coverage_extrapolated'])
               if m['sampled'] and m['coverage_measured'] is not None
               else ('%.1f %%' % (100 * m['coverage_measured']) if m['coverage_measured'] is not None else 'n/a'))
        A('| %s%s | %d | %s | %d | %s | %d |' % (
            m['tag'], ' (INCOMPLETE: %s)' % m['incomplete'] if m['incomplete'] else '', m['sent'], cov,
            m['fa_total_end_to_end'], json.dumps(m['fa_by_type']), len(rw['L2'])))
    A('\nL1 false acceptances carried into every row: %d of 105 (all judged tip-accept / valid reading in Phase 1c, 0 real).'
      % len(rw['L1']))
    A('\n## 2. Layer shares\n')
    tot = 340
    A('| set | L1 | L2 | L3 |')
    A('|---|---|---|---|')
    A('| all 340 | %d (%.1f %%) | %d (%.1f %%) | %d (%.1f %%) |' % (
        len(rc['L1']) + len(rw['L1']), 100 * (len(rc['L1']) + len(rw['L1'])) / tot,
        len(rc['L2']) + len(rw['L2']), 100 * (len(rc['L2']) + len(rw['L2'])) / tot,
        len(rc['L3']) + len(rw['L3']), 100 * (len(rc['L3']) + len(rw['L3'])) / tot))
    A('| 235 correct | %d (%.1f %%) | %d (%.1f %%) | %d (%.1f %%) |' % (
        len(rc['L1']), 100 * len(rc['L1']) / 235, len(rc['L2']), 100 * len(rc['L2']) / 235,
        len(rc['L3']), 100 * len(rc['L3']) / 235))
    A('\n## 3. L3 latency (ms)\n')
    A('| config | warm median | warm p95 | cold first call(s) |')
    A('|---|---|---|---|')
    for m in mets:
        A('| %s | %s | %s | %s |' % (m['tag'], m['lat_median'], m['lat_p95'], m['lat_cold']))
    A('\n## 4. Tokens and cost\n')
    A('| config | in | out | thoughts | cached | $/L3 call | $/active user/month |')
    A('|---|---|---|---|---|---|---|')
    l3_share = len(rc['L3']) / 235
    A('')
    rows = []
    for m in mets:
        price = PRICE['lite'] if ids['lite'] in m['tag'] else PRICE['flash']
        per_call, pr = cost_block(m, price)
        monthly = per_call * 20 * 30 * l3_share if per_call is not None else None
        rows.append('| %s | %.1f | %.1f | %.1f | %.1f | %s | %s |' % (
            m['tag'], m['tok']['in'], m['tok']['out'], m['tok']['thoughts'], m['tok']['cached'],
            ('$%.6f' % per_call) if per_call is not None else 'None',
            ('$%.4f' % monthly) if monthly is not None else 'None'))
    L[-1:] = rows
    A('\nAssumption: 20 exercises/day x 30 days, and the L3 share measured on the correct-answer distribution '
      '(%d of 235 = %.1f %% of answers reach the model when the learner is right). Flash-Lite $0.25 in / $1.50 out / '
      '$0.025 cached per 1M. 3.7 Flash %s' % (len(rc['L3']), 100 * l3_share, PRICE['flash']['src']))
    A('\n## 5. Disagreements\n')
    for m in mets:
        tag = m['tag']
        rws = res.get(tag, {}).get('rows', [])
        bad = [r for r in rws if (r['set'] == 'correct' and r['verdict'] not in ('SAME', 'TIP'))
               or (r['set'] == 'wrong' and r['verdict'] in ('SAME', 'TIP'))]
        A('\n**%s** — %d disagreements\n' % (tag, len(bad)))
        A('| id | set/type | Slovak | reference | learner answer | model |')
        A('|---|---|---|---|---|---|')
        for r in bad:
            it = r['item']
            A('| %d | %s/%s | %s | %s | %s | %s |' % (it['exercise_id'], r['set'], r['type'] or '-',
                                                      it['sk'], it['reference'], it['answer'], r['verdict']))
    A('\n## 6. Budget\n')
    A('- calls used: %d of the %d cap (%d HTTP attempts, cap %d)' % (bud.used, CALL_CAP, bud.attempts, ATTEMPT_CAP))
    A('- 429 "free tier rate-limited" responses: %d' % bud.r429)
    A('- free tier throughout: %s' % ('yes, no 429-forced switch' if bud.r429 == 0 else 'no — %d rate limits hit' % bud.r429))
    A('- %s' % p['cut'])
    A('\n## 7. Selfcheck\n')
    A('```\n%s\n```' % selfcheck(quiet=True))
    md = '\n'.join(L) + '\n'
    open(os.path.join(HERE, 'results.md'), 'w').write(md)
    return md


def do_run():
    bud = Budget()
    cfgs = json.load(open(MODEL_CFG)) if os.path.exists(MODEL_CFG) else {}
    ids = cfgs.get('_ids')
    if not ids:
        lite, f37 = list_models()
        ids = {'lite': lite, 'flash': f37}
        cfgs['_ids'] = ids
        json.dump(cfgs, open(MODEL_CFG, 'w'), ensure_ascii=False, indent=1)
    lite, f37 = ids['lite'], ids['flash']
    dflt = {'thinkingConfig': THINK_LADDER[0], 'max_output': 8, 'thinking': 'default'}
    correct, wrong = load_items()
    rc, rw = routing(correct, wrong)
    sane = sanity(rc, rw)
    p = plan(rc, rw, bud)
    print_plan(rc, rw, p)
    res, rng = {}, random.Random(1)
    if p['mode'] == 'full':
        items = rc['L3'] + rw['L3']
        for v in ('P-A', 'P-B'):
            run_config(bud, lite, v, items, cfgs.get(lite, dflt), '%s x %s' % (lite, v), res)
    else:
        sample = rng.sample(rc['L3'], p['stage1']['correct_sample'])
        items = rw['L3'] + sample
        for v in ('P-A', 'P-B'):
            run_config(bud, lite, v, items, cfgs.get(lite, dflt), '%s x %s' % (lite, v), res)
    mets = [metrics(t, res, rc, rw) for t in list(res)]
    if p['mode'] == 'full' and mets:
        best = sorted(mets, key=lambda m: (m['wrong_accepted'], -m['correct_accepted']))[0]
        v = best['tag'].split(' x ')[1]
        rem = CALL_CAP - bud.used
        n_w = min(len(rw['L3']), rem)
        sample = rng.sample(rc['L3'], max(0, min(len(rc['L3']), rem - n_w)))
        print('stage 2: %s with %s on %d wrong + %d sampled correct (seed 1); remaining budget %d'
              % (f37, v, n_w, len(sample), rem))
        run_config(bud, f37, v, rw['L3'][:n_w] + sample, cfgs.get(f37, dflt), '%s x %s' % (f37, v), res)
        mets = [metrics(t, res, rc, rw) for t in list(res)]
    json.dump({'plan': p, 'ids': ids, 'sanity_ok': sane,
               'routing': {'correct': {k: len(v) for k, v in rc.items()}, 'wrong': {k: len(v) for k, v in rw.items()}},
               'metrics': mets, 'calls_used': bud.used, 'r429': bud.r429},
              open(os.path.join(HERE, 'results.json'), 'w'), ensure_ascii=False, indent=1, default=str)
    print(write_report(res, mets, rc, rw, p, bud, ids, cfgs, sane))


# ---------------------------------------------------------------- selfcheck
def selfcheck(quiet=False):
    out = []
    r = subprocess.run(['git', '-C', APP, 'check-ignore', '-q', '.env.local'], cwd=APP)
    out.append('selfcheck(a) .env.local git-ignored: %s' % ('PASS' if r.returncode == 0 else 'FAIL'))
    k = None
    try:
        for line in open(ENV):
            if line.strip().startswith('GEMINI_API_KEY'):
                k = line.split('=', 1)[1].strip().strip('"').strip("'")
    except Exception:
        pass
    bad = []
    if k:
        for root, _d, fs in os.walk(HERE):
            for f in fs:
                pth = os.path.join(root, f)
                try:
                    if k in open(pth, errors='replace').read():
                        bad.append(os.path.relpath(pth, HERE))
                except Exception:
                    pass
    out.append('selfcheck(b) key value absent from phase1e/: %s%s'
               % ('PASS' if not bad else 'FAIL', (' — ' + ', '.join(bad)) if bad else ''))
    txt = '\n'.join(out)
    if not quiet:
        print(txt)
    return txt


def do_dry():
    correct, wrong = load_items()
    print('loaded: %d held-out correct, %d wrong' % (len(correct), len(wrong)))
    rc, rw = routing(correct, wrong)
    sanity(rc, rw)
    bud = Budget()
    p = plan(rc, rw, bud)
    print_plan(rc, rw, p)


def main():
    a = sys.argv[1:]
    act = a[0] if a else '--dry'
    if act == '--dry':
        do_dry()
    elif act == '--probe':
        probe()
    elif act == '--probe1':
        probe_one(a[1], a[2], a[3])
    elif act == '--run':
        do_run()
    elif act == '--selfcheck':
        pass
    else:
        print(__doc__)
        sys.exit(1)
    print('')
    selfcheck()


if __name__ == '__main__':
    main()
