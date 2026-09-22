"""Part 3 driver.  run_slice.py review_input <slice> | apply <slice> [--write] | status"""
import glob, json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "lib"))
import check3, writer
LANGS = check3.LANGS
INDEX = {x["slice"]: x for x in json.load(open(os.path.join(HERE, "slices/index.json")))}
STATE = os.path.join(HERE, "state.json")
ctx = json.load(open(os.path.join(ROOT, "snapshot/media_ctx.json")))


def state():
    return json.load(open(STATE)) if os.path.exists(STATE) else {}


def set_state(sl, **kw):
    s = state(); s.setdefault(sl, {}).update(kw)
    json.dump(s, open(STATE, "w"), indent=1, sort_keys=True)


def out_files(sl):
    return sorted(glob.glob(os.path.join(HERE, "out", f"{sl}_*.txt")), key=lambda p: int(re.search(r"_(\d+)\.txt$", p).group(1)))


def review_input(sl):
    ids = INDEX[sl]["ids"]
    blocks, probs = check3.parse_blocks(out_files(sl))
    res = check3.check_slice(ids, blocks)
    d = check3.data(); by, ex, S = d["by"], d["ex"], d["S"]
    lines, last_m = [], None
    for eid in ids:
        m = ctx["e2m"][str(eid)]
        if m != last_m:
            lines.append(f"MEDIA {m} | meaning: {ctx['media'][str(m)].get('meaning','')}"); last_m = m
        en = by[(eid, "en")]; info = ctx["e2info"][str(eid)]
        lines.append(f"E {eid} | {ex[eid]['type_level']} type {ex[eid]['exercise_type_id']} {ex[eid]['type_title']} | style {info['style']} | options {2 if not (en['distractor_2'] or '').strip() else 3}{' | SEL' if eid in S else ''}")
        lines.append("en|" + "|".join((en[k] or "") for k in ("intro_text", "correct_answer", "distractor_1", "distractor_2")))
        for L in LANGS:
            r = res[(eid, L)]
            lines.append(f"{L}|" + ("|".join(r["cells"]) if r["cells"] else "<MISSING>"))
            for h in r["hard"]:
                lines.append(f"  !HARD: {h}")
            for s_ in r["soft"]:
                if not s_.startswith("SEL: no subject pronoun"):     # noise: most are noun subjects; the reviewer checks SEL anyway
                    lines.append(f"  ~soft: {s_}")
    open(os.path.join(HERE, "review", f"{sl}_in.txt"), "w").write("\n".join(lines) + "\n")
    hard = sum(1 for r in res.values() if r["hard"]); soft = sum(1 for r in res.values() if r["soft"])
    set_state(sl, translated=len(blocks), format_problems=probs, hard_before_review=hard, soft_before_review=soft)
    print(sl, "blocks", len(blocks), "of", len(ids), "hard", hard, "soft", soft, "format", probs[:5])


def apply(sl, write):
    ids = INDEX[sl]["ids"]
    blocks, probs = check3.parse_blocks(out_files(sl))
    rv = os.path.join(HERE, "review", f"{sl}_out.txt")
    corr, emptied, rprobs = {}, {}, []
    for n, line in enumerate(open(rv, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.strip() == "NONE":
            continue
        p = line.split("|")
        try:
            eid, L = int(p[0]), p[1]
        except Exception:
            rprobs.append(f"{n}: {line[:80]}"); continue
        if eid not in ids or L not in LANGS:
            rprobs.append(f"{n}: not in slice: {line[:80]}"); continue
        if len(p) >= 3 and p[2] == "EMPTY":
            emptied[(eid, L)] = "|".join(p[3:]); continue
        if len(p) != 7:
            rprobs.append(f"{n}: {len(p)} fields: {line[:80]}"); continue
        corr[(eid, L)] = ([x.strip() for x in p[2:6]], p[6])
    for (eid, L), (cells, why) in corr.items():
        blocks.setdefault(eid, {})[L] = cells
    res = check3.check_slice(ids, blocks)
    d = check3.data(); by = d["by"]
    changes, left_empty = [], []
    COLS = ["intro_text", "correct_answer", "distractor_1", "distractor_2", "full_sentence"]
    for eid in ids:
        for L in LANGS:
            r = res[(eid, L)]
            if (eid, L) in emptied:
                left_empty.append((eid, L, "reviewer: " + emptied[(eid, L)])); continue
            if r["hard"]:
                left_empty.append((eid, L, "machine: " + "; ".join(r["hard"]))); continue
            row = by[(eid, L)]
            intro, ca, d1, d2 = r["cells"]
            old = {k: row[k] for k in COLS}
            if any((old[k] or "").strip() for k in COLS):
                left_empty.append((eid, L, "target fields not empty in the snapshot")); continue
            new = {"intro_text": intro, "correct_answer": ca, "distractor_1": d1 or None,
                   "distractor_2": d2 or None, "full_sentence": r["full"]}
            changes.append({"id": row["id"], "exercise_id": eid, "lang": L, "new": new, "old": old})
    json.dump({"changes": changes, "left_empty": left_empty, "corrections": {f"{k[0]}|{k[1]}": v for k, v in corr.items()},
               "review_format_problems": rprobs, "soft": {f"{k[0]}|{k[1]}": v["soft"] for k, v in res.items() if v["soft"]}},
              open(os.path.join(HERE, "final", f"{sl}.json"), "w"), ensure_ascii=False, indent=0)
    out = {"slice": sl, "cells": len(ids) * 6, "to_write": len(changes), "left_empty": len(left_empty),
           "reviewer_corrected": len(corr), "reviewer_emptied": len(emptied), "review_format_problems": len(rprobs)}
    if write:
        w = writer.run("part3", sl, changes, COLS)
        out.update({"written": w["written"], "already": w["already"], "skipped": len(w["skipped"]), "verify_bad": len(w["verify_bad"])})
        set_state(sl, done=True, **{k: v for k, v in out.items() if k != "slice"})
    print(json.dumps(out))


def status():
    s = state()
    for k in sorted(INDEX):
        print(k, INDEX[k]["levels"], len(INDEX[k]["ids"]), "SEL" if INDEX[k]["selected"] else "", s.get(k, {}))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "review_input":
        review_input(sys.argv[2])
    elif cmd == "apply":
        apply(sys.argv[2], "--write" in sys.argv)
    else:
        status()
