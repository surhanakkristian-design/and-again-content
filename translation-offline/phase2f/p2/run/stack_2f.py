#!/usr/bin/env python3
"""Phase 2F Part 2 stack = the FROZEN Phase 1W stack with the language changed to Czech and
nothing else: 1V round 2 (AG v4 full + v5 refsubj rs_nom + TIP determiner rule) + the §2 agent
reader (phase1w/reader_nom.py) installed with lang='cz' and the Czech modules from
phase1v/trackC/cz_reader.build() (the four 1T fixes em/se/jestli/aspect).  The three 2C reader
patches (tok/verbish/agent) are NOT applied here - they live in phase2c/derive_2c.py, which is the
annotation path, not the decision path.  RECORDED, not fixed."""
import os, sys
sys.dont_write_bytecode = True
TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')
for p in (os.path.join(TOFF, 'phase1w'), os.path.join(TOFF, 'phase1v', 'trackA_loop'),
          os.path.join(TOFF, 'phase1v', 'trackC')):
    if p not in sys.path:
        sys.path.insert(0, p)
import stack_1v as S                                                           # noqa: E402
import reader_nom as R                                                         # noqa: E402
import cz_reader as CZR                                                        # noqa: E402
EXTRA = ('rs_nom',)
READER_VARIANT = R._default()
CZ = CZR.build()                       # {'f9','CK','V2','V3'} - the Czech module copies
CZMODS = {'f9': CZ['f9'], 'CK': CZ['CK']}
LANG = 'cz'


def decide(sk, ann, wtags, answer, reference, variant='primary', flags=None, extra=EXTRA):
    with R.installed(S.V3.V2, LANG, READER_VARIANT, mods=CZMODS):
        return S.decide(sk, ann, wtags, answer, reference, variant, flags, extra)


def final_accept(row, extra=EXTRA, tip=True):
    return S.final_accept(row, extra, tip)
