#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F8v2 - AGENT DEMOTION guard (brief 1.1).  100% OFFLINE: no model, no API, no network, no DB.

Same public interface as f8 (the runner can swap the module by name):

    check(slovak, annotation, answer) -> {"verdict": reject|accept|abstain, "sk":…, "en":…, "reason":…}
    sk_agent(slovak, annotation=None)   (re-exported from f8, for callers that use it)
    en_passive(answer)                  (re-exported from f8)

New, for gold validation:

    sk_clauses(slovak, annotation=None) -> [{"i", "role", "agent": {...}|None, "text", "reason"}]
                                           agent None = abstain on that clause

RULE.  If a Slovak clause has a nominative AGENT, reject any answer in which that agent is not the
grammatical subject of the corresponding English clause:

  (1) passive verb group in that clause (main OR subordinate, with or without a by-phrase);
  (2) it-cleft / wh-cleft opening ("It was him who…", "What X did was…") that pushes the agent out
      of subject position;
  (3) reported-speech / perspective recast ("I was asked/told…", "It was said…", "It seems that…");
  (4) agent dropped - the agent's English equivalent replaced by someone / generic they / there /
      one in subject position.

DESIGN PRINCIPLE (inherited from F8/F9): assert LESS than the truth, never more.  A reject needs
POSITIVE evidence of demotion.  Everything uncertain abstains: Slovak impersonal / passive /
reflexive-passive / dative-experiencer / existential / imperative / copular / indefinite-subject
clauses, 3pl subjectless (Slovak impersonal "oznámili nám" = English "we were told"), unparseable
English, clause counts that do not line up.  A lexical mismatch of NOUNS is never a reject, and a
Slovak masculine/feminine pronoun rendered as English "it" is never a reject (inanimate gender).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f9   # noqa: E402
import f8   # noqa: E402  (v1: re-exported below, and optionally inherited)

# keep the v1 entry points available under the v2 module name
sk_agent = f8.sk_agent
en_passive = f8.en_passive

INHERIT_V1 = False      # True => also reject whenever v1 rejects (superset); measured in the eval

# --------------------------------------------------------------------------- Slovak side
PRON = dict(f8.PRON)                       # nominative pronouns -> (en, person, number, gender)
BYT_FIN = f8.BYT_PAST | f8.BYT_PRES | {'budem', 'budeš', 'bude', 'budeme', 'budete', 'budú', 'niet',
                                       'nebol', 'nebola', 'nebolo', 'neboli', 'nie', 'nebude',
                                       'nebudú', 'nebudem'}
PART_SUF = f8.PART_SUF
IMPERS_V = f8.IMPERS_V
DAT = ('mi', 'ti', 'mu', 'jej', 'nám', 'vám', 'im')
SPEECH = f8.SPEECH
SK_OBL_END = ('om', 'ou', 'mi', 'ch', 'ám', 'ami', 'ovi', 'em', 'ým')
# indefinite / negative pronouns: they may BE the subject, so never infer another agent -> abstain
INDEF = set("""niekto nikto niečo nič ktosi čosi hocikto ktokoľvek čokoľvek všetci všetko každý
každá každému nikoho niekoho ľudia""".split())
# masculine nouns that end like an l-participle ("terminál", "materiál")
L_NOUN_END = ('ál', 'él', 'ól', 'úl', 'ýl', 'íl')
# closed-class Slovak tokens: conjunctions, particles, adverbs, clitics, possessives,
# quantifiers.  They are never a nominative agent and never a finite verb.  General vocabulary,
# no sentence and no sid is special-cased.
STOP = set("""a i ale alebo lebo takze takže teda však vsak že ze aby nech ak keby kiežby kiezby keď
ked kým kym kedy hoci pretože pretoze zatiaľ zatial akonáhle akonahle či ci len iba už uz ešte este
aj ani tiež tiez práve prave asi možno mozno vraj snáď snad azda vôbec vobec nikdy vždy vzdy často
casto zvyčajne zvycajne obvykle dnes včera vcera zajtra teraz potom predtým predtym znova znovu opäť
opat zase stále stale ráno rano večer vecer poobede popoludní popoludni dopoludnia celkovo napokon
nakoniec konečne konecne hneď hned skoro takmer veľmi velmi úplne uplne celkom príliš prilis dosť
dost trochu tak takto tam tu sem ďalej dalej spolu rýchlo rychlo pomaly dlho krátko kratko medzitým
medzitym zrazu náhle nahle akurát akurat vlastne jednoducho naozaj skutočne skutocne určite urcite
samozrejme pravdepodobne žiaľ zial bohužiaľ bohuzial našťastie nastastie napriek kvôli kvoli
trikrát trikrat dvakrát dvakrat raz vyššie vyssie nižšie nizsie hore dole von dnu spať spat
jej jeho ich mu ho ma im nám nam vám vam mi ti si sa nás nas vás vas seba sebe sebou svoj svoja
svoje svojho svoju svojej svojim môj moj moja moje tvoj tvoja náš nas váš vas nie no
všetky vsetky všetci vsetci všetko vsetko veľa vela málo malo niekoľko niekolko každý kazdy každá
kazda každé kazde toto tento táto tato tieto títo tito taký taky taká taka také take tí ti""".split())
# auxiliaries/particles that may stand between the clause start and its finite verb
# copular / perception verbs: the surface noun is a state holder, not an agent -> abstain
STATE_V = set("""vyzerá vyzera vyzerajú vyzeraju vyzeral vyzerala vyzeralo zdá zda zdal zdala zdalo
zdajú zdaju pôsobí posobi ostáva ostava zostáva zostava ostal ostala zostal zostala""".split())


def _verbs(t):
    """[(index, token, 'lpart'|'pres')] - finite verb tokens of ONE clause, conservative."""
    out = []
    for i, w in enumerate(t):
        if i and t[i - 1] in f9.PREPS:
            continue
        if f9._is_l_part(t, i):
            if any(w.endswith(e) for e in L_NOUN_END):
                continue                                   # "terminál", "materiál": a noun
            out.append((i, w, 'lpart'))
        elif f9._looks_present(w):
            out.append((i, w, 'pres'))
    return out


def _pres_person(w):
    b = w[2:] if w.startswith('ne') and len(w) > 5 else w
    if b.endswith('me'):
        return (1, 'pl')
    if b.endswith('te'):
        return (2, 'pl')
    if b.endswith('š'):
        return (2, 'sg')
    if b.endswith('m'):
        return (1, 'sg')
    if b.endswith(('ajú', 'ujú', 'ejú', 'jú', 'ia', 'ú')):
        return (3, 'pl')
    return (3, 'sg')


def _lpart_person(t, w):
    """(person, number, gender) from the l-participle + auxiliary; None when ambiguous."""
    if 'si' in t:
        return None                       # 2sg auxiliary or reflexive particle: ambiguous -> abstain
    if 'som' in t:
        return (1, 'sg', None)
    if 'sme' in t:
        return (1, 'pl', None)
    if 'ste' in t:
        return (2, 'pl', None)
    if w.endswith('li'):
        return (3, 'pl', None)
    if w.endswith('la'):
        return (3, 'sg', 'f')
    if w.endswith('lo'):
        return (3, 'sg', 'n')
    if w.endswith('l'):
        return (3, 'sg', 'm')
    return None


def _en_of(person, number, gender):
    if person == 1:
        return 'i' if number == 'sg' else 'we'
    if person == 2:
        return 'you'
    if number == 'pl':
        return 'they'
    return {'m': 'he', 'f': 'she', 'n': 'it'}.get(gender)


def _noun_agent(t, vidx):
    """v1's heuristic, restricted to one clause and to the material BEFORE the first finite verb."""
    if 'sa' in t:
        return None
    for j in range(vidx - 1, -1, -1):
        x = t[j]
        if x in f9.PREPS:
            return None
        if x in f9.DET or x in ('si', 'už', 'ešte', 'nie', 'ktorý', 'ktorá', 'ktoré', 'ktorí'):
            continue
        if x in PRON:
            continue
        if len(x) > 2 and not any(x.endswith(e) for e in SK_OBL_END):
            return x
        return None
    return None


def _clause_agent(t):
    """-> (agent|None, reason).  agent = {'tok','kind','en','person','number','gender'}"""
    s = ' ' + ' '.join(t) + ' '
    # --- Slovak participial passive: byť + -ný/-tý
    for i, w in enumerate(t):
        if w in BYT_FIN:
            for j in (i + 1, i + 2, i - 1):
                if 0 <= j < len(t) and len(t[j]) > 4 and t[j].endswith(PART_SUF) and t[j] not in f9.DET:
                    return None, 'Slovak participial passive "%s %s" -> abstain' % (w, t[j])
    # --- impersonal verbs
    if 'podarilo' in t or 'podarí' in t or 'darí' in t or any(w in IMPERS_V for w in t):
        return None, 'subjectless / impersonal verb -> abstain'
    # --- dative experiencer
    for p in DAT:
        if (' bolo %s ' % p) in s or (' je %s ' % p) in s or (' bude %s ' % p) in s:
            return None, 'dative-experiencer construction -> abstain'
    # --- existential "na lavičke je …"
    if t and t[0] in f9.PREPS and ('je' in t or 'sú' in t or 'niet' in t or 'bolo' in t or 'boli' in t):
        return None, 'existential/locative "je/sú" clause -> abstain'
    verbs = _verbs(t)
    if not verbs:
        return None, 'no finite verb signal -> abstain'
    # --- copular byť-only clause ("On je unavený.", "Terminál bol prázdny.")
    if all(v[1] in BYT_FIN for v in verbs):
        return None, 'copular byť clause -> abstain'
    # --- explicit nominative pronoun (arm B states the subject)
    pron = None
    for i, w in enumerate(t):
        if w in PRON and not (i and t[i - 1] in f9.PREPS):
            pron = w
            break
    vidx, vtok, vkind = verbs[0]
    # --- indefinite / negative pronoun anywhere: it may be the subject -> abstain
    if pron is None and any(w in INDEF for w in t):
        return None, 'indefinite/negative pronoun subject ("%s") -> abstain' \
                     % next(w for w in t if w in INDEF)
    if pron is None:
        # --- reflexive passive / impersonal "sa"
        if 'sa' in t:
            if any(k == 'pres' and _pres_person(w)[0] == 3 for _i, w, k in verbs) \
               or any(k == 'lpart' and w.endswith('lo') for _i, w, k in verbs) \
               or any(w in SPEECH for w in t):
                return None, 'reflexive-passive / impersonal "sa" clause -> abstain'
        # --- imperative ("Zatvorte dvere.")
        if vidx == 0 and vkind == 'pres' and vtok.endswith(('te', 'ite', 'ajte')):
            return None, 'imperative clause -> abstain'
    if pron:
        en, p, n, g = PRON[pron]
        return ({'tok': pron, 'kind': 'pron', 'en': en, 'person': p, 'number': n, 'gender': g},
                'explicit nominative pronoun "%s"' % pron)
    noun = _noun_agent(t, vidx)
    if noun:
        return ({'tok': noun, 'kind': 'noun', 'en': None, 'person': 3, 'number': None, 'gender': None},
                'noun "%s" before the active verb "%s"' % (noun, vtok))
    # --- noun + copula ("terminál bol …") is not a pro-drop clause
    if len(verbs) > 1 and verbs[1][1] in BYT_FIN and verbs[1][0] == vidx + 1:
        return None, 'noun + copula, no agent asserted -> abstain'
    # --- pro-drop: person/number out of the verb morphology
    if vkind == 'lpart':
        pn = _lpart_person(t, vtok)
        if not pn:
            return None, 'l-participle person ambiguous -> abstain'
        p, n, g = pn
    else:
        p, n = _pres_person(vtok)
        g = None
    if p == 3 and n == 'pl':
        # subjectless 3pl is the Slovak IMPERSONAL ("oznámili nám" = "we were told")
        return None, 'subjectless 3pl (Slovak impersonal) -> abstain'
    en = _en_of(p, n, g)
    return ({'tok': vtok, 'kind': 'prodrop', 'en': en, 'person': p, 'number': n, 'gender': g},
            'pro-drop agent from "%s" (%s%s)' % (vtok, p, n))


def sk_clauses(slovak, annotation=None):
    out = []
    for i, c in enumerate(f9._clauses(slovak)):
        ag, why = _clause_agent(c['toks'])
        out.append({'i': i, 'role': 'sub' if c['is_sub'] else 'main', 'text': c['text'],
                    'marker': c['marker'], 'agent': ag, 'reason': why})
    return out


# --------------------------------------------------------------------------- English side
COORD = {'and', 'but', 'so', 'then', 'yet', 'or'}
MARK = set(f9.SUBCONJ) | set(f9.REL) | COORD | {'whether'}
GET = {'get', 'gets', 'got', 'getting', 'gotten'}
BE_FIN = {'is', 'are', 'was', 'were', 'am'}
BE_NONFIN = {'be', 'been', 'being'}
# what may license a non-finite "be/been/being" as a real passive auxiliary
BE_LIC = {'will', 'would', 'could', 'should', 'might', 'must', 'can', 'may', 'shall',
          'has', 'have', 'had', 'is', 'are', 'was', 'were', 'am', 'not'}
ADJ_PP = f8.ADJ_PP | {'supposed', 'located', 'based', 'covered', 'dressed', 'seated', 'gone',
                      'allowed', 'stuck', 'lost', 'deserted', 'empty'}
SUBJ_PRON = {'i', 'you', 'he', 'she', 'it', 'we', 'they', 'there', 'someone', 'somebody', 'anyone',
             'anybody', 'everyone', 'everybody', 'nobody', 'people', 'one'}
GENERIC_FULL = {'someone', 'somebody', 'anyone', 'anybody', 'nobody', 'there', 'they', 'one'}
GENERIC_STRICT = {'someone', 'somebody', 'anyone', 'anybody', 'nobody', 'there', 'one'}
GENERIC_NOUN = {'someone', 'somebody', 'anyone', 'anybody'}
SEEM_V = {'seems', 'seemed', 'appears', 'appeared', 'seem', 'appear'}
ADV_SKIP = set(f9.ADV_SKIP) | {'not', 'probably', 'really', 'then', 'even', 'often', 'usually'}


def _is_pp(w):
    return (w in f9.PP_ALL) or (w.endswith('ed') and len(w) > 3)


def _passive_idx(t):
    """finite passive verb group inside one clause; "'s"/"to be"/bare "being" never qualify."""
    for i, w in enumerate(t):
        if w not in BE_FIN and w not in BE_NONFIN and w not in GET:
            continue
        if w in BE_NONFIN:
            prev = ''
            for j in range(i - 1, -1, -1):
                if t[j] not in ADV_SKIP or t[j] == 'not':
                    prev = t[j]
                    break
            if prev not in BE_LIC:
                continue                    # "likes being chased", "to be chased" -> not asserted
        k = i + 1
        while k < len(t) and t[k] in ADV_SKIP:
            k += 1
        nxt = t[k] if k < len(t) else ''
        if nxt in ('being', 'been'):
            k2 = k + 1
            while k2 < len(t) and t[k2] in ADV_SKIP:
                k2 += 1
            nxt2 = t[k2] if k2 < len(t) else ''
            if _is_pp(nxt2) and nxt2 not in ADJ_PP:
                return i, '"%s %s %s"' % (w, nxt, nxt2)
            continue
        if nxt == 'going':
            continue
        if _is_pp(nxt) and nxt not in ADJ_PP:
            return i, '"%s %s"' % (w, nxt)
    return None, None


def _verb_idx(t):
    hits = f9._hits(t)
    if hits:
        return hits[0][0]
    for j in range(1, len(t)):
        v = t[j]
        if v in f9.FUNC or v == 's_amb' or v in MARK:
            continue
        if v in f9.AMBIG_V:
            return None
        if v in f9.BASE_V:
            return j
        if v.endswith('s') and not v.endswith('ss') and len(v) > 3 and v[:-1] not in f9.FUNC:
            return j
    return None


def _subject(pre):
    for w in reversed(pre):
        if w in SUBJ_PRON:
            return w
    for w in reversed(pre):
        if w.isalpha() and w not in f9.FUNC and w not in MARK and w != 's_amb':
            return w
    return None


def _segments(answer):
    """pieces of the answer + whether the piece started at a MID-clause cut (not a comma part)."""
    out = []
    for part in re.split(r'[,;:]', (answer or '')):
        t = f9._en_tokens(part)
        if not t:
            continue
        cuts = [0] + [i for i, w in enumerate(t) if i > 0 and w in MARK] + [len(t)]
        first = True
        for a, b in zip(cuts, cuts[1:]):
            if b > a:
                out.append({'toks': t[a:b], 'cut': not first})
                first = False
    return out


def _info(d):
    t = d['toks']
    pi, pr = _passive_idx(t)
    vi = pi if pi is not None else _verb_idx(t)
    return {'toks': t, 'cut': d['cut'], 'pi': pi, 'pr': pr, 'vi': vi}


def en_clauses(answer):
    """-> [{'i','role','marker','toks','passive','verb','vi','subject'}]; verbless pieces merge."""
    segs = [_info(d) for d in _segments(answer)]
    merged = []
    for d in segs:
        if d['vi'] is None and merged:
            merged[-1]['toks'] = merged[-1]['toks'] + d['toks']
            merged[-1].update(_info(merged[-1]))
            continue
        merged.append(dict(d))
    out, i = [], 0
    while i < len(merged):
        d = merged[i]
        if d['vi'] is None and i + 1 < len(merged):        # verbless FIRST piece joins the next one
            nxt = merged[i + 1]
            nxt['toks'] = d['toks'] + nxt['toks']
            nxt.update(_info(nxt))
            nxt['cut'] = d['cut']
            i += 1
            continue
        out.append(d)
        i += 1
    cls = []
    for k, d in enumerate(out):
        t = d['toks']
        marker = t[0] if t and t[0] in MARK else None
        if marker == 'that' and not d['cut']:
            marker = None            # part-initial "that furniture …" is a determiner, not a marker
        role = 'main' if (marker is None or marker in COORD) else 'sub'
        vi = d['vi']
        cls.append({'i': k, 'role': role, 'marker': marker, 'toks': t, 'vi': vi,
                    'passive': (d['pr'] if d['pi'] is not None else None),
                    'verb': (t[vi] if vi is not None else None),
                    'subject': (_subject(t[:vi]) if vi is not None else None)})
    return cls


def _cleft(cls, k, want):
    """demoting cleft?  An it-cleft whose relative clause still has the agent as subject is fine."""
    t = cls[k]['toks']
    if len(t) >= 2 and t[0] in ('it', 'this') and t[1] in BE_FIN:
        if k + 1 < len(cls) and cls[k + 1]['toks'] and cls[k + 1]['toks'][0] in ('who', 'that', 'which'):
            nsub = cls[k + 1]['subject']
            if want and nsub == want:
                return None                     # "It was on the bus that SHE lost her wallet."
            if nsub is None and cls[k + 1]['toks'][0] == 'who':
                return 'it-cleft with a subject relative ("%s %s … who")' % (t[0], t[1])
            if nsub is None:
                return None
            return 'it-cleft "%s %s … %s"' % (t[0], t[1], cls[k + 1]['toks'][0])
    if t and t[0] == 'what':
        for j, w in enumerate(t):
            if j >= 3 and w in BE_FIN:
                return 'wh-cleft "what … %s"' % w
    return None


def _ref_heads(annotation):
    """subject heads of the reference + variants (noun agents only; never used to reject)."""
    a = f9._ann(annotation) if isinstance(annotation, dict) else {}
    heads = set()
    refs = ([a.get('reference')] if a.get('reference') else []) + list(a.get('v') or [])
    for v in refs:
        if not isinstance(v, str):
            continue
        for c in en_clauses(v):
            if c['subject']:
                heads.add(c['subject'])
            break
    return heads


# --------------------------------------------------------------------------- pairing + verdict
def _pairs(skc, enc):
    out = []
    for role in ('main', 'sub'):
        s = [c for c in skc if c['role'] == role]
        e = [c for c in enc if c['role'] == role]
        if not s or not e or len(s) != len(e):
            continue
        out += list(zip(s, e))
    return out


def _judge_pair(sc, ec, enc, heads):
    ag = sc['agent']
    if ag is None:
        return 'abstain', 'SK %s clause: %s' % (sc['role'], sc['reason'])
    if ec['vi'] is None:
        return 'abstain', 'English clause not parseable ("%s") -> abstain' % ' '.join(ec['toks'][:6])
    want = ag.get('en')
    subj = ec.get('subject')
    tag = 'SK agent "%s" (%s%s)' % (ag['tok'], ag['kind'], '/' + want if want else '')
    # (2) cleft
    cl = _cleft(enc, ec['i'], want)
    if cl:
        return 'reject', '%s; the English clause is a %s - the agent is not its subject' % (tag, cl)
    # (1) passive verb group in the aligned clause (main OR subordinate)
    if ec['passive']:
        return 'reject', '%s; the aligned English clause is passive (%s) - the agent is demoted' \
                         % (tag, ec['passive'])
    if subj is None:
        return 'abstain', 'no English subject found -> abstain'
    # (3) perspective recast "it seems / it appears"
    if subj == 'it' and ec['verb'] in SEEM_V and want != 'it':
        return 'reject', '%s; the English recasts it as "it %s …" - the agent is not the subject' \
                         % (tag, ec['verb'])
    # (4) agent dropped / replaced by a generic subject
    gen = {'pron': GENERIC_FULL, 'prodrop': GENERIC_STRICT}.get(ag['kind'], GENERIC_NOUN)
    if subj in gen and subj != want:
        return 'reject', '%s; the English subject is the generic "%s" - the agent is gone' % (tag, subj)
    if want and subj == want:
        return 'accept', '%s is still the English subject' % tag
    if ag['kind'] == 'noun' and heads and subj in heads:
        return 'accept', '%s: the English subject "%s" is the reference subject' % (tag, subj)
    return 'accept', '%s: active English clause, subject "%s", no demotion evidence' % (tag, subj)


def check(slovak, annotation, answer):
    skc = sk_clauses(slovak, annotation)
    enc = en_clauses(answer)
    heads = _ref_heads(annotation)
    base = {'sk': sk_agent(slovak, annotation), 'en': en_passive(answer),
            'sk_clauses': [{'i': c['i'], 'role': c['role'], 'agent': c['agent'], 'reason': c['reason']}
                           for c in skc],
            'en_clauses': [{'i': c['i'], 'role': c['role'], 'subject': c['subject'],
                            'passive': c['passive'], 'verb': c['verb']} for c in enc]}
    if not enc:
        base.update(verdict='abstain', reason='empty / unparseable English -> abstain')
        return base
    decisions = [_judge_pair(sc, ec, enc, heads) for sc, ec in _pairs(skc, enc)]
    base['decisions'] = decisions
    for v, why in decisions:
        if v == 'reject':
            base.update(verdict='reject', reason=why)
            return base
    if INHERIT_V1:
        v1 = f8.check(slovak, annotation, answer)
        if v1.get('verdict') == 'reject':
            base.update(verdict='reject', reason='F8v1: ' + v1.get('reason', ''))
            return base
    for v, why in decisions:
        if v == 'accept':
            base.update(verdict='accept', reason=why)
            return base
    base.update(verdict='abstain',
                reason=(decisions[0][1] if decisions else 'no alignable clause pair -> abstain'))
    return base


# --------------------------------------------------------------------------- selftest
CASES = [
    # --- the Phase 1L false acceptance (reported-speech recast) and its faithful answer
    ("Spýtala sa ma, či ja ovládam ten program.",
     "I was asked whether I knew how to use that program.", {'reject'}),
    ("Spýtala sa ma, či ja ovládam ten program.",
     "She asked me whether I knew how to use that program.", {'accept'}),
    # --- (1) passive main clause
    ("Ona opravila bicykel.", "The bike was repaired by her.", {'reject'}),
    ("Ona opravila bicykel.", "The bike was repaired.", {'reject'}),
    ("Ona opravila bicykel.", "She repaired the bike.", {'accept'}),
    ("Ona číta knihu.", "The book is being read by her.", {'reject'}),
    ("Ty držíš pohár.", "The glass is held by you.", {'reject'}),
    ("Ja som napísal list.", "The letter was written.", {'reject'}),
    ("Ja som napísal list.", "I wrote the letter.", {'accept'}),
    ("Oni postavili dom.", "They built the house.", {'accept'}),
    ("Oni postavili dom.", "The house was built.", {'reject'}),
    ("Ona upratala kuchyňu.", "The kitchen got cleaned.", {'reject'}),
    ("My sme ten nábytok zložili za dve hodiny.", "That furniture was assembled by us in two hours.",
     {'reject'}),
    ("My sme ten nábytok zložili za dve hodiny.", "We assembled that furniture in two hours.",
     {'accept'}),
    # past=present ambiguous verb ("put") -> the English clause is not parseable with confidence
    ("My sme ten nábytok zložili za dve hodiny.", "We put that furniture together in two hours.",
     {'accept', 'abstain'}),
    # --- (1) passive SUBORDINATE clause (invisible to v1)
    ("On povedal, že ona upratala kuchyňu.", "He said that the kitchen was cleaned.", {'reject'}),
    ("On povedal, že ona upratala kuchyňu.", "He said that she cleaned the kitchen.", {'accept'}),
    # --- (2) clefts
    ("On natočil kuchyňu.", "It was him who filmed the kitchen.", {'reject'}),
    ("On natočil kuchyňu.", "What he did was film the kitchen.", {'reject'}),
    ("On natočil kuchyňu.", "He filmed the kitchen.", {'accept'}),
    ("Ona včera stratila peňaženku v autobuse.",
     "It was on the bus yesterday that she lost her wallet.", {'accept'}),   # agent still subject
    # --- (3) perspective recast
    ("On upratal kuchyňu.", "It seems that the kitchen is clean.", {'reject'}),
    ("Ona povedala pravdu.", "It was said to me.", {'reject'}),
    # --- (4) agent dropped
    ("Ona upratala kuchyňu.", "Someone cleaned the kitchen.", {'reject'}),
    ("Ona opravila bicykel.", "There was a repaired bike.", {'reject'}),
    ("Ona opravila bicykel.", "The woman repaired the bike.", {'accept'}),
    # --- abstain paths
    ("Hovorí sa, že je to ťažké.", "It is said that it is hard.", {'abstain'}),
    ("Jej prejav bol prepísaný dvakrát.", "Her speech was rewritten twice.", {'abstain'}),
    ("Dom bol postavený minulý rok.", "The house was built last year.", {'abstain'}),
    ("Podarilo sa jej vydržať nehybne.", "She managed to stay still.", {'abstain'}),
    ("Prší celý deň.", "It has been raining all day.", {'abstain'}),
    ("Na lavičke je jeden dlhý obväz.", "There is one long bandage on the bench.", {'abstain'}),
    ("Bolo mi zima.", "I was cold.", {'abstain'}),
    ("On je unavený.", "He is tired.", {'abstain'}),
    ("Terminál bol prázdny.", "The terminal was deserted.", {'abstain'}),
    ("Zatvorte dvere.", "The door should be closed.", {'abstain'}),
    # 3pl subjectless main clause abstains; only the subordinate pair (noun agent) is decided
    ("Oznámili nám, že letisko zatvoria.", "We were told that the airport will close.",
     {'abstain', 'accept'}),
    ("Nikto nemá rád, keď ho naháňajú.", "Nobody likes being chased.", {'abstain'}),
    ("Ona opravuje bicykel.", "Xyz qwe plonk.", {'abstain'}),
    # --- fronted adverbial must PASS
    ("Včera Peter napísal list.", "Yesterday Peter wrote the letter.", {'accept'}),
    ("Včera Peter napísal list.", "Yesterday the letter was written.", {'reject'}),
    ("Zajtra ona zavolá lekárovi.", "Tomorrow she will call the doctor.", {'accept'}),
    ("Ona si naniesla už tri vrstvy.", "She's already put on three coats.", {'accept'}),
]


def selftest(verbose=True):
    bad = []
    for sk, en, ok in CASES:
        r = check(sk, None, en)
        if r['verdict'] not in ok:
            bad.append((sk, en, r['verdict'], sorted(ok), r['reason']))
    print('F8v2 selftest: %d cases, %d failures' % (len(CASES), len(bad)))
    if verbose:
        for b in bad:
            print('  FAIL %-46s | %-46s -> %-8s want %s\n        %s' % (b[0][:46], b[1][:46], b[2], b[3], b[4]))
    return 1 if bad else 0


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    for s in sys.argv[1:]:
        print(s)
        for c in sk_clauses(s):
            print('   ', c['i'], c['role'], c['agent'], '|', c['reason'])
