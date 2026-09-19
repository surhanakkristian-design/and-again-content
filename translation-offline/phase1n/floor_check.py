#!/usr/bin/env python3
"""Phase 1N floor check — run BEFORE the model run, on JUDGED counts only.

Merges judge/out_part*.json through judge/blind_map.json onto data/items.json,
and judge/out_controls.json through judge/controls_map.json.  No model call.

Outputs: FLOOR_CHECK.md, floor_check.json, and (only when a floor is missed and
no judge file is bad) data/topup_request.json.  Every label file it opens is
appended to access_log.jsonl.
"""
import json, os, math, datetime, collections

HERE = os.path.dirname(os.path.abspath(__file__))
JUDGE = os.path.join(HERE, "judge")
DATA = os.path.join(HERE, "data")
LOG = os.path.join(HERE, "access_log.jsonl")
CALLER = "floor_check.py"
PURPOSE = "Phase 1N floor check on judged counts (pre-run)"
TYPES = ("T", "W", "M", "S")
TF_FLOOR, PASSIVE_FLOOR = 150, 60

_logged = []


def log(side, what, n):
    _logged.append({"ts": datetime.datetime.now(datetime.timezone.utc)
                    .strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "side": side, "what": what, "caller": CALLER,
                    "n": n, "purpose": PURPOSE})


def flush_log():
    with open(LOG, "a", encoding="utf-8") as fh:
        for r in _logged:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


# ---------- Clopper-Pearson (exact), no scipy ----------
def _betacf(a, b, x):
    tiny, eps = 1e-300, 3e-16
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d, h = 1.0 / d, 1.0 / d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        c = 1.0 + aa / c
        if abs(d) < tiny:
            d = tiny
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        c = 1.0 + aa / c
        if abs(d) < tiny:
            d = tiny
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < eps:
            break
    return h


def betai(a, b, x):
    """Regularised incomplete beta I_x(a,b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lb = (math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
          + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return math.exp(lb) * _betacf(a, b, x) / a
    return 1.0 - math.exp(lb) * _betacf(b, a, 1.0 - x) / b


def betainv(p, a, b):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if betai(a, b, mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def cp(k, n, alpha=0.05):
    """Exact 95% Clopper-Pearson interval for k/n."""
    if n == 0:
        return (0.0, 0.0, 1.0)
    lo = 0.0 if k == 0 else betainv(alpha / 2.0, k, n - k + 1)
    hi = 1.0 if k == n else betainv(1.0 - alpha / 2.0, k + 1, n - k)
    return (k / n, lo, hi)


def pct(x):
    return f"{100.0 * x:.2f} %"


# ---------- load the label side ----------
items = json.load(open(os.path.join(DATA, "items.json"), encoding="utf-8"))
log("new_1n", "data/items.json", len(items))
by_id = {it["id"]: it for it in items}

blind = json.load(open(os.path.join(JUDGE, "blind_map.json"), encoding="utf-8"))
log("new_1n", "judge/blind_map.json", len(blind))
cmap = json.load(open(os.path.join(JUDGE, "controls_map.json"), encoding="utf-8"))
log("new_1n", "judge/controls_map.json", len(cmap))

# a part is REQUIRED iff its input packet exists
required = [i for i in range(1, 10)
            if os.path.exists(os.path.join(JUDGE, f"in_part{i}.json"))]
absent_by_design = [f"part{i}" for i in range(1, 10) if i not in required]

bad_parts, bad_reasons = [], {}
rows_by_label = {}


def check_file(label, path, keymap):
    """Returns list of rows, or None when the file is BAD."""
    reasons = []
    if not os.path.exists(path):
        bad_parts.append(label)
        bad_reasons[label] = ["missing"]
        return None
    try:
        rows = json.load(open(path, encoding="utf-8"))
    except Exception as exc:
        bad_parts.append(label)
        bad_reasons[label] = [f"does not parse: {exc}"]
        return None
    log("new_1n", os.path.relpath(path, HERE),
        len(rows) if isinstance(rows, list) else -1)
    if not isinstance(rows, list):
        bad_parts.append(label)
        bad_reasons[label] = ["not a list of rows"]
        return None
    nojid = [i for i, r in enumerate(rows)
             if not isinstance(r, dict) or not r.get("jid")]
    if nojid:
        reasons.append(f"{len(nojid)} row(s) lack a jid (first at index {nojid[0]})")
    unknown = sorted({r.get("jid") for r in rows
                      if isinstance(r, dict) and r.get("jid")
                      and r["jid"] not in keymap})
    if unknown:
        reasons.append(f"{len(unknown)} unknown jid(s): {unknown[:5]}")
    badtype = sorted({r.get("jid") for r in rows
                      if isinstance(r, dict) and r.get("judged") == "wrong"
                      and r.get("type") not in TYPES})
    if badtype:
        reasons.append(f"{len(badtype)} wrong row(s) without a type in T/W/M/S: "
                       f"{badtype[:5]}")
    badverdict = sorted({r.get("jid") for r in rows
                         if isinstance(r, dict)
                         and r.get("judged") not in ("correct", "wrong")})
    if badverdict:
        reasons.append(f"{len(badverdict)} row(s) with a verdict outside "
                       f"correct/wrong: {badverdict[:5]}")
    dups = [j for j, c in collections.Counter(
        r.get("jid") for r in rows if isinstance(r, dict)).items() if c > 1]
    if dups:
        reasons.append(f"{len(dups)} duplicated jid(s): {sorted(dups)[:5]}")
    if reasons:
        bad_parts.append(label)
        bad_reasons[label] = reasons
        return None
    return rows


for i in required:
    lbl = f"part{i}"
    rows_by_label[lbl] = check_file(
        lbl, os.path.join(JUDGE, f"out_part{i}.json"), blind)
rows_by_label["controls"] = check_file(
    "controls", os.path.join(JUDGE, "out_controls.json"), cmap)

# ---------- merge ----------
judged = {}          # item id -> judge row (main parts)
jid_seen = {}
for lbl in [f"part{i}" for i in required]:
    for r in (rows_by_label[lbl] or []):
        jid_seen[r["jid"]] = lbl
        judged[blind[r["jid"]]] = dict(r, part=lbl)

missing_jids = sorted(set(blind) - set(jid_seen))
coverage_ok = not missing_jids and not bad_parts
if missing_jids:
    owner = collections.Counter()
    for j in missing_jids:
        owner[jid_seen.get(j, "?")] += 1

merged = [dict(by_id[iid], **{"judged": row["judged"],
                              "jtype": row.get("type"),
                              "jpassive": row.get("passive"),
                              "part": row["part"]})
          for iid, row in judged.items()]

# ---------- counts ----------
judged_correct = sum(1 for m in merged if m["judged"] == "correct")
judged_wrong = sum(1 for m in merged if m["judged"] == "wrong")

intent_x_judged = collections.Counter((m["intent"], m["judged"]) for m in merged)
intents = ["C", "TF", "T", "W", "M", "S"]
type_dist = collections.Counter(m["jtype"] for m in merged if m["judged"] == "wrong")

# TIME-FRAME floor
tf_items = [m for m in merged if m["intent"] == "TF"]
tf_judged_wrong = sum(1 for m in tf_items if m["judged"] == "wrong")
tf_wrong_typeT = sum(1 for m in tf_items
                     if m["judged"] == "wrong" and m["jtype"] == "T")
tf_ok = tf_judged_wrong >= TF_FLOOR

# PASSIVE floor
pas = [m for m in merged if m["passive"] in ("by", "agentless")]
by_items = [m for m in pas if m["passive"] == "by"]
ag_items = [m for m in pas if m["passive"] == "agentless"]
by_correct = sum(1 for m in by_items if m["judged"] == "correct")
agentless_correct = sum(1 for m in ag_items if m["judged"] == "correct")
passives_judged_correct = by_correct + agentless_correct
pas_ok = passives_judged_correct >= PASSIVE_FLOOR

# judge passive tag x writer passive tag (all merged items)
ptags = ["by", "agentless", None]
pcross = collections.Counter((m["passive"], m["jpassive"]) for m in merged)

# writer vs judge disagreements
verdict_dis = {"writer_C_judged_wrong": [], "writer_wrong_judged_correct": []}
type_dis = collections.Counter()
for m in merged:
    if m["intent"] == "C" and m["judged"] == "wrong":
        verdict_dis["writer_C_judged_wrong"].append(m["id"])
    elif m["intent"] != "C" and m["judged"] == "correct":
        verdict_dis["writer_wrong_judged_correct"].append(m["id"])
    elif m["intent"] != "C" and m["judged"] == "wrong":
        exp = "T" if m["intent"] in ("TF", "T") else m["intent"]
        if m["jtype"] != exp:
            type_dis[(m["intent"], m["jtype"])] += 1

n_verdict_dis = len(verdict_dis["writer_C_judged_wrong"]) + \
    len(verdict_dis["writer_wrong_judged_correct"])
n_type_dis = sum(type_dis.values())

# ---------- control noise ----------
ctl_rows = rows_by_label.get("controls") or []
pairs, ctl_judged_mismatch, ctl_type_mismatch, ctl_both_wrong, ctl_type_bw = \
    [], 0, 0, 0, 0
for r in ctl_rows:
    iid = cmap[r["jid"]]
    main = judged.get(iid)
    if not main:
        continue
    jm = r["judged"] != main["judged"]
    tm = r.get("type") != main.get("type")
    ctl_judged_mismatch += jm
    ctl_type_mismatch += tm
    if r["judged"] == "wrong" and main["judged"] == "wrong":
        ctl_both_wrong += 1
        ctl_type_bw += (r.get("type") != main.get("type"))
    pairs.append({"kid": r["jid"], "item": iid,
                  "control": [r["judged"], r.get("type")],
                  "main": [main["judged"], main.get("type")],
                  "judged_mismatch": bool(jm), "type_mismatch": bool(tm)})
n_ctl = len(pairs)
cp_judged = cp(ctl_judged_mismatch, n_ctl)
cp_type = cp(ctl_type_mismatch, n_ctl)
cp_type_bw = cp(ctl_type_bw, ctl_both_wrong)

floors_ok = tf_ok and pas_ok

# ---------- top-up request ----------
topup = None
topup_path = os.path.join(DATA, "topup_request.json")
if not floors_ok and not bad_parts:
    tf_by_sid = collections.Counter(m["sid"] for m in merged if m["intent"] == "TF")
    by_by_sid = collections.Counter(m["sid"] for m in merged if m["passive"] == "by")
    req = {"generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "reason": [], "tf": [], "passive_by": []}
    if not tf_ok:
        need = (TF_FLOOR - tf_judged_wrong) + 10
        cand = sorted(s for s, c in tf_by_sid.items() if c == 1)
        req["reason"].append(
            f"TIME-FRAME floor missed: {tf_judged_wrong} < {TF_FLOOR}; "
            f"shortfall {TF_FLOOR - tf_judged_wrong} + 10 = {need} extra TF answers")
        for s in cand[:need]:
            req["tf"].append({"sid": s, "extra_tf_answers": 1})
        if len(cand) < need:
            req["tf_note"] = (f"only {len(cand)} sids have exactly one TF item; "
                              f"{need - len(cand)} further answers must be spread "
                              f"over sids that already have two")
    if not pas_ok:
        need = (PASSIVE_FLOOR - passives_judged_correct) + 5
        cand = sorted(s for s, c in by_by_sid.items() if c >= 1)
        req["reason"].append(
            f"PASSIVE floor missed: {passives_judged_correct} < {PASSIVE_FLOOR}; "
            f"shortfall {PASSIVE_FLOOR - passives_judged_correct} + 5 = {need} "
            f"extra by-passives")
        for s in cand[:need]:
            req["passive_by"].append({"sid": s, "extra_by_answers": 1})
        if len(cand) < need:
            req["passive_note"] = (f"only {len(cand)} passivizable sids are "
                                   f"available; {need - len(cand)} further "
                                   f"by-answers need a second one per sid")
    topup = req
    json.dump(req, open(topup_path, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

# ---------- json ----------
out = {
    "phase": "1N", "label": "floor-check-1", "when": datetime.datetime.now(
        datetime.timezone.utc).isoformat(), "model_calls": 0,
    "floors_ok": floors_ok,
    "bad_parts": bad_parts,
    "bad_reasons": bad_reasons,
    "parts_required": [f"part{i}" for i in required],
    "parts_absent_by_design": absent_by_design,
    "coverage": {"jids_in_blind_map": len(blind), "jids_judged": len(jid_seen),
                 "missing_jids": missing_jids[:20],
                 "n_missing": len(missing_jids), "items_merged": len(merged),
                 "coverage_ok": coverage_ok},
    "judged_correct": judged_correct,
    "judged_wrong": judged_wrong,
    "judged_correct_rate": judged_correct / len(merged) if merged else 0.0,
    "intent_x_judged": {f"{i}|{v}": intent_x_judged[(i, v)]
                        for i in intents for v in ("correct", "wrong")},
    "judged_type_distribution": {str(k): v for k, v in
                                 sorted(type_dist.items(), key=lambda kv: str(kv[0]))},
    "tf_floor": {"required": TF_FLOOR, "n_tf_items": len(tf_items),
                 "tf_judged_wrong": tf_judged_wrong,
                 "tf_wrong_and_type_T": tf_wrong_typeT, "ok": tf_ok,
                 "margin": tf_judged_wrong - TF_FLOOR},
    "tf_judged_wrong": tf_judged_wrong,
    "passive_floor": {"required": PASSIVE_FLOOR, "n_passive_items": len(pas),
                      "by_total": len(by_items), "agentless_total": len(ag_items),
                      "by_correct": by_correct,
                      "agentless_correct": agentless_correct,
                      "passives_judged_correct": passives_judged_correct,
                      "ok": pas_ok,
                      "margin": passives_judged_correct - PASSIVE_FLOOR},
    "passives_judged_correct": passives_judged_correct,
    "by_correct": by_correct,
    "agentless_correct": agentless_correct,
    "passive_cross_tab_writer_x_judge": {
        f"{w or 'null'}|{j or 'null'}": pcross[(w, j)]
        for w in ptags for j in ptags},
    "writer_vs_judge": {
        "verdict_disagreements": n_verdict_dis,
        "writer_C_judged_wrong": len(verdict_dis["writer_C_judged_wrong"]),
        "writer_wrong_judged_correct": len(verdict_dis["writer_wrong_judged_correct"]),
        "type_disagreements": n_type_dis,
        "type_disagreement_cells": {f"{i}->{t}": c for (i, t), c in
                                    sorted(type_dis.items(),
                                           key=lambda kv: -kv[1])},
        "examples_C_judged_wrong": verdict_dis["writer_C_judged_wrong"][:10],
        "examples_wrong_judged_correct":
            verdict_dis["writer_wrong_judged_correct"][:10]},
    "control_noise": {
        "n": n_ctl,
        "judged_mismatch": ctl_judged_mismatch,
        "judged_rate": cp_judged[0], "judged_ci95": [cp_judged[1], cp_judged[2]],
        "type_mismatch": ctl_type_mismatch,
        "type_rate": cp_type[0], "type_ci95": [cp_type[1], cp_type[2]],
        "both_wrong_pairs": ctl_both_wrong,
        "type_mismatch_both_wrong": ctl_type_bw,
        "type_both_wrong_rate": cp_type_bw[0],
        "type_both_wrong_ci95": [cp_type_bw[1], cp_type_bw[2]],
        "mismatch_pairs": [p for p in pairs
                           if p["judged_mismatch"] or p["type_mismatch"]]},
    "topup_request_written": bool(topup),
}
json.dump(out, open(os.path.join(HERE, "floor_check.json"), "w",
                    encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- markdown ----------
def row(*c):
    return "| " + " | ".join(str(x) for x in c) + " |"


L = ["# Phase 1N — floor check (pre-run, judged counts)", "",
     f"Run {out['when']} by `floor_check.py`, label **floor-check-1**. "
     "No model call was made on this set; the check reads the human/blind judge "
     "output only.", "",
     "## 1. Judge files", "",
     row("file", "status", "rows"), row("---", "---", "---")]
for lbl in [f"part{i}" for i in required] + ["controls"]:
    r = rows_by_label.get(lbl)
    L.append(row(f"`out_{lbl}.json`", "BAD — " + "; ".join(bad_reasons[lbl])
                 if lbl in bad_parts else "ok", len(r) if r is not None else "–"))
for lbl in absent_by_design:
    L.append(row(f"`out_{lbl}.json`", "not required (no `in_" + lbl + ".json`)", "–"))
L += ["",
      f"- bad files: **{bad_parts if bad_parts else 'none'}**",
      f"- jids in `blind_map.json`: {len(blind)}; judged: {len(jid_seen)}; "
      f"missing: {len(missing_jids)}",
      f"- items merged onto `data/items.json`: {len(merged)}",
      f"- controls merged onto `controls_map.json`: {n_ctl} of {len(cmap)}", "",
      "## 2. Judged totals", "",
      row("verdict", "n", "share"), row("---", "---", "---"),
      row("correct", judged_correct, pct(judged_correct / len(merged))),
      row("wrong", judged_wrong, pct(judged_wrong / len(merged))),
      row("**total**", len(merged), "100 %"), "",
      "## 3. Writer intent x judged verdict", "",
      row("writer intent", "n", "judged correct", "judged wrong", "% wrong"),
      row("---", "---", "---", "---", "---")]
for i in intents:
    c, w = intent_x_judged[(i, "correct")], intent_x_judged[(i, "wrong")]
    n = c + w
    L.append(row(i, n, c, w, pct(w / n) if n else "–"))
L += ["", "## 4. Judged type distribution (wrong rows)", "",
      row("type", "n", "share of wrong"), row("---", "---", "---")]
for t in list(TYPES) + [k for k in type_dist if k not in TYPES]:
    n = type_dist.get(t, 0)
    L.append(row(str(t), n, pct(n / judged_wrong) if judged_wrong else "–"))
L += ["", "## 5. TIME-FRAME floor", "",
      f"- writer intent TF items: **{len(tf_items)}**",
      f"- of them judged WRONG: **{tf_judged_wrong}** (required >= {TF_FLOOR}) — "
      f"**{'PASS' if tf_ok else 'MISSED'}**, margin {tf_judged_wrong - TF_FLOOR}",
      f"- of those wrong ones carrying judge type `T`: {tf_wrong_typeT}", "",
      "## 6. PASSIVE floor", "",
      row("writer passive tag", "items", "judged correct", "judged wrong", "% correct"),
      row("---", "---", "---", "---", "---"),
      row("by", len(by_items), by_correct, len(by_items) - by_correct,
          pct(by_correct / len(by_items)) if by_items else "–"),
      row("agentless", len(ag_items), agentless_correct,
          len(ag_items) - agentless_correct,
          pct(agentless_correct / len(ag_items)) if ag_items else "–"),
      row("**by + agentless**", len(pas), passives_judged_correct,
          len(pas) - passives_judged_correct,
          pct(passives_judged_correct / len(pas)) if pas else "–"), "",
      f"- required >= {PASSIVE_FLOOR} judged correct — "
      f"**{'PASS' if pas_ok else 'MISSED'}**, margin "
      f"{passives_judged_correct - PASSIVE_FLOOR}", "",
      "### 6.1 Judge's own passive tag x writer's passive tag (all merged items)", "",
      row("writer \\ judge", "by", "agentless", "null", "total"),
      row("---", "---", "---", "---", "---")]
for w in ptags:
    cells = [pcross[(w, j)] for j in ptags]
    L.append(row(str(w or "null"), *cells, sum(cells)))
L.append(row("**total**", *[sum(pcross[(w, j)] for w in ptags) for j in ptags],
             len(merged)))
L += ["", "## 7. Writer versus judge disagreements", "",
      f"- verdict disagreements: **{n_verdict_dis}** of {len(merged)} "
      f"({pct(n_verdict_dis / len(merged))})",
      f"  - writer C, judged wrong: {len(verdict_dis['writer_C_judged_wrong'])}",
      f"  - writer wrong, judged correct: "
      f"{len(verdict_dis['writer_wrong_judged_correct'])}",
      f"- type disagreements among rows both sides call wrong: **{n_type_dis}**",
      "", row("writer intent -> judge type", "n"), row("---", "---")]
for (i, t), c in sorted(type_dis.items(), key=lambda kv: -kv[1])[:12]:
    L.append(row(f"{i} -> {t}", c))
if not type_dis:
    L.append(row("none — every wrong row got the writer's type "
                 "(TF and T both map to `T`)", 0))
L += ["", "## 8. Control noise (80 duplicated items, re-judged blind)", "",
      row("mismatch", "k / n", "rate", "exact 95 % CP interval"),
      row("---", "---", "---", "---"),
      row("judged verdict", f"{ctl_judged_mismatch} / {n_ctl}", pct(cp_judged[0]),
          f"[{pct(cp_judged[1])}, {pct(cp_judged[2])}]"),
      row("type field", f"{ctl_type_mismatch} / {n_ctl}", pct(cp_type[0]),
          f"[{pct(cp_type[1])}, {pct(cp_type[2])}]"),
      row("type, both-wrong pairs only",
          f"{ctl_type_bw} / {ctl_both_wrong}", pct(cp_type_bw[0]),
          f"[{pct(cp_type_bw[1])}, {pct(cp_type_bw[2])}]"), "",
      "## 9. Verdict", "",
      f"- floors_ok: **{floors_ok}**",
      f"- bad judge files: **{bad_parts if bad_parts else 'none'}**",
      f"- top-up request written: **{bool(topup)}**"
      + (f" -> `data/topup_request.json`" if topup else ""), ""]
if topup:
    for r_ in topup["reason"]:
        L.append(f"  - {r_}")
    L.append(f"  - TF sids asked for one extra TF answer: {len(topup['tf'])}")
    L.append(f"  - sids asked for one extra by-passive: {len(topup['passive_by'])}")
    L.append("")
L += ["Files: `FLOOR_CHECK.md`, `floor_check.json`"
      + (", `data/topup_request.json`" if topup else "")
      + f"; {len(_logged)} label reads appended to `access_log.jsonl`.", ""]

open(os.path.join(HERE, "FLOOR_CHECK.md"), "w", encoding="utf-8").write("\n".join(L))
flush_log()

print(json.dumps({"floors_ok": floors_ok, "bad_parts": bad_parts,
                  "judged_correct": judged_correct, "judged_wrong": judged_wrong,
                  "tf_judged_wrong": tf_judged_wrong,
                  "passives_judged_correct": passives_judged_correct,
                  "by_correct": by_correct,
                  "agentless_correct": agentless_correct,
                  "ctl_judged_mismatch": ctl_judged_mismatch,
                  "ctl_type_mismatch": ctl_type_mismatch,
                  "n_missing_jids": len(missing_jids),
                  "verdict_dis": n_verdict_dis, "type_dis": n_type_dis,
                  "topup": bool(topup)}, ensure_ascii=False))
