#!/usr/bin/env python3
"""Phase 1N — label 'assembler'.

Adapted from phase1m/assemble_1m.py. Builds and validates the new 100-sentence set:
  data/annotations.json, data/items.json, data/ITEMS_SUMMARY.md,
  judge/in_part1..5.json, judge/in_controls.json, judge/blind_map.json,
  judge/controls_map.json

--topup: read data/topup_answers.json, APPEND the new items (nothing is removed),
write ONLY the new rows to judge/in_part9.json with fresh jids continuing the J
sequence, extend judge/blind_map.json, refresh data/ITEMS_SUMMARY.md.

No model calls, no DB, deterministic. Never edits answers/sentences/annotations —
problems are only reported; nothing is invented or repaired.
"""
import json, os, re, sys, zlib, random, unicodedata
from datetime import datetime, timezone
from collections import Counter, defaultdict

P1N = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(P1N, "data")
JUDGE = os.path.join(P1N, "judge")
LOG = os.path.join(P1N, "access_log.jsonl")
CALLER = "assemble_1n.py"
SEED = 20260919
PURPOSE = "Phase 1N assemble: build the new 100-sentence item set + judge packets"

REQ_TOP = ["hygienised", "raw", "tf_gold", "voice_sk", "agent_nom",
           "perfective_present", "tense_open"]
REQ_INNER = ["id", "t", "lv", "v", "lk", "alt"]
LEVELS = ["A1", "A2", "B1", "B2"]
INTENTS = ["C", "TF", "T", "W", "M", "S"]
WRONG_INTENTS = ["TF", "T", "W", "M", "S"]
INTENT_TARGET = {"TF": 175, "T": 25, "W": 100, "M": 100, "S": 100}
PASSIVE_VALS = [None, "by", "agentless"]
ALL_SIDS = list(range(160001, 160101))
N_CORRECT_T, N_WRONG_T, N_ITEMS_T = 400, 500, 900
N_PARTS, PART_SIZE, N_CONTROLS = 5, 180, 80

TOPUP = "--topup" in sys.argv[1:]
problems = []


def prob(msg):
    problems.append(msg)


def log(side, what, n, purpose=PURPOSE):
    rec = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "side": side, "what": what, "caller": CALLER, "n": n, "purpose": purpose}
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def load(path, side, what, purpose=PURPOSE):
    with open(path, encoding="utf-8") as fh:
        obj = json.load(fh)
    log(side, what, len(obj), purpose)
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
sents = load(os.path.join(DATA, "sentences.json"), "new_1n", "data/sentences.json")
answers = []
for i in (1, 2, 3, 4):
    answers += load(os.path.join(DATA, f"answers_part{i}.json"), "new_1n",
                    f"data/answers_part{i}.json")
ann_parts = [load(os.path.join(DATA, f"annotations_part{i}.json"), "new_1n",
                  f"data/annotations_part{i}.json") for i in (1, 2)]
existing = load(os.path.join(P1N, "existing_350.json"), "existing", "existing_350.json",
                "contamination check of the new Slovak sentences")

by_sid = {s["sid"]: s for s in sents}
if len(sents) != len(ALL_SIDS):
    prob(f"sentences.json has {len(sents)} sentences, expected {len(ALL_SIDS)}")
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
    a = merged.get(str(sid))
    if a is None:
        prob(f"sid {sid}: annotation missing")
        continue
    for k in REQ_TOP:
        if k not in a:
            prob(f"sid {sid}: annotation missing top-level key '{k}'")
    if sid in by_sid and a.get("tf_gold") != by_sid[sid].get("tf_gold"):
        prob(f"sid {sid}: annotation.tf_gold={a.get('tf_gold')!r} != sentence "
             f"tf_gold={by_sid[sid].get('tf_gold')!r}")
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
n_dropped = 0
seen_norm = defaultdict(dict)   # sid -> normalised answer -> text
seen_ids = {}
per_sid = defaultdict(lambda: Counter())


def add_item(sid, kind, intent, passive, text, tag=""):
    """Append one item; drop (and report) duplicates. Returns the item or None."""
    global n_dropped
    if not isinstance(text, str) or not text.strip():
        prob(f"sid {sid}: empty {kind} answer{tag}")
        return None
    key = norm(text)
    if key in seen_norm[sid]:
        prob(f"sid {sid}: DROPPED duplicate answer text '{text}' "
             f"(same as '{seen_norm[sid][key]}')")
        n_dropped += 1
        return None
    seen_norm[sid][key] = text
    iid = f"{kind}:{sid}:{crc(text)}"
    if iid in seen_ids:
        prob(f"DROPPED duplicate item id {iid}")
        n_dropped += 1
        return None
    seen_ids[iid] = True
    per_sid[sid][kind] += 1
    per_sid[sid][intent] += 1
    return {"id": iid, "sid": sid, "kind": kind, "intent": intent,
            "form": None, "passive": passive, "answer": text}


def rows_to_items(sid, cor, wro, tag=""):
    out = []
    for c in cor:
        if not isinstance(c, dict):
            prob(f"sid {sid}: correct row is not an object{tag}")
            continue
        passive = c.get("passive")
        if passive not in PASSIVE_VALS:
            prob(f"sid {sid}: correct row has bad passive {passive!r}{tag}")
            passive = None
        it = add_item(sid, "C", "C", passive, c.get("answer"), tag)
        if it:
            out.append(it)
    for w in wro:
        if not isinstance(w, dict):
            prob(f"sid {sid}: wrong row is not an object{tag}")
            continue
        intent = w.get("intent")
        if intent not in WRONG_INTENTS:
            prob(f"sid {sid}: wrong answer has bad intent {intent!r}{tag}")
        if w.get("form") is not None:
            prob(f"sid {sid}: wrong answer has non-null form {w.get('form')!r}{tag}")
        it = add_item(sid, "W", intent, None, w.get("answer"), tag)
        if it:
            out.append(it)
    return out


items = []
for sid in ALL_SIDS:
    rec = ans_by_sid.get(sid)
    if rec is None:
        continue
    cor, wro = rec.get("correct", []), rec.get("wrong", [])
    if len(cor) != 4:
        prob(f"QUOTA sid {sid}: {len(cor)} correct rows, expected 4")
    if len(wro) != 5:
        prob(f"QUOTA sid {sid}: {len(wro)} wrong rows, expected 5")
    items += rows_to_items(sid, cor, wro)

n_base_items = len(items)

# --------------------------------------------------------------- 3b. topup
topup_items = []
if TOPUP:
    tpath = os.path.join(DATA, "topup_answers.json")
    if not os.path.exists(tpath):
        print(json.dumps({"status": "blocked", "error": "data/topup_answers.json missing"}))
        sys.exit(2)
    topup = load(tpath, "new_1n", "data/topup_answers.json",
                 "Phase 1N assemble --topup: append extra items")
    for rec in topup:
        sid = rec.get("sid")
        if sid not in by_sid:
            prob(f"topup: unknown sid {sid}")
        topup_items += rows_to_items(sid, rec.get("correct", []) or [],
                                     rec.get("wrong", []) or [], " [topup]")
    items += topup_items

# --------------------------------------------------- 4. composition + cells
intent_counts = Counter(i["intent"] for i in items)
kind_counts = Counter(i["kind"] for i in items)
passive_counts = Counter(str(i["passive"]) for i in items if i["kind"] == "C")
n_correct, n_wrong = kind_counts["C"], kind_counts["W"]
item_lv = Counter(by_sid[i["sid"]]["level"] for i in items if i["sid"] in by_sid)
lv_counts = Counter(s["level"] for s in sents)
for lv in lv_counts:
    if lv not in LEVELS:
        prob(f"unknown level {lv!r}")

if not TOPUP:
    if n_correct != N_CORRECT_T:
        prob(f"{n_correct} correct items, expected {N_CORRECT_T}")
    if n_wrong != N_WRONG_T:
        prob(f"{n_wrong} wrong items, expected {N_WRONG_T}")
    if len(items) != N_ITEMS_T:
        prob(f"{len(items)} items, expected {N_ITEMS_T}")
    for k, t in INTENT_TARGET.items():
        if intent_counts[k] != t:
            prob(f"intent {k} = {intent_counts[k]}, expected {t}")

# passive rules
passivizable = {s["sid"] for s in sents if (s.get("tags") or {}).get("passivizable")}
exp_agentless = sorted(s for s in passivizable if s % 4 == 0)
by_by_sid = defaultdict(int)
ag_by_sid = defaultdict(int)
for it in items:
    if it["kind"] != "C" or it["passive"] is None:
        continue
    if it["sid"] not in passivizable:
        prob(f"sid {it['sid']}: passive '{it['passive']}' on a non-passivizable sentence")
    if it["passive"] == "by":
        by_by_sid[it["sid"]] += 1
    else:
        ag_by_sid[it["sid"]] += 1
for sid in sorted(passivizable):
    if by_by_sid[sid] != 1:
        prob(f"QUOTA sid {sid}: {by_by_sid[sid]} 'by' passives, expected 1")
for sid in sorted(passivizable):
    want = 1 if sid % 4 == 0 else 0
    if ag_by_sid[sid] != want:
        prob(f"QUOTA sid {sid}: {ag_by_sid[sid]} 'agentless' passives, expected {want}")
for sid, n in sorted(ag_by_sid.items()):
    if sid not in passivizable and n:
        prob(f"QUOTA sid {sid}: agentless passive on a non-passivizable sentence")
n_passive_by = passive_counts["by"]
n_passive_ag = passive_counts["agentless"]

# sentence-tag hygiene
tag_counts = Counter()
TAGS = ("nom_agent", "reported_speech", "perfective_future", "impersonal_or_passive",
        "passivizable")
for s in sents:
    t = s.get("tags") or {}
    for k in TAGS:
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
    if not s.get("tf_gold"):
        prob(f"sid {s['sid']}: empty tf_gold")

# ------------------------------------------- 5. contamination vs existing_350
new_toks = {s["sid"]: toks(s["slovak"]) for s in sents}
ex_norm = {}
for n, e in enumerate(existing):
    ex_norm.setdefault(norm(e["slovak"]), n)
ex_toks = [(n, toks(e["slovak"])) for n, e in enumerate(existing)]
max_j, max_pair, n_identical, n_j80 = 0.0, None, 0, 0
for s in sents:
    nn = norm(s["slovak"])
    if nn in ex_norm:
        n_identical += 1
        prob(f"CONTAMINATION sid {s['sid']}: Slovak identical to existing_350 row {ex_norm[nn]}")
    for en, et in ex_toks:
        j = jaccard(new_toks[s["sid"]], et)
        if j > max_j:
            max_j, max_pair = j, (s["sid"], en)
        if j >= 0.8:
            n_j80 += 1
            prob(f"CONTAMINATION sid {s['sid']}: Jaccard {j:.2f} >= 0.80 vs existing_350 row {en}")

max_j_new, max_pair_new, seen_new = 0.0, None, {}
for s in sents:
    nn = norm(s["slovak"])
    if nn in seen_new:
        prob(f"sid {s['sid']}: Slovak identical to new sid {seen_new[nn]}")
    seen_new[nn] = s["sid"]
for a in range(len(sents)):
    for b in range(a + 1, len(sents)):
        j = jaccard(new_toks[sents[a]["sid"]], new_toks[sents[b]["sid"]])
        if j > max_j_new:
            max_j_new, max_pair_new = j, (sents[a]["sid"], sents[b]["sid"])
        if j >= 0.8:
            prob(f"sid {sents[a]['sid']} vs new sid {sents[b]['sid']}: Jaccard {j:.2f} >= 0.80")

with open(os.path.join(DATA, "items.json"), "w", encoding="utf-8") as fh:
    json.dump(items, fh, ensure_ascii=False, indent=1)

# -------------------------------------------------------- 6. judge packets
os.makedirs(JUDGE, exist_ok=True)
ALLOWED = {"jid", "slovak", "level", "answer"}


def judge_row(jid, it):
    s = by_sid.get(it["sid"], {})
    return {"jid": jid, "slovak": s.get("slovak"), "level": s.get("level"),
            "answer": it["answer"]}


bm_path = os.path.join(JUDGE, "blind_map.json")
if TOPUP:
    with open(bm_path, encoding="utf-8") as fh:
        blind_map = json.load(fh)
    log("1n:judge", "judge/blind_map.json", len(blind_map),
        "Phase 1N assemble --topup: continue the J sequence")
    start = max((int(k[1:]) for k in blind_map if k.startswith("J")), default=0)
    known = set(blind_map.values())
    new_rows = []
    for idx, it in enumerate(topup_items):
        if it["id"] in known:
            prob(f"topup item {it['id']} already in blind_map — skipped")
            continue
        jid = "J%04d" % (start + len(new_rows) + 1)
        blind_map[jid] = it["id"]
        new_rows.append(judge_row(jid, it))
    with open(os.path.join(JUDGE, "in_part9.json"), "w", encoding="utf-8") as fh:
        json.dump(new_rows, fh, ensure_ascii=False, indent=1)
    with open(bm_path, "w", encoding="utf-8") as fh:
        json.dump(blind_map, fh, ensure_ascii=False, indent=1)
    parts, controls, controls_map = new_rows, [], {}
    judge_note = (f"`judge/in_part9.json`: {len(new_rows)} new rows, jids "
                  f"J%04d–J%04d; `judge/blind_map.json` extended to {len(blind_map)}"
                  % (start + 1, start + len(new_rows))) if new_rows else \
        "`judge/in_part9.json`: 0 new rows"
else:
    rng = random.Random(SEED)
    order = items[:]
    rng.shuffle(order)
    blind_map, parts = {}, []
    for idx, it in enumerate(order):
        jid = "J%04d" % (idx + 1)
        blind_map[jid] = it["id"]
        parts.append(judge_row(jid, it))
    if len(parts) != N_PARTS * PART_SIZE:
        prob(f"{len(parts)} judge rows, expected {N_PARTS * PART_SIZE}")
    share = len(parts) // N_PARTS
    for p in range(N_PARTS):
        chunk = parts[p * share:(p + 1) * share] if p < N_PARTS - 1 else parts[p * share:]
        if len(chunk) != PART_SIZE:
            prob(f"judge part{p+1} has {len(chunk)} rows, expected {PART_SIZE}")
        with open(os.path.join(JUDGE, f"in_part{p+1}.json"), "w", encoding="utf-8") as fh:
            json.dump(chunk, fh, ensure_ascii=False, indent=1)
    with open(bm_path, "w", encoding="utf-8") as fh:
        json.dump(blind_map, fh, ensure_ascii=False, indent=1)

    ctrl_idx = rng.sample(range(len(order)), N_CONTROLS)
    controls, controls_map = [], {}
    for n, oi in enumerate(sorted(ctrl_idx)):
        it = order[oi]
        kid = "K%03d" % (n + 1)
        controls_map[kid] = it["id"]
        controls.append(judge_row(kid, it))
    rng.shuffle(controls)
    with open(os.path.join(JUDGE, "in_controls.json"), "w", encoding="utf-8") as fh:
        json.dump(controls, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(JUDGE, "controls_map.json"), "w", encoding="utf-8") as fh:
        json.dump(controls_map, fh, ensure_ascii=False, indent=1)
    judge_note = (f"`judge/in_part1..{N_PARTS}.json`: {N_PARTS} x {share} = {len(parts)} rows, "
                  f"jids J0001–J%04d" % len(parts))

for row in parts + controls:
    if set(row) != ALLOWED:
        prob(f"judge row {row.get('jid')} has fields {sorted(row)}")
        break
    if row["slovak"] is None or row["answer"] is None:
        prob(f"judge row {row['jid']} has a null slovak/answer")
        break

# --------------------------------------------------------------- 7. summary
quota_probs = [p for p in problems if p.startswith("QUOTA")]
cont_probs = [p for p in problems if p.startswith("CONTAMINATION")]
L = []
L.append("# Phase 1N — new set: items, cells and checks\n")
L.append(f"Built by `assemble_1n.py` (seed {SEED}{', --topup' if TOPUP else ''}). "
         f"Generated {datetime.now(timezone.utc).isoformat()}.\n")
L.append("## Set\n")
L.append("| quantity | value |")
L.append("|---|---|")
L.append(f"| sentences | {len(sents)} |")
L.append(f"| sids | {min(by_sid) if by_sid else '-'}–{max(by_sid) if by_sid else '-'} |")
L.append(f"| correct items | {n_correct} (target {N_CORRECT_T}) |")
L.append(f"| wrong items | {n_wrong} (target {N_WRONG_T}) |")
L.append(f"| total items | {len(items)} (target {N_ITEMS_T}) |")
L.append(f"| base items / topup items | {n_base_items} / {len(topup_items)} |")
L.append(f"| duplicates dropped | {n_dropped} |")
L.append("")
L.append("## Levels (counted from the data)\n")
L.append("| level | sentences | items |")
L.append("|---|---|---|")
for lv in LEVELS:
    L.append(f"| {lv} | {lv_counts.get(lv, 0)} | {item_lv.get(lv, 0)} |")
L.append(f"| **total** | **{sum(lv_counts.values())}** | **{sum(item_lv.values())}** |")
L.append("")
L.append("## Sentence tags (true count of %d)\n" % len(sents))
L.append("| tag | count |")
L.append("|---|---|")
for k in TAGS:
    L.append(f"| {k} | {tag_counts[k]} |")
L.append("")
L.append("## Writer intent cells\n")
L.append("| intent | count | expected | ok |")
L.append("|---|---|---|---|")
L.append(f"| C (correct) | {intent_counts['C']} | {N_CORRECT_T} | "
         f"{'yes' if intent_counts['C'] == N_CORRECT_T else 'NO'} |")
for k in WRONG_INTENTS:
    t = INTENT_TARGET[k]
    L.append(f"| {k} | {intent_counts[k]} | {t} | {'yes' if intent_counts[k] == t else 'NO'} |")
L.append(f"| **wrong total** | **{n_wrong}** | **{N_WRONG_T}** | "
         f"{'yes' if n_wrong == N_WRONG_T else 'NO'} |")
L.append("")
L.append("## Passive sub-cases (correct items)\n")
L.append("| sub-case | count | expected | ok |")
L.append("|---|---|---|---|")
L.append(f"| passive `by` | {n_passive_by} | {len(passivizable)} (one per passivizable sentence) | "
         f"{'yes' if n_passive_by == len(passivizable) else 'NO'} |")
L.append(f"| passive `agentless` | {n_passive_ag} | {len(exp_agentless)} (passivizable and sid % 4 == 0) | "
         f"{'yes' if n_passive_ag == len(exp_agentless) else 'NO'} |")
L.append(f"| no passive (null) | {passive_counts['None']} | – | – |")
L.append("")
L.append(f"Passivizable sentences: {len(passivizable)} of {len(sents)}; "
         f"of these {len(exp_agentless)} have sid % 4 == 0. "
         f"Passives on non-passivizable sentences: "
         f"{sum(1 for p in problems if 'non-passivizable' in p)}.\n")
L.append("## Quota violations by sid\n")
if quota_probs:
    for p in quota_probs:
        L.append(f"- {p[6:].strip()}")
else:
    L.append("- none (every sid: 4 correct rows, 5 wrong rows, 1 `by` where passivizable, "
             "1 `agentless` where passivizable and sid % 4 == 0)")
L.append("")
L.append("## Contamination check vs `existing_350.json`\n")
L.append(f"- existing rows compared: {len(existing)}")
L.append(f"- identical Slovak sentences: {n_identical}")
L.append(f"- pairs with token-Jaccard >= 0.80: {n_j80}")
L.append(f"- max token-Jaccard new vs existing: {max_j:.2f} {max_pair} (new sid, existing row index)")
L.append(f"- max token-Jaccard new vs new: {max_j_new:.2f} {max_pair_new}\n")
L.append("## Judge packets\n")
L.append(f"- {judge_note}; rows carry only jid/slovak/level/answer")
L.append(f"- `judge/blind_map.json`: {len(blind_map)} jid -> item id")
if not TOPUP:
    L.append(f"- `judge/in_controls.json`: {len(controls)} duplicated items, "
             "jids K001–K%03d" % len(controls))
    L.append(f"- `judge/controls_map.json`: {len(controls_map)} kid -> item id")
L.append("")
L.append("## Problems\n")
if problems:
    for p in problems:
        L.append(f"- {p}")
else:
    L.append("- none")
L.append("")
with open(os.path.join(DATA, "ITEMS_SUMMARY.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(L))

out = {"status": "done",
       "n_items": len(items), "n_correct": n_correct, "n_wrong": n_wrong,
       "n_tf": intent_counts["TF"], "n_passive_by": n_passive_by,
       "n_passive_agentless": n_passive_ag, "n_dropped": n_dropped,
       "n_topup": len(topup_items), "max_jaccard_existing": round(max_j, 3),
       "problems": problems}
print(json.dumps(out, ensure_ascii=False))
