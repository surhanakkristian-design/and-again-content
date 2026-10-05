import json
p='hu.json'; d=json.load(open(p))
fixes=[
("7073","phrases",1,"letérdelni egy párnázott takaróra","egy párnázott takarón térdelni"),
("7073","phrases",2,"megragadni a fenti állványzatot","megragadni a feje fölötti állványzatot"),
("7079","nouns",1,"szöges bádogdoboz","szögekkel teli bádogdoboz"),
("7083","nouns",1,"ereszcsatorna","lefolyócső"),
("7092","phrases",2,"elolvadni a tűző napon","olvadni a tűző napon"),
("7097","nouns",3,"fültisztító pálcikák","vattapálcikák"),
("7097","answer",None,"Egy fültisztító pálcikával dörzsöli a mellszobrot.","Egy vattapálcikával dörzsöli a mellszobrot."),
("7107","phrases",2,"szorosan lehunyni a szemét","erősen összeszorítani a szemét"),
("7111","nouns",1,"vezetőbíró","ringbíró"),
("7111","question",None,"Mit csinál a vezetőbíró?","Mit csinál a ringbíró?"),
("7123","phrases",1,"simára igazítani a húst","kisimítani a húst"),
("7123","answer",None,"Simára igazítja az élénk narancssárga húst.","Kisimítja az élénk narancssárga húst."),
("7184","question",None,"Mit csinál a férfi és a nő?","Mit csinálnak a férfi és a nő?"),
("7192","answer",None,"Egy diplomát tart a feje fölé.","Egy diplomát tart a feje fölött."),
]
for vid,f,i,b,a in fixes:
    if i is None:
        assert d[vid][f]==b,(vid,f); d[vid][f]=a
    else:
        assert d[vid][f][i]==b,(vid,f,i); d[vid][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
