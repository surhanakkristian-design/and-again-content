#!/usr/bin/env python3
"""Phase 1N prep: existing-sentence export, Task A packets, task briefs.

Reads only Phase 1M (closed, read-only). Every data read appends a JSON line to
N/access_log.jsonl in the 1M format {ts, side, what, caller, n, purpose}.
"""
import json
import os
import random
import shutil
from datetime import datetime, timezone

M = "/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1m"
N = "/Users/kristiansurhanak/Projects/and-again-content/translation-offline/phase1n"
CALLER = "prep_1n.py"
PURPOSE = ("Phase 1N prep-data: export Slovak/level/topic of the 350 already-used sentences and "
           "build the blind Task A re-judging packets for the withdrawn voice rule; no references "
           "or labels leave the blind_map")
SEED = 20260919

for d in ("data", "judge", "taskA", "tasks"):
    os.makedirs(os.path.join(N, d), exist_ok=True)

LOG = open(os.path.join(N, "access_log.jsonl"), "a")


def log(side, what, n):
    LOG.write(json.dumps({
        "ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "side": side, "what": what, "caller": CALLER, "n": n, "purpose": PURPOSE,
    }, ensure_ascii=False) + "\n")


def load(path, side, what):
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    log(side, what, len(d))
    return d


# ---------------------------------------------------------------- (a) existing
ex210 = load(os.path.join(M, "existing_210.json"), "1m", "existing_210 (Slovak/level/topic only)")
sents = load(os.path.join(M, "data", "sentences.json"), "1m:new", "sentences (Slovak/level/topic)")

existing = [{"slovak": r["slovak"], "level": r["level"], "topic": r["topic"]} for r in ex210]
existing += [{"slovak": r["slovak"], "level": r["level"], "topic": r["topic"]} for r in sents]
with open(os.path.join(N, "existing_350.json"), "w", encoding="utf-8") as fh:
    json.dump(existing, fh, ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- (b) Task A
items = load(os.path.join(M, "data", "items.json"), "1m:new", "items (id/sid/intent/form/answer)")
bmap = load(os.path.join(M, "judge", "blind_map.json"), "1m:judge", "blind_map (jid -> item_id)")

labels = {}  # item_id -> (judged, type)
for p in range(1, 7):
    path = os.path.join(M, "judge", "out_part%d.json" % p)
    if not os.path.exists(path):
        continue
    rows = load(path, "1m:judge", "judge out_part%d (verdict/type)" % p)
    for r in rows:
        iid = bmap.get(r["jid"])
        if iid is not None:
            labels[iid] = (r.get("judged"), r.get("type"))

lvl = {s["sid"]: s["level"] for s in sents}
sk = {s["sid"]: s["slovak"] for s in sents}

vrows, fill_ok, fill_bad = [], [], []
for it in items:
    judged, typ = labels.get(it["id"], (None, None))
    rec = {"item": it, "judged": judged, "type": typ}
    if it.get("intent") == "V" or typ == "V":
        vrows.append(rec)
    elif judged == "correct":
        fill_ok.append(rec)
    elif judged == "wrong":
        fill_bad.append(rec)

rng = random.Random(SEED)
fillers = rng.sample(fill_ok, 40) + rng.sample(fill_bad, 40)
for r in fillers:
    r["filler"] = True
for r in vrows:
    r["filler"] = False

pool = vrows + fillers
rng2 = random.Random(SEED)
rng2.shuffle(pool)

rows, blind = [], {}
for i, r in enumerate(pool, 1):
    jid = "A%03d" % i
    it = r["item"]
    rows.append({"jid": jid, "slovak": sk[it["sid"]], "level": lvl[it["sid"]], "answer": it["answer"]})
    blind[jid] = {"item_id": it["id"], "sid": it["sid"], "intent": it.get("intent"),
                  "form": it.get("form"), "old_judged": r["judged"], "old_type": r["type"],
                  "filler": r["filler"]}

half = (len(rows) + 1) // 2
for name, chunk in (("in_part1.json", rows[:half]), ("in_part2.json", rows[half:])):
    with open(os.path.join(N, "taskA", name), "w", encoding="utf-8") as fh:
        fh.write("[\n")
        fh.write(",\n".join(" " + json.dumps(r, ensure_ascii=False) for r in chunk))
        fh.write("\n]\n")
with open(os.path.join(N, "taskA", "blind_map.json"), "w", encoding="utf-8") as fh:
    json.dump(blind, fh, ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- (c) tasks
shutil.copy(os.path.join(M, "tasks", "ARM_B.md"), os.path.join(N, "tasks", "ARM_B.md"))
log("1m:tasks", "ARM_B.md (copied verbatim)", 1)
LOG.close()

n_int_v = sum(1 for r in vrows if r["item"].get("intent") == "V")
n_type_v = sum(1 for r in vrows if r["type"] == "V")
print(json.dumps({
    "n_existing": len(existing), "n_taskA_rows": len(rows), "n_filler": len(fillers),
    "n_v_union": len(vrows), "n_intent_v": n_int_v, "n_judged_type_v": n_type_v,
    "part1": half, "part2": len(rows) - half, "labelled_items": len(labels),
}, ensure_ascii=False))
