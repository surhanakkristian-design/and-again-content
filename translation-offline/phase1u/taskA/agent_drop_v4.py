#!/usr/bin/env python3
"""Phase 1U Task A - rule AG v4 (deterministic, 0 model calls, 0 network, no DB).

v4 = v3 (clause+subj+by, always on) + four independently switchable fixes:

  'union'   UNION of verdicts.  v3's PER-CLAUSE verdict REPLACED v2's whole-sentence verdict and
            so lost 15 catches v2 had.  v4 ORs them: the flat (whole-sentence) verdict of the v2
            machinery with the subj/by fixes is taken when the clause path abstained for a reason
            that is NOT a principled clause-level abstain ("the counterpart clause has no overt
            agent and none precedes it" / "is itself passive" / "is reflexive" / impersonal).
            Those three reasons are the ones the clause fix was BUILT to produce, and a flat
            verdict contradicting them is exactly the measured cost v3 removed.
  'unionx'  the same union WITHOUT that guard (raw v2-OR-v3).  Measured, not selected.
  'lex'     LEXICON.  (a) an ADJECTIVAL-listed participle (closed, used, locked, ...) counts as a
            real participle when the Slovak clause is ACTIVE with an overt nominative agent AND the
            English auxiliary is not a bare present 'is/are/am' - "The shop WAS closed at six" /
            "will be closed" / "gets closed" / "has been closed" are eventive passives, while "The
            garden gate IS closed every evening" stays the stative reading the 1S/1T pre-flight
            row asserts (that row's Slovak is an active transitive too, so the tense is the only
            deterministic discriminator available; W:180047 'the windows are always closed' and
            W:180090:w3 'the landfill is closed' are knowingly left uncaught by it).
            (b) re-/over-/under-/un-/mis-/pre- prefixed irregular participles are generated from
            the base irregular list (rewritten, redone, rebuilt, overthrown, undone, retold,
            resold, rewound, overtaken, ...).
            (c) a reduced passive relative ("a newspaper criticised for ...") is caught by its own
            pass, guarded by the reference having a finite relative clause with an overt
            non-pronoun subject that the answer never renders.
            (d) a LOCATIVE by-phrase (by the lake / river / door ...) no longer blocks AG - only an
            AGENT by-phrase does (instrument / means / time were already handled by v3's 'by').
  'align'   CLAUSE MATCHER, class B.  v3 let ANY reference clause's subject count as "the agent is
            rendered as that clause's own subject".  v4 admits the reference-clause subject as a
            candidate only if the Slovak clause aligned to that answer clause actually contains the
            agent (or no Slovak clause does).  Fixes "The present that my sister chose ... was
            wrapped", where 'sister' was read as rendering 'predavacka'.
  'local'   CLAUSE MATCHER, class A.  The phase1p annotation names the MAIN clause's agent, so a
            fronted subordinate clause with its OWN overt agent ("Ked starosta otvori ...") looked
            agentless to v3.  v4 reads the clause-local agent off the ALIGNED REFERENCE clause's
            subject and fires when the answer clause renders that clause as an agentless passive.
            Guards: equal clause counts, the Slovak clause active and non-reflexive, the reference
            clause active, and - for a PRONOUN reference subject - an overt Slovak pronoun in that
            clause (this keeps Slovak pro-drop / 3pl impersonal clauses, whose reference reads
            "Since THEY introduced the new system", out of the rule).

Public interface is v3's:  decide(sk, ann, wtags, answer, reference, variant='primary',
flags=ALL_FLAGS).  flags=() reproduces AG v3 (clause+subj+by) BIT FOR BIT - v4 never changes the
v3 code path, it only wraps it.  Inputs stay SOURCE-SIDE only (Slovak, phase1p annotation,
writer_tags, reference, answer); item tags of the measured set are never read.
"""
import os
import sys

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
sys.path.insert(0, os.path.join(BASE, "phase1t", "taskA"))
sys.path.insert(0, os.path.join(BASE, "phase1s", "taskC"))

import agent_drop_v3 as V3                                                     # noqa: E402
from agent_drop_v3 import V2                                                   # noqa: E402
from agent_drop_v2 import (ADJECTIVAL, BE, DET_START, EN_PRON, FINITE,         # noqa: E402,F401
                           IRREG_PP, PRON_EQ, SK_PRON, SK_REFLEX, SKIP, toks)

V3_BASE = ("clause", "subj", "by")
FLAG_NAMES = ("union", "unionx", "lex", "align", "local")
ALL_FLAGS = ("union", "lex", "align", "local")          # v4 default (see AG_V4_REGRESSION.md)

# ------------------------------------------------------------------ 2.2 lexicon
PROMOTABLE = {'closed', 'used', 'located', 'crowded', 'married', 'locked'}
PRESENT_BE = {'is', 'are', 'am', "'s", "'re", "'m"}

_PREFIXES = ('re', 'over', 'under', 'un', 'mis', 'pre')
_BLOCK = {'overcast', 'upset', 'output', 'offset', 'preset', 'undercut'}
IRREG_PP_V4 = set(IRREG_PP) | {p + b for p in _PREFIXES for b in IRREG_PP
                               if len(b) > 2 and (p + b) not in _BLOCK}
IRREG_PP_V4 |= {'understood', 'undertaken', 'undergone', 'overcome', 'overtaken', 'overthrown',
                'rewritten', 'overwritten', 'underwritten', 'redone', 'undone', 'rebuilt',
                'retold', 'resold', 'rewound', 'reread', 'mistaken', 'misled'}

BY_LOCATIVE = {'lake', 'river', 'sea', 'shore', 'beach', 'door', 'doors', 'window', 'windows',
               'road', 'roadside', 'wall', 'bridge', 'gate', 'fire', 'fireplace', 'pool',
               'entrance', 'corner', 'church', 'castle', 'park', 'tree', 'trees', 'fountain',
               'station', 'harbour', 'harbor', 'pond', 'stream', 'hedge', 'fence', 'stage',
               'water', 'waterfall', 'bank', 'shoreline', 'coast', 'garden', 'terrace'}

REL_PREP = {'for', 'by', 'with', 'in', 'on', 'at', 'from', 'during', 'over', 'about', 'after'}
REL_PRON = {'that', 'which', 'who', 'whom'}
USE_REDUCED_RELATIVE = True
PRON_GROUPS = [{'i', 'me'}, {'you'}, {'he', 'him'}, {'she', 'her'}, {'it'}, {'we', 'us'},
               {'they', 'them'}]


def _pron_group(h):
    for g in PRON_GROUPS:
        if h in g:
            return g
    return {h}


def _renders(alow, forms):
    """Does this token list render one of these agent forms?"""
    return any(a == f or (len(f) >= 4 and a.startswith(f)) for a in alow for f in forms)


def _has_finite_v4(low):
    for i, w in enumerate(low):
        if w in V3.EN_FINITE:
            return True
        if w.endswith('ed') and len(w) > 3 and w not in ADJECTIVAL:
            return True
        if (w.endswith('s') and len(w) > 3 and w not in DET_START
                and (i == 0 or low[i - 1] not in DET_START)):
            return True
    return False


class _Patch(object):
    """Temporarily rebind module globals (deterministic, restored in finally)."""

    def __init__(self, binds):
        self.binds, self.saved = binds, []

    def __enter__(self):
        for mod, name, val in self.binds:
            self.saved.append((mod, name, getattr(mod, name)))
            setattr(mod, name, val)
        return self

    def __exit__(self, *a):
        for mod, name, val in reversed(self.saved):
            setattr(mod, name, val)
        return False


def _make_is_participle(promote):
    def is_participle(w):
        lw = w.lower()
        if lw in ADJECTIVAL and not (promote and lw in PROMOTABLE):
            return False
        return lw in IRREG_PP_V4 or (lw.endswith('ed') and len(lw) > 3)
    return is_participle


def _make_find_passive(orig):
    """Reject a hit that is only a promoted ADJECTIVAL participle under a bare PRESENT be
    ("the gate is closed every evening" = stative)."""
    def find_passive(answer, use_by_fix=False, cands=None):
        hit = orig(answer, use_by_fix, cands)
        if hit is None:
            return None
        i, j, t = hit
        if t[j].lower() in ADJECTIVAL and t[i].lower() in PRESENT_BE:
            return None
        return hit
    return find_passive


def _lex_patch(ann, wtags):
    promote = V3.agent_gate(ann, wtags)[0]
    is_part = _make_is_participle(promote)
    return _Patch([(V2, 'is_participle', is_part), (V3, 'is_participle', is_part),
                   (V3, 'BY_NONAGENT', set(V3.BY_NONAGENT) | BY_LOCATIVE),
                   (V3, 'find_passive', _make_find_passive(V3.find_passive))])


def _reduced_relative(sk, ann, wtags, answer, reference, variant):
    """(c) "She writes commentaries for a newspaper criticised for shallow headlines."
    Fires only if the REFERENCE renders that relative clause with a finite verb and an overt
    non-pronoun subject which the answer never mentions."""
    if not (USE_REDUCED_RELATIVE and V3.agent_gate(ann, wtags)[0]):
        return None
    t = toks(answer)
    low = [w.lower() for w in t]
    is_part = _make_is_participle(True)
    for j, w in enumerate(low):
        if j < 2 or not is_part(w):
            continue
        prev = low[j - 1]
        if (prev in BE or prev in SKIP or prev in FINITE or prev in V3.EN_FINITE
                or prev in DET_START or prev in EN_PRON):
            continue
        if low[j - 2] not in DET_START:
            continue
        if (low[j + 1] if j + 1 < len(low) else '') not in REL_PREP:
            continue
        if not _has_finite_v4(low[:j - 1]):
            continue
        if any(low[b] == 'by' and V3.by_is_agent(t, b, None)[0] for b in range(j + 1, len(low))):
            continue
        rt = toks(reference)
        rlow = [x.lower() for x in rt]
        for k, rw in enumerate(rlow):
            if rw not in REL_PRON or k + 1 >= len(rt):
                continue
            rc = ' '.join(rt[k + 1:])
            rs = V3.strip_front_adv(V3.subject_np(rc))
            if not rs:
                continue
            # the relative clause's subject: its first token unless a determiner opens the NP
            head = (rt[k + 1] if rt[k + 1].lower() not in DET_START else rs[-1]).lower()
            if head in EN_PRON or head in DET_START or head in REL_PRON or len(head) < 3:
                continue
            if _renders(low, {head}):
                continue
            return {'fired': True, 'agent': head, 'agent_kind': 'relative-clause',
                    'agent_source': 'ref', 'answer_is_agentless_passive': True,
                    'agent_token_elsewhere_in_answer': False,
                    'clause': {'reduced_relative': ' '.join(t[j - 2:j + 2]), 'ref_clause': rc},
                    'reason': ('LEX/reduced-relative: %r renders the reference relative clause %r '
                               'without its agent (%s)' % (' '.join(t[j - 2:j + 2]), rc, head))}
    return None


# ------------------------------------------------------------------ 2.3 align (class B)
def _align_patch(sk, ann, wtags, answer, reference):
    agent = V2.slovak_agent(sk, ann, wtags)[0]
    atoks = V3.parse_agent_tokens(agent)[0]
    skc, ansc = V3.split_sk(sk), V3.split_en(answer)
    orig = V3.ref_clause_for

    def ref_clause_for(ac, refc, idx):
        rc = orig(ac, refc, idx)
        if not atoks or not skc or not refc:
            return rc
        si = V3.match_clause(ac, refc, len(skc), idx, len(ansc))[0]
        if V3.sk_clause_has(skc[si], atoks):
            return rc
        if any(V3.sk_clause_has(c, atoks) for c in skc):
            return ''            # the agent lives in ANOTHER Slovak clause: this clause's subject
        return rc                # cannot be "the agent rendered"
    return _Patch([(V3, 'ref_clause_for', ref_clause_for)])


# ------------------------------------------------------------------ 2.3 local agent (class A)
CLAUSE_ABSTAIN = ('has no overt agent and none precedes', 'is itself passive',
                  'is reflexive', 'impersonal/passive source')


def _local_agent(sk, ann, wtags, answer, reference, variant):
    """Fire on an answer clause that renders an ACTIVE Slovak clause with its OWN overt agent (the
    one the annotation does not name, e.g. after a fronted subordinator) as an agentless passive.
    The clause-local agent is read off the aligned REFERENCE clause's subject."""
    if not V3.agent_gate(ann, wtags)[0]:
        return None
    skc, ansc, refc = V3.split_sk(sk), V3.split_en(answer), V3.split_en(reference)
    if len(skc) < 2 or not (len(skc) == len(ansc) == len(refc)):
        return None
    agent = V2.slovak_agent(sk, ann, wtags)[0]
    atoks = V3.parse_agent_tokens(agent)[0]
    for idx, ac in enumerate(ansc):
        skcl, rcl = skc[idx], refc[idx]
        if V3.sk_clause_has(skcl, atoks):
            continue                                   # v3's own territory: annotation agent here
        if V3.sk_clause_is_passive(skcl) or SK_REFLEX.search(skcl):
            continue
        rsub = V3.strip_front_adv(V3.subject_np(rcl))
        if not rsub:
            continue
        head = rsub[-1].lower()
        if head in DET_START or (len(head) < 2 and head != 'i'):
            continue
        if V3.find_passive(rcl, True, None) is not None:
            continue                                   # the reference itself is agentless: licensed
        sk_low = {w.lower() for w in V3.sk_toks(skcl)}
        if head in EN_PRON:
            if variant == 'noun' or not (sk_low & SK_PRON):
                continue                               # Slovak pro-drop / 3pl impersonal
            forms = _pron_group(head)
        else:
            forms = {head}
        if V3.find_passive(ac, True, forms) is None:
            continue
        if _renders([w.lower() for w in toks(ac)], forms):
            continue                                   # the clause does render the agent
        return {'fired': True, 'agent': agent, 'agent_kind': 'clause-local', 'agent_source': 'ref',
                'agent_token_elsewhere_in_answer': False, 'answer_is_agentless_passive': True,
                'clause': {'idx': idx, 'answer_clause': ac, 'sk_clause': skcl, 'ref_clause': rcl,
                           'local_agent': head},
                'reason': ('LOCAL: agentless passive in clause %d against the active Slovak clause '
                           '%r whose own agent the reference renders as %r' % (idx, skcl, head))}
    return None


# ------------------------------------------------------------------ the rule
def decide(sk, ann, wtags, answer, reference, variant='primary', flags=ALL_FLAGS):
    flags = tuple(flags or ())
    if not flags:
        return V3.decide(sk, ann, wtags, answer, reference, variant, V3_BASE)
    lex = _lex_patch(ann, wtags) if 'lex' in flags else _Patch([])
    with lex:
        al = _align_patch(sk, ann, wtags, answer, reference) if 'align' in flags else _Patch([])
        with al:
            d = V3.decide(sk, ann, wtags, answer, reference, variant, V3_BASE)
        d['flags'] = list(flags)
        if d['fired']:
            return d
        if 'union' in flags or 'unionx' in flags:
            reason = d.get('reason') or ''
            guarded = 'union' in flags and 'unionx' not in flags
            if not (guarded and any(k in reason for k in CLAUSE_ABSTAIN)):
                f = V3.decide(sk, ann, wtags, answer, reference, variant, ('subj', 'by'))
                if f['fired']:
                    f['flags'] = list(flags)
                    f['reason'] = 'UNION(whole-sentence): ' + (f['reason'] or '')
                    return f
        for fl, fn in (('lex', _reduced_relative), ('local', _local_agent)):
            if fl in flags:
                r = fn(sk, ann, wtags, answer, reference, variant)
                if r:
                    r['flags'] = list(flags)
                    return r
    return d


if __name__ == '__main__':
    import gate_v4
    sys.exit(gate_v4.main("--measure" in sys.argv))
