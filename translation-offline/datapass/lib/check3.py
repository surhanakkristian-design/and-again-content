"""Machine checks for Part 3 translations (and the parser of the translator / reviewer files)."""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.expanduser("~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/scripts"))
from validate_part import derive_full_sentence

LANGS = ["de", "ua", "es", "fr", "tr", "hu"]
CYR = re.compile(r"[Ѐ-ӿ]")
RUS_ONLY = re.compile(r"[ыэъёЫЭЪЁ]")
LAT = re.compile(r"[A-Za-zÀ-ɏ]")
EN_WORDS = set("the an is are was were have has had will would and of to with you he she it they we this that my your his her their what where when why there here been being do does did not".split())
PRON = {"es": "yo tú él ella usted nosotros nosotras vosotros vosotras ellos ellas ustedes".split(),
        "ua": "я ти він вона воно ми ви вони".split(),
        "tr": "ben sen o biz siz onlar".split(),
        "hu": "én te ő mi ti ők ön önök".split()}
_DATA = {}


def data():
    if not _DATA:
        rows = [json.loads(l) for l in open(os.path.join(ROOT, "snapshot/loc_rows.jsonl"))]
        _DATA["by"] = {(r["exercise_id"], r["language_code"]): r for r in rows}
        _DATA["ex"] = {e["id"]: e for e in map(json.loads, open(os.path.join(ROOT, "snapshot/exercises.jsonl")))}
        s = json.load(open(os.path.join(ROOT, "snapshot/sets.json")))
        _DATA["S"] = {r["exercise_id"] for r in s["selected"]}
    return _DATA


def parse_blocks(paths):
    """E-block files -> {eid: {lang: [intro, ca, d1, d2]}}, plus format problems."""
    out, probs = {}, []
    cur = None
    for p in paths:
        for n, line in enumerate(open(p, encoding="utf-8"), 1):
            line = line.rstrip("\n").rstrip("\r")
            if not line.strip():
                continue
            m = re.match(r"^E (\d+)\s*$", line)
            if m:
                cur = int(m.group(1)); out.setdefault(cur, {}); continue
            parts = line.split("|")
            if cur is None or parts[0] not in LANGS:
                probs.append(f"{os.path.basename(p)}:{n} unparsable: {line[:80]}"); continue
            if len(parts) != 5:
                probs.append(f"{os.path.basename(p)}:{n} E {cur} {parts[0]} has {len(parts)} fields"); continue
            if parts[0] in out[cur]:
                probs.append(f"E {cur} {parts[0]} given twice")
            out[cur][parts[0]] = [x.strip() for x in parts[1:]]
    return out, probs


def check_cell(eid, L, cells, allrows=None):
    """Hard failures (cell not writable) and soft warnings for one exercise x language."""
    d = data(); by, ex = d["by"], d["ex"]
    en = by[(eid, "en")]
    intro, ca, d1, d2 = cells
    hard, soft = [], []
    txt = " ".join(x for x in cells if x)
    if not intro:
        hard.append("empty intro_text")
    if intro.count("...") != 1 or "...." in intro:
        hard.append("gap marker count != 1")
    if not (en["distractor_2"] or "").strip() and d2:
        hard.append("distractor_2 must be empty (options 2)")
    if L == "ua":
        if not CYR.search(intro):
            hard.append("ua without Cyrillic")
        if RUS_ONLY.search(txt):
            hard.append("Russian-only letters in ua")
        lat = re.findall(r"[A-Za-z]{3,}", txt)
        if len(lat) > 1:
            soft.append("Latin words in ua: " + " ".join(lat[:4]))
    elif CYR.search(txt):
        hard.append("Cyrillic in a Latin-script language")
    words = re.findall(r"[a-zA-Z']+", intro.lower())
    if words and L != "ua":
        enr = sum(1 for w in words if w in EN_WORDS) / len(words)
        if enr > 0.3:
            hard.append(f"looks English ({enr:.0%} English function words)")
    if intro.strip() == (en["intro_text"] or "").strip():
        hard.append("identical to the English intro")
    full = derive_full_sentence(intro, ca, L, ex[eid]["exercise_type_id"]) if intro else None
    if intro and full is None:
        hard.append("full_sentence not derivable")
    if full:
        if not re.search(r"[.!?…»“”\"]\s*$", full):
            hard.append("no final punctuation")
        r = len(full) / max(1, len(en["full_sentence"] or ""))
        if r < 0.45 or r > 2.3:
            hard.append(f"length ratio {r:.2f}")
        elif r < 0.6 or r > 1.9:
            soft.append(f"length ratio {r:.2f}")
    if L in ("tr", "hu") and intro and len(intro) > 45 and not re.search(r"[^\x00-\x7f]", intro):
        soft.append("no diacritics at all")
    if L == "es" and ("¿" in intro) and intro.count("¿") != intro.count("?") and not intro.rstrip().endswith("...?"):
        soft.append("unbalanced ¿?")
    if eid in d["S"] and L in PRON:
        toks = set(re.findall(r"\w+", intro.lower()))
        if not toks & set(PRON[L]):
            soft.append("SEL: no subject pronoun in intro")
        for opt in (ca, d1, d2):
            ot = re.findall(r"\w+", (opt or "").lower())
            if ot and ot[0] in PRON[L] and L != "tr":
                soft.append("SEL: pronoun inside an option")
                break
    return hard, soft, full


def check_slice(ids, blocks):
    """-> {(eid, L): {"cells", "hard", "soft", "full"}} for every id x lang (missing = hard)."""
    res = {}
    for eid in ids:
        b = blocks.get(eid, {})
        seen = set()
        for L in LANGS:
            if L not in b:
                res[(eid, L)] = {"cells": None, "hard": ["missing"], "soft": [], "full": None}; continue
            h, s, f = check_cell(eid, L, b[L])
            key = "|".join(b[L])
            if key in seen and any(b[L]):
                s.append("byte-identical to another language row")
            seen.add(key)
            res[(eid, L)] = {"cells": b[L], "hard": h, "soft": s, "full": f}
    return res
