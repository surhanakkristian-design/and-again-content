#!/usr/bin/env python3
"""Phase 1i — the offline pipeline as ONE importable wrapper module (agent E).

`checker_1i.py` is NEVER hand-edited. This module

  * seeds the frozen checker from the loader's DEV/HOLDOUT data (CONTEXT.md §3),
  * applies Task B (`backfill_s_ids` + `lock_fix`) and Task C (`guards_c`) by FLAGS,
  * builds the prompt variants (P-B frozen, P-E1/2/3/4),
  * makes model calls inside the frozen call shape with Task D's transport rules,
  * scores coverage / false acceptance with exact Clopper-Pearson intervals.

Nothing here reads the holdout: `setup(side)` goes through `loader.load_items`, which owns the guard.
The API key is loaded only inside `load_key()` and never printed, logged or put on a command line.
"""
import json
import math
import os
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (HERE, os.path.join(HERE, 'taskB'), os.path.join(HERE, 'taskC')):
    if _p not in sys.path:
        sys.path.insert(0, _p)

ROW7_FLAGS = {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 1}
MODEL = 'gemini-3.1-flash-lite'
GEN_CFG = {'temperature': 0, 'maxOutputTokens': 24, 'thinkingConfig': {'thinkingBudget': 0}}
API = 'https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent'
ENV = os.path.expanduser('~/Projects/and-again/.env.local')

VARIANTS = ('P-B', 'P-E1', 'P-E2', 'P-E3', 'P-E4a', 'P-E4b')

# ---------------------------------------------------------------- prompt pieces
GENDER_TMPL = ('Gender: the Slovak does not fix the gender here — the reference\'s {words} may equally be '
               'the other gender (he/she, him/her, his/her, himself/herself). An answer that keeps the '
               'meaning but picks the other gender is SAME on that point.')
INFO_LINE = ('Information: any information in the learner sentence that is not in the Slovak, or in the '
             'Slovak but not in the learner sentence, makes it DIFF — including a single adverb, particle, '
             'place word or time word.')
GROUND_LINE = ('The SLOVAK sentence is the ground truth and the English reference is only one valid '
               'rendering of it; judge the learner against the Slovak, not against the reference wording.')
ALT_TMPL = 'Also accepted English: {alts}'
WORDING_LINE = ('A synonym, a different word order or a different phrasing that keeps the Slovak meaning '
                'is SAME; a word that changes which thing, person, place, time or quantity the Slovak '
                'names is DIFF.')
SYS_BINARY_FALLBACK = ('You judge English translations. Reply with exactly one word: SAME or DIFF. '
                       'SAME = the learner sentence means the same as the Slovak. DIFF = it does not. '
                       'No explanation.')

# ---------------------------------------------------------------- checker setup
_ST = None


def setup(side='dev'):
    """Import the frozen checker once and seed it from `loader` (0 model calls, no file writes)."""
    global _ST
    if _ST is not None:
        if _ST['side'] != side:
            raise RuntimeError('pipeline already set up for side %r' % _ST['side'])
        return _ST
    import checker_1i as C
    from loader import load_items, load_annotations
    recs = load_items(side)
    ann = load_annotations(side)
    for s, a in ann.items():
        C._ANN[int(s)] = a.get('hygienised', a)
    for r in recs:
        C.SK_OF[r['sid']] = r['sk']
    _ST = {'C': C, 'recs': recs, 'ann': ann, 'side': side, 'base_decide': C.decide,
           'decide': C.decide, 'b_fix': False, 'guards': (), 'reports': {}}
    return _ST


def configure(b_fix=True, guards=('F4v3',), side='dev'):
    """Apply / remove Task B and Task C on the live checker module. Returns the state dict."""
    st = setup(side)
    C = st['C']
    if b_fix and not st['b_fix']:
        import backfill_s_ids as B
        import lock_fix
        st['reports']['backfill'] = B.apply_to_checker(C)
        st['reports']['lock_fix'] = lock_fix.apply(C, syn=True, gender=True, contraction=True)
        st['b_fix'] = True
    elif (not b_fix) and st['b_fix']:
        import lock_fix
        lock_fix.revert(C)
        st['b_fix'] = False
    import guards_c
    st['decide'] = guards_c.apply(C, guards=tuple(guards))
    st['guards'] = tuple(guards)
    return st


def to_item(r):
    return {'item_id': r['item_id'], 'kind': r['kind'], 'exercise_id': r['sid'], 'set': 'NEW',
            'level': r['level'], 'topic': r['topic'], 'sk': r['sk'], 'reference': r['reference'],
            'answer': r['answer'], 'verdict': r['chk']['verdict'], 'step': r['chk']['step'],
            'feedback': r['chk']['feedback'], 'chk_missing': r.get('chk_missing', False),
            'wrong_type': r['wrong_type'], 'wrong_why': '', 'locks': r['locks'],
            'lock_ok': r['lock_ok'], 'lock_released_2_1': r['lock_released_2_1'],
            'fa_class': None, 'fa_judgement': None, 'n': r['n']}


class VM(dict):
    """A verdict map that records which item_ids the pipeline actually asked for (= reached L3)."""

    def __init__(self, base):
        super().__init__(base)
        self.touched = set()

    def __contains__(self, k):
        self.touched.add(k)
        return dict.__contains__(self, k)

    def __getitem__(self, k):
        self.touched.add(k)
        return dict.__getitem__(self, k)

    def get(self, k, d=None):
        self.touched.add(k)
        return dict.get(self, k, d)


def run_pipeline(st, verdict_map, tip_reject=False):
    """Decide every item of the side. Returns {item_id: row}. 0 model calls (verdicts come from the map)."""
    out = {}
    for r in st['recs']:
        it = to_item(r)
        vm = VM(verdict_map)
        d = st['decide'](it, dict(ROW7_FLAGS), vm)
        acc = bool(d.get('accepted'))
        layer = d.get('layer')
        reached = r['item_id'] in vm.touched
        model = d.get('model') or (verdict_map.get(r['item_id']) if reached else None)
        tipped = bool(acc and model == 'TIP')
        if tip_reject and tipped:
            acc = False
            layer = 'L3:TIPrej'
        out[r['item_id']] = {'item_id': r['item_id'], 'kind': r['kind'], 'judged': r['judged'],
                            'wrong_type': r['wrong_type'], 'half': r['half'], 'level': r['level'],
                            'accepted': acc, 'verdict': d.get('verdict'), 'layer': layer,
                            'model': model, 'tip': bool(d.get('tip')), 'model_tip': tipped,
                            'reached_l3': r['item_id'] in vm.touched}
    return out


# ---------------------------------------------------------------- prompt builders
def pb_lines(st, it):
    """The frozen P-B user prompt, taken from the checker itself, as a list of lines."""
    C = st['C']
    try:
        txt = C.prompt(it, 'P-B')
    except Exception:
        import lib_prev
        txt = lib_prev.prompt(it, 'P-B')
    lines = txt.split('\n')
    assert lines[0].startswith('Slovak:'), lines[:1]
    assert lines[-1].strip().upper().startswith('SAME'), lines[-1]
    return lines


def sys_text(st, variant):
    import lib_prev
    s = lib_prev.SYS
    if variant != 'P-E2':
        return s
    t = s.replace('SAME, TIP or DIFF', 'SAME or DIFF')
    parts = re.split(r'(?<=\.)\s+', t)
    parts = [p for p in parts if 'TIP' not in p.upper()]
    out = ' '.join(parts).strip()
    if 'TIP' in out.upper() or len(out) < 40:
        out = SYS_BINARY_FALLBACK
    return out


def gender_chain(st, sid):
    a = st['ann'].get(str(sid)) or {}
    g = (a.get('hygienised') or a).get('g')
    if not g:
        return None
    words = []
    for entry in g:
        if isinstance(entry, str):
            words.append(entry)
        elif isinstance(entry, (list, tuple)):
            for w in entry:
                words.append(w if isinstance(w, str) else json.dumps(w, ensure_ascii=False))
        else:
            words.append(json.dumps(entry, ensure_ascii=False))
    words = [w for w in words if w]
    return words or None


def alt_refs(st, it, cap=3):
    C = st['C']
    try:
        rs = C.refs_of(it)
    except Exception:
        return []
    out = []
    for r in rs:
        if isinstance(r, str) and r.strip() and r.strip() != (it['reference'] or '').strip():
            if r.strip() not in out:
                out.append(r.strip())
    return out[:cap]


def build_prompt(st, r, variant):
    """(user_text, has_gender, equals_pb) for one item x variant."""
    it = to_item(r)
    lines = pb_lines(st, it)
    head, tail = lines[:-1], lines[-1]
    g = gender_chain(st, r['sid'])
    gline = GENDER_TMPL.format(words=', '.join('"%s"' % w for w in g)) if g else None
    extra = []
    if variant == 'P-B':
        pass
    elif variant == 'P-E1':
        if gline:
            extra = [gline]
    elif variant == 'P-E2':
        tail = 'SAME or DIFF?'
    elif variant == 'P-E3':
        extra = ([gline] if gline else []) + [INFO_LINE]
    elif variant == 'P-E4a':
        alts = alt_refs(st, it)
        extra = ([gline] if gline else []) + [GROUND_LINE]
        if alts:
            extra.append(ALT_TMPL.format(alts=' | '.join('"%s"' % a for a in alts)))
    elif variant == 'P-E4b':
        extra = ([gline] if gline else []) + [GROUND_LINE, WORDING_LINE]
    else:
        raise ValueError(variant)
    user = '\n'.join(head + extra + [tail])
    pb = '\n'.join(lines)
    return user, bool(g), user == pb


def parse_reply(txt, variant):
    up = (txt or '').upper()
    pat = r'\b(SAME|DIFF)\b' if variant == 'P-E2' else r'\b(SAME|TIP|DIFF)\b'
    m = re.search(pat, up)
    return m.group(1) if m else None


# ---------------------------------------------------------------- model calls
_LOCK = threading.Lock()


def load_key():
    if not os.path.exists(ENV):
        raise SystemExit('STOP: %s not found — no GEMINI_API_KEY' % ENV)
    for ln in open(ENV, encoding='utf-8'):
        if ln.strip().startswith('GEMINI_API_KEY'):
            v = ln.split('=', 1)[1].strip().strip('"').strip("'")
            if v:
                return v
    raise SystemExit('STOP: GEMINI_API_KEY missing from the env file')


def _redact(s, key):
    s = str(s or '')
    if key:
        s = s.replace(key, '<redacted>')
    return re.sub(r'(key=)[^&\s]+', r'\1<redacted>', s)[:400]


def _http(url, body, key):
    req = urllib.request.Request(url, data=json.dumps(body).encode('utf-8'),
                                headers={'Content-Type': 'application/json', 'x-goog-api-key': key})
    try:
        with urllib.request.urlopen(req, timeout=60) as rs:
            return rs.status, json.loads(rs.read().decode('utf-8')), ''
    except urllib.error.HTTPError as e:
        try:
            raw = e.read().decode('utf-8')
        except Exception:
            raw = ''
        try:
            js = json.loads(raw)
        except Exception:
            js = None
        return int(e.code), js, raw
    except Exception as e:                       # URLError, timeout, ssl, ...  -> http 0
        return 0, None, '%s: %s' % (type(e).__name__, e)


def ledger_append(path, row):
    with _LOCK:
        with open(path, 'a', encoding='utf-8') as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + '\n')


def call_variant(st, r, variant, ledger, key, tries=5):
    """One model call with Task D's rules. Returns (verdict|None, row). Retries never count."""
    user, _has_g, _pb = build_prompt(st, r, variant)
    sysx = sys_text(st, variant)
    body = {'systemInstruction': {'parts': [{'text': sysx}]},
            'contents': [{'role': 'user', 'parts': [{'text': user}]}],
            'generationConfig': GEN_CFG}
    url = API % MODEL
    delay = 1.0
    for attempt in range(1, tries + 1):
        t0 = time.time()
        st_code, js, raw = _http(url, body, key)
        lat = int((time.time() - t0) * 1000)
        if st_code == 200:
            cands = (js or {}).get('candidates') or []
            txt = ''.join(p.get('text', '') or '' for c in cands
                          for p in ((c.get('content') or {}).get('parts') or []))
            finish = cands[0].get('finishReason') if cands else None
            empty = (not cands) or txt.strip() == ''
            v = parse_reply(txt, variant)
            um = (js or {}).get('usageMetadata') or {}
            row = {'ts': time.time(), 'model': MODEL, 'variant': variant, 'item_id': r['item_id'],
                   'http': 200, 'counted': True, 'verdict': v or 'PARSE_FAIL', 'reply': txt,
                   'finish': finish, 'empty': empty, 'latency_ms': lat, 'try': attempt,
                   'prompt_tokens': um.get('promptTokenCount'),
                   'candidates_tokens': um.get('candidatesTokenCount'),
                   'thoughts_tokens': um.get('thoughtsTokenCount'),
                   'cached_tokens': um.get('cachedContentTokenCount'),
                   'thinking': '{"thinkingBudget": 0}', 'max_output': GEN_CFG['maxOutputTokens']}
            ledger_append(ledger, row)
            return v, row
        row = {'ts': time.time(), 'model': MODEL, 'variant': variant, 'item_id': r['item_id'],
               'http': st_code, 'counted': False, 'verdict': None, 'reply': '', 'finish': None,
               'empty': None, 'latency_ms': lat, 'try': attempt,
               'error': _redact(raw or js, key), 'transport_retry': True}
        ledger_append(ledger, row)
        if attempt == tries:
            return None, row
        time.sleep(delay * (1.0 + random.random() * 0.3))
        delay = min(delay * 2, 16.0)
    return None, row


def ledger_verdicts(path):
    """{(variant, item_id): (verdict, reply)} from HTTP-200 rows only; last row wins."""
    out, fails, retries = {}, {}, 0
    if not os.path.exists(path):
        return out, fails, retries
    for ln in open(path, encoding='utf-8'):
        ln = ln.strip()
        if not ln:
            continue
        try:
            row = json.loads(ln)
        except Exception:
            continue
        if row.get('http') != 200:
            retries += 1
            continue
        k = (row.get('variant'), row.get('item_id'))
        v = row.get('verdict')
        if v in ('SAME', 'TIP', 'DIFF'):
            out[k] = v
            fails.pop(k, None)
        else:
            out.pop(k, None)
            fails[k] = row.get('reply', '')
    return out, fails, retries


# ---------------------------------------------------------------- statistics
def _lbeta(a, b):
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


def _binom_cdf(k, n, p):
    if p <= 0:
        return 1.0
    if p >= 1:
        return 0.0 if k < n else 1.0
    s = 0.0
    for i in range(0, k + 1):
        s += math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                      + i * math.log(p) + (n - i) * math.log1p(-p))
    return min(1.0, s)


def cp(k, n, alpha=0.05):
    """Exact Clopper-Pearson (percent, 2 dp)."""
    if n == 0:
        return [0.0, 0.0]
    lo, hi = 0.0, 1.0
    if k > 0:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if 1.0 - _binom_cdf(k - 1, n, m) > alpha / 2:
                b = m
            else:
                a = m
        lo = (a + b) / 2
    if k < n:
        a, b = 0.0, 1.0
        for _ in range(200):
            m = (a + b) / 2
            if _binom_cdf(k, n, m) < alpha / 2:
                b = m
            else:
                a = m
        hi = (a + b) / 2
    else:
        hi = 1.0
    return [round(lo * 100, 2), round(hi * 100, 2)]


def rate(k, n):
    return {'k': k, 'n': n, 'pct': round(100.0 * k / n, 2) if n else None, 'ci': cp(k, n)}


def metrics(st, res):
    recs = {r['item_id']: r for r in st['recs']}
    corr = [i for i, r in recs.items() if r['kind'] == 'C' and r['judged'] == 'correct']
    wrong = [i for i, r in recs.items() if r['judged'] == 'wrong']
    acc_c = [i for i in corr if res[i]['accepted']]
    fa = [i for i in wrong if res[i]['accepted']]
    m = {'coverage': rate(len(acc_c), len(corr)), 'fa': rate(len(fa), len(wrong)),
         'fa_by_type': {}, 'fa_by_layer': {}, 'fa_by_half': {}, 'fa_items': [],
         'false_rejections': [], 'fr_by_layer': {}, 'tip_accepts': 0, 'failed_items': []}
    for t in ('T', 'W', 'M', 'S'):
        n = [i for i in wrong if recs[i]['wrong_type'] == t]
        k = [i for i in n if res[i]['accepted']]
        m['fa_by_type'][t] = rate(len(k), len(n))
    for h in ('OLD', 'NEW'):
        n = [i for i in wrong if recs[i]['half'] == h]
        m['fa_by_half'][h] = rate(len([i for i in n if res[i]['accepted']]), len(n))
    for i in sorted(fa):
        lay = res[i]['layer']
        m['fa_by_layer'][lay] = m['fa_by_layer'].get(lay, 0) + 1
        m['fa_items'].append({'id': i, 'type': recs[i]['wrong_type'], 'layer': lay,
                              'verdict': res[i]['verdict'], 'model': res[i]['model'],
                              'half': recs[i]['half']})
    for i in sorted(set(corr) - set(acc_c)):
        lay = res[i]['layer']
        m['fr_by_layer'][lay] = m['fr_by_layer'].get(lay, 0) + 1
        m['false_rejections'].append({'id': i, 'layer': lay, 'model': res[i]['model'],
                                      'half': recs[i]['half']})
    m['tip_accepts'] = sum(1 for i in res if res[i]['accepted'] and res[i]['model_tip'])
    m['failed_items'] = sorted(i for i in res if res[i]['verdict'] == 'failed')
    return m
