#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F8 - voice guard (Slovak nominative agent vs English passive).  100% OFFLINE.

    sk_agent(slovak, annotation=None) -> {"agent_nom", "agent", "voice_sk", "reason"}
    check(slovak, annotation, answer)  -> {"verdict": reject|accept|abstain, ...}
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f9  # noqa: E402

PRON = {'on': ('he', 3, 'sg', 'm'), 'ona': ('she', 3, 'sg', 'f'), 'ono': ('it', 3, 'sg', 'n'),
        'oni': ('they', 3, 'pl', None), 'ony': ('they', 3, 'pl', None), 'ja': ('i', 1, 'sg', None),
        'ty': ('you', 2, 'sg', None), 'my': ('we', 1, 'pl', None), 'vy': ('you', 2, 'pl', None)}
BYT_PAST = {'bol', 'bola', 'bolo', 'boli'}
BYT_PRES = {'je', 'sú', 'som', 'si', 'sme', 'ste'}
PART_SUF = ('ný', 'ná', 'né', 'ní', 'tý', 'tá', 'té', 'tí', 'ná', 'ané', 'ený', 'aná', 'ená', 'uté')
IMPERS_V = {'prší', 'sneží', 'mrzne', 'svitá', 'stmieva'}
DAT_PRON = {'mi', 'ti', 'mu', 'jej', 'nám', 'vám', 'im', 'sa'}
SPEECH = set('hovorí hovoria hovorilo vraví vravia tvrdí tvrdia povráva píše píšu zdá myslí verí vie'.split())
EXIST_PREP = f9.PREPS

EN_BE = {'is', 'are', 'was', 'were', 'be', 'been', 'being', 'am', 'gets', 'get', 'got', 'gotten'}
EN_SUBJ_MAP = {'he': ('he', 3, 'sg', 'm'), 'she': ('she', 3, 'sg', 'f'), 'it': ('it', 3, 'sg', 'n'),
               'they': ('they', 3, 'pl', None), 'i': ('i', 1, 'sg', None), 'you': ('you', 2, None, None),
               'we': ('we', 1, 'pl', None)}
ADJ_PP = f9.PP_ADJ | {'born', 'gone', 'over', 'done', 'finished', 'ready', 'known', 'used'}


def _is_pp(w):
    return (w in f9.PP_ALL) or (w.endswith('ed') and len(w) > 3)


def sk_agent(slovak, annotation=None):
    t = f9.tok(slovak)
    s = ' ' + ' '.join(t) + ' '
    r = lambda nom, ag, voice, why: {'agent_nom': nom, 'agent': ag, 'voice_sk': voice, 'reason': why}
    # participial passive: byť + -ný/-tý
    for i, w in enumerate(t):
        if w in BYT_PAST or w in BYT_PRES:
            for j in (i + 1, i + 2, i - 1):
                if 0 <= j < len(t) and len(t[j]) > 4 and t[j].endswith(PART_SUF) and t[j] not in f9.DET:
                    return r(False, None, 'passive', 'participial passive "%s %s"' % (w, t[j]))
    # reflexive impersonal/passive decided on the MAIN clause only ("Hovorí sa, že ona ..." is impersonal
    # even though a nominative pronoun stands in the subordinate clause)
    _cl = f9._clauses(slovak)
    ft = _cl[0]['toks'] if _cl else t
    if 'sa' in ft and any(w in SPEECH for w in ft) and not any(w in PRON for w in ft):
        return r(False, None, 'impersonal', 'reflexive impersonal main clause ("sa" + speech verb)')
    if 'podarilo' in t or 'darí' in t or any(w in IMPERS_V for w in t):
        return r(False, None, 'impersonal', 'subjectless / impersonal verb')
    for p in ('mi', 'ti', 'mu', 'jej', 'nám', 'vám', 'im'):
        if ' bolo %s ' % p in s or ' je %s ' % p in s:
            return r(False, None, 'impersonal', 'dative-experiencer construction')
    # explicit nominative pronoun (arm B states them)
    for i, w in enumerate(t):
        if w in PRON:
            prev = t[i - 1] if i else ''
            if prev in f9.PREPS:
                continue
            return r(True, w, 'active', 'explicit nominative pronoun "%s"' % w)
    # existential je/sú + PP
    if t and (t[0] in EXIST_PREP) and ('je' in t or 'sú' in t):
        return r(False, None, 'impersonal', 'existential "je/sú" with a locative phrase')
    # noun agent: a noun before an active finite verb, not governed by a preposition
    for i, w in enumerate(t):
        if f9._looks_present(w) or f9._is_l_part(t, i):
            cand = None
            for j in range(i - 1, -1, -1):
                x = t[j]
                if x in f9.PREPS:
                    cand = None
                    break
                if x in f9.DET or x in ('sa', 'si', 'už', 'ešte', 'nie', 'ktorý', 'ktorá', 'ktoré'):
                    continue
                if len(x) > 2 and not any(x.endswith(e) for e in ('om', 'ou', 'mi', 'ch', 'ám', 'ám')):
                    cand = x
                    break
            if cand and 'sa' not in t:
                return r(True, cand, 'active', 'noun "%s" before the active verb "%s"' % (cand, w))
            return r(None, None, None, 'finite verb found but the subject is not clearly nominative')
    return r(None, None, None, 'no clear finite verb / subject signal')


def en_passive(answer):
    raw = (answer or '').strip()
    t = f9._en_tokens(raw)
    if t and t[0] in f9.SUBCONJ:
        m = re.search(r',', raw)
        if not m:
            return {'passive': None, 'reason': 'leading subordinate clause -> abstain', 'subject': None}
        t = f9._en_tokens(raw[m.end():])
    subj = None
    for w in t:
        if w in EN_SUBJ_MAP:
            subj = w
            break
        if w not in ('the', 'a', 'an', 'this', 'that', 'those', 'these', 'my', 'his', 'her', 'their') and w.isalpha():
            subj = w
            break
    rel = 0
    for i, w in enumerate(t):
        if w in f9.REL or (w in f9.SUBCONJ and i > 0):
            rel += 1
            continue
        if w in EN_BE and i + 1 < len(t):
            nxt = t[i + 1]
            if nxt in ('not', 'just', 'already', 'now', 'still', 'also'):
                nxt = t[i + 2] if i + 2 < len(t) else ''
            if _is_pp(nxt) and nxt not in ADJ_PP:
                if rel > 0:
                    rel -= 1
                    continue
                by = None
                if 'by' in t:
                    k = t.index('by')
                    by = ' '.join(t[k + 1:k + 3])
                return {'passive': True, 'reason': '"%s %s"' % (w, nxt), 'subject': subj, 'by': by}
    return {'passive': False, 'reason': 'no passive main clause found', 'subject': subj, 'by': None}


def _ref_subject(annotation):
    a = f9._ann(annotation) if hasattr(f9, '_ann') else {}
    for v in (a.get('v') or []):
        t = f9._en_tokens(v)
        for w in t:
            if w in EN_SUBJ_MAP:
                return w
            if w not in ('the', 'a', 'an', 'this', 'that') and w.isalpha():
                return w
    return None


def check(slovak, annotation, answer):
    sk = sk_agent(slovak, annotation)
    en = en_passive(answer)
    base = {'sk': sk, 'en': en}
    if not sk.get('agent_nom'):
        base.update(verdict=('accept' if sk['agent_nom'] is False else 'abstain'),
                    reason='Slovak has no asserted nominative agent (%s)' % sk['reason'])
        return base
    if en.get('passive') is not True:
        base.update(verdict='accept', reason='English main clause is not passive')
        return base
    ag = sk['agent']
    want = PRON.get(ag, (None,))[0]
    subj = (en.get('subject') or '')
    low = ' ' + ' '.join(f9._en_tokens(answer)) + ' '
    if want:
        if subj == want or (want == 'they' and subj in ('they',)) :
            base.update(verdict='accept', reason='the Slovak agent is still the English subject')
            return base
        if (' %s ' % want) not in low and not (want == 'i' and ' me ' in low):
            base.update(verdict='reject', reason='Slovak names the agent "%s" in the nominative; the English main '
                                                 'clause is passive (%s) and the agent is gone' % (ag, en['reason']))
            return base
        if en.get('by'):
            base.update(verdict='reject', reason='Slovak agent "%s" appears only in a by-phrase of a passive' % ag)
            return base
        base.update(verdict='reject', reason='Slovak agent "%s" is not the subject of the passive English clause' % ag)
        return base
    ref = _ref_subject(annotation)
    if ref and subj and ref == subj:
        base.update(verdict='accept', reason='English subject matches the reference subject')
        return base
    if en.get('by'):
        base.update(verdict='reject', reason='Slovak names a nominative agent "%s"; English demotes it to a by-phrase' % ag)
        return base
    base.update(verdict='abstain', reason='noun agent, English subject not resolvable -> abstain')
    return base


CASES = [
    ("Ona opravila bicykel.", "The bike was repaired by her.", {'reject'}),
    ("Ona opravila bicykel.", "The bike was repaired.", {'reject'}),
    ("Ona opravila bicykel.", "She repaired the bike.", {'accept'}),
    ("On natočil kuchyňu.", "The kitchen was filmed by him.", {'reject'}),
    ("On natočil kuchyňu.", "He filmed the kitchen.", {'accept'}),
    ("Hovorí sa, že je to ťažké.", "It is said that it is hard.", {'accept', 'abstain'}),
    ("O tejto riasenke sa hovorí, že zdvojnásobí dĺžku rias.", "This mascara is said to double the length of the lashes.", {'accept', 'abstain'}),
    ("Jej prejav bol prepísaný dvakrát.", "Her speech was rewritten twice.", {'accept'}),
    ("Najrýchlejšia akcia je ukázaná na konci.", "The fastest action is shown at the end.", {'accept'}),
    ("Ona číta knihu.", "She is reading a book.", {'accept'}),
    ("Ona číta knihu.", "The book is being read by her.", {'reject'}),
    ("Oni postavili dom.", "They built the house.", {'accept'}),
    ("Oni postavili dom.", "The house was built.", {'reject'}),
    ("Dom bol postavený minulý rok.", "The house was built last year.", {'accept'}),
    ("Podarilo sa jej vydržať nehybne.", "She managed to stay still.", {'accept', 'abstain'}),
    ("Ja som napísal list.", "The letter was written.", {'reject'}),
    ("Ja som napísal list.", "I wrote the letter.", {'accept'}),
    ("Prší celý deň.", "It has been raining all day.", {'accept', 'abstain'}),
    ("Na lavičke je jeden dlhý obväz.", "There is one long bandage on the bench.", {'accept', 'abstain'}),
    ("Ty držíš pohár.", "You are holding the glass.", {'accept'}),
    ("Ty držíš pohár.", "The glass is held by you.", {'accept', 'reject'}),
    ("On je unavený.", "He is tired.", {'accept', 'abstain'}),
]


def selftest():
    bad = []
    for sk, en, ok in CASES:
        r = check(sk, None, en)
        if r['verdict'] not in ok:
            bad.append((sk, en, r['verdict'], sorted(ok), r['reason']))
    print('F8 selftest: %d cases, %d failures' % (len(CASES), len(bad)))
    for b in bad:
        print('  FAIL %-45s | %-45s -> %-8s want %s\n        %s' % (b[0][:45], b[1][:45], b[2], b[3], b[4]))
    return 1 if bad else 0


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    for s in sys.argv[1:]:
        print(s, sk_agent(s))
