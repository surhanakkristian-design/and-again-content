#!/usr/bin/env python3
"""
lang_scope.py — BRIEF §0p: which languages an exercise is translated into.

ONE definition, imported by `validate_part.py`, `check_lang.py` and `apply_lang.py`.
Three copies of a rule is how the `distractor_2` guard came to be wrong in two scripts
for a day (REPORT_2026-09-15_07 §7, the eighth time the checker was the fault). Nothing
here is duplicated anywhere else: a script that needs the scope imports it.

RULING, 15 September 2026 — Kristian: *"Vsetky gramaticke cvicenia prekladaj iba do
cestiny a slovenciny."* Scope is decided per exercise TYPE, not per part:

    Vocabulary types 27, 68, 69, 74, 75   ->  all nine: en + sk cz ua de fr es tr hu
    every other (grammar) type            ->  en + sk + cz only

**Types 70-73 ("Random", A1/A2/B1/B2, focus category Grammar) and 76-77 ("Random", A and B,
focus category Vocabulary) are UNRULED** (70-73 added 16.9.2026, BRIEF §0s). Kristian was
not asked about them. `scope_for` raises `UnruledTypeError` rather than guessing, so a part
that contains one stops instead of being silently translated into the wrong set.

**Part 1 is not retrofitted.** A part 1 was finished in all eight translating languages before
this ruling and stays that way, so it carries the legacy profile. The profile is stored
per workbook in a `lang_scope.json` beside it:

    {"default": "0p", "by_workbook": {"6.9.2026_A_part1.xlsx": "all-nine"}}

It is read from the workbook's own directory first and from this scripts directory second, so a
§0f scratch copy that keeps the workbook's file name resolves the same way the original does.

**The default is the ruling, not the legacy.** A part that nobody remembers to configure — part 3,
part 4, a B part — gets §0p, because `DEFAULT_PROFILE` is `"0p"` and a missing file means the
default. Only the one finished part is named as an exception. Forgetting therefore produces the
current rule, never the superseded one.
"""
import json
import os

# The nine, in the workbook's own column order.
LANGS9 = ("sk", "en", "de", "cz", "fr", "es", "ua", "tr", "hu")
LANGS8 = tuple(l for l in LANGS9 if l != "en")          # the translating languages

# --- the type sets. These live here and nowhere else. ---------------------------------
VOCAB_TYPES = frozenset({27, 68, 69, 74, 75})   # Label the video A/B, Meaning of the word,
                                                # Simple Explanation A/B
UNRULED_TYPES = frozenset({70, 71, 72, 73, 76, 77})  # "Random" — no ruling, BRIEF §0p/§0s
UNRULED_NAMES = {                               # by name, so the refusal says which one
    70: '"Random" A1, Grammar', 71: '"Random" A2, Grammar',
    72: '"Random" B1, Grammar', 73: '"Random" B2, Grammar',
    76: '"Random" A, Vocabulary', 77: '"Random" B, Vocabulary',
}
NO_INTRO_TYPES = frozenset({27, 68, 74, 75})    # options only, no stem, no gap
STEM_TYPES = frozenset({69})                    # '"<word>" means...' — a stem, not a gap

# --- the profiles ---------------------------------------------------------------------
GRAMMAR_0P = frozenset({"en", "sk", "cz"})
ALL_NINE = frozenset(LANGS9)

PROFILES = {
    "0p":       {"vocab": ALL_NINE, "grammar": GRAMMAR_0P},   # BRIEF §0p, from part 2 on
    "all-nine": {"vocab": ALL_NINE, "grammar": ALL_NINE},     # part 1, finished before §0p
}
DEFAULT_PROFILE = "0p"
SCOPE_FILE = "lang_scope.json"


class UnruledTypeError(Exception):
    """An exercise type nobody has ruled a language scope for (76 / 77)."""


def profile_sources(workbook_path):
    """The `lang_scope.json` files consulted, nearest first: the workbook's own directory, then
    the scripts directory. The second one is why a workbook COPIED to a scratch directory still
    resolves correctly — §0f copies every workbook out of Drive before writing to it, and a map
    that lived only beside the original would be invisible there."""
    return [os.path.join(os.path.dirname(os.path.abspath(workbook_path)), SCOPE_FILE),
            os.path.join(os.path.dirname(os.path.abspath(__file__)), SCOPE_FILE)]


def profile_for(workbook_path):
    """The profile name for one workbook, keyed by its FILE NAME.

    Keyed by file name, not by directory: partsA/ holds part 1, part 2 and part 3 side by side,
    so a directory-level setting could not tell them apart — and a scratch copy that keeps its
    name keeps its scope.

    **A copy that is RENAMED (work.xlsx) resolves to DEFAULT_PROFILE, which is the ruling.** That
    fails loudly and safely: a part-1 batch applied to such a copy is REFUSED row by row for being
    out of scope, never written with the wrong scope. Keep the workbook's own name in scratch."""
    base = os.path.basename(workbook_path)
    fallback = DEFAULT_PROFILE
    for f in profile_sources(workbook_path):
        if not os.path.exists(f):
            continue
        with open(f, encoding="utf-8") as fh:
            conf = json.load(fh)
        if base in conf.get("by_workbook", {}):
            name = conf["by_workbook"][base]
            if name not in PROFILES:
                raise ValueError(f"{f}: unknown profile {name!r}; known: {sorted(PROFILES)}")
            return name
        fallback = conf.get("default", fallback)
        if fallback not in PROFILES:
            raise ValueError(f"{f}: unknown default profile {fallback!r}; known: {sorted(PROFILES)}")
    return fallback


def scope_for(exercise_type, profile=DEFAULT_PROFILE):
    """The set of language codes this exercise type is translated into, `en` included."""
    t = int(exercise_type)
    if t in UNRULED_TYPES:
        raise UnruledTypeError(
            f"exercise type {t} ({UNRULED_NAMES[t]}) has no ruled language scope — "
            f"BRIEF §0p covers types {sorted(VOCAB_TYPES)} as vocabulary and every other type "
            f"as grammar. Stop and ask; do not assign it to either.")
    p = PROFILES[profile]
    return p["vocab"] if t in VOCAB_TYPES else p["grammar"]


def translating_scope(exercise_type, profile=DEFAULT_PROFILE):
    """`scope_for` without English — what a translation pass is expected to fill."""
    return frozenset(scope_for(exercise_type, profile)) - {"en"}


def describe(profile=DEFAULT_PROFILE):
    p = PROFILES[profile]
    return (f"profile {profile!r}: vocabulary types {sorted(VOCAB_TYPES)} -> "
            f"{sorted(p['vocab'])}; every other type -> {sorted(p['grammar'])}")


if __name__ == "__main__":
    import sys
    for name in sorted(PROFILES):
        print(describe(name))
    for wbp in sys.argv[1:]:
        print(f"{os.path.basename(wbp)}: profile {profile_for(wbp)!r}")
