#!/usr/bin/env python3
"""Phase 1N — structural validation of data/sentences.json (label: sentence-check).

Checks, all mechanical (the linguistic read is done by hand in data/SENTENCES_CHECK.md):
  1. exactly 100 rows
  2. sids are 160001..160100, unique
  3. every field present (sid, slovak, level, topic, tf_gold, tags{...})
  4. level counts exactly A1 13 / A2 21 / B1 36 / B2 30
  5. tags.passivizable true >= 80
  6. tf_gold in {past, present, future}, each frame >= 20
  7. no sentence string identical to one in existing_350.json
  8. max token-Jaccard new-vs-existing < 0.80 and new-vs-new < 0.60

Usage: python3 check_sentences.py            (prints a JSON report to stdout)
"""
import json
import re
import sys
from pathlib import Path
from itertools import combinations

N = Path(__file__).resolve().parent
SENT = N / "data" / "sentences.json"
EXIST = N / "existing_350.json"

REQ_TOP = ["sid", "slovak", "level", "topic", "tf_gold", "tags"]
REQ_TAGS = ["nom_agent", "agent", "passivizable", "reported_speech",
            "perfective_future", "impersonal_or_passive"]
LEVELS = {"A1": 13, "A2": 21, "B1": 36, "B2": 30}
FRAMES = {"past", "present", "future"}

WORD = re.compile(r"[^\W\d_]+", re.UNICODE)


def toks(s):
    return set(w.lower() for w in WORD.findall(s))


def jac(a, b):
    u = a | b
    return len(a & b) / len(u) if u else 0.0


def main():
    fail = []
    rows = json.loads(SENT.read_text(encoding="utf-8"))
    ex = json.loads(EXIST.read_text(encoding="utf-8"))
    ex_sent = [r["slovak"] if isinstance(r, dict) else r for r in ex]

    # 1 count
    if len(rows) != 100:
        fail.append(f"row count {len(rows)} != 100")

    # 2 sids
    sids = [r.get("sid") for r in rows]
    if sorted(sids) != list(range(160001, 160101)):
        missing = sorted(set(range(160001, 160101)) - set(sids))
        extra = sorted(set(sids) - set(range(160001, 160101)))
        dup = sorted(s for s in set(sids) if sids.count(s) > 1)
        fail.append(f"sid set wrong (missing={missing} extra={extra} dup={dup})")

    # 3 fields
    for r in rows:
        for k in REQ_TOP:
            if k not in r:
                fail.append(f"sid {r.get('sid')}: missing field {k}")
        t = r.get("tags", {})
        if not isinstance(t, dict):
            fail.append(f"sid {r.get('sid')}: tags not an object")
            continue
        for k in REQ_TAGS:
            if k not in t:
                fail.append(f"sid {r.get('sid')}: missing tag {k}")
        if not isinstance(r.get("slovak"), str) or not r.get("slovak", "").strip():
            fail.append(f"sid {r.get('sid')}: empty slovak")

    # 4 levels
    lv = {k: 0 for k in LEVELS}
    for r in rows:
        lv[r["level"]] = lv.get(r["level"], 0) + 1
    if lv != LEVELS:
        fail.append(f"level counts {lv} != {LEVELS}")

    # 5 passivizable
    n_pass = sum(1 for r in rows if r["tags"].get("passivizable") is True)
    if n_pass < 80:
        fail.append(f"passivizable true = {n_pass} < 80")

    # 6 frames
    fr = {}
    for r in rows:
        g = r["tf_gold"]
        if g not in FRAMES:
            fail.append(f"sid {r['sid']}: tf_gold {g!r} not in {sorted(FRAMES)}")
        fr[g] = fr.get(g, 0) + 1
    for f in sorted(FRAMES):
        if fr.get(f, 0) < 20:
            fail.append(f"tf_gold {f} = {fr.get(f, 0)} < 20")

    # 7 identity vs existing
    exset = set(s.strip() for s in ex_sent)
    for r in rows:
        if r["slovak"].strip() in exset:
            fail.append(f"sid {r['sid']}: identical to an existing_350 sentence")

    # 8 jaccard
    nt = [(r["sid"], toks(r["slovak"])) for r in rows]
    et = [toks(s) for s in ex_sent]
    max_ne, arg_ne = 0.0, None
    for sid, a in nt:
        for i, b in enumerate(et):
            j = jac(a, b)
            if j > max_ne:
                max_ne, arg_ne = j, (sid, i)
    max_nn, arg_nn = 0.0, None
    for (s1, a), (s2, b) in combinations(nt, 2):
        j = jac(a, b)
        if j > max_nn:
            max_nn, arg_nn = j, (s1, s2)
    if max_ne >= 0.80:
        fail.append(f"new-vs-existing jaccard {max_ne:.3f} >= 0.80 at {arg_ne}")
    if max_nn >= 0.60:
        fail.append(f"new-vs-new jaccard {max_nn:.3f} >= 0.60 at {arg_nn}")

    rep = {
        "rows": len(rows),
        "sids_ok": sorted(sids) == list(range(160001, 160101)),
        "levels": lv,
        "passivizable_true": n_pass,
        "frames": fr,
        "reported_speech": sum(1 for r in rows if r["tags"].get("reported_speech")),
        "perfective_future": sum(1 for r in rows if r["tags"].get("perfective_future")),
        "impersonal_or_passive": sum(1 for r in rows if r["tags"].get("impersonal_or_passive")),
        "nom_agent": sum(1 for r in rows if r["tags"].get("nom_agent")),
        "identical_to_existing": 0,
        "max_jaccard_new_vs_existing": round(max_ne, 4),
        "argmax_new_vs_existing": arg_ne,
        "max_jaccard_new_vs_new": round(max_nn, 4),
        "argmax_new_vs_new": arg_nn,
        "mechanical_failures": fail,
        "mechanical_ok": not fail,
    }
    print(json.dumps(rep, ensure_ascii=False, indent=1))
    return 0 if not fail else 1


if __name__ == "__main__":
    sys.exit(main())
