#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 2C GATE 1 DERIVE = phase2b/derive_2b.py + EXACTLY THREE reader patches (0 model calls, offline).

Frozen code (phase1*/, checker/, phase2b/) is IMPORTED and monkeypatched IN MEMORY ONLY; nothing outside
phase2c/ is edited.  Switchable: patches off  == byte-identical 2B behaviour ("before").

  P1 tok      f9.WORD character class did not contain r-hacek / u-kroucek: the Czech tokenizer split
              'Rekne mu domu' into ['ekne','mu','dom'].  WORD is replaced (on BOTH f9 module objects,
              Slovak f9_1n and the cz_reader.build() copy) by the full Czech+Slovak alphabet.
              Reaches f9.sk_frame (tf / tense_open / perfective_present), CZ_PERF aspect and
              reader_nom._lpset (l-participle -> person/number/gender).
  P2 verbish  reader_nom._verbish accepted nouns as finite verbs.  Wrapper around the frozen function:
              a token stays verbish for free only if it is a byt/byt-copula, a modal or an l-participle;
              otherwise it is rejected when (a) it is governed by a preposition in this sentence,
              (b) it is capitalised but not sentence-initial (proper noun / noun), (c) it ends in -s
              without a real 2sg present ending (-as/-is/-es).  General morphology, no sample words.
  P3 agent    reader_nom._decide_clause returned non-nominatives as agents.  A patched copy lives here:
              * pronoun step: a form that is BOTH a pronoun and a determiner (cz 'ty', 'ta', 'ti', 'to')
                immediately in front of a noun (adjectives skipped) is a determiner, not the pronoun;
              * NP-head filter for the noun-preverbal and noun-postcopula steps: closed-class
                adverbs / particles / conjunctions / subordinators (incl. the generated kdyby-/aby-
                conditional paradigm and the X+'ze' conjunction rule), deictic obliques in -hle,
                preposition-governed forms, and bare long-form adjectives (no head noun) are rejected;
              * when nothing survives the reader abstains, exactly as the frozen code does.

ENTRY POINT (production):   derive_2c.derive(row, lang=None, mode="after") -> dict
  row: {"n":int, "lang":"sk"|"cz", "src":str, "en":str, "level":str}  (lang= overrides/fills row["lang"])
  mode: "after" (all three patches, default) | "before" (exact 2B) | dict/kwargs for ablation
  returns the SAME schema as phase2b/derive_2b.derive():
     {"n","lang","level","src","en",
      "reader": {agent, why, clause, feats, agent_on_fallback_clause},
      "derived": {agent_nom, finite_verb, person, number, gender, tf, tense_open, perfective_present,
                  voice_sk}  each {"value":..., "source":str} (tf also "frames"),
      "voice_paths": {g4_v2_sk_reflex, g4_v3_passive_or_reflex, g4_cz_se_missed, agv4_sk_clause_passive,
                      agv4_sk_clause_reflex, agv4_main_passive, agv4_main_reflex, agv4_en_passive,
                      agv4_en_passive_span, reader_nom_full_agent},
      "rewrite": {action(U|R|ABSTAIN), new, pronoun, where, reason, check}}
  main() renames rewrite["new"] -> "sk_new"/"cz_new" exactly as derive_2b.main() does, so the arm-B
  script rewrite consumed by run_2b.py keeps working unchanged.
"""
import os, re, sys, json, collections, contextlib
sys.dont_write_bytecode = True
BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.join(BASE, "phase2c")
if os.path.join(BASE, "phase2b") not in sys.path:
    sys.path.insert(0, os.path.join(BASE, "phase2b"))
import derive_2b as D2B                                   # noqa: E402  frozen 2B derive (never edited)
R = D2B.R                                                 # phase1w/reader_nom
MODS = D2B.MODS
S = lambda s: set(s.split())

# --------------------------------------------------------------------- P1: the tokenizer character class
WORD_2C = re.compile(r"[a-záäčďéěíĺľňóôöŕřšťúůüýž]+", re.I)   # + r-hacek, u-kroucek (and o/u-umlaut)

# --------------------------------------------------------------------- P3: closed classes (NOT sample words)
# modal / evidential particles (closed class)
PARTICLE = {"sk": S("vraj asi azda snáď hádam vari veď však predsa akurát bodaj kiež nuž ba dokonca aspoň "
                    "zrejme pravdepodobne údajne skrátka jednoducho proste bohužiaľ našťastie žiaľ napokon "
                    "mimochodom totiž najmä hlavne len iba práve azda"),
            "cz": S("prý asi snad nejspíš zřejmě patrně údajně přece vždyť holt prostě jednoduše zkrátka "
                    "rozhodně bohužel naštěstí žel ostatně mimochodem totiž dokonce aspoň alespoň zejména "
                    "hlavně jen pouze právě")}
# deictic adverbs (demonstrative stems tak-/tam-/tu-/sem-/tehdy-...): closed class
ADV_DEIX = {"sk": S("tak takto takže tam tamto tadiaľ tu tuto sem odtiaľto vtedy odvtedy dovtedy potom predtým "
                    "inak ináč akosi nejako zase znovu preto nato"),
            "cz": S("tak takto takhle tudy tady tamhle onde tehdy potom předtím dosud doposud jinak nějak zase "
                    "znovu proto nato")}
# temporal / frequency adverbs (closed class of adverbials)
ADV_FREQ = {"sk": S("zvyčajne obyčajne bežne väčšinou občas zriedka pravidelne neustále ihneď vopred neskôr skôr "
                    "dopredu dozadu nabudúce najprv spočiatku zrazu odrazu doteraz odteraz dnes zajtra včera"),
            "cz": S("obvykle obyčejně běžně většinou občas zřídka pravidelně neustále ihned předem později dříve "
                    "dopředu dozadu napřed nejprve zprvu náhle dosud odteď dnes zítra včera")}
# conditional subordinators, generated from the paradigm (kdyby/aby + conditional auxiliary endings)
_CZ_COND = {b + e for b in ("kdyb", "ab") for e in ("y", "ych", "ys", "ychom", "yste")}
COND_SUB = {"sk": S("keby kebyže aby abyže žeby akoby čoby keďže pokiaľ nakoľko"),
            "cz": _CZ_COND | S("pokud jelikož ježto přestože ačkoli ačkoliv zatímco kdežto")}
# relative / interrogative particles
REL_PART = {"sk": S("čož čo ktorýžto čožeby"), "cz": S("což jenž jež jehož jejíž kterýžto")}
# stems that make a conjunction when 'že' is attached (nejenže, protože, takže, ...)
CONJ_STEM = {"sk": S("nielen preto tak ale a i lebo hoci sotva ibaže len"),
             "cz": S("nejen proto tak ale a i sotva jen ledaže takže")}
CLOSED = {L: (PARTICLE[L] | ADV_DEIX[L] | ADV_FREQ[L] | COND_SUB[L] | REL_PART[L] | R.SUB[L] | R.STOPALL[L])
          for L in ("sk", "cz")}
VALID_2SG = ("áš", "íš", "eš", "ýš")          # real 2sg present endings (-aš/-iš/-eš families)

_CTX = {"prep_gov": set(), "sent_init": set(), "lang": "sk"}
_ORIG_VERBISH = R._verbish
_ORIG_DECIDE = R._decide_clause


def _context(text, L):
    """Sentence-level context for the _verbish guards: preposition-governed forms + sentence-initial forms."""
    gov, init = set(), set()
    for s in re.split(r"[.!?…]+", text or ""):
        t = R._toks(s); low = [w.lower() for w in t]
        if low:
            init.add(low[0])
        i = 0
        while i < len(low):
            if low[i] in R.PREP[L]:
                j = i + 1
                while j < len(low) and (low[j] in R.DET[L] or low[j] in R.QUANT[L] or low[j] in R.PLNUM[L]
                                        or (len(low[j]) > 3 and low[j].endswith(R.ADJEND))):
                    gov.add(low[j]); j += 1
                if j < len(low):
                    gov.add(low[j])
                i = j + 1
            else:
                i += 1
    return gov, init


def _verbish_2c(tok, low, L, CK, lps):
    """P2: the frozen _verbish, minus noun readings (prep-governed / proper-noun / fake -š 2sg)."""
    if not _ORIG_VERBISH(tok, low, L, CK, lps):
        return False
    if low in R.BYT[L] or low in R.MODAL[L] or low in lps:
        return True                                       # unambiguous finite forms: keep
    if low in _CTX["prep_gov"]:
        return False                                      # 'po pobrežnej ceste' -> locative, not 2pl
    if tok[:1].isupper() and low not in _CTX["sent_init"]:
        return False                                      # capitalised mid-sentence: proper noun
    if low.endswith("š") and not low.endswith(VALID_2SG):
        return False                                      # 'Kámoš' is not a 2sg present
    return True


def _dem_not_pron(t, low, i, L, CK, lps):
    """P3a: a pronoun form that is also a determiner and stands in front of a noun is a determiner."""
    w = low[i]
    if w not in R.DET[L]:
        return False
    j = i + 1
    while j < len(low) and len(low[j]) > 3 and low[j].endswith(R.ADJEND):
        j += 1
    if j >= len(low):
        return False
    nx = low[j]
    if (nx in R.PREP[L] or nx in R.STOPALL[L] or nx in R.BYT[L] or nx in R.PRON[L] or nx in R.DET[L]
            or len(nx) < 3 or not nx.replace("-", "").isalpha()):
        return False
    return not R._verbish(t[j], nx, L, CK, lps)


def _nom_ok(low, mods, h, L):
    """P3b: is this NP head a possible NOMINATIVE noun phrase head?"""
    w = low[h]
    if w in CLOSED[L]:
        return False                                      # adverb / particle / conjunction / subordinator
    if w.endswith("že") and len(w) > 3 and (w[:-2] in CONJ_STEM[L] or w[:-2] in CLOSED[L]):
        return False                                      # Nejenže, ibaže, ...
    if w in _CTX["prep_gov"]:
        return False                                      # oblique inside a prepositional phrase
    if len(w) >= 5 and w.endswith("hle"):
        return False                                      # cz deictic oblique (touhle, tímhle, tomhle)
    if not mods and len(w) >= 5 and w.endswith(R.ADJEND):
        return False                                      # bare long-form adjective, no head noun
    return True


def _decide_clause_2c(t, low, f, L, variant, CK, lps):
    """P3: copy of reader_nom._decide_clause with the demonstrative rule and the NP-head filter."""
    p, n, g = f
    for i, w in enumerate(low):
        pr = R.PRON[L].get(w)
        if pr and (p is None or p == pr[0]) and (n is None or n == pr[1]) and \
                not (pr[2] and g and n != "pl" and g != pr[2]):
            if _dem_not_pron(t, low, i, L, CK, lps):
                continue
            return t[i], "pronoun"
    if variant == "pron":
        return None, "abstain:pronoun-only variant"
    if p in ("1", "2"):
        return None, "abstain:1st/2nd person pro-drop"
    if R.REFLEX[L].search(" ".join(low)):
        return None, "abstain:reflexive clause"
    vidx = {i for i in range(len(low)) if R._verbish(t[i], low[i], L, CK, lps)}
    if not vidx:
        return None, "abstain:no finite verb token"
    vi = min(vidx)
    if low[0] in ("to", "toto", "tohle") and len(low) > 1 and low[1] in R.BYT[L]:
        return t[0], "demonstrative+copula"
    i = 0
    while i < vi:
        if low[i] in R.PREP[L]:
            i = R._skip_pp(low, i + 1, L, vidx); continue
        if low[i] in R.STOPALL[L]:
            i += 1; continue
        r = R._np(t, low, i, L, vidx)
        if r:
            mods, h, nums = r
            if not _nom_ok(low, mods, h, L):
                i = h + 1; continue
            if h < vi and (n is None or n in nums):
                return " ".join(t[m] for m in mods + [h]), "noun-preverbal"
            i = h + 1; continue
        i += 1
    if low[vi] in R.BYT[L]:
        i = vi + 1
        while i < len(low):
            if low[i] in R.PREP[L]:
                i = R._skip_pp(low, i + 1, L, vidx); continue
            if low[i] in R.STOPALL[L] or i in vidx:
                i += 1; continue
            r = R._np(t, low, i, L, vidx)
            if r and (n is None or n in r[2]) and _nom_ok(low, r[0], r[1], L):
                return " ".join(t[m] for m in r[0] + [r[1]]), "noun-postcopula"
            break
    return None, "abstain:no agreeing nominative"


@contextlib.contextmanager
def patches(tok=True, verbish=True, agent=True):
    """Install the three patches in memory; restore the frozen behaviour on exit."""
    saved = []
    if tok:
        for L in ("sk", "cz"):
            f9 = MODS[L]["f9"]; saved.append((f9, "WORD", f9.WORD)); f9.WORD = WORD_2C
    if verbish:
        saved.append((R, "_verbish", R._verbish)); R._verbish = _verbish_2c
    if agent:
        saved.append((R, "_decide_clause", R._decide_clause)); R._decide_clause = _decide_clause_2c
    try:
        yield
    finally:
        for o, k, v in reversed(saved):
            setattr(o, k, v)


MODES = {"before": dict(tok=False, verbish=False, agent=False),
         "tok": dict(tok=True, verbish=False, agent=False),
         "verbish": dict(tok=False, verbish=True, agent=False),
         "agent": dict(tok=False, verbish=False, agent=True),
         "after": dict(tok=True, verbish=True, agent=True)}


def derive(row, lang=None, mode="after"):
    """Production entry point.  See the module docstring for the row and the output schema."""
    row = dict(row)
    if lang:
        row["lang"] = lang
    L = row["lang"]
    cfg = MODES[mode] if isinstance(mode, str) else dict(mode)
    _CTX["prep_gov"], _CTX["sent_init"] = _context(row["src"], L)
    _CTX["lang"] = L
    with patches(**cfg):
        return D2B.derive(row)


def main(mode="after", out="derived_2c.json"):
    rows = json.load(open(os.path.join(BASE, "phase2b", "sample_2b.json"), encoding="utf-8"))["rows"]
    res = [derive(r, mode=mode) for r in rows]
    for o in res:                                         # 2B-compatible key rename
        o["rewrite"]["sk_new" if o["lang"] == "sk" else "cz_new"] = o["rewrite"].pop("new")
    fields = ["agent_nom", "person", "number", "gender", "tf", "tense_open", "perfective_present", "voice_sk"]
    summ = {"fields": {f: {L: sum(1 for o in res if o["lang"] == L and o["derived"][f]["value"] is not None)
                           for L in ("sk", "cz")} for f in fields},
            "voice_sk_dist": dict(collections.Counter("%s:%s" % (o["lang"], o["derived"]["voice_sk"]["value"])
                                                      for o in res)),
            "rewrite": dict(collections.Counter("%s:%s:%s" % (o["lang"], o["level"], o["rewrite"]["action"])
                                                for o in res)),
            "machine_check_fail": [o["n"] for o in res if o["rewrite"]["check"] == "FAIL"]}
    doc = {"generated_by": "phase2c/derive_2c.py", "mode": mode, "model_calls": 0,
           "entry_point": "derive_2c.derive(row, lang=None, mode='after')", "summary": summ, "rows": res}
    json.dump(doc, open(os.path.join(HERE, out), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(summ, ensure_ascii=False)[:1200])


if __name__ == "__main__":
    main(*sys.argv[1:])
