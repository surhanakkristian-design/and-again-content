#!/usr/bin/env python3
"""Phase 2F §1.2 — why is s04 refused?  Static half: byte-for-byte prompt comparison and slice analysis.
0 model calls, 0 DB access.  Writes diag/s04_facts.json."""
import json, os, sys, unicodedata, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prompts_2f
H = os.path.dirname(os.path.abspath(__file__))
SUSPECT = ["cz_0002_s04_v", "cz_0003_s04_v", "cz_0004_s04_v"]
OK      = ["cz_0002_s03_v", "cz_0001_s07_v", "cz_0002_s05_v"]
m = prompts_2f.load(["cz_0001", "cz_0002", "cz_0003", "cz_0004"])
CACHE = {}
def get(sid):
    if sid not in CACHE:
        CACHE[sid] = prompts_2f.chunk_task(m, sid.rsplit("_s", 1)[0], sid)
    return CACHE[sid]
def profile(sid):
    lang, brows, crows, header, lines = get(sid)
    prompt = header + "\n".join(lines)
    b = prompt.encode("utf-8")
    cats = collections.Counter(unicodedata.category(c) for c in prompt)
    nonascii = collections.Counter(c for c in prompt if ord(c) > 127)
    ctrl = {hex(ord(c)): n for c, n in collections.Counter(
        c for c in prompt if unicodedata.category(c) == "Cc" and c not in "\n\t").items()}
    lens = sorted(len(l) for l in lines)
    srcs = [r["src"] for r in crows]
    return {"sid": sid, "bytes": len(b), "chars": len(prompt), "lines": prompt.count("\n") + 1,
            "row_lines": len(lines), "max_line_chars": max(len(l) for l in lines),
            "max_line_bytes": max(len(l.encode("utf-8")) for l in lines),
            "longest_row_n": crows[lines.index(max(lines, key=len))]["n"],
            "row_len_quartiles": [lens[0], lens[len(lens)//4], lens[len(lens)//2], lens[3*len(lens)//4], lens[-1]],
            "mean_row_len": round(sum(lens)/len(lens), 1),
            "unicode_categories": dict(cats), "control_chars_besides_nl_tab": ctrl,
            "lone_surrogates": sum(1 for c in prompt if 0xD800 <= ord(c) <= 0xDFFF),
            "format_chars_Cf": {hex(ord(c)): n for c, n in nonascii.items() if unicodedata.category(c) == "Cf"},
            "nbsp_zero_width": {hex(ord(c)): n for c, n in nonascii.items()
                                if ord(c) in (0x00A0, 0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF)},
            "bidi_marks": {hex(ord(c)): n for c, n in nonascii.items() if 0x202A <= ord(c) <= 0x202E or 0x2066 <= ord(c) <= 0x2069},
            "nonascii_codepoints": sorted(hex(ord(c)) for c in nonascii),
            "nonascii_total": sum(nonascii.values()),
            "angle_brackets": prompt.count("<") + prompt.count(">"),
            "backticks": prompt.count("`"), "triple_quote": prompt.count('"""'),
            "n_range": [min(r["n"] for r in crows), max(r["n"] for r in crows)],
            "levels": dict(collections.Counter(r.get("level") for r in crows)),
            "langs": dict(collections.Counter(r.get("lang") for r in crows)),
            "src_chars_mean": round(sum(len(s) for s in srcs)/len(srcs), 1),
            "src_chars_max": max(len(s) for s in srcs),
            "topics": dict(collections.Counter(r.get("type_title") for r in crows).most_common(5)),
            "_cp_set": set(nonascii), "_srcs": srcs, "_ns": [r["n"] for r in crows]}
P = {s: profile(s) for s in SUSPECT + OK}
ok_union = set().union(*[P[s]["_cp_set"] for s in OK])
for s in SUSPECT:
    P[s]["codepoints_in_this_chunk_and_in_NO_successful_chunk"] = sorted(
        "%s U+%04X %s" % (c, ord(c), unicodedata.name(c, "?")) for c in P[s]["_cp_set"] - ok_union)
sus_union = set().union(*[P[s]["_cp_set"] for s in SUSPECT])
for s in OK:
    P[s]["codepoints_absent_from_every_suspect"] = sorted("U+%04X" % ord(c) for c in P[s]["_cp_set"] - sus_union)
# slice position + shared material across the three s04 chunks
pos = {}
for bid in ("cz_0001", "cz_0002", "cz_0003", "cz_0004"):
    _b, _l, rows = [b for b in m.BATCHES if b[0] == bid][0]
    ch = m.chunks(rows)
    pos[bid] = {"chunks": len(ch), "s04_index_of": "4 of %d" % len(ch),
                "s04_n_range": [ch[3][0]["n"], ch[3][-1]["n"]] if len(ch) >= 4 else None,
                "s04_offset_in_batch": [300, 399] if len(ch) >= 4 else None}
srcs04 = {b: set(P[b + "_s04_v"]["_srcs"]) for b in ("cz_0002", "cz_0003", "cz_0004")}
shared = {"cz_0002&cz_0003": len(srcs04["cz_0002"] & srcs04["cz_0003"]),
          "cz_0002&cz_0004": len(srcs04["cz_0002"] & srcs04["cz_0004"]),
          "cz_0003&cz_0004": len(srcs04["cz_0003"] & srcs04["cz_0004"]),
          "all_three": len(srcs04["cz_0002"] & srcs04["cz_0003"] & srcs04["cz_0004"])}
dupe_in_s04 = {b: len(P[b + "_s04_v"]["_srcs"]) - len(set(P[b + "_s04_v"]["_srcs"])) for b in srcs04}
byte_eq = {}
for s in SUSPECT:
    for o in OK:
        a, bb = P[s], P[o]
        byte_eq["%s vs %s" % (s, o)] = {"byte_delta": a["bytes"] - bb["bytes"],
                                        "char_delta": a["chars"] - bb["chars"],
                                        "max_line_delta": a["max_line_chars"] - bb["max_line_chars"],
                                        "header_identical": get(s)[3] == get(o)[3]}
out = {"profiles": {k: {kk: vv for kk, vv in v.items() if not kk.startswith("_")} for k, v in P.items()},
       "slice_position": pos, "shared_src_between_s04_chunks": shared,
       "duplicate_src_inside_each_s04": dupe_in_s04, "pairwise": byte_eq}
json.dump(out, open(os.path.join(H, "s04_facts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1)[:6000])
