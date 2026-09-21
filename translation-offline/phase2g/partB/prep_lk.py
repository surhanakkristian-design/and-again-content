#!/usr/bin/env python3
"""B5 prep: every Czech row present in partB/out lacking a dedicated lk judgement -> partB/lk/annotations_cz_NNNN.jsonl.
Judged = rows returned by an exit-0 lk session in phase2f/out/sessions (+ phase2f/out/lk_corrected_cz.jsonl). 0 model calls."""
import json, os, re, glob, sys
DRY = "--dry" in sys.argv
H = os.path.dirname(os.path.abspath(__file__)); TO = os.path.dirname(os.path.dirname(H)); F2OUT = os.path.join(TO, "phase2f", "out")
OUT = os.path.join(H, "out_dry" if DRY else "out"); LKD = os.path.join(H, "lk_dry" if DRY else "lk")
os.makedirs(os.path.join(LKD, "sessions"), exist_ok=True)
def nranges(ns):
    ns, o = sorted(ns), []
    for n in ns:
        if o and n == o[-1][1] + 1: o[-1][1] = n
        else: o.append([n, n])
    return ["%d-%d" % (a, b) if a != b else str(a) for a, b in o]
corr, sess = set(), set()
p = os.path.join(F2OUT, "lk_corrected_cz.jsonl")
if os.path.exists(p):
    for l in open(p, encoding="utf-8"):
        try: corr.add(json.loads(l)["n"])
        except Exception: pass
for fp in glob.glob(os.path.join(F2OUT, "sessions", "cz_*_lk.json")):
    try:
        d = json.load(open(fp, encoding="utf-8"))
        if (d.get("meta") or {}).get("exit") == 0 and isinstance(d.get("rows"), list):
            sess |= {o.get("n") for o in d["rows"] if isinstance(o, dict)}
    except Exception: pass
judged = sess   # 2G: lk_corrected_cz.jsonl lists all 2,850 merged rows, judged or not; only exit-0 lk session rows count
f2 = {json.loads(l)["n"] for l in open(os.path.join(F2OUT, "annotations_cz_final.jsonl"), encoding="utf-8") if l.strip()}
for x in glob.glob(os.path.join(LKD, "annotations_cz_*.jsonl")): os.remove(x)
need, present = [], set()
for fp in sorted(glob.glob(os.path.join(OUT, "annotations_cz_[0-9][0-9][0-9][0-9].jsonl"))):
    keep = []
    for l in open(fp, encoding="utf-8"):
        if not l.strip(): continue
        n = json.loads(l)["n"]; present.add(n)
        if n not in judged: keep.append(l if l.endswith("\n") else l + "\n"); need.append(n)
    if keep: open(os.path.join(LKD, os.path.basename(fp)), "w", encoding="utf-8").writelines(keep)
info = {"judged_source": "rows returned by exit-0 lk sessions in phase2f/out/sessions",
        "lk_corrected_rows": len(corr), "phase2f_lk_session_rows": len(sess), "f2_rows": len(f2),
        "f2_rows_judged": len(f2 & judged), "f2_rows_lacking_dedicated_lk": nranges(f2 - judged), "f2_lacking_count": len(f2 - judged),
        "present_rows": len(present), "new_rows_2g": len(present - f2), "need": len(need), "need_ranges": nranges(need),
        "need_ns": sorted(need)}
json.dump(info, open(os.path.join(H, "lk_need%s.json" % ("_dry" if DRY else "")), "w", encoding="utf-8"), indent=1)
if not need: open(os.path.join(LKD, "NOTHING_TO_JUDGE"), "w").write("0 rows\n")
print(json.dumps({k: v for k, v in info.items() if k != "need_ns"}))
