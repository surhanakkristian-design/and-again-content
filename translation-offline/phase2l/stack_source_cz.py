#!/usr/bin/env python3
# Phase 2L Part D: byte copy of stack_source.py (= phase2k/stack_source.py) except load(): lang cz only, the
# Czech reader assembled into the AG chain by cz_assemble.assemble(), F4v2/F4v3 = f4fix.build_fixed_v3(guards_c, Czech CK, 'cz').
"""Phase 2K SOURCE-ONLY stack (Part 2, built from 2J's fixed TRANSLATION-ONLY stack).
The L3 request carries ONLY the source sentence, its language and the answer: no reference, no v / alt / lk / en,
no English sentence.  Kept deterministic SOURCE-side guards (all pre-L3, 0 calls), in this order:
  AG    runner_1u.AG_CFG primary (= stack_1w.decide: AG v4 + reader_nom v6) called with reference='' and extra=()
        -> the AGv5 refsubj/rs_nom reference read is removed; the annotation it sees is stripped (below).
  F4v2  2J-fixed (f4fix.build_fixed_v3 -> f4v2_subject_mismatch), input {sk, answer} only.
  F4v3  2J-fixed (f4fix.build_fixed_v3 -> f4v3_subject_mismatch), input {sk, answer} only (2J ran it after L3 on
        accepted rows; here pre-L3 -> only the layer label of an L3-rejected item can differ).
Every other answer goes to L3 (gemini-3.1-flash-lite, temperature 0, thinkingBudget 0): SAME = accept, TIP = reject
(TIP-as-rejection ON), DIFF = reject.  Removed (analysis/REMOVED_LAYERS.md): L1 exact-reference accept, F3, F5, L2 lock /
F1 / F2 / LOCKTIP, F2B, TIPdet, AGv5 refsubj, the reference lines of the P-FROZEN prompt.
Annotations are stripped of v/alt/en/lk/lk_*/headword/rewrite/reference/refs and wrapped in PoisonDict: a read attempt
of such a key raises PoisonHit (BaseException) and is recorded in HITS; inside AG it makes AG abstain on that item."""
import inspect, os, sys, traceback
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import write_guard  # noqa: E402,F401  every write outside phase2k/ is redirected
RUN_1W = os.path.join(TOFF, 'phase1w', 'a4', 'run')
LANG = {'sk': 'Slovak', 'cz': 'Czech'}
STRIP_KEYS = ('v', 'alt', 'en', 'lk', 'headword', 'rewrite', 'reference', 'refs', 'references')
VERDICTS = ('SAME', 'TIP', 'DIFF')
GCFG = {'temperature': 0, 'maxOutputTokens': 24, 'thinkingConfig': {'thinkingBudget': 0}}
RULING = ("Dropping a word is judged by its KIND. ACCEPTABLE to drop: time adverbs, degree adverbs and interjections "
          "— now, today, already, still, finally, then, totally, completely, just, Look! (Slovak: teraz, dnes, už, "
          "ešte, konečne, vtedy, úplne, práve, Pozri!; Czech: teď, dnes, už, ještě, "
          "konečně, tehdy, úplně, právě, Podívej!). WRONG to drop: nouns, adjectives, main "
          "verbs, and place or direction phrases — hot, in the room, off the plant. The owner's reason: where even the "
          "model does not treat it as a serious error, it is not counted as one.")
SYS_TMPL = (
    "You check a learner's English translation of a {L} sentence. There is no reference translation: judge the answer "
    "against the {L} sentence only. The one question: is the answer a correct English translation of this {L} sentence? "
    "Reply with exactly one word: SAME, TIP or DIFF. SAME = a correct English translation of the {L} sentence. "
    "TIP = the same meaning, but with a small slip. DIFF = not a correct translation of the {L} sentence. No explanation.\n"
    "Rules:\n"
    "- Any correct English with the same meaning is correct, whatever grammar structure it uses.\n"
    "- The time frame must match the {L} sentence; the English tense inside that time frame is free.\n"
    "- A passive is acceptable, but a passive that drops an agent the {L} sentence names is WRONG.\n"
    "- A missing obligatory English article is an ERROR, while the choice of article is free.\n"
    "- {RULING}\n"
    "- Added content is WRONG.\n"
    "WRONG or an ERROR = DIFF.")
HITS = []
ST = {}


def sys_text(lang):
    return SYS_TMPL.replace('{L}', LANG[lang]).replace('{RULING}', RULING)


def user_text(lang, src, answer):
    return '%s sentence: %s\nLearner answer: %s\nSAME, TIP or DIFF?' % (LANG[lang], src, answer)


def is_ref(k):
    return isinstance(k, str) and (k in STRIP_KEYS or k.startswith('lk_'))


class PoisonHit(BaseException):
    pass


def _hit(k):
    HITS.append({'key': str(k), 'where': ['%s:%d %s' % (os.path.relpath(f.filename, TOFF), f.lineno, f.name)
                                          for f in traceback.extract_stack()[-7:-2]]})
    raise PoisonHit(k)


class PoisonDict(dict):
    def _c(self, k):
        if is_ref(k):
            _hit(k)

    def __getitem__(self, k):
        self._c(k); return dict.__getitem__(self, k)

    def get(self, k, d=None):
        self._c(k); return dict.get(self, k, d)

    def __contains__(self, k):
        self._c(k); return dict.__contains__(self, k)

    def pop(self, k, *d):
        self._c(k); return dict.pop(self, k, *d)

    def setdefault(self, k, d=None):
        self._c(k); return dict.setdefault(self, k, d)


class PoisonVal(object):
    """A reference VALUE that raises on any use (attribute or operator)."""
    def __getattribute__(self, n):
        _hit('poison-value.' + n)


for _n in ('__str__', '__repr__', '__len__', '__iter__', '__eq__', '__ne__', '__hash__', '__bool__', '__getitem__',
           '__contains__', '__add__', '__radd__', '__lt__', '__gt__', '__le__', '__ge__', '__format__', '__fspath__',
           '__index__', '__int__', '__float__', '__mul__', '__mod__'):
    setattr(PoisonVal, _n, (lambda n: lambda self, *a, **k: _hit('poison-value.' + n))(_n))


def _say(*a, **k):
    sys.stderr.write(' '.join(str(x) for x in a) + '\n')


def _rd():
    return os.environ.get('P2I_RUN_DIR') or os.path.join(HERE, 'run')


def load(lang='sk'):
    if lang not in LANG:
        raise SystemExit('REFUSED: language %r (sk|cz)' % (lang,))
    if ST.get('lang'):
        if ST['lang'] != lang:
            raise SystemExit('REFUSED: one language per process')
        return ST
    if lang != 'cz':
        raise SystemExit('REFUSED: stack_source_cz is the Czech stack (lang cz only)')
    if RUN_1W not in sys.path:
        sys.path.insert(0, RUN_1W)
    import runner_1u as R1U                                                     # noqa: E402  (the 1W chain, read-only)
    for m in list(sys.modules.values()):
        f = os.path.abspath(getattr(m, '__file__', None) or '')
        if f.startswith(TOFF + os.sep) and not f.startswith(HERE + os.sep):
            if callable(getattr(m, 'say', None)):
                m.say = _say
            if isinstance(getattr(m, 'STOP_CHK', None), str):
                m.STOP_CHK = os.path.join(_rd(), 'STOP_CHK_source.txt')
    import f4fix
    import cz_assemble as CZA
    CZX = CZA.assemble()
    C = CZX['CK']                                  # the Czech checker_1i (em fix)
    G = [m for m in list(sys.modules.values())
         if (getattr(m, '__file__', '') or '').endswith(os.sep + 'guards_c.py') and hasattr(m, 'GUARDS')]
    if len(G) != 1:
        raise SystemExit('REFUSED: %d guards_c modules' % len(G))
    fx = f4fix.build_fixed_v3(G[0], C, lang)
    agc = R1U.AG_CFG
    name = 'primary' if 'primary' in agc else sorted(agc)[0]
    mod, flags = agc[name]
    ag_fn, ag_how = mod.decide, 'AG_CFG[%r].decide' % name
    if 'extra' not in inspect.signature(mod.decide).parameters:
        # runner_1u's PATCH object has no extra= parameter; it forwards to stack_1w.decide (CONTEXT 1.2 step 2), which
        # is called directly here so that extra=() removes the AGv5 refsubj/rs_nom reference read.
        s1w = sys.modules.get('stack_1w')
        if s1w is None or 'extra' not in inspect.signature(s1w.decide).parameters:
            raise SystemExit('REFUSED: no AG entry with extra= (refsubj cannot be removed)')
        ag_fn, ag_how = s1w.decide, 'stack_1w.decide called directly (AG_CFG[%r] = %s forwards to it)' % (name, type(mod).__name__)
    ST.update(lang=lang, R1U=R1U, C=C, G=G[0], f4v2=fx['f4v2_subject_mismatch'], f4v3=fx['f4v3_subject_mismatch'],
              ag_name=name, ag_fn=ag_fn, ag_how=ag_how, ag_flags=flags, ag_cfg_names=sorted(agc))
    ST.update(CZ=CZX, fx=fx, cz_rebound=len(CZA.REBOUND))
    return ST


def _strip(d):
    out = {k: v for k, v in dict.items(d) if not is_ref(k)}
    for sub in ('hygienised', 'raw'):
        if isinstance(out.get(sub), dict):
            out[sub] = PoisonDict({k: v for k, v in dict.items(out[sub]) if not is_ref(k)})
    return PoisonDict(out)


def ag_annotations(items):
    """The 1W annotation shape AG expects, via the verbatim 2F adapter, from SOURCE-side fields only."""
    import adapter_2f as A2F
    rows, seen = [], set()
    for it in items:
        sid = int(it['sid'])
        if sid in seen:
            continue
        seen.add(sid)
        a = {k: v for k, v in it['ann'].items() if not is_ref(k)}
        a.update(v=[''], alt=[], en='', lk=[])        # shape placeholders for the adapter; they carry no reference
        rows.append({'sid': sid, 'exercise_id': a.get('exercise_id'), 'level': it['level'],
                     'topic': a.get('type_title') or 'general', 'slovak': it['src'], 'ann': a})
    sents, ann = A2F.convert(rows, os.path.join(_rd(), '_adapter_source'))
    return {str(k): _strip(v) for k, v in ann.items()}, {str(s['sid']): s.get('slovak') for s in sents}


def guards(items, lang, reference=''):
    S_ = load(lang)
    ann, skmap = ag_annotations(items)
    out = {}
    for it in items:
        sid = str(int(it['sid']))
        sk = skmap.get(sid) or it['src']
        g = {'ag_fired': False, 'ag_reason': None, 'ag_ref_read': False, 'ag_error': None,
             'f4v2_fired': False, 'f4v3_fired': False, 'f4_error': None}
        try:
            d = S_['ag_fn'](sk, ann.get(sid) or PoisonDict(), {}, it['answer'], reference, 'primary',
                                    S_['ag_flags'], extra=())
            g['ag_fired'], g['ag_reason'] = bool(d.get('fired')), d.get('reason')
        except PoisonHit as e:
            g['ag_ref_read'], g['ag_reason'] = True, 'AG abstains: reference read removed (%s)' % e.args[0]
        except Exception as e:
            g['ag_error'], g['ag_reason'] = '%s: %s' % (type(e).__name__, e), 'AG ERROR (abstains)'
        f4in = PoisonDict({'sk': sk, 'answer': it['answer']})
        for nm in ('f4v2', 'f4v3'):
            try:
                hit, tr = S_[nm](f4in)
                g[nm + '_fired'] = bool(hit)
                if hit:
                    g[nm + '_why'] = '%s clash, answer %r' % (tr.get('clash'), tr.get('answer_subject'))
            except PoisonHit as e:
                g['f4_error'] = '%s reads %s' % (nm, e.args[0])
            except Exception as e:
                g['f4_error'] = '%s %s: %s' % (nm, type(e).__name__, e)
        g['guard_layer'] = ('AG' if g['ag_fired'] else 'F4v2' if g['f4v2_fired'] else
                            'F4v3' if g['f4v3_fired'] else None)
        out[it['jid']] = g
    return out


def prepare(items, lang):
    g = guards(items, lang)
    return {it['jid']: {'sys': sys_text(lang), 'user': user_text(lang, it['src'], it['answer']), 'gcfg': dict(GCFG)}
            for it in items if g[it['jid']]['guard_layer'] is None}


def finish(items, lang, replies, failed):
    g, failed, out = guards(items, lang), set(failed), {}
    for it in items:
        j = it['jid']
        r = dict(g[j])
        if r['guard_layer']:
            r.update(accept=False, layer=r['guard_layer'], reached_l3=False, l3_reply=None, call_failed=False)
        elif j in failed:
            r.update(accept=False, layer='L3:failed', reached_l3=True, l3_reply=None, call_failed=True)
        elif replies.get(j) in VERDICTS:
            v = replies[j]
            r.update(accept=(v == 'SAME'), layer='L3:TIPrej' if v == 'TIP' else 'L3', reached_l3=True, l3_reply=v,
                     call_failed=False)
        else:
            continue
        out[j] = r
    return out
