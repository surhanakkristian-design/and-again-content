#!/usr/bin/env python3
"""Phase 1T Task A - regression of AG v3 against AG v2.  0 model calls, 0 network, no DB.
Reads phase1p/ (source data), phase1s/taskA/rows_1s.json, phase1s/taskC/judge/ + _key.json.
Writes ONLY phase1t/taskA/AG_V3_REGRESSION.{json,md}.

Gate 1: the 183-item blind-judge packet of 1S Task C (97 agentless agent drops judged wrong,
        42 by-passive controls, 39 judged-correct plain controls, 3 judged-correct AG-v2 misfires,
        1 agentless item the judge called correct).
Gate 2: all 1,080 items of the 1Q set, K3 stack (lever 1 off + AG), labels RUL' = label_1r with the
        judge's WRONG verdicts folded in - exactly the label set of phase1s/taskC.
        This 1Q set is DESIGN-only: it is the set the rule was built on, never a held-out result.
"""
import json
import os
import sys
from collections import Counter

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.dirname(os.path.abspath(__file__))
P1P, P1R, TA1S, TC1S = (os.path.join(BASE, "phase1p"), os.path.join(BASE, "phase1r"),
                        os.path.join(BASE, "phase1s", "taskA"), os.path.join(BASE, "phase1s", "taskC"))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(BASE, "phase1s"))
import agent_drop_v3 as V3                                                     # noqa: E402
from agent_drop_v3 import V2                                                   # noqa: E402
from safe_json import safe_dump                                                # noqa: E402
import preflight_v3                                                            # noqa: E402

L = lambda p: json.load(open(p, encoding="utf-8"))
_src = open(os.path.join(P1R, "taskB", "rescore_1r.py"), encoding="utf-8").read()
_g = {}
exec(compile(_src.split("# ---------- data ----------")[0], "hdr", "exec"), _g)
cp, kn = _g["cp"], _g["kn"]

CONFIGS = [("AG v2", None), ("v2+clause", ("clause",)), ("v2+subj", ("subj",)),
           ("v2+by", ("by",)), ("AG v3 (all)", ("clause", "subj", "by"))]
DET_LAYERS_AFTER_AG = {"L3", "L3:TIPrej"}


def c(d):
    return "-" if not d or not d["n"] else "%d/%d = %.2f %% [%.2f, %.2f]" % (
        d["k"], d["n"], d["pct"], d["ci"][0], d["ci"][1])


def main():
    ok, pf_lines = preflight_v3.main(verbose=True)
    if not ok:
        print("ABORT: pre-flight failed")
        sys.exit(2)

    rows = L(os.path.join(TA1S, "rows_1s.json"))
    byiid = {r["iid"]: r for r in rows}
    sents = {s["sid"]: s for s in L(os.path.join(P1P, "data", "sentences.json"))}
    ann = L(os.path.join(P1P, "data", "annotations.json"))
    items = {it["id"]: it for it in L(os.path.join(P1P, "data", "items.json"))}
    key = L(os.path.join(TC1S, "_key.json"))
    verd = {v["jid"]: v for v in L(os.path.join(TC1S, "judge", "verdicts.json"))}

    # ---------------- AG decisions per configuration
    dec = {name: {} for name, _ in CONFIGS}
    for iid, it in items.items():
        s = sents[it["sid"]]
        a = ann.get(str(it["sid"])) or {}
        wt = (s.get("tags") or {}).get("writer_tags") or {}
        ref = ((a.get("hygienised") or a).get("v") or [""])[0]
        for name, fl in CONFIGS:
            dec[name][iid] = (V2.decide(s["slovak"], a, wt, it["answer"], ref, "primary") if fl is None
                              else V3.decide(s["slovak"], a, wt, it["answer"], ref, "primary", fl))

    # ---------------- gate 1: the judge packet
    packet = {}
    for name, _ in CONFIGS:
        buckets = {}
        for jid, k in key.items():
            iid, b = k["iid"], k["bucket"]
            v = verd[jid]["verdict"]
            grp = ("agent drops (judged wrong)" if (b == "agentless" and v == "wrong") else
                   "agentless judged CORRECT" if b == "agentless" else
                   "by-passive controls" if b == "by-passive-control" else
                   "plain controls (judged correct)" if (b == "plain-control" and v == "correct") else
                   "plain control judged wrong" if b == "plain-control" else
                   "v2 misfires (judged correct)")
            e = buckets.setdefault(grp, {"n": 0, "fired": 0, "fired_items": [], "missed": []})
            e["n"] += 1
            d = dec[name][iid]
            if d["fired"]:
                e["fired"] += 1
                e["fired_items"].append(iid)
            else:
                e["missed"].append({"iid": iid, "slovak": byiid[iid]["slovak"],
                                    "answer": byiid[iid]["answer"], "why": d["reason"]})
        packet[name] = buckets

    # ---------------- gate 2: all 1,080 rows, RUL' labels, K3 stack
    lab = {r["iid"]: (r["label_1r"], r["label_1r_type"]) for r in rows}
    for jid, k in key.items():
        if str(verd[jid]["verdict"]).lower() == "wrong":
            lab[k["iid"]] = ("wrong", "M")

    def stack(name):
        out = {}
        for r in rows:
            i = r["iid"]
            off_a, off_l = r["lever1_off_accept"], r["lever1_off_layer"]
            if dec[name][i]["fired"]:
                out[i] = (False, off_l if (not off_a and off_l not in DET_LAYERS_AFTER_AG) else "AG")
            else:
                out[i] = (off_a, off_l)
        return out

    full = {}
    stacks = {name: stack(name) for name, _ in CONFIGS}
    for name, _ in CONFIGS:
        st = stacks[name]
        cor = [r for r in rows if lab[r["iid"]][0] == "correct"]
        wro = [r for r in rows if lab[r["iid"]][0] == "wrong"]
        ag_w = [r for r in wro if "agentless" in r["tags"]]
        ag_c = [r for r in cor if "agentless" in r["tags"]]
        cost = [{"iid": r["iid"], "slovak": r["slovak"], "answer": r["answer"],
                 "was_accepted_without_AG": bool(r["lever1_off_accept"]),
                 "why": dec[name][r["iid"]]["reason"]}
                for r in cor if dec[name][r["iid"]]["fired"]]
        base = dec["AG v2"]
        new_catch = [{"iid": r["iid"], "answer": r["answer"], "label": lab[r["iid"]][0],
                      "why": dec[name][r["iid"]]["reason"]}
                     for r in rows if dec[name][r["iid"]]["fired"] and not base[r["iid"]]["fired"]]
        lost = [{"iid": r["iid"], "answer": r["answer"], "label": lab[r["iid"]][0],
                 "why": dec[name][r["iid"]]["reason"]}
                for r in rows if base[r["iid"]]["fired"] and not dec[name][r["iid"]]["fired"]]
        full[name] = {
            "ag_firings": sum(1 for r in rows if dec[name][r["iid"]]["fired"]),
            "coverage": kn(sum(1 for r in cor if st[r["iid"]][0]), len(cor)),
            "fa": kn(sum(1 for r in wro if st[r["iid"]][0]), len(wro)),
            "agentless_coverage": kn(sum(1 for r in ag_c if st[r["iid"]][0]), len(ag_c)),
            "agentless_fa": kn(sum(1 for r in ag_w if st[r["iid"]][0]), len(ag_w)),
            "measured_cost_correct_rows_AG_rejects": len(cost),
            "measured_cost_flipping_an_accept": sum(1 for x in cost if x["was_accepted_without_AG"]),
            "cost_rows": cost,
            "new_catches_vs_v2": new_catch, "n_new_catches_vs_v2": len(new_catch),
            "firings_lost_vs_v2": lost, "n_firings_lost_vs_v2": len(lost),
            "false_rejections_by_layer": dict(Counter(st[r["iid"]][1] for r in cor if not st[r["iid"]][0])),
        }

    OUT = {"what": "Phase 1T Task A - AG v3 regression (deterministic)", "date": "2026-09-19",
           "model_calls": 0, "network_calls": 0,
           "design_only": ("the 1,080-item 1Q set and the 183-item judge packet are the sets AG v3 was "
                           "BUILT on - DESIGN numbers, not a held-out measurement"),
           "preflight": pf_lines, "configs": [n for n, _ in CONFIGS],
           "packet_gate": packet, "full_set": full}
    safe_dump(OUT, os.path.join(HERE, "AG_V3_REGRESSION.json"))

    # ---------------- markdown
    GRPS = ["agent drops (judged wrong)", "by-passive controls", "plain controls (judged correct)",
            "v2 misfires (judged correct)", "agentless judged CORRECT", "plain control judged wrong"]
    md = ["# Phase 1T Task A - AG v3 regression (0 model calls, 0 network)\n",
          "**DESIGN-only.** Both gates use sets AG v3 was built on (the 1S judge packet and the "
          "closed 1Q set). Nothing here is a held-out measurement.\n",
          "Flags: `clause` (clause-aware test), `subj` (subject-NP reader + agent-string parsing), "
          "`by` (instrument != agent). `flags=()` reproduces AG v2 bit for bit (pre-flight row 22).\n",
          "## Pre-flight (synthetic rows only)\n", "```"] + pf_lines + ["```\n",
          "## Gate 1 - the 183-item blind-judge packet (fired counts)\n",
          "| config | " + " | ".join("%s (n=%d)" % (g, packet["AG v2"][g]["n"]) for g in GRPS) + " |",
          "| --- |" + " --- |" * len(GRPS)]
    for name, _ in CONFIGS:
        md.append("| %s | %s |" % (name, " | ".join(str(packet[name][g]["fired"]) for g in GRPS)))
    md += ["", "Wanted: column 1 as high as possible; columns 2-5 exactly 0 (they are judged-correct "
               "answers, every firing is a measured cost); column 6 is the one plain control the judge "
               "called wrong.\n",
           "### remaining misses of AG v3 among the 97 judged agent drops\n",
           "| iid | Slovak | answer | why AG v3 abstains |", "| --- | --- | --- | --- |"]
    for m in packet["AG v3 (all)"]["agent drops (judged wrong)"]["missed"]:
        md.append("| %s | %s | %s | %s |" % (m["iid"], m["slovak"], m["answer"], m["why"]))
    md += ["", "## Gate 2 - all 1,080 items of the 1Q set, K3 stack, labels RUL' (judge-folded)\n",
           "| config | AG firings | coverage | FA | agentless coverage | agentless FA |",
           "| --- | --- | --- | --- | --- | --- |"]
    for name, _ in CONFIGS:
        f = full[name]
        md.append("| %s | %d | %s | %s | %s | %s |" % (name, f["ag_firings"], c(f["coverage"]),
                                                       c(f["fa"]), c(f["agentless_coverage"]),
                                                       c(f["agentless_fa"])))
    md += ["", "| config | judged-correct rows AG rejects (MEASURED COST) | of them: flip an accept "
               "into a rejection | new firings vs v2 | v2 firings dropped |",
           "| --- | --- | --- | --- | --- |"]
    for name, _ in CONFIGS:
        f = full[name]
        md.append("| %s | %d | %d | %d | %d |" % (name, f["measured_cost_correct_rows_AG_rejects"],
                                                  f["measured_cost_flipping_an_accept"],
                                                  f["n_new_catches_vs_v2"], f["n_firings_lost_vs_v2"]))
    md += ["", "### MEASURED COST - every judged-correct item AG v3 rejects\n",
           "| iid | Slovak | answer | flips an accept? | why |", "| --- | --- | --- | --- | --- |"]
    for x in full["AG v3 (all)"]["cost_rows"]:
        md.append("| %s | %s | %s | %s | %s |" % (x["iid"], x["slovak"], x["answer"],
                                                  "YES" if x["was_accepted_without_AG"] else "no",
                                                  x["why"]))
    if not full["AG v3 (all)"]["cost_rows"]:
        md.append("| - | - | none | - | - |")
    JC = ["by-passive controls", "plain controls (judged correct)", "v2 misfires (judged correct)",
          "agentless judged CORRECT"]
    md += ["", "### JUDGE-VERIFIED cost - judged-correct packet items AG v3 rejects\n",
           "| group | iid | Slovak | answer |", "| --- | --- | --- | --- |"]
    _n = 0
    for g in JC:
        for iid in packet["AG v3 (all)"][g]["fired_items"]:
            _n += 1
            md.append("| %s | %s | %s | %s |" % (g, iid, byiid[iid]["slovak"], byiid[iid]["answer"]))
            print("JUDGE-VERIFIED COST %s | %s | %s || %s" % (g, iid, byiid[iid]["slovak"], byiid[iid]["answer"]))
    if not _n:
        md.append("| - | - | none | - |")
    md += ["", "### new catches of AG v3 that AG v2 did not fire on (%d)\n"
           % full["AG v3 (all)"]["n_new_catches_vs_v2"],
           "| iid | answer | RUL' label |", "| --- | --- | --- |"]
    _nc = full["AG v3 (all)"]["new_catches_vs_v2"]
    for x in _nc[:18]:
        md.append("| %s | %s | %s |" % (x["iid"], x["answer"], x["label"]))
    if len(_nc) > 18:
        md.append("| ... | +%d more - full list in AG_V3_REGRESSION.json | |" % (len(_nc) - 18))
    md += ["", "### v2 firings AG v3 drops (%d)\n" % full["AG v3 (all)"]["n_firings_lost_vs_v2"],
           "| iid | answer | RUL' label | why v3 abstains |", "| --- | --- | --- | --- |"]
    for x in full["AG v3 (all)"]["firings_lost_vs_v2"]:
        md.append("| %s | %s | %s | %s |" % (x["iid"], x["answer"], x["label"], x["why"]))
    open(os.path.join(HERE, "AG_V3_REGRESSION.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")

    for name, _ in CONFIGS:
        f = full[name]
        print("%-12s fired %3d | cov %-26s FA %-24s | cost %d (flips %d) | new %d lost %d | packet drops %d/%d"
              % (name, f["ag_firings"], c(f["coverage"]), c(f["fa"]),
                 f["measured_cost_correct_rows_AG_rejects"], f["measured_cost_flipping_an_accept"],
                 f["n_new_catches_vs_v2"], f["n_firings_lost_vs_v2"],
                 packet[name]["agent drops (judged wrong)"]["fired"],
                 packet[name]["agent drops (judged wrong)"]["n"]))
        print("             controls fired: by-passive %d/42, plain-correct %d/39, misfires %d/3, agentless-correct %d/1"
              % (packet[name]["by-passive controls"]["fired"],
                 packet[name]["plain controls (judged correct)"]["fired"],
                 packet[name]["v2 misfires (judged correct)"]["fired"],
                 packet[name]["agentless judged CORRECT"]["fired"]))
    print("\nremaining misses (v3):")
    for m in packet["AG v3 (all)"]["agent drops (judged wrong)"]["missed"]:
        print("  %s | %s || %s || %s" % (m["iid"], m["slovak"], m["answer"], m["why"]))
    print("\nMEASURED COST rows (v3):")
    for x in full["AG v3 (all)"]["cost_rows"]:
        print("  %s | %s || %s || flips=%s | %s" % (x["iid"], x["slovak"], x["answer"],
                                                    x["was_accepted_without_AG"], x["why"]))


if __name__ == "__main__":
    main()
