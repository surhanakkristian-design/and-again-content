#!/usr/bin/env python3
"""
exercise_selection.py — BRIEF §0r and §0s: how many exercises a word carries, and which.

ONE definition, the same discipline as `lang_scope.py`. Imported by `rebuild_skeleton.py`
(which builds a part's exercise rows), by `validate_part.py` (whose [E8] contract check is
derived from it) and by the top-up step of an English pass. Nothing here is written twice.

§0r — RULED 15-16 September 2026 (Kristian: "1. ano, súhlas. 2. ano."):

    | A word, video | 8 of 26 grammar  | 2 vocabulary (27, 74)     | 10 |
    | A word, image | 1 grammar        | 2                         |  3 |
    | B word, video | 11 of 37 grammar | 3 vocabulary (68, 69, 75) | 14 |
    | B word, image | 1 grammar        | 3                         |  4 |

8 and 11 are 30% rounded up. A part 1 keeps its old 28-per-video shape ("Nechaj to tak"),
except its images, which gain one grammar exercise — it is the one exception, named in
`exercise_contract.json`; every other part defaults to §0r.

§0s — the selection table, APPROVED 16.9.2026. Grouped by where the gap sits relative to the
target word. Only the A level is designed; **the B-level grouping of the 37 types does not
exist and is not invented here** — asking for it raises `SelectionNotDesigned`.

§0s.2 — the 8 (or 11) for a video, in this order:
  1. adjectives take group 3 first (22, then 1); adverbs take 25, then 1
     ("Chcem aby prídavné mená a príslovky išli na tieto cvičenia prednostne.");
  2. the remainder: the types with the FEWEST exercises in this part so far, from the word's
     available set; ties broken by type id, so a rerun reproduces the result exactly;
  3. a type that cannot be built for that word is skipped and the next one taken — at write
     time, by a flag and a top-up (`next_video_type`), never forced.

§0s.3 — images: round-robin in media_id order. Image n takes grammar type n, cycling; no
suitability ranking, no deficit rule ("A nemusí sa nad tým premýšľať."). A type outside the
word's part-of-speech set, or flagged unbuildable, is skipped and the next in the cycle taken.

Types 70-73 and 76-77 ("Random") are unruled and are never selected; `lang_scope` raises on them.
"""
import json
import os
from collections import Counter

# ---------------------------------------------------------------------------------------
# §0r — the counts
# ---------------------------------------------------------------------------------------
GRAMMAR_TYPES = {"A": tuple(range(1, 27)), "B": tuple(range(31, 68))}
VOCAB_TYPES = {"A": (27, 74), "B": (68, 69, 75)}
GRAMMAR_PER = {"A": {"video": 8, "image": 1}, "B": {"video": 11, "image": 1}}

# ---------------------------------------------------------------------------------------
# §0s — the A-level groups, approved 16.9.2026
# ---------------------------------------------------------------------------------------
GROUPS_A = {
    1: (2, 5, 6, 7, 8, 10, 11, 19, 20, 21),           # the gap is at a noun — nouns only
    2: (3, 4, 12, 13, 14, 15, 16, 17, 18, 23, 24),    # the gap is at a verb — any POS
    3: (1, 22, 25),                                   # the gap is at an adjective or adverb
    4: (9, 26),                                       # part of speech irrelevant
}
POS_GROUPS_A = {
    "noun": (1, 2, 4),
    "verb": (2, 4),
    "adjective": (2, 3, 4),
    "adverb": (2, 3, 4),
}
OTHER_POS_GROUPS_A = (2, 4)          # any POS not listed ('phrase' occurs live) — §0s
PRIORITY_A = {"adjective": (22, 1), "adverb": (25, 1)}   # §0s.2 point 1

assert sorted(t for g in GROUPS_A.values() for t in g) == list(GRAMMAR_TYPES["A"])


class SelectionNotDesigned(Exception):
    """The B-level grouping of the 37 grammar types has not been designed (BRIEF §0s)."""


def _require_a(level):
    if level != "A":
        raise SelectionNotDesigned(
            f"level {level}: the §0s grouping exists for level A only. The B-level grouping of "
            f"the 37 grammar types has not been designed — do not invent it; ask Kristian.")


def available_types(pos, level="A"):
    """The grammar types a word of this part of speech may draw from, sorted by id."""
    _require_a(level)
    groups = POS_GROUPS_A.get((pos or "").strip().lower(), OTHER_POS_GROUPS_A)
    return tuple(sorted(t for g in groups for t in GROUPS_A[g]))


def is_other_pos(pos):
    return (pos or "").strip().lower() not in POS_GROUPS_A


def select_video(pos, counts, level="A", exclude=(), n=None):
    """§0s.2 — the grammar types for ONE video, given the part's running per-type counts.

    `counts` is a Counter of exercises per type already assigned in this part; it is NOT
    modified here (the caller adds the result). `exclude` holds types flagged unbuildable for
    this word. Deterministic: priority first, then fewest-so-far, ties by type id."""
    _require_a(level)
    n = GRAMMAR_PER[level]["video"] if n is None else n
    avail = [t for t in available_types(pos, level) if t not in set(exclude)]
    chosen = []
    for t in PRIORITY_A.get((pos or "").strip().lower(), ()):
        if t in avail and len(chosen) < n:
            chosen.append(t)
    rest = sorted((t for t in avail if t not in chosen), key=lambda t: (counts.get(t, 0), t))
    chosen += rest[: n - len(chosen)]
    return sorted(chosen)


def next_video_type(pos, counts, already, flagged, level="A"):
    """The top-up of §0s.2 point 3: one replacement for a flagged pairing. `already` = the
    word's current grammar types (the flagged one excluded or not — both are skipped),
    `flagged` = every type flagged for this word. Returns None when the set is exhausted."""
    _require_a(level)
    skip = set(already) | set(flagged)
    pos_l = (pos or "").strip().lower()
    cand = [t for t in PRIORITY_A.get(pos_l, ()) if t in available_types(pos, level) and t not in skip]
    if cand:
        return cand[0]
    rest = sorted((t for t in available_types(pos, level) if t not in skip),
                  key=lambda t: (counts.get(t, 0), t))
    return rest[0] if rest else None


def image_type(n, pos, level="A", exclude=()):
    """§0s.3 — image number `n` (1-based, media_id order within the part) takes grammar type n,
    cycling. A type outside the word's part-of-speech set, or in `exclude`, is skipped and the
    next in the cycle taken. Returns (type, [skipped types])."""
    _require_a(level)
    cycle = GRAMMAR_TYPES[level]
    avail = set(available_types(pos, level)) - set(exclude)
    skipped = []
    for k in range(len(cycle)):
        t = cycle[(n - 1 + k) % len(cycle)]
        if t in avail:
            return t, skipped
        skipped.append(t)
    return None, skipped


def select_part(media, level="A", exclude=None):
    """The whole part. `media` = iterable of (media_id, media_kind 'video'|'image', pos), any
    order — processed in media_id order. `exclude` = {media_id: set(types)} flagged unbuildable.
    Returns (assignment {media_id: [grammar types]}, counts Counter, image_skips {media_id: [..]})."""
    _require_a(level)
    exclude = exclude or {}
    counts, out, skips = Counter(), {}, {}
    img_n = 0
    for mid, kind, pos in sorted(media, key=lambda m: int(m[0])):
        ex = exclude.get(mid, ())
        if kind == "video":
            types = select_video(pos, counts, level, exclude=ex)
        elif kind == "image":
            img_n += 1
            t, sk = image_type(img_n, pos, level, exclude=ex)
            types = [t] if t is not None else []
            if sk:
                skips[mid] = sk
        else:
            raise ValueError(f"media {mid}: kind {kind!r} is neither video nor image")
        counts.update(types)
        out[mid] = types
    return out, counts, skips


# ---------------------------------------------------------------------------------------
# The [E8] contract, per workbook — keyed the way lang_scope.json keys the language profile
# ---------------------------------------------------------------------------------------
CONTRACT_FILE = "exercise_contract.json"
DEFAULT_CONTRACT = "0r"
CONTRACTS = {
    # BRIEF §0r: grammar count per media kind + the level's vocabulary types, exactly
    "0r": "§0r — A: video 8 grammar + 27 + 74, image 1 + 27 + 74; B: video 11 + 68 69 75, image 1 + 68 69 75",
    # A part 1 only: videos keep all 26 grammar types + 27 + 74 (28); images 1 grammar + 27 + 74 (3)
    "part1-28": "A part 1 — video all 26 grammar + 27 + 74 (28); image 1 grammar + 27 + 74 (3)",
}


def contract_for(workbook_path):
    """Contract profile name for one workbook, by FILE NAME: the workbook's directory first, then
    this scripts directory. A missing file or an unnamed workbook gets the ruling, §0r."""
    base = os.path.basename(workbook_path)
    fallback = DEFAULT_CONTRACT
    for f in (os.path.join(os.path.dirname(os.path.abspath(workbook_path)), CONTRACT_FILE),
              os.path.join(os.path.dirname(os.path.abspath(__file__)), CONTRACT_FILE)):
        if not os.path.exists(f):
            continue
        conf = json.load(open(f, encoding="utf-8"))
        if base in conf.get("by_workbook", {}):
            name = conf["by_workbook"][base]
            if name not in CONTRACTS:
                raise ValueError(f"{f}: unknown contract {name!r}; known {sorted(CONTRACTS)}")
            return name
        fallback = conf.get("default", fallback)
        if fallback not in CONTRACTS:
            raise ValueError(f"{f}: unknown default contract {fallback!r}")
    return fallback


def check_media(types, level, kind, contract):
    """Problems (list of str) with one media's exercise types under a contract. Empty = OK."""
    probs = []
    grammar = [t for t in types if t in GRAMMAR_TYPES[level]]
    vocab = sorted(t for t in types if t not in GRAMMAR_TYPES[level])
    want_vocab = sorted(VOCAB_TYPES[level])
    if vocab != want_vocab:
        probs.append(f"vocabulary types {vocab}, expected {want_vocab}")
    if len(set(grammar)) != len(grammar):
        probs.append(f"a grammar type repeats: {sorted(grammar)}")
    if contract == "part1-28" and kind == "video":
        want = len(GRAMMAR_TYPES[level])
        if sorted(grammar) != list(GRAMMAR_TYPES[level]):
            probs.append(f"{len(grammar)} grammar exercises, expected all {want} (part-1 contract)")
    else:
        want = GRAMMAR_PER[level][kind]
        if len(grammar) != want:
            probs.append(f"{len(grammar)} grammar exercises, expected {want} ({contract})")
    return probs


def expected_total(level, kind, contract):
    if contract == "part1-28" and kind == "video":
        return len(GRAMMAR_TYPES[level]) + len(VOCAB_TYPES[level])
    return GRAMMAR_PER[level][kind] + len(VOCAB_TYPES[level])


if __name__ == "__main__":
    import sys
    for pos in ("noun", "verb", "adjective", "adverb", "phrase"):
        a = available_types(pos)
        print(f"{pos:10s} {len(a):2d} types: {list(a)}")
    for wbp in sys.argv[1:]:
        print(f"{os.path.basename(wbp)}: contract {contract_for(wbp)!r}")
