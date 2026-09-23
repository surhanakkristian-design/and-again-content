import json
m=json.load(open("media_text_map.json")); sd=json.load(open("split_det.json"))
A={}
for k,v in sd.items():
    if v["det"] is not None and v["speech_sentences"]: A[int(k)]=(v["det"],"deterministic: "+v["det_reason"])
for x in json.load(open("elig/judge_output.json")): A[x["id"]]=(x["full"],"judge")
B={}
for i in (1,2,3):
    for x in json.load(open(f"elig/verify_output_{i}.json")): B[x["id"]]=(x["full"],x["sentence"])
T={x["id"]:x for x in json.load(open("elig/tiebreak_output.json"))}
rows=[];elig={}
for k,v in m.items():
    k=int(k); d={"id":k,"title":v["title"],"transcript":v["transcript"],"asset_description":v["asset_description"]}
    if v["media_type"]=="video":
        ss=sd[str(k)]["speech_sentences"] if v["transcript"] else None
        d["speech_sentences"]=ss
        if ss:
            a=A[k][0]; b=B[k][0]
            if a==b: e=a; src="agree"
            else: e=T[k]["full"]; src="tiebreak"
        else: e=False; src="no speech" if v["transcript"] else "no transcript"
        d["listening_eligible"]=e; d["speaking_eligible"]=e
        elig[k]={"eligible":e,"source":src,"first_path":A.get(k,(None,""))[1],"verifier_sentence":B.get(k,(None,None))[1]}
    else:
        d["speech_sentences"]=None; d["listening_eligible"]=None; d["speaking_eligible"]=None
    if any(d[f] is not None for f in ("transcript","asset_description","speech_sentences","listening_eligible")):
        rows.append(d)
rows.sort(key=lambda r:r["id"])
json.dump(rows,open("payload.json","w"),ensure_ascii=False)
json.dump(elig,open("eligibility_final.json","w"),indent=0)
import collections
print(len(rows), collections.Counter((e["eligible"],e["source"]) for e in elig.values()))
