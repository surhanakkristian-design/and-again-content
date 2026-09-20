#!/usr/bin/env python3
"""Phase 2F §1.2/§1.3 — run ONE 100-row v chunk as two 50-row halves through run_2f_cz.py's own
machinery (same prompt builder, same session(), same back-off, retry ceiling MAX_RETRY = 3).
Writes diag/halves_<sid>.json and, if both halves return their rows, the merged out/sessions/<sid>.json."""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prompts_2f
H = os.path.dirname(os.path.abspath(__file__))
SID = sys.argv[1]
BID = SID.rsplit("_s", 1)[0]
m = prompts_2f.load([BID])
assert m.MAX_RETRY == 3, m.MAX_RETRY
lang, brows, crows, header, lines = prompts_2f.chunk_task(m, BID, SID)
assert len(crows) == 100
m.load_ledger(); m.load_token()
m.log("HALVES", SID, "n", crows[0]["n"], "-", crows[-1]["n"], "MAX_RETRY", m.MAX_RETRY,
      "prompt_chars_full", len(header) + len("\n".join(lines)))
res, t_all = {}, time.time()
for tag, a, b in (("h1", 0, 50), ("h2", 50, 100)):
    hsid = "%s_%s" % (SID, tag)
    rows, prompt = crows[a:b], header + "\n".join(lines[a:b])
    r0, k0, t0 = m.STATE["retries"], m.STATE["tok"], time.time()
    try:
        ret = m.session(hsid, "v", prompt, rows)
    except Exception as e:
        ret = ("EXCEPTION", type(e).__name__, str(e)[:200])
    d = json.load(open(m.sess_path(hsid), encoding="utf-8")) if os.path.exists(m.sess_path(hsid)) else None
    meta = (d or {}).get("meta") or {}
    res[tag] = {"sid": hsid, "n_range": [rows[0]["n"], rows[-1]["n"]], "prompt_chars": len(prompt),
                "prompt_bytes": len(prompt.encode("utf-8")), "result": repr(ret)[:300],
                "wall_s": round(time.time() - t0, 1), "tokens": m.STATE["tok"] - k0,
                "retry_attempts_429_or_nonzero": m.STATE["retries"] - r0,
                "exit": meta.get("exit"), "session_tokens": meta.get("tokens"),
                "rows_returned": len(d["rows"]) if d and isinstance(d.get("rows"), list) else 0,
                "covers_its_half": bool(d and isinstance(d.get("rows"), list) and
                                        {r["n"] for r in rows} <= {o.get("n") for o in d["rows"] if isinstance(o, dict)}),
                "SUCCEEDED": False}
    res[tag]["SUCCEEDED"] = bool(res[tag]["exit"] == 0 and res[tag]["covers_its_half"])
    m.log("HALF-RESULT", hsid, json.dumps(res[tag], ensure_ascii=False))
res["both_succeeded"] = bool(res["h1"]["SUCCEEDED"] and res["h2"]["SUCCEEDED"])
res["total_wall_s"] = round(time.time() - t_all, 1)
res["total_tokens"] = res["h1"]["tokens"] + res["h2"]["tokens"]
if res["both_succeeded"]:
    rr = []
    for tag in ("h1", "h2"):
        rr += json.load(open(m.sess_path("%s_%s" % (SID, tag)), encoding="utf-8"))["rows"]
    json.dump({"meta": {"session": SID, "kind": "v", "exit": 0, "rows_asked": 100,
                        "tokens": (res["h1"]["session_tokens"] or 0) + (res["h2"]["session_tokens"] or 0),
                        "wall_s": res["total_wall_s"], "assembled_from_halves": [SID + "_h1", SID + "_h2"],
                        "note": "2F §1.2: this chunk is only obtainable in 50-row halves"},
               "rows": rr}, open(m.sess_path(SID), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    m.log("HALVES-MERGED", SID, len(rr), "rows")
json.dump(res, open(os.path.join(H, "halves_%s.json" % SID), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
m.STATE["finished"] = True; m.save_ledger()
m.commit([os.path.join(H, "halves_%s.json" % SID), m.LEDGER, m.LOGP], "Phase 2F: %s as two 50-row halves" % SID)
print(json.dumps(res, ensure_ascii=False, indent=1))
