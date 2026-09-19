#!/usr/bin/env python3
"""Phase 1T Task A - rule AG v3 (deterministic, 0 model calls, 0 network).

v3 = v2 + three independently switchable fixes:

  'clause'  CLAUSE-AWARE.  v2 inspected the sentence as one unit: it charged a passive in clause X
            with an agent that lives in clause Y, and it read the reference's MAIN-clause subject as
            "the agent rendered".  v3 splits the Slovak (commas), the answer and the reference
            (commas + subordinators/coordinators), matches answer clause -> reference clause (token
            overlap) -> Slovak clause (order, clamped) and applies the AG test PER CLAUSE.
  'subj'    SUBJECT-NP LOOKUP.  v2's subject reader broke on "the old newspapers were thrown"
            ('newspapers' was taken for a finite verb, so 'old' became the subject head) and on any
            multi-clause reference.  v3 reads the subject as the tokens before the FIRST unambiguous
            finite verb (auxiliary/modal/irregular past), and only then falls back to -ed / -s.
            The Slovak agent string is parsed properly: "ona (kolegyna)" -> {ona, kolegyna}, so the
            parenthesised pronoun reaches PRON_EQ and proper names reach the answer directly.
  'by'      INSTRUMENT != AGENT.  v2 treated ANY 'by' in the answer as a by-agent, so "by bike",
            "by the end of September", "by the end of the week" silenced the rule.  v3 reads the
            by-phrase's object: a by-phrase blocks AG only if its object can be the agent.

The module IMPORTS v2 rather than duplicating it, so decide(..., flags=()) is v2 bit for bit.
Inputs stay SOURCE-SIDE only (Slovak, phase1p annotation, writer_tags, reference, answer).  The
writers' ITEM tags ('agentless', 'by-passive', ...) are labels of the measured set and are NEVER read.
"""
import os
import re
import sys

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
sys.path.insert(0, os.path.join(BASE, "phase1s", "taskC"))

import agent_drop_v2 as V2                                                    # noqa: E402
from agent_drop_v2 import (ADJECTIVAL, BE, DET_START, EN_PRON, FINITE,        # noqa: E402,F401
                           IRREG_PP, PRON_EQ, SK_PRON, SK_REFLEX, SKIP,
                           is_participle, toks)

ALL_FLAGS = ("clause", "subj", "by")

# ----------------------------------------------------------------- new lexicons
# finite irregular PAST forms (v2 only knew participles) - used to find where a subject NP ends
IRREG_PAST = {
    'ate', 'awoke', 'became', 'began', 'bent', 'bet', 'bit', 'bled', 'blew', 'bore', 'bought',
    'bound', 'bred', 'broke', 'brought', 'built', 'burnt', 'burst', 'cast', 'caught', 'chose',
    'clung', 'came', 'cost', 'crept', 'cut', 'dealt', 'did', 'drank', 'drew', 'drove', 'dug',
    'dwelt', 'fed', 'fell', 'felt', 'fled', 'flew', 'flung', 'forbade', 'forgave', 'forgot',
    'fought', 'found', 'froze', 'gave', 'grew', 'ground', 'held', 'heard', 'hid', 'hit', 'hung',
    'hurt', 'kept', 'knelt', 'knew', 'laid', 'lay', 'leant', 'leapt', 'learnt', 'led', 'left',
    'lent', 'let', 'lit', 'lost', 'made', 'meant', 'met', 'mistook', 'mowed', 'overcame',
    'overtook', 'paid', 'put', 'quit', 'ran', 'rang', 'read', 'rebuilt', 'rode', 'rose', 'said',
    'sang', 'sank', 'sat', 'saw', 'sent', 'set', 'sewed', 'shed', 'shone', 'shook', 'shot',
    'showed', 'shrank', 'shut', 'slept', 'slid', 'slit', 'sold', 'sought', 'sowed', 'spat',
    'sped', 'spelt', 'spent', 'spilt', 'split', 'spoilt', 'spoke', 'spread', 'sprang', 'spun',
    'stank', 'stole', 'stood', 'struck', 'stuck', 'stung', 'swam', 'swept', 'swore', 'swung',
    'taught', 'tore', 'thought', 'threw', 'thrust', 'told', 'took', 'trod', 'underwent',
    'understood', 'undertook', 'upset', 'wept', 'went', 'withdrew', 'woke', 'won', 'wore',
    'wound', 'wrote'}

# by-phrase objects that can NEVER be the agent of the verb (instrument / means / time / manner)
BY_NONAGENT = {
    'bike', 'bicycle', 'car', 'bus', 'train', 'tram', 'metro', 'taxi', 'plane', 'boat', 'ship',
    'truck', 'foot', 'hand', 'email', 'mail', 'post', 'phone', 'telephone', 'fax', 'letter',
    'internet', 'card', 'cash', 'cheque', 'transfer', 'mistake', 'accident', 'chance', 'heart',
    'force', 'law', 'default', 'surprise', 'luck', 'road', 'rail', 'sea', 'air', 'then', 'now',
    'today', 'tomorrow', 'yesterday', 'time', 'times', 'end', 'start', 'beginning', 'deadline',
    'midnight', 'noon', 'morning', 'afternoon', 'evening', 'night', 'day', 'week', 'weekend',
    'month', 'year', 'hour', 'minute', 'second', 'half', 'quarter', 'percent', 'degrees',
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
    'october', 'november', 'december', 'spring', 'summer', 'autumn', 'winter', 'christmas',
    'easter', 'comparison', 'contrast', 'chance', 'nature', 'name', 'means', 'way'}
BY_KEEP = EN_PRON | {'her', 'his', 'their', 'its', 'my', 'your', 'our'}
BY_STOP = {'in', 'on', 'at', 'for', 'to', 'with', 'from', 'of', 'and', 'but', 'because', 'that',
           'when', 'while', 'as', 'before', 'after', 'until', 'since', 'so', 'than', 'which',
           'who', 'if', 'although', 'though'}

# English clause connectors.  'that' only after a verb; the rest only when a finite verb follows.
EN_CONN = {'that', 'which', 'who', 'because', 'since', 'although', 'though', 'while', 'when',
           'whenever', 'if', 'unless', 'until', 'till', 'after', 'before', 'and', 'but', 'so'}
EN_COORD = {'and', 'but', 'so'}
EN_FINITE = FINITE | IRREG_PAST | {'will', 'would', 'shall', 'should', 'can', 'could', 'may',
                                   'might', 'must', 'used', 'was', 'were', 'is', 'are', 'am',
                                   'has', 'have', 'had', 'does', 'do', 'did', 'be', 'been'}

# Slovak surface: byt' + passive participle = the clause is itself passive -> no nominative AGENT
SK_BYT = {'je', 'sú', 'som', 'sme', 'ste', 'bol', 'bola', 'bolo', 'boli', 'budem', 'budeš',
          'bude', 'budeme', 'budete', 'budú'}
SK_PPART = re.compile(r'(ný|ná|né|ní|tý|tá|té|tí|ných|nými|tých|tými)$', re.I)
SK_CONN = {'že', 'keď', 'keďže', 'lebo', 'pretože', 'hoci', 'kým', 'ak', 'aby', 'odkedy', 'akonáhle',
           'ktorý', 'ktorá', 'ktoré', 'ktorú', 'ktorí', 'ktorého', 'ktorým', 'a', 'ale', 'alebo',
           'takže', 'keby', 'napriek'}
EN_STRIP = {'that', 'which', 'who', 'because', 'since', 'although', 'though', 'while', 'when',
            'whenever', 'if', 'unless', 'until', 'till', 'after', 'before', 'and', 'but', 'so',
            'as', 'soon'}


# ----------------------------------------------------------------- fix 2: subject NP
def sk_toks(s):
    return re.findall(r"[^\s.,!?;:()\"]+", s or '')


def subject_np(text):
    """Tokens of the first subject NP: everything before the FIRST unambiguous finite verb.
    Only if there is none does the reader fall back to -ed / -s (v2 used the fallback first, which
    turned 'the old newspapers' into the verb 'newspapers')."""
    t = toks(strip_leading_conn(text))
    low = [w.lower() for w in t]
    if not t:
        return []
    end = None
    for i, w in enumerate(low):
        if i == 0:
            continue
        if w in EN_FINITE:
            end = i
            break
        # an -ed form is the finite verb unless a determiner sits in front of it ("the finished text")
        if (w.endswith('ed') and len(w) > 3 and w not in ADJECTIVAL
                and low[i - 1] not in DET_START):
            end = i
            break
    if end is None:                       # only now the -s rule (v2 ran it first: "the old
        for i, w in enumerate(low):       # newspapers were thrown" made 'newspapers' the verb)
            if i == 0:
                continue
            if w.endswith('s') and len(w) > 3 and w not in DET_START and low[i - 1] not in DET_START:
                end = i
                break
    if not end:
        return t[:1]
    return t[:end]


FRONT_ADV = {'tomorrow', 'today', 'yesterday', 'now', 'then', 'next', 'last', 'this', 'once',
             'later', 'soon', 'again', 'also', 'obviously', 'finally', 'recently', 'currently',
             'in', 'on', 'at', 'by', 'during', 'after', 'before', 'from', 'for', 'over', 'despite',
             'month', 'months', 'week', 'weeks', 'year', 'years', 'morning', 'afternoon', 'evening',
             'night', 'day', 'days', 'spring', 'summer', 'autumn', 'winter', 'monday', 'tuesday',
             'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'january', 'february',
             'march', 'april', 'june', 'july', 'august', 'september', 'october', 'november',
             'december', 'weather', 'bad', 'good'}


def strip_front_adv(tokens):
    """Drop a fronted adverbial so that the subject NP's head is the real head:
    'Tomorrow I' -> 'I';  'Next month a new branch' -> 'a new branch'."""
    k = 0
    while k < len(tokens) - 1 and tokens[k].lower() in FRONT_ADV:
        k += 1
    return tokens[k:] if k < len(tokens) else tokens


def strip_leading_conn(text):
    t = toks(text)
    k = 0
    while k < len(t) and t[k].lower() in EN_STRIP:
        k += 1
    return ' '.join(t[k:]) if k < len(t) else (text or '')


def parse_agent_tokens(agent):
    """'ona (zákazníčka)' -> (['ona','zákazníčka'], 'pronoun');  'Jana' -> (['Jana'],'noun')."""
    if not agent:
        return [], None
    parts = sk_toks(agent.replace('(', ' ').replace(')', ' '))
    parts = [p for p in parts if p not in {'/', '-'}]
    if not parts:
        return [], None
    kind = 'pronoun' if parts[0].lower() in SK_PRON else 'noun'
    return parts, kind


# ----------------------------------------------------------------- fix 3: by-phrase
def by_object(tokens, start):
    """content tokens of the by-phrase that starts at index `start` ('by')."""
    phrase = []
    for w in tokens[start + 1:start + 8]:
        lw = w.lower()
        if lw in BY_STOP:
            break
        phrase.append(lw)
    out = [w for w in phrase if w in BY_KEEP or (w not in DET_START and w not in {'a', 'an', 'the'})]
    # "by her" / "by them": the object IS a determiner-shaped pronoun - BY_KEEP keeps it
    return out or phrase


def by_is_agent(tokens, start, cands=None):
    """A by-phrase blocks AG only if its object CAN be the agent.
    - object renders the Slovak agent (PRON_EQ / reference subject head / proper name) -> agent
    - object is an instrument / means / time expression (BY_NONAGENT, or a number) -> NOT an agent
    - unknown object -> counted as an agent (conservative: AG abstains, costs nothing)."""
    obj = by_object(tokens, start)
    if not obj:
        return False, 'bare "by" with no object'
    if cands and (set(obj) & set(cands)):
        return True, 'by-agent renders the Slovak agent (%s)' % ', '.join(sorted(set(obj) & set(cands)))
    if all(o in BY_NONAGENT or o.isdigit() for o in obj):
        return False, 'the by-phrase is an instrument/time expression ("by %s")' % ' '.join(obj)
    return True, 'by-phrase with a possible agent ("by %s")' % ' '.join(obj)


def find_passive(answer, use_by_fix=False, cands=None):
    """(aux index, participle index, tokens) for a be/get-passive with no by-AGENT, else None."""
    if not use_by_fix:
        return V2.find_passive(answer)
    t = toks(answer)
    low = [w.lower() for w in t]
    for i, w in enumerate(low):
        if w not in BE:
            continue
        j = i + 1
        while j < len(low) and low[j] in SKIP:
            j += 1
        if j < len(low) and is_participle(low[j]):
            for b in range(j + 1, len(low)):
                if low[b] == 'by' and by_is_agent(t, b, cands)[0]:
                    return None
            return i, j, t
    return None


# ----------------------------------------------------------------- fix 1: clauses
def _has_finite(tokens):
    for w in tokens:
        lw = w.lower()
        if lw in EN_FINITE or (lw.endswith('ed') and len(lw) > 3 and lw not in ADJECTIVAL):
            return True
    return False


def _split_conn(segment):
    t = toks(segment)
    if not t:
        return []
    low = [w.lower() for w in t]
    cuts = []
    for i, w in enumerate(low):
        if i == 0 or w not in EN_CONN:
            continue
        rest = low[i + 1:]
        if not _has_finite(rest):
            continue
        if w == 'that':
            p, nx = low[i - 1], (low[i + 1] if i + 1 < len(low) else '')
            verbish = (p in EN_FINITE or (p.endswith('ed') and len(p) > 3) or
                       (p.endswith('s') and len(p) > 3 and p not in DET_START))
            if not (verbish or nx in DET_START or nx in EN_PRON or nx in EN_FINITE):
                continue                       # determiner 'that' ("for that presentation")
        if w in EN_COORD:
            k = 0
            for x in rest:
                if x in EN_FINITE:
                    break
                k += 1
            if k < 1 or (k < 2 and rest and rest[0] not in EN_PRON):
                continue                       # "bread and butter is ..." is one clause
        cuts.append(i)
    if not cuts:
        return [' '.join(t)]
    out, prev = [], 0
    for cidx in cuts + [len(t)]:
        if cidx > prev:
            out.append(' '.join(t[prev:cidx]))
        prev = cidx
    return [o for o in out if o.strip()]


def split_en(text):
    out = []
    for part in re.split(r'[,;:]', text or ''):
        out.extend(_split_conn(part))
    return [o for o in out if toks(o)]


def split_sk(sk):
    """Slovak clause split: commas (mandatory before Slovak subordinate clauses)."""
    return [p.strip() for p in re.split(r'[,;:]', sk or '') if p.strip()]


def sk_clause_is_passive(clause):
    t = [w.lower() for w in sk_toks(clause)]
    for i, w in enumerate(t):
        if w in SK_BYT:
            for x in t[i + 1:i + 4]:
                if len(x) >= 6 and SK_PPART.search(x):
                    return True
    return False


def sk_clause_has(clause, agent_tokens):
    low = {w.lower() for w in sk_toks(clause)}
    return any(a.lower() in low for a in agent_tokens)


def match_clause(ans_clause, ref_clauses, n_sk, idx, n_ans):
    """answer clause -> Slovak clause index. Order first; lexical anchors via the reference split."""
    if n_sk == n_ans:
        return min(idx, n_sk - 1), 'order'
    if ref_clauses and len(ref_clauses) == n_sk:
        a = {w.lower() for w in toks(ans_clause)}
        best, bidx = -1, None
        for k, rc in enumerate(ref_clauses):
            ov = len(a & {w.lower() for w in toks(rc)})
            if ov > best:
                best, bidx = ov, k
        if bidx is not None and best > 0:
            return bidx, 'ref-anchor(overlap=%d)' % best
    return min(idx, n_sk - 1), 'order-clamped'


def ref_clause_for(ans_clause, ref_clauses, idx):
    if not ref_clauses:
        return ''
    a = {w.lower() for w in toks(ans_clause)}
    best, bidx = -1, min(idx, len(ref_clauses) - 1)
    for k, rc in enumerate(ref_clauses):
        ov = len(a & {w.lower() for w in toks(rc)})
        if ov > best:
            best, bidx = ov, k
    return ref_clauses[bidx]


# ----------------------------------------------------------------- gates
def agent_gate(ann, wtags):
    """(ok, why, strict). strict = the agent must be OVERT in the very clause that is charged."""
    ann, wtags = ann or {}, wtags or {}
    voice = ann.get('voice_sk')
    if voice in ('passive', 'reflexive_passive'):
        return False, 'the Slovak is %s (voice_sk)' % voice, False
    if ann.get('agent_nom') is False:
        return False, 'the annotation says the Slovak names no nominative agent', False
    if wtags.get('nom_agent') is False:
        return False, 'writer_tags say the Slovak has no nominative subject', False
    if voice is None and not (ann.get('agent_nom') or wtags.get('nom_agent')):
        return False, 'no annotation evidence of a nominative agent', False
    strict = (voice == 'impersonal') or (wtags.get('impersonal_or_passive') is True)
    return True, 'the Slovak names a nominative agent', strict


def v2_candidates(agent, reference):
    """v2's own candidate set (last token of the agent + PRON_EQ + last token of the reference
    subject as v2 read it) - used when the 'subj' fix is switched OFF."""
    c = set()
    rs = V2.subject_tokens(reference)
    if rs:
        c.add(rs[-1].lower())
        for w in rs:
            if w.lower() in EN_PRON:
                c.add(w.lower())
    al = (agent or '').lower().split()
    if al:
        c.add(al[-1])
        c |= PRON_EQ.get(al[-1], set())
    return {x for x in c if x and x not in DET_START}


def pron_forms(agent_tokens):
    """English forms of a Slovak pronoun agent, INCLUDING 'her'/'his' - they are in DET_START, so
    candidates() drops them (a possessive 'her paper' is no agent), but "by her" IS the agent."""
    c = set()
    for a in agent_tokens or []:
        c |= PRON_EQ.get(a.lower(), set())
    return c


def candidates(agent_tokens, ref_clause, use_subj):
    c = set()
    for a in agent_tokens:
        la = a.lower()
        c |= PRON_EQ.get(la, set())
        if a[:1].isupper() and la not in SK_PRON:
            c.add(la)                                   # proper name, same form in English
    rs = strip_front_adv(subject_np(ref_clause)) if use_subj else V2.subject_tokens(ref_clause)
    if rs:
        c.add(rs[-1].lower())                           # the subject NP's head
        for w in rs:
            if w.lower() in EN_PRON:
                c.add(w.lower())
    return {x for x in c if x and x not in DET_START}


# ----------------------------------------------------------------- the rule
def decide(sk, ann, wtags, answer, reference, variant='primary', flags=ALL_FLAGS):
    flags = tuple(flags or ())
    if 'clause' not in flags:
        return _decide_flat(sk, ann, wtags, answer, reference, variant, flags)
    return _decide_clauses(sk, ann, wtags, answer, reference, variant, flags)


def _decide_flat(sk, ann, wtags, answer, reference, variant, flags):
    """v2, optionally with the 'by' fix and/or the 'subj' fix (no clause split)."""
    if not flags:
        return V2.decide(sk, ann, wtags, answer, reference, variant)
    out = {'fired': False, 'reason': None, 'agent': None, 'agent_kind': None, 'agent_source': None,
           'answer_is_agentless_passive': False, 'agent_token_elsewhere_in_answer': False,
           'clause': None, 'flags': list(flags)}
    agent, kind0, src = V2.slovak_agent(sk, ann, wtags)
    atoks, kind = parse_agent_tokens(agent) if 'subj' in flags else ([agent] if agent else [], kind0)
    kind = kind or kind0
    cands0 = (candidates(atoks, reference, True) if 'subj' in flags
              else v2_candidates(agent, reference))
    hit = find_passive(answer, 'by' in flags, cands0 | pron_forms(atoks))
    if hit is None:
        out['reason'] = 'the answer is not a marked passive without a by-agent'
        return out
    out['answer_is_agentless_passive'] = True
    ok, why, strict = agent_gate(ann, wtags) if 'subj' in flags else V2.has_nominative_agent(ann, wtags) + (False,)
    if not ok:
        out['reason'] = why
        return out
    out.update({'agent': agent, 'agent_kind': kind, 'agent_source': src})
    if not agent:
        out['reason'] = 'no agent string could be read off the Slovak'
        return out
    if variant == 'noun' and kind == 'pronoun':
        out['reason'] = 'AG-noun variant: the Slovak agent is a pronoun'
        return out
    i, j, t = hit
    ans_subj = {w.lower() for w in t[:i]}
    cands = cands0 or (candidates(atoks, reference, True) if 'subj' in flags
                       else v2_candidates(agent, reference))
    out['agent_token_elsewhere_in_answer'] = bool(cands & {w.lower() for w in t})
    if cands & ans_subj:
        out['reason'] = "the agent is rendered as the answer's own subject (%s)" % (
            ', '.join(sorted(cands & ans_subj)))
        return out
    out['fired'] = True
    out['reason'] = 'agentless passive against a Slovak that names the agent: %s' % agent
    return out


def _decide_clauses(sk, ann, wtags, answer, reference, variant, flags):
    use_subj, use_by = 'subj' in flags, 'by' in flags
    out = {'fired': False, 'reason': None, 'agent': None, 'agent_kind': None, 'agent_source': None,
           'answer_is_agentless_passive': False, 'agent_token_elsewhere_in_answer': False,
           'clause': None, 'flags': list(flags)}
    agent, kind0, src = V2.slovak_agent(sk, ann, wtags)
    # the agent string is always tokenised here: the clause machinery has to LOCATE the agent in a
    # Slovak clause.  What the 'subj' flag switches is the CANDIDATE set (v2 reader vs v3 reader).
    atoks, kind = parse_agent_tokens(agent)
    kind = kind or kind0
    out.update({'agent': agent, 'agent_kind': kind, 'agent_source': src})
    skc, ansc, refc = split_sk(sk), split_en(answer), split_en(reference)
    if not skc or not ansc:
        out['reason'] = 'no clause could be read'
        return out
    ok, why, strict = agent_gate(ann, wtags)
    reasons = []
    # v2's whole-answer by-agent abstain, kept: clause-awareness must not charge an answer that
    # names the agent in a by-phrase ANYWHERE ("If the instructions had been read by Lucia, the
    # whole spreadsheet would not have been ruined." keeps Lucia for both clauses).
    cands_all = pron_forms(atoks)
    for rc in (refc or [reference or '']):
        cands_all |= candidates(atoks, rc, use_subj)
    at = toks(answer)
    for b, w in enumerate(at):
        if w.lower() == 'by' and set(by_object(at, b)) & cands_all:
            out['reason'] = ('the agent is kept in a by-phrase of the answer ("by %s")'
                             % ' '.join(by_object(at, b)))
            return out
    for idx, ac in enumerate(ansc):
        rc = ref_clause_for(ac, refc, idx)
        cands = candidates(atoks, rc, use_subj) if atoks else set()
        hit = find_passive(ac, use_by, cands | pron_forms(atoks))
        if hit is None:
            continue
        out['answer_is_agentless_passive'] = True
        if not ok:
            reasons.append('c%d: %s' % (idx, why))
            continue
        if not agent:
            reasons.append('c%d: no agent string could be read off the Slovak' % idx)
            continue
        if variant == 'noun' and kind == 'pronoun':
            reasons.append('c%d: AG-noun variant: the Slovak agent is a pronoun' % idx)
            continue
        si, how = match_clause(ac, refc, len(skc), idx, len(ansc))
        skcl = skc[si]
        if sk_clause_is_passive(skcl):
            reasons.append('c%d: the Slovak counterpart clause is itself passive' % idx)
            continue
        overt = sk_clause_has(skcl, atoks)
        inherited = False
        if not overt:
            # v2's reflexive abstain path, now clause-scoped: it only speaks when the clause has no
            # overt agent of its own ("On si cisti topanky" is reflexive but names its agent).
            if SK_REFLEX.search(skcl):
                reasons.append('c%d: the Slovak counterpart clause is reflexive (sa/si)' % idx)
                continue
            if strict:
                reasons.append('c%d: impersonal/passive source and the agent is not overt in the '
                               'counterpart clause' % idx)
                continue
            if any(sk_clause_has(skc[k], atoks) for k in range(si)):
                inherited = True                     # pro-drop: antecedent in a PRECEDING clause
            else:
                reasons.append('c%d: the Slovak counterpart clause has no overt agent and none '
                               'precedes it (subjectless / 3pl pro-drop)' % idx)
                continue
        i, j, t = hit
        ans_subj = {w.lower() for w in t[:i]}
        out['agent_token_elsewhere_in_answer'] = bool(cands & {w.lower() for w in t})
        if cands & ans_subj:
            reasons.append("c%d: the agent is rendered as that clause's own subject (%s)"
                           % (idx, ', '.join(sorted(cands & ans_subj))))
            continue
        out['fired'] = True
        out['clause'] = {'idx': idx, 'answer_clause': ac, 'sk_clause': skcl, 'ref_clause': rc,
                         'match': how, 'agent_overt_in_clause': overt, 'agent_inherited': inherited,
                         'candidates': sorted(cands)}
        out['reason'] = ('agentless passive in clause %d against the Slovak clause %r that names '
                         'the agent: %s%s' % (idx, skcl, agent, ' (inherited)' if inherited else ''))
        return out
    if not out['answer_is_agentless_passive']:
        out['reason'] = 'the answer is not a marked passive without a by-agent'
    else:
        out['reason'] = '; '.join(reasons) or 'no clause qualifies'
    return out


if __name__ == '__main__':
    import preflight_v3
    sys.exit(0 if preflight_v3.main() else 1)
