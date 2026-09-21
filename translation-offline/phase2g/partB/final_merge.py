#!/usr/bin/env python3
"""B6: partB/out/annotations_cz_final.jsonl over EVERY Czech row present (2F's rows + new), upload_cz_final.xlsx via
build_upload_2g.py, lk_2g.json, README row sources, input-hash check.  0 model calls, 0 DB access, uploads nothing."""
import json, os, re, glob, subprocess, sys, time, hashlib, collections
DRY = "--dry" in sys.argv
H = os.path.dirname(os.path.abspath(__file__)); TO = os.path.dirname(os.path.dirname(H)); REPO = os.path.dirname(TO)
F2OUT = os.path.join(TO, "phase2f", "out"); OUT = os.path.join(H, "out_dry" if DRY else "out"); LKD = os.path.join(H, "lk_dry" if DRY else "lk")
def jl(p): return [l.rstrip("\n") for l in open(p, encoding="utf-8") if l.strip()] if os.path.exists(p) else []
def nranges(ns):
    ns, o = sorted(ns), []
    for n in ns:
        if o and n == o[-1][1] + 1: o[-1][1] = n
        else: o.append([n, n])
    return ["%d-%d" % (a, b) if a != b else str(a) for a, b in o]
f2 = {json.loads(l)["n"]: l for l in jl(os.path.join(F2OUT, "annotations_cz_final.jsonl"))}
pb = {}
for p in sorted(glob.glob(os.path.join(OUT, "annotations_cz_[0-9][0-9][0-9][0-9].jsonl"))):
    for l in jl(p): pb[json.loads(l)["n"]] = l
lkf = {json.loads(l)["n"]: l for l in jl(os.path.join(LKD, "annotations_cz_final.jsonl"))}
needf = os.path.join(H, "lk_need%s.json" % ("_dry" if DRY else ""))
need = set(json.load(open(needf)).get("need_ns", [])) if os.path.exists(needf) else set()
judged = set()
for fp in glob.glob(os.path.join(LKD, "sessions", "*_lk.json")):
    try:
        d = json.load(open(fp, encoding="utf-8"))
        if (d.get("meta") or {}).get("exit") == 0 and isinstance(d.get("rows"), list):
            judged |= {o.get("n") for o in d["rows"] if isinstance(o, dict)}
    except Exception: pass
final, src, nolk, disagree = [], collections.Counter(), [], 0
IGN = ("lk", "lk_verdict", "lk_reason")
for n in sorted(set(f2) | set(pb)):
    if n in f2 and n in pb:
        a, b = json.loads(f2[n]), json.loads(pb[n])
        if {k: v for k, v in a.items() if k not in IGN} != {k: v for k, v in b.items() if k not in IGN}: disagree += 1
    if n in lkf and n in judged:
        final.append(lkf[n]); src["lk_2g_dedicated"] += 1
    elif n in f2 and n not in need:
        final.append(f2[n]); src["phase2f_final_dedicated_lk"] += 1
    else:
        final.append(lkf.get(n) or pb.get(n) or f2[n]); src["NO_dedicated_lk"] += 1; nolk.append(n)
fin = os.path.join(OUT, "annotations_cz_final.jsonl")
open(fin, "w", encoding="utf-8").write("\n".join(final) + "\n")
sel = [json.loads(l) for l in open(os.path.join(TO, "phase2c", "selection_2c.jsonl"), encoding="utf-8") if l.strip()]
allcz = {r["n"] for r in sel if r["lang"] == "cz"}
present = set(f2) | set(pb); missing = sorted(allcz - present)
biggest = max((len(l) for l in final), default=0)
rep = json.load(open(os.path.join(LKD, "REPORT_2e_lk.json"), encoding="utf-8")) if os.path.exists(os.path.join(LKD, "REPORT_2e_lk.json")) else None
shachk = {"checked": 0, "mismatch": [], "unresolved": []}
shaf = os.path.join(os.path.dirname(H), "SHA_inputs_before.txt")
if os.path.exists(shaf):
    for l in open(shaf, encoding="utf-8"):
        l = l.strip()
        if not l or l.startswith("#"): continue
        h, name = l.split(None, 1); name = name.strip().lstrip("*")
        cands = [name] if os.path.isabs(name) else [os.path.join(TO, name), os.path.join(REPO, name), os.path.join(os.path.dirname(H), name)]
        pth = next((c for c in cands if os.path.isfile(c)), None)
        if not pth: shachk["unresolved"].append(name); continue
        shachk["checked"] += 1
        if hashlib.sha256(open(pth, "rb").read()).hexdigest() != h: shachk["mismatch"].append(name)
out = {"rows_final": len(final), "sources": dict(src), "rows_without_dedicated_lk": {"count": len(nolk), "ranges": nranges(nolk)},
       "rows_missing_of_4064": {"count": len(missing), "ranges": nranges(missing)},
       "phase2f_rows_reassembled_disagreeing_outside_lk": disagree, "largest_structure_json_chars": biggest,
       "lk_prompt_sha16": "5fa910459c078539", "lk_rows_needing_judgement": len(need), "lk_rows_judged_2g": len(judged & need),
       "lk_report": rep, "input_sha_check": shachk, "gemini_counted_calls_partB": 0, "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
print(json.dumps({k: v for k, v in out.items() if k != "lk_report"}, ensure_ascii=False))
if DRY: sys.exit(0)
json.dump(out, open(os.path.join(H, "lk_2g.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
subprocess.run([sys.executable, "build_upload_2g.py"], cwd=H)
rd = os.path.join(H, "UPLOAD_README.md")
if os.path.exists(rd):
    open(rd, "a", encoding="utf-8").write(
        "\n## Row sources in `out/annotations_cz_final.jsonl` (Phase 2G Part B)\n\n" +
        "\n".join("* `%s`: %d rows" % kv for kv in sorted(src.items())) +
        "\n* rows without a dedicated lk judgement: %d (%s)\n* rows still missing of 4,064: %d (%s)\n"
        "* largest structure_json cell: %d chars (Excel limit 32,767)\n* nothing uploaded, nothing written to the database.\n"
        % (len(nolk), ", ".join(nranges(nolk)[:12]) or "-", len(missing), ", ".join(nranges(missing)[:12]) or "-", biggest))
stops = []
if missing: stops.append(("rows_missing", "%d of 4,064 Czech rows are still missing: %s" % (len(missing), ", ".join(nranges(missing)))))
if nolk: stops.append(("lk_incomplete", "%d rows have no dedicated lk judgement: %s" % (len(nolk), ", ".join(nranges(nolk)))))
if shachk["mismatch"]: stops.append(("input_changed", "input files changed: %s" % shachk["mismatch"]))
for r, t in stops:
    open(os.path.join(H, "STOP_%s.md" % r), "w", encoding="utf-8").write("# Phase 2G Part B STOP: %s\n\n%s\n\nWritten %s by final_merge.py (B6).\n" % (r, t, time.strftime("%Y-%m-%d %H:%M:%S")))
