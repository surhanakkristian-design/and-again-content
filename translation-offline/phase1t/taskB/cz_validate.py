#!/usr/bin/env python3
"""Phase 1T / Task B2 - run every deterministic SOURCE-SIDE guard reader UNCHANGED on the 120 Czech
sentences and on their Slovak siblings (control). 0 model calls. ann = {} everywhere, as in production."""
import os, re, sys, json, importlib.util

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.join(BASE, "phase1t", "taskB")
sys.path.insert(0, BASE)


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE, rel))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


f9 = load("f9_1n", "phase1n/f9.py")
CK = load("checker_1i", "phase1i/checker_1i.py")
V2 = load("agent_drop_v2", "phase1s/taskC/agent_drop_v2.py")
try:
    V3 = load("agent_drop_v3", "phase1t/taskA/agent_drop_v3.py")
except Exception as e:                                   # guard 3: v3 may not exist
    V3, V3ERR = None, repr(e)
else:
    V3ERR = None
SJ = load("safe_json", "phase1s/safe_json.py")

rows = json.load(open(os.path.join(HERE, "cz_sample_numbered.json"), encoding="utf-8"))
czg = {g["n"]: g for g in json.load(open(os.path.join(HERE, "cz_gold.json"), encoding="utf-8"))}
skg = {g["n"]: g for g in json.load(open(os.path.join(HERE, "sk_gold.json"), encoding="utf-8"))}

WORD = re.compile(r"[a-záäčďéěíĺľňóôöŕřšťúůüýž]+", re.I)
# Czech nouns/adjectives that end like an l-participle and are NOT in f9.L_NONVERB (Slovak list)
CZ_L_NOUNS = set("""stůl stolu úhel úhlu kotel kotle popel popela orel orla posel posla duben dubna hotel
motel model panel tunel kabel bicykl anděl kanál materiál obal email koktejl gól styl cíl díl kartel
zrcadlo jídlo světlo číslo křeslo sedlo máslo heslo křídlo čelo tělo kolo pravidlo divadlo mýdlo sklo
hrdlo dílo vlákno škola chvíle síla vila jehla metla skála cihla koule tabule postel sůl role židle
sedmdesát""".split())
INSTR = re.compile(r"(em)$", re.I)


def words(s):
    return WORD.findall((s or "").lower())


def gold_subj_words(g):
    out = set()
    for s in ([g.get("subject")] + list(g.get("embedded_agents") or [])):
        if s:
            out |= set(words(s))
    return out


def main_subj_words(g):
    return set(words(g.get("subject") or ""))


# ----------------------------------------------------------------- guard 1: F9 time frame
def g1(text, g):
    got = f9.sk_frame(text)
    S = set(got["frames"])
    G = set() if g["tf"] == "none" else {g["tf"]}
    if not S:
        cls = "CONSERVATIVE"
    elif S == G:
        cls = "AGREE"
    elif G <= S:
        cls = "CONSERVATIVE"
    else:
        cls = "ERROR"
    # which tokens f9 read as l-participles (the :85-86 exception-list risk)
    tt = f9.tok(text)
    lp = [w for i, w in enumerate(tt) if f9._is_l_part(tt, i)]
    return {"frames": sorted(S), "gold": g["tf"], "class": cls, "reason": got["reason"],
            "assert_on_gold_none": bool(S and not G), "l_parts": lp,
            "cz_noun_read_as_participle": sorted(set(lp) & CZ_L_NOUNS)}


# ----------------------------------------------------------------- guard 2: F4v2 person/number
def g2(text, g):
    feats, sigs = CK.sk_features(text)
    p, n = feats["person"], feats["number"]
    gp = gn = None
    if g["person"] != "none":
        gp, gn = g["person"][0], g["person"][1:]
    if p is None and n is None:
        cls = "CONSERVATIVE"
    elif gp is None:
        cls = "ERROR"                                   # asserts person where gold has no finite verb
    elif (p and p != gp) or (n and n != gn):
        cls = "ERROR"
    else:
        cls = "AGREE"
    instr = [s for s in sigs if s.startswith("present -m ")
             and INSTR.search(s.split()[-1]) and not s.split()[-1].endswith(("ím", "ám", "iem"))]
    return {"person": p, "number": n, "gender": feats["gender"], "gold": g["person"],
            "class": cls, "signals": sigs, "instrumental_em_signals": instr,
            "partial": bool(cls == "AGREE" and (p is None or n is None))}


# ----------------------------------------------------------------- guard 3: AG nominative-agent reader
def g3(text, g, mod):
    agent, kind, src = V2.slovak_agent(text, {}, {})
    toks_ = [agent] if agent else []
    if mod is V3 and V3 is not None and agent:
        toks_, kind = V3.parse_agent_tokens(agent)
    gold_main = main_subj_words(g)
    gold_all = gold_subj_words(g)
    low = {t.lower().strip(".,!?;:„“\"'") for t in toks_ if t}
    if not agent:
        cls = "CONSERVATIVE" if gold_main else "AGREE"
    elif not gold_all:
        cls = "ERROR"
    elif low & gold_main:
        cls = "AGREE"
    elif low & gold_all:
        cls = "ERROR"                                   # embedded agent read as the main-clause agent
    else:
        cls = "ERROR"
    return {"agent": agent, "tokens": toks_, "kind": kind, "source": src, "class": cls,
            "gold_subject": g.get("subject"), "gold_agent_nom": g.get("agent_nom"),
            "gold_embedded": g.get("embedded_agents")}


# ----------------------------------------------------------------- guard 4: passive / reflexive / subjectless
NONACTIVE = ("passive", "reflexive_passive", "impersonal")


def g4(text, g):
    reflex = bool(V2.SK_REFLEX.search(text or ""))
    v3pass = None
    if V3 is not None:
        cls_ = V3.split_sk(text)
        v3pass = any(V3.sk_clause_is_passive(c) for c in cls_) or any(
            V2.SK_REFLEX.search(c) for c in cls_)
    gold_na = g["voice"] in NONACTIVE
    def verdict(det):
        if det is None:
            return None
        if gold_na and not det:
            return "ERROR_as_active"
        if (not gold_na) and det and g["voice"] == "active_agent":
            return "ERROR_as_passive"
        return "AGREE"
    has_se = bool(re.search(r"(^|\s)se(\s|[.,!?]|$)", text or "", re.I))
    return {"sk_reflex": reflex, "v3_passive_or_reflex": v3pass, "gold_voice": g["voice"],
            "class_v2": verdict(reflex), "class_v3": verdict(v3pass),
            "czech_se_missed_by_SK_REFLEX": bool(has_se and not reflex)}


# ----------------------------------------------------------------- end to end: AG on the EN reference
def e2e(text, g, en):
    res = {}
    ann_gold = {"voice_sk": g["voice"], "agent_nom": g["agent_nom"]}
    for tag, mod in (("v2", V2), ("v3", V3)):
        if mod is None:
            continue
        for lbl, ann in (("ann_empty", {}), ("ann_gold", ann_gold)):
            try:
                d = mod.decide(text, ann, {}, en, en, "primary")
                res["%s_%s" % (tag, lbl)] = {"fired": bool(d.get("fired")), "reason": d.get("reason"),
                                             "agent": d.get("agent")}
            except Exception as ex:
                res["%s_%s" % (tag, lbl)] = {"fired": None, "reason": "CRASH " + repr(ex)}
    return res


out = []
for r in rows:
    n = r["n"]
    rec = {"n": n, "level": r["level"], "en": r["en"]}
    for lang in ("cz", "sk"):
        text = r[lang]
        g = (czg if lang == "cz" else skg)[n]
        rec[lang] = {"text": text, "gold": g, "g1": g1(text, g), "g2": g2(text, g),
                     "g3_v2": g3(text, g, V2), "g3_v3": g3(text, g, V3) if V3 else None,
                     "g4": g4(text, g), "e2e": e2e(text, g, r["en"])}
    out.append(rec)


def counts(key, sub, langs=("cz", "sk"), skip_frag=False):
    c = {}
    for lang in langs:
        d = {}
        for rec in out:
            if skip_frag and rec[lang]["gold"].get("fragment"):
                continue
            v = rec[lang][key]
            if v is None:
                continue
            k = v[sub]
            if k is None:
                continue
            d[k] = d.get(k, 0) + 1
        c[lang] = d
    return c


summary = {
    "n": len(out),
    "fragments": {l: sum(1 for r in out if r[l]["gold"].get("fragment")) for l in ("cz", "sk")},
    "g1_f9": counts("g1", "class"), "g1_f9_nofrag": counts("g1", "class", skip_frag=True),
    "g1_assert_on_gold_none": {l: sum(1 for r in out if r[l]["g1"]["assert_on_gold_none"]) for l in ("cz", "sk")},
    "g2_f4v2": counts("g2", "class"), "g2_f4v2_nofrag": counts("g2", "class", skip_frag=True),
    "g2_partial_agree": {l: sum(1 for r in out if r[l]["g2"]["partial"]) for l in ("cz", "sk")},
    "g3_v2": counts("g3_v2", "class"), "g3_v3": counts("g3_v3", "class") if V3 else None,
    "g4_v2": counts("g4", "class_v2"), "g4_v3": counts("g4", "class_v3"),
    "v3_present": V3 is not None, "v3_import_error": V3ERR,
}
for k in ("v2_ann_empty", "v3_ann_empty", "v2_ann_gold", "v3_ann_gold"):
    summary.setdefault("e2e_rejections", {})[k] = {
        l: sorted(r["n"] for r in out if (r[l]["e2e"].get(k) or {}).get("fired")) for l in ("cz", "sk")}
    summary.setdefault("e2e_crashes", {})[k] = {
        l: sorted(r["n"] for r in out if (r[l]["e2e"].get(k) or {}).get("fired") is None) for l in ("cz", "sk")}

probes = {
    "f9_l_noun_misfire": {l: [(r["n"], r[l]["g1"]["cz_noun_read_as_participle"], r[l]["g1"]["frames"],
                               r[l]["gold"]["tf"]) for r in out if r[l]["g1"]["cz_noun_read_as_participle"]]
                          for l in ("cz", "sk")},
    "f4v2_instrumental_em": {l: [(r["n"], r[l]["g2"]["instrumental_em_signals"], r[l]["g2"]["person"],
                                  r[l]["g2"]["number"], r[l]["gold"]["person"], r[l]["g2"]["class"])
                                 for r in out if r[l]["g2"]["instrumental_em_signals"]] for l in ("cz", "sk")},
    "reflex_se_missed": {l: [(r["n"], r[l]["gold"]["voice"]) for r in out
                             if r[l]["g4"]["czech_se_missed_by_SK_REFLEX"]] for l in ("cz", "sk")},
}
summary["probes"] = probes

errors = {}
for guard, key, sub in (("g1", "g1", "class"), ("g2", "g2", "class"), ("g3_v2", "g3_v2", "class"),
                        ("g3_v3", "g3_v3", "class"), ("g4_v2", "g4", "class_v2"), ("g4_v3", "g4", "class_v3")):
    for lang in ("cz", "sk"):
        lst = []
        for r in out:
            v = r[lang][key]
            if v and str(v.get(sub, "")).startswith("ERROR"):
                lst.append({"n": r["n"], "text": r[lang]["text"], "class": v[sub],
                            "gold": r[lang]["gold"], "guard": v})
        errors["%s_%s" % (guard, lang)] = lst
summary["error_counts"] = {k: len(v) for k, v in errors.items()}

SJ.safe_dump({"summary": summary, "errors": errors, "rows": out},
             os.path.join(HERE, "cz_validation.json"), indent=1)
print(json.dumps(summary, ensure_ascii=False, indent=1))
print("---- ERROR SAMPLES ----")
for k, v in errors.items():
    if not v:
        continue
    print("##", k, len(v))
    for e in v[:40]:
        gg = e["gold"]
        print("  n=%-3d %s | gold tf=%s person=%s voice=%s subj=%r | guard=%s" % (
            e["n"], e["text"][:90], gg["tf"], gg["person"], gg["voice"], gg.get("subject"),
            {kk: vv for kk, vv in e["guard"].items() if kk in
             ("frames", "person", "number", "agent", "tokens", "sk_reflex", "v3_passive_or_reflex",
              "signals", "reason")}))
