#!/usr/bin/env python3
"""Phase 1S Task C3/C4 - configuration x LABEL-SET re-score of the closed 1Q set.
0 model calls, 0 network, no DB. Reads phase1p/, phase1q/, phase1r/, phase1s/taskA/.
Writes only phase1s/taskC/.

  configurations: K0 (1Q as closed, lever 1 ON) | K1 (lever 1 off, no AG) | K2 (lever 1 off + AG v1)
                  K3 (lever 1 off + AG v2 = the new base) | K3+TIPall | K3+TIPfunc | K3+TIPfunc+adv
  label sets:     1R (label_1r) | S2 (label_s2) | RDET / RDET+S2 (CIRCULAR stand-ins: AG v2 grades
                  itself) | RUL / RUL+S2 (the blind judge's verdicts, via --judge)
"""
import argparse, difflib, json, os, re, sys
from collections import Counter

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
TA, TC = os.path.join(BASE, "phase1s", "taskA"), os.path.join(BASE, "phase1s", "taskC")
P1I, P1R = os.path.join(BASE, "phase1i"), os.path.join(BASE, "phase1r")
sys.path.insert(0, TC)
sys.path.insert(0, P1I)
from ag_apply import ag_maps, variants

L = lambda p: json.load(open(p, encoding="utf-8"))

# cp() / kn() / fisher_exact() verbatim from phase1r/taskB/rescore_1r.py (header only, no writes)
_src = open(os.path.join(P1R, "taskB", "rescore_1r.py"), encoding="utf-8").read()
_g = {}
exec(compile(_src.split("# ---------- data ----------")[0], "rescore_1r_header", "exec"), _g)
cp, kn, fisher_exact = _g["cp"], _g["kn"], _g["fisher_exact"]

import checker_1i as C1I
FUNCSET = set(C1I.NONINFO) | set(C1I.FUNCTION)               # pre-existing classes, not fitted here
FUNCSET_ADV = FUNCSET | set(C1I.ADVERBS) | set(C1I.INFO_FUNC)
ART = {"a", "an", "the"}
DET_LAYERS_AFTER_AG = {"L3", "L3:TIPrej"}
CONFIGS = ["K0", "K1", "K2", "K3", "K3+TIPall", "K3+TIPfunc", "K3+TIPfunc+adv"]


def jdef(o):
    if isinstance(o, (set, frozenset)):
        return sorted(o, key=str)
    if isinstance(o, tuple):
        return list(o)
    return str(o)


def dump(obj, path):
    json.dump(obj, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1, default=jdef)


# ---------------------------------------------------------------- the deterministic "difference"
def tok(s):
    return [w for w in re.findall(r"[a-z']+", (s or "").lower())]


def difference(answer, refs):
    """Tokens that differ between the answer and its CLOSEST reference variant, both directions
    (dropped from the reference AND added/substituted in the answer). Articles are free.
    difflib on lowercased tokens; the closest variant = the one with the fewest differing tokens."""
    A = [t for t in tok(answer) if t not in ART]
    best = None
    for ref in (refs or [""]):
        R = [t for t in tok(ref) if t not in ART]
        d = set()
        for tg, i1, i2, j1, j2 in difflib.SequenceMatcher(a=R, b=A, autojunk=False).get_opcodes():
            if tg != "equal":
                d |= set(R[i1:i2]) | set(A[j1:j2])
        if best is None or len(d) < len(best[0]):
            best = (d, ref)
    return best[0], best[1]


# ---------------------------------------------------------------- label sets
def label_map(rows, base):
    f = {"1R": ("label_1r", "label_1r_type"), "S2": ("label_s2", "label_s2_type")}[base]
    return {r["iid"]: (r[f[0]], r[f[1]]) for r in rows}


def labels_from_judge(verdicts_path, key_path, base_map):
    """A packet item judged WRONG by the blind judge flips to wrong (type M); everything else keeps
    the base label. -> dict iid -> (label, wrong_type)."""
    v = L(verdicts_path)
    v = v["verdicts"] if isinstance(v, dict) and "verdicts" in v else v
    vby = {x["jid"]: x for x in v} if isinstance(v, list) else {k: {"jid": k, **x} for k, x in v.items()}
    key = L(key_path)
    out = dict(base_map)
    flipped = []
    for jid, k in key.items():
        d = vby.get(jid)
        if d and str(d.get("verdict", "")).lower() == "wrong":
            out[k["iid"]] = ("wrong", "M")
            flipped.append(k["iid"])
    return out, flipped


def labels_rdet(rows, base_map, ag2):
    """CIRCULAR stand-in: every judged-correct row on which AG v2 fires flips to wrong."""
    out, flipped = dict(base_map), []
    for r in rows:
        i = r["iid"]
        if out[i][0] == "correct" and ag2[i]["fired"]:
            out[i] = ("wrong", "M")
            flipped.append(i)
    return out, flipped


# ---------------------------------------------------------------- metrics
def kn2(k, n):
    return kn(k, n)


def pack(rs, acc, lab):
    cor = [r for r in rs if lab[r["iid"]][0] == "correct"]
    wro = [r for r in rs if lab[r["iid"]][0] == "wrong"]
    return {"coverage": kn2(sum(1 for r in cor if r[acc]), len(cor)),
            "fa": kn2(sum(1 for r in wro if r[acc]), len(wro))}


def full(rs, acc, lay, lab):
    d = {"pooled": pack(rs, acc, lab),
         "P1": pack([r for r in rs if r["half"] == "P1"], acc, lab),
         "P2": pack([r for r in rs if r["half"] == "P2"], acc, lab)}
    p1c, p2c, p1f, p2f = d["P1"]["coverage"], d["P2"]["coverage"], d["P1"]["fa"], d["P2"]["fa"]
    d["agreement"] = {
        "cov_fisher_p": round(fisher_exact(p1c["k"], p1c["n"] - p1c["k"], p2c["k"], p2c["n"] - p2c["k"]), 4),
        "fa_fisher_p": round(fisher_exact(p1f["k"], p1f["n"] - p1f["k"], p2f["k"], p2f["n"] - p2f["k"]), 4)}
    sub = [r for r in rs if "agentless" in r["tags"]]
    d["agentless"] = pack(sub, acc, lab)
    d["fa_by_wrongtype"] = {}
    for wt in ["T", "W", "M", "S"]:
        s2 = [r for r in rs if lab[r["iid"]][0] == "wrong" and lab[r["iid"]][1] == wt]
        d["fa_by_wrongtype"][wt] = kn2(sum(1 for r in s2 if r[acc]), len(s2))
    d["false_rejections_by_layer"] = dict(Counter(r[lay] for r in rs
                                                  if lab[r["iid"]][0] == "correct" and not r[acc]))
    d["false_accepts_by_layer"] = dict(Counter(r[lay] for r in rs
                                               if lab[r["iid"]][0] == "wrong" and r[acc]))
    d["true_rejections_by_layer"] = dict(Counter(r[lay] for r in rs
                                                 if lab[r["iid"]][0] == "wrong" and not r[acc]))
    fa = d["pooled"]["fa"]
    d["fa_crosses_5pct"] = bool(fa["n"] and fa["ci"][1] >= 5.0)
    return d


def c(d):
    return "-" if not d or not d["n"] else "%d/%d = %.2f %% [%.2f, %.2f]" % (
        d["k"], d["n"], d["pct"], d["ci"][0], d["ci"][1])


def dct(d):
    return ", ".join("%s %d" % (k, v) for k, v in sorted(d.items(), key=lambda kv: -kv[1])) or "-"


# ---------------------------------------------------------------- build the configurations
def build(rows, ag1, ag2, var):
    tip_detail = {}
    for r in rows:
        i = r["iid"]
        off_a, off_l = r["lever1_off_accept"], r["lever1_off_layer"]
        r["acc_K0"], r["lay_K0"] = r["accept_1q"], r["layer_1q"]
        r["acc_K1"], r["lay_K1"] = off_a, off_l
        for nm, ag in (("K2", ag1), ("K3", ag2)):
            if ag[i]["fired"]:
                r["acc_" + nm] = False
                r["lay_" + nm] = off_l if (not off_a and off_l not in DET_LAYERS_AFTER_AG) else "AG"
            else:
                r["acc_" + nm], r["lay_" + nm] = off_a, off_l
        # ---- TIP variants: only rows the K3 stack still rejects at L3:TIPrej; AG v2 always overrides
        is_tiprej = (r["lay_K3"] == "L3:TIPrej")
        diff, ref = difference(r["answer"], var.get(str(r["sid"])) or [r["reference"]])
        r["tip_diff"] = sorted(diff)
        r["tip_diff_ref"] = ref
        r["tip_all_func"] = all(t in FUNCSET for t in diff)
        r["tip_all_func_adv"] = all(t in FUNCSET_ADV for t in diff)
        for nm, cond in (("K3+TIPall", True), ("K3+TIPfunc", r["tip_all_func"]),
                         ("K3+TIPfunc+adv", r["tip_all_func_adv"])):
            if is_tiprej and cond:
                r["acc_" + nm], r["lay_" + nm] = True, "L3:TIPacc"
            else:
                r["acc_" + nm], r["lay_" + nm] = r["acc_K3"], r["lay_K3"]
        if is_tiprej:
            tip_detail[i] = r
    return tip_detail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--judge", default=None, help="path to the blind judge's verdicts.json")
    a = ap.parse_args()

    rows = L(os.path.join(TA, "rows_1s.json"))
    ag1, ag2 = ag_maps()
    var = variants()
    tip_rows = build(rows, ag1, ag2, var)

    base_1r, base_s2 = label_map(rows, "1R"), label_map(rows, "S2")
    labelsets = {"1R": base_1r, "S2": base_s2}
    rdet, rdet_flip = labels_rdet(rows, base_1r, ag2)
    rdet2, _ = labels_rdet(rows, base_s2, ag2)
    labelsets["RDET (CIRCULAR)"] = rdet
    labelsets["RDET+S2 (CIRCULAR)"] = rdet2
    judged_flipped = None
    if a.judge:
        rul, judged_flipped = labels_from_judge(a.judge, os.path.join(TC, "_key.json"), base_1r)
        rul2, _ = labels_from_judge(a.judge, os.path.join(TC, "_key.json"), base_s2)
        labelsets["RUL"] = rul
        labelsets["RUL+S2"] = rul2

    # ---------------- pre-flight against the closed numbers (label set 1R)
    pf = {}
    for cfgname, want in (("K0", (425, 483, 19, 597)), ("K2", (359, 483, 9, 597)),
                          ("K1", (401, 483, 9, 597))):
        d = full(rows, "acc_" + cfgname, "lay_" + cfgname, base_1r)
        got = (d["pooled"]["coverage"]["k"], d["pooled"]["coverage"]["n"],
               d["pooled"]["fa"]["k"], d["pooled"]["fa"]["n"])
        pf[cfgname] = {"want": list(want), "got": list(got), "ok": list(got) == list(want)}
    if not all(v["ok"] for v in pf.values()):
        dump({"ABORT": "pre-flight failed", "preflight": pf}, os.path.join(TC, "ABORT_1S_C.json"))
        print("ABORT pre-flight:", json.dumps(pf))
        sys.exit(2)
    print("pre-flight OK:", json.dumps({k: v["got"] for k, v in pf.items()}))

    # ---------------- the table
    table = {}
    for lsname, lab in labelsets.items():
        table[lsname] = {cfg: full(rows, "acc_" + cfg, "lay_" + cfg, lab) for cfg in CONFIGS}

    # ---------------- TIP variant detail
    tipinfo = {}
    for cfg in ("K3+TIPall", "K3+TIPfunc", "K3+TIPfunc+adv"):
        acc = [r for r in tip_rows.values() if r["acc_" + cfg]]
        e = {"n_tiprej_rows": len(tip_rows), "n_accepted": len(acc), "per_label_set": {}}
        for lsname, lab in labelsets.items():
            w = [r for r in acc if lab[r["iid"]][0] == "wrong"]
            e["per_label_set"][lsname] = {
                "accepted_correct": sum(1 for r in acc if lab[r["iid"]][0] == "correct"),
                "accepted_wrong_FA": len(w),
                "wrong_rows_let_in": [{"iid": r["iid"], "answer": r["answer"],
                                       "wrong_type": lab[r["iid"]][1],
                                       "difference": r["tip_diff"], "closest_ref": r["tip_diff_ref"]}
                                      for r in sorted(w, key=lambda x: x["iid"])]}
        tipinfo[cfg] = e

    ag_change = [{"iid": r["iid"], "answer": r["answer"], "slovak": r["slovak"],
                  "v1": ag1[r["iid"]]["fired"], "v2": ag2[r["iid"]]["fired"],
                  "v1_reason": ag1[r["iid"]]["reason"], "v2_reason": ag2[r["iid"]]["reason"],
                  "label_1r": r["label_1r"]}
                 for r in rows if ag1[r["iid"]]["fired"] != ag2[r["iid"]]["fired"]]

    OUT = {"what": "Phase 1S Task C - configurations x label sets, 0 model calls", "date": "2026-09-19",
           "model_calls": 0, "network_calls": 0,
           "note_RDET": "RDET / RDET+S2 are CIRCULAR: AG v2 grades itself. Bound only, never a result.",
           "tiprej_meaning": ("L3:TIPrej = the L3 model answered TIP (same meaning, but with a "
                              "reservation); the frozen stack runs tip_reject=True, so that acceptance "
                              "is turned into a rejection. The stored tip is the bare token 'TIP' - no "
                              "tip text, so the tip names no word."),
           "preflight": pf, "ag_v1_vs_v2_changes": ag_change,
           "ag_firings": {"v1": sum(1 for r in rows if ag1[r["iid"]]["fired"]),
                          "v2": sum(1 for r in rows if ag2[r["iid"]]["fired"])},
           "rdet_flipped_n": len(rdet_flip), "rdet_flipped": rdet_flip,
           "judge_flipped": judged_flipped, "table": table, "tip_variants": tipinfo,
           "configs": CONFIGS, "label_sets": list(labelsets)}
    suffix = "_JUDGED" if a.judge else ""
    dump(OUT, os.path.join(TC, "RESCORE_1S_C%s.json" % suffix))

    md = ["# Phase 1S Task C - configuration x label set (0 model calls)\n",
          OUT["tiprej_meaning"], "",
          "RDET / RDET+S2 are **CIRCULAR** (AG v2 grades itself) - a bound, not a result.\n",
          "AG v1 -> v2 changes: %d rows.\n" % len(ag_change)]
    for lsname in labelsets:
        md += ["## label set %s\n" % lsname,
               "| config | coverage | FA | FA crosses 5 % | agentless cov | agentless FA | P1/P2 cov p | P1/P2 FA p |",
               "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for cfg in CONFIGS:
            d = table[lsname][cfg]
            md.append("| %s | %s | %s | %s | %s | %s | %.4f | %.4f |" % (
                cfg, c(d["pooled"]["coverage"]), c(d["pooled"]["fa"]),
                "YES" if d["fa_crosses_5pct"] else "no", c(d["agentless"]["coverage"]),
                c(d["agentless"]["fa"]), d["agreement"]["cov_fisher_p"], d["agreement"]["fa_fisher_p"]))
        md += ["", "| config | FA T | FA W | FA M | FA S | false rejections by layer |",
               "| --- | --- | --- | --- | --- | --- |"]
        for cfg in CONFIGS:
            d = table[lsname][cfg]
            md.append("| %s | %s | %s | %s | %s | %s |" % (
                cfg, c(d["fa_by_wrongtype"]["T"]), c(d["fa_by_wrongtype"]["W"]),
                c(d["fa_by_wrongtype"]["M"]), c(d["fa_by_wrongtype"]["S"]),
                dct(d["false_rejections_by_layer"])))
        md.append("")
    md += ["## TIP variants\n",
           "| variant | TIPrej rows | accepted | label set | accepted correct | accepted wrong (FA) |",
           "| --- | --- | --- | --- | --- | --- |"]
    for cfg, e in tipinfo.items():
        for lsname, p in e["per_label_set"].items():
            md.append("| %s | %d | %d | %s | %d | %d |" % (cfg, e["n_tiprej_rows"], e["n_accepted"],
                                                           lsname, p["accepted_correct"], p["accepted_wrong_FA"]))
    md += ["", "### wrong rows let in (label set 1R)\n", "| variant | iid | answer | difference |",
           "| --- | --- | --- | --- |"]
    for cfg, e in tipinfo.items():
        for x in e["per_label_set"]["1R"]["wrong_rows_let_in"]:
            md.append("| %s | %s | %s | %s |" % (cfg, x["iid"], x["answer"], " ".join(x["difference"])))
    open(os.path.join(TC, "RESCORE_1S_C%s.md" % suffix), "w", encoding="utf-8").write("\n".join(md) + "\n")

    # ---------------- console
    print("AG firings v1 %d -> v2 %d; changed rows %d" % (OUT["ag_firings"]["v1"], OUT["ag_firings"]["v2"], len(ag_change)))
    for x in ag_change:
        print("  CHANGE %s | %s | v1=%s v2=%s | label_1r=%s | %s" % (x["iid"], x["answer"], x["v1"], x["v2"], x["label_1r"], x["v2_reason"]))
    for lsname in labelsets:
        print("\n== label set %s ==" % lsname)
        for cfg in CONFIGS:
            d = table[lsname][cfg]
            print("%-16s cov %-28s FA %-26s cross5 %-3s | agentless cov %-26s FA %-24s | p cov %.4f fa %.4f"
                  % (cfg, c(d["pooled"]["coverage"]), c(d["pooled"]["fa"]),
                     "YES" if d["fa_crosses_5pct"] else "no", c(d["agentless"]["coverage"]),
                     c(d["agentless"]["fa"]), d["agreement"]["cov_fisher_p"], d["agreement"]["fa_fisher_p"]))
            print("%-16s FA T %s W %s M %s S %s | falserej %s" % ("", c(d["fa_by_wrongtype"]["T"]),
                  c(d["fa_by_wrongtype"]["W"]), c(d["fa_by_wrongtype"]["M"]), c(d["fa_by_wrongtype"]["S"]),
                  dct(d["false_rejections_by_layer"])))
    print("\n== TIP variants ==")
    for cfg, e in tipinfo.items():
        print("%s: TIPrej rows %d, accepted %d" % (cfg, e["n_tiprej_rows"], e["n_accepted"]))
        for lsname, p in e["per_label_set"].items():
            print("   %-20s correct %3d  wrong(FA) %3d" % (lsname, p["accepted_correct"], p["accepted_wrong_FA"]))
        for x in e["per_label_set"]["1R"]["wrong_rows_let_in"]:
            print("   WRONG-IN(1R) %s | %s | diff: %s" % (x["iid"], x["answer"], " ".join(x["difference"])))
    print("\nRDET flips (CIRCULAR): %d" % len(rdet_flip))


if __name__ == "__main__":
    main()
