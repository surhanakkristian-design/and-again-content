import json
def add(i, row, word):
    p=f"content/es/{i}.json"; d=json.load(open(p))
    for part in d["recall"][row]["parts"]:
        if part.get("gap"):
            if word not in part["accept"]: part["accept"].append(word)
    json.dump(d, open(p,"w"), ensure_ascii=False, indent=1); open(p,"a").write("\n") if False else None
add(7236,3,"chocando")
add(4809,0,"cesta")
add(54,0,"introducir")
