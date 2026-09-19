#!/usr/bin/env python3
"""Phase 1S Task C1 - the BLIND judge packet (0 model calls). Writes phase1s/taskC/judge/packet.json
and phase1s/taskC/_key.json (the key stays OUT of judge/)."""
import json, os, random, sys

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
TC = os.path.join(BASE, "phase1s", "taskC")
sys.path.insert(0, TC)
from ag_apply import ag_maps, levels

SEED = 20260919
RULE = ("A translation is judged only on whether it renders the whole Slovak sentence. An English "
        "passive is CORRECT when it keeps the agent (e.g. 'is repaired by my father'), or when the "
        "Slovak sentence itself names no agent. When the Slovak names an agent (a nominative subject "
        "doing the action, including a pronoun or 'niekto') and the English answer drops it, the "
        "learner left out half the translation: that is an omission and the answer is WRONG. Dropping "
        "any other content word is WRONG too; dropping only a function word or particle is CORRECT. "
        "For each item answer: verdict correct|wrong, dropped (Slovak = English, or empty), borderline "
        "true|false with a short reason.")


def jdef(o):
    if isinstance(o, (set, frozenset)):
        return sorted(o, key=str)
    if isinstance(o, tuple):
        return list(o)
    return str(o)


def main():
    rows = json.load(open(os.path.join(BASE, "phase1s", "taskA", "rows_1s.json"), encoding="utf-8"))
    _m1, m2 = ag_maps()
    lev = levels()
    cor = [r for r in rows if r["label_1r"] == "correct"]
    picked, buckets = [], {}

    def add(r, b):
        if r["iid"] in buckets:
            return
        buckets[r["iid"]] = b
        picked.append(r)

    for r in sorted(cor, key=lambda x: x["iid"]):
        if "agentless" in r["tags"]:
            add(r, "agentless")
    for r in sorted(cor, key=lambda x: x["iid"]):
        if "by-passive" in r["tags"]:
            add(r, "by-passive-control")
    for r in sorted(cor, key=lambda x: x["iid"]):
        if m2[r["iid"]]["fired"] and r["iid"] not in buckets:
            add(r, "ag-outside-tags")
    pool = [r for r in sorted(cor, key=lambda x: x["iid"]) if "plain" in r["tags"] and r["iid"] not in buckets]
    for r in random.Random(SEED).sample(pool, 40):
        add(r, "plain-control")

    random.Random(SEED).shuffle(picked)
    items, key = [], {}
    for n, r in enumerate(picked, 1):
        jid = "J%03d" % n
        items.append({"jid": jid, "slovak": r["slovak"], "answer": r["answer"],
                      "level": lev.get(r["iid"])})
        key[jid] = {"iid": r["iid"], "bucket": buckets[r["iid"]]}
    packet = {"rule": RULE, "items": items}
    json.dump(packet, open(os.path.join(TC, "judge", "packet.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, default=jdef)
    json.dump(key, open(os.path.join(TC, "_key.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1, default=jdef)
    from collections import Counter
    comp = Counter(buckets.values())
    print("packet items:", len(items), "composition:", json.dumps(comp, sort_keys=True))
    print("no labels/tags/AG/references in packet:",
          all(set(x) == {"jid", "slovak", "answer", "level"} for x in items))


if __name__ == "__main__":
    main()
