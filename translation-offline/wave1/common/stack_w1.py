#!/usr/bin/env python3
"""Wave 1 checker stack for native de / ua / es -> English (brief "Checker for the new languages").
  L3 SOURCE-ONLY (gemini-3.1-flash-lite, temperature 0, thinkingBudget 0; prompts_w1.l3_request: the language's
     sentence + the answer, nothing else): SAME -> content check, TIP -> REJECT, DIFF -> reject, failed reply -> reject.
  content check (prompts_w1.cc_request, the same model): NONE -> accept, MISSING -> reject, failed call -> keeps the
     L3 accept (= phase2l content_check.decide, TIP rejected).
  NO F4 and NO AG guards (they exist only for sk/cz).  No exact-reference layer (2K removed L1).
Transport = byte copy of phase2l/run_2i_base.py (call_one: counted = HTTP 200 only; rate limit ONLY from the HTTP
status / error envelope; daily/usage quota envelope -> STOP; empty or unparsable 200 = counted FAILED call, never
retried, never guessed); the content-check parser = byte copy of phase2l/content_check.py (parse / decide / transport).
Caps (brief: Gemini HARD CAP 5,000 calls and $1.50 for the wave, counted = HTTP 200 only): per language 1,800 calls and
$0.50 (3 x $0.50 = $1.50); the stage cap = min(language cap - the language's other stages, 5,000 - every other counted
call of the wave), checked before any call (counted + needed > cap -> STOP, 0 calls) and before every call, and the wave
total over wave1/{de,ua,es}/GEMINI_LEDGER.json is re-read before every call (a call that would be the 5,001st -> STOP).
Items reach the stack wrapped in PoisonDict: reading a reference key (en, v, alt, lk, lk_*, reference, english, ...)
raises PoisonHit.  Every path must be ABSOLUTE and lie under wave1/; anything else is REFUSED before anything opens."""
import contextlib, json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
W1 = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import run_2i_base as B      # noqa: E402  byte copy of phase2l/run_2i_base.py
import content_check as CC   # noqa: E402  byte copy of phase2l/content_check.py (parse / decide / transport only)
import prompts_w1 as P       # noqa: E402
LANGS = tuple(sorted(P.LANG))
LANG_CAP, LANG_SPEND = 1800, 0.50
WAVE_CAP, WAVE_SPEND = 5000, 1.50
# tr/hu retry (brief 23 Sept 2026): the ledgers under wave1/retry_trhu are their own wave, HARD CAP 4,000 calls / $1.00.
RETRY_ROOT = os.path.join(W1, 'retry_trhu')
RETRY_CAP, RETRY_SPEND = 4000, 1.00


def wave_caps(root=W1):
    return (RETRY_CAP, RETRY_SPEND) if os.path.normpath(root) == RETRY_ROOT else (WAVE_CAP, WAVE_SPEND)
Stop = B.Stop
REF_KEYS = ('en', 'v', 'alt', 'lk', 'reference', 'references', 'refs', 'english', 'en_full_sentence',
            'full_sentence_en', 'translation', 'headword', 'correct_answer_en')


class Refused(Exception):
    pass


class PoisonHit(BaseException):
    pass


def is_ref(k):
    return isinstance(k, str) and (k in REF_KEYS or k.startswith('lk_'))


class PoisonDict(dict):
    def _c(self, k):
        if is_ref(k):
            raise PoisonHit(k)

    def __getitem__(self, k):
        self._c(k); return dict.__getitem__(self, k)

    def get(self, k, d=None):
        self._c(k); return dict.get(self, k, d)

    def __contains__(self, k):
        self._c(k); return dict.__contains__(self, k)

    def pop(self, k, *d):
        self._c(k); return dict.pop(self, k, *d)


def must_abs(p, what):
    if not isinstance(p, str) or not os.path.isabs(p):
        raise Refused('REFUSED: %s must be an absolute path, got %r' % (what, p))


def guard_path(p, what):
    must_abs(p, what)
    ap = os.path.normpath(p)
    if not ap.startswith(W1 + os.sep):
        raise Refused('REFUSED: %s must lie under %s, got %r' % (what, W1, p))


def read_json(p, d):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return d


def write_json(p, o):
    tmp = p + '.tmp'
    json.dump(o, open(tmp, 'w', encoding='utf-8'), indent=1, sort_keys=True, ensure_ascii=False)
    os.replace(tmp, p)


def lang_ledger(lang, root=W1):
    return os.path.join(root, lang, 'GEMINI_LEDGER.json')


def wave_langs(lang=None):
    """The languages of lang's wave (wave 1 de/ua/es, wave 2 fr/tr/hu: separate 5,000-call / $1.50 caps); None = wave 1."""
    w = P.WAVE.get(lang, 1)
    return tuple(lg for lg in LANGS if P.WAVE[lg] == w)


def wave_counted(root=W1, lang=None):
    return sum(int(v) for lg in wave_langs(lang) for v in read_json(lang_ledger(lg, root), {}).values())


@contextlib.contextmanager
def wave_lock(root=W1):
    import fcntl
    with open(os.path.join(root, '.wave.lock'), 'w') as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


def spend_of(d):
    tot = 0.0
    for dp, dn, fn in os.walk(d):
        if 'ledger.jsonl' in fn:
            tot += sum(float(r.get('cost_usd') or 0) for r in B.jl_read(os.path.join(dp, 'ledger.jsonl'))
                       if r.get('http') == 200)
    return tot


def lang_spend(root, lg):
    """A language's HTTP-200 spend: <lang>/run (test layout) + <lang>/partD/run (the production layout; 23 Sept 2026 fix:
    the wave-1 code read only <lang>/run, so the spend guard never saw the other stage of the same language)."""
    return sum(spend_of(p) for p in (os.path.join(root, lg, 'run'), os.path.join(root, lg, 'partD', 'run')) if os.path.isdir(p))


def wave_spend(root=W1, lang=None):
    return sum(lang_spend(root, lg) for lg in wave_langs(lang))


def clean_item(it):
    """Only jid / sid / level / src / answer leave the item; a reference key read raises PoisonHit."""
    it = it if isinstance(it, PoisonDict) else PoisonDict(it)
    return {'jid': it['jid'], 'sid': it.get('sid'), 'level': it.get('level'), 'src': it['src'], 'answer': it['answer']}


def run_calls(kind, items, run_dir, stage, lang, ledger_path, key=None, root=W1, expect_needed=None):
    """kind 'l3' | 'cc'.  One row per jid in run_dir/replies.jsonl; identical requests are called once."""
    for p, w in ((run_dir, 'run dir'), (ledger_path, 'ledger'), (root, 'root')):
        guard_path(p, w) if p != W1 else None
    if lang not in LANGS:
        raise Refused('REFUSED: language %r (de|ua|es|fr|tr|hu)' % (lang,))
    build = P.l3_request if kind == 'l3' else P.cc_request
    os.makedirs(run_dir, exist_ok=True)
    PP = B.paths(run_dir)
    RP = os.path.join(run_dir, 'replies.jsonl')
    jids = [it['jid'] for it in items]
    if len(set(jids)) != len(jids):
        raise Refused('REFUSED: duplicate jid')
    done = {r['jid'] for r in B.jl_read(RP)}
    todo = [it for it in items if it['jid'] not in done]
    got = {}
    for row in B.jl_read(PP['ledger']):
        if row.get('http') == 200 and row.get('req_key') and row['req_key'] not in got:
            got[row['req_key']] = row
    phase = read_json(ledger_path, {})
    others = sum(int(v) for k, v in phase.items() if k != stage)
    counted0 = sum(1 for r in B.jl_read(PP['ledger']) if r.get('http') == 200)
    wave_other = wave_counted(root, lang) - sum(int(v) for v in phase.values())
    wcap, wspend = wave_caps(root)
    cap = min(LANG_CAP - others, wcap - wave_other - others)
    spent_here = spend_of(run_dir)
    spent_lang = lang_spend(root, lang)
    spent_lang_other = spent_lang - spent_here
    spent_wave_other = wave_spend(root, lang) - spent_lang
    ctx = {'P': PP, 'cap': cap, 'spend_cap': min(LANG_SPEND - spent_lang_other, wspend - spent_wave_other - spent_lang_other),
           'key': None, 'last': 0.0, 'made': 0, 'uncounted': 0, 'counted': counted0, 'spent': spent_here,
           'est': B.EST_CALL_USD}

    def sync():
        phase[stage] = ctx['counted']
        write_json(ledger_path, phase)
    st = {'status': 'COMPLETE', 'kind': kind, 'stage': stage, 'lang': lang, 'items': len(items), 'todo_items': len(todo),
          'requests': 0, 'unique_requests': 0, 'needed': 0, 'calls_made': 0, 'stop': None, 'cap_for_stage': cap,
          'other_stages_counted': others, 'wave_other_languages_counted': wave_other, 'mock': key == 'MOCK'}
    if todo:
        reqs = {it['jid']: build(lang, it['src'], it['answer']) for it in todo}
        rq, users = {}, {}
        for j, q in sorted(reqs.items()):
            k = q['k'] = B.req_key(q)
            rq[k] = q
            users.setdefault(k, []).append('%s:%s' % (kind, j))
        need = [k for k in sorted(rq) if k not in got]
        st.update(requests=len(reqs), unique_requests=len(rq), needed=len(need))
        stop = None
        if expect_needed is not None and len(need) != int(expect_needed):
            stop = Stop('expect', 'needed %d != expected %d; NO call was made' % (len(need), int(expect_needed)))
        elif ctx['counted'] + len(need) > cap:
            stop = Stop('cap', 'counted %d + needed %d > cap for this stage %d (language cap %d - other stages %d; wave '
                        'cap %d - other languages %d); NO call was made' % (ctx['counted'], len(need), cap, LANG_CAP,
                                                                              others, wcap, wave_other))
        elif need:
            try:
                ctx['key'] = key or B.load_key()
                with (CC.transport(B) if kind == 'cc' else contextlib.nullcontext()):
                    for k in need:
                        with wave_lock(root):       # check + reserve ONE call under the wave lock (strict 5,000)
                            if wave_counted(root, lang) - sum(int(v) for v in phase.values()) + others + ctx['counted'] + 1 > wcap:
                                raise Stop('wave_cap', 'wave total would exceed %d' % wcap)
                            phase[stage] = ctx['counted'] + 1
                            write_json(ledger_path, phase)
                        try:
                            got[k] = B.call_one(ctx, k, rq[k], users[k])
                        finally:
                            with wave_lock(root):
                                sync()
            except Stop as e:
                stop = e
        sync()
        if stop:
            st.update(status='STOPPED', stop={'kind': stop.kind, 'why': stop.why})
            open(os.path.join(run_dir, 'STOP_%s.md' % stop.kind), 'w', encoding='utf-8').write(
                '# STOP (%s)\n\n%s\n\n%s. Counted calls %d, spend $%.6f. Resume with the same command.\n'
                % (stop.kind, stop.why, B.now(), ctx['counted'], ctx['spent']))
        for it in todo:
            q = reqs[it['jid']]
            row = got.get(q['k'])
            if row is None:
                continue
            v = None if row.get('failed') else row.get('verdict')
            B.jl_append(RP, {'jid': it['jid'], 'level': it.get('level'), 'req_key': q['k'], 'verdict': v,
                             'word': CC.word_of(v) if kind == 'cc' else None, 'failed': bool(row.get('failed')),
                             'raw': row.get('reply'), 'lang': lang, 'ts': B.now()})
    sync()
    rows = B.jl_read(RP)
    fin = {r['jid'] for r in rows}
    missing = sum(1 for j in jids if j not in fin)
    if missing and st['status'] == 'COMPLETE':
        st['status'] = 'INCOMPLETE'
    st.update(calls_made=ctx['made'], uncounted_attempts=ctx['uncounted'], counted_total=ctx['counted'],
              spend_usd=round(ctx['spent'], 6), results_missing=missing, ts=B.now(), phase_ledger=dict(phase),
              failed_items=sum(1 for r in rows if r.get('failed')))
    write_json(PP['status'], st)
    return st


def l3_row(r):
    """L3 reply row -> the SOURCE-ONLY result shape content_check.decide expects."""
    if r is None:
        return None
    if r.get('failed') or r.get('verdict') not in B.VERDICTS:
        return {'accept': False, 'layer': 'L3:failed', 'l3_reply': None}
    v = r['verdict']
    return {'accept': v == 'SAME', 'layer': 'L3:TIPrej' if v == 'TIP' else 'L3', 'l3_reply': v}


TIP_ACCEPT = False


def run_full(items, run_dir, stage, lang, ledger_path, key=None, root=W1):
    clean = [clean_item(it) for it in items]
    l3d, ccd = os.path.join(run_dir, 'l3'), os.path.join(run_dir, 'cc')
    st1 = run_calls('l3', clean, l3d, stage + '_L3', lang, ledger_path, key, root)
    out = {'status': st1['status'], 'l3': st1, 'cc': None, 'tip_accept': TIP_ACCEPT}
    if st1['status'] != 'COMPLETE':
        return out
    res = {r['jid']: l3_row(r) for r in B.jl_read(os.path.join(l3d, 'replies.jsonl'))}
    cand = [c for c in clean if CC.l3_ok(res[c['jid']], TIP_ACCEPT)]
    st2 = run_calls('cc', cand, ccd, stage + '_CC', lang, ledger_path, key, root)
    out.update(cc=st2, status=st2['status'])
    cc = {r['jid']: r for r in B.jl_read(os.path.join(ccd, 'replies.jsonl'))}
    fp = os.path.join(run_dir, 'final_tiprej.jsonl')
    with open(fp, 'w', encoding='utf-8') as fh:
        for c in clean:
            r = res[c['jid']]
            a, layer, s = CC.decide(r, cc.get(c['jid']), TIP_ACCEPT)
            x = cc.get(c['jid']) or {}
            fh.write(json.dumps({'jid': c['jid'], 'sid': c['sid'], 'level': c['level'], 'accept': a, 'layer': layer,
                                 'cc_state': s, 'cc_word': x.get('word'), 'cc_raw': x.get('raw'),
                                 'l3_layer': r.get('layer'), 'l3_reply': r.get('l3_reply'), 'tip_accept': TIP_ACCEPT},
                                ensure_ascii=False, sort_keys=True) + '\n')
    return out
