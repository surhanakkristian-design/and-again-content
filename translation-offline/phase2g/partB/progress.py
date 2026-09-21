#!/usr/bin/env python3
import json, os, re, sys, time, glob
H = os.path.dirname(os.path.abspath(__file__))
def spent(p):
    try: return int(json.load(open(os.path.join(H, p))).get("spent") or 0)
    except Exception: return 0
a, l = spent("ledger_2g_cz.json"), spent("ledger_2g_lk.json")
pres = sum(sum(1 for x in open(f, encoding="utf-8") if x.strip()) for f in glob.glob(os.path.join(H, "out", "annotations_cz_[0-9][0-9][0-9][0-9].jsonl")))
new = pres - 2850; tpr = a / float(new) if new > 0 else None
rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "who": "chain", "stage": sys.argv[1] if len(sys.argv) > 1 else "?",
       "annotation_tokens": a, "lk_tokens": l, "cum_headless_tokens_partB": a + l, "cap_partB": 2900000,
       "rows_present": pres, "new_rows": new, "annotation_tok_per_new_row": round(tpr, 1) if tpr else None,
       "projected_annotation_tokens_all_4064": int(a + tpr * max(0, 4064 - pres)) if tpr else None,
       "gemini_counted_calls_partB": 0, "gemini_cap_partB": 150}
open(os.path.join(H, "progress.log"), "a", encoding="utf-8").write(json.dumps(rec) + "\n")
