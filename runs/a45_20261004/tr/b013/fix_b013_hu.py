import json
f='hu.json'; d=json.load(open(f))
fixes=[
("4281","phrases",2,"felmászni a fára","felmászni a fadarabra"),
("4281","nouns",2,"fa","fadarab"),
("4285","phrases",0,"egy nyakkendőt felkötni","nyakkendőt kötni"),
("4291","phrases",2,"hideg levegőt fújni","hűvös levegőt fújni"),
("4291","answer",None,"Hideg levegőt fúj a férfira.","Hűvös levegőt fúj a férfira."),
("4336","phrases",1,"felszerelni egy falábat","felszerelni egy fából készült lábat"),
("4340","phrases",2,"elkapni egy szem sült krumplit","elcsenni egy szem sült krumplit"),
("4377","phrases",2,"tárva-nyitva kicsapódni","szélesre kitárulni"),
("4398","phrases",0,"tágra nyitni a száját","nagyra kinyitni a száját"),
("4432","phrases",1,"elvitelre kért kávét vinni","elviteles kávét vinni"),
]
for k,fld,i,a,b in fixes:
    if i is None:
        assert d[k][fld]==a,(k,fld); d[k][fld]=b
    else:
        assert d[k][fld][i]==a,(k,fld,i); d[k][fld][i]=b
json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
