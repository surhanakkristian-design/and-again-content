import json
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/de/tr.json'
d=json.load(open(P))
fixes=[("596","answer",None,"Sarılı kadın koşucu yarışı kazanıyor.","Sarı giyen kadın koşucu yarışı kazanıyor."),
("278","phrases",0,"ağaçların tepesinin üzerinden doğmak","ağaç tepelerinin üzerinden doğmak"),
("278","recall",0,"ağaçların tepesinin üzerinden doğmak","ağaç tepelerinin üzerinden doğmak"),
("5712","phrases",1,"bir kâğıt yaprağını düşürmek","bir kâğıt yaprağı düşürmek"),
("5712","recall",1,"bir kâğıt yaprağını düşürmek","bir kâğıt yaprağı düşürmek"),
("4156","nouns",0,"çalı çit","çalı çiti"),
("6820","phrases",1,"yetişkin hayvanın yanında paytak paytak yürümek","yetişkin hayvanın yanında tıpış tıpış yürümek"),
("6820","recall",1,"yetişkin hayvanın yanında paytak paytak yürümek","yetişkin hayvanın yanında tıpış tıpış yürümek"),
("7813","nouns",0,"şemsiyeler","güneş şemsiyeleri"),
("4920","nouns",3,"yükseltilmiş bahçe yatağı","yükseltilmiş tarh")]
for i,f,k,a,b in fixes:
    if k is None: assert d[i][f]==a,(i,f); d[i][f]=b
    else: assert d[i][f][k]==a,(i,f,k); d[i][f][k]=b
json.dump(d,open(P,'w'),ensure_ascii=False,indent=1)
print('ok')
