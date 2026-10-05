import json
p='hu.json'; d=json.load(open(p))
fixes=[
('4989','phrases',2,'a domb alatt állni','a domb lábánál állni','"a domb alatt" reads as underneath the hill; the tent stands at the foot of the ridge'),
('5008','phrases',2,'tárva-nyitva kitárulni','szélesre kitárulni','"tárva-nyitva kitárulni" is redundant'),
('5032','phrases',1,'hó van a tetején','hó van a tetejükön','target is plural (the snowy mountains): possessive must agree'),
('5034','phrases',1,'az asztalra folyni','kifolyni az asztalra','"to leak" needs the ki- prefix (leaking out), not just flowing'),
('5042','answer',None,'Óvatosan leereszkedik egy padra.','Leereszkedik egy padra.','"óvatosan" (carefully) is not in the English'),
('5050','phrases',0,'rémülten levegő után kapkodni','rémülten levegő után kapni','"kapkodni" = panting repeatedly; a gasp is a single "levegő után kapni"'),
('5061','phrases',2,'átsiklani a vízen','siklani a vízben','sharks glide through (inside) the water; "átsiklani a vízen" means skimming across the surface'),
('5073','nouns',3,'fedő','kupak','the lid is the screw cap of the medicine bottle: "kupak"; "fedő" is a pot lid'),
('5079','phrases',2,'átlógni az utca fölött','az utca fölött lógni','"átlógni" is unidiomatic; banners hang across/over the street'),
('5098','phrases',0,'filmezni magát','lefilmezni magát','filming oneself takes the perfective le- prefix in Hungarian'),
]
for k,f,i,b,a,w in fixes:
    if i is None:
        assert d[k][f]==b,(k,f); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,i); d[k][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
with open('verify_hu.md','w') as o:
    o.write(f'# verify hu b018\n\nTexts checked: {n} ({len(d)} videos)\n\n## Fixes\n')
    for k,f,i,b,a,w in fixes:
        o.write(f'- {k} {f}{"" if i is None else "["+str(i)+"]"}: {b} -> {a} ({w})\n')
    o.write('''
## Doubts left unchanged
- 4977/5039/5045/5078/5085/5091 "to have ..." phrases kept as "... van" (e.g. "hosszú farka van"): Hungarian has no natural infinitive for possession; "rendelkezni" would be stilted.
- 5089 "to have a sore knee" -> "fáj a térde": same reason.
- 4981 "győzedelmesen ökölbe szorítani a kezét": "győzedelmesen" carries the meaning of a fist pump; no single verb.
- 4982 "to sit on a bench" -> "leülni egy padra" (he ends up sitting; "egy padon ülni" also possible).
- 5068 question "Mit csinál a menyasszony és a vőlegény?" singular verb with "és" compound subject is standard; plural also acceptable.
- 5008 "kulccsal kinyitni" renders "unlock"; "kulccsal" makes the sense explicit, not an addition of meaning.
''')
print(n)
