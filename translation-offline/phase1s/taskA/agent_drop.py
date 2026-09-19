#!/usr/bin/env python3
"""Phase 1S Task A — rule AG: the DROPPED AGENT is a meaning omission (deterministic, 0 model calls).

Owner's ruling: an English passive is CORRECT when it keeps the agent ("is repaired by my father")
or when the Slovak itself names no agent. When the Slovak NAMES a nominative agent of an active
verb and the answer is an agentless passive that renders that agent nowhere, the answer drops a
meaning (type M) and is WRONG. AG therefore REJECTS exactly there and ABSTAINS everywhere else.

Inputs are SOURCE-SIDE only: the Slovak sentence, its phase1p annotation (voice_sk / agent_nom),
the sentence's writer_tags (nom_agent / agent), the reference and the answer. The writer's ITEM
tags (`agentless`, `by-passive`, ...) are LABELS of the measured set and are NEVER read here.
"""
import re

# ----------------------------------------------------------------- lexicons
BE = {'is', 'are', 'am', 'was', 'were', 'be', 'been', 'being', "'s", "'re", "'m",
      'get', 'gets', 'got', 'getting', 'gotten'}
SKIP = {'not', "n't", 'being', 'been', 'also', 'already', 'just', 'still', 'never', 'always',
        'usually', 'often', 'now', 'then', 'finally', 'completely', 'quickly', 'slowly',
        'carefully', 'quietly', 'recently', 'immediately', 'suddenly', 'probably', 'certainly',
        'all', 'both', 'only', 'even', 'generally', 'normally', 'regularly', 'rarely', 'seldom'}
ADJECTIVAL = {'tired', 'interested', 'bored', 'worried', 'excited', 'scared', 'pleased',
              'annoyed', 'confused', 'married', 'surprised', 'disappointed', 'satisfied',
              'used', 'supposed', 'gone', 'ready', 'closed', 'crowded', 'talented', 'located'}
IRREG_PP = {'taken', 'given', 'written', 'made', 'done', 'seen', 'found', 'sent', 'built', 'told',
            'sold', 'bought', 'brought', 'caught', 'taught', 'put', 'read', 'cut', 'held', 'kept',
            'left', 'lost', 'paid', 'met', 'set', 'shut', 'spent', 'won', 'worn', 'broken',
            'chosen', 'driven', 'eaten', 'forgotten', 'hidden', 'known', 'shown', 'spoken',
            'stolen', 'thrown', 'drawn', 'grown', 'heard', 'led', 'let', 'lit', 'said', 'sung',
            'sunk', 'understood', 'beaten', 'bitten', 'blown', 'drunk', 'fed', 'felt', 'fought',
            'frozen', 'hung', 'hurt', 'laid', 'meant', 'run', 'sat', 'slept', 'sought', 'sworn',
            'swept', 'torn', 'woken', 'repaired', 'delivered'}
FINITE = {'is', 'are', 'am', 'was', 'were', 'has', 'have', 'had', 'do', 'does', 'did', 'will',
          'shall', 'can', 'could', 'may', 'might', 'must', 'should', 'would', "'s", "'re", "'m",
          "'ll", "'ve", "'d", 'gets', 'get', 'got'}
DET_START = {'the', 'a', 'an', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her',
             'its', 'our', 'their', 'every', 'each', 'both', 'all', 'some', 'no', 'one', 'two',
             'three', 'several', 'many'}
SK_PRON = {'ja', 'ty', 'on', 'ona', 'ono', 'my', 'vy', 'oni', 'ony'}
EN_PRON = {'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}
PRON_EQ = {'ja': {'i', 'me'}, 'ty': {'you'}, 'on': {'he', 'him'}, 'ona': {'she', 'her'},
           'ono': {'it'}, 'my': {'we', 'us'}, 'vy': {'you'}, 'oni': {'they', 'them'},
           'ony': {'they', 'them'}}
# Slovak surface markers of a source that has NO nominative agent
SK_REFLEX = re.compile(r'(^|\s)(sa|si)(\s|[.,!?]|$)', re.I)


def toks(s):
    return re.findall(r"[A-Za-z']+", s or '')


def is_participle(w):
    lw = w.lower()
    if lw in ADJECTIVAL:
        return False
    return lw in IRREG_PP or (lw.endswith('ed') and len(lw) > 3)


def find_passive(answer):
    """(aux index, participle index, tokens) for a be/get-passive WITHOUT a by-agent, else None."""
    t = toks(answer)
    low = [w.lower() for w in t]
    for i, w in enumerate(low):
        if w not in BE:
            continue
        j = i + 1
        while j < len(low) and low[j] in SKIP:
            j += 1
        if j < len(low) and is_participle(low[j]):
            if 'by' in low[j + 1:]:
                return None                      # by-agent present -> not ours
            return i, j, t
    return None


def subject_tokens(text):
    """Everything before the first finite verb = the subject NP (same reading lever 1 uses)."""
    t = toks(text)
    low = [w.lower() for w in t]
    end = None
    for i, w in enumerate(low):
        if i == 0:
            continue
        if w in FINITE:
            end = i
            break
        if w.endswith('s') and len(w) > 3 and w not in DET_START and low[i - 1] not in DET_START:
            end = i
            break
        if (w.endswith('ed') and len(w) > 3) or w in {'went', 'made', 'took', 'saw', 'said',
                                                      'gave', 'found', 'sent', 'put', 'wrote',
                                                      'read', 'built', 'bought', 'brought',
                                                      'locks', 'repairs'}:
            end = i
            break
    if end is None or end == 0:
        return t[:1]
    return t[:end]


def slovak_agent(sk, ann, wtags):
    """(agent string, kind 'pronoun'/'noun'/None, source). Annotation first, Slovak surface second."""
    ann = ann or {}
    wtags = wtags or {}
    a = wtags.get('agent')
    src = 'writer_tags.agent'
    if not a:
        # Slovak-side heuristic: the first word, when it is capitalised mid-sentence-initial and the
        # clause carries no reflexive passive marker.
        ws = re.findall(r"[^\s.,!?;:]+", sk or '')
        if ws and not SK_REFLEX.search(sk or ''):
            a, src = ws[0], 'sk_heuristic_first_word'
    if not a:
        return None, None, 'none'
    kind = 'pronoun' if a.strip().lower() in SK_PRON else 'noun'
    return a.strip(), kind, src


def has_nominative_agent(ann, wtags):
    """(bool, reason). True only when the Slovak is ACTIVE with an explicit nominative agent."""
    ann = ann or {}
    wtags = wtags or {}
    voice = ann.get('voice_sk')
    if voice is not None and voice != 'active_agent':
        return False, 'the Slovak is not active with an explicit agent (voice_sk=%r)' % voice
    if ann.get('agent_nom') is False:
        return False, 'the annotation says the Slovak names no nominative agent'
    if wtags.get('nom_agent') is False:
        return False, 'writer_tags say the Slovak has no nominative subject'
    if voice is None and not (ann.get('agent_nom') or wtags.get('nom_agent')):
        return False, 'no annotation evidence of a nominative agent'
    if wtags.get('impersonal_or_passive') is True:
        return False, 'the Slovak source is impersonal or passive'
    return True, 'the Slovak is active with an explicit nominative agent'


def decide(sk, ann, wtags, answer, reference, variant='primary'):
    """variant 'primary' = any explicit nominative agent counts (pronouns included).
       variant 'noun'    = pronoun agents ABSTAIN."""
    out = {'fired': False, 'reason': None, 'agent': None, 'agent_kind': None,
           'agent_source': None, 'answer_is_agentless_passive': False,
           'agent_token_elsewhere_in_answer': False}
    hit = find_passive(answer)
    if hit is None:
        out['reason'] = 'the answer is not a marked passive without a by-agent'
        return out
    out['answer_is_agentless_passive'] = True
    ok, why = has_nominative_agent(ann, wtags)
    if not ok:
        out['reason'] = why
        return out
    agent, kind, src = slovak_agent(sk, ann, wtags)
    out.update({'agent': agent, 'agent_kind': kind, 'agent_source': src})
    if not agent:
        out['reason'] = 'no agent string could be read off the Slovak'
        return out
    if variant == 'noun' and kind == 'pronoun':
        out['reason'] = 'AG-noun variant: the Slovak agent is a pronoun'
        return out
    # (iii) is the agent otherwise rendered as the answer's subject?
    i, j, t = hit
    ans_subj = {w.lower() for w in t[:i]}
    ans_all = {w.lower() for w in t}
    cands = set()
    rs = subject_tokens(reference)
    if rs:
        cands.add(rs[-1].lower())
        for w in rs:
            if w.lower() in EN_PRON:
                cands.add(w.lower())
    al = agent.lower().split()
    if al:
        cands.add(al[-1])
        cands |= PRON_EQ.get(al[-1], set())
    cands = {c for c in cands if c and c not in DET_START}
    out['agent_token_elsewhere_in_answer'] = bool(cands & ans_all)
    if cands & ans_subj:
        out['reason'] = 'the agent is rendered as the answer\'s own subject (%s)' % (
            ', '.join(sorted(cands & ans_subj)))
        return out
    out['fired'] = True
    out['reason'] = 'agentless passive against a Slovak that names the agent: %s' % agent
    return out


# ----------------------------------------------------------------- pre-flight
SYN = [
    # name, sk, ann, wtags, answer, reference, expect_primary, expect_noun
    ('furniture example (owner)', 'Môj otec opravuje starý nábytok vo svojej dielni.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'môj otec'},
     'Old furniture is repaired.', 'My father repairs old furniture in his workshop.', True, True),
    ('by-passive keeps the agent', 'Môj otec opravuje starý nábytok vo svojej dielni.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'môj otec'},
     'Old furniture is repaired by my father.', 'My father repairs old furniture in his workshop.',
     False, False),
    ('active answer', 'Môj otec opravuje starý nábytok vo svojej dielni.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'môj otec'},
     'My father repairs old furniture in his workshop.',
     'My father repairs old furniture in his workshop.', False, False),
    ('Slovak reflexive passive, no agent', 'Nábytok sa opravuje v dielni.',
     {'voice_sk': 'reflexive_passive', 'agent_nom': False}, {'nom_agent': False, 'agent': None},
     'The furniture is repaired in the workshop.', 'The furniture is repaired in the workshop.',
     False, False),
    ('Slovak passive, no agent', 'Brána bola zamknutá.',
     {'voice_sk': 'passive', 'agent_nom': False}, {'nom_agent': False},
     'The gate was locked.', 'The gate was locked.', False, False),
    ('was/is + adjective is no passive', 'Marek každý večer zamyká bránu do záhrady.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'Marek'},
     'The garden gate is closed every evening.', 'Marek locks the garden gate every evening.',
     False, False),
    ('agent rendered as the answer subject', 'Marek každý večer zamyká bránu do záhrady.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'Marek'},
     'Marek is woken every evening.', 'Marek locks the garden gate every evening.', False, False),
    ('get-passive fires', 'Marek každý večer zamyká bránu do záhrady.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'Marek'},
     'The garden gate gets locked every evening.', 'Marek locks the garden gate every evening.',
     True, True),
    ('perfect passive fires', 'Marek už zamkol bránu.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'Marek'},
     'The gate has been locked.', 'Marek has locked the gate.', True, True),
    ('pronoun agent: primary fires, AG-noun abstains', 'On opravuje starý nábytok.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'On'},
     'Old furniture is repaired.', 'He repairs old furniture.', True, False),
    ('impersonal source', 'Hovorí sa, že brána je zamknutá.',
     {'voice_sk': 'impersonal', 'agent_nom': False}, {'nom_agent': False},
     'It is said that the gate is locked.', 'It is said that the gate is locked.', False, False),
    ('pronoun agent rendered in the answer subject', 'On opravuje starý nábytok.',
     {'voice_sk': 'active_agent', 'agent_nom': True}, {'nom_agent': True, 'agent': 'On'},
     'He is given old furniture.', 'He repairs old furniture.', False, False),
]


def preflight(verbose=True):
    ok = True
    lines = []
    for name, sk, ann, wt, ans, ref, ep, en in SYN:
        p = decide(sk, ann, wt, ans, ref, 'primary')['fired']
        n = decide(sk, ann, wt, ans, ref, 'noun')['fired']
        good = (p == ep and n == en)
        ok = ok and good
        lines.append('%-4s %-45s primary=%-5s (want %-5s)  noun=%-5s (want %-5s)'
                     % ('PASS' if good else 'FAIL', name, p, ep, n, en))
    if verbose:
        print('\n'.join(lines))
        print('PRE-FLIGHT %s: %d/%d synthetic rows' % ('PASS' if ok else 'FAIL',
                                                       sum(1 for l in lines if l.startswith('PASS')),
                                                       len(lines)))
    return ok, lines


if __name__ == '__main__':
    import sys
    sys.exit(0 if preflight()[0] else 1)
