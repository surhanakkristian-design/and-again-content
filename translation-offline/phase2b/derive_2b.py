#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 2B DERIVE (measurement only, 0 model calls, deterministic).

Reads phase2b/sample_2b.json (200 rows, sk 1..100, cz 101..200) and writes phase2b/derived_2b.json.
Frozen code is IMPORTED, never edited:
  reader      phase1w/reader_nom.py  read(text, lang, 'full', mods)   (cz: mods = phase1v/trackC/cz_reader.build())
  stack       phase1w/stack_1w.py -> phase1v/trackA_loop/stack_1v.py -> phase1u/taskA/agent_drop_v4.py
              -> phase1t/taskA/agent_drop_v3.py (V3.decide, V3_BASE)  = "the frozen AG v4 voice path"
  guards      phase1t/taskB/cz_validate.py g1..g4 (exec'd exactly as phase2a/run_2a.py did), per language
  tense       f9.sk_frame (phase1n/f9.py; cz copy with the 'aspect' + 'jestli' fixes)
Only new logic here: a small finite-verb morphology table (MORPH below), the voice mapping, and the
arm-B pronoun-insertion script with its machine check."""
import os, re, sys, json, collections
sys.dont_write_bytecode = True
BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.join(BASE, "phase2b")
for p in (os.path.join(BASE, "phase1w"), os.path.join(BASE, "phase1v", "trackC")):
    sys.path.insert(0, p)
import stack_1w as SW                                   # noqa: E402  frozen stack (imports V4, V3, V2, reader_nom)
import reader_nom as R                                  # noqa: E402
import cz_reader as CZR                                 # noqa: E402
V4 = SW.S.V4
V3 = SW.S.V3
V2 = V3.V2 if hasattr(V3, "V2") else sys.modules["agent_drop_v2"]
SKM = R.sk_mods()                                       # {'f9','CK'} Slovak
SKM = {"f9": SKM["f9"], "CK": SKM["CK"], "V2": V2, "V3": V3}
CZM = CZR.build()                                       # all four Czech fixes {'f9','CK','V2','V3'}
MODS = {"sk": SKM, "cz": CZM}

SRC = open(os.path.join(BASE, "phase1t/taskB/cz_validate.py"), encoding="utf-8").read()
GSLICE = SRC[SRC.index("WORD = re.compile"):SRC.index("\nout = []")]
NS = {}
for L, m in MODS.items():
    ns = {"re": re, "json": json, "os": os, "f9": m["f9"], "CK": m["CK"], "V2": m["V2"], "V3": m["V3"]}
    exec(GSLICE, ns)
    NS[L] = ns
EN_PASSIVE_V4 = V4._make_find_passive(V3.find_passive)  # the V4-patched English passive finder

# ------------------------------------------------------------------ morphology table (the only new lexicon)
MORPH = {
    "sk": {"aux_past": {"som": ("1", "sg"), "sme": ("1", "pl"), "ste": ("2", "pl")},   # 'si' = 2sg OR reflexive -> not used
           "copula": {"som": ("1", "sg"), "je": ("3", "sg"), "sme": ("1", "pl"), "ste": ("2", "pl"), "sú": ("3", "pl"),
                      "nie": None},
           "future": {"budem": ("1", "sg"), "budeš": ("2", "sg"), "bude": ("3", "sg"), "budeme": ("1", "pl"),
                      "budete": ("2", "pl"), "budú": ("3", "pl")},
           "cond": ("by",),
           # present endings, longest first; value (person, number) or None = ambiguous -> abstain
           "pres": [("ajú", ("3", "pl")), ("ujú", ("3", "pl")), ("ejú", ("3", "pl")), ("ia", ("3", "pl")),
                    ("ú", ("3", "pl")),
                    ("me", ("1", "pl")), ("te", ("2", "pl")), ("š", ("2", "sg")), ("m", ("1", "sg")),
                    ("uje", ("3", "sg")), ("á", ("3", "sg")), ("í", ("3", "sg")), ("e", ("3", "sg"))],
           "modal3sg": set("môže musí chce vie má smie"), "modal3pl": set("môžu musia chcú vedia majú smú"),
           "clitics": set("sa si ho mu jej ich im mi ti ma ťa nás vás sme som ste by to".split()),
           "impersonal": set("treba netreba možno".split()),
           "pron": {("1", "sg"): "ja", ("2", "sg"): "ty", ("1", "pl"): "my", ("2", "pl"): "vy",
                    ("3", "sg", "m"): "on", ("3", "sg", "f"): "ona", ("3", "sg", "n"): "ono",
                    ("3", "pl", "m"): "oni", ("3", "pl", "f"): "ony"}},
    "cz": {"aux_past": {"jsem": ("1", "sg"), "jsi": ("2", "sg"), "jsme": ("1", "pl"), "jste": ("2", "pl")},
           "copula": {"jsem": ("1", "sg"), "jsi": ("2", "sg"), "je": ("3", "sg"), "není": ("3", "sg"),
                      "jsme": ("1", "pl"), "jste": ("2", "pl"), "jsou": ("3", "pl"), "nejsou": ("3", "pl")},
           "future": {"budu": ("1", "sg"), "budeš": ("2", "sg"), "bude": ("3", "sg"), "budeme": ("1", "pl"),
                      "budete": ("2", "pl"), "budou": ("3", "pl")},
           "cond": ("by", "bych", "bys", "bychom", "byste"),
           "pres": [("ají", ("3", "pl")), ("ují", ("3", "pl")), ("ou", ("3", "pl")),
                    ("me", ("1", "pl")), ("te", ("2", "pl")), ("š", ("2", "sg")), ("m", ("1", "sg")),
                    ("uji", ("1", "sg")), ("u", ("1", "sg")),
                    ("í", None),                                   # 3sg or 3pl (prosí / prosí) -> ambiguous
                    ("uje", ("3", "sg")), ("á", ("3", "sg")), ("e", ("3", "sg")), ("ě", ("3", "sg"))],
           "modal3sg": set("může musí chce ví má smí umí".split()), "modal3pl": set("můžou mohou musejí chtějí vědí mají umějí".split()),
           "clitics": set("se si ho mu jí je jim mi ti mě tě nás vás jsem jsi jsme jste bych bys by to".split()),
           "impersonal": set("lze nelze třeba".split()),
           "pron": {("1", "sg"): "já", ("2", "sg"): "ty", ("1", "pl"): "my", ("2", "pl"): "vy",
                    ("3", "sg", "m"): "on", ("3", "sg", "f"): "ona", ("3", "sg", "n"): "ono",
                    ("3", "pl", "m"): "oni", ("3", "pl", "f"): "ony"}},
}
for L in MORPH:
    MORPH[L]["modal3sg"] = set(MORPH[L]["modal3sg"]) if not isinstance(MORPH[L]["modal3sg"], set) else MORPH[L]["modal3sg"]
MORPH["sk"]["modal3sg"] = set("môže musí chce vie má smie".split())
MORPH["sk"]["modal3pl"] = set("môžu musia chcú vedia majú smú".split())
EN_PRON = {"i": ("1", "sg", None), "we": ("1", "pl", None), "you": ("2", None, None), "he": ("3", "sg", "m"),
           "she": ("3", "sg", "f"), "it": ("3", "sg", "n"), "they": ("3", "pl", None)}
EN_SKIP = set("oh wow hey look well so yes no okay ok now today tomorrow yesterday then suddenly finally "
              "always never sometimes often maybe really just still also".split())


def en_subject(en):
    """First word of the English reference after interjections/adverbs, if it is a personal pronoun."""
    for w in re.findall(r"[a-z']+", (en or "").lower()):
        w = w.split("'")[0]
        if w in EN_SKIP:
            continue
        return w if w in EN_PRON else None
    return None


def verb_morph(tok, L, lps, low_clause):
    """(person, number, gender, tense_hint, source) for one verbal token; None fields = undecidable."""
    M, w = MORPH[L], tok.lower()
    if w in M["future"]:
        return M["future"][w] + (None, "future", "table:future-aux")
    if w in M["copula"] and M["copula"][w]:
        return M["copula"][w] + (None, "present", "table:copula")
    if w in lps:                                        # l-participle (f9._is_l_part, frozen)
        end = "li" if w.endswith("li") else "ly" if w.endswith("ly") else "la" if w.endswith("la") else \
              "lo" if w.endswith("lo") else "l"
        n = "pl" if end in ("li", "ly") else "sg"
        g = {"l": "m", "la": "f", "lo": "n", "li": "m", "ly": "f"}[end]
        aux = [M["aux_past"][x] for x in low_clause if x in M["aux_past"]]
        if L == "sk" and "si" in low_clause:
            return None, n, g, "past", "table:l-participle+ambiguous si"
        if aux:
            if len(set(aux)) > 1 or aux[0][1] != n and not (aux[0] == ("2", "pl")):
                return None, n, g, "past", "table:l-participle+conflicting aux"
            return aux[0][0], aux[0][1], g, "past", "table:l-participle+aux"
        cond = any(x in M["cond"] for x in low_clause)
        return "3", n, g, ("conditional" if cond else "past"), "table:l-participle,no aux"
    if w in M["modal3sg"]:
        return "3", "sg", None, "present", "table:modal"
    if w in M["modal3pl"]:
        return "3", "pl", None, "present", "table:modal"
    for end, pn in M["pres"]:
        if w.endswith(end) and len(w) > len(end) + 1:
            if pn is None:
                return "3", None, None, "present", "table:present -%s (number ambiguous)" % end
            return pn + (None, "present", "table:present -%s" % end)
    return None, None, None, None, "table:no ending"


def main_clause_verb(text, L, info):
    """Finite verb of the reader's main clause: first _verbish token (reader_nom, frozen)."""
    m = MODS[L]
    cl, fb = info.get("clause"), False
    cands = [cl] if cl else []
    if not cl:                                   # reader found no clause with person/number feats (e.g. 3sg
        fb = True                                # present): first non-subordinate, non-imperative clause
        for s_ in re.split(r'[.!?…]+', text or ''):
            for c in V3.split_sk(s_):
                t0 = [x.lower() for x in R._toks(c)]
                if t0 and t0[0] not in R.SUB[L] and t0[0] not in R.IMPER[L]:
                    cands.append(c)
    for cl in cands:
        t = R._toks(cl); low = [x.lower() for x in t]
        lps = R._lpset(cl, m["f9"])
        vidx = [i for i in range(len(low)) if R._verbish(t[i], low[i], L, m["CK"], lps)]
        if vidx:
            break
    else:
        return None
    # prefer the lexical verb over a clitic auxiliary for morphology, but keep the first index for placement
    vi = vidx[0]
    lex = [i for i in vidx if low[i] not in MORPH[L]["aux_past"]] or vidx
    return {"clause": cl, "fallback_clause": fb, "toks": t, "low": low, "vidx": vidx, "vi": vi, "lex_i": lex[0], "lps": lps}


def derive(row):
    L, text, en = row["lang"], row["src"], row["en"]
    m = MODS[L]
    agent, info = R.read(text, L, "full", m)
    feats = info.get("feats")
    out = {"n": row["n"], "lang": L, "level": row["level"], "src": text, "en": en,
           "reader": {"agent": agent, "why": info.get("why"), "clause": info.get("clause"),
                      "feats": list(feats) if feats else None}}
    V = main_clause_verb(text, L, info)
    # ---- person / number / gender from the morphology table, cross-checked with the frozen reader feats
    p = n = g = th = None; msrc = "no_source:no main clause with a finite verb"
    if V:
        p, n, g, th, msrc = verb_morph(V["toks"][V["lex_i"]], L, V["lps"], V["low"])
        if feats:
            rp, rn, rg = feats
            if (rp and p and rp != p) or (rn and n and rn != n):
                msrc += " | CONFLICT with reader feats %s -> null" % (feats,)
                p = n = None
            else:
                p, n = p or rp, n or rn
                g = g or rg
    elif feats:
        p, n, g = feats; msrc = "reader feats (checker_1i.sk_features / f9 l-part)"
    agent_fb = None
    if V and V["fallback_clause"] and (p or n):
        a2, why2 = R._decide_clause(V["toks"], V["low"], (p, n, g), L, "full", m["CK"], V["lps"])
        if a2:
            agent_fb = a2; msrc += " | fallback clause; reader_nom._decide_clause(table feats) found %r (%s)" % (a2, why2)
    out["reader"]["agent_on_fallback_clause"] = agent_fb
    # nominative pronoun / adjective gender (the reader's agent when it is a pronoun)
    gsrc = "l-participle" if g and "l-participle" in msrc else None
    if not g and agent and agent.lower() in R.PRON[L] and R.PRON[L][agent.lower()][2]:
        g, gsrc = R.PRON[L][agent.lower()][2], "nominative pronoun"
    if g and not gsrc:
        gsrc = "reader feats"
    # ---- tense frame (f9, frozen; cz copy with the aspect lexicon)
    fr = m["f9"].sk_frame(text)
    frames = fr["frames"]
    tf = frames[0] if len(frames) == 1 else None
    tense_open = len(frames) > 1
    reason = fr["reason"] or ""
    perf_pres = True if reason.startswith("perfective present") else (
        False if ("imperfective present" in reason or tf in ("past", "conditional")) else None)
    if tf is None and not frames:
        tf_src = "no_source:f9 abstained (%s)" % reason
    else:
        tf_src = "f9.sk_frame: " + reason
    # ---- voice paths
    clauses = V3.split_sk(text)
    v3m = m["V3"]; v2m = m["V2"]
    sk_pass_cl = [bool(v3m.sk_clause_is_passive(c)) for c in clauses]
    sk_refl_cl = [bool(v2m.SK_REFLEX.search(c)) for c in clauses]
    main_cl = info.get("clause")
    main_pass = bool(main_cl and v3m.sk_clause_is_passive(main_cl))
    main_refl = bool(main_cl and v2m.SK_REFLEX.search(main_cl))
    g4raw = NS[L]["g4"](text, {"voice": "active_agent"})          # dummy gold; only the raw readings are kept
    en_hit = EN_PASSIVE_V4(en, True, None)
    impers_tok = [w for w in (V["low"] if V else []) if w in MORPH[L]["impersonal"]]
    impers = bool(impers_tok) or (V is not None and p == "3" and n == "sg" and g == "n" and agent is None
                                  and "l-participle" in msrc)
    why = info.get("why") or ""
    if main_pass:
        voice, vsrc = "passive", "V3.sk_clause_is_passive(main clause): byť + -ný/-tý participle"
    elif agent or agent_fb:
        voice, vsrc = "active_agent", "reader_nom agent = %r (%s)" % (agent or agent_fb, why if agent else "fallback clause")
    elif impers:
        voice, vsrc = "impersonal", "impersonal token %s / 3sg neuter l-participle without nominative" % impers_tok
    elif "1st/2nd person pro-drop" in why:
        voice, vsrc = "active_prodrop", "reader abstain: 1st/2nd person pro-drop"
    elif "reflexive" in why:
        voice, vsrc = None, "abstain: reflexive clause (reflexive-passive vs reflexive verb undecidable)"
    elif "no agreeing nominative" in why and p == "3":
        voice, vsrc = None, "abstain: 3rd person, no nominative found (pro-drop vs missed subject)"
    else:
        voice, vsrc = None, "abstain: " + why
    out["derived"] = {
        "agent_nom": {"value": agent or agent_fb, "source": "reader_nom full" if agent else (
            "reader_nom._decide_clause on derive fallback clause (table feats)" if agent_fb else "reader_nom full abstain: " + why)},
        "finite_verb": {"value": V["toks"][V["lex_i"]] if V else None, "source": "reader_nom._verbish in main clause"},
        "person": {"value": (p + n) if p and n else None, "source": msrc},
        "number": {"value": n, "source": msrc},
        "gender": {"value": g, "source": gsrc or "no_source"},
        "tf": {"value": tf, "source": tf_src, "frames": frames},
        "tense_open": {"value": tense_open if frames else None, "source": "f9.sk_frame frame set size"},
        "perfective_present": {"value": perf_pres,
                               "source": "f9.aspect lexicon via sk_frame reason" if perf_pres is not None else "no_source"},
        "voice_sk": {"value": voice, "source": vsrc},
    }
    out["voice_paths"] = {
        "g4_v2_sk_reflex": g4raw["sk_reflex"], "g4_v3_passive_or_reflex": g4raw["v3_passive_or_reflex"],
        "g4_cz_se_missed": g4raw["czech_se_missed_by_SK_REFLEX"],
        "agv4_sk_clause_passive": sk_pass_cl, "agv4_sk_clause_reflex": sk_refl_cl,
        "agv4_main_passive": main_pass, "agv4_main_reflex": main_refl,
        "agv4_en_passive": en_hit is not None,
        "agv4_en_passive_span": (" ".join(en_hit[2][en_hit[0]:en_hit[1] + 1]) if en_hit else None),
        "reader_nom_full_agent": agent,
    }
    out["rewrite"] = rewrite(row, out, V, p, n, g, voice, main_refl)
    return out


def rewrite(row, o, V, p, n, g, voice, main_refl):
    L, text = row["lang"], row["src"]
    agent = o["reader"]["agent"] or o["reader"].get("agent_on_fallback_clause")
    r = {"action": None, "new": None, "pronoun": None, "where": None, "reason": None, "check": None}
    if agent:
        r.update(action="U", reason="overt subject (reader_nom: %r)" % agent); return r
    if voice in ("passive", "impersonal"):
        r.update(action="U", reason="source is %s" % voice); return r
    if V is None:
        r.update(action="ABSTAIN", reason="no finite verb in a main clause"); return r
    if main_refl:
        r.update(action="ABSTAIN", reason="reflexive clitic in main clause (reflexive passive risk)"); return r
    if p is None:
        r.update(action="ABSTAIN", reason="person undecidable from morphology"); return r
    low = V["low"]
    if p in ("1", "2") and any(x in MORPH[L]["aux_past"] for x in low):
        r.update(action="ABSTAIN", reason="1st/2nd past with auxiliary clitic: one inserted token cannot keep clitic order")
        return r
    ens = en_subject(row["en"])
    en_words = set(re.findall(r"[a-z]+", row["en"].lower()))
    if p in ("1", "2"):
        need = {("1", "sg"): {"i"}, ("1", "pl"): {"we"}, ("2", "sg"): {"you"}, ("2", "pl"): {"you"}}.get((p, n), set())
        if not need & en_words:
            r.update(action="ABSTAIN", reason="%s%s verb but EN has no %s (verb misread risk)" % (p, n, sorted(need)))
            return r
        if n is None:
            r.update(action="ABSTAIN", reason="number undecidable"); return r
        pron = MORPH[L]["pron"][(p, n)]
    else:
        if ens not in ("he", "she", "they"):
            r.update(action="ABSTAIN", reason="3rd person but EN main subject is %r, not he/she/they "
                                             "(post-verbal noun subject / expletive risk)" % ens); return r
        en_n = "pl" if ens == "they" else "sg"
        if n and n != en_n:
            r.update(action="ABSTAIN", reason="number %s vs EN %s" % (n, ens)); return r
        n2 = n or en_n
        gg = g if g and (n2 == "sg" or True) else None
        if n2 == "sg":
            eg = {"he": "m", "she": "f"}[ens]
            if gg and gg != eg:
                r.update(action="ABSTAIN", reason="gender %s vs EN %s" % (gg, ens)); return r
            gg = gg or eg
        elif gg is None:
            r.update(action="ABSTAIN", reason="3pl gender undecidable (oni/ony)"); return r
        pron = MORPH[L]["pron"][("3", n2, gg)]
    # placement: before the finite verb, or before the contiguous clitic/aux cluster right before it
    t = V["toks"]; i = V["vi"]
    while i > 0 and t[i - 1].lower() in MORPH[L]["clitics"]:
        i -= 1
    anchor = t[i]
    # locate the anchor token in the raw source, searching from the main clause start
    cstart = text.find(t[0]) if t[0] in text else 0
    k = i
    pos = cstart
    for j in range(k + 1):
        mm = re.search(r"(?<![\wÀ-ž])" + re.escape(t[j]) + r"(?![\wÀ-ž])", text[pos:])
        if not mm:
            r.update(action="ABSTAIN", reason="anchor not locatable in source"); return r
        at = pos + mm.start(); pos = at + len(t[j])
    at = pos - len(anchor)
    sentence_initial = re.search(r'(^|[.!?…])[\s„"\'«»]*$', text[:at]) is not None
    if sentence_initial:
        new = text[:at] + pron[0].upper() + pron[1:] + " " + anchor[0].lower() + anchor[1:] + text[at + len(anchor):]
    else:
        new = text[:at] + pron + " " + text[at:]
    old_t = [x.lower() for x in R._toks(text)]
    new_t = [x.lower() for x in R._toks(new)]
    ok = len(new_t) == len(old_t) + 1 and any(new_t[:q] + new_t[q + 1:] == old_t and new_t[q] == pron
                                              for q in range(len(new_t)))
    r.update(action="R", new=new, pronoun=pron, where="before %r (%s)" % (anchor, "sentence-initial" if sentence_initial else "token %d of main clause" % i),
             reason="pro-drop %s%s%s" % (p, n or "?", (" " + g) if g else ""), check="PASS" if ok else "FAIL")
    return r


def main():
    rows = json.load(open(os.path.join(HERE, "sample_2b.json"), encoding="utf-8"))["rows"]
    res = [derive(r) for r in rows]
    for o in res:
        o["rewrite"]["sk_new" if o["lang"] == "sk" else "cz_new"] = o["rewrite"].pop("new")
    fb = [o["n"] for o in res if o["rewrite"]["action"] == "ABSTAIN"]
    fields = ["agent_nom", "person", "number", "gender", "tf", "tense_open", "perfective_present", "voice_sk"]
    summ = {"fields": {f: {L: sum(1 for o in res if o["lang"] == L and o["derived"][f]["value"] is not None)
                           for L in ("sk", "cz")} for f in fields}}
    summ["voice_sk_dist"] = dict(collections.Counter((o["lang"], o["derived"]["voice_sk"]["value"]) and
                                                     "%s:%s" % (o["lang"], o["derived"]["voice_sk"]["value"]) for o in res))
    summ["rewrite"] = dict(collections.Counter("%s:%s:%s" % (o["lang"], o["level"], o["rewrite"]["action"]) for o in res))
    summ["machine_check_fail"] = [o["n"] for o in res if o["rewrite"]["check"] == "FAIL"]
    summ["voice_paths"] = {k: {L: sum(1 for o in res if o["lang"] == L and o["voice_paths"][k] is True) for L in ("sk", "cz")}
                           for k in ("g4_v2_sk_reflex", "g4_v3_passive_or_reflex", "g4_cz_se_missed",
                                     "agv4_main_passive", "agv4_main_reflex", "agv4_en_passive")}
    doc = {"generated_by": "phase2b/derive_2b.py", "model_calls": 0,
           "frozen_voice_path": "phase1u/taskA/agent_drop_v4.py decide() -> phase1t/taskA/agent_drop_v3.py decide(V3_BASE); "
                                "Slovak side = V3.sk_clause_is_passive + V2.SK_REFLEX per clause; English side = "
                                "V4._make_find_passive(V3.find_passive); rs_nom (stack_1v.refsubj) needs an answer, not recorded",
           "summary": summ, "model_fallback_ns": fb, "rows": res}
    json.dump(doc, open(os.path.join(HERE, "derived_2b.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(summ, ensure_ascii=False, indent=1))
    print("model_fallback_ns", len(fb))


if __name__ == "__main__":
    main()
