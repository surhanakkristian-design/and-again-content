import json,re,collections
raw=json.load(open("raw_records.json"))["recs"]; live=json.load(open("live_media.json"))
vids=live
def norm(s): return re.sub(r"\s+"," ",s or "").strip()
def word_of(t): return re.sub(r"_\d+$","",t).replace("_"," ").strip().lower()
EMPTY={"","-","—","none","n/a","na","no voiceover","(no voiceover)","null"}
out={}; conflicts=[]; excluded=[]
for m in vids:
    rs=raw.get(str(m["id"]),[]); tw=word_of(m["title"])
    match=[r for r in rs if r["word"].strip().lower().replace("_"," ").replace("-"," ")==tw]
    if rs and not match: excluded.append({"id":m["id"],"title":m["title"],"workbook_words":sorted(set(r["word"] for r in rs))})
    match.sort(key=lambda r:-r["mtime"])
    def pick(field):
        vals=[(norm(r[field]),r["file"]) for r in match if norm(r[field]).lower() not in EMPTY]
        if not vals: return None,None
        distinct=collections.OrderedDict()
        for v,f in vals: distinct.setdefault(v,f)
        if len(distinct)>1: conflicts.append({"id":m["id"],"title":m["title"],"field":field,"chosen":vals[0][0],"chosen_file":vals[0][1],"others":[{"value":v,"file":f} for v,f in list(distinct.items())[1:]]})
        return vals[0]
    vo,vf=pick("vo"); ex,ef=pick("expl")
    out[m["id"]]={"title":m["title"],"media_type":m["media_type"],"transcript":vo,"transcript_file":vf,"asset_description":ex,"description_file":ef}
json.dump(out,open("media_text_map.json","w"),indent=0,ensure_ascii=False)
json.dump({"conflicts":conflicts,"excluded_word_mismatch":excluded},open("conflicts.json","w"),indent=1,ensure_ascii=False)
c=collections.Counter((v["transcript"] is not None, v["asset_description"] is not None) for v in out.values())
print(c, "conflicts:",collections.Counter(x["field"] for x in conflicts))
for x in conflicts[:6]: print(json.dumps(x,ensure_ascii=False)[:400])
