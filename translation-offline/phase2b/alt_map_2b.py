#!/usr/bin/env python3
"""Phase 2B: map the content words of the 200 English references to the existing synonym groups
(phase1b/synonyms/table.json, 863 groups = the "~862" table; the live translation_synonym_groups table does not exist).
Classes: mapped = token or its lemma is a member / generated surface form of an existing group;
propose_new = known content word (wordlist/en_words.txt), not mapped, and >=1 candidate synonym that IS in the table's
member vocabulary, where candidates come from the only thesauri the pipeline has (no WordNet installed):
the 1C contextual groups not merged into the table (phase1b/synonyms/ng_phase1c.json) and every annotator "alt"
map ({word: [alternatives]}) found in phase1*/phase2a JSON files; unmapped = everything else."""
import json, os, re, glob, collections
H = os.path.dirname(os.path.abspath(__file__)); TO = os.path.dirname(H); SY = f"{TO}/phase1b/synonyms"
table = json.load(open(f"{SY}/table.json"))["groups"]; forms = json.load(open(f"{SY}/forms.json"))["groups"]
ids = {g["id"] for g in table}
member = collections.defaultdict(set); surface = collections.defaultdict(set); phrases = collections.defaultdict(set)
for g in table:
    for m in g["m"]:
        (phrases if " " in m else member)[m.lower()].add(g["id"])
for gid, g in forms.items():
    if gid not in ids: continue
    for lst in (g.get("forms") or {}).values():
        for s in lst:
            (phrases if " " in s else surface)[s.lower()].add(gid)
vocab = set(member) | set(surface)
known = set(w.strip().lower() for w in open(f"{TO}/wordlist/en_words.txt"))
STOP = set("""a an the and or but if so than then that this these those there here it its i me my mine you your yours he him his she
her hers we us our ours they them their theirs who whom whose which what when where why how not no nor of to in on at by for
with from into onto about as up down out off over under again very too also just only be am is are was were been being have
has had having do does did doing will would shall should can could may might must let s t d ll re ve m don doesn didn isn aren
wasn weren won wouldn can't cannot all any some each every both either neither one ones own same such more most much many
few other another""".split())
def lemmas(t):
    c = [t]
    for suf, rep in (("ies", "y"), ("ied", "y"), ("ier", "y"), ("iest", "y"), ("ing", ""), ("ing", "e"), ("ed", ""), ("ed", "e"),
                     ("es", ""), ("s", ""), ("er", ""), ("est", ""), ("ly", "")):
        if t.endswith(suf) and len(t) - len(suf) >= 3:
            b = t[: -len(suf)] + rep; c.append(b)
            if len(b) > 3 and b[-1] == b[-2] and not rep: c.append(b[:-1])
    return list(dict.fromkeys(c))
# candidate thesaurus
cand = collections.defaultdict(set)
for g in json.load(open(f"{SY}/ng_phase1c.json"))["groups"]:
    ms = [m.lower() for m in g["m"]]
    for m in ms: cand[m].update(x for x in ms if x != m)
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "alt" and isinstance(v, dict):
                for w, alts in v.items():
                    if isinstance(alts, list): cand[str(w).lower()].update(str(a).lower() for a in alts if isinstance(a, str))
            else: walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
nfiles = 0
for fp in glob.glob(f"{TO}/phase1*/**/*.json", recursive=True) + glob.glob(f"{TO}/phase2a/**/*.json", recursive=True):
    try: walk(json.load(open(fp))); nfiles += 1
    except Exception: pass
rows = json.load(open(f"{H}/sample_2b.json"))["rows"]
cnt = collections.Counter(); bylvl = collections.defaultdict(collections.Counter); bylang = collections.defaultdict(collections.Counter); detail = []
for r in rows:
    s = (r["en"] or "").lower().replace("’", "'")
    covered = {}
    for p, gs in phrases.items():
        if re.search(r"\b" + re.escape(p) + r"\b", s):
            for w in p.split(): covered[w] = sorted(gs)
    toks = [t for t in re.findall(r"[a-z]+(?:'[a-z]+)?", s)]
    toks = [t.split("'")[0] for t in toks]
    items = []
    for t in toks:
        if t in STOP or len(t) < 2: continue
        L = lemmas(t); gs = set()
        if t in covered: gs.update(covered[t])
        for l in L: gs |= member.get(l, set()) | surface.get(l, set())
        if gs: cls, info = "mapped", sorted(gs)
        else:
            c = set()
            for l in L: c |= {x for x in cand.get(l, set()) if x in vocab}
            if c and any(l in known for l in L): cls, info = "propose_new", sorted(c)[:5]
            else: cls, info = "unmapped", []
        items.append({"tok": t, "lemma": L[-1] if len(L) > 1 else t, "class": cls, "groups_or_candidates": info})
        cnt[cls] += 1; bylvl[r["level"]][cls] += 1; bylang[r["lang"]][cls] += 1
    detail.append({"n": r["n"], "exercise_id": r["exercise_id"], "level": r["level"], "en": r["en"], "tokens": items,
                   "rows_with_mapped": any(i["class"] == "mapped" for i in items)})
res = {"table": "phase1b/synonyms/table.json", "groups": len(table), "member_vocab": len(member), "surface_forms": len(surface),
       "phrase_members": len(phrases), "candidate_thesaurus_words": len(cand), "candidate_files_scanned": nfiles,
       "definition": __doc__, "overall": dict(cnt), "by_level": {k: dict(v) for k, v in sorted(bylvl.items())},
       "by_lang": {k: dict(v) for k, v in bylang.items()}, "rows_with_any_mapped": sum(d["rows_with_mapped"] for d in detail),
       "rows": detail}
json.dump(res, open(f"{H}/alt_map_2b.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ("rows", "definition")}))
