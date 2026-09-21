#!/usr/bin/env python3
"""Phase 2I - TRANSLATION-ONLY stack = the frozen 1W stack (stack_frozen.py engine, runner_1u in place) with the
three copied modules in phase2i/tonly/ (lib_prev, pipeline_1i, runner_1p; changes in TONLY_CHANGES.md) loaded
under their original names BEFORE the chain is imported, and lk / lk_* stripped from every annotation before
the stack sees it.  CLI identical to stack_frozen.py.
TONLY_POISON=1 (tests only): annotations, records and checker items become PoisonDicts that raise PoisonHit (a
BaseException, so no `except Exception` can swallow it) on any read of lk / locks / lock_ok / lock_released_2_1."""
import importlib.util, os, sys, traceback
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
TONLY = os.path.join(HERE, 'tonly')
sys.path.insert(0, HERE)
import write_guard  # noqa: E402,F401  stage 2b: before any 1W module
COPIED = ('lib_prev', 'pipeline_1i', 'runner_1p')          # load order
BAD = ('lk', 'locks', 'lock_ok', 'lock_released_2_1')
HITS = []


def _is_lk(k):
    return k == 'lk' or (isinstance(k, str) and k.startswith('lk_'))


def _preload():
    for name in COPIED:
        m = sys.modules.get(name)
        if m is not None:
            if os.path.dirname(os.path.abspath(m.__file__)) != TONLY:
                raise SystemExit('REFUSED: the ORIGINAL %s is already imported' % name)
            continue
        spec = importlib.util.spec_from_file_location(name, os.path.join(TONLY, name + '.py'))
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
        if name == 'lib_prev':
            # checker_1i.py:32 asserts lib_prev lives in phase1i/ (reads base.__file__). Pin __file__ to the
            # original path; __spec__.origin keeps the true (copy) path, which the import graph reports.
            mod.__file__ = os.path.join(TOFF, 'phase1i', 'lib_prev.py')


_preload()
sys.path.insert(0, HERE)
import stack_frozen as E                                                       # noqa: E402
E.STATE['stack'] = 'tonly'


class PoisonHit(BaseException):
    pass


def _hit(k):
    HITS.append({'key': str(k), 'where': [('%s:%d %s' % (os.path.relpath(f.filename, TOFF), f.lineno, f.name))
                                          for f in traceback.extract_stack()[-6:-2]]})
    raise PoisonHit(k)


class PoisonVal(object):
    def __getattribute__(self, n):
        _hit('lk-value.' + n)


class PoisonDict(dict):
    def _c(self, k):
        if k in BAD or _is_lk(k):
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


POISON = bool(os.environ.get('TONLY_POISON'))


def strip_lk(ann):
    out = {}
    for sid, a in ann.items():
        b = {k: v for k, v in a.items() if not _is_lk(k)}
        for sub in ('hygienised', 'raw'):
            if isinstance(b.get(sub), dict):
                b[sub] = {k: v for k, v in b[sub].items() if not _is_lk(k)}
                if POISON:
                    b[sub] = PoisonDict(b[sub])
        out[sid] = PoisonDict(b) if POISON else b
    return out


def _poison_recs(st, recs, by):
    keep = {}
    for lst in (recs, st.get('recs')):
        if isinstance(lst, list):
            for k, r in enumerate(lst):
                if id(r) not in keep:
                    keep[id(r)] = (r, PoisonDict(r))
                lst[k] = keep[id(r)][1]
    for k in list(by):
        if id(by[k]) in keep:
            by[k] = keep[id(by[k])][1]
    st['_poison_keep'] = keep


def strip_row(a):
    """stage 2b: lk / lk_* removed from the production row BEFORE the 2F adapter reads it (the verbatim adapter
    does d.get('lk'); on this stack that key is absent, so hygienised/raw get lk = [] which strip_lk then drops)."""
    return {k: v for k, v in a.items() if not _is_lk(k)}


E.STATE['row_hook'] = strip_row
E.STATE['ann_hook'] = strip_lk
if POISON:
    E.STATE['post_build'] = _poison_recs
    _P = sys.modules['pipeline_1i']
    _orig_to_item = _P.to_item
    _P.to_item = lambda r: PoisonDict(_orig_to_item(r))

if __name__ == '__main__':
    E.cli(sys.argv)
