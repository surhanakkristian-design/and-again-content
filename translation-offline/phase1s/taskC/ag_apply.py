#!/usr/bin/env python3
"""Phase 1S Task C - apply rule AG (v1 from taskA, v2 from taskC) to the frozen 1P items. 0 model calls."""
import json, os, sys

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
TA, TC, P1P = (os.path.join(BASE, "phase1s", "taskA"), os.path.join(BASE, "phase1s", "taskC"),
               os.path.join(BASE, "phase1p"))
L = lambda p: json.load(open(p, encoding="utf-8"))


def ag_maps():
    """-> (v1_map, v2_map): item_id -> AG.decide(...) dict, primary variant."""
    sys.path.insert(0, TA)
    sys.path.insert(0, TC)
    import agent_drop as V1
    import agent_drop_v2 as V2
    sents = {s["sid"]: s for s in L(os.path.join(P1P, "data", "sentences.json"))}
    ann = L(os.path.join(P1P, "data", "annotations.json"))
    items = {it["id"]: it for it in L(os.path.join(P1P, "data", "items.json"))}
    m1, m2 = {}, {}
    for i, it in items.items():
        s = sents[it["sid"]]
        a = ann.get(str(it["sid"])) or {}
        wt = (s.get("tags") or {}).get("writer_tags") or {}
        ref = ((a.get("hygienised") or a).get("v") or [""])[0]
        m1[i] = V1.decide(s["slovak"], a, wt, it["answer"], ref, "primary")
        m2[i] = V2.decide(s["slovak"], a, wt, it["answer"], ref, "primary")
    return m1, m2


def levels():
    res = L(os.path.join(P1P, "results_1p.json"))["rows"]
    res = list(res.values()) if isinstance(res, dict) else res
    return {r["item_id"]: r.get("level") for r in res}


def variants():
    """sid(str) -> list of reference variants (hygienised)."""
    ann = L(os.path.join(P1P, "data", "annotations.json"))
    out = {}
    for sid, a in ann.items():
        v = ((a or {}).get("hygienised") or a or {}).get("v") or []
        out[str(sid)] = [x for x in v if x]
    return out
