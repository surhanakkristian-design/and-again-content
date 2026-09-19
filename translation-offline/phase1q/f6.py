#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F6 - ADDITION GUARD (mirror of F5).  100% OFFLINE, 0 model calls.

Owner's rule: "An OMISSION is accepted.  An ADDITION is rejected."
F5 catches dropped content; F6 catches content the English answer CARRIES
that the Slovak sentence does not have ("in the pot", "at night", an extra
adjective, an extra object).

    check(slovak, annotation, answer) -> {"verdict": "reject"|"accept"|"abstain",
                                          "added": [...], "reason": str, ...}

Licensed vocabulary of a sentence = content lemmas of ALL stored renderings v
+ every alt key and every alt synonym + a closed function-word list, compared
under light lemmatisation (plural -s, -ed, -ing, -ly, -ise/-ize, irregulars).
An answer is rejected ONLY when it is safe: it otherwise lines up with the
references (high content overlap) AND carries a small number of extra content
tokens.  A free paraphrase full of unknown words ABSTAINS, never rejects.
"""
import os
import re
import sys

# ---------------------------------------------------------------- variants --
VARIANTS = {
    # A - aggressive: low overlap bar, up to 3 addition groups, a solo extra
    #     adjective/adverb is enough to reject.
    'A': dict(min_overlap=0.70, max_groups=3, require_anchored=False, solo_modifier=True),
    # B - middle: high overlap bar, at most 2 addition groups, solo modifier counts.
    'B': dict(min_overlap=0.85, max_groups=2, require_anchored=False, solo_modifier=True),
    # C - conservative: high overlap bar, at most 2 groups, and at least one
    #     addition must be anchored (inside a prepositional phrase or an extra
    #     determined noun phrase); a lone extra adjective/adverb abstains.
    'C': dict(min_overlap=0.80, max_groups=2, require_anchored=True, solo_modifier=False,
              strict_anchor=True),
}
VARIANT = 'C'

# ------------------------------------------------------------ word classes --
PREPS = set("""in on at by for with from into onto to of about after before during under over
above below behind beside near around through across between among against without within
towards toward up down out off past along inside outside per via""".split())

FUNCTION = set("""a an the this that these those such
i you he she it we they me him her us them my your his its our their mine yours hers ours theirs
myself yourself himself herself itself ourselves yourselves themselves one ones oneself
am is are was were be been being get gets got gotten getting
do does did doing done have has had having
will would shall should can could may might must ought need dare going gonna let lets
not no nor n't never ever yet still already just also only even too very really quite rather
much many more most less least all both each every either neither some any none other another same
and or but so because since as if when while whenever until unless although though whether than
that which who whom whose what where why how there here then thus however nevertheless nonetheless
else ok well away back again far quite sort kind
s t re ll ve d m""".split()) | PREPS

IRREG = {
    'children': 'child', 'men': 'man', 'women': 'woman', 'feet': 'foot', 'teeth': 'tooth',
    'geese': 'goose', 'mice': 'mouse', 'people': 'person', 'lives': 'life', 'leaves': 'leaf',
    'knives': 'knife', 'wives': 'wife', 'shelves': 'shelf', 'halves': 'half', 'loaves': 'loaf',
    'cacti': 'cactus', 'cactuses': 'cactus', 'analyses': 'analysis',
    'went': 'go', 'gone': 'go', 'goes': 'go', 'going': 'go',
    'took': 'take', 'taken': 'take', 'takes': 'take', 'taking': 'take',
    'made': 'make', 'makes': 'make', 'making': 'make',
    'said': 'say', 'says': 'say', 'told': 'tell', 'tells': 'tell',
    'gave': 'give', 'given': 'give', 'gives': 'give', 'giving': 'give',
    'wrote': 'write', 'written': 'write', 'writes': 'write', 'writing': 'write',
    'brought': 'bring', 'brings': 'bring', 'bought': 'buy', 'buys': 'buy',
    'caught': 'catch', 'catches': 'catch', 'catching': 'catch',
    'built': 'build', 'builds': 'build', 'found': 'find', 'finds': 'find',
    'left': 'leave', 'leaves_v': 'leave', 'lost': 'lose', 'loses': 'lose',
    'kept': 'keep', 'keeps': 'keep', 'held': 'hold', 'holds': 'hold',
    'sold': 'sell', 'sells': 'sell', 'stood': 'stand', 'stands': 'stand',
    'ran': 'run', 'runs': 'run', 'running': 'run', 'began': 'begin', 'begun': 'begin',
    'broke': 'break', 'broken': 'break', 'breaks': 'break',
    'drove': 'drive', 'driven': 'drive', 'drives': 'drive', 'driver': 'drive',
    'saw': 'see', 'seen': 'see', 'sees': 'see', 'sent': 'send', 'sends': 'send',
    'read': 'read', 'put': 'put', 'puts': 'put', 'cut': 'cut', 'cuts': 'cut',
    'set': 'set', 'sets': 'set', 'hung': 'hang', 'hangs': 'hang',
    'knew': 'know', 'known': 'know', 'knows': 'know', 'grew': 'grow', 'grown': 'grow',
    'ground': 'grind', 'grinds': 'grind', 'wound': 'wind', 'winds': 'wind',
    'felt': 'feel', 'feels': 'feel', 'slept': 'sleep', 'sleeps': 'sleep',
    'won': 'win', 'wins': 'win', 'paid': 'pay', 'pays': 'pay',
    'swept': 'sweep', 'fell': 'fall', 'fallen': 'fall', 'falls': 'fall',
    'spoke': 'speak', 'spoken': 'speak', 'speaks': 'speak',
    'meant': 'mean', 'means': 'mean', 'sewn': 'sew', 'sewed': 'sew', 'sews': 'sew',
    'better': 'good', 'best': 'good', 'worse': 'bad', 'worst': 'bad',
    'mum': 'mother', 'mom': 'mother', 'mummy': 'mother', 'dad': 'father', 'daddy': 'father',
    'grandad': 'grandpa', 'granddad': 'grandpa', 'grandfather': 'grandpa',
    'kids': 'child', 'kid': 'child',
}
NUM = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six',
       '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve',
       '18': 'eighteen', '20': 'twenty'}
CONTRACT = [("won't", "will not"), ("can't", "can not"), ("shan't", "shall not"),
            ("n't", " not"), ("'re", " are"), ("'ve", " have"), ("'ll", " will"), ("'m", " am"),
            ("'d", " would"), ("cannot", "can not")]


def _tok(s):
    s = (s or '').lower().replace('’', "'").replace('á', 'a').replace('é', 'e')
    for a, b in CONTRACT:
        s = s.replace(a, b)
    s = s.replace("'s", ' ')
    s = re.sub(r'[^a-z0-9À-ſ\- ]+', ' ', s)
    out = []
    for w in s.split():
        out.extend([p for p in w.split('-') if p])
    return out


PREFIX = ('re', 'un', 'over', 'under', 'out', 'up', 'mis', 'dis')


def _irr(w):
    if w in IRREG:
        return IRREG[w]
    for pre in PREFIX:
        if w.startswith(pre) and w[len(pre):] in IRREG:
            return pre + IRREG[w[len(pre):]]
    return None


def canon(w):
    w = NUM.get(w, w)
    if _irr(w):
        return _irr(w)
    if len(w) > 4 and w.endswith('ise'):
        w = w[:-3] + 'ize'
    if len(w) > 5 and w.endswith('ised'):
        w = w[:-4] + 'ize'
    if len(w) > 4 and w.endswith('our'):
        w = w[:-3] + 'or'
    if len(w) > 4 and w.endswith('re') and w[:-2].endswith(('t', 'b')):
        w = w[:-2] + 'er'
    for suf, cut in (('ies', 3), ('ied', 3), ('ily', 3)):
        if len(w) > 4 and w.endswith(suf):
            return w[:-cut] + 'y'
    for suf in ('ingly', 'edly', 'ing', 'ed', 'ly', 'es', 's'):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            b = w[:-len(suf)]
            if suf in ('ing', 'ed') and len(b) > 2 and b[-1] == b[-2] and b[-1] not in 'aeiou':
                b = b[:-1]
            if suf in ('ing', 'ed') and b.endswith(('at', 'iz', 'us', 'as', 'ur', 'ov', 'nc', 'nag')):
                b = b + 'e'
            return _irr(b) or b
    return w


def _ann(annotation):
    a = annotation
    if isinstance(a, dict):
        if isinstance(a.get('hygienised'), dict):
            a = a['hygienised']
        elif isinstance(a.get('raw'), dict) and 'v' in a['raw']:
            a = a['raw']
        elif isinstance(a.get('annotation'), dict):
            return _ann(a['annotation'])
    return a if isinstance(a, dict) else {}


def licensed_vocab(annotation):
    """Content lemmas licensed by the references: every rendering v, every alt
    key and every alt synonym."""
    a = _ann(annotation)
    lic, seen_v = set(), []
    for v in (a.get('v') or []):
        seen_v.append(v)
        for w in _tok(v):
            if w not in FUNCTION:
                lic.add(canon(w))
    alt = a.get('alt') or {}
    if isinstance(alt, dict):
        for k, vals in alt.items():
            for phrase in [k] + list(vals or []):
                for w in _tok(phrase):
                    if w not in FUNCTION:
                        lic.add(canon(w))
    return lic, seen_v


def _groups(idx, toks, extra_idx):
    """maximal runs of extra tokens, separated by at most one function token"""
    out, cur = [], []
    prev = None
    for i in idx:
        if prev is not None and i - prev > 2:
            out.append(cur)
            cur = []
        cur.append(i)
        prev = i
    if cur:
        out.append(cur)
    return out


def _anchored(g, toks, lic, strict=False):
    """is this addition group anchored as a phrase (PP or a determined NP)?

    strict: the group must be introduced by a preposition directly, or by a
    preposition plus a single article ("in the pot", "at night", "with tape").
    """
    i = g[0]
    if strict:
        if i > 0 and toks[i - 1] in PREPS:
            return True
        if i > 1 and toks[i - 1] in ('a', 'an', 'the') and toks[i - 2] in PREPS:
            return True
        return False
    for j in (i - 1, i - 2):
        if j >= 0 and toks[j] in PREPS:
            return True
    for j in (i - 1, i - 2):
        if j >= 0 and toks[j] in ('a', 'an', 'the', 'that', 'this', 'those', 'these'):
            # an extra noun phrase only counts if the head itself is extra
            if g[-1] == max(g) and (g[-1] + 1 >= len(toks) or canon(toks[g[-1] + 1]) in lic
                                    or toks[g[-1] + 1] in FUNCTION):
                return True
    return False


def _modifier_only(g, toks, lic):
    """group is a bare modifier: -ly adverb, or an adjective glued to a licensed noun"""
    for i in g:
        w = toks[i]
        if w.endswith('ly'):
            continue
        nxt = toks[i + 1] if i + 1 < len(toks) else ''
        if nxt and canon(nxt) in lic:
            continue
        return False
    return True


def check(slovak, annotation, answer, variant=None):
    cfg = VARIANTS[variant or VARIANT]
    lic, vs = licensed_vocab(annotation)
    toks = _tok(answer)
    content = [(i, w) for i, w in enumerate(toks) if w not in FUNCTION]
    base = {'added': [], 'overlap': None, 'variant': variant or VARIANT, 'n_content': len(content)}
    if not lic:
        base.update(verdict='abstain', reason='no reference vocabulary available')
        return base
    if len(content) < 3:
        base.update(verdict='abstain', reason='too few content tokens to judge')
        return base
    extra_idx = [i for i, w in content if canon(w) not in lic]
    known = len(content) - len(extra_idx)
    overlap = known / float(len(content))
    base['overlap'] = round(overlap, 3)
    base['added'] = [toks[i] for i in extra_idx]
    if not extra_idx:
        base.update(verdict='accept', reason='every content word of the answer is licensed by the references')
        return base
    if overlap < cfg['min_overlap']:
        base.update(verdict='abstain', reason='content overlap %.2f below %.2f - free paraphrase, not judged'
                    % (overlap, cfg['min_overlap']))
        return base
    gs = _groups(extra_idx, toks, extra_idx)
    if len(gs) > cfg['max_groups']:
        base.update(verdict='abstain', reason='%d separate unknown groups - too diffuse to blame an addition' % len(gs))
        return base
    anchored = [g for g in gs if _anchored(g, toks, lic, cfg.get('strict_anchor', False))]
    if cfg['require_anchored'] and not anchored:
        base.update(verdict='abstain', reason='extra content is not an anchored phrase (no preposition / determiner)')
        return base
    if not cfg['solo_modifier']:
        real = [g for g in gs if not _modifier_only(g, toks, lic)]
        if not real:
            base.update(verdict='abstain', reason='only a bare extra modifier - not rejected under this variant')
            return base
    phrases = [' '.join(toks[g[0]:g[-1] + 1]) for g in gs]
    base.update(verdict='reject', added_phrases=phrases,
                reason='added meaning: the answer carries content the Slovak does not have (%s)'
                       % '; '.join('"%s"' % p for p in phrases))
    return base


# ----------------------------------------------------------------- selftest --
ANN = {'v': ['Peter checks the letterbox by the gate every morning.',
             'Every morning Peter checks the letterbox by the gate.'],
       'alt': {'gate': ['gateway'], 'letterbox': ['mailbox', 'postbox']}}
CASES = [
    ('Peter kontroluje schranku.', 'Every morning Peter checks the mailbox by the gateway.', {'accept'}),
    ('Peter kontroluje schranku.', 'Peter checks the mailbox by the gate every morning before work.', {'reject'}),
    ('Peter kontroluje schranku.', 'Each dawn the fellow inspects his correspondence receptacle outdoors.',
     {'abstain'}),
]


def selftest():
    bad = []
    for sk, en, ok in CASES:
        r = check(sk, ANN, en)
        if r['verdict'] not in ok:
            bad.append((en, r['verdict'], sorted(ok), r['reason']))
    print('F6 selftest (VARIANT=%s): %d cases, %d failures' % (VARIANT, len(CASES), len(bad)))
    for b in bad:
        print('  FAIL %-60s -> %-8s want %s\n       %s' % (b[0][:60], b[1], b[2], b[3]))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(selftest())
