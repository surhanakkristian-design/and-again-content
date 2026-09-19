#!/usr/bin/env python3
"""Phase 1S Task A — re-score of the CLOSED 1Q set with lever 1 REMOVED and rule AG added.
0 model calls, 0 network, no DB. Reads phase1p/, phase1q/, phase1r/. Writes only phase1s/taskA/."""
import json, os, sys
from collections import Counter

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
P1P, P1Q, P1R = [os.path.join(BASE, x) for x in ("phase1p", "phase1q", "phase1r")]
OUT = os.path.join(BASE, "phase1s", "taskA")
sys.path.insert(0, OUT)
import agent_drop as AG

L = lambda p: json.load(open(p, encoding="utf-8"))

# reuse cp() / fisher_exact() / kn() verbatim from rescore_1r.py (header only: no file writes)
src = open(os.path.join(P1R, "taskB", "rescore_1r.py"), encoding="utf-8").read()
head = src.split("# ---------- data ----------")[0]
g = {}
exec(compile(head, "rescore_1r_header", "exec"), g)
cp, kn, fisher_exact = g["cp"], g["kn"], g["fisher_exact"]

def jdef(o):
    if isinstance(o, (set, frozenset)):
        return sorted(o, key=str)
    if isinstance(o, tuple):
        return list(o)
    try:
        return str(o)
    except Exception:
        return None

def dump(obj, path):
    json.dump(obj, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=jdef)

# ---------------- data ----------------
rows_q = L(os.path.join(P1Q, "rows_1q.json"))
res = L(os.path.join(P1P, "results_1p.json"))
res_rows = res["rows"]
if isinstance(res_rows, dict):
    res_rows = list(res_rows.values())
rbi = {r["item_id"]: r for r in res_rows}
sents = {s["sid"]: s for s in L(os.path.join(P1P, "data", "sentences.json"))}
ann = L(os.path.join(P1P, "data", "annotations.json"))
items = {it["id"]: it for it in L(os.path.join(P1P, "data", "items.json"))}
verdicts = L(os.path.join(P1R, "taskA", "judge", "verdicts.json"))
key = L(os.path.join(P1R, "taskA", "_key.json"))
RES1R = L(os.path.join(P1R, "taskB", "RESCORE_1R.json"))

half_of = {s["sid"]: (s.get("tags") or {}).get("half") for s in sents.values()}
for r in rows_q:
    r["half"] = half_of.get(r["sid"]) or ("P1" if r["sid"] % 2 == 1 else "P2")
    r["tags"] = r.get("tags") or []

vby = {v["jid"]: v for v in verdicts}
movers, borderline_movers = set(), set()
for jid, k in key.items():
    v = vby.get(jid)
    if not v or k["bucket"] != "M2":
        continue
    if v["verdict"] == "wrong":
        movers.add(k["iid"])
        if v.get("borderline"):
            borderline_movers.add(k["iid"])
s2_flip = movers - borderline_movers

def labelled(rs, flip):
    out = []
    for r in rs:
        r2 = dict(r)
        if r2["iid"] in flip:
            r2["judged"], r2["wrong_type"] = "wrong", "M"
        out.append(r2)
    return out

# ---------------- metric machinery (same shapes as rescore_1r.py) ----------------
def cov_fa(rs, acc="accept"):
    cor = [r for r in rs if r["judged"] == "correct"]
    wro = [r for r in rs if r["judged"] == "wrong"]
    return kn(sum(1 for r in cor if r[acc]), len(cor)), kn(sum(1 for r in wro if r[acc]), len(wro))

def pack(rs, acc="accept"):
    c, f = cov_fa(rs, acc)
    return {"coverage": c, "fa": f}

def cells_of(rs, acc="accept"):
    out = {}
    for tag in ["agentless", "timeframe", "determiner", "by-passive", "plain", "aspect", "number"]:
        sub = [r for r in rs if tag in r["tags"]]
        c, f = cov_fa(sub, acc)
        out[tag.replace("-", "") + "_cov"] = c
        out[tag.replace("-", "") + "_fa"] = f
    return out

def layer_tables(rs, acc="accept", lay="layer"):
    return (dict(Counter(r[lay] for r in rs if r["judged"] == "correct" and not r[acc])),
            dict(Counter(r[lay] for r in rs if r["judged"] == "wrong" and not r[acc])),
            dict(Counter(r[lay] for r in rs if r["judged"] == "wrong" and r[acc])),
            dict(Counter(r[lay] for r in rs if r["judged"] == "correct" and r[acc])))

def fa_by_type(rs, acc="accept"):
    out = {}
    for wt in ["T", "W", "M", "S"]:
        sub = [r for r in rs if r["judged"] == "wrong" and r["wrong_type"] == wt]
        out[wt] = kn(sum(1 for r in sub if r[acc]), len(sub))
    return out

def agree(d):
    p1c, p2c, p1f, p2f = d["P1"]["coverage"], d["P2"]["coverage"], d["P1"]["fa"], d["P2"]["fa"]
    return {"cov_diff_points": round(p1c["pct"] - p2c["pct"], 2),
            "cov_fisher_p": round(fisher_exact(p1c["k"], p1c["n"] - p1c["k"], p2c["k"], p2c["n"] - p2c["k"]), 4),
            "fa_diff_points": round(p1f["pct"] - p2f["pct"], 2),
            "fa_fisher_p": round(fisher_exact(p1f["k"], p1f["n"] - p1f["k"], p2f["k"], p2f["n"] - p2f["k"]), 4)}

def full(rs, acc="accept", lay="layer"):
    rc, rw, ac, afc = layer_tables(rs, acc, lay)
    d = {"pooled": pack(rs, acc), "P1": pack([r for r in rs if r["half"] == "P1"], acc),
         "P2": pack([r for r in rs if r["half"] == "P2"], acc),
         "fa_by_wrongtype": fa_by_type(rs, acc), "cells": cells_of(rs, acc),
         "layers_reject_correct": rc, "layers_reject_wrong": rw,
         "layers_accept_wrong_FA": ac, "layers_accept_correct": afc,
         "n_correct": sum(1 for r in rs if r["judged"] == "correct"),
         "n_wrong": sum(1 for r in rs if r["judged"] == "wrong")}
    d["agreement"] = agree(d)
    return d

# ---------------- A4 step 1: reproduce the 1R numbers exactly ----------------
rows_1r = labelled(rows_q, movers)
BEFORE = full(rows_1r)
exp = RES1R["step2_new_primary"]
checks = {}
for k in ("pooled", "P1", "P2", "fa_by_wrongtype", "layers_reject_correct", "layers_reject_wrong",
          "layers_accept_wrong_FA"):
    checks[k] = json.loads(json.dumps(BEFORE[k])) == json.loads(json.dumps(exp[k]))
for k in ("agentless_cov", "agentless_fa", "bypassive_cov", "plain_cov", "timeframe_fa"):
    checks["cell:" + k] = json.loads(json.dumps(BEFORE["cells"][k])) == json.loads(json.dumps(exp["cells"][k]))
checks["headline_425_483"] = [BEFORE["pooled"]["coverage"]["k"], BEFORE["pooled"]["coverage"]["n"]] == [425, 483]
checks["headline_19_597"] = [BEFORE["pooled"]["fa"]["k"], BEFORE["pooled"]["fa"]["n"]] == [19, 597]
checks["agentless_75_98"] = [BEFORE["cells"]["agentless_cov"]["k"], BEFORE["cells"]["agentless_cov"]["n"]] == [75, 98]
checks["agentless_11_172"] = [BEFORE["cells"]["agentless_fa"]["k"], BEFORE["cells"]["agentless_fa"]["n"]] == [11, 172]
if not all(checks.values()):
    dump({"ABORT": "1R numbers not reproduced", "checks": checks, "got": BEFORE}, os.path.join(OUT, "ABORT_1S_A.json"))
    print("ABORT: 1R not reproduced ->", {k: v for k, v in checks.items() if not v})
    sys.exit(2)
print("A4 pre-flight: 1R reproduced,", sum(checks.values()), "/", len(checks), "checks OK")

# ---------------- A1 / A3: lever 1 off + AG ----------------
lev_fired = {i: bool((r.get("lever1") or {}).get("fired")) for i, r in rbi.items()}
ag, ag_noun = {}, {}
for i, it in items.items():
    s = sents[it["sid"]]
    a = ann.get(str(it["sid"])) or {}
    wt = (s.get("tags") or {}).get("writer_tags") or {}
    ref = ((a.get("hygienised") or a).get("v") or [""])[0]
    ag[i] = AG.decide(s["slovak"], a, wt, it["answer"], ref, "primary")
    ag_noun[i] = AG.decide(s["slovak"], a, wt, it["answer"], ref, "noun")

DET_LAYERS_AFTER_AG = {"L3", "L3:TIPrej"}
needs_call, lever1_off_used, rows_s = [], 0, []
for r in rows_q:
    i = r["iid"]
    rr = rbi[i]
    l1 = rr.get("lever1") or {}
    off_acc, off_lay = bool(l1.get("shadow_unrewritten_accept")), l1.get("shadow_unrewritten_layer")
    if off_lay is None:
        needs_call.append(i)
        off_acc, off_lay = r["accept"], r["layer"]
    elif lev_fired[i]:
        lever1_off_used += 1
    f = ag[i]["fired"]
    if f:
        acc_s = False
        lay_s = off_lay if (not off_acc and off_lay not in DET_LAYERS_AFTER_AG) else "AG"
    else:
        acc_s, lay_s = off_acc, off_lay
    rows_s.append({**r, "accept_1q": r["accept"], "layer_1q": r["layer"],
                   "lever1_fired": lev_fired[i], "lever1_agent": l1.get("agent"),
                   "lever1_off_accept": off_acc, "lever1_off_layer": off_lay,
                   "ag_fired": f, "ag_reason": ag[i]["reason"], "ag_agent": ag[i]["agent"],
                   "ag_agent_kind": ag[i]["agent_kind"], "ag_agent_source": ag[i]["agent_source"],
                   "ag_answer_is_agentless_passive": ag[i]["answer_is_agentless_passive"],
                   "ag_agent_elsewhere_in_answer": ag[i]["agent_token_elsewhere_in_answer"],
                   "ag_noun_fired": ag_noun[i]["fired"],
                   "accept_1s": acc_s, "layer_1s": lay_s,
                   "slovak": sents[r["sid"]]["slovak"], "answer": items[i]["answer"],
                   "reference": ((ann.get(str(r["sid"])) or {}).get("hygienised") or {}).get("v", [""])[0],
                   "l3_tip": (rr.get("layers") or {}).get("model_tip") if r["layer"] in ("L3:TIPrej",) else None})

def with_labels(flip):
    out = []
    for r in rows_s:
        r2 = dict(r)
        if r2["iid"] in flip:
            r2["judged"], r2["wrong_type"] = "wrong", "M"
        out.append(r2)
    return out

R_pri = with_labels(movers)
R_s2 = with_labels(s2_flip)
BEFORE_S2 = full(R_s2, "accept_1q", "layer_1q")
AFTER = full(R_pri, "accept_1s", "layer_1s")
AFTER_S2 = full(R_s2, "accept_1s", "layer_1s")
BEFORE_pri = full(R_pri, "accept_1q", "layer_1q")
assert json.dumps(BEFORE_pri["pooled"]) == json.dumps(BEFORE["pooled"])

# AG-noun side line
AFTER_noun_rows = []
for r in R_pri:
    r2 = dict(r)
    if r2["ag_noun_fired"]:
        r2["accept_1s"] = False
    else:
        r2["accept_1s"] = r2["lever1_off_accept"]
    AFTER_noun_rows.append(r2)
AFTER_NOUN = full(AFTER_noun_rows, "accept_1s", "layer_1s")

# lever-1-off only (no AG), for the decomposition
OFFONLY = full([{**r, "acc_off": r["lever1_off_accept"]} for r in R_pri], "acc_off", "lever1_off_layer")

# ---------------- A5 cost list ----------------
def line(r):
    return {"iid": r["iid"], "sid": r["sid"], "slovak": r["slovak"], "answer": r["answer"],
            "reference": r["reference"], "agent": r["ag_agent"], "agent_kind": r["ag_agent_kind"],
            "agent_source": r["ag_agent_source"], "was_accepted_in_1R": r["accept_1q"],
            "lever1_fired": r["lever1_fired"], "layer_1q": r["layer_1q"],
            "agent_elsewhere": r["ag_agent_elsewhere_in_answer"]}

agentless_correct = [r for r in R_pri if "agentless" in r["tags"] and r["judged"] == "correct"]
cost = [line(r) for r in agentless_correct if r["ag_fired"]]
cost_new = [c for c in cost if c["was_accepted_in_1R"]]
fa_agentless = [r for r in R_pri if "agentless" in r["tags"] and r["judged"] == "wrong" and r["accept_1q"]]
fa_caught = [line(r) for r in fa_agentless if r["ag_fired"]]
fa_missed = [{**line(r), "why_missed": r["ag_reason"]} for r in fa_agentless if not r["ag_fired"]]
ag_outside = [line(r) for r in R_pri if r["ag_fired"] and "agentless" not in r["tags"]]
confusion = {"ag_fired & tag agentless": sum(1 for r in R_pri if r["ag_fired"] and "agentless" in r["tags"]),
             "ag_fired & tag NOT agentless": sum(1 for r in R_pri if r["ag_fired"] and "agentless" not in r["tags"]),
             "ag_abstain & tag agentless": sum(1 for r in R_pri if not r["ag_fired"] and "agentless" in r["tags"]),
             "ag_abstain & tag NOT agentless": sum(1 for r in R_pri if not r["ag_fired"] and "agentless" not in r["tags"]),
             "tag by-passive & ag_fired": sum(1 for r in R_pri if r["ag_fired"] and "by-passive" in r["tags"])}

A1 = {"lever1_fired_items": sum(1 for v in lev_fired.values() if v),
      "lever1_gain": res["cells"]["lever1"]["gain"], "lever1_fa_cost": res["cells"]["lever1"]["fa_cost"],
      "lever1_shadow_accept": res["cells"]["lever1"]["shadow_accept"],
      "answer_is_agentless_passive": sum(1 for r in res_rows if (r.get("lever1") or {}).get("reason") != "the answer is not a be-passive without a by-agent")}

pf_ok, pf_lines = AG.preflight(verbose=False)
RESULT = {"what": "Phase 1S Task A - lever 1 removed, rule AG added; re-score of the closed 1Q set",
          "date": "2026-09-19", "model_calls": 0, "network_calls": 0,
          "A1_lever1": A1, "A2_preflight": {"ok": pf_ok, "lines": pf_lines},
          "A4_reproduction_checks": checks,
          "BEFORE_primary": BEFORE, "AFTER_primary": AFTER,
          "BEFORE_S2": BEFORE_S2, "AFTER_S2": AFTER_S2,
          "AFTER_lever1_off_only_primary": OFFONLY, "AFTER_AGnoun_primary": AFTER_NOUN,
          "ag_firings_total": sum(1 for r in rows_s if r["ag_fired"]),
          "ag_noun_firings_total": sum(1 for r in rows_s if r["ag_noun_fired"]),
          "detector_vs_tag": confusion,
          "needs_new_call": {"n": len(needs_call), "iids": needs_call,
                             "lever1_fired_rows_scored_from_the_stored_lever1_OFF_verdict": lever1_off_used},
          "A5_cost_all_ag_fired_judged_correct_agentless": cost,
          "A5_cost_newly_lost_were_accepted": len(cost_new),
          "A5_fa_caught": fa_caught, "A5_fa_missed": fa_missed, "A5_ag_outside_agentless": ag_outside,
          "movers": {"n": len(movers), "borderline": len(borderline_movers), "s2_flip": len(s2_flip)}}
dump(RESULT, os.path.join(OUT, "RESCORE_1S_A.json"))
dump(rows_s, os.path.join(OUT, "rows_1s.json"))

def c(d):
    return "-" if not d or not d["n"] else "%d/%d = %.2f %% [%.2f, %.2f]" % (d["k"], d["n"], d["pct"], d["ci"][0], d["ci"][1])
def dct(d):
    return ", ".join("%s %d" % (k, v) for k, v in sorted(d.items(), key=lambda kv: -kv[1])) or "-"

md = ["# Phase 1S Task A - lever 1 out, rule AG in (re-score of the closed 1Q set)\n",
      "0 model calls, 0 network calls. The stack decisions are the frozen 1Q ones with lever 1's "
      "rewrite-accept removed (the stored MAIN-side verdict is exactly the lever-1-OFF verdict of "
      "the unrewritten answer) and the deterministic rule AG inserted before L3.\n",
      "## Fields of `rows_1s.json` (one object per item, 1,080 rows)\n",
      "| field | meaning |\n| --- | --- |",
      "| iid, sid, half, tags, wrong_type | as in `phase1q/rows_1q.json` (tags are writer LABELS of the set) |",
      "| judged | the 1Q label; apply `movers` for 1R-primary, `s2_flip` for S2 (both listed in RESCORE_1S_A.json) |",
      "| accept_1q, layer_1q | the frozen 1Q decision (lever 1 ON) |",
      "| lever1_fired, lever1_agent | lever 1's detector on this item |",
      "| lever1_off_accept, lever1_off_layer | the stored MAIN-side verdict = lever 1 OFF |",
      "| ag_fired, ag_reason, ag_agent, ag_agent_kind, ag_agent_source | rule AG (primary variant) |",
      "| ag_answer_is_agentless_passive, ag_agent_elsewhere_in_answer, ag_noun_fired | AG diagnostics / AG-noun variant |",
      "| accept_1s, layer_1s | the NEW stack decision (lever 1 off + AG) |",
      "| slovak, answer, reference, l3_tip | source text, the answer, main reference, L3 tip for L3:TIPrej rows |\n",
      "## Headline\n", "| metric | BEFORE (1R) | AFTER | BEFORE S2 | AFTER S2 |\n| --- | --- | --- | --- | --- |"]
for nm, kk in [("pooled coverage", ("pooled", "coverage")), ("pooled FA", ("pooled", "fa")),
               ("P1 coverage", ("P1", "coverage")), ("P1 FA", ("P1", "fa")),
               ("P2 coverage", ("P2", "coverage")), ("P2 FA", ("P2", "fa"))]:
    md.append("| %s | %s | %s | %s | %s |" % (nm, c(BEFORE[kk[0]][kk[1]]), c(AFTER[kk[0]][kk[1]]),
                                              c(BEFORE_S2[kk[0]][kk[1]]), c(AFTER_S2[kk[0]][kk[1]])))
md += ["", "Fisher p: BEFORE cov %.4f / FA %.4f; AFTER cov %.4f / FA %.4f; S2 AFTER cov %.4f / FA %.4f\n"
       % (BEFORE["agreement"]["cov_fisher_p"], BEFORE["agreement"]["fa_fisher_p"],
          AFTER["agreement"]["cov_fisher_p"], AFTER["agreement"]["fa_fisher_p"],
          AFTER_S2["agreement"]["cov_fisher_p"], AFTER_S2["agreement"]["fa_fisher_p"]),
       "## Cells\n", "| cell | BEFORE | AFTER | BEFORE S2 | AFTER S2 |\n| --- | --- | --- | --- | --- |"]
for lbl, k2 in [("agentless cov", "agentless_cov"), ("agentless FA", "agentless_fa"),
                ("by-passive cov", "bypassive_cov"), ("plain cov", "plain_cov"),
                ("timeframe FA", "timeframe_fa")]:
    md.append("| %s | %s | %s | %s | %s |" % (lbl, c(BEFORE["cells"][k2]), c(AFTER["cells"][k2]),
                                              c(BEFORE_S2["cells"][k2]), c(AFTER_S2["cells"][k2])))
md += ["", "## FA by wrong type\n", "| type | BEFORE | AFTER | BEFORE S2 | AFTER S2 |\n| --- | --- | --- | --- | --- |"]
for wt in ["T", "W", "M", "S"]:
    md.append("| %s | %s | %s | %s | %s |" % (wt, c(BEFORE["fa_by_wrongtype"][wt]), c(AFTER["fa_by_wrongtype"][wt]),
                                              c(BEFORE_S2["fa_by_wrongtype"][wt]), c(AFTER_S2["fa_by_wrongtype"][wt])))
md += ["", "## Layers\n",
       "- false rejections BEFORE: %s\n- false rejections AFTER: %s\n" % (dct(BEFORE["layers_reject_correct"]), dct(AFTER["layers_reject_correct"])),
       "- false accepts BEFORE: %s\n- false accepts AFTER: %s\n" % (dct(BEFORE["layers_accept_wrong_FA"]), dct(AFTER["layers_accept_wrong_FA"])),
       "- true rejections AFTER: %s\n" % dct(AFTER["layers_reject_wrong"]),
       "## A5 - the cost (AG fires on judged-correct agentless items)\n",
       "| iid | Slovak | answer | agent | kind | was accepted |\n| --- | --- | --- | --- | --- | --- |"]
for x in cost:
    md.append("| %s | %s | %s | %s | %s | %s |" % (x["iid"], x["slovak"], x["answer"], x["agent"], x["agent_kind"], x["was_accepted_in_1R"]))
md += ["", "## A5 - the 11 agentless false accepts\n", "caught: %d, missed: %d\n" % (len(fa_caught), len(fa_missed)),
       "| iid | answer | caught | why |\n| --- | --- | --- | --- |"]
for x in fa_caught:
    md.append("| %s | %s | caught | agent %s |" % (x["iid"], x["answer"], x["agent"]))
for x in fa_missed:
    md.append("| %s | %s | MISSED | %s |" % (x["iid"], x["answer"], x["why_missed"]))
md += ["", "## Side lines\n",
       "- AG firings: %d (AG-noun: %d). Detector vs writer tag: %s\n" % (RESULT["ag_firings_total"], RESULT["ag_noun_firings_total"], json.dumps(confusion)),
       "- AG-noun pooled: coverage %s, FA %s\n" % (c(AFTER_NOUN["pooled"]["coverage"]), c(AFTER_NOUN["pooled"]["fa"])),
       "- lever 1 OFF, no AG: coverage %s, FA %s\n" % (c(OFFONLY["pooled"]["coverage"]), c(OFFONLY["pooled"]["fa"])),
       "- needs new call: %d\n" % len(needs_call)]
open(os.path.join(OUT, "RESCORE_1S_A.md"), "w", encoding="utf-8").write("\n".join(md))

# ---------------- console ----------------
P = print
P("A1 lever1:", json.dumps(A1))
P("AG firings", RESULT["ag_firings_total"], "AG-noun", RESULT["ag_noun_firings_total"], "confusion", json.dumps(confusion))
P("needs_new_call", len(needs_call), "lever1-fired rows re-scored from stored OFF verdict", lever1_off_used)
for nm, d in [("BEFORE", BEFORE), ("AFTER", AFTER), ("BEFORE_S2", BEFORE_S2), ("AFTER_S2", AFTER_S2),
              ("OFFONLY", OFFONLY), ("AGNOUN", AFTER_NOUN)]:
    P("%-10s cov %s | FA %s | P1 cov %s FA %s | P2 cov %s FA %s | fisher cov %.4f fa %.4f"
      % (nm, c(d["pooled"]["coverage"]), c(d["pooled"]["fa"]), c(d["P1"]["coverage"]), c(d["P1"]["fa"]),
         c(d["P2"]["coverage"]), c(d["P2"]["fa"]), d["agreement"]["cov_fisher_p"], d["agreement"]["fa_fisher_p"]))
    P("           cells agentless_cov %s agentless_fa %s bypassive_cov %s plain_cov %s timeframe_fa %s"
      % (c(d["cells"]["agentless_cov"]), c(d["cells"]["agentless_fa"]), c(d["cells"]["bypassive_cov"]),
         c(d["cells"]["plain_cov"]), c(d["cells"]["timeframe_fa"])))
    P("           FA type " + "  ".join("%s %s" % (w, c(d["fa_by_wrongtype"][w])) for w in "TWMS"))
    P("           falserej %s | falseacc %s" % (dct(d["layers_reject_correct"]), dct(d["layers_accept_wrong_FA"])))
P("COST n=%d (of which were accepted before: %d) of %d judged-correct agentless" % (len(cost), len(cost_new), len(agentless_correct)))
for x in cost:
    P("  COST %s | %s | %s | agent=%s (%s) | acc_before=%s | l1=%s | layer1q=%s" % (x["iid"], x["slovak"], x["answer"], x["agent"], x["agent_kind"], x["was_accepted_in_1R"], x["lever1_fired"], x["layer_1q"]))
P("FA caught %d missed %d" % (len(fa_caught), len(fa_missed)))
for x in fa_caught:
    P("  CAUGHT %s | %s | agent=%s" % (x["iid"], x["answer"], x["agent"]))
for x in fa_missed:
    P("  MISSED %s | %s | %s" % (x["iid"], x["answer"], x["why_missed"]))
P("AG outside agentless tag: %d" % len(ag_outside))
for x in ag_outside[:40]:
    P("  OUT %s | tags? | %s | %s | agent=%s | judged_correct_before=%s" % (x["iid"], x["slovak"], x["answer"], x["agent"], x["was_accepted_in_1R"]))
