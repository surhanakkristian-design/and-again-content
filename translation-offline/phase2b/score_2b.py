#!/usr/bin/env python3
"""Phase 2B SCORE (0 model calls): every field vs the blind gold, exact 95 % Clopper-Pearson, pooled + per language.
Inputs: sample_2b.json, derived_2b.json, alt_map_2b.json, selection_2b_summary.json, run_2b_results.json.
Guards imported exactly as derive_2b.py does (frozen code, never edited); g4 run as phase2a/run_2a.py did
(reader_nom 'full' installed). Output: results_2b.json."""
import os, re, sys, json, math, collections
sys.dont_write_bytecode = True
BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
H = os.path.join(BASE, "phase2b")
for p in (os.path.join(BASE, "phase1w"), os.path.join(BASE, "phase1v", "trackC")):
    sys.path.insert(0, p)
import stack_1w as SW                                   # noqa: E402
import reader_nom as R                                  # noqa: E402
import cz_reader as CZR                                 # noqa: E402
V4 = SW.S.V4; V3 = SW.S.V3
V2 = V3.V2 if hasattr(V3, "V2") else sys.modules["agent_drop_v2"]
SKM = R.sk_mods(); SKM = {"f9": SKM["f9"], "CK": SKM["CK"], "V2": V2, "V3": V3}
CZM = CZR.build()
MODS = {"sk": SKM, "cz": CZM}
SRC = open(os.path.join(BASE, "phase1t/taskB/cz_validate.py"), encoding="utf-8").read()
GSLICE = SRC[SRC.index("WORD = re.compile"):SRC.index("\nout = []")]
NS = {}
for L, m in MODS.items():
    ns = {"re": re, "json": json, "os": os, "f9": m["f9"], "CK": m["CK"], "V2": m["V2"], "V3": m["V3"]}
    exec(GSLICE, ns); NS[L] = ns
WORD = re.compile(r"[a-záäčďéěíĺľňóôöŕřšťúůüýž]+", re.I)
words = lambda s: set(WORD.findall((s or "").lower()))

def g3cls(agent, g, v3m):                                # verbatim logic of phase2a/run_2a.py g3cls
    toks_ = v3m.parse_agent_tokens(agent)[0] if agent else []
    gm = words(g.get("subject")); ga = set(gm)
    for e in (g.get("embedded_agents") or []):
        ga |= words(e)
    low = {x.lower().strip(".,!?;:„“\"'") for x in toks_ if x}
    if not agent:
        return "CONSERVATIVE" if gm else "AGREE"
    if not ga:
        return "ERROR"
    return "AGREE" if low & gm else "ERROR"

def cp(k, n, a=0.05):                                    # copied from 2A
    if n == 0: return [None, None]
    def cdf(x, p): return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(x + 1))
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid): lo = mid
            else: hi = mid
        return (lo + hi) / 2
    lo = 0.0 if k == 0 else bis(lambda p: 1 - cdf(k - 1, p) < a / 2)
    hi = 1.0 if k == n else bis(lambda p: cdf(k, p) > a / 2)
    return [round(100 * lo, 2), round(100 * hi, 2)]
def rate(k, n): return {"k": k, "n": n, "pct": round(100 * k / n, 2) if n else None, "cp95": cp(k, n)}

def gold_full(g):
    g = dict(g); g.setdefault("embedded_agents", []); g.setdefault("fragment", False)
    g["subject_explicit"] = g.get("subject") is not None; g["agent_nom"] = g.get("voice") == "active_agent"; g["tf_note"] = ""
    return g
def gold_after(g, w):
    ga = json.loads(json.dumps(g))
    if w.get("action") == "R" and w.get("machine_check"):
        if w.get("where") == "main" and g.get("voice") == "active_prodrop":
            ga.update(subject=w["pronoun"], subject_explicit=True, voice="active_agent", agent_nom=True)
        elif w.get("where") == "embedded":
            ga["embedded_agents"] = list(ga.get("embedded_agents") or []) + [w["pronoun"]]
    return ga
def toks(s): return [w.lower() for w in re.findall(r"\w+", s or "")]
def machine_check(old, new, pron):
    a, b = toks(old), toks(new or old); ok = True
    for t in a:
        if t in b: b.remove(t)
        else: ok = False
    return ok and b == [str(pron or "").lower()]
MULTI = re.compile(r"[.!?…]\s+\S")
def multi(t): return bool(MULTI.search((t or "").strip()))

S = json.load(open(f"{H}/sample_2b.json", encoding="utf-8"))
ROWS = S["rows"]; BY = {r["n"]: r for r in ROWS}
D = json.load(open(f"{H}/derived_2b.json", encoding="utf-8")); DR = {r["n"]: r for r in D["rows"]}
AL = json.load(open(f"{H}/alt_map_2b.json", encoding="utf-8"))
SEL = json.load(open(f"{H}/selection_2b_summary.json", encoding="utf-8"))
RUN = json.load(open(f"{H}/run_2b_results.json", encoding="utf-8"))
OUT = RUN["outputs"]
GOLD = {**{int(k): v for k, v in OUT["gold_sk"].items()}, **{int(k): v for k, v in OUT["gold_cz"].items()}}
LANGS = ["sk", "cz"]; LEVELS = ["A1", "A2", "B1", "B2"]
def by_lang(fn):                                         # fn(rows) -> (k, n) ; returns pooled + per lang
    out = {}
    for tag, rs in (("pooled", ROWS), ("sk", [r for r in ROWS if r["lang"] == "sk"]), ("cz", [r for r in ROWS if r["lang"] == "cz"])):
        out[tag] = rate(*fn(rs))
    return out
RES = {"model_calls": 0, "gold_returned": len(GOLD), "caveat": "gold = same model family (Opus) as every model-authored field: self-consistency, not independent accuracy"}
nrm = lambda x: None if x is None else str(x).strip().lower()

# ---------------------------------------------------------------- gold meta
RES["gold_meta"] = {L: {"fragment": sum(1 for r in ROWS if r["lang"] == L and (GOLD.get(r["n"]) or {}).get("fragment")),
                        "multi_sentence_src": sum(1 for r in ROWS if r["lang"] == L and multi(r["src"])),
                        "main_sentence_index_gt0": sum(1 for r in ROWS if r["lang"] == L and ((GOLD.get(r["n"]) or {}).get("main_sentence_index") or 0) > 0),
                        "voice": dict(collections.Counter(str((GOLD.get(r["n"]) or {}).get("voice")) for r in ROWS if r["lang"] == L)),
                        "missing": [r["n"] for r in ROWS if r["lang"] == L and r["n"] not in GOLD]} for L in LANGS}

# ---------------------------------------------------------------- 2.1 lk
LKJ = {int(k): v for k, v in OUT["lk_judge"].items()}
lk = {"judge": {}, "mechanical": {}, "cross": collections.Counter(), "by_level": {}, "missing": [r["n"] for r in ROWS if r["n"] not in LKJ]}
for r in ROWS:
    j = (LKJ.get(r["n"]) or {}).get("class", "missing")
    mech = "substring" if r["correct_answer_en"] and r["correct_answer_en"] in r["en"] else (
        "substring_ci" if r["correct_answer_en"] and r["correct_answer_en"].lower() in r["en"].lower() else "not_substring")
    for tag in ("pooled", r["lang"]):
        lk["judge"].setdefault(tag, collections.Counter())[j] += 1
        lk["mechanical"].setdefault(tag, collections.Counter())[mech] += 1
    lk["by_level"].setdefault(r["level"], collections.Counter())[j] += 1
    lk["cross"][f"{j}|{mech}"] += 1
    if j == "adjust" and (LKJ[r["n"]].get("lk") or "") not in r["en"]: lk.setdefault("adjust_span_not_in_en", []).append(r["n"])
lk["judge_rates"] = {tag: {c: rate(v, sum(cnt.values())) for c, v in cnt.items()} for tag, cnt in lk["judge"].items()}
lk["examples_non_exact"] = [[r["n"], r["en"][:80], r["correct_answer_en"], LKJ.get(r["n"], {}).get("class"), LKJ.get(r["n"], {}).get("lk")]
                            for r in ROWS if LKJ.get(r["n"], {}).get("class") != "exact"][:12]
RES["2.1_lk"] = json.loads(json.dumps(lk))

# ---------------------------------------------------------------- 2.2 topic + level coverage
RES["2.2_topic_level"] = {"rows": len(ROWS), "type_missing": sum(1 for r in ROWS if r.get("type_missing") or not r.get("type_title")),
                          "level_missing": sum(1 for r in ROWS if not r.get("level")),
                          "types_covered_in_sample": S.get("exercise_types_covered"),
                          "selection_topics": {L: {k: v for k, v in SEL["topics_per_level"][L].items() if k != "per_topic"} for L in SEL.get("topics_per_level", {})}}

# ---------------------------------------------------------------- 2.3 derived fields vs gold
FIELDS = {"voice_sk": "voice", "agent_nom": "subject", "person": "person", "number": "number", "gender": "gender",
          "tf": "tf", "tense_open": "tense_open", "perfective_present": "perfective_present"}
f23 = {}; f23_err = {}
for f, gk in FIELDS.items():
    cls = {}
    for r in ROWS:
        g = GOLD.get(r["n"])
        if not g: continue
        dvv = DR[r["n"]]["derived"][f]["value"]
        if dvv is None: c = "CONSERVATIVE"
        elif f == "agent_nom":
            c = "AGREE" if (words(dvv) & words(g.get("subject"))) else "ERROR"
        elif f in ("tense_open", "perfective_present"):
            c = "AGREE" if bool(dvv) == bool(g.get(gk)) else "ERROR"
        else:
            c = "AGREE" if nrm(dvv) == nrm(g.get(gk)) else "ERROR"
        cls[r["n"]] = c
        if c == "ERROR": f23_err.setdefault(f, []).append([r["n"], r["src"][:70], dvv, g.get(gk), "multi" if multi(r["src"]) else ""])
    blk = {}
    for tag in ("pooled", "sk", "cz"):
        ns_ = [n for n in cls if tag == "pooled" or BY[n]["lang"] == tag]
        cnt = collections.Counter(cls[n] for n in ns_); dec = cnt["AGREE"] + cnt["ERROR"]
        blk[tag] = {"counts": dict(cnt), "n": len(ns_), "ERROR_of_all": rate(cnt["ERROR"], len(ns_)),
                    "ERROR_of_decided": rate(cnt["ERROR"], dec), "coverage_decided": rate(dec, len(ns_)),
                    "ERROR_multi_sentence": sum(1 for n in ns_ if cls[n] == "ERROR" and multi(BY[n]["src"]))}
    f23[f] = blk
RES["2.3_fields"] = f23; RES["2.3_errors"] = {k: v[:15] for k, v in f23_err.items()}
RES["2.3_reference"] = "1W §2.2 blind Slovak reader error 1.67 %; 2A §3 reader_nom 3-4 %"

# ---------------------------------------------------------------- 2.4 alt
RES["2.4_alt"] = {"overall": AL["overall"], "by_level": AL["by_level"], "by_lang": AL["by_lang"], "rows_with_any_mapped": AL.get("rows_with_any_mapped"),
                  "note": "rough match: surface word/lemma in a group, sense not checked"}

# ---------------------------------------------------------------- 2.5 v cost + decomposition
SES = {m["session"]: m for m in RUN["sessions"] if m.get("exit") == 0 and not m.get("result_unparsable")}
def tot(m): return sum(m.get(k) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))
# fit cache_creation = a + b * (head+rows chars) over all successful sessions (fixed system context vs tokens/char)
pts = [(RUN["chars"][k]["head"] + RUN["chars"][k]["rows"], SES[k]["cache_creation_input_tokens"] + SES[k]["input_tokens"]) for k in SES if k in RUN["chars"]]
mx = sum(x for x, _ in pts) / len(pts); my = sum(y for _, y in pts) / len(pts)
b = sum((x - mx) * (y - my) for x, y in pts) / (sum((x - mx) ** 2 for x, _ in pts) or 1); a = my - b * mx
def decomp(k):
    m = SES[k]; n = RUN["rows_per_session"][k]
    head_t = b * RUN["chars"][k]["head"]; rows_t = b * RUN["chars"][k]["rows"]
    fixed_nc = a + head_t; fixed_all = fixed_nc + m["cache_read_input_tokens"]
    marg = rows_t / n + m["output_tokens"] / n
    return {"N": n, "all": tot(m), "per_sent_all": round(tot(m) / n, 1), "per_sent_excl_cache_read": round((tot(m) - m["cache_read_input_tokens"]) / n, 1),
            "per_sent_output": round(m["output_tokens"] / n, 1), "cache_read": m["cache_read_input_tokens"], "cache_creation": m["cache_creation_input_tokens"],
            "output": m["output_tokens"], "duration_s": round((m.get("duration_ms") or 0) / 1000, 1), "usd": m.get("total_cost_usd"),
            "fixed_all_est": round(fixed_all), "fixed_excl_cache_read_est": round(fixed_nc), "marginal_per_sent_est": round(marg, 1),
            "N30_per_sent_all_ESTIMATE": round(fixed_all / 30 + marg, 1), "N30_per_sent_excl_cache_read_ESTIMATE": round(fixed_nc / 30 + marg, 1),
            "N30_s_per_sent_ESTIMATE": round((m.get("duration_ms") or 0) / 1000 / n, 2)}
DEC = {k: decomp(k) for k in SES}
vk = [k for k in ("v_sk", "v_cz") if k in DEC]
vtot = sum(DEC[k]["all"] for k in vk); vn = sum(DEC[k]["N"] for k in vk)
v_all = round(vtot / vn, 1); v_nc = round(sum(DEC[k]["all"] - DEC[k]["cache_read"] for k in vk) / vn, 1)
v30 = round(sum(DEC[k]["N30_per_sent_all_ESTIMATE"] for k in vk) / len(vk), 1); v30nc = round(sum(DEC[k]["N30_per_sent_excl_cache_read_ESTIMATE"] for k in vk) / len(vk), 1)
RES["2.5_v"] = {"sessions": vk, "per_sent_all_N100": v_all, "per_sent_excl_cache_read_N100": v_nc,
                "per_sent_output_N100": round(sum(DEC[k]["output"] for k in vk) / vn, 1),
                "N30_per_sent_all_ESTIMATE": v30, "N30_per_sent_excl_cache_read_ESTIMATE": v30nc,
                "share_of_2A_1611.8": round(v_all / 1611.8, 3), "share_of_2A_713.3_excl": round(v_nc / 713.3, 3),
                "N30_share_of_2A_1611.8_ESTIMATE": round(v30 / 1611.8, 3), "N30_share_of_2A_713.3_ESTIMATE": round(v30nc / 713.3, 3),
                "fit": {"a_fixed_creation_tokens": round(a), "b_tokens_per_char": round(b, 4), "points": pts}}
V = {int(k): v for k in vk for k, v in OUT[k].items()}
RES["2.5_v"]["v0_is_reference"] = sum(1 for n, o in V.items() if (o.get("v") or [None])[0] == BY[n]["en"])
RES["2.5_v"]["returned"] = len(V); RES["2.5_v"]["two_variants"] = sum(1 for o in V.values() if len(o.get("v") or []) > 1)
RES["2.5_v"]["lk0_equals_supplied"] = sum(1 for n, o in V.items() if (o.get("lk") or [None])[0] == BY[n]["correct_answer_en"])
RES["session_decomposition"] = DEC

# ---------------------------------------------------------------- 2.6 rewrite
PRON = {"ja": ("1sg", None), "já": ("1sg", None), "ty": ("2sg", None), "on": ("3sg", "m"), "ona": ("3sg", "f"), "ono": ("3sg", "n"),
        "my": ("1pl", None), "vy": ("2pl", None), "oni": ("3pl", "m"), "ony": ("3pl", "f")}
MF = {int(k): v for k, v in OUT["rewrite_fallback"].items()}
def pron_ok(p, g):
    pp = PRON.get(str(p or "").lower())
    if not pp: return False
    if nrm(g.get("person")) != pp[0]: return False
    return pp[1] is None or g.get("gender") is None or nrm(g.get("gender")) == pp[1]
rw = {"script": {}, "model": {}, "errors_script": [], "errors_model": []}
W = {}
for r in ROWS:
    n, L = r["n"], r["lang"]; g = GOLD.get(n); sr = DR[n]["rewrite"]; act = sr["action"]
    if act in ("R", "U"):
        w = {"action": act, "pronoun": sr.get("pronoun"), "where": "main" if act == "R" else None,
             "machine_check": sr.get("check") == "PASS", "text": sr.get(f"{L}_new") if act == "R" and sr.get("check") == "PASS" else r["src"], "by": "script"}
        if g:
            if act == "R": c = "AGREE" if g.get("voice") == "active_prodrop" and pron_ok(sr.get("pronoun"), g) else "ERROR"
            else: c = "AGREE" if g.get("voice") != "active_prodrop" else "ERROR"
            for tag in ("pooled", L):
                rw["script"].setdefault(tag, collections.Counter())[f"{act}:{c}"] += 1
            if c == "ERROR": rw["errors_script"].append([n, act, r["src"][:70], sr.get("pronoun"), g.get("voice"), g.get("person"), g.get("gender")])
    else:
        o = MF.get(n, {"action": "U", "missing": True})
        mc = o.get("action") == "R" and machine_check(r["src"], o.get("sk_new"), o.get("pronoun"))
        w = {"action": o.get("action"), "pronoun": o.get("pronoun"), "where": o.get("where"), "machine_check": mc,
             "text": o.get("sk_new") if mc else r["src"], "by": "model", "missing": o.get("missing", False)}
        if g:
            if o.get("action") == "R" and o.get("where") == "main":
                c = "AGREE" if g.get("voice") == "active_prodrop" and pron_ok(o.get("pronoun"), g) else "ERROR"
            else: c = "AGREE" if g.get("voice") != "active_prodrop" else "ERROR"
            key = f"{o.get('action')}{'_' + str(o.get('where')) if o.get('action') == 'R' else ''}:{c}"
            for tag in ("pooled", L):
                rw["model"].setdefault(tag, collections.Counter())[key] += 1
                rw["model"].setdefault(tag + "_machine_check_fail", collections.Counter())["fail" if o.get("action") == "R" and not mc else "ok"] += 1
            if c == "ERROR": rw["errors_model"].append([n, o.get("action"), o.get("where"), r["src"][:70], o.get("pronoun"), g.get("voice"), g.get("person")])
    W[n] = w
def acc(cnt):
    e = sum(v for k, v in cnt.items() if k.endswith(":ERROR")); t = sum(v for k, v in cnt.items() if ":" in k)
    return {"ERROR": rate(e, t), "AGREE": rate(t - e, t)}
rw["script_acc"] = {t: acc(c) for t, c in rw["script"].items()}
rw["model_acc"] = {t: acc(c) for t, c in rw["model"].items() if not t.endswith("fail")}
rw["handled"] = {L: dict(collections.Counter(DR[r["n"]]["rewrite"]["action"] for r in ROWS if r["lang"] == L)) for L in LANGS}
fb = SES.get("rewrite_fallback")
rw["fallback_tokens"] = tot(fb) if fb else None
rw["tokens_per_sent_over_200"] = round(tot(fb) / 200, 1) if fb else None
rw["tokens_per_fallback_row"] = round(tot(fb) / 97, 1) if fb else None
rw["N30_per_fallback_row_ESTIMATE"] = DEC["rewrite_fallback"]["N30_per_sent_all_ESTIMATE"] if fb else None
rw["N30_per_sent_over_all_ESTIMATE"] = round(DEC["rewrite_fallback"]["N30_per_sent_all_ESTIMATE"] * 97 / 200, 1) if fb else None
rw["vs_2A_1264.5"] = round(tot(fb) / 200 / 1264.5, 3) if fb else None
rw["model_R_applied"] = sum(1 for w in W.values() if w["by"] == "model" and w["action"] == "R" and w["machine_check"])
rw["model_R_machine_fail"] = [n for n, w in W.items() if w["by"] == "model" and w["action"] == "R" and not w["machine_check"]]
RES["2.6_rewrite"] = json.loads(json.dumps(rw))

# ---------------------------------------------------------------- §3 g4 / AG v4 / reader_nom
SIREF = re.compile(r"\b(si|sa|se)\b", re.I)
def g4_run(L, text, g):
    ctx = R.installed(V2, "sk", "full") if L == "sk" else R.installed(CZM["V2"], "cz", "full", CZM)
    with ctx:
        try:
            o = NS[L]["g4"](text, g); return o["class_v2"], o["class_v3"]
        except Exception as ex:
            return "CRASH " + repr(ex)[:60], "CRASH " + repr(ex)[:60]
def cause(text, g):
    if SIREF.search(text) and g.get("subject"): return "reflexive_si_sa_se_with_overt_nominative"
    if multi(text): return "multi_sentence"
    return "other"
per = {}; errs = []
for r in ROWS:
    n, L = r["n"], r["lang"]; g = GOLD.get(n)
    if not g: continue
    g0 = gold_full(g); w = W[n]; g1 = gold_after(g0, w)
    cl = {}
    cl["before:g4_v2"], cl["before:g4_v3"] = g4_run(L, r["src"], g0)
    cl["after:g4_v2"], cl["after:g4_v3"] = g4_run(L, w["text"], g1)
    vp = DR[n]["voice_paths"]; reads_pass = bool(vp.get("agv4_main_passive") or vp.get("agv4_main_reflex"))
    gv = g0.get("voice")
    if gv in ("active_agent", "active_prodrop") and reads_pass: cl["before:agv4"] = "ERROR_as_passive"
    elif gv == "passive" and not reads_pass: cl["before:agv4"] = "ERROR_as_active"
    else: cl["before:agv4"] = "AGREE"
    m = MODS[L]
    try: cl["before:reader_nom_full"] = g3cls(R.read(r["src"], L, "full", m)[0], g0, m["V3"])
    except Exception as ex: cl["before:reader_nom_full"] = "CRASH " + repr(ex)[:60]
    try: cl["after:reader_nom_full"] = g3cls(R.read(w["text"], L, "full", m)[0], g1, m["V3"])
    except Exception as ex: cl["after:reader_nom_full"] = "CRASH " + repr(ex)[:60]
    for k, c in cl.items():
        key = "ERROR" if str(c).startswith(("ERROR", "CRASH")) else str(c)
        for tag in ("pooled", L):
            per.setdefault(k, {}).setdefault(tag, collections.Counter())[key] += 1
        if key == "ERROR":
            txt = r["src"] if k.startswith("before") else w["text"]
            errs.append({"n": n, "lang": L, "guard": k, "class": str(c)[:40], "cause": cause(txt, g0 if k.startswith("before") else g1),
                         "multi": multi(txt), "text": txt[:90], "gold_voice": gv, "gold_subject": g.get("subject")})
S3 = {}
for k, t in per.items():
    S3[k] = {}
    for tag, cnt in t.items():
        nn = sum(cnt.values())
        S3[k][tag] = {"counts": dict(cnt), "n": nn, "ERROR": rate(cnt["ERROR"], nn),
                      "error_causes": dict(collections.Counter(e["cause"] for e in errs if e["guard"] == k and (tag == "pooled" or e["lang"] == tag))),
                      "error_classes": dict(collections.Counter(e["class"] for e in errs if e["guard"] == k and (tag == "pooled" or e["lang"] == tag)))}
RES["3_guards"] = S3; RES["3_errors"] = errs
RES["3_reference"] = {"2A_before": {"g4_v2": 15.0, "g4_v3": 16.0, "reader_nom_full": 3.0}, "2A_after": {"g4_v2": 24.0, "g4_v3": 25.0, "reader_nom_full": 4.0},
                      "1W": {"SKP_coverage": 97.22, "by_passive_coverage": 98.75}, "agv4_after": "not computed (derived voice path read on raw text only)"}

# ---------------------------------------------------------------- residual nulls (for the v-session ESTIMATE)
nulls = collections.Counter(); nn = 0
for r in ROWS:
    nn += 1
    for f in FIELDS: nulls[f] += DR[r["n"]]["derived"][f]["value"] is None
gold_out_per_field = (DEC["gold_sk"]["per_sent_output"] + DEC["gold_cz"]["per_sent_output"]) / 2 / 12 if "gold_sk" in DEC and "gold_cz" in DEC else None
RES["residual_nulls"] = {"per_field": dict(nulls), "per_sentence_avg": round(sum(nulls.values()) / nn, 2),
                         "gold_output_tokens_per_field_ESTIMATE": round(gold_out_per_field, 1) if gold_out_per_field else None,
                         "ride_in_v_output_per_sentence_ESTIMATE": round(sum(nulls.values()) / nn * gold_out_per_field, 1) if gold_out_per_field else None}
RES["headless"] = {"tokens_total": RUN["tokens_headless_total"], "sessions": [[m["session"], m["attempt"], m["exit"], tot(m)] for m in RUN["sessions"]],
                   "refused": RUN["refused"], "stop": RUN["stop"]}
json.dump(RES, open(f"{H}/results_2b.json", "w"), ensure_ascii=False, indent=1, default=dict)

# ---------------------------------------------------------------- compact print
P = lambda *a: print(*a, flush=True)
P("GOLD", RES["gold_returned"], json.dumps(RES["gold_meta"], ensure_ascii=False))
P("LK", json.dumps({t: dict(c) for t, c in lk["judge"].items()}), json.dumps({t: dict(c) for t, c in lk["mechanical"].items()}), dict(lk["cross"]), {L: dict(c) for L, c in lk["by_level"].items()}, "adjust_not_in_en", lk.get("adjust_span_not_in_en"))
P("LKEX", json.dumps(lk["examples_non_exact"][:6], ensure_ascii=False))
P("TOPIC", json.dumps(RES["2.2_topic_level"])[:400])
for f, blk in f23.items():
    P("F", f, *[f"{t}:{blk[t]['counts']} Eall={blk[t]['ERROR_of_all']['pct']}{blk[t]['ERROR_of_all']['cp95']} Edec={blk[t]['ERROR_of_decided']['pct']}{blk[t]['ERROR_of_decided']['cp95']} cov={blk[t]['coverage_decided']['pct']} multi={blk[t]['ERROR_multi_sentence']}" for t in ("pooled", "sk", "cz")])
P("FERR", json.dumps({k: v[:4] for k, v in f23_err.items()}, ensure_ascii=False)[:2500])
P("V", json.dumps({k: v for k, v in RES["2.5_v"].items() if k != "fit"}), "fit a,b", RES["2.5_v"]["fit"]["a_fixed_creation_tokens"], RES["2.5_v"]["fit"]["b_tokens_per_char"])
P("DEC", json.dumps({k: {x: v[x] for x in ("N", "all", "per_sent_all", "per_sent_excl_cache_read", "per_sent_output", "cache_read", "cache_creation", "output", "duration_s", "usd", "N30_per_sent_all_ESTIMATE", "N30_per_sent_excl_cache_read_ESTIMATE", "N30_s_per_sent_ESTIMATE")} for k, v in DEC.items()}))
P("RW", json.dumps({k: rw[k] for k in ("handled", "script_acc", "model_acc", "fallback_tokens", "tokens_per_sent_over_200", "tokens_per_fallback_row", "N30_per_fallback_row_ESTIMATE", "N30_per_sent_over_all_ESTIMATE", "vs_2A_1264.5", "model_R_applied", "model_R_machine_fail")}, default=dict))
P("RWC", json.dumps({"script": rw["script"], "model": rw["model"]}, default=dict))
P("RWERR", json.dumps(rw["errors_script"][:6] + rw["errors_model"][:6], ensure_ascii=False)[:1500])
for k in sorted(S3):
    P("G", k, *[f"{t}:{S3[k][t]['counts']} E={S3[k][t]['ERROR']['pct']}{S3[k][t]['ERROR']['cp95']} causes={S3[k][t]['error_causes']} cls={S3[k][t]['error_classes']}" for t in ("pooled", "sk", "cz")])
P("GERR", json.dumps([e for e in errs if e["guard"] in ("before:g4_v3", "before:agv4")][:10], ensure_ascii=False)[:2000])
P("NULLS", json.dumps(RES["residual_nulls"]))
P("HEADLESS", json.dumps(RES["headless"]))
