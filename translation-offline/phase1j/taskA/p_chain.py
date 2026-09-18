#!/usr/bin/env python3
"""Phase 1j Task A — the `p` chain (person / number of the Slovak subject).

Mirrors the `g` (gender) chain: a per-SENTENCE fact derived from the SLOVAK ONLY (the English reference is
never consulted, exactly as in checker_1i.sk_features / taskC F4v3), stored next to `g` in the annotation,
rendered as ONE prompt line that sits where the gender line sits, and consulted by one guard (`f4p`).

Why: 10 of the 23 Phase 1i holdout false acceptances were singular -> plural recasts (8 of them he/she ->
they), every one on a Slovak sentence with a DROPPED subject where person/number live only in the verb
ending.  The P-E4b gender line says "the other gender is SAME"; the model generalised that licence to
person and number.  The `p` line states the person/number explicitly and withdraws the licence there.

API (see README_A.md):
    derive_p(sk, annotation) -> dict | None      dict = {person, number, gender, subject, en_subjects,
                                                        evidence, signals, has_g}
    p_prompt_line(p)         -> str              ONE line, same slot as GENDER_TMPL
    f4p_guard(answer, p, annotation) -> (reject, reason)
    annotate(annotations, sentences)  -> {sid(str): p|None}
    p_of(ann_entry, sk)      -> p|None           read a stored p, else derive on the fly

CLI (0 model calls):
    PYTHONDONTWRITEBYTECODE=1 python3 p_chain.py --side dev          # writes annotations_p_dev.json
    PHASE1J_FINAL=1 PYTHONDONTWRITEBYTECODE=1 python3 p_chain.py --side holdout   # agent F only
    PYTHONDONTWRITEBYTECODE=1 python3 p_chain.py --count-all         # COUNTS ONLY over all 140
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P1J = os.path.dirname(HERE)

# ---------------------------------------------------------------- Slovak lexical resources
WORD_RE = re.compile(r"[a-záäčďéěíľĺňóôöŕřšťúůüýž]+")
VOW = 'aeiouáéíóúýäôyě'

SK_PREP = {'s', 'so', 'z', 'zo', 'k', 'ku', 'v', 'vo', 'na', 'do', 'od', 'po', 'pod', 'nad', 'pred', 'za',
           'medzi', 'o', 'pri', 'cez', 'bez', 'u', 'popri', 'okolo', 'podľa', 'proti', 'voči', 'napriek'}
# nominative subject pronouns only (oblique forms are never nominative subjects)
PRON = {'ja': (1, 'sg', None), 'ty': (2, 'sg', None), 'on': (3, 'sg', 'm'), 'ona': (3, 'sg', 'f'),
        'ono': (3, 'sg', 'n'), 'my': (1, 'pl', None), 'vy': (2, None, None),
        'oni': (3, 'pl', None), 'ony': (3, 'pl', None)}
AUX = {'som': (1, 'sg'), 'sme': (1, 'pl'), 'ste': (2, 'pl')}      # 'si' is ambiguous -> handled apart
BYT_FUT = {'budem': (1, 'sg'), 'budes': (2, 'sg'), 'budeš': (2, 'sg'), 'bude': (3, 'sg'),
           'budeme': (1, 'pl'), 'budete': (2, 'pl'), 'budu': (3, 'pl'), 'budú': (3, 'pl')}
# closed class of very frequent finite forms whose person+number is unambiguous and which no noun shares
LEX = {'má': (3, 'sg'), 'nemá': (3, 'sg'), 'majú': (3, 'pl'), 'nemajú': (3, 'pl'),
       'môže': (3, 'sg'), 'nemôže': (3, 'sg'), 'môžu': (3, 'pl'), 'nemôžu': (3, 'pl'),
       'musí': (3, 'sg'), 'nemusí': (3, 'sg'), 'musia': (3, 'pl'), 'nemusia': (3, 'pl'),
       'chce': (3, 'sg'), 'nechce': (3, 'sg'), 'chcú': (3, 'pl'), 'nechcú': (3, 'pl'),
       'vie': (3, 'sg'), 'nevie': (3, 'sg'), 'vedia': (3, 'pl'), 'nevedia': (3, 'pl'),
       'ide': (3, 'sg'), 'nejde': (3, 'sg'), 'idú': (3, 'pl'), 'nejdú': (3, 'pl'),
       'príde': (3, 'sg'), 'prídu': (3, 'pl'), 'dá': (3, 'sg'), 'dajú': (3, 'pl'),
       'smie': (3, 'sg'), 'smú': (3, 'pl')}
COPULA = {'je', 'sú', 'nie', 'niet', 'su'}       # never read: existentials + explicit-noun predications
# imperative forms: they are 2nd person but say nothing about the sentence's subject
IMPER = {'pozri', 'pozrite', 'pozor', 'rozlúč', 'rozlúčte', 'počkaj', 'počkajte', 'poď', 'poďte', 'daj',
         'dajte', 'drž', 'držte', 'nechaj', 'nechajte', 'skús', 'skúste', 'choď', 'choďte', 'urob',
         'urobte', 'povedz', 'povedzte', 'vezmi', 'vezmite', 'ukáž', 'ukážte', 'nezabudni', 'predstav'}
# impersonal reflexive verbs ("hovorí sa, že ...") — no subject at all, so no signal
REFL_IMPERSONAL = {'hovorí', 'hovori', 'vraví', 'vravi', 'zdá', 'zda', 'povráva', 'tvrdí', 'zdalo', 'zdá'}
# whole-sentence vetoes
IMPERSONAL_WORDS = {'treba', 'prší', 'prsi', 'sneží', 'mrzne', 'svitá', 'stmieva'}
QUANT = {'veľa', 'vela', 'mnoho', 'málo', 'malo', 'niekoľko', 'niekolko', 'pár', 'par', 'väčšina',
         'vacsina', 'polovica', 'tucet'}     # a quantified subject takes a 3sg verb, English is plural
DAT = {'mi', 'ti', 'mu', 'jej', 'nám', 'nam', 'vám', 'vam', 'im'}           # dative experiencer recasts
SK_NOT_VERB = {'sedem', 'osem', 'sem', 'tam', 'dom', 'program', 'problém', 'systém', 'krém', 'sám', 'iba',
               'však', 'ešte', 'aspoň', 'práve', 'kôš', 'kos', 'album', 'tandem', 'totem', 'diplom',
               'zlatko', 'predtým', 'potom', 'znova', 'celkom', 'tiež', 'príliš', 'prilis', 'vankúš',
               'vankus', 'klobúk', 'ďalej', 'dnes', 'včera', 'vcera'}
# words that LOOK like an l-participle (vowel + l/la/lo/li) but are nouns or adjectives
NOT_PARTICIPLE = {'škola', 'skola', 'školy', 'sila', 'sily', 'skala', 'skaly', 'vila', 'víla', 'žila',
                  'telo', 'čelo', 'celo', 'kolo', 'dielo', 'biela', 'bielo', 'hotel', 'hotely',
                  'materiál', 'detail', 'mobil', 'štýl', 'styl', 'gól', 'kanál', 'panel', 'futbal',
                  'basketbal', 'volejbal', 'bicykel', 'stôl', 'uhol', 'kotol', 'popol', 'anjel', 'motýl',
                  'email', 'level', 'kúpeľ', 'nedeľa', 'chvíla', 'ihla', 'guľa', 'salón', 'salóne'}
NOUN_I = {'ľudí', 'ludi', 'dverí', 'dveri', 'detí', 'deti', 'očí', 'oci', 'koní', 'vecí', 'veci',
          'hostí', 'nocí', 'kostí', 'častí', 'casti', 'peňazí', 'penazi', 'tri', 'štyri', 'styri',
          'ruží', 'zvierat', 'mesiací', 'schodí', 'ľudi'}
NOUN_I_SUF = ('ší', 'cí', 'zí', 'ží', 'čí', 'ji', 'ci', 'si', 'zi')       # comparatives, soft adjectives
VERB_S_SUF = ('eš', 'íš', 'áš', 'ieš', 'ýš', 'iš')                        # 2sg -š, not 'vankúš' / 'kôš'
L_PART = re.compile(r'^(.*?)(l|la|lo|li)$')        # modern Slovak plural participle is -li only, never -ly


def sk_words(sk):
    return WORD_RE.findall((sk or '').lower())


def _is_participle(x):
    """Is `x` plausibly an l-participle?  (vowel + l(+a/o/i), not a known noun/adjective, never -lá.)"""
    if len(x) < 4 or x in NOT_PARTICIPLE or x.endswith('lá'):
        return None
    m = L_PART.match(x)
    if not m or not m.group(1):
        return None
    stem, end = m.group(1), m.group(2)
    if stem[-1:] not in VOW:
        return None
    num = 'pl' if end == 'li' else 'sg'
    gen = {'l': 'm', 'la': 'f', 'lo': 'n', 'li': None}[end]
    return num, gen


# ---------------------------------------------------------------- derivation
CLAUSE_IGNORE = {'že', 'ze', 'takže', 'takze', 'lebo', 'pretože', 'pretoze', 'keď', 'ked', 'kým', 'kym',
                 'keby', 'aby', 'žeby', 'zeby', 'ak', 'či', 'ci', 'než', 'nez', 'ktorý', 'ktory', 'ktorá',
                 'ktora', 'ktoré', 'ktore', 'ktorého', 'ktoreho', 'ktorú', 'ktoru', 'ktorom', 'ktorým',
                 'ktorym', 'ktorej', 'ktorých', 'ktorych', 'ktorí', 'ktori', 'preto', 'kde', 'prečo',
                 'preco', 'kedy', 'pokiaľ', 'pokial', 'zatiaľ', 'zatial', 'hoci', 'akoby', 'kto', 'čo'}
SEG_RE = re.compile(r"[a-záäčďéěíľĺňóôöŕřšťúůüýž]+|[,.;!?—–]")
PUNCT = ',.;!?—–'


def clause_words(sk):
    """-> [[words of a READABLE clause]].

    The Slovak is cut at commas and sentence marks.  The first non-empty clause is always read; a later
    clause is read only when it is coordinated or unmarked ('..., ale dnes tancuje', '..., tak ho musíš
    držať').  A clause introduced by a subordinator has its OWN subject and is never read — without that
    rule sid 7444 ('Naniesla si už tri vrstvy, takže jej riasy vyzerajú obrovské') would claim 3pl from
    the lashes and reject the correct singular answer."""
    toks = SEG_RE.findall((sk or '').lower())
    segs, cur = [], []
    for t in toks:
        if t in PUNCT:
            if cur:
                segs.append(cur)
            cur = []
        else:
            cur.append(t)
    if cur:
        segs.append(cur)
    out = []
    for seg in segs:
        if not seg:
            continue
        if out and seg[0] in CLAUSE_IGNORE:
            continue
        out.append(seg)
    return out


def derive_p(sk, annotation=None):
    """Person / number (/ gender) of the Slovak subject, or None when the Slovak leaves it open.

    Conservative by construction: only readable clauses are consulted (clause_words), every signal must
    agree, a single disagreement inside the sentence cancels the feature, an impersonal ('prší', 'treba')
    or a dative experiencer ('podarilo sa jej') returns None, and a quantified subject ('veľa ľudí' takes a
    3sg verb but is plural in English) suppresses the number claim.  Imperatives and the impersonal
    'hovorí sa' contribute nothing; the present copula 'je'/'sú' is never read (existentials and explicit
    noun subjects).  The English reference is never consulted."""
    return explain_p(sk, annotation)[0]


def explain_p(sk, annotation=None):
    """-> (p|None, reason).  Same derivation as derive_p, with the reason a sentence stays ambiguous."""
    w = sk_words(sk)
    if not w:
        return None, 'empty'
    if IMPERSONAL_WORDS & set(w):
        return None, 'impersonal verb (prší / treba ...)'
    for i, x in enumerate(w):                                  # dative experiencer next to a reflexive
        if x == 'sa':
            for j, y in enumerate(w):
                if y in DAT and 0 < abs(i - j) <= 3:
                    return None, 'dative experiencer next to a reflexive (podarilo sa jej ...)'
    clauses = clause_words(sk)
    if not clauses:
        return None, 'no readable clause'
    p, reason = _derive(clauses, annotation)
    if p and (QUANT & set(w)) and p['number']:
        p['number'] = None
        p['signals'].append('quantified subject (veľa / mnoho / niekoľko ...): number not claimed')
        if not p['person']:
            return None, 'quantified subject: number unreliable, no person signal'
        p['en_subjects'] = licensed_subjects(p)
        p['evidence'] = _evidence(p)
    return p, reason


def _evidence(p):
    return '%s -> person %s, number %s, gender %s' % ('; '.join(p['signals'][:5]), p['person'] or 'open',
                                                      p['number'] or 'open', p['gender'] or 'open')


def _derive(clauses, annotation=None):
    sig = []
    ambiguous_si = any(x == 'si' for c in clauses for x in c)
    for c in clauses:
        prev = ''
        for i, x in enumerate(c):
            after_prep = prev in SK_PREP
            nxt = c[i + 1] if i + 1 < len(c) else ''
            prv = prev
            prev = x
            if x in ('si', 'sa') or x in IMPER:
                continue
            if x in PRON and not after_prep:
                pp, nn, gg = PRON[x]
                sig.append(('pronoun ' + x, pp, nn, gg))
                continue
            if x in AUX and not after_prep:
                pp, nn = AUX[x]
                sig.append(('past auxiliary ' + x, pp, nn, None))
                continue
            if after_prep or x in SK_NOT_VERB or x in COPULA:
                continue
            if x in REFL_IMPERSONAL and 'sa' in (prv, nxt):
                continue                                       # 'hovorí sa, že ...' — no subject at all
            base = x[2:] if (x.startswith('ne') and len(x) > 5) else x
            if base in BYT_FUT:
                pp, nn = BYT_FUT[base]
                sig.append(('byt-future ' + x, pp, nn, None))
                continue
            if x in LEX:
                pp, nn = LEX[x]
                sig.append(('finite ' + x, pp, nn, None))
                continue
            if len(x) < 4:
                continue
            if x.endswith(VERB_S_SUF):
                sig.append(('present -š ' + x, 2, 'sg', None))
                continue
            if x.endswith('me') and len(x) >= 5:
                sig.append(('present -me ' + x, 1, 'pl', None))
                continue
            if x.endswith('te') and len(x) >= 5:
                sig.append(('present -te ' + x, 2, None, None))   # vy = polite sg or pl -> number open
                continue
            if x.endswith(('ím', 'ám', 'iem', 'em')) and not x.endswith(('om', 'ním', 'tím', 'ctvom')):
                sig.append(('present -m ' + x, 1, 'sg', None))
                continue
            if x.endswith(('ujú', 'uju', 'ajú', 'aju')) and len(x) >= 5:
                sig.append(('present 3pl ' + x, 3, 'pl', None))
                continue
            if x.endswith('uje') and len(x) >= 5:
                sig.append(('present 3sg ' + x, 3, 'sg', None))
                continue
            # 3sg present in -í / -i ('tlačí', 'nedelí', 'strávi', 'vráti').  Genitive plurals and
            # comparatives share the ending, so a noun list and the soft-adjective suffixes are excluded,
            # and a short -i needs 5 letters ('kúpi' stays unread, 'deti' / 'tri' are nouns).
            if x not in NOUN_I and not x.endswith(NOUN_I_SUF):
                if x.endswith('í') or (x.endswith('i') and len(x) >= 5):
                    sig.append(('present 3sg ' + x, 3, 'sg', None))
                    continue
        prev = ''
        for x in c:                                            # l-participles (past / conditional)
            after_prep = prev in SK_PREP
            prev = x
            if after_prep or x in SK_NOT_VERB or x in IMPER:
                continue
            pr = _is_participle(x)
            if not pr:
                continue
            num, gen = pr
            has_aux = ambiguous_si or any(s[0].startswith('past auxiliary') for s in sig)
            sig.append(('l-participle ' + x, None if has_aux else 3, num, gen))
    if not sig:
        return None, 'no readable person/number morphology in the main clause'

    def agree(idx):
        vals = {s[idx] for s in sig if s[idx] is not None}
        return list(vals)[0] if len(vals) == 1 else None

    person, number, gender = agree(1), agree(2), agree(3)
    if person is None and number is None:
        return None, 'signals disagree on both person and number (%s)' % '; '.join(s[0] for s in sig)
    p = {'person': person, 'number': number, 'gender': gender,
         'subject': 'explicit' if any(s[0].startswith('pronoun') for s in sig) else 'dropped',
         'signals': [s[0] for s in sig],
         'has_g': bool(_g_of(annotation))}
    p['en_subjects'] = licensed_subjects(p)
    p['evidence'] = _evidence(p)
    return p, 'ok'


def _g_of(annotation):
    if not annotation:
        return None
    a = annotation.get('hygienised') or annotation
    return a.get('g') or annotation.get('g')


def p_of(ann_entry, sk=None):
    """Stored p if the annotation carries one, else derived from the Slovak."""
    if ann_entry and isinstance(ann_entry, dict) and ann_entry.get('p_chain'):
        return ann_entry['p_chain']
    return derive_p(sk, ann_entry)


# ---------------------------------------------------------------- English side
EN_SUBJ = {'i': (1, 'sg'), 'we': (1, 'pl'), 'you': (2, None), 'he': (3, 'sg'), 'she': (3, 'sg'),
           'it': (3, 'sg'), 'they': (3, 'pl')}
SUBORD = {'that', 'which', 'who', 'whom', 'whose', 'when', 'while', 'before', 'after', 'until', 'till',
          'if', 'because', 'since', 'so', 'as', 'though', 'although', 'unless', 'and', 'but', 'or',
          'than', 'why', 'how', 'where', 'what', 'whether'}
# Only INFLECTED reporting forms: a bare 'say' / 'ask' / 'tell' is usually an imperative ("Say goodbye,
# and in an hour they will come back") and must not hide the main-clause subject that follows it.
REPORTING = {'said', 'says', 'asked', 'asks', 'told', 'tells', 'thought', 'thinks', 'knew', 'knows',
             'hoped', 'hopes', 'wished', 'wishes', 'heard', 'hears', 'believed', 'believes', 'noticed',
             'mentioned', 'replied', 'explained', 'wanted', 'wants', 'watched', 'watches', 'lets',
             'makes', 'feels'}
IMPERSONAL_FRAMES = ('they say', 'they said', 'they tell', 'they told', 'people say', 'people said',
                      'it is said', 'it was said', 'one says')
INDEF = {'everyone', 'everybody', 'someone', 'somebody', 'anyone', 'anybody', 'nobody', 'none', 'each',
         'either', 'neither', 'whoever', 'people', 'person', 'everything', 'anything', 'something'}
EN_RE = re.compile(r"[a-z]+")   # "they'll" -> they, ll


def main_subjects(answer):
    """-> [pronoun] that can be a MAIN-CLAUSE subject of `answer`.

    The answer is cut into segments at commas-free subordinators; inside a segment a pronoun counts only
    when it stands in the first 4 tokens.  Two exclusions keep correct answers safe:
      * once a reporting verb has occurred, no later pronoun counts — "The director said that they would
        film ..." has no main-clause pronoun subject, so the guard abstains;
      * the impersonal frame "they say / people say" does not make 'they' a subject — "Honey, they say he
        left the bowl" abstains."""
    toks = EN_RE.findall((answer or '').lower())
    low = ' '.join(toks)
    drop_they = any(f in low for f in IMPERSONAL_FRAMES)
    segs, cur = [], []
    for t in toks:
        if t in SUBORD:
            segs.append(cur)
            cur = []
        else:
            cur.append(t)
    segs.append(cur)
    out, seen_report = [], False
    for seg in segs:
        for t in seg[:4]:
            if t in REPORTING:
                break
            if t in EN_SUBJ:
                if not seen_report and not (t == 'they' and drop_they):
                    out.append(t)
                break
        if any(t in REPORTING for t in seg):
            seen_report = True
    return out


def licensed_subjects(p):
    return [s for s in ('i', 'we', 'you', 'he', 'she', 'it', 'they') if _clash(s, p) is None]


def _clash(pronoun, p):
    """-> 'person' / 'number' / None.  GENDER IS NEVER CHECKED: gender belongs to the g chain and to
    F4v2/F4v3; the p chain must not re-open a point the gender licence deliberately leaves open."""
    ep, en = EN_SUBJ[pronoun]
    if pronoun == 'you':
        return None
    if p.get('person') == 2 and pronoun in ('i', 'we'):
        return None                       # generic Slovak 2sg is often rendered 'I'/'we' — abstain
    if p.get('person') and ep and p['person'] != ep:
        return 'person'
    if p.get('number') and en and p['number'] != en:
        return 'number'
    return None


# ---------------------------------------------------------------- the prompt line
def p_prompt_line(p):
    """ONE line for the L3 prompt, to sit exactly where the gender line sits (before the ground-truth and
    wording lines).  Returns '' when there is no p chain."""
    if not p:
        return ''
    person, number, g = p.get('person'), p.get('number'), p.get('gender')
    if person == 3 and number == 'sg':
        if p.get('has_g'):
            return ('Person and number: the Slovak verb is third person singular — the subject is ONE '
                    'person (he or she). The gender licence above does NOT extend to person or number: a '
                    'plural subject (they, we) where the Slovak is singular, or a different person (I, we, '
                    'you), is DIFF.')
        # No g chain: the subject may be a thing or an animal ('terapia bude pokračovať'), so no pronoun
        # is named — only the number and the person are claimed.
        return ('Person and number: the Slovak verb is third person singular — its subject is one, not '
                'several. An answer that makes the subject plural (they, we) or changes the person '
                '(I, we) is DIFF.')
    if person == 3 and number == 'pl':
        return ('Person and number: the Slovak verb is third person plural — the subject is more than one '
                '(they). An answer with a singular subject (he, she, it) or a different person (I, we) is '
                'DIFF.')
    if person == 1:
        who = 'first person singular (I)' if number == 'sg' else 'first person plural (we)'
        return ('Person and number: the Slovak verb is %s. An answer with any other subject (he, she, it, '
                'they, %s) is DIFF.' % (who, 'we' if number == 'sg' else 'I'))
    if person == 2:
        return ('Person and number: the Slovak verb is second person — the subject is the addressee (you). '
                'An answer with a third-person subject (he, she, it, they) is DIFF.')
    if number == 'sg':
        return ('Number: the Slovak verb is singular — the subject is one. An answer with a plural subject '
                '(they, we) is DIFF.')
    if number == 'pl':
        return ('Number: the Slovak verb is plural — the subject is more than one. An answer with a '
                'singular subject (he, she, it) is DIFF.')
    if person == 3:
        return ('Person: the Slovak verb is third person. An answer whose subject is I, we or you is DIFF.')
    return ''


# ---------------------------------------------------------------- the F4p consultation
def f4p_guard(answer_en, p, annotation=None):
    """-> (reject, reason).  Fires ONLY when every main-clause subject pronoun of the answer contradicts
    the person or the number the Slovak fixes.  Never on 'you', never on noun subjects (no pronoun ->
    abstain), never on gender, never when p is None, never on an indefinite antecedent ('everyone ... they'
    is singular they -> abstain), never on I/we against a Slovak generic 2nd person."""
    if not p:
        return False, 'no p chain'
    if not (p.get('person') or p.get('number')):
        return False, 'p chain carries neither person nor number'
    subs = main_subjects(answer_en)
    if not subs:
        return False, 'no main-clause subject pronoun in the answer'
    clashes = [(s, _clash(s, p)) for s in subs]
    if any(c is None for _s, c in clashes):
        return False, 'a main-clause pronoun (%s) is compatible with the Slovak' % ','.join(
            s for s, c in clashes if c is None)
    low = set(EN_RE.findall((answer_en or '').lower()))
    if (low & INDEF) and all(s == 'they' for s, _c in clashes):
        return False, 'indefinite antecedent (%s) — singular "they" cannot be separated' % ','.join(
            sorted(low & INDEF))
    s0, c0 = clashes[0]
    return True, ('answer subject "%s" contradicts the Slovak %s (person %s, number %s; %s)'
                  % (s0, c0, p.get('person') or 'open', p.get('number') or 'open',
                     '; '.join(p.get('signals', [])[:3])))


def f4p_subject_mismatch(it, annotation=None):
    """guards_c-compatible adapter: (hit, trace) for one item dict with 'sk' and 'answer'."""
    p = derive_p(it.get('sk'), annotation)
    rej, reason = f4p_guard(it.get('answer'), p, annotation)
    return rej, {'fired': rej, 'guard': 'f4p', 'reason': reason, 'p': p,
                 'pronouns': main_subjects(it.get('answer'))}


# ---------------------------------------------------------------- annotation plumbing
def annotate(annotations, sentences, out_path=None):
    """Store the p chain next to `g`.  `annotations` is the loader's {sid(str): {hygienised, raw}} dict;
    `sentences` is the answer-free export (or any list of {sid, sk}).  Returns {sid(str): p|None} and
    writes it to `out_path` (default taskA/annotations_p_<side>.json) when given."""
    sk_of = {str(s['sid']): s['sk'] for s in sentences}
    out = {}
    for sid, sk in sk_of.items():
        entry = annotations.get(sid) or {}
        p = derive_p(sk, entry)
        out[sid] = p
        if isinstance(entry, dict):
            entry['p_chain'] = p
            if isinstance(entry.get('hygienised'), dict):
                entry['hygienised']['p_chain'] = p
            annotations[sid] = entry
    if out_path:
        json.dump(out, open(out_path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    return out


def _cli():
    side = 'dev'
    count_all = '--count-all' in sys.argv
    if '--side' in sys.argv:
        side = sys.argv[sys.argv.index('--side') + 1]
    sys.path.insert(0, P1J)
    from loader_1j import load_sentences, load_annotations
    if count_all:
        S = load_sentences('all', purpose='Task A p-chain COUNT ONLY over all 140 sentences')
        import collections
        c = collections.Counter()
        for s in S:
            p = derive_p(s['sk'], {'g': s.get('g')})
            key = 'chain' if p else 'ambiguous'
            c[(s.get('side', '?'), key)] += 1
            if p:
                c[(s.get('side', '?'), 'p=%s%s' % (p.get('person') or 'open', p.get('number') or 'open'))] += 1
        for k in sorted(c, key=str):
            print(k, c[k])
        print('TOTAL', len(S), 'with chain', sum(v for k, v in c.items() if k[1] == 'chain'))
        return
    S = load_sentences(side, purpose='Task A p-chain annotation (%s)' % side)
    A = load_annotations(side, purpose='Task A p-chain annotation (%s)' % side)
    out = os.path.join(HERE, 'annotations_p_%s.json' % side)
    res = annotate(A, S, out_path=out)
    print('%s: %d sentences, %d with a p chain, %d ambiguous -> %s'
          % (side, len(res), sum(1 for v in res.values() if v), sum(1 for v in res.values() if not v), out))


if __name__ == '__main__':
    _cli()
