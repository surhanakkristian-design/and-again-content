import json
p='cz.json'; d=json.load(open(p))
fixes=[
("7214","phrases",0,"rozhodit ruce","rozpřáhnout ruce"),
("7214","answer",None,"Rozhazuje ruce.","Rozpřahuje ruce."),
("7217","answer",None,"Nabírá mu štědrou porci.","Nakládá mu štědrou porci."),
("7220","phrases",0,"rozvalit se na ledě","rozplácnout se na ledě"),
("7220","answer",None,"Rozvaluje se na ledě.","Leží rozpláclý na ledě."),
("7255","phrases",1,"kousat hůl","kousat do hole"),
("7262","phrases",1,"sát od matky","sát u matky"),
("7262","answer",None,"Saje od matky.","Saje u matky."),
("7293","phrases",2,"zůstat dokořán otevřená","být dokořán"),
("7298","phrases",2,"ukazovat perem","ukazovat propiskou"),
]
for k,f,i,a,b in fixes:
    if i is None:
        assert d[k][f]==a,(k,f); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,i); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
