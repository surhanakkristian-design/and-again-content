"""Part 3 source slices. Order: the 2,015 selected first, then the other 8,268; inside each group by
media then exercise id; ~150 exercises per slice, never splitting a media across the selected/rest border.
Each slice gets the MEDIA context, the English row (the source), the sk/cz rows (meaning/register check),
and the loanword entries whose English term occurs in the slice."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
rows = [json.loads(l) for l in open(os.path.join(ROOT, "snapshot/loc_rows.jsonl"))]
ex = {e["id"]: e for e in map(json.loads, open(os.path.join(ROOT, "snapshot/exercises.jsonl")))}
sets = json.load(open(os.path.join(ROOT, "snapshot/sets.json")))
ctx = json.load(open(os.path.join(ROOT, "snapshot/media_ctx.json")))
loan = json.load(open(os.path.expanduser("~/Projects/and-again-content/skills/ugc-vocab-sheet-fill-level-ab/loanwords.json")))
by = {(r["exercise_id"], r["language_code"]): r for r in rows}
E = sets["empty_ids"]; S = {r["exercise_id"] for r in sets["selected"]}
TARGET = 150

def grp(i):
    return (i in S, ex[i]["type_level"][0])

def key(i):
    return (0 if i in S else 1, ex[i]["type_level"][0], ctx["e2m"][str(i)], i)

order = sorted(E, key=key)
slices, cur, cur_m = [], [], None
for i in order:
    m = (grp(i), ctx["e2m"][str(i)])
    if cur and m != cur_m and (len(cur) >= TARGET or m[0] != cur_m[0]):
        slices.append(cur); cur = []
    cur.append(i); cur_m = m
if cur:
    slices.append(cur)

def f(v):
    return "" if v is None else v

os.makedirs(os.path.join(HERE, "slices"), exist_ok=True)
index = []
for n, sl in enumerate(slices, 1):
    name = f"s{n:03d}"
    lvl = {ex[i]["type_level"][0] for i in sl}
    text, last_m = [], None
    blob = []
    for i in sl:
        m = ctx["e2m"][str(i)]
        if m != last_m:
            md = ctx["media"][str(m)]
            text.append(f"MEDIA {m} | word: {md.get('word','')} | meaning: {md.get('meaning','')} | irony: {md.get('irony','')}")
            sc = md.get('scene', ''); text.append('scene: ' + (sc if len(sc) <= 320 else sc[:320].rsplit(' ', 1)[0] + ' …'))
            last_m = m
        en = by[(i, "en")]; info = ctx["e2info"][str(i)]
        sel = " | SEL" if i in S else ""
        text.append(f"E {i} | {ex[i]['type_level']} type {ex[i]['exercise_type_id']} {ex[i]['type_title']} | style {info['style']} | options {2 if not f(en['distractor_2']).strip() else 3}{sel}")
        for L in ("en", "sk", "cz"):
            r = by[(i, L)]
            text.append(f"{L}|{f(r['intro_text'])}|{f(r['correct_answer'])}|{f(r['distractor_1'])}|{f(r['distractor_2'])}")
        blob.append(" ".join(f(en[k]) for k in ("intro_text", "correct_answer", "distractor_1", "distractor_2")).lower())
    b = " ".join(blob)
    lw = {k: {L: v[L] for L in ("en", "de", "ua", "es", "fr", "tr", "hu") if L in v}
          for k, v in loan.items() if k != "_readme" and isinstance(v, dict) and re.search(r"\b" + re.escape(k.lower()) + r"s?\b", b)}
    if lw:
        text.append("LOANWORD LOCK (binding for these terms in this sense): " + json.dumps(lw, ensure_ascii=False))
    open(os.path.join(HERE, "slices", name + ".txt"), "w").write("\n".join(text) + "\n")
    index.append({"slice": name, "ids": sl, "selected": sum(1 for i in sl if i in S), "levels": "".join(sorted(lvl))})
json.dump(index, open(os.path.join(HERE, "slices", "index.json"), "w"))
import collections
print(len(slices), collections.Counter(x["levels"] for x in index), [len(s) for s in slices][:30], max(len(s) for s in slices))
print("selected slices", sum(1 for x in index if x["selected"]), "mixed", sum(1 for x in index if 0 < x["selected"] < len(x["ids"])))
