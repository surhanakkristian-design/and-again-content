#!/usr/bin/env python3
"""Phase 1U — the ONE line the L3 prompt gains, as a module-level string.

The text is the block between the `>>>` markers of phase1u/stack/L3_PROMPT_1U.txt.  At import the
module re-reads that file and REFUSES if the literal below is not byte-identical to it, and if the
owner's ruling block carried in the same file is not byte-identical to phase1u/RULING_ARTICLE.txt.
Nothing outside phase1u/ is written or edited.
"""
import os
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
P1U = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(HERE))), 'phase1u')   # 1W: read the frozen 1U prompt/ruling in place (path fix, pre-run)
STACK = os.path.join(P1U, 'stack', 'L3_PROMPT_1U.txt')
RULING = os.path.join(P1U, 'RULING_ARTICLE.txt')

ARTICLE_LINE_1U = (
    'Articles: the previous point is about the CHOICE of article. An article that English grammar '
    'REQUIRES and the learner sentence simply leaves out ("Dad will buy new fridge.", "It is cold '
    'in kitchen today.") is not acceptable English and is DIFF. An English article is a '
    'grammatical requirement of the target language, and Slovak has no article to omit in the '
    'first place, so nothing was dropped in translation: the sentence is simply not grammatical '
    'English. Where more than one determiner is grammatical (a / the / a possessive / no article '
    'where English allows it), the choice stays free and is SAME on that point.')


def line_from_stack(path=STACK):
    """The first non-empty line after the '>>>' marker block."""
    lines = open(path, encoding='utf-8').read().split('\n')
    at = [k for k, ln in enumerate(lines) if ln.startswith('>>>')]
    if not at:
        raise SystemExit('REFUSED: no >>> marker in %s' % path)
    for ln in lines[at[-1] + 1:]:
        if ln.strip():
            return ln
    raise SystemExit('REFUSED: no prompt line after the >>> markers in %s' % path)


def ruling_from_stack(path=STACK):
    txt = open(path, encoding='utf-8').read()
    at = txt.find("OWNER'S RULING ON ARTICLES (Phase 1U)")
    if at < 0:
        raise SystemExit('REFUSED: the ruling block is not in %s' % path)
    body = txt[at:]
    cut = body.find('\n(The ruling is the owner')
    return (body[:cut] if cut > 0 else body).strip()


def check():
    got = line_from_stack()
    if got != ARTICLE_LINE_1U:
        raise SystemExit('REFUSED: ARTICLE_LINE_1U differs from L3_PROMPT_1U.txt\nfile: %r\nhere: %r'
                         % (got, ARTICLE_LINE_1U))
    ruling = open(RULING, encoding='utf-8').read().strip()
    if ruling_from_stack() != ruling:
        raise SystemExit('REFUSED: the ruling block in L3_PROMPT_1U.txt is not RULING_ARTICLE.txt')
    for probe in ('"Dad will buy new fridge."', '"It is cold in kitchen today."',
                  'is DIFF', 'the choice stays free and is SAME on that point'):
        if probe not in ARTICLE_LINE_1U:
            raise SystemExit('REFUSED: the ruling phrase %r is not in ARTICLE_LINE_1U' % probe)
    if ARTICLE_LINE_1U != ARTICLE_LINE_1U.strip() or '\n' in ARTICLE_LINE_1U:
        raise SystemExit('REFUSED: ARTICLE_LINE_1U is not one bare physical line')
    return {'ok': True, 'sha_line': _sha(ARTICLE_LINE_1U), 'sha_ruling': _sha(ruling),
            'chars': len(ARTICLE_LINE_1U)}


def _sha(s):
    import hashlib
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


CHECK = check()

if __name__ == '__main__':
    import json
    print(json.dumps(CHECK, indent=1))
