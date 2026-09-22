#!/usr/bin/env python3
"""Phase 2L Part D - assemble the CZECH source reader into the loaded (read-only) 1W AG chain. 0 model calls.
1. phase1v/trackC/cz_reader.build(ALL_FIXES) -> new module objects (cz_f9 / cz_ck / cz_v2 / cz_v3) carrying 1V Track C's
   four fixes: em (no 1sg in -em/-iem), se (SK_REFLEX + se), jestli (L_NONVERB + SUB_MARK), aspect (Czech perfective
   lexicon, dokaze out of MOD).  Each fix is verified present (VERIFY; assemble() raises otherwise).
2. Rebind: in every loaded chain module (file under translation-offline/, not phase2l/, not the four Slovak reader
   modules themselves) and in the four Czech modules, every global / default argument / closure cell that IS a Slovak
   reader module (f9, checker_1i, agent_drop_v2, agent_drop_v3) or IS an object defined by one is replaced by the Czech
   counterpart of the same name.  The Slovak module objects and every file stay untouched (process-local binding).
3. residual() lists every Slovak reader object still reachable that way (must be empty).
expected_stack_source_cz() is the ONLY difference between stack_source.py and stack_source_cz.py (tested)."""
import os, re, sys, types
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
CZR_DIR = os.path.join(TOFF, 'phase1v', 'trackC')
KEYS = (('f9', 'f9'), ('CK', 'checker_1i'), ('V2', 'agent_drop_v2'), ('V3', 'agent_drop_v3'))
FIXES = ('em', 'se', 'jestli', 'aspect')
_DONE, REBOUND, VERIFY, _VM, _SL = {}, [], {}, {}, {}
_SKIP = (int, float, str, bool, bytes, type(None), complex)


def _chain():
    out = []
    for m in list(sys.modules.values()):
        f = os.path.abspath(getattr(m, '__file__', None) or '') if isinstance(m, types.ModuleType) else ''
        if f.startswith(TOFF + os.sep) and not f.startswith(HERE + os.sep) and all(m is not s for s in _SL.values()):
            out.append(m)
    return out


def _own_fns(m):
    for v in list(vars(m).values()):
        fs = [v] if isinstance(v, types.FunctionType) else (
            [f for f in vars(v).values() if isinstance(f, types.FunctionType)] if isinstance(v, type) else [])
        for f in fs:
            if getattr(f, '__module__', None) == m.__name__:
                yield f


def _hit(x):
    e = _VM.get(id(x))
    return e if e is not None and e[0] is x else None


def _walk(apply):
    for m in _chain():
        d = vars(m)
        for n, v in list(d.items()):
            e = _hit(v)
            if e:
                apply(('global', m.__name__, n, e), lambda e=e, n=n, d=d: d.__setitem__(n, e[1]))
        for f in _own_fns(m):
            if f.__defaults__ and any(_hit(x) for x in f.__defaults__):
                apply(('default', m.__name__, f.__name__, None),
                      lambda f=f: setattr(f, '__defaults__', tuple((_hit(x) or (0, x))[1] for x in f.__defaults__)))
            for c in f.__closure__ or ():
                try:
                    x = c.cell_contents
                except ValueError:
                    continue
                e = _hit(x)
                if e:
                    apply(('closure', m.__name__, f.__name__, e), lambda c=c, e=e: setattr(c, 'cell_contents', e[1]))


def residual():
    out = []
    _walk(lambda info, fix: out.append('%s %s.%s' % (info[0], info[1], info[2])))
    return out


def _verify(X, CZR):
    assert tuple(CZR.ALL_FIXES) == FIXES, CZR.ALL_FIXES
    srcs = X['CK'].sk_features('Ředitelem školy je pan Novák.')[1] + X['CK'].sk_features('Hercem roku se stal Petr.')[1]
    VERIFY['em'] = not any(re.search(r'-m \S*em\b', s) for s in srcs)
    VERIFY['se'] = bool(X['V2'].SK_REFLEX.search('Dveře se otevřely.')) and X['V3'].V2 is X['V2']
    VERIFY['jestli'] = CZR.CZ_LI <= X['f9'].L_NONVERB and CZR.CZ_LI <= X['f9'].SUB_MARK
    VERIFY['aspect'] = CZR.CZ_PERF <= X['f9'].PERF_LEX and not (CZR.CZ_PERF & X['f9'].MOD)
    bad = [k for k in FIXES if not VERIFY.get(k)]
    if bad:
        raise AssertionError('Czech reader fix(es) not present: %s' % bad)


def assemble():
    if 'X' in _DONE:
        return _DONE['X']
    if CZR_DIR not in sys.path:
        sys.path.insert(0, CZR_DIR)
    import cz_reader as CZR
    _SL.update({k: sys.modules.get(n) for k, n in KEYS})
    X = CZR.build(CZR.ALL_FIXES)
    _verify(X, CZR)
    for k, _ in KEYS:
        s = _SL[k]
        if s is not None:
            _VM[id(s)] = (s, X[k], k, '<module>')
    for k, _ in KEYS:
        s, c = _SL[k], X[k]
        if s is None:
            continue
        for n, v in list(vars(s).items()):
            if n.startswith('__') or isinstance(v, _SKIP) or id(v) in _VM:
                continue
            if hasattr(c, n) and getattr(c, n) is not v:
                _VM[id(v)] = (v, getattr(c, n), k, n)

    def apply(info, fix):
        fix(); REBOUND.append(info[:3] + ((info[3][2], info[3][3]) if info[3] else None,))
    _walk(apply)
    for m in _chain():                      # guards_c resolves its checker lazily (_C, set on first use): pin the Czech CK
        if (getattr(m, '__file__', '') or '').endswith(os.sep + 'guards_c.py') and '_C' in vars(m):
            if m._C is None or m._C is _SL['CK']:
                m._C = X['CK']; REBOUND.append(('global', m.__name__, '_C', ('CK', 'lazy')))
    _DONE['X'] = X
    return X


SUBS = (
    ("#!/usr/bin/env python3\n",
     "#!/usr/bin/env python3\n# Phase 2L Part D: byte copy of stack_source.py (= phase2k/stack_source.py) except load(): lang cz only, the\n"
     "# Czech reader assembled into the AG chain by cz_assemble.assemble(), F4v2/F4v3 = f4fix.build_fixed_v3(guards_c, Czech CK, 'cz').\n"),
    ("    if lang == 'cz':\n        raise SystemExit('REFUSED: the Czech guards (cz_reader + f4fix cz) are assembled in stage S3')\n",
     "    if lang != 'cz':\n        raise SystemExit('REFUSED: stack_source_cz is the Czech stack (lang cz only)')\n"),
    ("    import f4fix\n    C = sys.modules['checker_1i']\n",
     "    import f4fix\n    import cz_assemble as CZA\n    CZX = CZA.assemble()\n    C = CZX['CK']                                  # the Czech checker_1i (em fix)\n"),
    ("    return ST\n\n\ndef _strip",
     "    ST.update(CZ=CZX, fx=fx, cz_rebound=len(CZA.REBOUND))\n    return ST\n\n\ndef _strip"),
)


def expected_stack_source_cz(text):
    for old, new in SUBS:
        if text.count(old) != 1:
            raise AssertionError('stack_source substitution site count %d: %r' % (text.count(old), old))
        text = text.replace(old, new)
    return text
