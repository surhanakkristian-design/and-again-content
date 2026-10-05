import json
p='tr/b017/hu.json'; d=json.load(open(p))
fixes=[
("4865","answer",None,"Egy finom rózsaszín rózsát fényképez.","Egy kecses rózsaszín rózsát fényképez."),
("4884","phrases",1,"szélesre tátani a száját","nagyra tátani a száját"),
("4895","nouns",2,"a talaj","a föld"),
("4900","phrases",2,"egy kupaccá összeomlani","kupacba omlani"),
("4900","answer",None,"A rakás egy kupaccá omlik össze.","A rakás kupacba omlik."),
("4902","phrases",2,"nagy csobbanással visszazuhanni","visszazuhanni"),
("4906","phrases",1,"le lenni súlyozva","lesúlyozva lenni"),
("4925","nouns",0,"gyümölcsleves doboz","gyümölcslés doboz"),
("4932","nouns",0,"lapos sapka","simlis sapka"),
("4956","phrases",2,"lemenni a város fölött","lenyugodni a város fölött"),
("4964","phrases",0,"megetetni egy kanállal","adni neki egy kanálnyit"),
]
for vid,f,i,b,a in fixes:
    if i is None: assert d[vid][f]==b,(vid,f); d[vid][f]=a
    else: assert d[vid][f][i]==b,(vid,f,i); d[vid][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print(len(fixes))
