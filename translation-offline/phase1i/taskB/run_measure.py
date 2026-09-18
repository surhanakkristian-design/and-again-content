"""Task B measurement on DEV. TASKB_CALLS=1 makes model calls for the items the fix releases to L3."""
import os, sys, json, time, collections, urllib.request, urllib.error
HERE = os.path.dirname(os.path.abspath(__file__)); P1I = os.path.dirname(HERE)
sys.path.insert(0, P1I); sys.path.insert(0, HERE)
import checker_1i as C
from loader import load_items, load_annotations
import lock_fix, backfill_s_ids

URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent'
MODEL = 'gemini-3.1-flash-lite'
LEDGER = os.path.join(HERE, 'calls.jsonl')
CALLS = os.environ.get('TASKB_CALLS') == '1'
MAX_CALLS = 150
ROW7 = {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 1}


def cp(k, n, alpha=0.05):
    if n == 0:
        return (0.0, 100.0)
    try:
        from scipy.stats import beta
        lo = 0.0 if k == 0 else beta.ppf(alpha / 2, k, n - k + 1)
        hi = 1.0 if k == n else beta.ppf(1 - alpha / 2, k + 1, n - k)
        return (round(100 * lo, 2), round(100 * hi, 2))
    except Exception:
        pass
    from math import comb
    def cdf(p, kk, n): return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(kk + 1))
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid) > 0: lo = mid
            else: hi = mid
        return (lo + hi) / 2
    lo = 0.0 if k == 0 else bis(lambda p: cdf(p, k - 1, n) - (1 - alpha / 2))
    hi = 1.0 if k == n else bis(lambda p: cdf(p, k, n) - alpha / 2)
    return (round(100 * lo, 2), round(100 * hi, 2))


recs = load_items('dev'); ann = load_annotations('dev')
for s, a in ann.items(): C._ANN[int(s)] = a['hygienised']
for r in recs: C.SK_OF[r['sid']] = r['sk']


def to_item(r):
    return {'item_id': r['item_id'], 'kind': r['kind'], 'exercise_id': r['sid'], 'set': 'NEW',
            'level': r['level'], 'topic': r['topic'], 'sk': r['sk'], 'reference': r['reference'],
            'answer': r['answer'], 'verdict': r['chk']['verdict'], 'step': r['chk']['step'],
            'feedback': r['chk']['feedback'], 'chk_missing': r.get('chk_missing', False),
            'wrong_type': r['wrong_type'], 'wrong_why': '', 'locks': r['locks'], 'lock_ok': r['lock_ok'],
            'lock_released_2_1': r['lock_released_2_1'], 'fa_class': None, 'fa_judgement': None,
            'n': r['n']}


items = {r['item_id']: to_item(r) for r in recs}
by = {r['item_id']: r for r in recs}
vm = {r['item_id']: r['rows']['row7']['model'] for r in recs if r['rows']['row7']['model']}

# ---------------- baseline, must reproduce row7 exactly (apparatus check)
base_out, mism = {}, []
for i, it in items.items():
    d = C.decide(it, ROW7, vm); base_out[i] = d
    r7 = by[i]['rows']['row7']
    if d['layer'] != r7['layer'] or bool(d['accepted']) != bool(r7['accepted']) or d['verdict'] != r7['verdict']:
        mism.append((i, d['layer'], d['accepted'], d['verdict'], r7['layer'], r7['accepted'], r7['verdict']))
print('baseline mismatches vs stored row7:', len(mism))
for m in mism[:10]: print('  ', m)

# ---------------- backfill + patch
bf = backfill_s_ids.apply_to_checker(C)
print('backfill:', {k: v for k, v in bf.items() if k != 'per_sid'})
patch = lock_fix.apply(C, syn=True, gender=True, contraction=True)

post_out = {i: C.decide(it, ROW7, vm) for i, it in items.items()}
released = [i for i in items if base_out[i]['layer'] == 'L2' and post_out[i]['layer'] != 'L2']
print('released from L2:', len(released))
for i in released:
    r = by[i]
    print('   ', i, r['kind'], r['judged'], r['wrong_type'], '| now', post_out[i]['layer'],
          post_out[i]['why'], '|', json.dumps(patch['releases'].get(i), ensure_ascii=False),
          '| ans:', r['answer'])
# part-by-part attribution
parts = {}
for name, kw in (('syn', dict(syn=True, gender=False, contraction=False)),
                 ('gender', dict(syn=False, gender=True, contraction=False)),
                 ('contraction', dict(syn=False, gender=False, contraction=True))):
    p = lock_fix.apply(C, **kw)
    o = {i: C.decide(it, ROW7, vm) for i, it in items.items()}
    parts[name] = [i for i in items if base_out[i]['layer'] == 'L2' and o[i]['layer'] != 'L2']
    print('part %-11s releases %d %s' % (name, len(parts[name]), parts[name]))
patch = lock_fix.apply(C, syn=True, gender=True, contraction=True)

if released:
    e = items[released[0]]
    print('--- prompt sample ---'); print(C.prompt(e, 'P-B')); print('--- end ---')

# ---------------- model calls for the released items only
def log(row):
    with open(LEDGER, 'a') as f: f.write(json.dumps(row, ensure_ascii=False) + '\n')


def call_one(it):
    key = C.base.load_key()
    if not key: raise SystemExit('NO GEMINI_API_KEY')
    body = {'systemInstruction': {'parts': [{'text': C.base.SYS}]},
            'contents': [{'role': 'user', 'parts': [{'text': C.prompt(it, 'P-B')}]}],
            'generationConfig': {'temperature': 0, 'maxOutputTokens': 24,
                                 'thinkingConfig': {'thinkingBudget': 0}}}
    data = json.dumps(body).encode()
    for attempt in range(5):
        t0 = time.time()
        req = urllib.request.Request(URL, data=data, headers={'content-type': 'application/json',
                                                              'x-goog-api-key': key})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                js = json.loads(resp.read().decode()); http = resp.status
        except urllib.error.HTTPError as ex:
            http = ex.code
            try: txt = ex.read().decode()[:300]
            except Exception: txt = ''
            txt = txt.replace(key, '<redacted>') if key else txt
            log({'ts': time.time(), 'model': MODEL, 'variant': 'P-B', 'item_id': it['item_id'],
                 'http': http, 'counted': False, 'verdict': None, 'reply': txt, 'finish': None,
                 'latency_ms': int(1000 * (time.time() - t0)), 'attempt': attempt + 1,
                 'thinking': '{"thinkingBudget": 0}', 'max_output': 24})
            if http in (429, 500, 502, 503, 504) and attempt < 4:
                time.sleep(2 ** attempt * 2); continue
            return None, 'HTTP %s' % http
        except Exception as ex:
            msg = str(ex)[:200]
            if key: msg = msg.replace(key, '<redacted>')
            log({'ts': time.time(), 'model': MODEL, 'variant': 'P-B', 'item_id': it['item_id'],
                 'http': 0, 'counted': False, 'verdict': None, 'reply': msg, 'finish': None,
                 'latency_ms': int(1000 * (time.time() - t0)), 'attempt': attempt + 1,
                 'thinking': '{"thinkingBudget": 0}', 'max_output': 24})
            if attempt < 4:
                time.sleep(2 ** attempt * 2); continue
            return None, 'ERR'
        lat = int(1000 * (time.time() - t0))
        v = C.base.parse_verdict(js)
        if isinstance(v, (list, tuple)):
            v = v[0]          # parse_verdict returns (verdict, text, usage, finish)
        cand = (js.get('candidates') or [{}])[0]
        reply = ''.join(p.get('text', '') for p in ((cand.get('content') or {}).get('parts') or []))
        um = js.get('usageMetadata') or {}
        log({'ts': time.time(), 'model': MODEL, 'variant': 'P-B', 'item_id': it['item_id'], 'http': http,
             'counted': True, 'verdict': v, 'reply': reply, 'finish': cand.get('finishReason'),
             'latency_ms': lat, 'attempt': attempt + 1, 'thinking': '{"thinkingBudget": 0}',
             'max_output': 24, 'prompt_tokens': um.get('promptTokenCount'),
             'candidates_tokens': um.get('candidatesTokenCount'),
             'thoughts_tokens': um.get('thoughtsTokenCount'), 'cached_tokens': um.get('cachedContentTokenCount')})
        return v, None
    return None, 'ERR'


new_v, failed = {}, []
if CALLS:
    prior = {}
    if os.path.exists(LEDGER):
        for line in open(LEDGER):
            try: row = json.loads(line)
            except Exception: continue
            pv = row.get('verdict')
            if isinstance(pv, (list, tuple)): pv = pv[0]
            if row.get('counted') and pv: prior[row['item_id']] = pv
    assert len(released) <= MAX_CALLS, 'budget'
    for i in released:
        if i in prior:
            v = prior[i]
        else:
            v, err = call_one(items[i])
        if v in ('SAME', 'TIP', 'DIFF'): new_v[i] = v
        else: failed.append(i)
    print('calls: made/cached %d, verdicts %d, failed %d %s' % (len(released), len(new_v), len(failed), failed))

vm2 = dict(vm); vm2.update(new_v)
final_out = {i: C.decide(it, ROW7, vm2) for i, it in items.items()}


def acc(d, tip_reject):
    if not d['accepted']: return False
    if tip_reject and d['verdict'] == 'correct_with_tip': return False
    return True


def score(out, tip_reject):
    cov_n = [r for r in recs if r['kind'] == 'C' and r['judged'] == 'correct']
    fa_n = [r for r in recs if r['kind'] == 'W' and r['judged'] == 'wrong']
    cov = [r['item_id'] for r in cov_n if acc(out[r['item_id']], tip_reject)]
    fa = [r['item_id'] for r in fa_n if acc(out[r['item_id']], tip_reject)]
    byt = {}
    for t in ('T', 'W', 'M', 'S'):
        d = [r for r in fa_n if r['wrong_type'] == t]
        k = [r['item_id'] for r in d if acc(out[r['item_id']], tip_reject)]
        byt[t] = {'k': len(k), 'n': len(d), 'pct': round(100 * len(k) / max(1, len(d)), 2),
                  'ci': cp(len(k), len(d)), 'ids': k}
    return {'coverage': {'k': len(cov), 'n': len(cov_n), 'pct': round(100 * len(cov) / len(cov_n), 2),
                         'ci': cp(len(cov), len(cov_n)), 'ids': cov},
            'fa': {'k': len(fa), 'n': len(fa_n), 'pct': round(100 * len(fa) / len(fa_n), 2),
                   'ci': cp(len(fa), len(fa_n)), 'ids': fa}, 'fa_by_type': byt}


res = {'released': released, 'releases': patch['releases'], 'backfill': {k: v for k, v in bf.items() if k != 'per_sid'},
       'baseline_mismatches': mism, 'parts': parts, 'model': {'calls': len(released), 'verdicts': new_v,
       'failed': failed}, 'scorings': {}}
for name, tr in (('tip_accept', False), ('tip_reject', True)):
    b, a = score(base_out, tr), score(final_out, tr)
    res['scorings'][name] = {
        'before': {k: {kk: vv for kk, vv in b[k].items() if kk != 'ids'} for k in ('coverage', 'fa')},
        'after': {k: {kk: vv for kk, vv in a[k].items() if kk != 'ids'} for k in ('coverage', 'fa')},
        'fa_by_type_before': {t: {k: v for k, v in b['fa_by_type'][t].items() if k != 'ids'} for t in b['fa_by_type']},
        'fa_by_type_after': {t: {k: v for k, v in a['fa_by_type'][t].items() if k != 'ids'} for t in a['fa_by_type']},
        'recovered_correct': sorted(set(a['coverage']['ids']) - set(b['coverage']['ids'])),
        'lost_correct': sorted(set(b['coverage']['ids']) - set(a['coverage']['ids'])),
        'new_fa': sorted(set(a['fa']['ids']) - set(b['fa']['ids'])),
        'new_fa_types': collections.Counter(by[i]['wrong_type'] for i in set(a['fa']['ids']) - set(b['fa']['ids'])),
    }
    print('== %s ==' % name)
    print('   coverage %d/%d %.1f%% %s -> %d/%d %.1f%% %s' % (b['coverage']['k'], b['coverage']['n'], b['coverage']['pct'], b['coverage']['ci'], a['coverage']['k'], a['coverage']['n'], a['coverage']['pct'], a['coverage']['ci']))
    print('   FA       %d/%d %.1f%% %s -> %d/%d %.1f%% %s' % (b['fa']['k'], b['fa']['n'], b['fa']['pct'], b['fa']['ci'], a['fa']['k'], a['fa']['n'], a['fa']['pct'], a['fa']['ci']))
    print('   by type before', {t: '%d/%d' % (b['fa_by_type'][t]['k'], b['fa_by_type'][t]['n']) for t in 'TWMS'})
    print('   by type after ', {t: '%d/%d' % (a['fa_by_type'][t]['k'], a['fa_by_type'][t]['n']) for t in 'TWMS'})
    print('   recovered', res['scorings'][name]['recovered_correct'], 'lost', res['scorings'][name]['lost_correct'], 'new FA', res['scorings'][name]['new_fa'])
# lock-outcome change on every WRONG answer
wrong_chg = []
for r in recs:
    if r['kind'] != 'W': continue
    i = r['item_id']
    if base_out[i]['layer'] == 'L2' and final_out[i]['layer'] != 'L2':
        wrong_chg.append({'item_id': i, 'judged': r['judged'], 'wrong_type': r['wrong_type'],
                          'answer': r['answer'], 'lock': r['locks'], 'release': patch['releases'].get(i),
                          'now': final_out[i]['layer'], 'accepted': final_out[i]['accepted'],
                          'verdict': final_out[i]['verdict']})
res['wrong_lock_outcome_changed'] = wrong_chg
print('WRONG answers whose lock outcome changed:', len(wrong_chg))
for w in wrong_chg: print('   ', w)
res['dev_l2_rejected_baseline'] = sorted(i for i in items if base_out[i]['layer'] == 'L2')
json.dump(res, open(os.path.join(HERE, 'results.json'), 'w'), ensure_ascii=False, indent=1)
print('wrote results.json ; calls mode', CALLS)
