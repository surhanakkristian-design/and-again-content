import json
p='tr/b020/es.json'; d=json.load(open(p))
fixes=[
('5255','nouns',1,'un juez','una jueza','the judge is a woman (her/she)'),
('5255','answer',None,'Está mirando hacia arriba al juez.','Está alzando la vista hacia la jueza.','female judge; "mirar hacia arriba al" unidiomatic'),
('5265','phrases',2,'mirar hacia arriba al barco','alzar la vista hacia el barco','"mirar hacia arriba al barco" unidiomatic'),
('5280','phrases',1,'mirar hacia arriba a los carteles','alzar la vista hacia los carteles','"mirar hacia arriba a" + thing unidiomatic'),
('5337','phrases',1,'mirar hacia arriba al techo','alzar la vista hacia el techo','unidiomatic; align with answer'),
('5337','answer',None,'Está mirando hacia arriba el techo de cristal.','Está alzando la vista hacia el techo de cristal.','same wording as the phrase'),
('5297','phrases',2,'salpicar el agua turquesa','chapotear en el agua turquesa','"salpicar el agua" = sprinkle water onto; splash in the water = chapotear en'),
('5298','phrases',1,'alcanzar otro frasco','alargar la mano hacia otro frasco','reach for = alargar la mano hacia; alcanzar = get/reach'),
('5304','phrases',2,'echar agua en la pila','echar agua en el fregadero','same thing as noun "un fregadero" in this video'),
('5312','nouns',1,'unas pinzas','pinzas','English bare plural -> bare noun per brief'),
('5317','phrases',0,'arremolinar su falda de volantes','hacer girar su falda de volantes','"arremolinar" transitive is unnatural'),
('5317','answer',None,'Está arremolinando su falda de volantes.','Está haciendo girar su falda de volantes.','same wording as the phrase'),
('5327','phrases',1,'sujetar un peine de peinado','sujetar un peine de peluquería','"peine de peinado" redundant/unnatural'),
]
out=[]
for k,f,i,b,a,w in fixes:
    if i is None:
        assert d[k][f]==b,(k,f,d[k][f]); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,d[k][f][i]); d[k][f][i]=a
    out.append(f'- {k} {f}{"" if i is None else "["+str(i)+"]"}: "{b}" -> "{a}" ({w})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('tr/b020/verify_es.md','w').write(f"# verify es b020\n\nTexts checked: {n} (100 videos)\n\n## Fixes ({len(fixes)})\n"+"\n".join(out)+"""

## Doubts left unchanged
- 5232 "accionar un winche": nautical "winche" accepted; "manivela" variants possible.
- 5232 "a yacht" -> "un velero": classic sailing boat, velero fits the clip better than yate.
- 5265 "conducir una barca pequeña": motorboat, "lancha" also possible.
- 5307 "floorboards" -> "tarima": acceptable; "tablas del suelo" alternative.
- 5324 "una sartén": large steel pan with sauce could also be "una olla"; kept.
- 5339 "un asiento del conductor": literal dictionary form, slightly stiff.
""")
print(len(fixes),n)
