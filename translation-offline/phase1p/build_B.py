#!/usr/bin/env python3
"""Phase 1P writer B: merge parts, validate, build blind judge packets."""
import json, random, re, sys, unicodedata
from collections import Counter
from pathlib import Path

C = Path(__file__).resolve().parent.parent          # translation-offline
P = Path(__file__).resolve().parent                 # phase1p
DATA, JUDGE = P / "data", P / "judge"
JUDGE.mkdir(parents=True, exist_ok=True)

# ---------- merge -------------------------------------------------------
S = []
for i in (1, 2, 3):
    S += json.loads((DATA / f"writer_B_part{i}.json").read_text(encoding="utf-8"))
(DATA / "writer_B.json").write_text(json.dumps(S, ensure_ascii=False, indent=1), encoding="utf-8")

err = []
def chk(cond, msg):
    if not cond:
        err.append(msg)

# ---------- structural validation --------------------------------------
chk(len(S) == 60, f"sentence count {len(S)} != 60")
want = ["1P%03d" % n for n in range(61, 121)]
chk([s["sid"] for s in S] == want, "sid sequence wrong")
for s in S:
    n = int(s["sid"][2:])
    chk(s["level"] == ("B1" if n <= 90 else "B2"), f"{s['sid']} level")
    chk(len(s["correct"]) == 4, f"{s['sid']} correct != 4")
    chk(len(s["wrong"]) == 5, f"{s['sid']} wrong != 5")
    chk(bool(s.get("topic")), f"{s['sid']} topic missing")
    chk(s.get("tf_gold") in ("past", "present", "future"), f"{s['sid']} tf_gold")
    for f in ("nom_agent", "agent", "passivizable", "reported_speech",
              "perfective_future", "impersonal_or_passive"):
        chk(f in s["tags"], f"{s['sid']} tags.{f} missing")
    for a in s["correct"]:
        chk(set(a) == {"aid", "answer", "passive", "tags"}, f"{s['sid']}/{a.get('aid')} correct fields")
        chk(a["passive"] in (None, "by", "agentless"), f"{s['sid']}/{a['aid']} passive value")
    for a in s["wrong"]:
        chk(set(a) == {"aid", "intent", "form", "answer", "tags"}, f"{s['sid']}/{a.get('aid')} wrong fields")
        chk(a["intent"] in ("TF", "W", "M", "S"), f"{s['sid']}/{a['aid']} intent {a.get('intent')}")
    txt = [a["answer"] for a in s["correct"] + s["wrong"]]
    chk(len(set(txt)) == len(txt), f"{s['sid']} duplicate answer inside sentence")
    aids = [a["aid"] for a in s["correct"] + s["wrong"]]
    chk(len(set(aids)) == 9, f"{s['sid']} duplicate aid")
    for a in s["correct"] + s["wrong"]:
        chk(all(t in {"agentless", "by-passive", "determiner", "aspect",
                      "timeframe", "number", "plain"} for t in a["tags"]),
            f"{s['sid']}/{a['aid']} bad tag {a['tags']}")

# ---------- overlap with the existing 450 -------------------------------
def norm(t):
    t = unicodedata.normalize("NFKC", t).lower()
    t = re.sub(r"[^\w\s]", " ", t, flags=re.UNICODE)
    return re.sub(r"\s+", " ", t).strip()

existing = [e["slovak"] for e in json.loads((C / "phase1n/existing_350.json").read_text(encoding="utf-8"))]
existing += [e["slovak"] for e in json.loads((C / "phase1n/data/sentences.json").read_text(encoding="utf-8"))]
chk(len(existing) == 450, f"existing pool {len(existing)} != 450")
epool = {norm(x) for x in existing}
mine = [norm(s["slovak"]) for s in S]
chk(len(set(mine)) == 60, "duplicate Slovak sentence inside the new set")
clash = [s["sid"] for s, m in zip(S, mine) if m in epool]
chk(not clash, f"Slovak duplicates vs existing 450: {clash}")
etok = [set(x.split()) for x in epool]
near = []
for s, m in zip(S, mine):
    mt = set(m.split())
    for et in etok:
        j = len(mt & et) / len(mt | et)
        if j >= 0.6:
            near.append((s["sid"], round(j, 2)))
            break

# ---------- required counts --------------------------------------------
cc, wc = Counter(), Counter()
intents = Counter()
odd_even = {"correct": Counter(), "wrong": Counter()}
for s in S:
    par = "odd" if int(s["sid"][2:]) % 2 else "even"
    for a in s["correct"]:
        for t in a["tags"]:
            cc[t] += 1
            odd_even["correct"][(t, par)] += 1
    for a in s["wrong"]:
        intents[a["intent"]] += 1
        for t in a["tags"]:
            wc[t] += 1
            odd_even["wrong"][(t, par)] += 1
w_agentless_not_tf = sum(1 for s in S for a in s["wrong"]
                         if "agentless" in a["tags"] and "timeframe" not in a["tags"])
oe_anf = Counter("odd" if int(s["sid"][2:]) % 2 else "even"
                 for s in S for a in s["wrong"]
                 if "agentless" in a["tags"] and "timeframe" not in a["tags"])

chk(cc["agentless"] >= 42, f"CORRECT agentless {cc['agentless']} < 42")
chk(cc["determiner"] >= 52, f"CORRECT determiner {cc['determiner']} < 52")
chk(cc["by-passive"] > 0 and cc["aspect"] > 0, "CORRECT needs some by-passive and aspect")
chk(wc["timeframe"] >= 82, f"WRONG timeframe {wc['timeframe']} < 82")
chk(wc["agentless"] >= 42, f"WRONG agentless {wc['agentless']} < 42")
chk(w_agentless_not_tf >= 25, f"WRONG agentless-not-timeframe {w_agentless_not_tf} < 25")
n_pass_sent = sum(1 for s in S if s["tags"]["passivizable"])
chk(n_pass_sent >= 45, f"passivizable sentences {n_pass_sent} < 45")

# ---------- packets -----------------------------------------------------
base = []
for s in S:
    for a in s["correct"] + s["wrong"]:
        base.append({"sid": s["sid"], "aid": a["aid"], "slovak": s["slovak"],
                     "level": s["level"], "answer": a["answer"], "topic": s["topic"]})
rng = random.Random(1602)
dups = [dict(b, dup_of=(b["sid"], b["aid"])) for b in rng.sample(base, 40)]
allp = base + dups
rng.shuffle(allp)
key, out = {}, {"B1": [], "B2": []}
seen_first = {}
for i, p in enumerate(allp, 1):
    jid = "JB%04d" % i
    if "dup_of" not in p:
        seen_first[(p["sid"], p["aid"])] = jid
for i, p in enumerate(allp, 1):
    jid = "JB%04d" % i
    dof = seen_first[p["dup_of"]] if "dup_of" in p else None
    key[jid] = {"sid": p["sid"], "aid": p["aid"], "is_duplicate_of": dof}
    out[p["level"]].append({"jid": jid, "slovak": p["slovak"], "level": p["level"],
                            "answer": p["answer"], "topic": p["topic"]})

chk(len(allp) == 580, f"packets {len(allp)} != 580")
chk(sum(1 for v in key.values() if v["is_duplicate_of"]) == 40, "duplicate count != 40")
chk(len(key) == 580 and len(out["B1"]) + len(out["B2"]) == 580, "packet/key mismatch")
for f in out["B1"] + out["B2"]:
    chk(set(f) == {"jid", "slovak", "level", "answer", "topic"}, "packet leaks a field")

(JUDGE / "packets_B1.json").write_text(json.dumps(out["B1"], ensure_ascii=False, indent=1), encoding="utf-8")
(JUDGE / "packets_B2.json").write_text(json.dumps(out["B2"], ensure_ascii=False, indent=1), encoding="utf-8")
(JUDGE / "_key_B.json").write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------- report ------------------------------------------------------
print("sentences:", len(S), "| B1:", sum(1 for s in S if s["level"] == "B1"),
      "B2:", sum(1 for s in S if s["level"] == "B2"),
      "| answers 4+5 per sentence: OK")
print("tf_gold:", dict(Counter(s["tf_gold"] for s in S)))
print("passivizable sentences:", n_pass_sent)
print("CORRECT tags:", dict(cc))
print("WRONG tags:", dict(wc), "| agentless-not-timeframe:", w_agentless_not_tf)
print("WRONG intents:", dict(intents))
print("odd/even CORRECT agentless:", odd_even["correct"][("agentless", "odd")], "/",
      odd_even["correct"][("agentless", "even")],
      "| determiner:", odd_even["correct"][("determiner", "odd")], "/",
      odd_even["correct"][("determiner", "even")],
      "| by-passive:", odd_even["correct"][("by-passive", "odd")], "/",
      odd_even["correct"][("by-passive", "even")])
print("odd/even WRONG timeframe:", odd_even["wrong"][("timeframe", "odd")], "/",
      odd_even["wrong"][("timeframe", "even")],
      "| agentless:", odd_even["wrong"][("agentless", "odd")], "/",
      odd_even["wrong"][("agentless", "even")],
      "| agentless-not-tf:", oe_anf["odd"], "/", oe_anf["even"])
print("Slovak duplicates vs existing 450:", len(clash), "| near (jaccard>=0.6):", near)
print("packets: B1", len(out["B1"]), "B2", len(out["B2"]), "| duplicates 40 | key", len(key))
print("OK" if not err else "FAIL\n" + "\n".join(err))
sys.exit(1 if err else 0)
