#!/usr/bin/env python3
"""Phase 1U Task A - AG v4 pre-flight + regression gate + (--measure) the 1T design measurement.
0 model calls, 0 network, no DB.  Writes ONLY phase1u/taskA/AG_V4_REGRESSION.{md,json}.

  python gate_v4.py            pre-flight + the 1S blind-judge regression gate; exit != 0 on failure
  python gate_v4.py --measure  the same, plus the 1T (DESIGN-only) measurement and the report

GATE (must hold for the selected configuration): >= 96 of the 97 judged agent drops caught,
0 of 42 by-passive controls rejected, 0 of 39 plain controls rejected.
"""
import json
import os
import sys
from collections import Counter

BASE = os.path.expanduser("~/Projects/and-again-content/translation-offline")
HERE = os.path.dirname(os.path.abspath(__file__))
P1P = os.path.join(BASE, "phase1p")
TA1S, TC1S = os.path.join(BASE, "phase1s", "taskA"), os.path.join(BASE, "phase1s", "taskC")
T1 = os.path.join(BASE, "phase1t")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(T1, "taskA"))
import agent_drop_v4 as V4                                                     # noqa: E402
from agent_drop_v4 import V2, V3                                               # noqa: E402
import preflight_v3 as PF3                                                     # noqa: E402

L = lambda p: json.load(open(p, encoding="utf-8"))
ACT = {'voice_sk': 'active_agent', 'agent_nom': True}

CONFIGS = [
    ("AG v2", None),
    ("AG v3 (= v4 flags=())", ()),
    ("v3+union", ("union",)),
    ("v3+unionx (raw)", ("unionx",)),
    ("v3+lex", ("lex",)),
    ("v3+align", ("align",)),
    ("v3+local", ("local",)),
    ("union+lex", ("union", "lex")),
    ("union+lex+align", ("union", "lex", "align")),
    ("AG v4 (full)", ("union", "lex", "align", "local")),
    ("AG v4 with raw union", ("unionx", "lex", "align", "local")),
]
CHOSEN = "AG v4 (full)"

# ---------------------------------------------------------------- pre-flight rows (new in v4)
NEW = [
    ('V4 closed + SK active transitive = passive', 'Oni zavreli obchod o šiestej večer.',
     ACT, {'nom_agent': True, 'agent': 'oni'},
     'The shop was closed at six in the evening.', 'They closed the shop at six in the evening.',
     True, False),
    ('V4 "The garden gate is closed every evening" is NOT a passive',
     'Brána do záhrady je každý večer zatvorená.',
     {'voice_sk': 'passive', 'agent_nom': False}, {'nom_agent': False},
     'The garden gate is closed every evening.', 'The garden gate is closed every evening.',
     False, False),
    ('V4 rewritten (prefixed irregular participle)', 'Právnik prepísal celý posledný odsek.',
     ACT, {'nom_agent': True, 'agent': 'právnik'},
     'The whole last paragraph was rewritten.', 'The lawyer rewrote the whole last paragraph.',
     True, True),
    ('V4 reduced passive relative', 'Čitatelia kritizujú ten denník za povrchné titulky.',
     ACT, {'nom_agent': True, 'agent': 'čitatelia'},
     'She writes commentaries for a newspaper criticised for shallow headlines.',
     'She writes commentaries for a newspaper that readers criticise for shallow headlines.',
     True, True),
    ('V4 locative by-phrase does not block AG', 'My zorganizujeme veľký piknik pri jazere.',
     ACT, {'nom_agent': True, 'agent': 'my'},
     'A big picnic will be organized by the lake.', 'We will organise a big picnic by the lake.',
     True, False),
    ('V4 instrument by-phrase does not block AG', 'Ja som poslal tie dokumenty e-mailom.',
     ACT, {'nom_agent': True, 'agent': 'ja'},
     'The documents were sent by email.', 'I sent the documents by email.', True, False),
    ('V4 agent by-phrase blocks AG', 'Majiteľ zavrel obchod o šiestej večer.',
     ACT, {'nom_agent': True, 'agent': 'majiteľ'},
     'The shop was closed at six by the owner.', 'The owner closed the shop at six.', False, False),
    ('V4 fronted keď-clause: the clause-local agent is dropped',
     'Keď starosta otvorí ten nový park, my zorganizujeme veľký detský festival.',
     ACT, {'nom_agent': True, 'agent': 'my'},
     'When that new park is opened, we will organise a big children\'s festival.',
     'When the mayor opens that new park, we will organise a big children\'s festival.',
     True, True),
    ('V4 fronted ja-clause: overt Slovak pronoun agent dropped',
     'Keď ja upracem kuchyňu, mama uvarí večeru.',
     ACT, {'nom_agent': True, 'agent': 'mama'},
     'When the kitchen is tidied up, Mum will cook dinner.',
     'When I tidy up the kitchen, Mum will cook dinner.', True, False),
    ('V4 class-B alignment: another clause subject is not the agent',
     'Predavačka zabalila darček, ktorý moja sestra vybrala pre babičku.',
     ACT, {'nom_agent': True, 'agent': 'predavačka'},
     'The present that my sister chose for grandma was wrapped.',
     'The shop assistant wrapped the present that my sister chose for grandma.', True, True),
    ('V4 class-B control: the agent is kept',
     'Predavačka zabalila darček, ktorý moja sestra vybrala pre babičku.',
     ACT, {'nom_agent': True, 'agent': 'predavačka'},
     'The shop assistant wrapped the present that my sister chose for grandma.',
     'The shop assistant wrapped the present that my sister chose for grandma.', False, False),
]
ROWS = list(PF3.ROWS) + NEW


def preflight(flags):
    lines, ok = [], True
    for name, sk, ann, wt, ans, ref, ep, en in ROWS:
        p = V4.decide(sk, ann, wt, ans, ref, 'primary', flags)['fired']
        n = V4.decide(sk, ann, wt, ans, ref, 'noun', flags)['fired']
        good = (p == ep and n == en)
        ok = ok and good
        lines.append('%-4s %-66s primary=%-5s (want %-5s)  noun=%-5s (want %-5s)'
                     % ('PASS' if good else 'FAIL', name, p, ep, n, en))
    same = all(V4.decide(r[1], r[2], r[3], r[4], r[5], v, flags=())['fired']
               == V3.decide(r[1], r[2], r[3], r[4], r[5], v, V4.V3_BASE)['fired']
               for r in ROWS for v in ('primary', 'noun'))
    lines.append('%-4s flags=() reproduces AG v3 bit for bit on all %d rows'
                 % ('PASS' if same else 'FAIL', len(ROWS)))
    ok = ok and same
    return ok, lines


# ---------------------------------------------------------------- gate: 1S blind-judge packet
def dec(name, fl, sk, a, wt, answer, ref):
    if fl is None:
        return V2.decide(sk, a, wt, answer, ref, "primary")
    return V4.decide(sk, a, wt, answer, ref, "primary", fl)


def packet_gate(configs):
    rows = L(os.path.join(TA1S, "rows_1s.json"))
    byiid = {r["iid"]: r for r in rows}
    sents = {s["sid"]: s for s in L(os.path.join(P1P, "data", "sentences.json"))}
    ann = L(os.path.join(P1P, "data", "annotations.json"))
    items = {it["id"]: it for it in L(os.path.join(P1P, "data", "items.json"))}
    key = L(os.path.join(TC1S, "_key.json"))
    verd = {v["jid"]: v for v in L(os.path.join(TC1S, "judge", "verdicts.json"))}
    out = {}
    for name, fl in configs:
        buckets = {}
        for jid, k in key.items():
            iid, b = k["iid"], k["bucket"]
            v = verd[jid]["verdict"]
            grp = ("agent drops (judged wrong)" if (b == "agentless" and v == "wrong") else
                   "agentless judged CORRECT" if b == "agentless" else
                   "by-passive controls" if b == "by-passive-control" else
                   "plain controls (judged correct)" if (b == "plain-control" and v == "correct")
                   else "plain control judged wrong" if b == "plain-control" else
                   "v2 misfires (judged correct)")
            it = items[iid]
            s = sents[it["sid"]]
            a = ann.get(str(it["sid"])) or {}
            wt = (s.get("tags") or {}).get("writer_tags") or {}
            ref = ((a.get("hygienised") or a).get("v") or [""])[0]
            d = dec(name, fl, s["slovak"], a, wt, it["answer"], ref)
            e = buckets.setdefault(grp, {"n": 0, "fired": 0, "missed": [], "hit": []})
            e["n"] += 1
            if d["fired"]:
                e["fired"] += 1
                e["hit"].append(iid)
            else:
                e["missed"].append({"iid": iid, "slovak": byiid[iid]["slovak"],
                                    "answer": byiid[iid]["answer"], "why": d["reason"]})
        out[name] = buckets
    return out


def gate_ok(b):
    g = lambda k: b.get(k, {"n": 0, "fired": 0})
    return (g("agent drops (judged wrong)")["fired"] >= 96
            and g("by-passive controls")["fired"] == 0
            and g("plain controls (judged correct)")["fired"] == 0)


# ---------------------------------------------------------------- 1T measurement (DESIGN-only)
CLASS = {}
for _i in ("W:180005:w3 W:180029:w3 W:180035:w3 W:180040:w3 W:180061:w3 W:180065:w3 W:180068:w3 "
           "W:180072:w3 W:180077:w3 W:180081:w3 W:180094:w3 W:180094:w4 W:180097:w3 "
           "W:180097:w4").split():
    CLASS[_i] = "A"
for _i in ("W:180026:w3 W:180032:w2 W:180035:w2 W:180052:w4 W:180060:w2 W:180060:w4 W:180061:w4 "
           "W:180073:w2 W:180086:w2").split():
    CLASS[_i] = "B"
for _i in ("W:180034:w2 W:180047:w2 W:180051:w3 W:180051:w4 W:180062:w2 W:180062:w3 W:180062:w4 "
           "W:180090:w3 W:180090:w4 W:180092:w4").split():
    CLASS[_i] = "C"
L3_ACCEPTED = set(("W:180026:w3 W:180034:w2 W:180035:w2 W:180052:w4 W:180061:w4 W:180062:w2 "
                   "W:180062:w3 W:180062:w4 W:180072:w3 W:180090:w3 W:180092:w4 W:180097:w3 "
                   "W:180097:w4").split())


def load_1t():
    SET = os.path.join(T1, "set")
    rows = L(os.path.join(T1, "run", "results_1t.json"))["rows"]
    items = {i["id"]: i for i in L(os.path.join(SET, "data", "items.json"))}
    sents = {s["sid"]: s for s in L(os.path.join(SET, "data", "sentences.json"))}
    apath = os.path.join(SET, "data", "annotations.json")
    ann = L(apath) if os.path.exists(apath) else {}
    if not ann:
        print("DIAG: no annotations.json in", SET, "- sentence keys:", sorted(list(sents.values())[0].keys()))
    return rows, items, sents, ann


def ref_of(a, s):
    r = ((a.get("hygienised") or a).get("v") or [""])[0] if a else ""
    if not r:
        for k in ("reference", "english", "en", "gold"):
            v = s.get(k)
            if isinstance(v, list) and v:
                return v[0]
            if isinstance(v, str) and v:
                return v
        v = (s.get("tags") or {}).get("reference")
        if isinstance(v, list) and v:
            return v[0]
        if isinstance(v, str):
            return v
    return r


def acc(r):
    for k in ("final_accept", "accept", "accepted"):
        if k in r:
            return bool(r[k])
    return None


def measure_1t(configs):
    rows, items, sents, ann = load_1t()
    lab = [r for r in rows if r.get("judged") in ("correct", "wrong")]
    tagc = Counter(t for r in rows for t in r.get("tags", []))
    res, mism = {}, 0
    src = {}
    for r in rows:
        it = items[r["item_id"]]
        s = sents[r["sid"]]
        a = (ann.get(str(r["sid"])) or ann.get(r["sid"]) or {}) if ann else {}
        wt = (s.get("tags") or {}).get("writer_tags") or {}
        src[r["item_id"]] = (s["slovak"], a, wt, it["answer"], ref_of(a, s))
    for name, fl in configs:
        fired = {}
        for r in rows:
            sk, a, wt, answer, ref = src[r["item_id"]]
            fired[r["item_id"]] = dec(name, fl, sk, a, wt, answer, ref)["fired"]
        if fl == ():
            mism = sum(1 for r in rows
                       if bool((r.get("ag") or {}).get("fired")) != fired[r["item_id"]])
        ad = [r for r in lab if any(t.startswith("agentdrop") for t in r["tags"])
              and r["judged"] == "wrong"]
        cost = [r for r in lab if r["judged"] == "correct" and fired[r["item_id"]]]
        rec = {"A": [], "B": [], "C": []}
        for i, c in CLASS.items():
            if fired.get(i):
                rec[c].append(i)
        e = {"fires": sum(1 for r in rows if fired[r["item_id"]]),
             "catches": sum(1 for r in lab if r["judged"] == "wrong" and fired[r["item_id"]]),
             "agentdrop_catches": sum(1 for r in ad if fired[r["item_id"]]),
             "agentdrop_n": len(ad),
             "measured_cost": len(cost),
             "cost_rows": [{"iid": r["item_id"], "sk": src[r["item_id"]][0],
                            "answer": src[r["item_id"]][3]} for r in cost],
             "recovered": {k: sorted(v) for k, v in rec.items()},
             "recovered_L3_accepted": {k: len([x for x in v if x in L3_ACCEPTED])
                                       for k, v in rec.items()}}
        for tag in sorted(tagc):
            e["rej_" + tag] = "%d/%d" % (sum(1 for r in rows if tag in r["tags"]
                                             and fired[r["item_id"]]), tagc[tag])
        res[name] = e
    return res, tagc, mism, len(rows), len(lab)


# ---------------------------------------------------------------- main
def main(measure=False):
    ok, pf = preflight(V4.ALL_FLAGS)
    print("\n".join(pf))
    print("PRE-FLIGHT %s (%d rows)" % ("PASS" if ok else "FAIL", len(pf)))
    cfgs = CONFIGS if measure else [("AG v2", None), ("AG v3 (= v4 flags=())", ()),
                                    (CHOSEN, dict(CONFIGS)[CHOSEN])]
    pk = packet_gate(cfgs)
    g = gate_ok(pk[CHOSEN])
    for n in cfgs:
        b = pk[n[0]]
        print("%-24s catches %2d/%d | by-passive %d/%d | plain %d/%d | v2-misfire %d/%d"
              % (n[0], b["agent drops (judged wrong)"]["fired"], b["agent drops (judged wrong)"]["n"],
                 b["by-passive controls"]["fired"], b["by-passive controls"]["n"],
                 b["plain controls (judged correct)"]["fired"],
                 b["plain controls (judged correct)"]["n"],
                 b.get("v2 misfires (judged correct)", {}).get("fired", 0),
                 b.get("v2 misfires (judged correct)", {}).get("n", 0)))
    print("GATE %s for %s" % ("PASS" if g else "FAIL", CHOSEN))
    if not measure:
        return 0 if (ok and g) else 1
    m, tagc, mism, nrows, nlab = measure_1t(CONFIGS)
    print("1T wiring self-check: v4(flags=()) disagrees with the stored v3 verdict on %d of %d rows"
          % (mism, nrows))
    print("1T tags:", dict(tagc))
    write_report(pf, ok, g, pk, m, tagc, mism, nrows, nlab)
    return 0 if (ok and g and mism == 0) else 1


def write_report(pf, ok, g, pk, m, tagc, mism, nrows, nlab):
    GR = ["agent drops (judged wrong)", "by-passive controls", "plain controls (judged correct)",
          "v2 misfires (judged correct)", "agentless judged CORRECT", "plain control judged wrong"]
    md = ["# Phase 1U Task A - AG v4 regression (0 model calls, 0 network, no DB)\n",
          "**DESIGN-only.** Both measurement sets (the 1S blind-judge packet and the closed 1T set) "
          "are sets the rule was built on or already opened. Nothing here is a held-out result.\n",
          "Flags: `union` (guarded whole-sentence OR per-clause), `unionx` (raw union, measured not "
          "selected), `lex` (2.2 lexicon), `align` (2.3 class B), `local` (2.3 class A). "
          "`flags=()` reproduces AG v3 bit for bit.\n",
          "## Pre-flight (synthetic rows only)\n", "```", "\n".join(pf),
          "PRE-FLIGHT %s" % ("PASS" if ok else "FAIL"), "```\n",
          "## Gate 1 (RUN FIRST) - the 183-item 1S blind-judge packet\n",
          "| config | " + " | ".join("%s (n=%d)" % (x, pk[CONFIGS[0][0]].get(x, {}).get("n", 0))
                                     for x in GR) + " |",
          "| --- |" + " --- |" * len(GR)]
    for n, _ in CONFIGS:
        md.append("| %s | " % n + " | ".join(str(pk[n].get(x, {}).get("fired", 0)) for x in GR)
                  + " |")
    md += ["\nGate: >= 96/97 agent drops caught, 0/42 by-passive controls, 0/39 plain controls. "
           "**%s** for `%s`.\n" % ("PASS" if g else "FAIL", CHOSEN),
           "### remaining packet misses of the chosen configuration\n",
           "| iid | Slovak | answer | why |", "| --- | --- | --- | --- |"]
    for x in pk[CHOSEN]["agent drops (judged wrong)"]["missed"]:
        md.append("| %s | %s | %s | %s |" % (x["iid"], x["slovak"], x["answer"], x["why"]))
    md += ["\n## Gate 2 - the 1T set (%d items, %d judged), DESIGN-only\n" % (nrows, nlab),
           "Wiring self-check: `flags=()` disagrees with the AG verdict stored in results_1t.json "
           "on **%d** of %d rows.\n" % (mism, nrows)]
    tags = sorted(tagc)
    md += ["| config | fires | catches (judged wrong) | agent-drop catches | MEASURED COST "
           "(judged-correct rejected) | " + " | ".join("%s /%d" % (t, tagc[t]) for t in tags) + " |",
           "| --- | --- | --- | --- | --- |" + " --- |" * len(tags)]
    for n, _ in CONFIGS:
        e = m[n]
        md.append("| %s | %d | %d | %d/%d | %d | " % (n, e["fires"], e["catches"],
                                                      e["agentdrop_catches"], e["agentdrop_n"],
                                                      e["measured_cost"])
                  + " | ".join(e["rej_" + t] for t in tags) + " |")
    md += ["\n### the 33 v3 misses recovered, BY CLASS\n",
           "| config | A: fronted subordinate clause (n=14) | B: clause misalignment (n=9) | "
           "C: passive not seen (n=10) | of the recovered, L3 had accepted |",
           "| --- | --- | --- | --- | --- |"]
    for n, _ in CONFIGS:
        e = m[n]
        md.append("| %s | %d/14 | %d/9 | %d/10 | A %d, B %d, C %d |"
                  % (n, len(e["recovered"]["A"]), len(e["recovered"]["B"]),
                     len(e["recovered"]["C"]), e["recovered_L3_accepted"]["A"],
                     e["recovered_L3_accepted"]["B"], e["recovered_L3_accepted"]["C"]))
    md += ["\n### MEASURED COST of the chosen configuration on the 1T set\n",
           "| iid | Slovak | answer |", "| --- | --- | --- |"]
    for x in m[CHOSEN]["cost_rows"]:
        md.append("| %s | %s | %s |" % (x["iid"], x["sk"], x["answer"]))
    if not m[CHOSEN]["cost_rows"]:
        md.append("| - | (no judged-correct answer of the 1T set is rejected by AG v4) | - |")
    md += ["\n### remaining misses of AG v4 among the 33\n",
           "| iid | class | L3 accepted | reason it still abstains |", "| --- | --- | --- | --- |"]
    rows, items, sents, ann = load_1t()
    srcs = {r["item_id"]: r for r in rows}
    for i, c in sorted(CLASS.items(), key=lambda kv: (kv[1], kv[0])):
        if i in sum(m[CHOSEN]["recovered"].values(), []):
            continue
        r = srcs.get(i)
        s = sents[r["sid"]] if r else None
        a = (ann.get(str(r["sid"])) or {}) if (ann and r) else {}
        wt = (s.get("tags") or {}).get("writer_tags") or {} if s else {}
        d = V4.decide(s["slovak"], a, wt, items[i]["answer"], ref_of(a, s), "primary",
                      V4.ALL_FLAGS) if s else {"reason": "?"}
        md.append("| %s | %s | %s | %s |" % (i, c, "yes" if i in L3_ACCEPTED else "no",
                                             d.get("reason")))
    md += ["\n## Chosen configuration\n",
           "`agent_drop_v4.ALL_FLAGS = %r` - selected on MEASURED COST (judged-correct answers "
           "rejected), never on gold-assertion accuracy; see the cost columns above.\n" %
           (V4.ALL_FLAGS,),
           "Runner import line:\n",
           "```python", "import sys, os",
           "sys.path.insert(0, os.path.expanduser('~/Projects/and-again-content/translation-"
           "offline/phase1u/taskA'))",
           "import agent_drop_v4 as AG   # AG.decide(sk, ann, wtags, answer, reference, 'primary',"
           " AG.ALL_FLAGS)", "```"]
    open(os.path.join(HERE, "AG_V4_REGRESSION.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
    json.dump({"preflight": pf, "preflight_ok": ok, "gate_ok": g, "packet": pk, "set_1t": m,
               "tags_1t": dict(tagc), "wiring_mismatch": mism, "chosen": CHOSEN,
               "flags": list(V4.ALL_FLAGS), "model_calls": 0},
              open(os.path.join(HERE, "AG_V4_REGRESSION.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    sys.exit(main("--measure" in sys.argv))
