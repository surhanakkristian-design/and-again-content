#!/usr/bin/env python3
"""Phase 1h 2.3 — REFERENCE HYGIENE. Deterministic, zero model tokens, import-safe.

(a) Where the English reference adds content the Slovak does not have, the added span is marked OPTIONAL
    (written into the annotation's `d` field, which the checker already reads) so that F3 and F5 stop
    punishing a faithful answer. Two existing, already-annotated sources are used - no new judgement:
      a1  the annotation's own `p` entries of the form "-span"  (e.g. C:9244 `p:["-in"]`,
          C:5595 `p:["-at last"]`) - the Phase 1c annotators already marked the span as droppable;
      a2  a synonym/alt group of the annotation in which one member is a strict token-subsequence of the
          annotated span and the extra tokens are particles/directionals or adverbs
          (e.g. C:9992 span "swelled up", group member "swelled" -> "up" optional).
(b) Where the Slovak verb morphology leaves person or gender OPEN but the English reference fixes a
    nominative pronoun, the `g` gender chain is added automatically. "Open" is decided by F4v2's Slovak
    morphology reader (checker_1h.sk_features), never by the reference. The chain is then used by
    gender_variants() to expand the accepted variants, so the reference's arbitrary he/she no longer
    counts as content.

Output goes to phase1h/ only; phase1c/ is never written.

    python3 phase1h/reference_hygiene.py <annotations dir or file> [outdir]
"""
import os, sys, json, re, glob, copy

HERE = os.path.dirname(os.path.abspath(__file__))
MASC = {'he': 'she', 'him': 'her', 'his': 'her', 'himself': 'herself'}
FEM = {'she': 'he', 'her': 'him', 'hers': 'his', 'herself': 'himself'}
NOMINATIVE = ('he', 'she')


def _toks(s):
    return re.findall(r"[a-z']+", (s or '').lower())


def _droppable_tokens():
    """Particles / directionals / adjunct adverbs, taken from the checker's existing tables."""
    import checker_1h as chk
    return set(chk.PARTICLES) | set(chk.ADVERBS) | {'at', 'last', 'in', 'up', 'out', 'down', 'back'}


def half_a(ann):
    """-> {token: token} additions for `d`, plus a trace."""
    add, trace = {}, []
    drop = _droppable_tokens()
    for e in (ann.get('p') or []):
        s = str(e)
        if s.startswith('-'):
            span = s[1:].split('@')[0]
            for t in _toks(span):
                add[t] = t
            trace.append({'source': 'p', 'entry': s, 'optional': _toks(span)})
    groups = []
    for k, vs in (ann.get('alt') or {}).items():
        groups.append((k, list(vs)))
    for k, vs in groups:
        kt = _toks(k)
        for v in vs:
            vt = _toks(v)
            if not vt or vt == kt:
                continue
            i, extra = 0, []
            for t in kt:
                if i < len(vt) and vt[i] == t:
                    i += 1
                else:
                    extra.append(t)
            if i == len(vt) and extra and all(x in drop for x in extra):
                for t in extra:
                    add[t] = t
                trace.append({'source': 'alt', 'span': k, 'member': v, 'optional': extra})
    return add, trace


def morphology_open(sk):
    """F4v2's reader: -> (features, open_gender, open_person)."""
    import checker_1h as chk
    feats, sig = chk.sk_features(sk or '')
    return feats, feats.get('gender') not in ('m', 'f'), feats.get('person') is None



def _gender_signal(sk):
    """True when the Slovak carries a word that can carry gender (l-participle shape or a gendered
    pronoun), using F4v2's own tables. Then the gender is NOT safely open."""
    import checker_1h as chk
    for x in chk._sk_words(sk or ''):
        if x in chk.SK_PRON and chk.SK_PRON[x][2] in ('m', 'f'):
            return True
        if len(x) < 4 or x in chk.SK_NOT_VERB:
            continue
        m = chk.SK_L_PART.match(x)
        if m and m.group(1) and m.group(1)[-1:] in chk.VOW:
            return True
    return False


def half_b(ann, sk):
    """-> (g chains to add, trace). Only when the Slovak leaves gender/person open and a reference fixes a
    nominative pronoun."""
    if not sk or ann.get('g'):
        return None, None
    feats, open_g, open_p = morphology_open(sk)
    if not (open_g or open_p):
        return None, None
    if _gender_signal(sk):        # the reader ABSTAINS on an l-participle without a past marker; a
        return None, None         # gender-shaped word means the Slovak may well fix the gender
    refs = [v for v in (ann.get('v') or []) if isinstance(v, str)]
    chains = []
    for pron in NOMINATIVE:
        occ = []
        for r in refs[:1]:
            for m in re.finditer(r'\b(%s)\b' % pron, r, re.I):
                occ.append(m.group(1))
        if occ:
            chain = [occ[0]] + ['%s#%d' % (occ[0], i + 1) for i in range(1, len(occ))]
            chains.append(chain)
    if not chains:
        return None, None
    return chains, {'features': feats, 'open_gender': open_g, 'open_person': open_p, 'chains': chains}


def hygienise(ann, sk=None):
    """-> (new annotation, trace). Never mutates the input."""
    a = copy.deepcopy(ann or {})
    tr = {'a': None, 'b': None}
    add, ta = half_a(a)
    if add:
        d = dict(a.get('d') or {})
        for k, v in add.items():
            d.setdefault(k, v)
        a['d'] = d
        tr['a'] = ta
    chains, tb = half_b(a, sk)
    if chains:
        a['g'] = chains
        a['g_auto'] = True
        tr['b'] = tb
    return a, tr


def gender_variants(refs, g):
    """Expand accepted variants over the `g` gender chain (he <-> she consistently in the whole variant)."""
    if not g:
        return list(refs)
    chained = {str(x).split('#')[0].lower() for ch in g for x in ch}
    if not (chained & set(NOMINATIVE)):
        return list(refs)
    out = list(refs)
    for r in list(refs):
        def sw(m):
            w = m.group(0)
            low = w.lower()
            rep = MASC.get(low) or FEM.get(low)
            if not rep:
                return w
            return rep.capitalize() if w[0].isupper() else rep
        v = re.sub(r"\b(he|she|him|her|his|hers|himself|herself)\b", sw, r, flags=re.I)
        if v != r and v not in out:
            out.append(v)
    return out


def run(path, outdir, sk_map=None):
    """Apply hygiene to every annotation in `path` (dir or single file); write to outdir + a report."""
    files = sorted(glob.glob(os.path.join(path, '*.json'))) if os.path.isdir(path) else [path]
    os.makedirs(os.path.join(outdir, 'annotated'), exist_ok=True)
    sk_map = sk_map or {}
    rep = {'source': path, 'n_files': len(files), 'touched_a': 0, 'touched_b': 0,
           'ids_a': [], 'ids_b': [], 'examples_a': [], 'examples_b': []}
    for f in files:
        ann = json.load(open(f))
        eid = ann.get('id')
        sk = sk_map.get(eid) or sk_map.get(str(eid))
        new, tr = hygienise(ann, sk)
        json.dump(new, open(os.path.join(outdir, 'annotated', os.path.basename(f)), 'w'),
                  ensure_ascii=False)
        if tr['a']:
            rep['touched_a'] += 1
            rep['ids_a'].append(eid)
            if len(rep['examples_a']) < 10:
                rep['examples_a'].append({'id': eid, 'before_d': ann.get('d'), 'after_d': new.get('d'),
                                          'trace': tr['a'], 'reference': (ann.get('v') or [None])[0]})
        if tr['b']:
            rep['touched_b'] += 1
            rep['ids_b'].append(eid)
            if len(rep['examples_b']) < 10:
                rep['examples_b'].append({'id': eid, 'before_g': ann.get('g'), 'after_g': new.get('g'),
                                          'sk': sk, 'trace': tr['b'],
                                          'reference': (ann.get('v') or [None])[0]})
    name = 'hygiene_report_old.json' if 'annotated_after' in path else 'hygiene_report_new.json'
    json.dump(rep, open(os.path.join(HERE, name), 'w'), ensure_ascii=False, indent=1)
    return rep


if __name__ == '__main__':
    sys.path.insert(0, HERE)
    import checker_1h as chk
    chk.load_items_1h()
    p = sys.argv[1] if len(sys.argv) > 1 else os.path.join(chk.base.P1C, 'annotated_after')
    o = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'hygiene')
    r = run(p, o, chk.SK_OF)
    print(json.dumps({k: v for k, v in r.items() if not k.startswith('examples')}, indent=1)[:1200])
