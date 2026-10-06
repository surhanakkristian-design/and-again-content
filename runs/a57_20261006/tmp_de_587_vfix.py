import json
def fix(i, row, word, fn):
    p=f"content/de/{i}.json"; d=json.load(open(p))
    for part in d["recall"][row]["parts"]:
        if part.get("gap"): assert part["text"]==word; fn(part["accept"])
    json.dump(d,open(p,"w"),ensure_ascii=False,indent=2)
fix(587,1,"Treffer",lambda a:a.remove("Tor"))
fix(7069,2,"beobachten",lambda a:a.append("verfolgen"))
fix(5626,3,"Orangen",lambda a:a.append("Apfelsinen"))
fix(7929,1,"Fäuste",lambda a:a.append("Arme"))
