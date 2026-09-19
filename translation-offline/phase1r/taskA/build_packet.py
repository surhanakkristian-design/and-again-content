#!/usr/bin/env python3
"""Phase 1R / Task A PREP -- build the BLIND judge packet.

The judge sees ONLY: the rule, the Slovak sentence, the learner's English
answer, the CEFR level. No checker verdicts, no F5 output, no reference,
no 1Q bucket, no old judge label, no report text.

Inputs (read-only):
  phase1q/taskA/triage.json   -- 129 type-M items with slovak/answer/level/bucket
  phase1q/rows_1q.json        -- join/existence check on `iid`
  phase1p/data/sentences.json -- sid -> half (tags.half), optional

Outputs:
  phase1r/taskA/judge/packet.json  (the only file in judge/)
  phase1r/taskA/_key.json          (unblinding key, NOT in judge/)

No model calls, no network, no DB.
"""
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
OFFLINE = os.path.abspath(os.path.join(HERE, "..", ".."))
Q = os.path.join(OFFLINE, "phase1q")
P = os.path.join(OFFLINE, "phase1p")
JUDGE_DIR = os.path.join(HERE, "judge")

RULE = """
THE RULE, now settled:
- M1, a dropped FUNCTION word or particle (just, already, an article, optional "that") — CORRECT, accepted, the missing word surfaced as a tip.
- M2, a dropped CONTENT word (noun, main verb, meaning-carrying adjective or adverb) — WRONG. When `Práve teraz dievča sfukuje sviečky` is answered "the girl is blowing out", the object of the action was not translated. The app teaches translation, not gist.
- M3, ADDED content — WRONG.
"""


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def half_map():
    """sid -> 'P1'/'P2' from sentences.json tags.half; fall back to sid parity."""
    path = os.path.join(P, "data", "sentences.json")
    out = {}
    if os.path.exists(path):
        data = load(path)
        rows = data if isinstance(data, list) else list(data.values())
        for r in rows:
            if not isinstance(r, dict):
                continue
            sid = r.get("sid", r.get("id"))
            tags = r.get("tags") or {}
            h = tags.get("half") if isinstance(tags, dict) else None
            h = h or r.get("half")
            if sid is not None and h:
                out[sid] = h
    return out


def main():
    triage = load(os.path.join(Q, "taskA", "triage.json"))
    rows = load(os.path.join(Q, "rows_1q.json"))
    rows_by_iid = {r["iid"]: r for r in rows}
    halves = half_map()

    # the judged-correct type-M population the owner re-opened
    pop = [t for t in triage
           if t.get("judged") == "correct" and t.get("bucket") in ("M1", "M2")]

    n_m2 = sum(1 for t in pop if t["bucket"] == "M2")
    n_m1 = sum(1 for t in pop if t["bucket"] == "M1")
    assert n_m2 == 116, "expected 116 M2, got %d" % n_m2
    assert n_m1 == 3, "expected 3 M1 controls, got %d" % n_m1
    assert len(pop) == 119, "expected 119 items, got %d" % len(pop)

    for t in pop:
        for f in ("slovak", "answer", "level"):
            assert isinstance(t.get(f), str) and t[f].strip(), \
                "empty %s on %s" % (f, t.get("iid"))
        assert t["iid"] in rows_by_iid, "iid %s not in rows_1q.json" % t["iid"]

    # one deterministic shuffle, jids assigned AFTER it
    order = list(pop)
    random.Random(20260919).shuffle(order)

    items, key = [], {}
    for i, t in enumerate(order, 1):
        jid = "J%03d" % i
        items.append({
            "jid": jid,
            "slovak": t["slovak"],
            "answer": t["answer"],
            "level": t["level"],
        })
        key[jid] = {
            "iid": t["iid"],
            "bucket": t["bucket"],
            "half": halves.get(t["sid"]) or ("P1" if int(t["sid"]) % 2 else "P2"),
            "level": t["level"],
            "old_judge_label": t["judged"],
        }

    assert len(items) == 119 and len(key) == 119
    assert all(set(it) == {"jid", "slovak", "answer", "level"} for it in items)

    os.makedirs(JUDGE_DIR, exist_ok=True)
    with open(os.path.join(JUDGE_DIR, "packet.json"), "w", encoding="utf-8") as fh:
        json.dump({"rule": RULE, "items": items}, fh, ensure_ascii=False, indent=2)
    with open(os.path.join(HERE, "_key.json"), "w", encoding="utf-8") as fh:
        json.dump(key, fh, ensure_ascii=False, indent=2)

    stray = [f for f in os.listdir(JUDGE_DIR) if f != "packet.json"]
    assert not stray, "judge/ must contain only packet.json, found %s" % stray

    print("OK  M2=%d  M1=%d  total=%d" % (n_m2, n_m1, len(items)))
    print("halves:", {h: sum(1 for v in key.values() if v["half"] == h)
                      for h in ("P1", "P2")})
    print("levels:", {l: sum(1 for v in key.values() if v["level"] == l)
                      for l in sorted({v["level"] for v in key.values()})})
    print("packet:", os.path.join(JUDGE_DIR, "packet.json"))
    print("key:   ", os.path.join(HERE, "_key.json"))


if __name__ == "__main__":
    main()
