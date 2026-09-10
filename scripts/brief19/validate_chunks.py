import re
#!/usr/bin/env python3
"""Brief 19 validator. usage: validate_chunks.py rows.json out_1.json [out_2.json ...] --report accepted.json --rejects rejects.json
Every rule from the brief is checked mechanically; a row is accepted only if all pass.
Rows are never repaired."""
import json, re, sys, math, statistics, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from determiners import determiner_faults, exemptions as _exemptions
MIN_PIECES_3_UP_TO_WORDS = 8  # Brief 20 Part 6: up to 8 words, three pieces is a legitimate split
# Brief 20 Part 8: for a 9-word sentence three pieces may stand, and a whole-phrase piece may exceed the half cap,
# ONLY when every piece is uncuttable (see determiners.exemptions); each such case is named and counted.

def word_count(s):
    """Words = whitespace tokens holding at least one letter or digit; a French " ?", " !" or a spaced dash is not a word."""
    return sum(1 for t in s.split() if re.search(r"[^\W_]", t))

def largest_share(fs, ch):
    return max(word_count(p) for p in ch) / max(1, word_count(fs))

def check(row, out, lang=None):
    return check2(row, out, lang)[0]

def check2(row, out, lang=None):
    """-> (reasons, exemptions). reasons empty = accepted; exemptions = the Part 8 proxies this split exceeds."""
    fs, ans = row["full_sentence"], row["correct_answer"]
    lang = lang or row.get("language_code")
    ch = out.get("chunks"); alts = out.get("alternatives", [])
    reasons = []
    if not isinstance(ch, list) or not all(isinstance(p, str) for p in ch):
        return ["chunks_not_list"], []
    ex = _exemptions(fs, ch, lang, ans) if lang else []
    if " ".join(ch) != fs: reasons.append("join_mismatch")
    floor = 3 if word_count(fs) <= MIN_PIECES_3_UP_TO_WORDS else 4
    if "floor_min_pieces" in ex and len(ch) == 3: floor = 3
    if not (floor <= len(ch) <= 7): reasons.append(f"piece_count_{len(ch)}")
    reasons += determiner_faults(ch, lang) if lang else []
    if any(p != p.strip() or p == "" for p in ch): reasons.append("piece_whitespace")
    # answer inside one piece (as a whole-token sequence)
    # Brief 20 Part 3: a two-blank answer "a ... b" has two parts; each part must sit whole in ONE piece
    # (they normally sit in different pieces: that is the verb bracket the exercise teaches).
    for part in [x.strip() for x in ans.split("...")]:
        if not part: continue
        pat = r"(?<!\w)" + re.escape(part) + r"(?!\w)"
        if not any(re.search(pat, p) for p in ch): reasons.append("answer_split"); break
    if len(set(ch)) < len(ch): reasons.append("duplicate_pieces")  # byte-identical only (Kristian, 2026-09-07)
    n = word_count(fs); mx = max(word_count(p) for p in ch)
    if mx > math.ceil(n / 2) and "cap_whole_phrase" not in ex and "cap_whole_phrase_long" not in ex: reasons.append(f"dominant_piece_{mx}of{n}")
    if not isinstance(alts, list): reasons.append("alts_not_list"); alts = []
    if len(alts) > 2: reasons.append(f"alts_{len(alts)}")
    seen = set()
    for a in alts:
        if not isinstance(a, list) or sorted(a) != sorted(ch): reasons.append("alt_not_permutation"); continue
        if a == ch: reasons.append("alt_equals_chunks")
        t = tuple(a)
        if t in seen: reasons.append("alt_duplicate")
        seen.add(t)
    return reasons, (ex if not reasons else [])

def main():
    args = sys.argv[1:]
    rep = args[args.index("--report")+1]; rej = args[args.index("--rejects")+1]
    files = [a for i,a in enumerate(args) if not a.startswith("--") and (i==0 or not args[i-1].startswith("--"))]
    rows = {r["id"]: r for r in json.load(open(files[0]))}
    outs = {}
    for f in files[1:]:
        for o in json.load(open(f)): outs[o["id"]] = o
    accepted, rejects = [], []
    for rid, row in rows.items():
        o = outs.get(rid)
        if o is None: rejects.append({"id": rid, "reasons": ["missing_output"], "full_sentence": row["full_sentence"]}); continue
        rs = check(row, o)
        if rs: rejects.append({"id": rid, "reasons": rs, "full_sentence": row["full_sentence"], "chunks": o.get("chunks"), "alternatives": o.get("alternatives")})
        else: accepted.append({**row, "chunks": o["chunks"], "alternatives": o.get("alternatives", [])})
    json.dump(accepted, open(rep, "w"), ensure_ascii=False, indent=1)
    json.dump(rejects, open(rej, "w"), ensure_ascii=False, indent=1)
    n = len(rows)
    print(f"rows {n}  accepted {len(accepted)}  rejected {len(rejects)}  ({100*len(rejects)/n:.1f}%)")
    print("reject reasons:", Counter(r for x in rejects for r in x["reasons"]))
    if accepted:
        pcs = [len(a["chunks"]) for a in accepted]
        print(f"pieces/sentence median {statistics.median(pcs)}  dist {sorted(Counter(pcs).items())}")
        na = Counter(len(a["alternatives"]) for a in accepted)
        print(f"alternatives per row: {sorted(na.items())}  cap(2) hit: {na.get(2,0)}")
        ratio = [max(word_count(p) for p in a["chunks"])/word_count(a["full_sentence"]) for a in accepted]
        print(f"largest piece share: median {statistics.median(ratio):.2f} max {max(ratio):.2f}")
if __name__ == "__main__":
    main()
