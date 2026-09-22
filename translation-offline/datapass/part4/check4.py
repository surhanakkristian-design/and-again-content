"""Part 4: machine check of the rewrite proposals (the wave-1 arm-B check, applied to intro_text AND
full_sentence), then the verifier input; `apply [--write]` writes the changes both passes agree on."""
import glob, json, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "lib"))
sys.path.insert(0, os.path.expanduser("~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/scripts"))
from validate_part import derive_full_sentence
PRON = {"es": "yo tú él ella usted nosotros nosotras vosotros vosotras ellos ellas ustedes".split(),
        "ua": "я ти він вона воно ми ви вони".split(), "tr": "ben sen o biz siz onlar".split(),
        "hu": "én te ő mi ti ők ön önök".split()}


def low(w):
    """lower() with Turkish dotted/dotless I (İçeri -> içeri, Islak -> ıslak), so a recased first word still matches."""
    return w.replace("I", "ı").replace("İ", "i").lower() if LANG_NOW[0] == "tr" else w.lower()


LANG_NOW = [""]


def toks(s):
    return [low(w) for w in re.findall(r"\w+", s or "")]


def punct(s):
    return re.sub(r"\s+", "", re.sub(r"\w+", "", s or ""))


def machine_check(lang, old, new):   # wave1/common/pipeline_w1.py::machine_check + ONE relaxation (marked below)
    LANG_NOW[0] = lang
    if not isinstance(new, str) or not new.strip():
        return False, None, 'empty new'
    a, b = toks(old), toks(new)
    rest = list(b)
    for t in a:
        if t in rest:
            rest.remove(t)
        else:
            return False, None, 'old token %r missing' % t
    if len(rest) != 1:
        return False, None, 'added tokens %r' % rest
    if rest[0] not in PRON[lang]:
        return False, rest[0], 'added %r is not an allowed pronoun' % rest[0]
    if punct(old) != punct(new):
        return False, rest[0], 'punctuation changed'
    wo, wn = re.findall(r'\w+', old), re.findall(r'\w+', new)
    lo = [low(w) for w in wo]
    ks = [k for k in range(len(wn)) if low(wn[k]) == rest[0] and [low(w) for w in wn[:k] + wn[k + 1:]] == lo]
    if not ks:
        return False, rest[0], 'word order changed'
    stripped = wn[:ks[0]] + wn[ks[0] + 1:]
    diffcase = [i for i, (x, y) in enumerate(zip(stripped, wo)) if x != y]
    # data-pass relaxation: a capitalised pronoun inserted at a sentence start in mid-text ('… recepcionista. Ella dijo')
    # takes the capital from the next word; that word, and only it, may lose its capital.
    k0 = ks[0]
    ok_mid = (k0 > 0 and wn[k0][:1].isupper() and diffcase == [k0] and stripped[k0][:1].islower()
              and wo[k0][:1].isupper() and low(stripped[k0]) == low(wo[k0]))
    if not ok_mid and (any(i != 0 for i in diffcase) or (diffcase and ks[0] != 0)):
        return False, rest[0], 'case changed'
    if ks[0] == 0 and stripped and stripped[0][:1].isupper() and not stripped[0].isupper():
        return False, rest[0], 'old first word kept its capital after the pronoun'
    return True, rest[0], None


rows = {(r["exercise_id"], r["language_code"]): r for r in json.load(open(os.path.join(HERE, "rows_before.json")))}
ex = {e["id"]: e for e in map(json.loads, open(os.path.join(ROOT, "snapshot/exercises.jsonl")))}


def load_props():
    props = []
    for L in ("es", "ua", "tr", "hu"):
        for p in sorted(glob.glob(os.path.join(HERE, f"prop_{L}_*.txt"))):
            for line in open(p, encoding="utf-8"):
                line = line.rstrip("\n")
                if not line.strip() or line.strip() == "NONE":
                    continue
                f = line.split("|")
                flag = f[3][5:].strip() if len(f) == 4 and f[3].startswith("FLAG") else None
                if len(f) not in (3, 4) or not f[0].strip().isdigit():
                    props.append({"lang": L, "raw": line, "ok": False, "why": "format"}); continue
                eid = int(f[0]); r = rows.get((eid, L))
                if r is None:
                    props.append({"lang": L, "raw": line, "ok": False, "why": "not an input row"}); continue
                oi, of, ans = r["intro_text"] or "", r["full_sentence"], r["correct_answer"] or ""
                ni, nf = f[1], f[2]
                ok1, p1, w1 = machine_check(L, oi, ni)
                ok2, p2, w2 = machine_check(L, of, nf)
                why = w1 and "intro: " + w1 or w2 and "full: " + w2
                ok = ok1 and ok2 and not why
                if ok and p1 != p2:
                    ok, why = False, "different pronouns in intro and full"
                if ok and ni.count("...") != oi.count("..."):
                    ok, why = False, "gap count changed"
                t = ex[eid]["exercise_type_id"]
                ans_cap = ans[:1].isupper() and ans[:1] != ans[:1].lower()
                if ok and (oi.lstrip().startswith("...") or (ans_cap and derive_full_sentence(ni, ans, L, t) != nf)):
                    ok, why = False, "gap opens the sentence: the pronoun would need correct_answer re-cased (left untouched)"
                if ok and derive_full_sentence(oi, ans, L, t) == of and derive_full_sentence(ni, ans, L, t) != nf:
                    ok, why = False, "full_sentence != intro+answer"
                props.append({"lang": L, "exercise_id": eid, "id": r["id"], "old": [oi, of], "new": [ni, nf],
                              "pronoun": p1, "flag": flag, "ok": ok, "why": why})
    return props


if __name__ == "__main__":
    props = load_props()
    json.dump(props, open(os.path.join(HERE, "props_checked.json"), "w"), ensure_ascii=False, indent=0)
    c = collections.Counter((p["lang"], p["ok"]) for p in props)
    print(c)
    for p in props:
        if not p["ok"]:
            print(" FAIL", p.get("exercise_id"), p["lang"], p["why"], p.get("new", p.get("raw")))
    for L in ("es", "ua", "tr", "hu"):
        with open(os.path.join(HERE, f"verify_in_{L}.txt"), "w") as f:
            n = 0
            for p in props:
                if p["lang"] == L and p["ok"]:
                    n += 1
                    f.write(f"{p['exercise_id']}|OLD: {p['old'][1]}|NEW: {p['new'][1]}\n")
        print(L, "to verify", n)
