#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 1V / Track C runner. Re-runs phase1t/taskB/cz_validate.py UNCHANGED (its source text is executed
as-is; only the output path is redirected and, for the Czech side, the guard modules are swapped for the
Czech reader). Slovak control always runs on the original Slovak modules. 0 model calls."""
import os, io, sys, json, hashlib, contextlib

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.join(BASE, "phase1v", "trackC")
VAL = os.path.join(BASE, "phase1t", "taskB", "cz_validate.py")
sys.path.insert(0, HERE)
import cz_reader as CZ  # noqa: E402

WATCH = list(CZ.SRC.values()) + ["phase1t/taskB/cz_validate.py", "phase1t/taskB/cz_validation.json",
                                 "phase1t/taskB/cz_gold.json", "phase1t/taskB/sk_gold.json",
                                 "phase1t/taskB/cz_sample_numbered.json"]
H_BEFORE = {r: CZ.sha(r) for r in WATCH}

SRC = open(VAL, encoding="utf-8").read()
head, tail = SRC.split("\nout = []\n", 1)
tail = "out = []\n" + tail
for old, new in (("        text = r[lang]\n", "        text = r[lang]\n        _swap(lang)\n"),
                 ('os.path.join(HERE, "cz_validation.json")', "OUTPATH")):
    assert tail.count(old) == 1, old
    tail = tail.replace(old, new)


def run(label, fixes):
    ns = {"__name__": "cz_validate_1v", "__file__": VAL}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(head, VAL, "exec"), ns)
        sk_mods = {k: ns[k] for k in ("f9", "CK", "V2", "V3")}
        cz_mods = CZ.build(fixes) if fixes is not None else sk_mods

        def _swap(lang):
            ns.update(cz_mods if lang == "cz" else sk_mods)
        ns["_swap"] = _swap
        ns["OUTPATH"] = os.path.join(HERE, "cz_validation_%s.json" % label)
        exec(compile(tail, VAL, "exec"), ns)
    return ns["summary"], ns["out"]


def cp(k, n, a=0.05):
    try:
        from scipy.stats import beta
        lo = 0.0 if k == 0 else beta.ppf(a / 2, k, n - k + 1)
        hi = 1.0 if k == n else beta.ppf(1 - a / 2, k + 1, n - k)
        return round(100 * lo, 1), round(100 * hi, 1)
    except ImportError:
        return None


RUNS = [("before", None), ("fix_em", ["em"]), ("fix_se", ["se"]), ("fix_jestli", ["jestli"]),
        ("fix_aspect", ["aspect"]), ("after", list(CZ.ALL_FIXES))]
res = {lab: run(lab, fx) for lab, fx in RUNS}

old = json.load(open(os.path.join(BASE, "phase1t/taskB/cz_validation.json"), encoding="utf-8"))
same_as_1t = json.dumps(old["summary"], sort_keys=True, ensure_ascii=False) == \
    json.dumps(res["before"][0], sort_keys=True, ensure_ascii=False, default=str)
sk_rows = {lab: json.dumps([r["sk"] for r in out], sort_keys=True, ensure_ascii=False, default=str)
           for lab, (s, out) in res.items()}
sk_identical = {lab: sk_rows[lab] == sk_rows["before"] for lab in sk_rows}
sk_identical_1t = sk_rows["before"] == json.dumps([r["sk"] for r in old["rows"]], sort_keys=True,
                                                  ensure_ascii=False, default=str)

GUARDS = [("g1 F9", "g1_f9"), ("g2 F4v2", "g2_f4v2"), ("g3 AG v2", "g3_v2"), ("g3 AG v3", "g3_v3"),
          ("g4 voice v2", "g4_v2"), ("g4 voice v3", "g4_v3")]


def cell(summary, key, lang):
    d = summary[key][lang] if summary.get(key) else {}
    ag = d.get("AGREE", 0)
    co = d.get("CONSERVATIVE", 0)
    er = sum(v for k, v in d.items() if k.startswith("ERROR"))
    split = {k: v for k, v in d.items() if k.startswith("ERROR_")}
    return ag, co, er, split


table = []
for gname, key in GUARDS:
    for lab in ("before", "fix_em", "fix_se", "fix_jestli", "fix_aspect", "after"):
        ag, co, er, split = cell(res[lab][0], key, "cz")
        table.append({"guard": gname, "lang": "cz", "run": lab, "agree": ag, "conservative": co,
                      "error": er, "error_split": split, "error_ci": cp(er, 120)})
    for lab in ("before", "after"):
        ag, co, er, split = cell(res[lab][0], key, "sk")
        table.append({"guard": gname, "lang": "sk", "run": lab, "agree": ag, "conservative": co,
                      "error": er, "error_split": split, "error_ci": cp(er, 120)})


def rowinfo(out, n):
    r = [x for x in out if x["n"] == n][0]["cz"]
    return {"text": r["text"][:110], "g1": [r["g1"]["frames"], r["g1"]["gold"], r["g1"]["class"],
                                             r["g1"]["reason"]],
            "g2": [r["g2"]["person"], r["g2"]["number"], r["g2"]["gold"], r["g2"]["class"],
                   r["g2"]["signals"]],
            "g3": [r["g3_v2"]["agent"], r["g3_v2"]["class"]],
            "g4": [r["g4"]["gold_voice"], r["g4"]["class_v2"], r["g4"]["class_v3"]]}


targets = {}
b_out, a_out = res["before"][1], res["after"][1]
for n in sorted({15, 29, 17, 21, 61, 79, 80, 83, 87, 105, 112, 102, 120}):
    targets[n] = {"before": rowinfo(b_out, n), "after": rowinfo(a_out, n)}

# every Czech cell that changed class, per guard, before -> after
changes = {}
for gname, key, sub in (("g1", "g1", "class"), ("g2", "g2", "class"), ("g3_v2", "g3_v2", "class"),
                        ("g3_v3", "g3_v3", "class"), ("g4_v2", "g4", "class_v2"), ("g4_v3", "g4", "class_v3")):
    lst = []
    for rb, ra in zip(b_out, a_out):
        cb, ca = (rb["cz"][key] or {}).get(sub), (ra["cz"][key] or {}).get(sub)
        if cb != ca:
            lst.append([rb["n"], cb, ca, rb["cz"]["gold"].get("voice") if key == "g4" else None])
    changes[gname] = lst

probes = {lab: {"instrumental_em": len(res[lab][0]["probes"]["f4v2_instrumental_em"]["cz"]),
                "instrumental_em_false_class": [x[0] for x in res[lab][0]["probes"]["f4v2_instrumental_em"]["cz"]
                                                if x[5] == "ERROR"],
                "se_missed": len(res[lab][0]["probes"]["reflex_se_missed"]["cz"]),
                "se_missed_gold_nonactive": [x[0] for x in res[lab][0]["probes"]["reflex_se_missed"]["cz"]
                                             if x[1] in ("passive", "reflexive_passive", "impersonal")],
                "e2e_rejections": res[lab][0]["e2e_rejections"], "e2e_crashes": res[lab][0]["e2e_crashes"]}
          for lab in ("before", "after")}

H_AFTER = {r: CZ.sha(r) for r in WATCH}
report = {"model_calls": 0, "same_as_1t_summary": same_as_1t, "sk_control_identical_to_before": sk_identical,
          "sk_before_identical_to_1t_rows": sk_identical_1t,
          "hash_before": H_BEFORE, "hash_after": H_AFTER, "hash_unchanged": H_BEFORE == H_AFTER,
          "table": table, "targets": targets, "changes_before_to_after": changes, "probes": probes}
json.dump(report, open(os.path.join(HERE, "trackC_results.json"), "w", encoding="utf-8"), ensure_ascii=False,
          indent=1, default=str)

print("same_as_1t", same_as_1t, "| sk identical", sk_identical, "| sk==1t rows", sk_identical_1t,
      "| hashes unchanged", H_BEFORE == H_AFTER)
for t in table:
    print("%-12s %s %-10s A%3d C%3d E%3d %s %s" % (t["guard"], t["lang"], t["run"], t["agree"], t["conservative"],
                                                  t["error"], t["error_ci"], t["error_split"] or ""))
print("CHANGES", json.dumps(changes, ensure_ascii=False))
print("PROBES", json.dumps({k: {kk: vv for kk, vv in v.items() if not kk.startswith("e2e")} for k, v in probes.items()}))
print("E2E", json.dumps({k: v["e2e_rejections"] for k, v in probes.items()}), json.dumps({k: v["e2e_crashes"] for k, v in probes.items()}))
for n, v in targets.items():
    print("T", n, json.dumps(v, ensure_ascii=False))
for r, h in H_BEFORE.items():
    print("H", r, h[:16])
