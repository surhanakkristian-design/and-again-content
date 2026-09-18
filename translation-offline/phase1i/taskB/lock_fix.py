"""Task B — L2 lock fix, delivered as a monkeypatch module (phase1i/checker_1i.py is NOT edited).

Import is side-effect free (stdlib only, no file read, no call). Use:

    import lock_fix
    report = lock_fix.apply(checker_module, syn=True, gender=True, contraction=True)

`apply` wraps, on the module object it is handed:
  * f1_lock_ok        -> also satisfied by an equivalent rendering of the locked span
  * lock_equivalent_ok-> same candidate set for the §2.1 load-time release
  * _has              -> contraction-safe (only when contraction=True)
It returns a dict describing what was patched. Call `revert(checker_module)` to undo.

Three independent parts:
  syn          the locked span may be satisfied by a member of an EXISTING synonym group (phase1c/synonyms/*,
               reached by phrase, by the annotation's `s` group id — see backfill_s_ids.py — or by the
               annotation's `alt`).  HARD GUARD: the equivalent must have the IDENTICAL grammatical
               signature as the locked span (same parse_lock kind, same aux chain, same verb form,
               same needs_to).  A tense/aspect/voice change can therefore never release the lock, so the
               grammatical test is not loosened.
  gender       the locked span is expanded over the annotation's own `g` gender chain with exactly the
               function reference_hygiene already uses for the accepted references (gender_variants).
               Fixes the pipeline asymmetry: hygiene expands `v` but not `lk`.
  contraction  `_has` (used by f2_equivalent) matched literal token strings, so expand()'s ambiguity
               tokens ("he's" -> "is|has") hid equivalences the code already grants (will -> going to).
"""
import os
import json

_ORIG = {}
_IDX = {}


def _norm(C, s):
    return C.base.norm(s or '').strip()


def _index(C):
    """gid -> [members]  from the existing tables only. Cached per module."""
    key = id(C)
    if key not in _IDX:
        idx = {}
        for fn in getattr(C, 'SYN_FILES', ('table.json', 'ng_phase1c.json', 'review_added.json')):
            p = os.path.join(C.base.P1C, 'synonyms', fn)
            if os.path.exists(p):
                for g in (json.load(open(p)).get('groups') or []):
                    m = [_norm(C, x) for x in (g.get('m') or [])]
                    m = [x for x in m if x]
                    if len(m) > 1 and g.get('id'):
                        idx[str(g['id'])] = m
        _IDX[key] = idx
    return _IDX[key]


def _alt_map(C, a):
    return {_norm(C, k): [_norm(C, x) for x in (v or [])] for k, v in (a.get('alt') or {}).items()}


def lock_equivalents(C, a, lk):
    """Every rendering of the locked span this annotation / the existing tables already accept."""
    lkn = _norm(C, lk)
    out = set(C.syn_equivalents(lkn))
    idx = _index(C)
    for k, gid in (a.get('s') or {}).items():
        mem = idx.get(str(gid))
        if not mem:
            continue
        if _norm(C, k) == lkn or lkn in mem:
            out |= set(mem)
    alt = _alt_map(C, a)
    out |= set(alt.get(lkn) or [])
    for k, vs in alt.items():
        if lkn in vs:
            out |= set(vs) | {k}
    out.discard(lkn)
    return {x for x in out if x}


def _sig(C, span):
    """The grammatical signature of a span: identical signature = same grammar, different words."""
    p = C.parse_lock(span)
    k = p.get('kind')
    if k == 'pattern':
        return ('pattern', tuple(p.get('chain') or []), p.get('form'), bool(p.get('needs_to')))
    if k in ('bare_aux', 'exact_aux_main'):
        return (k, p.get('literal'))
    if k == 'det_noun':
        return ('det_noun',)
    if k == 'quant':
        return ('quant',)
    return ('literal',)


def _present(C, span, answer):
    j = ' ' + ' '.join(C.toks(answer)) + ' '
    return (' ' + _norm(C, span) + ' ') in j


def _gender_lock_variants(C, lk, g):
    if not g:
        return []
    try:
        out = C.hyg.gender_variants([lk], g)
    except Exception:
        return []
    return [x for x in out if _norm(C, x) != _norm(C, lk)]


def _extended_release(C, it, syn, gender):
    """-> trace dict or None. Never calls the model, never reads anything outside the existing tables."""
    a = C.annot(it['exercise_id'])
    for lk in (it.get('locks') or []):
        base_sig = _sig(C, lk)
        if syn:
            for c in sorted(lock_equivalents(C, a, lk)):
                if _sig(C, c) != base_sig:
                    continue                      # different grammar -> refused (keeps the T test intact)
                if base_sig[0] == 'literal':
                    # non-verb spans only, exactly the §2.1 rule, now with the s/alt candidate set
                    if not (C._lock_is_non_verb(lk) and C._lock_is_non_verb(c)):
                        continue
                    if _present(C, c, it['answer']):
                        return {'part': 'syn', 'lock': lk, 'equivalent': c}
                elif C.pattern_match(C.parse_lock(c), it['answer']):
                    return {'part': 'syn', 'lock': lk, 'equivalent': c}
        if gender:
            for v in _gender_lock_variants(C, lk, a.get('g')):
                if _sig(C, v) != base_sig:
                    continue
                if base_sig[0] == 'literal':
                    if _present(C, v, it['answer']):
                        return {'part': 'gender', 'lock': lk, 'equivalent': v}
                elif C.pattern_match(C.parse_lock(v), it['answer']):
                    return {'part': 'gender', 'lock': lk, 'equivalent': v}
    return None


def _has_fixed(C):
    def _has(answer, phrases):
        at = [t.split('|') for t in C.expand(C.toks(answer))]
        for p in phrases:
            pt = p.split()
            n = len(pt)
            for i in range(len(at) - n + 1):
                if all(pt[j] in at[i + j] for j in range(n)):
                    return p
        return None
    return _has


def apply(C, syn=True, gender=True, contraction=True):
    """Patch the checker module in place. Idempotent-safe: reverts first, then re-patches."""
    revert(C)
    _ORIG[id(C)] = {'f1_lock_ok': C.f1_lock_ok, 'lock_equivalent_ok': C.lock_equivalent_ok,
                    '_has': C._has}
    of1, olk = C.f1_lock_ok, C.lock_equivalent_ok
    RELEASES = {}

    def f1_lock_ok(it):
        if of1(it):
            return True
        if not (syn or gender):
            return False
        tr = _extended_release(C, it, syn, gender)
        if tr:
            RELEASES[it['item_id']] = tr
            return True
        return False

    def lock_equivalent_ok(it):
        ok, tr = olk(it)
        if ok:
            return ok, tr
        if not (syn or gender):
            return False, None
        tr = _extended_release(C, it, syn, gender)
        if tr:
            return True, {'lock': tr['lock'], 'equivalent': tr['equivalent'], 'part': tr['part']}
        return False, None

    C.f1_lock_ok = f1_lock_ok
    C.lock_equivalent_ok = lock_equivalent_ok
    if contraction:
        C._has = _has_fixed(C)
    return {'syn': syn, 'gender': gender, 'contraction': contraction, 'releases': RELEASES}


def revert(C):
    o = _ORIG.pop(id(C), None)
    if o:
        for k, v in o.items():
            setattr(C, k, v)
