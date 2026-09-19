#!/usr/bin/env python3
"""Phase 1W §3 (A2(a)) - the L3 determiner prompt line.  Inserted per record (like the lever lines),
ONLY where the answer differs from the reference in determiner tokens alone; placed after the last
inserted line (voice / lever lines / ARTICLE_LINE_1U) and before the frozen tail."""
import re, difflib
DETS = {'a', 'an', 'the', 'this', 'that', 'these', 'those',
        'my', 'your', 'his', 'her', 'its', 'our', 'their'}
DET_LINE = ("Determiners: Slovak has no articles, so where the learner sentence differs from the reference "
            "only in a determiner, judge that point like this. A different article (a / an / the), or no "
            "article where English allows none, is SAME on that point; an article English grammar requires "
            "that is simply left out stays DIFF. A demonstrative (this, that, these, those) that the learner "
            "adds, drops or uses instead of an article or a possessive is DIFF only where the Slovak itself "
            "has a demonstrative at that point (ten, tá, to, tie, tieto or another form of them); where "
            "the Slovak has none, it is SAME on that point. A possessive (my, our, his, her, their) used "
            "instead of an article where the Slovak context makes it natural is SAME on that point.")


def toks(s):
    return re.findall(r"[a-z']+", (s or '').lower().replace('’', "'"))


def det_diff(answer, reference):
    a, r = toks(answer), toks(reference)
    if a == r:
        return False
    sm = difflib.SequenceMatcher(a=r, b=a, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'equal' and not all(t in DETS for t in r[i1:i2] + a[j1:j2]):
            return False
    return True


def insert_line(user, wording, skip, line=DET_LINE):
    lines = user.split('\n')
    at = [k for k, ln in enumerate(lines) if ln == wording]
    if len(at) != 1:
        raise SystemExit('REFUSED: WORDING_LINE occurs %d times' % len(at))
    k = at[0] + 1
    while k < len(lines) and lines[k] in skip:
        k += 1
    return '\n'.join(lines[:k] + [line] + lines[k:])


def install(RU, ids=None):
    """Patch RU.R1K.build_req so triggered records carry DET_LINE.  ids=None -> trigger = det_diff.
    RU = runner_1u-like module (R1K, R1N, AL, P, R).  Returns the original builder."""
    orig = RU.R1K.build_req

    def br(st, r, pid):
        s, u, g, h = orig(st, r, pid)
        hit = det_diff(r['answer'], r['reference']) if ids is None else r['item_id'] in ids
        if not hit:
            return s, u, g, h
        skip = {RU.R1N.VOICE_SAME_LINE, RU.AL.ARTICLE_LINE_1U} | set(r.get('_extra') or [])
        u2 = insert_line(u, RU.P.WORDING_LINE, skip)
        return s, u2, g, RU.R.req_hash(s, u2, g)
    RU.R1K.build_req = br
    return orig
