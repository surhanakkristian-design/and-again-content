#!/usr/bin/env python3
"""Phase 2J A2 - deterministic fix of the F4v2 subject-guard misfire (checker_1i.sk_features, the reader F4v2 uses).
Cause (A1): the present-tense ENDING heuristics of sk_features (checker_1i.py:552-563: -š -> 2sg, -me -> 1pl,
-te -> 2pl, -m -> 1sg) read NON-VERBS as finite verbs:
  (a) a locative noun that heads a prepositional phrase whose preposition is NOT the immediately preceding word
      ('po vidieckej CESTE', 'v celom jeho ŽIVOTE', 'pri tomto PLOTE' -> 2pl). The only guard, after_prep
      (checker_1i.py:542/544), looks one token back, so a modifier between preposition and noun defeats it;
  (b) adverbs ending like a verb ('PRÍLIŠ' -> 2sg, 'SAMOZREJME' -> 1pl), not in SK_NOT_VERB (checker_1i.py:526).
The false feature then contradicts every correct 3rd-person answer and F4v2 (checker_1i.py:608, decide 815-820)
rejects it. Not reported speech, not the wrong clause: the misread words are nouns and adverbs.
Fix = two source patches of sk_features, used ONLY by F4v2 (reader_nom's CK.sk_features is left unchanged):
  PP  a preposition followed by 1-3 modifiers (closed determiner/possessive list or adjective ending) shadows the
      modifiers AND the head noun after them exactly like after_prep already shadows the first word;
  NV  a closed list of non-verbs ending in -š/-me/-te/-em (adverbs, the preposition 'okrem', first names in -š).
No threshold, no abstain rule: every other signal is read as before."""
import os, re, sys, types
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
CK_FILE = os.path.join(TOFF, 'phase1i', 'checker_1i.py')
NP_DET = set('''tento táto toto tomto tejto tom tej tomu toho tých tými tieto tí jeho jej ich môj moja moje mojom
mojej mojich tvoj tvojom tvojej náš našom našej našich váš vašom vašej svoj svojom svojej svojich celom celej
celého celému každom každej inom inej jednom jednej tomhle tém mém mojí tvém tvojí našem naší vašem vaší svém
svojí celém každém jiném jedné'''.split())
ADJ_END = ('ej', 'ých', 'ého', 'ému', 'ým', 'ovom', 'skom', 'ckom', 'nom', 'ém')
NON_VERB = {'príliš', 'příliš', 'samozrejme', 'proste', 'okrem', 'tomáš', 'lukáš', 'matúš', 'matyáš', 'mikuláš',
            'miloš', 'aleš', 'tobiáš'}
PREP_CZ = {'při', 'přes', 'ke', 've', 'se', 'ze', 'podle', 'kolem', 'mezi', 'bez', 'za', 'před', 'pod', 'nad',
           'od', 'do', 'na', 'po', 'o', 'u', 'v', 's', 'z', 'k', 'proti', 'vůči', 'kvůli', 'během', 'okolo'}
PATCH_EM_OLD = "if (x.endswith(('ím', 'ám', 'iem', 'em')) and len(x) >= 4"
PATCH_EM_NEW = "if (x.endswith(('ím', 'ám')) and len(x) >= 4"


def is_mod(x):
    return x in NP_DET or (len(x) >= 4 and x.endswith(ADJ_END))


# S2 narrowing (verb-loss cost of S1): the PP head is NOT shadowed when it looks like a finite verb - an
# l-participle (-l/-la/-lo/-li/-ly), a 2sg present (-s-caron) or a form of byt/mat.  Such a head returns to the 2I reading,
# so the narrowing can only move the fixed reader back towards 2I, never create a new signal.
VERB_HEAD_END = ('l', 'la', 'lo', 'li', 'ly', 'š')
BE_HAVE = set('''je sú som si sme ste bol bola bolo boli boly bude budú budem budeš budeme budete jsem jsi jsme jste
jsou byl byla bylo byli byly má mám máš máme máte majú mají'''.split())


def is_verb_head(x):
    return x not in NON_VERB and (x in BE_HAVE or x.endswith(VERB_HEAD_END))


def pp_shadow(w, preps):
    sh = set()
    for i, x in enumerate(w):
        if x in preps:
            j, k = i + 1, 0
            while j < len(w) and k < 3 and is_mod(w[j]):
                sh.add(j); j += 1; k += 1
            if k and j < len(w) and not is_verb_head(w[j]):
                sh.add(j)
    return sh


def _func_src(text, name):
    m = re.search(r'^def %s\(.*?(?=^\S)' % name, text, re.S | re.M)
    return m.group(0)


def _sub(src, old, new, n):
    if src.count(old) != n:
        raise AssertionError('patch site count %d != %d: %r' % (src.count(old), n, old))
    return src.replace(old, new)


def build_fixed(C, lang='sk'):
    """-> {'sk_features', 'f4v2_subject_mismatch'} bound to module C's globals, with PP + NV applied."""
    text = open(CK_FILE, encoding='utf-8').read()
    sf = _func_src(text, 'sk_features')
    if lang == 'cz':
        sf = _sub(sf, PATCH_EM_OLD, PATCH_EM_NEW, 1)          # cz_reader's 'em' patch, same site
    sf = _sub(sf, "    w = _sk_words(sk)\n", "    w = _sk_words(sk)\n    _SH = _pp_shadow(w)\n", 1)
    sf = _sub(sf, "    for x in w:\n        after_prep = prev in SK_PREP\n",
              "    for _i, x in enumerate(w):\n        after_prep = prev in SK_PREP or _i in _SH\n", 2)
    sf = _sub(sf, "x in SK_NOT_VERB", "x in _NOT_VERB", 2)
    ns = dict(C.__dict__)
    preps = set(C.SK_PREP) | (PREP_CZ if lang == 'cz' else set())
    ns['_pp_shadow'] = lambda w: pp_shadow(w, preps)
    ns['_NOT_VERB'] = set(C.SK_NOT_VERB) | NON_VERB
    exec(compile(sf, CK_FILE + ':sk_features[2J]', 'exec'), ns)
    exec(compile(_func_src(text, 'f4v2_subject_mismatch'), CK_FILE + ':f4v2[2J]', 'exec'), ns)
    return {'sk_features': ns['sk_features'], 'f4v2_subject_mismatch': ns['f4v2_subject_mismatch']}


def apply(C):
    fx = build_fixed(C)
    C.f4v2_subject_mismatch = fx['f4v2_subject_mismatch']      # decide() looks it up in C's globals
    C._F4FIX_FN = fx['f4v2_subject_mismatch']
    C.F4FIX_2J = True
    return fx


def apply_loaded():
    import sys
    done, already = [], []
    for m in list(sys.modules.values()):
        f = os.path.abspath(getattr(m, '__file__', '') or '')
        if f.endswith(os.sep + 'checker_1i.py') and hasattr(m, 'decide'):
            if getattr(m, 'F4FIX_2J', False):
                already.append(f)                            # idempotent: load() runs again in finish
            else:
                apply(m); done.append(f)
    if not done and not already:
        raise SystemExit('REFUSED: F4FIX found no checker_1i module to patch')
    return done


# ---------------------------------------------------------------- S2: the hook defect
# S1 set C.f4v2_subject_mismatch on the checker_1i module, but the decide the stack actually runs is the guards_c
# wrapper (pipeline_1i.configure -> guards_c.apply) whose globals are NOT checker_1i.__dict__ (S2 probe: st['decide']
# globals != C.__dict__, 0 calls reached the patched name).  sweep() therefore replaces the ORIGINAL
# f4v2_subject_mismatch in EVERY live namespace dict and closure cell of the process (gc walk), so whichever copy
# decide resolves is the fixed one.  Called after load, after build (post_build) and before every run_pipeline.
SWEEPS = []


def _is_old(v, FN):
    return (isinstance(v, types.FunctionType) and v is not FN and v.__name__ == 'f4v2_subject_mismatch'
            and not v.__code__.co_filename.endswith('[2J]'))


def sweep(where=''):
    import gc
    C = sys.modules.get('checker_1i')
    FN = getattr(C, '_F4FIX_FN', None)
    if FN is None:
        raise SystemExit('REFUSED: F4FIX sweep before apply')
    nd = nc = 0
    for o in gc.get_objects():
        if type(o) is types.FunctionType:
            for c in (o.__closure__ or ()):
                try:
                    v = c.cell_contents
                except ValueError:
                    continue
                if _is_old(v, FN):
                    c.cell_contents = FN; nc += 1
        elif isinstance(o, dict):
            try:
                v = dict.get(o, 'f4v2_subject_mismatch')
            except Exception:
                continue
            if _is_old(v, FN):
                dict.__setitem__(o, 'f4v2_subject_mismatch', FN); nd += 1
    SWEEPS.append({'where': where, 'dicts': nd, 'cells': nc})
    sys.stderr.write('F4FIX sweep %s: %d dicts, %d cells\n' % (where, nd, nc))
    return nd + nc


def install_sweeps(PP):
    if getattr(PP, '_F4FIX_RP', False):
        return
    orig = PP.run_pipeline

    def run_pipeline(*a, **k):
        sweep('run_pipeline')
        return orig(*a, **k)
    PP.run_pipeline = run_pipeline
    PP._F4FIX_RP = True


# ---------------------------------------------------------------- S2c: the same misreading through F4v3
# guards_c.f4v3_subject_mismatch (phase1i/taskC/guards_c.py:339) -> sk_features_v3 (:323), whose FIRST step is
# `feats, sources = C.sk_features(sk)` (:328) = the ORIGINAL checker_1i.sk_features with the A1 ending misreading.
# F4v3 = F4v2 + an extra number signal consulted only when sk_features finds nothing, so on the 5 sentences it
# re-fires on exactly the false -te/-s/-me signals. It runs in the guards_c decide wrapper AFTER the model layer
# (guards_c.py:127-142), so un-firing it never creates an L3 request. Fix = the same fixed sk_features bound into
# copies of sk_features_v3 + f4v3_subject_mismatch; sk_number_extra is untouched. P2J_F4V3FIX=0 = run_S2 behaviour.
OLD3, FN3 = [], [None]


def build_fixed_v3(G, C, lang='sk'):
    src = os.path.abspath(G.__file__)
    text = open(src, encoding='utf-8').read()
    fx = build_fixed(C, lang)
    ns = dict(G.__dict__)
    ns['_SF_2J'] = fx['sk_features']
    v3 = _sub(_func_src(text, 'sk_features_v3'), "feats, sources = C.sk_features(sk)", "feats, sources = _SF_2J(sk)", 1)
    exec(compile(v3, src + ':sk_features_v3[2J]', 'exec'), ns)
    exec(compile(_func_src(text, 'f4v3_subject_mismatch'), src + ':f4v3[2J]', 'exec'), ns)
    return dict(fx, sk_features_v3=ns['sk_features_v3'], f4v3_subject_mismatch=ns['f4v3_subject_mismatch'])


def v3_patch():
    C = sys.modules.get('checker_1i'); n = 0
    for m in list(sys.modules.values()):
        f = getattr(m, '__file__', '') or ''
        if f.endswith(os.sep + 'guards_c.py') and hasattr(m, 'GUARDS') and not getattr(m, 'F4V3FIX_2J', False):
            fx = build_fixed_v3(m, C)
            for old in (m.f4v3_subject_mismatch, m.GUARDS.get('F4v3')):
                if old is not None and all(old is not o for o in OLD3):
                    OLD3.append(old)
            m.GUARDS['F4v3'] = m.f4v3_subject_mismatch = FN3[0] = fx['f4v3_subject_mismatch']
            m.sk_features_v3 = fx['sk_features_v3']; m.F4V3FIX_2J = True; n += 1
    return n


def _is_old3(v):
    return any(v is o for o in OLD3)


def sweep3():
    import gc
    if not OLD3 or FN3[0] is None:
        return 0
    n = 0
    for o in gc.get_objects():
        if type(o) is types.FunctionType:
            for c in (o.__closure__ or ()):
                try:
                    v = c.cell_contents
                except ValueError:
                    continue
                if _is_old3(v):
                    c.cell_contents = FN3[0]; n += 1
        elif isinstance(o, dict):
            for k in ('f4v3_subject_mismatch', 'F4v3'):
                try:
                    v = dict.get(o, k)
                except Exception:
                    continue
                if _is_old3(v):
                    dict.__setitem__(o, k, FN3[0]); n += 1
    return n


_sweep_v2 = sweep


def sweep(where=''):
    r = _sweep_v2(where)
    if os.environ.get('P2J_F4V3FIX', '1') == '1':
        m = v3_patch(); k = sweep3()
        sys.stderr.write('F4V3FIX sweep %s: %d modules, %d refs\n' % (where, m, k))
        r += k
    return r
