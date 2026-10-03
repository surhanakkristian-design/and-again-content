import json,collections
R="data"
L=lambda n: json.load(open(f"{R}/{n}.json"))
cats={c["id"]:c["title"] for c in L("categories")}
media={m["id"]:m for m in L("media")}
mc=collections.defaultdict(set)
for r in L("media_categories"): mc[r["media_id"]].add(r["category_id"])
concepts={c["id"]:c for c in L("concepts")}
cm=L("concept_media"); ex=L("ex")
loc=collections.defaultdict(dict)
for r in L("loc"): loc[r["concept_id"]][r["language_code"]]=r
MERGE={7:"travel",39:"travel",12:"sport",25:"sport",16:"family",26:"family",32:"health",29:"health",13:"beauty",9:"beauty"}
def gkey(cid): return MERGE.get(cid,cid)
# media -> levels, concepts
mlev=collections.defaultdict(set); mcon=collections.defaultdict(lambda: collections.defaultdict(set))
for e in ex:
    lv="A" if e["exercise_type_id"]==74 else "B"
    mlev[e["media_id"]].add(lv); mcon[e["media_id"]][lv].add(e["concept_id"])
live=[m for m in media if m in mlev and media[m]["has_thumb"]]
