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
import os, re
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


def pp_shadow(w, preps):
    sh = set()
    for i, x in enumerate(w):
        if x in preps:
            j, k = i + 1, 0
            while j < len(w) and k < 3 and is_mod(w[j]):
                sh.add(j); j += 1; k += 1
            if k and j < len(w):
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
