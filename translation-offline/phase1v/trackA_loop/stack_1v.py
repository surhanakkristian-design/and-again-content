#!/usr/bin/env python3
"""Phase 1V Track A - candidate stack additions on top of the frozen 1U stack (0 model calls).
agent_drop_v5 = AG v4 (unchanged, called first) + 'refsubj' patch: a REFERENCE clause subject
(the agent, active reference clause, not an expletive, pronoun only if the Slovak has an overt
pronoun) is rendered nowhere in the answer AND the answer carries (rs_pass) a be/get + participle
or (rs_nom) a nominalisation 'the X-tion/-ment/-ance/-al of'.  tip_det_rule = TIP-path rule:
an L3:TIPrej item whose answer differs from the reference ONLY by a determiner SWAP (a/an/the/
this/that/these/those/possessive <-> another one, no deletion/insertion) is accepted when the
Slovak has no demonstrative (ten/ta/to/tie/tieto and forms).
Entry point:  python3 stack_1v.py --results <results.json with rows[sk,answer,reference,ag,
final_accept,final_layer]> [--extra rs_pass,rs_nom] [--tip]  -> prints re-scored accept per row."""
import os, re, sys, json
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TO = os.path.dirname(os.path.dirname(HERE))
for p in (os.path.join(TO, 'phase1u', 'taskA'), os.path.join(TO, 'phase1t', 'taskA'),
          os.path.join(TO, 'phase1s', 'taskC')):
    if p not in sys.path:
        sys.path.insert(0, p)
import agent_drop_v4 as V4                                                    # noqa: E402
V3 = V4.V3
ORIG_V4_DECIDE = V4.decide
SK_PRON = getattr(V4, 'SK_PRON', {'ja', 'ty', 'on', 'ona', 'ono', 'my', 'vy', 'oni', 'ony'})
V5_EXTRA = ('rs_pass', 'rs_nom')
BADP = set('not it that what but just out at yet about most almost last next lot front want '
           'different important present absent excellent recent silent quiet great sweet hot '
           'cold old bold wild kind tired interested bored excited worried scared sent_'.split())
PASS_RE = re.compile(r"\b(?:is|are|was|were|be|been|being|get|gets|got|getting|gotten)\s+"
                     r"(?:\w+ly\s+)?([a-z]+(?:ed|en|wn|ne|lt|pt|nt|ght|ld|id|ung|ade|ost|et|ut|ot))\b", re.I)
NOM_RE = re.compile(r"\b(?:the|of|about|during)\s+(?:\w+\s+)?([a-z]+(?:tion|sion|ment|ance|ence|al))"
                    r"\s+of\b", re.I)
SKIP_HEAD = {'it', 'there', 'this', 'that', 'which', 'who', 'what', 'here'}


def _norm(x):
    x = x.lower().strip(".,;:!?\"'")
    for s in ('es', 's'):
        if x.endswith(s) and len(x) > len(s) + 2:
            return x[:-len(s)]
    return x


def ref_subject_heads(sk, reference):
    out, sk_low = [], {w.lower() for w in V3.sk_toks(sk)}
    for rcl in V3.split_en(reference):
        try:
            sub = V3.strip_front_adv(V3.subject_np(rcl))
        except Exception:
            continue
        if not sub:
            continue
        head = sub[-1].lower().strip(",.")
        if head in V4.DET_START or head in SKIP_HEAD or (len(head) < 2 and head != 'i'):
            continue
        try:
            if V3.find_passive(rcl, True, None) is not None:
                continue
        except Exception:
            pass
        if head in V4.EN_PRON:
            if not (sk_low & SK_PRON):
                continue
            forms = set(V4._pron_group(head))
        else:
            forms = {head}
        out.append((head, forms))
    return out


def refsubj(sk, answer, reference, extra=V5_EXTRA):
    if not extra:
        return None
    heads = ref_subject_heads(sk, reference)
    at = {_norm(t) for t in re.findall(r"[A-Za-z']+", answer)}
    missing = [h for h, f in heads if not ({_norm(x) for x in f} & at)]
    if not missing:
        return None
    if 'rs_pass' in extra:
        for m in PASS_RE.finditer(answer):
            if m.group(1).lower() not in BADP:
                return {'fired': True, 'agent_kind': 'refsubj', 'patch': 'rs_pass',
                        'reason': 'V5 rs_pass: reference subject %s not rendered; answer has %r'
                                  % (missing, m.group(0))}
    if 'rs_nom' in extra:
        m = NOM_RE.search(answer)
        if m:
            return {'fired': True, 'agent_kind': 'refsubj', 'patch': 'rs_nom',
                    'reason': 'V5 rs_nom: reference subject %s not rendered; nominalisation %r'
                              % (missing, m.group(0))}
    return None


def decide(sk, ann, wtags, answer, reference, variant='primary', flags=None, extra=V5_EXTRA):
    """agent_drop_v5.  v4 first (bit for bit), refsubj only where v4 abstains."""
    d = ORIG_V4_DECIDE(sk, ann, wtags, answer, reference, variant,
                       V4.ALL_FLAGS if flags is None else flags)
    if d.get('fired') or not extra:
        return d
    r = refsubj(sk, answer, reference, extra)
    if r:
        r['flags'] = list(d.get('flags') or []) + list(extra)
        return r
    return d


DETS = set('a an the this that these those my your his her its our their'.split())
SK_DEM = re.compile(r"(?<!\w)(ten|tá|to|tie|tí|tieto|títo|tento|táto|toto|toho|tej|tú|tom|tým|tou|"
                    r"tých|tými|tohto|tejto|túto|tomto|týmto|touto|týchto|týmito|onen|oná|ono|tamten|"
                    r"tamtá|tamto|tamtie)(?!\w)", re.I)
CONTR = [("it's", "it is"), ("that's", "that is"), ("there's", "there is"), ("won't", "will not"),
         ("don't", "do not"), ("doesn't", "does not"), ("isn't", "is not"), ("aren't", "are not"),
         ("can't", "cannot"), ("i'm", "i am"), ("we're", "we are"), ("they're", "they are")]


def _dtoks(s):
    s = s.lower().replace('’', "'")
    for a, b in CONTR:
        s = s.replace(a, b)
    return ['D' if t in DETS else t for t in re.findall(r"[a-z']+", s)]


def det_swap_only(answer, reference):
    a, r = _dtoks(answer), _dtoks(reference)
    if a != r:
        return False
    ra = [t for t in re.findall(r"[a-z']+", answer.lower().replace('’', "'"))]
    return True


def tip_det_rule(sk, answer, reference, layer):
    """True -> the TIP-path rejection is overturned (accept)."""
    if layer != 'L3:TIPrej' or SK_DEM.search(sk or ''):
        return False
    return det_swap_only(answer, reference) and answer.strip().lower() != reference.strip().lower()


def final_accept(row, extra=V5_EXTRA, tip=True):
    """Re-score one stored 1U-stack row (row['ag'] = stored AG v4 decision)."""
    acc = bool(row.get('final_accept'))
    layer = row.get('final_layer')
    if acc and extra and not (row.get('ag') or {}).get('fired'):
        if refsubj(row['sk'], row['answer'], row['reference'], extra):
            return False, 'AGv5'
    if not acc and tip and tip_det_rule(row['sk'], row['answer'], row['reference'], layer):
        return True, 'TIPdet'
    return acc, layer


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--results', required=True)
    ap.add_argument('--extra', default=','.join(V5_EXTRA))
    ap.add_argument('--tip', action='store_true')
    a = ap.parse_args()
    ex = tuple(x for x in a.extra.split(',') if x)
    rows = json.load(open(a.results))['rows']
    for r in rows:
        acc, lay = final_accept(r, ex, a.tip)
        print(json.dumps({'item_id': r.get('item_id'), 'accept': acc, 'layer': lay}))
