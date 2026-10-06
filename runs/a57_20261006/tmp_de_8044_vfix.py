import json
def L(i): return json.load(open(f"content/de/{i}.json"))
def S(i,d): json.dump(d,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
d=L(8044)
r=d["recall"][3]; g=[p for p in r["parts"] if p.get("gap")][0]
assert g["text"]=="wild"; g["accept"]=["wild","hoch"]; S(8044,d)
d=L(7782)
d["answer"]="Er streckt seinen Rüssel immer näher zur Banane.".split()
d["recall"][3]={"from":"answer","parts":[{"text":"streckt seinen Rüssel immer"},{"text":"näher","gap":True,"accept":["näher"]},{"text":"zur Banane"}]}
S(7782,d)
d=L(4)
d["taps"][0]["phrase"]="kalten Kaffee trinken"
d["answer"]="Sie trinkt kalten Kaffee.".split()
d["recall"][0]={"from":"taps","parts":[{"text":"kalten Kaffee"},{"text":"trinken","gap":True,"accept":["trinken"]}]}
d["recall"][3]={"from":"answer","parts":[{"text":"trinkt kalten"},{"text":"Kaffee","gap":True,"accept":["Kaffee","Eiskaffee"]}]}
S(4,d)
