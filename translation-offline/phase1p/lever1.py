#!/usr/bin/env python3
"""Phase 1P — LEVER 1: the agentless passive, accepted WITH A TIP by a deterministic rewrite.

Owner rule: a passive is acceptable, and a dropped meaning of type M is accepted with a tip; an
agentless passive is both. Today (1N) 6/22 judged-correct agentless items are accepted, 14 of the
16 rejections are a bare DIFF at L3 and 2 stop at F4v2, and no accept-with-tip path exists.

Design (unchanged from the task's preferred one):
  1. DETECT, by script: the ANSWER is an English be-passive with no by-agent, while the SLOVAK is
     active with an explicit nominative agent (annotation `voice_sk` == 'active_agent' /
     `agent_nom` true; arm B makes the subject explicit).
  2. REWRITE: insert "by <agent>" directly after the participle, the agent being the English
     subject NP of the MAIN reference, put in the object case.
  3. Send the REWRITTEN answer through the normal stack. by-passives are accepted at 93.98 %, and a
     wrong tense / verb / object is still caught, so the path does not depend on the model obeying
     a prompt line.
  4. Passes  -> ACCEPT with the tip "The Slovak names who did it: <agent>". This is NOT a
     TIP-rejection. Fails -> the unmodified stack decision stands.
  5. F4v2 FIX (the 2 items that stop there): F4v2 asks whether the ANSWER's subject pronoun
     contradicts a feature the SLOVAK fixes. In a passive the answer's subject is the PATIENT, not
     the Slovak's subject, so the guard's premise is false. When this lever fires, F4v2/F4 are
     suppressed for the rewritten record only. Nothing else is suppressed.

The SHADOW readout (what the stack says about the UNREWRITTEN answer) is recorded per item by the
runner, so the lever's gain and its FA cost can be read separately.
"""
import re

TIP_TMPL = 'The Slovak names who did it: %s'

BE = {'is', 'are', 'am', 'was', 'were', 'be', 'been', 'being', "'s", "'re", "'m"}
SKIP = {'not', "n't", 'being', 'been', 'also', 'already', 'just', 'still', 'never', 'always',
        'usually', 'often', 'now', 'then', 'finally', 'completely', 'quickly', 'slowly',
        'carefully', 'quietly', 'recently', 'immediately', 'suddenly', 'probably', 'certainly',
        'all', 'both', 'only', 'even', 'never'}
# clearly adjectival -ed forms: "she is tired" is not a passive
ADJECTIVAL = {'tired', 'interested', 'bored', 'worried', 'excited', 'scared', 'pleased',
              'annoyed', 'confused', 'married', 'surprised', 'disappointed', 'satisfied',
              'used', 'supposed', 'gone', 'ready', 'closed'}
IRREG_PP = {'taken', 'given', 'written', 'made', 'done', 'seen', 'found', 'sent', 'built', 'told',
            'sold', 'bought', 'brought', 'caught', 'taught', 'put', 'read', 'cut', 'held', 'kept',
            'left', 'lost', 'paid', 'met', 'set', 'shut', 'spent', 'won', 'worn', 'broken',
            'chosen', 'driven', 'eaten', 'forgotten', 'hidden', 'known', 'shown', 'spoken',
            'stolen', 'thrown', 'drawn', 'grown', 'heard', 'led', 'let', 'lit', 'said', 'sung',
            'sunk', 'understood', 'beaten', 'bitten', 'blown', 'drunk', 'fed', 'felt', 'fought',
            'frozen', 'hung', 'hurt', 'laid', 'meant', 'run', 'sat', 'slept', 'sought', 'sworn',
            'swept', 'torn', 'woken', 'worn', 'repaired', 'delivered'}
OBJ_CASE = {'i': 'me', 'he': 'him', 'she': 'her', 'we': 'us', 'they': 'them', 'who': 'whom',
            'you': 'you', 'it': 'it'}
FINITE = {'is', 'are', 'am', 'was', 'were', 'has', 'have', 'had', 'do', 'does', 'did', 'will',
          'shall', 'can', 'could', 'may', 'might', 'must', 'should', 'would', "'s", "'re", "'m",
          "'ll", "'ve", "'d", 'gets', 'get', 'got'}
DET_START = {'the', 'a', 'an', 'this', 'that', 'these', 'those', 'my', 'your', 'his', 'her',
             'its', 'our', 'their', 'every', 'each', 'both', 'all', 'some', 'no', 'one', 'two',
             'three', 'several', 'many'}


def _spans(s):
    return [(m.group(0), m.start(), m.end()) for m in re.finditer(r"[A-Za-z']+", s or '')]


def is_participle(w):
    lw = w.lower()
    if lw in ADJECTIVAL:
        return False
    return lw in IRREG_PP or (lw.endswith('ed') and len(lw) > 3)


def find_passive(answer):
    """(index of the participle span, span list) for a be-passive with no by-agent, else None."""
    sp = _spans(answer)
    low = [w.lower() for w, _a, _b in sp]
    for i, w in enumerate(low):
        if w not in BE:
            continue
        j = i + 1
        while j < len(low) and low[j] in SKIP:
            j += 1
        if j < len(low) and is_participle(low[j]):
            if 'by' in low[j + 1:]:
                return None                      # a by-agent (or any 'by') is present -> not ours
            return j, sp
    return None


def agent_of(reference):
    """The subject NP of the main reference: everything before its first finite verb."""
    sp = _spans(reference)
    if not sp:
        return None
    low = [w.lower() for w, _a, _b in sp]
    end = None
    for i, w in enumerate(low):
        if i == 0:
            continue
        if w in FINITE:
            end = i
            break
        if w.endswith('s') and len(w) > 3 and w not in DET_START and i >= 1 and low[i - 1] not in DET_START:
            end = i
            break
        if (w.endswith('ed') and len(w) > 3) or w in {'went', 'made', 'took', 'saw', 'said',
                                                      'gave', 'found', 'sent', 'put', 'wrote',
                                                      'read', 'built', 'bought', 'brought'}:
            end = i
            break
    if end is None or end == 0:
        return None
    words = [sp[k][0] for k in range(end)]
    if len(words) == 1 and words[0].lower() in OBJ_CASE:
        return OBJ_CASE[words[0].lower()]
    out = ' '.join(words)
    if out[:1].isupper() and (len(words) > 1 or words[0].lower() in DET_START) and words[0].lower() in DET_START:
        out = out[0].lower() + out[1:]
    return out or None


def detect(sk, ann, answer, reference):
    """The deterministic detector + rewrite. Returns a dict; 'fired' says whether lever 1 applies."""
    ann = ann or {}
    out = {'fired': False, 'agent': None, 'rewritten': None, 'tip': None, 'reason': None,
           'answer_is_agentless_passive': False}
    hit = find_passive(answer)
    if hit is None:
        out['reason'] = 'the answer is not a be-passive without a by-agent'
        return out
    out['answer_is_agentless_passive'] = True
    voice = ann.get('voice_sk')
    if not (voice == 'active_agent' or (voice is None and ann.get('agent_nom'))):
        out['reason'] = 'the Slovak is not active with an explicit agent (voice_sk=%r)' % voice
        return out
    if ann.get('agent_nom') is False:
        out['reason'] = 'the annotation says the Slovak names no nominative agent'
        return out
    agent = agent_of(reference)
    if not agent:
        out['reason'] = 'no subject NP could be read off the main reference'
        return out
    j, sp = hit
    _w, _a, b = sp[j]
    out.update({'fired': True, 'agent': agent,
                'rewritten': answer[:b] + ' by ' + agent + answer[b:],
                'tip': TIP_TMPL % agent, 'reason': 'agentless passive against an active Slovak'})
    return out
