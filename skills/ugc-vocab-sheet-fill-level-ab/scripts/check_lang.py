#!/usr/bin/env python3
"""check_lang.py <workbook.xlsx> <content.txt> [--loanwords loanwords.json] [--langs sk,de,...]
Mechanical gates for one language-pass batch, before anything is written to the workbook.
Content file, one block per exercise, the `en` row taken from the workbook, not from the file:

    E <exercise_id>
    sk|<intro_text>|<correct_answer>|<distractor_1>|<distractor_2>
    de|...

Checks, in order:
 1  the exercise exists, the language code is one of the eight, no code twice in a block
 2  intro_text non-empty except on type 27, which must be empty in every language;
    answer cells MAY be empty and options MAY repeat (brief v26) — counted, never refused
 3  gap invariant: intro '...' count minus correct_answer '...' count == 1 on gapped types
 4  exactly three dots, never four; no pipe left in a field
 5  no row byte-identical to this exercise's en row (E10, the English fallback)
 6  no two language rows of one exercise identical (E11); sk/cz identical is a warning (W1)
 7  typography per language: quote marks, French space before ? ! ; :, Spanish opening ¿ ¡
 8  loanword lock over SENTENCE rows, which the validator checks only on word_localizations
 9  an English slang or address token surviving untranslated, against the anglicism allowlist
Exit 0 only when every error check passes. Warnings are printed and do not fail."""
import json, os, re, sys, collections
import openpyxl

# BRIEF §0p, 15.9.2026 — one definition of the per-type language scope, shared with
# validate_part.py and apply_lang.py. The no-intro / stem type sets come from there too:
# this file used to test `t == 27`, which was right while type 27 was the only no-intro
# type in an A part and wrong the moment type 74 was authored.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lang_scope

LANGS = ["sk", "de", "cz", "fr", "es", "ua", "tr", "hu"]
NO_INTRO = set(lang_scope.NO_INTRO_TYPES)      # 27 68 74 75 — options only, no stem
STEM = set(lang_scope.STEM_TYPES)              # 69 — '"<word>" means...' is a stem, not a gap
QUOTES = {"sk": ("„", "“"), "cz": ("„", "“"), "de": ("„", "“"), "hu": ("„", "”"),
          "fr": ("«", "»"), "es": ("«", "»"), "ua": ("«", "»"), "tr": ("“", "”")}
ALLOWED_ANGLICISM = {"mood", "glow up", "chill", "nerd mode", "ok", "okay", "wow", "hey"}
# Words of the target language that happen to spell an English slang token (found 11 Sept 2026:
# Spanish possessive "sus" flagged 11 times; French "respect" is an ordinary French noun).
FALSE_FRIEND = {"es": {"sus"}, "fr": {"respect"}}
ENGLISH_TOKEN = re.compile(r"\b(bro|bruh|dude|bestie|no cap|lowkey|low-key|highkey|gonna|wanna|gotta|"
                           r"kinda|ain't|tryna|dunno|lemme|y'all|fr|sus|mid|slay|delulu|rizz|cooked|"
                           r"goated|unhinged|npc|not gonna lie|guess what|listen|respect|smooth|iconic)\b", re.I)

wbp, cpath = sys.argv[1], sys.argv[2]
loan = {}
if "--loanwords" in sys.argv:
    loan = json.load(open(sys.argv[sys.argv.index("--loanwords") + 1], encoding="utf-8"))
langs = None          # None = "whatever §0p says for this exercise type"
if "--langs" in sys.argv:
    langs = [x.strip() for x in sys.argv[sys.argv.index("--langs") + 1].split(",") if x.strip()]
profile = lang_scope.profile_for(wbp)
print(f"language scope: {lang_scope.describe(profile)}")

wb = openpyxl.load_workbook(wbp, read_only=True)
ex = {}
for r in wb["exercises"].iter_rows(min_row=2, values_only=True):
    if isinstance(r[0], int): ex[r[0]] = (r[1], r[2], r[3], r[4])          # concept, media, type, options_count
con = {r[0]: str(r[1] or "").strip().lower() for r in wb["word_concepts"].iter_rows(min_row=2, values_only=True) if isinstance(r[0], int)}
enrow = {}
for r in wb["sentence_translations"].iter_rows(min_row=2, values_only=True):
    if isinstance(r[0], int) and str(r[2]).strip() == "en":
        enrow[int(r[1])] = tuple(str(x or "").strip() for x in r[3:7])

content, cur = collections.defaultdict(dict), None
words, wcur, kind = collections.defaultdict(dict), None, None
errs, warns = [], []
for ln, raw in enumerate(open(cpath, encoding="utf-8"), 1):
    line = raw.rstrip("\n")
    if not line.strip() or line.lstrip().startswith("#"): continue
    if line.startswith("E "):
        cur = int(line[2:].strip()); kind = "E"; continue
    if line.startswith("W "):
        wcur = int(line[2:].strip()); kind = "W"; continue
    if kind == "W":
        wp = line.split("|")
        if len(wp) != 2: errs.append(f"line {ln}: W {wcur}: expected '<lang>|<translation>', got {len(wp)} fields"); continue
        wl = wp[0].strip()
        if wl not in LANGS + ["en"]: errs.append(f"line {ln}: W {wcur}: {wl!r} is not a language code"); continue
        if wl in words[wcur]: errs.append(f"line {ln}: W {wcur} has two {wl} rows"); continue
        if not wp[1].strip(): errs.append(f"line {ln}: W {wcur}/{wl}: empty translation")
        words[wcur][wl] = wp[1].strip(); continue
    parts = line.split("|")
    if len(parts) != 5:
        errs.append(f"line {ln}: expected '<lang>|intro|correct|d1|d2', got {len(parts)} fields"); continue
    lang = parts[0].strip()
    if lang not in LANGS: errs.append(f"line {ln}: {lang!r} is not one of the eight language codes"); continue
    if cur is None: errs.append(f"line {ln}: text row before any E header"); continue
    if lang in content[cur]: errs.append(f"line {ln}: exercise {cur} has two {lang} rows"); continue
    content[cur][lang] = tuple(p.strip() for p in parts[1:])

for eid, got in sorted(content.items()):
    tag = f"E {eid}"
    if eid not in ex: errs.append(f"{tag}: not in the workbook"); continue
    cid, mid, t, oc = ex[eid]
    # BRIEF §0p — the languages this exercise TYPE is translated into, in this PART's profile.
    try:
        scope = lang_scope.translating_scope(t, profile)
    except lang_scope.UnruledTypeError as exc:
        errs.append(f"{tag}: {exc}"); continue
    want = [l for l in (langs if langs is not None else LANGS) if l in scope]
    missing = [l for l in want if l not in got]
    if missing: errs.append(f"{tag}: missing {missing}")
    extra = [l for l in got if l not in scope]
    if extra:
        errs.append(f"{tag}: §0p — type {t} is translated into {sorted(scope)} in this part; "
                    f"{sorted(extra)} out of scope")
    for lang, (intro, ca, d1, d2) in got.items():
        if lang not in scope: continue
        w = f"{tag}/{lang}"
        if t in NO_INTRO and intro: errs.append(f"{w}: type {t} must have an empty intro_text")
        if t not in NO_INTRO and not intro: errs.append(f"{w}: empty intro_text")
        # BRIEF v26, 14.9.2026: an empty answer cell and duplicate options are both legal in the
        # eight translating languages. This file only ever sees those eight (LANGS has no 'en'),
        # so both checks are removed outright rather than made conditional. The empty/duplicate
        # rows are counted, non-blocking, by apply_lang.py::count_gaps.
        # RULING 2 OF 15.9.2026 — Kristian: "To pravidlo o prazdnych bunkach sa netyka iba clenov.
        # Patria tam akekolvek slova." Brief §0m: where an English option has no adequate equivalent
        # in the target language the cell is EMPTY, for ANY word, not only for articles. So the
        # `options_count 3 but distractor_2 empty` guard is REMOVED for the eight translating
        # languages, the same way the empty-answer and duplicate-option guards were removed on
        # 14.9.2026. The article-keyed carve-out of proposed_article_cell_guard_20260915.diff is
        # superseded: it would have refused a Turkish ek-fiil cell emptied while its English
        # counterpart is `is`/`are`. The safety net is apply_lang.py::count_gaps, which writes every
        # empty cell with its row id and type per language. ENGLISH KEEPS THE GUARD (§0h.1).
        if t not in NO_INTRO and t not in STEM and intro.count("...") - ca.count("...") != 1:
            errs.append(f"{w}: gap invariant broken ({intro.count('...')} in intro, {ca.count('...')} in answer)")
        if "...." in intro or "…" in intro + ca + d1 + d2: errs.append(f"{w}: four-dot gap or a U+2026 ellipsis")
        op, cl = QUOTES[lang]
        # flag any quote mark that is not this language's own pair (found 11 Sept 2026: the old rule
        # flagged the closing U+201D for every language but hu, although tr closes with it too)
        for q in ('"', "“", "”", "„", "«", "»"):
            if q in intro and q not in (op, cl):
                warns.append(f"{w}: quote {q!r} where {lang} uses {op}…{cl}")
        if lang == "fr" and re.search(r"\S[?!;:]", intro): errs.append(f"{w}: French needs a space before ? ! ; :")
        if lang == "es":
            if intro.rstrip().endswith("?") and "¿" not in intro: errs.append(f"{w}: Spanish question without ¿")
            if intro.rstrip().endswith("!") and "¡" not in intro: errs.append(f"{w}: Spanish exclamation without ¡")
        en = enrow.get(eid)
        if en and (intro, ca, d1, d2) == en: errs.append(f"{w}: byte-identical to the en row (English fallback)")
        word = con.get(cid, "")
        if word in loan and lang in loan[word]:
            want = loan[word][lang]
            body = " ".join((intro, ca, d1, d2)).lower()
            if word in " ".join(en or ()).lower() and want.lower() not in body:
                warns.append(f"{w}: sentence does not carry the agreed loanword {want!r} for {word!r}")
        m = next((x for x in ENGLISH_TOKEN.finditer(" ".join((intro, ca, d1, d2)))
                  if x.group(0).lower() not in FALSE_FRIEND.get(lang, set())), None)
        if m and m.group(0).lower() not in ALLOWED_ANGLICISM:
            warns.append(f"{w}: English token {m.group(0)!r} left untranslated — check the slang/flirt/idiom rule")
    seen = {}
    for lang in sorted(l for l in got if l in scope):
        k = got[lang]
        if k in seen:
            o = seen[k]
            (warns if {lang, o} == {"sk", "cz"} else errs).append(f"{tag}: {o}/{lang} rows identical")
        seen[k] = lang

print(f"words {len(words)} | word rows {sum(len(v) for v in words.values())} | "
      f"exercises {len(content)} | language rows {sum(len(v) for v in content.values())} | "
      f"errors {len(errs)} | warnings {len(warns)}")
for e in errs[:60]: print("  ERROR   " + e)
for w in warns[:40]: print("  warning " + w)
sys.exit(1 if errs else 0)
