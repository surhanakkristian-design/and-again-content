#!/usr/bin/env python3
"""Phase 1i — Task C: three offline guards that cut false acceptance, DEV-only design.

  F6   addition guard   — content in the answer that no accepted rendering of the Slovak has
  F5t  F5 tightening    — deletions F5 misses because the answer ALSO substitutes a word somewhere
  F4v3 number signal    — Slovak number signals F4v2 has no rule for (byt-future paradigm, -uje/-ujú/-ajú)

Zero model calls: a guard that fires rejects an answer before the model layer, everything else keeps the
frozen Phase 1h row-7 verdict.  NO import-time side effects: the checker module is bound lazily
(`bind(mod)` / `apply(mod)`), nothing is written and no path is touched at import.

Integration:
    import checker_1i as C, guards_c
    guards_c.apply(C, guards=("F6", "F5t", "F4v3"))   # -> C.decide is wrapped, returns layer 'F6'/'F5t'/'F4v3'
    guards_c.apply(C, guards=())                       # -> restores the original C.decide

Measurement (offline, re-runnable, writes taskC/results.json):
    python3 phase1i/taskC/guards_c.py --selftest
    python3 phase1i/taskC/guards_c.py --measure
"""
import difflib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P1I = os.path.dirname(HERE)

# ---------------------------------------------------------------- lazy binding of the checker module
_C = None


def bind(mod):
    global _C
    _C = mod
    return _C


def _c():
    global _C
    if _C is None:                                   # only on demand, never at import
        if P1I not in sys.path:
            sys.path.insert(0, P1I)
        import checker_1i as m
        _C = m
    return _C


# ---------------------------------------------------------------- shared machinery (same as F5's)
_VOCAB = {}


def _variant_vocab(it):
    """Every English token the annotation sanctions for this sentence: all accepted references (incl. the
    gender variants refs_of() adds), every `alt` alternative, every `d` optional and, when the table
    answers, the synonym group of each reference token.  STRUCTURAL: nothing is hand-listed here."""
    C = _c()
    key = (it['exercise_id'], it['reference'])
    if key in _VOCAB:
        return _VOCAB[key]
    a = C.annot(it['exercise_id']) or {}
    vocab = set()
    for r in C.refs_of(it):
        vocab |= set(C.expand(C.toks(r)))
    pieces = []
    alt = a.get('alt')
    if isinstance(alt, dict):
        for k, v in alt.items():
            pieces.append(str(k))
            pieces += [str(x) for x in (v if isinstance(v, (list, tuple)) else [v])]
    elif isinstance(alt, list):
        for e in alt:
            if isinstance(e, dict):
                pieces += [str(x) for x in e.keys()] + [str(x) for x in e.values()]
            elif isinstance(e, (list, tuple)):
                pieces += [str(x) for x in e]
            else:
                pieces.append(str(e))
    for k, v in (a.get('d') or {}).items():
        pieces += [str(k), str(v)]
    for k, v in (a.get('s') or {}).items():
        pieces.append(str(k))
    for p in pieces:
        for part in re.split(r'[|/]', str(p)):
            vocab |= set(C.expand(C.toks(part)))
    for w in list(vocab):
        try:
            for e in C.syn_equivalents(w) or []:
                vocab |= set(C.expand(C.toks(str(e))))
        except Exception:
            pass
    vocab.discard('')
    _VOCAB[key] = vocab
    return vocab


def _eff(text, opt):
    C = _c()
    return [t for t in C.expand(C.toks(text)) if t not in opt]


def _hunks(ref_eff, ans_eff):
    """difflib opcodes on the option-stripped token lists.
    'delete'  = ref span with nothing in its place        -> deletion candidate (F5t)
    'insert'  = answer span with nothing in its place      -> addition candidate (F6)
    'replace' = both sides non-empty in the same gap       -> word choice / substitution, NEVER a fire.
    Because difflib never emits an adjacent insert+delete pair (that gap is one 'replace'), pairing an
    addition with the deletion it substitutes is automatic and needs no heuristic."""
    sm = difflib.SequenceMatcher(None, ref_eff, ans_eff, autojunk=False)
    dels, ins, reps = [], [], []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'delete':
            dels.append((i1, ref_eff[i1:i2]))
        elif tag == 'insert':
            ins.append((i1, ans_eff[j1:j2]))
        elif tag == 'replace':
            reps.append((ref_eff[i1:i2], ans_eff[j1:j2]))
    return dels, ins, reps


_LEMMA = {}
NEG = {'not', 'no', 'none', 'never', 'nothing', 'nobody', 'nowhere', 'neither', 'nor', "n't"}
_SUF = ('ingly', 'edly', 'ly', 'ing', 'ies', 'ied', 'es', 'ed', 's')


def _lemma(t):
    C = _c()
    if not _LEMMA:
        for b, p, pp in C.IRREG:
            _LEMMA.setdefault(p, b)
            _LEMMA.setdefault(pp, b)
    return _LEMMA.get(t, t)


def _stem(t):
    """Crude derivational stem: irregular past/participle -> base, then one regular suffix, then a final -e.
    Used ONLY to recognise that a word is still present in the other sentence in another form
    (careful/carefully, left/leave, lashes/eyelash) — never to decide meaning."""
    l = _lemma(t)
    for s in _SUF:
        if l.endswith(s) and len(l) - len(s) >= 3:
            l = l[:-len(s)]
            break
    if len(l) >= 4 and l.endswith('e'):
        l = l[:-1]
    return l


def _present(tok, others, other_stems):
    if tok in others:
        return True
    if tok in NEG and (others & NEG):
        return True                                  # negation realised by another negative word
    s = _stem(tok)
    if s in other_stems:
        return True
    return len(s) >= 4 and any(s in o for o in others)     # lashes <-> eyelash


def _drop_moves(hunks, other_side_tokens):
    """A token that is simply somewhere else in the other sentence — in any form — is a word-order move or
    a re-realisation, not a deletion and not an addition."""
    stems = {_stem(t) for t in other_side_tokens}
    out = []
    for pos, span in hunks:
        keep = [t for t in span if not _present(t, other_side_tokens, stems)]
        if keep:
            out.append((pos, keep, span))
    return out


def _unpair(dels, ins, window=3):
    """difflib emits an ADJACENT insert+delete pair as a single 'replace' hunk, but a substitution whose two
    words sit a couple of tokens apart ('Honey, apparently he left' -> 'Honey, he supposedly left') comes
    back as a separate delete and insert.  A deletion and an insertion within `window` reference positions
    of each other are therefore treated as one substitution and BOTH are dropped."""
    dpos = [p for p, _k, _s in dels]
    ipos = [p for p, _k, _s in ins]
    d = [(p, k, s) for p, k, s in dels if not any(abs(p - q) <= window for q in ipos)]
    i = [(p, k, s) for p, k, s in ins if not any(abs(p - q) <= window for q in dpos)]
    return d, i


# ---------------------------------------------------------------- C2: F5t, the tightened deletion guard
def f5t_deletion(it):
    """F5 fires only when the answer is a pure order-preserving subsequence of an accepted rendering, so a
    single substituted word anywhere ("thorns" for "spines") makes it abstain on the whole sentence, even
    when a meaning-carrying span is missing elsewhere.  F5t replaces the subsequence test by a diff: only
    'delete' hunks count, 'replace' hunks (word choice) are left to F3 / the model.  The information test is
    F5's own `span_information()` — no new word list.  Abstains as soon as ONE accepted rendering yields no
    fire, exactly like F5."""
    C = _c()
    opt = C.optional_tokens(it)
    ans = _eff(it['answer'], opt)
    ans_set = set(ans)
    best = None
    for r in C.refs_of(it):
        ref = _eff(r, opt)
        if ref == ans:
            return False, {'fired': False, 'reason': 'answer equals an accepted variant', 'variant': r}
        dels, ins, reps = _hunks(ref, ans)
        dels, ins = _unpair(_drop_moves(dels, ans_set), _drop_moves(ins, set(ref)))
        pds = C._postdash_start(r, opt)
        reasons = []
        for pos, keep, span in dels:
            why = C.span_information([(pos + i, t) for i, t in enumerate(keep)], opt, pds)
            if why:
                reasons.append({'deleted': ' '.join(keep), 'why': why, 'position': pos, 'ref_len': len(ref)})
        if not reasons:
            return False, {'fired': False, 'reason': 'no information-carrying unpaired deletion', 'variant': r,
                           'substitutions': [[' '.join(a), ' '.join(b)] for a, b in reps][:4]}
        if best is None or len(reasons) < len(best[1]):
            best = (r, reasons)
    if best is None:
        return False, {'fired': False, 'reason': 'no accepted rendering to compare with'}
    return True, {'fired': True, 'guard': 'F5t', 'variant': best[0], 'spans': best[1],
                  'deleted': '; '.join(s['deleted'] for s in best[1]),
                  'why': '; '.join(s['why'] for s in best[1])}


# ---------------------------------------------------------------- C1: F6, the addition guard
def addition_information(span, vocab):
    """Mirror of F5's span_information, deliberately ASYMMETRIC: only a CONTENT word the annotation does not
    sanction anywhere counts as added meaning.  Function words are never an addition, because English
    realises Slovak morphology with them: articles, do-support, the dropped pronoun subject, optional
    'that', contractions, particles and degree adverbs.  Nothing here is a list built from the DEV
    failures — FUNCTION is F3/F5's table and `vocab` is the annotation."""
    C = _c()
    content = [t for t in span if t not in C.FUNCTION and t not in vocab]
    if not content:
        return None
    return 'added content word(s) %s' % ' '.join(content[:4])


def f6_addition(it):
    """The mirror of F5: content the learner states that no accepted rendering of the Slovak states.
    Fires on 'insert' hunks only (a 'replace' hunk is a word-choice error, not an addition), never on a
    token that only moved, never on a token any accepted rendering / `alt` / `d` / synonym group contains,
    and abstains as soon as ONE accepted rendering yields no fire."""
    C = _c()
    opt = C.optional_tokens(it)
    ans = _eff(it['answer'], opt)
    vocab = _variant_vocab(it)
    best = None
    for r in C.refs_of(it):
        ref = _eff(r, opt)
        if ref == ans:
            return False, {'fired': False, 'reason': 'answer equals an accepted variant', 'variant': r}
        dels, ins, reps = _hunks(ref, ans)
        ref_set = set(ref)
        dels, ins = _unpair(_drop_moves(dels, set(ans)), _drop_moves(ins, ref_set))
        reasons = []
        for pos, keep, span in ins:
            # Only a PREPOSITIONAL PHRASE counts as added meaning ('in the pot', 'at night', 'on the cake').
            # A bare added word is almost always a re-realisation of something the Slovak does carry and the
            # reference words differently ('private property', 'right now', 'the guard regrets it'), and F6
            # cannot see the Slovak, so it must not judge those.
            if not (span and span[0] in C.PREP_HEADS and len(span) >= 2):
                continue
            why = addition_information(keep, vocab)
            if why:
                reasons.append({'added': ' '.join(keep), 'why': why, 'position': pos, 'ref_len': len(ref)})
        if not reasons:
            return False, {'fired': False, 'reason': 'no unsanctioned prepositional-phrase addition',
                           'variant': r,
                           'inserted': [' '.join(k) for _p, k, _s in ins][:4],
                           'substitutions': [[' '.join(a), ' '.join(b)] for a, b in reps][:4]}
        if best is None or len(reasons) < len(best[1]):
            best = (r, reasons)
    if best is None:
        return False, {'fired': False, 'reason': 'no accepted rendering to compare with'}
    return True, {'fired': True, 'guard': 'F6', 'variant': best[0], 'spans': best[1],
                  'added': '; '.join(s['added'] for s in best[1]),
                  'why': '; '.join(s['why'] for s in best[1])}


# ---------------------------------------------------------------- C3: F4v3, the missing number signal
# Closed-class paradigm, not a vocabulary: the six future forms of byt' (+ the negated ne- forms).
SK_BYT_FUT = {'budem': ('1', 'sg'), 'budes': ('2', 'sg'), 'budeš': ('2', 'sg'), 'bude': ('3', 'sg'),
              'budeme': ('1', 'pl'), 'budete': ('2', 'pl'), 'budu': ('3', 'pl'), 'budú': ('3', 'pl')}
# Unambiguous present-tense verb endings.  -uje / -ujú are the 3sg / 3pl of the -ovat' class (potrebuje /
# potrebujú, skontroluje / skontrolujú); -ajú is the 3pl of the -at' class.  Endings that a noun or an
# adjective can also carry (-í, -ie, -ia, -a, bare -ú) are deliberately NOT read.
SK_CLAUSE = {'a', 'ale', 'alebo', 'ze', 'že', 'takze', 'takže', 'ked', 'keď', 'keby', 'aby', 'lebo',
             'pretoze', 'pretože', 'ak', 'ci', 'či', 'kym', 'kým', 'nez', 'než', 'ktory', 'ktorý', 'ktora',
             'ktorá', 'ktore', 'ktoré', 'ktoreho', 'ktorého', 'preto', 'kde', 'preco', 'prečo'}
SK_PRESENT_NUM = [('ujú', 'pl'), ('uju', 'pl'), ('ajú', 'pl'), ('aju', 'pl'), ('uje', 'sg')]


def sk_number_extra(sk):
    """-> (number or None, [signal labels]).  NUMBER ONLY.  Person is deliberately not asserted from these
    signals: Slovak recasts the subject freely ('Bude sa ti to pacit' = 'You will like it'), so a person
    claim from a 3sg verb would reject correct answers, while the number of the Slovak subject survives the
    recast.  Two disagreeing signals cancel, exactly like sk_features()'s agree()."""
    C = _c()
    w = C._sk_words(sk)
    # A number read off a verb is the number of THAT verb's subject.  In a multi-clause Slovak sentence
    # ('Naniesla si uz tri vrstvy, takze jej riasy vyzeraju obrovske') the verbs belong to different
    # subjects, so a sentence-level claim is unsound: only single-clause sentences are read.
    if ',' in (sk or '') or (set(w) & SK_CLAUSE):
        return None, ['multi-clause Slovak: no sentence-level number read']
    sig, prev = [], ''
    for x in w:
        after_prep = prev in C.SK_PREP
        prev = x
        if after_prep or x in C.SK_NOT_VERB:
            continue
        base = x[2:] if (x.startswith('ne') and len(x) > 5) else x
        if base in SK_BYT_FUT:
            sig.append(('byt-future ' + x, SK_BYT_FUT[base][1]))
            continue
        if len(x) < 5:
            continue
        for end, num in SK_PRESENT_NUM:
            if x.endswith(end):
                sig.append(('present %s %s' % (end, x), num))
                break
    vals = {n for _l, n in sig}
    return (list(vals)[0] if len(vals) == 1 else None), [l for l, _n in sig]


def sk_features_v3(sk):
    """F4v2's features, plus the extra NUMBER signal — consulted ONLY when F4v2 found no signal at all.
    That makes F4v3 a strict superset of F4v2: on every sentence F4v2 already speaks about, F4v3 decides
    exactly as F4v2 did, so no existing behaviour (and no type-T behaviour) can change."""
    C = _c()
    feats, sources = C.sk_features(sk)
    if sources:
        return feats, sources, False
    num, extra = sk_number_extra(sk)
    if not num:
        return feats, sources, False
    out = dict(feats)
    out['number'] = num
    return out, extra, True


def f4v3_subject_mismatch(it):
    """F4v2 with the extra number signal.  Same clash logic, same abstention rules (no subject pronoun in
    the answer; any answer pronoun compatible with the Slovak)."""
    C = _c()
    feats, sources, used_extra = sk_features_v3(it['sk'])
    if not any(feats.values()):
        return False, {'fired': False, 'reason': 'Slovak underdetermined', 'features': feats,
                       'signals': sources, 'extra_signal': used_extra}
    A = C.en_subjects(it['answer'])
    if not A:
        return False, {'fired': False, 'reason': 'no subject pronoun in the answer', 'features': feats,
                       'signals': sources, 'extra_signal': used_extra}

    def clash(a):
        p, n, g = C.EN_SUBJ[a]
        if feats['person'] and p and feats['person'] != p:
            return 'person'
        if feats['number'] and n and a != 'you' and feats['number'] != n:
            return 'number'
        if feats['gender'] in ('m', 'f') and g in ('m', 'f') and feats['gender'] != g:
            return 'gender'
        return None

    if any(clash(a) is None for a in A):
        return False, {'fired': False, 'reason': 'an answer pronoun is compatible with the Slovak',
                       'features': feats, 'signals': sources, 'pronouns': A, 'extra_signal': used_extra}
    return True, {'fired': True, 'guard': 'F4v3', 'clash': clash(A[0]), 'answer_subject': A[0],
                  'features': feats, 'signals': sources, 'pronouns': A, 'extra_signal': used_extra}


# ---------------------------------------------------------------- integration
GUARDS = {'F5t': f5t_deletion, 'F6': f6_addition, 'F4v3': f4v3_subject_mismatch}
ORDER = ('F5t', 'F6', 'F4v3')
_ORIG_DECIDE = {}


def guards_report(it, guards=ORDER):
    return {g: GUARDS[g](it) for g in guards}


def run_guards(it, guards=ORDER):
    """-> (guard name, trace) of the first guard that fires, else (None, {})."""
    for g in [x for x in ORDER if x in guards]:
        hit, tr = GUARDS[g](it)
        if hit:
            return g, tr
    return None, {}


def apply(checker_module, guards=("F6", "F5t", "F4v3")):
    """Switch the guards into the pipeline of `checker_module` by wrapping its decide().

    The wrapper lets the frozen stack decide first and only re-examines answers it ACCEPTED, which gives
    exactly the accept/reject outcome of inserting the guards in front of the model layer (a guard can only
    ever turn an acceptance into a rejection) while keeping the deciding layer reportable as 'F5t' / 'F6' /
    'F4v3'.  In production the guards are meant to run BEFORE L3, so a fired guard also saves the call.
    `apply(mod, guards=())` restores the original decide.  Idempotent."""
    bind(checker_module)
    orig = _ORIG_DECIDE.get(id(checker_module)) or checker_module.decide
    _ORIG_DECIDE[id(checker_module)] = orig
    if not guards:
        checker_module.decide = orig
        return orig
    use = tuple(g for g in ORDER if g in guards)

    def decide(it, flags, verdicts):
        d = orig(it, flags, verdicts)
        if not d.get('accepted'):
            return d
        on = tuple(g for g in use if flags.get(g, True))
        g, tr = run_guards(it, on)
        if g is None:
            return d
        why = {'F5t': 'missing meaning (%s)', 'F6': 'added meaning (%s)',
               'F4v3': 'wrong subject (%s)'}[g]
        detail = tr.get('why') or ('%s clash, answer "%s", Slovak %s'
                                   % (tr.get('clash'), tr.get('answer_subject'), tr.get('features')))
        out = {'layer': g, 'accepted': False, 'verdict': 'wrong', 'tip': None,
               'why': (why % detail) + '; accepted at %s before the guard' % d['layer'],
               'trace': {g: tr}}
        return out

    checker_module.decide = decide
    return decide


# ================================================================ pre-flight self test (synthetic rows)
def _mk(C, sk, ref, ans, eid=999901, topic='x'):
    C._ANN.setdefault(eid, {})
    C.SK_OF[eid] = sk
    return {'item_id': 'S:%d:%d' % (eid, abs(hash(ans)) % 10 ** 8), 'kind': 'W', 'exercise_id': eid,
            'set': 'NEW', 'level': 'A2', 'topic': topic, 'sk': sk, 'reference': ref, 'answer': ans,
            'verdict': 'wrong', 'step': 'match', 'feedback': '', 'chk_missing': False, 'wrong_type': 'M',
            'wrong_why': '', 'locks': [], 'lock_ok': True, 'lock_released_2_1': None, 'fa_class': None,
            'fa_judgement': None, 'n': 1}


def selftest():
    C = _c()
    ok, bad = 0, []
    cases = [
        # (guard, expect, sk, reference, answer, label)
        ('F6', True, 'Pockaj chvilu a voda zovrie!', 'Wait a minute and the water will boil!',
         'Wait a minute and the water will boil in the pot!', 'pure content addition'),
        ('F6', True, 'Pockaj chvilu a voda zovrie!', 'Wait a minute and the water will boil!',
         'Wait a moment and the water will boil in the pot!', 'addition + unrelated substitution'),
        ('F6', False, 'Pockaj chvilu a voda zovrie!', 'Wait a minute and the water will boil!',
         'Just wait a minute and the water will boil!', 'function-word addition is not an addition'),
        ('F6', False, 'Pockaj chvilu a voda zovrie!', 'Wait a minute and the water will boil!',
         'Wait a moment and the water will boil!', 'substitution only'),
        ('F6', False, 'Pockaj chvilu a voda zovrie!', 'Wait a minute and the water will boil!',
         'Wait a minute and the water will boil', 'identical after normalisation'),
        ('F6', False, 'On uz precital sest zdrojov.', 'He has checked six sources tonight.',
         'Tonight he has checked six sources.', 'word-order move is not an addition'),
        ('F5t', True, 'Strav i vecer vytahovanim trnov z prsta.',
         'He will spend the evening pulling spines out of his finger.',
         "He'll spend the evening pulling thorns out.", 'deletion behind a substitution (F5 abstains)'),
        ('F5t', False, 'Voda zovrie.', 'The water will boil.', 'Water will boil.', 'article only'),
        ('F5t', False, 'On uz precital sest zdrojov.', 'He has checked six sources tonight.',
         'Tonight he has checked six sources.', 'word-order move is not a deletion'),
        ('F5t', False, 'Pockaj chvilu a voda zovrie!', 'Wait a minute and the water will boil!',
         'Wait a moment and the water will boil!', 'substitution only'),
        ('F4v3', True, 'Potrebuje novy telefon.', 'He needs a new phone.', 'They need a new phone.',
         '-uje is 3sg, "they" is plural'),
        ('F4v3', False, 'Potrebuju novy telefon.', 'They need a new phone.', 'They need a new phone.',
         '-uju is 3pl, no clash'),
        ('F4v3', False, 'Potrebuje novy telefon.', 'He needs a new phone.', 'He needs a new phone.',
         '3sg vs he, no clash'),
        ('F4v3', False, 'Potrebuje novy telefon.', 'He needs a new phone.', 'I need a new phone.',
         'person is NOT asserted from the extra signal (1sg is singular -> no number clash)'),
        ('F4v3', True, 'Do desiatej bude zohrievat rezance.', 'He will be reheating noodles by ten.',
         'They will be reheating noodles by ten.', 'byt-future "bude" is 3sg'),
        ('F4v3', False, 'Bude sa ti to pacit.', 'You will like it.', 'You will like it.',
         'recast subject: "you" is exempt from the number test'),
        ('F4v3', False, 'Budu cakat pred domom.', 'They will wait in front of the house.',
         'They will wait in front of the house.', 'byt-future "budu" is 3pl'),
    ]
    for guard, expect, sk, ref, ans, label in cases:
        hit, tr = GUARDS[guard](_mk(C, sk, ref, ans))
        if bool(hit) == expect:
            ok += 1
        else:
            bad.append({'guard': guard, 'expected': expect, 'got': bool(hit), 'case': label,
                        'answer': ans, 'trace': tr})
    print('selftest %d/%d' % (ok, len(cases)))
    for b in bad:
        print('  FAIL', json.dumps(b, ensure_ascii=False)[:400])
    return not bad


# ================================================================ measurement on DEV
ROW7 = {'F1': 1, 'F2': 1, 'F3': 1, 'F4v2': 1, 'F5': 1, 'F2B': 1}


def _load():
    if P1I not in sys.path:
        sys.path.insert(0, P1I)
    C = _c()
    from loader import load_items, load_annotations
    recs, ann = load_items('dev'), load_annotations('dev')
    for s, a in ann.items():
        C._ANN[int(s)] = a['hygienised']
    for r in recs:
        C.SK_OF[r['sid']] = r['sk']
    return C, recs, ann


def to_item(r):
    return {'item_id': r['item_id'], 'kind': r['kind'], 'exercise_id': r['sid'], 'set': 'NEW',
            'level': r['level'], 'topic': r['topic'], 'sk': r['sk'], 'reference': r['reference'],
            'answer': r['answer'], 'verdict': r['chk']['verdict'], 'step': r['chk']['step'],
            'feedback': r['chk']['feedback'], 'chk_missing': r['chk_missing'],
            'wrong_type': r['wrong_type'], 'wrong_why': '', 'locks': r['locks'], 'lock_ok': r['lock_ok'],
            'lock_released_2_1': r['lock_released_2_1'], 'fa_class': None, 'fa_judgement': None, 'n': r['n']}


def measure():
    C, recs, ann = _load()
    items = {r['item_id']: to_item(r) for r in recs}
    vm = {r['item_id']: r['rows']['row7']['model'] for r in recs if r['rows']['row7']['model']}
    correct = [r for r in recs if r['kind'] == 'C' and r['judged'] == 'correct']
    wrong = [r for r in recs if r['judged'] == 'wrong']
    cw = [r for r in recs if r['kind'] == 'W' and r['judged'] == 'correct']
    base = {r['item_id']: C.decide(items[r['item_id']], ROW7, vm) for r in recs}

    def acc(iid, tip_rejects, fired=None):
        if fired:
            return False
        if not base[iid]['accepted']:
            return False
        if tip_rejects and vm.get(iid) == 'TIP':
            return False
        return True

    fa_file = set(json.load(open(os.path.join(P1I, 'dev', 'false_acceptances.json'))))
    fa_base = {r['item_id'] for r in wrong if acc(r['item_id'], False)}
    checks = {'dev_correct_n': len(correct), 'dev_wrong_n': len(wrong),
              'dev_wrong_judged_correct_n': len(cw),
              'coverage_base_tip_accept': sum(1 for r in correct if acc(r['item_id'], False)),
              'fa_base_tip_accept': len(fa_base),
              'fa_base_matches_dev_file': sorted(fa_base) == sorted(fa_file),
              'coverage_base_tip_reject': sum(1 for r in correct if acc(r['item_id'], True)),
              'fa_base_tip_reject': sum(1 for r in wrong if acc(r['item_id'], True))}
    print('measuring apparatus check:', json.dumps(checks, ensure_ascii=False))
    assert checks['fa_base_matches_dev_file'], 'baseline does not reproduce dev/false_acceptances.json'
    assert checks['coverage_base_tip_accept'] == 160 and checks['fa_base_tip_accept'] == 30

    # every guard on every item, once
    fires = {}
    for r in recs:
        it = items[r['item_id']]
        fires[r['item_id']] = {g: GUARDS[g](it) for g in ORDER}

    def fired_by(iid, gs):
        for g in [x for x in ORDER if x in gs]:
            if fires[iid][g][0]:
                return g
        return None

    out = {'note': 'DEV only. Guards evaluated offline, before the model layer; 0 model calls.',
           'checks': checks, 'configs': {}}
    configs = [('F5t',), ('F6',), ('F4v3',), ('F5t', 'F6', 'F4v3')]
    for cfg in configs:
        name = '+'.join(cfg) if len(cfg) > 1 else cfg[0]
        entry = {'guards': list(cfg)}
        for tip_rejects, scoring in ((False, 'TIP_accept'), (True, 'TIP_reject')):
            removed, lost, kept = [], [], []
            for r in wrong:
                iid = r['item_id']
                g = fired_by(iid, cfg)
                if acc(iid, tip_rejects) and g:
                    removed.append({'id': iid, 'type': r['wrong_type'], 'guard': g,
                                    'layer': base[iid]['layer'], 'model': vm.get(iid),
                                    'why': (fires[iid][g][1].get('why') or fires[iid][g][1].get('clash'))})
                elif acc(iid, tip_rejects):
                    kept.append(iid)
            for r in correct:
                iid = r['item_id']
                g = fired_by(iid, cfg)
                if acc(iid, tip_rejects) and g:
                    tr = fires[iid][g][1]
                    lost.append({'id': iid, 'guard': g, 'answer': r['answer'], 'reference': r['reference'],
                                 'reason': tr.get('why') or ('%s clash %s' % (tr.get('clash'),
                                                                              tr.get('features')))})
            fa_before = sum(1 for r in wrong if acc(r['item_id'], tip_rejects))
            cov_before = sum(1 for r in correct if acc(r['item_id'], tip_rejects))
            fa_after, cov_after = fa_before - len(removed), cov_before - len(lost)
            bytype = {}
            for x in removed:
                bytype[x['type']] = bytype.get(x['type'], 0) + 1
            entry[scoring] = {
                'fa_before': fa_before, 'fa_after': fa_after, 'fa_removed': len(removed),
                'fa_removed_by_type': bytype, 'fa_removed_items': removed,
                'fa_rate_before': [fa_before, len(wrong), C.clopper_pearson(fa_before, len(wrong))],
                'fa_rate_after': [fa_after, len(wrong), C.clopper_pearson(fa_after, len(wrong))],
                'coverage_before': cov_before, 'coverage_after': cov_after,
                'correct_lost': len(lost), 'correct_lost_items': lost,
                'coverage_rate_before': [cov_before, len(correct),
                                         C.clopper_pearson(cov_before, len(correct))],
                'coverage_rate_after': [cov_after, len(correct), C.clopper_pearson(cov_after, len(correct))],
                'residue_ids': [x for x in kept]}
        out['configs'][name] = entry

    # residue after all three guards, itemised
    allg = ('F5t', 'F6', 'F4v3')
    residue = []
    for r in wrong:
        iid = r['item_id']
        if not acc(iid, False) or fired_by(iid, allg):
            continue
        it = items[iid]
        opt = C.optional_tokens(it)
        ans = _eff(it['answer'], opt)
        ref = _eff(it['reference'], opt)
        dels, ins, reps = _hunks(ref, ans)
        subs = ['%s->%s' % (' '.join(a), ' '.join(b)) for a, b in reps]
        insf = [' '.join(k) for _p, k, _s in _drop_moves(ins, set(ref))]
        delf = [' '.join(k) for _p, k, _s in _drop_moves(dels, set(ans))]
        if subs and not insf and not delf:
            why = 'substitution only (%s): word choice, no addition and no deletion to catch' % '; '.join(subs[:3])
        elif insf and not [t for span in insf for t in span.split() if t not in C.FUNCTION]:
            why = 'inserted function words only (%s)' % '; '.join(insf[:3])
        elif not subs and not insf and not delf:
            why = 'no diff against the reference (tense/form or writer artefact)'
        else:
            why = 'diff is %s' % json.dumps({'sub': subs[:2], 'ins': insf[:2], 'del': delf[:2]},
                                            ensure_ascii=False)
        residue.append({'id': iid, 'type': r['wrong_type'], 'layer': base[iid]['layer'],
                        'model': vm.get(iid), 'tip_reject_still_accepted': acc(iid, True), 'why': why})
    out['residue_after_all_guards_tip_accept'] = residue
    out['residue_by_type'] = {t: sum(1 for x in residue if x['type'] == t)
                              for t in sorted({x['type'] for x in residue})}
    out['residue_tip_reject_count'] = sum(1 for x in residue if x['tip_reject_still_accepted'])
    # C3 diagnosis of the 'si' claim
    si_items = [r for r in recs if ' si ' in (' ' + (r['sk'] or '').lower() + ' ')]
    si_stats = {'n_items_with_si': len(si_items), 'person_none': 0, 'person_set': 0, 'examples': []}
    for r in si_items:
        f, s = C.sk_features(r['sk'])
        if f['person'] is None:
            si_stats['person_none'] += 1
        else:
            si_stats['person_set'] += 1
            if len(si_stats['examples']) < 6:
                si_stats['examples'].append({'sid': r['sid'], 'features': f, 'signals': s})
    out['c3_si_diagnosis'] = si_stats
    out['c3_extra_signal_items'] = sorted({r['sid'] for r in recs
                                          if sk_features_v3(r['sk'])[2]})
    dst = os.path.join(HERE, 'results.json')
    json.dump(out, open(dst, 'w'), ensure_ascii=False, indent=1)
    for name, e in out['configs'].items():
        for sc in ('TIP_accept', 'TIP_reject'):
            x = e[sc]
            print('%-14s %-11s FA %d->%d (-%d %s) | coverage %d->%d (-%d)'
                  % (name, sc, x['fa_before'], x['fa_after'], x['fa_removed'], x['fa_removed_by_type'],
                     x['coverage_before'], x['coverage_after'], x['correct_lost']))
    print('residue', len(residue), out['residue_by_type'], 'tip_reject residue', out['residue_tip_reject_count'])
    print('lost items (combined, TIP_accept):')
    for l in out['configs']['F5t+F6+F4v3']['TIP_accept']['correct_lost_items']:
        print('  ', l['guard'], l['id'], '|', l['reason'][:90], '|', l['answer'][:70])
    print('si:', json.dumps(si_stats, ensure_ascii=False)[:600])
    print('extra-signal sids:', out['c3_extra_signal_items'])
    print('wrote', dst)
    return out


if __name__ == '__main__':
    a = sys.argv[1:]
    if '--selftest' in a or not a:
        okc = selftest()
        if '--measure' not in a:
            sys.exit(0 if okc else 3)
    if '--measure' in a:
        measure()
