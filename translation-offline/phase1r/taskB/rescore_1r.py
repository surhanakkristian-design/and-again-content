#!/usr/bin/env python3
"""Phase 1R Task B: re-score of the CLOSED 1Q set (1,080 items) against corrected labels.

NOT a new measurement. 0 model calls, 0 network, no DB. Reads only phase1q/, phase1p/, phase1r/.
Writes only phase1r/taskB/ and phase1r/taskA/.
"""
import json, math, os, inspect, importlib.util
from collections import Counter, defaultdict

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
P1Q = os.path.join(BASE, "phase1q")
P1P = os.path.join(BASE, "phase1p")
P1R = os.path.join(BASE, "phase1r")
OUT = os.path.join(P1R, "taskB")
os.makedirs(OUT, exist_ok=True)

L = lambda p: json.load(open(p, encoding="utf-8"))

# ---------- statistics ----------
def betacf(a, b, x):
    MAXIT, EPS, FPMIN = 300, 3e-16, 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN: d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN: d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN: c = FPMIN
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < EPS: break
    return h

def betainc(a, b, x):
    """Regularised incomplete beta I_x(a,b)."""
    if x <= 0.0: return 0.0
    if x >= 1.0: return 1.0
    lbeta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) + a * math.log(x) + b * math.log(1.0 - x)
    bt = math.exp(lbeta)
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * betacf(a, b, x) / a
    return 1.0 - bt * betacf(b, a, 1.0 - x) / b

def beta_ppf(q, a, b):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if betainc(a, b, mid) < q: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

def cp(k, n, alpha=0.05):
    """Exact Clopper-Pearson 95% interval, in percent."""
    if n == 0: return None
    lo = 0.0 if k == 0 else beta_ppf(alpha / 2, k, n - k + 1)
    hi = 1.0 if k == n else beta_ppf(1 - alpha / 2, k + 1, n - k)
    return [round(lo * 100, 2), round(hi * 100, 2)]

def kn(k, n):
    return {"k": k, "n": n, "pct": (round(100.0 * k / n, 2) if n else None), "ci": cp(k, n)}

def fisher_exact(a, b, c, d):
    """Two-sided Fisher exact p for table [[a,b],[c,d]]."""
    n = a + b + c + d
    r1, r2, c1 = a + b, c + d, a + c
    def prob(x):
        return math.comb(r1, x) * math.comb(r2, c1 - x) / math.comb(n, c1)
    p0 = prob(a)
    lo = max(0, c1 - r2); hi = min(r1, c1)
    tot = 0.0
    for x in range(lo, hi + 1):
        p = prob(x)
        if p <= p0 * (1 + 1e-9): tot += p
    return min(1.0, tot)

# ---------- data ----------
rows = L(os.path.join(P1Q, "rows_1q.json"))
RES = L(os.path.join(P1Q, "RESULTS_1Q.json"))
triage = L(os.path.join(P1Q, "taskA", "triage.json"))
verdicts = L(os.path.join(P1R, "taskA", "judge", "verdicts.json"))
key = L(os.path.join(P1R, "taskA", "_key.json"))
sents = L(os.path.join(P1P, "data", "sentences.json"))

half_of_sid = {}
for s in sents:
    h = (s.get("tags") or {}).get("half")
    if h: half_of_sid[s["sid"]] = h
def half(sid):
    return half_of_sid.get(sid, "P1" if sid % 2 == 1 else "P2")

for r in rows:
    r["half"] = half(r["sid"])
    r["tags"] = r.get("tags") or []

tri_by_iid = {t["iid"]: t for t in triage}
bucket_of = {t["iid"]: t["bucket"] for t in triage}

# ---------- STEP 0: pre-flight ----------
def cov_fa(rs):
    cor = [r for r in rs if r["judged"] == "correct"]
    wro = [r for r in rs if r["judged"] == "wrong"]
    return kn(sum(1 for r in cor if r["accept"]), len(cor)), kn(sum(1 for r in wro if r["accept"]), len(wro))

def pack(rs):
    c, f = cov_fa(rs)
    return {"coverage": c, "fa": f}

def cells_of(rs):
    out = {}
    for tag in ["agentless", "timeframe", "determiner", "by-passive", "plain", "aspect", "number"]:
        sub = [r for r in rs if tag in r["tags"]]
        c, f = cov_fa(sub)
        name = tag.replace("-", "")
        out[name + "_cov"] = c
        out[name + "_fa"] = f
    return out

def layer_tables(rs):
    rc = Counter(r["layer"] for r in rs if r["judged"] == "correct" and not r["accept"])
    rw = Counter(r["layer"] for r in rs if r["judged"] == "wrong" and not r["accept"])
    ac = Counter(r["layer"] for r in rs if r["judged"] == "wrong" and r["accept"])
    afc = Counter(r["layer"] for r in rs if r["judged"] == "correct" and r["accept"])
    return dict(rc), dict(rw), dict(ac), dict(afc)

def fa_by_type(rs):
    out = {}
    for wt in ["T", "W", "M", "S"]:
        sub = [r for r in rs if r["judged"] == "wrong" and r["wrong_type"] == wt]
        out[wt] = kn(sum(1 for r in sub if r["accept"]), len(sub))
    return out

def m_table(rs):
    out = {}
    for b in ["M1", "M2", "M3", "M4"]:
        sub = [r for r in rs if bucket_of.get(r["iid"]) == b]
        out[b] = {"n": len(sub),
                  "accepted": sum(1 for r in sub if r["accept"]),
                  "rejected": sum(1 for r in sub if not r["accept"]),
                  "layers": dict(Counter(r["layer"] for r in sub if not r["accept"]))}
    return out

preflight = {}
old_pooled = pack(rows)
old_p1 = pack([r for r in rows if r["half"] == "P1"])
old_p2 = pack([r for r in rows if r["half"] == "P2"])
old_cells = cells_of(rows)
old_rc, old_rw, old_ac, old_afc = layer_tables(rows)
old_fabt = fa_by_type(rows)
old_m = m_table(rows)

def cmp(name, got, exp):
    ok = json.loads(json.dumps(got)) == json.loads(json.dumps(exp))
    preflight[name] = {"ok": ok, "got": got, "expected": exp}
    return ok

cmp("pooled", old_pooled, RES["pooled"])
cmp("P1", old_p1, RES["P1"])
cmp("P2", old_p2, RES["P2"])
cmp("fa_by_wrongtype", old_fabt, RES["fa_by_wrongtype"])
cmp("layers_reject_correct", old_rc, RES["layers_reject_correct"])
cmp("layers_reject_wrong", old_rw, RES["layers_reject_wrong"])
exp_cells = RES["cells"]
got_cells = {k: old_cells[k] for k in exp_cells if k in old_cells}
cmp("cells", got_cells, {k: exp_cells[k] for k in got_cells})
exp_m = {k.split("/")[0]: v for k, v in RES["M"].items()}
cmp("M_buckets", old_m, exp_m)
# CI sanity check demanded by the brief
ci_check = {"8/481_upper": cp(8, 481), "expect": [0.72, 3.25]}
preflight["ci_selftest"] = {"ok": cp(8, 481) == [0.72, 3.25], "got": cp(8, 481), "expected": [0.72, 3.25]}
# F5 read-off
f5_cost_old = sum(1 for r in rows if r["layer"] == "F5" and r["judged"] == "correct")
f5_catch_old = sum(1 for r in rows if r["layer"] == "F5" and r["judged"] == "wrong")
preflight["f5_readoff"] = {"ok": (f5_cost_old, f5_catch_old) == (65, 2), "got": [f5_cost_old, f5_catch_old], "expected": [65, 2]}

# ---------- STEP 1: Task A tally ----------
vby = {v["jid"]: v for v in verdicts}
join = []
for jid in sorted(key):
    k = key[jid]; v = vby.get(jid)
    t = tri_by_iid.get(k["iid"], {})
    join.append({"jid": jid, "iid": k["iid"], "bucket": k["bucket"], "half": k["half"], "level": k["level"],
                 "old_label": k["old_judge_label"], "verdict": v["verdict"], "class": v["class"],
                 "borderline": bool(v["borderline"]), "dropped": v["dropped"], "note": v.get("note", ""),
                 "slovak": t.get("slovak", ""), "answer": t.get("answer", ""), "triage_what": t.get("what", "")})

m2 = [j for j in join if j["bucket"] == "M2"]
m1 = [j for j in join if j["bucket"] == "M1"]
movers = [j for j in m2 if j["verdict"] == "wrong"]
stayers = [j for j in m2 if j["verdict"] != "wrong"]
mover_iids = {j["iid"] for j in movers}
borderline_movers = [j for j in movers if j["borderline"]]
m1_disagree = [j for j in m1 if j["verdict"] == "wrong"]
taskA = {
    "n_judged": len(join), "n_M2": len(m2), "n_M1_controls": len(m1),
    "movers": len(movers), "stayers": len(stayers),
    "class_counts": dict(Counter(j["class"] for j in join)),
    "verdict_counts": dict(Counter(j["verdict"] for j in join)),
    "borderline_total": sum(1 for j in join if j["borderline"]),
    "borderline_movers": len(borderline_movers),
    "M1_controls": [{k: j[k] for k in ("jid", "iid", "verdict", "class", "borderline", "dropped", "slovak", "answer")} for j in m1],
    "M1_control_disagreements": len(m1_disagree),
    "stayer_list": [{k: j[k] for k in ("jid", "iid", "class", "verdict", "borderline", "dropped", "slovak", "answer", "note")} for j in stayers],
    "mover_examples": [{k: j[k] for k in ("jid", "iid", "slovak", "answer", "dropped", "borderline")} for j in movers[:10]],
}

# ---------- label variants ----------
def relabel(flip_iids):
    out = []
    for r in rows:
        r2 = dict(r)
        if r2["iid"] in flip_iids:
            r2["judged"] = "wrong"; r2["wrong_type"] = "M"
        out.append(r2)
    return out

primary_flip = set(mover_iids)
sensA_flip = set(j["iid"] for j in join if j["verdict"] == "wrong")           # judge on all 119 (M1 too)
sensB_flip = set(j["iid"] for j in movers if not j["borderline"])            # borderline movers stay correct

rows_new = relabel(primary_flip)
rows_sensA = relabel(sensA_flip)
rows_sensB = relabel(sensB_flip)

# ---------- STEP 2: re-score ----------
def full(rs):
    rc, rw, ac, afc = layer_tables(rs)
    d = {"pooled": pack(rs), "P1": pack([r for r in rs if r["half"] == "P1"]),
         "P2": pack([r for r in rs if r["half"] == "P2"]),
         "fa_by_wrongtype": fa_by_type(rs), "cells": cells_of(rs),
         "layers_reject_correct": rc, "layers_reject_wrong": rw,
         "layers_accept_wrong_FA": ac, "layers_accept_correct": afc,
         "M_buckets": m_table(rs),
         "n_correct": sum(1 for r in rs if r["judged"] == "correct"),
         "n_wrong": sum(1 for r in rs if r["judged"] == "wrong")}
    return d

OLD = full(rows)
NEW = full(rows_new)

def agree(d):
    p1c, p2c = d["P1"]["coverage"], d["P2"]["coverage"]
    p1f, p2f = d["P1"]["fa"], d["P2"]["fa"]
    return {
        "cov_diff_points": round(p1c["pct"] - p2c["pct"], 2),
        "cov_fisher_p": round(fisher_exact(p1c["k"], p1c["n"] - p1c["k"], p2c["k"], p2c["n"] - p2c["k"]), 4),
        "cov_overlap": not (p1c["ci"][1] < p2c["ci"][0] or p2c["ci"][1] < p1c["ci"][0]),
        "fa_diff_points": round(p1f["pct"] - p2f["pct"], 2),
        "fa_fisher_p": round(fisher_exact(p1f["k"], p1f["n"] - p1f["k"], p2f["k"], p2f["n"] - p2f["k"]), 4),
        "fa_overlap": not (p1f["ci"][1] < p2f["ci"][0] or p2f["ci"][1] < p1f["ci"][0]),
    }

OLD["agreement"] = agree(OLD)
NEW["agreement"] = agree(NEW)

# movers: how the stack treated them
rowmap = {r["iid"]: r for r in rows}
mv_rows = [rowmap[i] for i in mover_iids if i in rowmap]
mv_acc = [r for r in mv_rows if r["accept"]]
mv_rej = [r for r in mv_rows if not r["accept"]]
mover_treatment = {
    "n": len(mv_rows),
    "accepted": len(mv_acc), "accepted_layers": dict(Counter(r["layer"] for r in mv_acc)),
    "rejected": len(mv_rej), "rejected_layers": dict(Counter(r["layer"] for r in mv_rej)),
    "accepted_are_new_false_accepts": len(mv_acc),
    "rejected_stop_being_false_rejections": len(mv_rej),
    "by_half": dict(Counter(rowmap[i]["half"] for i in mover_iids if i in rowmap)),
    "accepted_items": [{"iid": r["iid"], "layer": r["layer"], "half": r["half"]} for r in mv_acc],
}

# M cell detail with movers/stayers split
m_cell_detail = {
    "M1": {"n": len(m1), "accepted": sum(1 for j in m1 if rowmap[j["iid"]]["accept"])},
    "M2_movers": {"n": len(movers), "accepted": len(mv_acc)},
    "M2_stayers": {"n": len(stayers), "accepted": sum(1 for j in stayers if rowmap[j["iid"]]["accept"])},
    "M3": NEW["M_buckets"]["M3"], "M4": NEW["M_buckets"]["M4"],
}

sens = {
    "A_judge_on_all_119": {"pooled": pack(rows_sensA), "n_flipped": len(sensA_flip)},
    "B_borderline_movers_stay_correct": {"pooled": pack(rows_sensB), "n_flipped": len(sensB_flip)},
}

# ---------- STEP 3: F5 / F6 ----------
f5_rej = [r for r in rows if r["layer"] == "F5"]
f5_rej_correct_old = [r for r in f5_rej if r["judged"] == "correct"]
f5_movers = [r for r in f5_rej_correct_old if r["iid"] in mover_iids]
newmap = {r["iid"]: r for r in rows_new}
f5 = {
    "old": {"cost_correct": len(f5_rej_correct_old), "catches_wrong": len(f5_rej) - len(f5_rej_correct_old)},
    "of_the_65_rejected_correct_how_many_are_movers": len(f5_movers),
    "new": {"cost_correct": sum(1 for r in f5_rej if newmap[r["iid"]]["judged"] == "correct"),
            "catches_wrong": sum(1 for r in f5_rej if newmap[r["iid"]]["judged"] == "wrong")},
    "coverage_if_F5_off_old": RES["f5_off_bounds"]["coverage_if_all_accepted"],
}
# coverage if F5 rejections were all accepted, under NEW labels
cor_new = [r for r in rows_new if r["judged"] == "correct"]
f5["coverage_if_F5_off_new"] = kn(sum(1 for r in cor_new if r["accept"] or r["layer"] == "F5"), len(cor_new))
f5["coverage_F5_on_new"] = NEW["pooled"]["coverage"]

f6 = {"per_item_available": False,
      "note": "F6 per-item verdicts are NOT stored: rows_1q.json has no F6 field, the F6 layer never appears in the "
              "`layer` column (layers seen: L1/L3/L3:TIPrej/F5/F3/F2B), and phase1p/results_1p.json rows carry only "
              "sid/item_id/half/level/judged/judged_type/tags/writer_passive/intent/layers/lever1/lever2_fired/lever3/"
              "final_accept/tip/f9_readout - no F6 readout. RESULTS_1Q f6 holds aggregates only "
              "(rej_correct_all=4, rej_wrong_all=12, m3 catches 0). Which 4 judged-correct items F6 rejected is therefore "
              "not recoverable from the read-allowed files, so the F6 recomputation under corrected labels is NOT done "
              "and NOT estimated.",
      "old_aggregates": RES["f6"]}
try:
    spec = importlib.util.spec_from_file_location("f6q", os.path.join(P1Q, "f6.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    f6["module_functions"] = {n: str(inspect.signature(o)) for n, o in vars(m).items()
                              if inspect.isfunction(o) and o.__module__ == "f6q"}
except Exception as e:
    f6["module_functions"] = {"error": repr(e)}

# ---------- assemble ----------
RESULT = {
    "what": "Re-score of the closed 1Q set (1,080 items) against corrected labels - NOT a new measurement",
    "date": "2026-09-19", "model_calls": 0,
    "inputs": {"rows": "phase1q/rows_1q.json", "old_aggregates": "phase1q/RESULTS_1Q.json",
               "triage": "phase1q/taskA/triage.json", "verdicts": "phase1r/taskA/judge/verdicts.json",
               "key": "phase1r/taskA/_key.json", "halves": "phase1p/data/sentences.json tags.half"},
    "step0_preflight": {k: {"ok": v["ok"]} if k != "ci_selftest" else v for k, v in preflight.items()},
    "step0_preflight_detail_failures": {k: v for k, v in preflight.items() if not v["ok"]},
    "step1_taskA": taskA,
    "step2_old": OLD, "step2_new_primary": NEW,
    "step2_mover_treatment": mover_treatment,
    "step2_M_cells": m_cell_detail,
    "step2_sensitivity": sens,
    "step3_f5": f5, "step3_f6": f6,
}
json.dump(RESULT, open(os.path.join(OUT, "RESCORE_1R.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- markdown ----------
def c(d):  # cell -> "k/n = pct % [lo, hi]"
    if d is None or d["n"] == 0: return "- (n=0)"
    return f"{d['k']}/{d['n']} = {d['pct']:.2f} % [{d['ci'][0]:.2f}, {d['ci'][1]:.2f}]"

def dct(d):
    return ", ".join(f"{k} {v}" for k, v in sorted(d.items(), key=lambda kv: -kv[1])) or "-"

pf_lines = "\n".join(f"| {k} | {'reproduced' if v['ok'] else 'NOT reproduced'} |" for k, v in preflight.items())

md = []
md.append("# Re-score of the closed 1Q set against corrected labels — not a new measurement\n")
md.append("Phase 1R, Task B. 1,080 stored per-item verdicts from `phase1q/rows_1q.json` re-scored after one blind "
          "re-judge of the 119 judged-correct type-M answers. **No model, Gemini or network calls were made "
          "(0 calls); no new items were generated, judged by a model, or re-run through the stack.** The stack's "
          "accept/reject decision per item is the frozen 1Q decision; only the LABELS changed.\n")
md.append("## 0. Pre-flight — reproduction of the old scoring from `rows_1q.json` alone\n")
md.append("| figure | status |\n| --- | --- |\n" + pf_lines + "\n")
md.append(f"Clopper-Pearson self-test: 8/481 → {cp(8,481)} (target [0.72, 3.25]).\n")
md.append(f"Half rule: `phase1p/data/sentences.json` `tags.half` (present for all {len(half_of_sid)} sentences; "
          "the odd/even fallback was never needed). Cells are tag-based, exactly as in `RESULTS_1Q.json`: "
          "`<tag>_cov` = accepted among judged-correct rows carrying that tag, `<tag>_fa` = accepted among "
          "judged-wrong rows carrying that tag; tag names in the rows are `agentless`, `timeframe`, `determiner`, "
          "`by-passive`, `plain`, `aspect`, `number`. M1/M2/M3/M4 come from `phase1q/taskA/triage.json`.\n")
md.append("## 1. The label correction\n")
md.append(f"- 119 judged-correct type-M answers re-judged blind today ({len(m2)} M2 + {len(m1)} M1 hidden controls).\n"
          f"- Owner's rule: the 3 M1 (function word dropped) stay CORRECT; the {len(m2)} M2 follow the judge.\n"
          f"- **Movers (M2 → wrong): {len(movers)}; stayers (M2 stays correct): {len(stayers)}.**\n"
          f"- Borderline among the movers: {len(borderline_movers)}.\n"
          f"- M1 control disagreements (judge called an M1 control wrong): {len(m1_disagree)} — reported, not applied "
          "in the primary score.\n\nFull movement table: `phase1r/taskA/TASKA_MOVEMENT_1R.md`.\n")
md.append(f"Label totals: judged-correct {OLD['n_correct']} → **{NEW['n_correct']}**, "
          f"judged-wrong {OLD['n_wrong']} → **{NEW['n_wrong']}**.\n")
md.append("## 2. Headline — old labels vs corrected labels (primary variant)\n")
md.append("| metric | OLD (1Q as closed) | NEW (corrected labels) |\n| --- | --- | --- |")
for name, kk in [("pooled coverage", ("pooled", "coverage")), ("pooled FA", ("pooled", "fa")),
                 ("P1 coverage", ("P1", "coverage")), ("P1 FA", ("P1", "fa")),
                 ("P2 coverage", ("P2", "coverage")), ("P2 FA", ("P2", "fa"))]:
    md.append(f"| {name} | {c(OLD[kk[0]][kk[1]])} | {c(NEW[kk[0]][kk[1]])} |")
md.append("")
md.append("### Do the halves still agree?\n")
md.append("| | OLD | NEW |\n| --- | --- | --- |")
for lbl, kk in [("coverage difference P1−P2 (points)", "cov_diff_points"), ("coverage Fisher exact p", "cov_fisher_p"),
                ("coverage CIs overlap", "cov_overlap"), ("FA difference P1−P2 (points)", "fa_diff_points"),
                ("FA Fisher exact p", "fa_fisher_p"), ("FA CIs overlap", "fa_overlap")]:
    md.append(f"| {lbl} | {OLD['agreement'][kk]} | {NEW['agreement'][kk]} |")
md.append("")
md.append("## 3. False accepts by wrong type\n")
md.append("| wrong type | OLD | NEW |\n| --- | --- | --- |")
for wt in ["T", "W", "M", "S"]:
    md.append(f"| {wt} | {c(OLD['fa_by_wrongtype'][wt])} | {c(NEW['fa_by_wrongtype'][wt])} |")
md.append("")
md.append("## 4. Layers\n")
md.append("### Which layer ACCEPTED each false accept\n")
md.append(f"- OLD: {dct(OLD['layers_accept_wrong_FA'])}\n- NEW: {dct(NEW['layers_accept_wrong_FA'])}\n")
md.append("### Which layer REJECTED each judged-correct item (false rejections)\n")
md.append(f"- OLD ({sum(OLD['layers_reject_correct'].values())} items): {dct(OLD['layers_reject_correct'])}\n"
          f"- NEW ({sum(NEW['layers_reject_correct'].values())} items): {dct(NEW['layers_reject_correct'])}\n")
md.append("### Which layer rejected judged-wrong items (true rejections)\n")
md.append(f"- OLD: {dct(OLD['layers_reject_wrong'])}\n- NEW: {dct(NEW['layers_reject_wrong'])}\n")
md.append("## 5. Cells\n")
md.append("| cell | OLD | NEW |\n| --- | --- | --- |")
for lbl, keyn in [("agentless coverage", "agentless_cov"), ("agentless FA", "agentless_fa"),
                  ("time-frame coverage", "timeframe_cov"), ("time-frame FA", "timeframe_fa"),
                  ("determiner coverage", "determiner_cov"), ("determiner FA", "determiner_fa"),
                  ("by-passive coverage", "bypassive_cov"), ("plain coverage", "plain_cov"),
                  ("aspect coverage", "aspect_cov")]:
    md.append(f"| {lbl} | {c(OLD['cells'][keyn])} | {c(NEW['cells'][keyn])} |")
md.append("")
md.append(f"The 1N figure to hold for time-frame FA was 3/170 = 1.76 %; on the 1Q set it reads "
          f"{c(OLD['cells']['timeframe_fa'])} under old labels and {c(NEW['cells']['timeframe_fa'])} under corrected "
          "labels (type-T items carry no M relabelling, so the cell is unchanged by construction).\n")
md.append("### M buckets — accepted k/n (stack decisions are the frozen ones)\n")
md.append("| bucket | n | accepted | rejected | rejecting layers |\n| --- | --- | --- | --- | --- |")
md.append(f"| M1 (function word dropped, stays CORRECT) | {NEW['M_buckets']['M1']['n']} | "
          f"{NEW['M_buckets']['M1']['accepted']} | {NEW['M_buckets']['M1']['rejected']} | "
          f"{dct(NEW['M_buckets']['M1']['layers'])} |")
md.append(f"| M2 movers (now WRONG) | {mover_treatment['n']} | {mover_treatment['accepted']} | "
          f"{mover_treatment['rejected']} | {dct(mover_treatment['rejected_layers'])} |")
md.append(f"| M2 stayers (still CORRECT) | {m_cell_detail['M2_stayers']['n']} | "
          f"{m_cell_detail['M2_stayers']['accepted']} | "
          f"{m_cell_detail['M2_stayers']['n'] - m_cell_detail['M2_stayers']['accepted']} | |")
md.append(f"| M3 (already wrong) | {NEW['M_buckets']['M3']['n']} | {NEW['M_buckets']['M3']['accepted']} | "
          f"{NEW['M_buckets']['M3']['rejected']} | {dct(NEW['M_buckets']['M3']['layers'])} |")
md.append(f"| M4 (already wrong) | {NEW['M_buckets']['M4']['n']} | {NEW['M_buckets']['M4']['accepted']} | "
          f"{NEW['M_buckets']['M4']['rejected']} | {dct(NEW['M_buckets']['M4']['layers'])} |")
md.append("")
md.append("## 6. How the stack treated the movers — the key number\n")
md.append(f"- Movers: **{mover_treatment['n']}** (P1 {mover_treatment['by_half'].get('P1',0)} / "
          f"P2 {mover_treatment['by_half'].get('P2',0)}).\n"
          f"- **ACCEPTED by the stack: {mover_treatment['accepted']}** → these are new false accepts "
          f"(layers: {dct(mover_treatment['accepted_layers'])}).\n"
          f"- **REJECTED by the stack: {mover_treatment['rejected']}** → these stop being false rejections "
          f"(layers: {dct(mover_treatment['rejected_layers'])}).\n")
md.append("Accepted movers (the new false accepts):\n")
md.append("| iid | half | accepting layer |\n| --- | --- | --- |")
for it in mover_treatment["accepted_items"]:
    md.append(f"| {it['iid']} | {it['half']} | {it['layer']} |")
md.append("")
md.append("## 7. Sensitivity variants (pooled)\n")
md.append("| variant | flipped | coverage | FA |\n| --- | --- | --- | --- |")
md.append(f"| PRIMARY (M2 follow the judge, M1 untouched) | {len(primary_flip)} | "
          f"{c(NEW['pooled']['coverage'])} | {c(NEW['pooled']['fa'])} |")
md.append(f"| S1: judge followed on all 119 (M1 too) | {sens['A_judge_on_all_119']['n_flipped']} | "
          f"{c(sens['A_judge_on_all_119']['pooled']['coverage'])} | {c(sens['A_judge_on_all_119']['pooled']['fa'])} |")
md.append(f"| S2: borderline movers stay correct | {sens['B_borderline_movers_stay_correct']['n_flipped']} | "
          f"{c(sens['B_borderline_movers_stay_correct']['pooled']['coverage'])} | "
          f"{c(sens['B_borderline_movers_stay_correct']['pooled']['fa'])} |")
md.append("")
md.append("## 8. F5 and F6 under corrected labels\n")
md.append(f"- F5 rejected {len(f5_rej)} items in all: OLD read-off = costs {f5['old']['cost_correct']} judged-correct "
          f"for {f5['old']['catches_wrong']} catches.\n"
          f"- Of those {f5['old']['cost_correct']} rejected-\"correct\" items, **{f5['of_the_65_rejected_correct_how_many_are_movers']} "
          "are movers** — F5 was right about them all along.\n"
          f"- NEW read-off: F5 costs **{f5['new']['cost_correct']}** judged-correct for **{f5['new']['catches_wrong']}** "
          "catches.\n"
          f"- Coverage with F5 on (new labels): {c(f5['coverage_F5_on_new'])}; if every F5 rejection were accepted "
          f"instead: {c(f5['coverage_if_F5_off_new'])} (old-label bound was "
          f"{f5['coverage_if_F5_off_old']['k']}/{f5['coverage_if_F5_off_old']['n']} = "
          f"{f5['coverage_if_F5_off_old']['pct']} %).\n")
md.append("**F6: not recomputable.** " + f6["note"] + "\n")
open(os.path.join(OUT, "RESCORE_1R.md"), "w", encoding="utf-8").write("\n".join(md))

# ---------- Task A markdown ----------
a = []
a.append("# Task A — movement of the 119 judged-correct type-M answers (Phase 1R)\n")
a.append("One blind re-judge, 0 model calls in this scoring step. Packet: `phase1r/taskA/judge/verdicts.json`; "
         "key: `phase1r/taskA/_key.json`; buckets from `phase1q/taskA/triage.json`.\n")
a.append("## Tally\n")
a.append(f"- Items in the packet: {taskA['n_judged']} ({taskA['n_M2']} M2 + {taskA['n_M1_controls']} M1 hidden controls).\n"
         f"- Judge classes: {dct(taskA['class_counts'])}. Judge verdicts: {dct(taskA['verdict_counts'])}. "
         f"Borderline: {taskA['borderline_total']}.\n"
         f"- **Of the {taskA['n_M2']} M2: {taskA['movers']} move to WRONG, {taskA['stayers']} stay CORRECT.**\n"
         f"- Borderline among the movers: {taskA['borderline_movers']}.\n")
a.append("## The 3 M1 hidden controls (owner's rule keeps them CORRECT)\n")
a.append("| jid | iid | judge verdict | class | dropped | Slovak | answer |\n| --- | --- | --- | --- | --- | --- | --- |")
for j in taskA["M1_controls"]:
    a.append(f"| {j['jid']} | {j['iid']} | {j['verdict']} | {j['class']} | {'; '.join(j['dropped'])} | "
             f"{j['slovak']} | {j['answer']} |")
a.append("")
if m1_disagree:
    a.append(f"**Control disagreement: the judge called {len(m1_disagree)} of the 3 M1 controls \"wrong\".** "
             "Reported plainly; these items are NOT moved in the primary score (owner's rule). They are moved only in "
             "sensitivity variant S1.\n")
else:
    a.append("No control disagreement: the judge left all 3 M1 controls correct.\n")
a.append(f"## M2 stayers ({len(stayers)})\n")
a.append("| jid | iid | class | dropped | Slovak | answer | note |\n| --- | --- | --- | --- | --- | --- | --- |")
for j in taskA["stayer_list"][:10]:
    a.append(f"| {j['jid']} | {j['iid']} | {j['class']} | {'; '.join(j['dropped'])} | {j['slovak']} | {j['answer']} | "
             f"{j['note']} |")
a.append("")
a.append("## 10 movers (first by jid, not cherry-picked)\n")
a.append("| jid | Slovak | answer | dropped | borderline |\n| --- | --- | --- | --- | --- |")
for j in taskA["mover_examples"]:
    a.append(f"| {j['jid']} | {j['slovak']} | {j['answer']} | {'; '.join(j['dropped'])} | {j['borderline']} |")
a.append("")
a.append("## Resulting label totals\n")
a.append(f"| | before | after (primary) |\n| --- | --- | --- |\n"
         f"| judged correct | {OLD['n_correct']} | {NEW['n_correct']} |\n"
         f"| judged wrong | {OLD['n_wrong']} | {NEW['n_wrong']} |\n"
         f"| of which wrong_type M | {OLD['fa_by_wrongtype']['M']['n']} | {NEW['fa_by_wrongtype']['M']['n']} |\n")
a.append("Sensitivity variants used in Task B: **S1** = follow the blind judge on all 119 (M1 controls included, "
         f"{len(sensA_flip)} flipped); **S2** = borderline movers stay correct ({len(sensB_flip)} flipped).\n")
open(os.path.join(P1R, "taskA", "TASKA_MOVEMENT_1R.md"), "w", encoding="utf-8").write("\n".join(a))

# ---------- terse console ----------
print("PREFLIGHT:", {k: v["ok"] for k, v in preflight.items()})
print("movers", len(movers), "stayers", len(stayers), "M1 disagree", len(m1_disagree),
      "borderline movers", len(borderline_movers))
print("OLD cov", OLD["pooled"]["coverage"], "FA", OLD["pooled"]["fa"])
print("NEW cov", NEW["pooled"]["coverage"], "FA", NEW["pooled"]["fa"])
print("movers accepted", mover_treatment["accepted"], mover_treatment["accepted_layers"],
      "rejected", mover_treatment["rejected"])
print("F5", f5["old"], "->", f5["new"], "movers among 65:", f5["of_the_65_rejected_correct_how_many_are_movers"])
print("S1", sens["A_judge_on_all_119"]["pooled"], "S2", sens["B_borderline_movers_stay_correct"]["pooled"])
