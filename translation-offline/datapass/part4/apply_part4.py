"""Write the Part 4 rewrites that pass the machine check AND the independent verifier (per language, <=500/batch)."""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "lib"))
import writer
props = json.load(open(os.path.join(HERE, "props_checked.json")))
COLS = ["intro_text", "full_sentence"]
snap = {r["id"]: r for r in json.load(open(os.path.join(HERE, "rows_before.json")))}
out, summary = {}, {}
for L in ("es", "ua", "tr", "hu"):
    ok = [p for p in props if p["lang"] == L and p["ok"]]
    v = [l.rstrip("\n").split("|") for l in open(os.path.join(HERE, f"verdict_{L}.txt"), encoding="utf-8") if l.strip()]
    assert [int(x[0]) for x in v] == [p["exercise_id"] for p in ok], L
    agreed = [p for p, x in zip(ok, v) if x[1] == "OK"]
    no = [{**p, "verifier": x[2] if len(x) > 2 else ""} for p, x in zip(ok, v) if x[1] != "OK"]
    changes = [{"id": p["id"], "exercise_id": p["exercise_id"], "lang": L,
                "new": {"intro_text": p["new"][0], "full_sentence": p["new"][1]},
                "old": {"intro_text": snap[p["id"]]["intro_text"], "full_sentence": snap[p["id"]]["full_sentence"]}} for p in agreed]
    out[L] = {"written": changes, "verifier_no": no, "machine_fail": [p for p in props if p["lang"] == L and not p["ok"]]}
    if "--write" in sys.argv:
        summary[L] = writer.run("part4", f"part4_{L}", changes, COLS)
    else:
        summary[L] = {"agreed": len(changes), "no": len(no)}
json.dump(out, open(os.path.join(HERE, "part4_final.json"), "w"), ensure_ascii=False, indent=0)
for L, r in summary.items():
    print(L, json.dumps({k: r[k] for k in r if k not in ("skipped",)} , ensure_ascii=False)[:400], "skipped", len(r.get("skipped", [])))
