#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1V / Track C - CZECH-SPECIFIC source reader (0 model calls, offline).

The Slovak readers are NOT touched. This module builds NEW, separate module objects (cz_f9, cz_ck,
cz_v2, cz_v3) from the Slovak source text plus four named, asserted Czech patches:

  em      checker_1i.sk_features: Czech has no 1sg present in -em (Slovak `poviem/idem` family); the
          `-em` ending there is the Czech instrumental (hercem, záběrem, ředitelem, certifikátem) or a
          preposition (kolem) or the auxiliary `jsem`. The Czech reader drops `em` from the 1sg ending
          list. `-ím/-ám` stay (Czech 1sg vidím / dělám). Slovak `-iem` is dropped too (not Czech).
  se      agent_drop_v2.SK_REFLEX: add the Czech reflexive clitic `se` (Slovak had only sa|si). Czech V3
          is loaded against the Czech V2, so its clause-scoped SK_REFLEX (:462) sees `se` as well.
  jestli  f9: `jestli / jestliže / zdali` (Czech "if/whether") end in -li and were read as a plural
          l-participle -> past. Added to L_NONVERB (never a participle) and SUB_MARK (subordinator).
  aspect  f9: Czech perfective lexicon (present form = future meaning), incl. `dokáže` which the Slovak
          list files as a MODAL (present) - moved out of MOD in the Czech copy only.

build(fixes) returns {"f9", "CK", "V2", "V3"} for any subset of the four fixes (ablation).
"""
import os
import sys
import types
import hashlib

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
SRC = {"f9": "phase1n/f9.py", "CK": "phase1i/checker_1i.py",
       "V2": "phase1s/taskC/agent_drop_v2.py", "V3": "phase1t/taskA/agent_drop_v3.py"}
ALL_FIXES = ("em", "se", "jestli", "aspect")

# (old, new) source patches; each must match EXACTLY once in the Slovak source text
PATCH_EM = [(
    "if (x.endswith(('ím', 'ám', 'iem', 'em')) and len(x) >= 4",
    "if (x.endswith(('ím', 'ám')) and len(x) >= 4                    # CZ: no 1sg in -em/-iem",
)]
PATCH_SE = [(
    "SK_REFLEX = re.compile(r'(^|\\s)(sa|si)(\\s|[.,!?]|$)', re.I)",
    "SK_REFLEX = re.compile(r'(^|\\s)(se|sa|si)(\\s|[.,!?]|$)', re.I)   # CZ: + se",
)]

CZ_LI = {"jestli", "jestliže", "zdali", "zdalipak"}
CZ_PERF = set("""dokáže dokážu dokážeš dokážeme dokážete zkusí zkusím zkusíš zkusíme zkusíte vydrží vydržím
vydržíš vydržíme vydržíte koupí koupím koupíš koupíme koupíte dá dám dáš dáme dáte dají vrátí vrátím vrátíš
vrátíme vrátíte řekne řeknu řekneš řekneme řeknete řeknou přijde přijdu přijdeš přijdeme přijdete přijdou
potká potkám potkáš potkáme potkají začne začnu začneš začneme začnou skončí skončím skončíš skončíme
najde najdu najdeš najdeme najdou vezme vezmu vezmeš vezmeme vezmou pustí pustím pustíš padne padnu padnou
sedne sednu sednou vstane vstanu vstanou ukáže ukážu ukážeš ukážeme ukážou pošle pošlu pošleš pošleme pošlou
zastaví zastavím zastavíš hodí hodím hodíš chytí chytím chytíš pozve pozvu pozveš pozvou dostane dostanu
dostaneš dostaneme dostanou stane stanou otevře otevřu otevřeš otevřou zavře zavřu zavřeš zavřou sní sním
vypije vypiju udělá udělám uděláš uděláme udělají přestane přestanu přestanou zavolá zavolám zavoláme
pomůže pomůžu pomůžeš pomůžeme pomohou""".split())


def sha(rel):
    return hashlib.sha256(open(os.path.join(BASE, rel), "rb").read()).hexdigest()


def _exec(name, rel, patches=()):
    text = open(os.path.join(BASE, rel), encoding="utf-8").read()
    for old, new in patches:
        k = text.count(old)
        if k != 1:
            raise RuntimeError("patch for %s matched %d times: %r" % (rel, k, old))
        text = text.replace(old, new)
    m = types.ModuleType(name)
    m.__file__ = os.path.join(BASE, rel)          # original dir, so relative sys.path inserts work
    sys.modules[name] = m
    exec(compile(text, "<%s:%s>" % (name, rel), "exec"), m.__dict__)
    return m


def build(fixes=ALL_FIXES):
    fixes = set(fixes)
    bad = fixes - set(ALL_FIXES)
    if bad:
        raise ValueError(bad)
    tag = "_".join(sorted(fixes)) or "none"
    f9 = _exec("cz_f9_" + tag, SRC["f9"])
    if "jestli" in fixes:
        f9.L_NONVERB |= CZ_LI
        f9.SUB_MARK |= CZ_LI
    if "aspect" in fixes:
        f9.MOD -= CZ_PERF
        f9.PERF_LEX |= CZ_PERF
    ck = _exec("cz_ck_" + tag, SRC["CK"], PATCH_EM if "em" in fixes else ())
    v2 = _exec("cz_v2_" + tag, SRC["V2"], PATCH_SE if "se" in fixes else ())
    saved = sys.modules.get("agent_drop_v2")
    sys.modules["agent_drop_v2"] = v2               # V3 binds `import agent_drop_v2 as V2` to the Czech V2
    try:
        v3 = _exec("cz_v3_" + tag, SRC["V3"])
    finally:
        if saved is None:
            sys.modules.pop("agent_drop_v2", None)
        else:
            sys.modules["agent_drop_v2"] = saved
    return {"f9": f9, "CK": ck, "V2": v2, "V3": v3}
