#!/usr/bin/env python3
"""Phase 1m — label 'assemble'.

Builds and validates the new 140-sentence set:
  data/items.json, data/annotations.json, judge/in_part1..6.json,
  judge/in_controls.json, judge/blind_map.json, judge/controls_map.json,
  data/ITEMS_SUMMARY.md

No model calls, no DB, deterministic. Never edits answers/sentences/annotations —
problems are only reported.
"""
import json, os, re, sys, zlib, random, unicodedata
from datetime import datetime, timezone
from collections import Counter, defaultdict

P1M = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(P1M, "data")
JUDGE = os.path.join(P1M, "judge")
LOG = os.path.join(P1M, "access_log.jsonl")
CALLER = "assemble_1m.py"

REQ_TOP = ["hygienised", "raw", "tf_gold", "voice_sk", "agent_nom",
           "perfective_present", "tense_open"]
REQ_INNER = ["id", "t", "lv", "v", "lk", "alt"]
LEVELS = ["A1", "A2", "B1", "B2"]
V_FORMS = ["passive", "cleft", "reported", "dropped"]
INTENTS = ["C", "V", "TF", "T", "W", "M", "S"]

problems = []


def prob(msg):
    problems.append(msg)


def log(side, what, n, purpose):
    rec = {"ts": datetime.now(timezone.utc).isoformat(), "side": side,
           "what": what, "caller": CALLER, "n": n, "purpose": purpose}
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def load(path, side, what, purpose, n_of=len):
    with open(path, encoding="utf-8") as fh:
        obj = json.load(fh)
    log(side, what, n_of(obj), purpose)
    return obj


def crc(text):
    return zlib.crc32(text.encode("utf-8")) & 0xffffffff


PUNCT = re.compile(r"[^\w\s]", re.UNICODE)


def norm(text):
    t = unicodedata.normalize("NFKC", text).lower()
    t = PUNCT.sub(" ", t)
    return " ".join(t.split())


def toks(text):
    return set(norm(text).split())


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# ---------------------------------------------------------------- 1. inputs
sents = load(os.path.join(DATA, "sentences.json"), "new_1m", "data/sentences.json",
             "assemble items + validate composition")
answers = []
for i in (1, 2, 3, 4):
    answers += load(os.path.join(DATA, f"answers_part{i}.json"), "new_1m",
                    f"data/answers_part{i}.json", "assemble items")
ann_parts = []
for i in (1, 2):
    ann_parts.append(load(os.path.join(DATA, f"annotations_part{i}.json"), "new_1m",
                          f"data/annotations_part{i}.json", "merge annotations"))
existing = load(os.path.join(P1M, "existing_210.json"), "existing", "existing_210.json",
                "overlap check against the new Slovak sentences")

by_sid = {s["sid"]: s for s in sents}
ALL_SIDS = list(range(150001, 150141))

if len(sents) != 140:
    prob(f"sentences.json has {len(sents)} sentences, expected 140")
missing_s = [s for s in ALL_SIDS if s not in by_sid]
extra_s = [s for s in by_sid if s not in set(ALL_SIDS)]
if missing_s:
    prob(f"sentences.json missing sids: {missing_s[:10]} (n={len(missing_s)})")
if extra_s:
    prob(f"sentences.json has out-of-range sids: {sorted(extra_s)[:10]}")

ans_by_sid = {}
for rec in answers:
    sid = rec["sid"]
    if sid in ans_by_sid:
        prob(f"sid {sid}: duplicate answer record across answers_part files")
    ans_by_sid[sid] = rec
for sid in ALL_SIDS:
    if sid not in ans_by_sid:
        prob(f"sid {sid}: no answer record")

# ---------------------------------------------------------- 2. annotations
merged = {}
for part in ann_parts:
    for k, v in part.items():
        if k in merged:
            prob(f"sid {k}: annotation present in both annotation parts")
        merged[k] = v
for sid in ALL_SIDS:
    key = str(sid)
    a = merged.get(key)
    if a is None:
        prob(f"sid {sid}: annotation missing")
        continue
    for k in REQ_TOP:
        if k not in a:
            prob(f"sid {sid}: annotation missing top-level key '{k}'")
    for half in ("hygienised", "raw"):
        h = a.get(half)
        if not isinstance(h, dict):
            prob(f"sid {sid}: annotation.{half} is not an object")
            continue
        for k in REQ_INNER:
            if k not in h:
                prob(f"sid {sid}: annotation.{half} missing key '{k}'")
        if h.get("id") != sid:
            prob(f"sid {sid}: annotation.{half}.id = {h.get('id')}")
        if sid in by_sid and h.get("lv") != by_sid[sid]["level"]:
            prob(f"sid {sid}: annotation.{half}.lv={h.get('lv')} != level {by_sid[sid]['level']}")
        v, lk = h.get("v"), h.get("lk")
        if not isinstance(v, list) or not v:
            prob(f"sid {sid}: annotation.{half}.v empty/not a list")
        if not isinstance(lk, list) or (isinstance(v, list) and len(lk or []) != len(v)):
            prob(f"sid {sid}: annotation.{half}.lk not parallel to v "
                 f"({len(lk or [])} vs {len(v or [])})")
        if not isinstance(h.get("alt"), dict):
            prob(f"sid {sid}: annotation.{half}.alt is not an object")
extra_ann = [k for k in merged if k not in {str(s) for s in ALL_SIDS}]
if extra_ann:
    prob(f"annotations with out-of-range sids: {sorted(extra_ann)[:10]}")

with open(os.path.join(DATA, "annotations.json"), "w", encoding="utf-8") as fh:
    json.dump({str(s): merged[str(s)] for s in ALL_SIDS if str(s) in merged},
              fh, ensure_ascii=False, indent=1, sort_keys=True)

# --------------------------------------------------------------- 3. items
items = []
n_correct = n_wrong = 0
for sid in ALL_SIDS:
    rec = ans_by_sid.get(sid)
    if rec is None:
        continue
    cor = rec.get("correct", [])
    wro = rec.get("wrong", [])
    if len(cor) != 4:
        prob(f"sid {sid}: {len(cor)} correct answers, expected 4")
    if len(wro) != 5:
        prob(f"sid {sid}: {len(wro)} wrong answers, expected 5")
    seen = {}
    for text in cor:
        if not isinstance(text, str) or not text.strip():
            prob(f"sid {sid}: empty correct answer")
            continue
        key = norm(text)
        if key in seen:
            prob(f"sid {sid}: duplicate answer text (normalised) '{text}' vs '{seen[key]}'")
        seen[key] = text
        items.append({"id": f"C:{sid}:{crc(text)}", "sid": sid, "kind": "C",
                      "intent": "C", "form": None, "answer": text})
        n_correct += 1
    for w in wro:
        text = w.get("answer")
        intent = w.get("intent")
        form = w.get("form")
        if not isinstance(text, str) or not text.strip():
            prob(f"sid {sid}: empty wrong answer")
            continue
        key = norm(text)
        if key in seen:
            prob(f"sid {sid}: duplicate answer text (normalised) '{text}' vs '{seen[key]}'")
        seen[key] = text
        if intent not in INTENTS or intent == "C":
            prob(f"sid {sid}: wrong answer has bad intent {intent!r}")
        if intent == "V":
            if form not in V_FORMS:
                prob(f"sid {sid}: V answer has bad form {form!r}")
        elif form is not None:
            prob(f"sid {sid}: intent {intent} has non-null form {form!r}")
        items.append({"id": f"W:{sid}:{crc(text)}", "sid": sid, "kind": "W",
                      "intent": intent, "form": form, "answer": text})
        n_wrong += 1

ids = Counter(i["id"] for i in items)
dups = [i for i, c in ids.items() if c > 1]
if dups:
    prob(f"duplicate item ids: {dups[:5]} (n={len(dups)})")
if n_correct != 560:
    prob(f"{n_correct} correct items, expected 560")
if n_wrong != 700:
    prob(f"{n_wrong} wrong items, expected 700")

with open(os.path.join(DATA, "items.json"), "w", encoding="utf-8") as fh:
    json.dump(items, fh, ensure_ascii=False, indent=1)

# --------------------------------------------------- 4. overlap / composition
new_toks = {s["sid"]: toks(s["slovak"]) for s in sents}
ex_norm = {}
for e in existing:
    ex_norm.setdefault(norm(e["slovak"]), e["sid"])
ex_toks = [(e["sid"], toks(e["slovak"])) for e in existing]
max_j = 0.0
max_pair = None
for s in sents:
    n = norm(s["slovak"])
    if n in ex_norm:
        prob(f"sid {s['sid']}: Slovak sentence identical to existing sid {ex_norm[n]}")
    for esid, et in ex_toks:
        j = jaccard(new_toks[s["sid"]], et)
        if j > max_j:
            max_j, max_pair = j, (s["sid"], esid)
        if j >= 0.8:
            prob(f"sid {s['sid']}: Jaccard {j:.2f} >= 0.80 against existing sid {esid}")

max_j_new = 0.0
max_pair_new = None
seen_new = {}
for s in sents:
    n = norm(s["slovak"])
    if n in seen_new:
        prob(f"sid {s['sid']}: Slovak sentence identical to new sid {seen_new[n]}")
    seen_new[n] = s["sid"]
for a in range(len(sents)):
    for b in range(a + 1, len(sents)):
        j = jaccard(new_toks[sents[a]["sid"]], new_toks[sents[b]["sid"]])
        if j > max_j_new:
            max_j_new, max_pair_new = j, (sents[a]["sid"], sents[b]["sid"])
        if j >= 0.8:
            prob(f"sid {sents[a]['sid']} vs new sid {sents[b]['sid']}: Jaccard {j:.2f} >= 0.80")

lv_counts = Counter(s["level"] for s in sents)
for lv in lv_counts:
    if lv not in LEVELS:
        prob(f"unknown level {lv!r}")
lv_target = {"A1": 12, "A2": 32, "B1": 50, "B2": 46}
lv_dev = {lv: lv_counts.get(lv, 0) - lv_target[lv] for lv in LEVELS}

tag_counts = Counter()
for s in sents:
    t = s.get("tags") or {}
    for k in ("nom_agent", "reported_speech", "perfective_future", "impersonal_or_passive"):
        if k not in t:
            prob(f"sid {s['sid']}: tags missing '{k}'")
        elif not isinstance(t[k], bool):
            prob(f"sid {s['sid']}: tags.{k} is not a bool")
        elif t[k]:
            tag_counts[k] += 1
    if "agent" not in t:
        prob(f"sid {s['sid']}: tags missing 'agent'")
    else:
        if t.get("nom_agent") and not t.get("agent"):
            prob(f"sid {s['sid']}: nom_agent true but agent is null")
        if not t.get("nom_agent") and t.get("agent"):
            prob(f"sid {s['sid']}: nom_agent false but agent is set")
    if not s.get("topic"):
        prob(f"sid {s['sid']}: empty topic")

# --------------------------------------------------------------- 5. cells
intent_counts = Counter(i["intent"] for i in items)
form_counts = Counter(i["form"] for i in items if i["intent"] == "V")
V = intent_counts["V"]
TF = intent_counts["TF"]
passive_share = (form_counts["passive"] / V * 100) if V else 0.0

if V < 195:
    prob(f"REQUIRED: V = {V} < 195")
if passive_share > 35.0:
    prob(f"REQUIRED: passive share of V = {passive_share:.1f} % > 35 %")
for f in V_FORMS:
    if form_counts[f] < 30:
        prob(f"REQUIRED: V form '{f}' = {form_counts[f]} < 30")
if TF < 165:
    prob(f"REQUIRED: TF = {TF} < 165")

# -------------------------------------------------------- 6. judge packets
os.makedirs(JUDGE, exist_ok=True)
rng = random.Random(20260919)
order = items[:]
rng.shuffle(order)
blind_map = {}
parts = []
for idx, it in enumerate(order):
    jid = "J%04d" % (idx + 1)
    blind_map[jid] = it["id"]
    s = by_sid.get(it["sid"], {})
    parts.append({"jid": jid, "slovak": s.get("slovak"), "level": s.get("level"),
                  "topic": s.get("topic"), "answer": it["answer"]})
if len(parts) != 1260:
    prob(f"{len(parts)} judge rows, expected 1260")
for p in range(6):
    chunk = parts[p * 210:(p + 1) * 210]
    if len(chunk) != 210:
        prob(f"judge part{p+1} has {len(chunk)} rows, expected 210")
    with open(os.path.join(JUDGE, f"in_part{p+1}.json"), "w", encoding="utf-8") as fh:
        json.dump(chunk, fh, ensure_ascii=False, indent=1)
with open(os.path.join(JUDGE, "blind_map.json"), "w", encoding="utf-8") as fh:
    json.dump(blind_map, fh, ensure_ascii=False, indent=1)

ctrl_idx = rng.sample(range(len(order)), 100)
controls, controls_map = [], {}
for n, oi in enumerate(sorted(ctrl_idx)):
    it = order[oi]
    kid = "K%03d" % (n + 1)
    controls_map[kid] = it["id"]
    s = by_sid.get(it["sid"], {})
    controls.append({"jid": kid, "slovak": s.get("slovak"), "level": s.get("level"),
                     "topic": s.get("topic"), "answer": it["answer"]})
rng.shuffle(controls)
with open(os.path.join(JUDGE, "in_controls.json"), "w", encoding="utf-8") as fh:
    json.dump(controls, fh, ensure_ascii=False, indent=1)
with open(os.path.join(JUDGE, "controls_map.json"), "w", encoding="utf-8") as fh:
    json.dump(controls_map, fh, ensure_ascii=False, indent=1)

# leak check: the judge packets must carry nothing but the five fields
allowed = {"jid", "slovak", "level", "topic", "answer"}
for row in parts + controls:
    if set(row) != allowed:
        prob(f"judge row {row.get('jid')} has fields {sorted(row)}")
        break
    if row["slovak"] is None or row["answer"] is None:
        prob(f"judge row {row['jid']} has a null slovak/answer")
        break

# --------------------------------------------------------------- 7. summary
lines = []
lines.append("# Phase 1m — new set: items, cells and checks\n")
lines.append(f"Built by `assemble_1m.py` (seed 20260919). Generated {datetime.now(timezone.utc).isoformat()}.\n")
lines.append("## Set\n")
lines.append("| quantity | value |")
lines.append("|---|---|")
lines.append(f"| sentences | {len(sents)} |")
lines.append(f"| sids | {min(by_sid) if by_sid else '-'}–{max(by_sid) if by_sid else '-'} |")
lines.append(f"| correct items | {n_correct} |")
lines.append(f"| wrong items | {n_wrong} |")
lines.append(f"| total items | {len(items)} |")
lines.append(f"| unique item ids | {len(ids)} |")
lines.append("")
lines.append("## Levels\n")
lines.append("| level | count | 1k-proportion target | delta |")
lines.append("|---|---|---|---|")
for lv in LEVELS:
    lines.append(f"| {lv} | {lv_counts.get(lv,0)} | {lv_target[lv]} | {lv_dev[lv]:+d} |")
lines.append("")
lines.append("## Sentence tags (true count of 140)\n")
lines.append("| tag | count |")
lines.append("|---|---|")
for k in ("nom_agent", "reported_speech", "perfective_future", "impersonal_or_passive"):
    lines.append(f"| {k} | {tag_counts[k]} |")
lines.append("")
lines.append("## Writer intent cells (wrong items)\n")
lines.append("| intent | count | floor | ok |")
lines.append("|---|---|---|---|")
lines.append(f"| V | {V} | 195 | {'yes' if V>=195 else 'NO'} |")
lines.append(f"| TF | {TF} | 165 | {'yes' if TF>=165 else 'NO'} |")
for k in ("T", "W", "M", "S"):
    lines.append(f"| {k} | {intent_counts[k]} | – | – |")
lines.append("")
lines.append("## V by form\n")
lines.append("| form | count | share of V | floor 30 |")
lines.append("|---|---|---|---|")
for f in V_FORMS:
    share = (form_counts[f] / V * 100) if V else 0.0
    lines.append(f"| {f} | {form_counts[f]} | {share:.1f} % | {'yes' if form_counts[f]>=30 else 'NO'} |")
lines.append("")
lines.append(f"Passive share of V = **{passive_share:.1f} %** (cap 35 %: "
             f"{'ok' if passive_share<=35 else 'EXCEEDED'}).\n")
lines.append("## Overlap with the existing 210\n")
lines.append(f"- identical Slovak sentences: {sum(1 for p in problems if 'identical to existing' in p)}")
lines.append(f"- max token-Jaccard new vs existing: {max_j:.2f} {max_pair} (threshold 0.80)")
lines.append(f"- max token-Jaccard new vs new: {max_j_new:.2f} {max_pair_new}\n")
lines.append("## Judge packets\n")
lines.append(f"- `judge/in_part1..6.json`: 6 x 210 = {len(parts)} rows, jids J0001–J%04d, fields jid/slovak/level/topic/answer only" % len(parts))
lines.append(f"- `judge/blind_map.json`: {len(blind_map)} jid -> item id")
lines.append(f"- `judge/in_controls.json`: {len(controls)} duplicate items, jids K001–K%03d" % len(controls))
lines.append(f"- `judge/controls_map.json`: {len(controls_map)} kid -> item id\n")
lines.append("## Problems\n")
if problems:
    for p in problems:
        lines.append(f"- {p}")
else:
    lines.append("- none")
lines.append("")
with open(os.path.join(DATA, "ITEMS_SUMMARY.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))

ok = not problems
out = {"ok": ok, "sentences": len(sents), "correct": n_correct, "wrong": n_wrong,
       "V": V, "V_forms": {f: form_counts[f] for f in V_FORMS}, "TF": TF,
       "others": {k: intent_counts[k] for k in ("T", "W", "M", "S")},
       "problems": problems}
print(json.dumps(out, ensure_ascii=False))
