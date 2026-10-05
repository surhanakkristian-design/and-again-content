import json
f='es.json'; d=json.load(open(f))
fixes=[
("5614","phrases",2,"caminar en la parte de atrás","caminar detrás","unnatural; 'walk at the back' = caminar detrás"),
("5617","phrases",1,"sostener un mazo de madera","sostener un martillo de madera","same thing must match noun 'un martillo'"),
("5623","nouns",0,"unos auriculares","auriculares","English bare plural -> bare plural in es"),
("5627","phrases",1,"bostezar mucho","bostezar con la boca muy abierta","'bostezar mucho' = yawn a lot, wrong sense"),
("5630","phrases",2,"bailar bajo una guirnalda de luces","bailar bajo guirnaldas de luces","English plural 'string lights' stays plural"),
("5640","nouns",2,"unas botas de montaña","botas de montaña","English bare plural -> bare plural in es"),
("5648","phrases",2,"llevar unas mallas negras","llevar mallas negras","English bare plural -> no article"),
("5654","answer",None,"Se siente amargada por su medalla de plata.","Se siente resentida por su medalla de plata.","'amargada' = embittered person in general; 'bitter about' = resentida por"),
("5655","nouns",3,"unas zapatillas de deporte","zapatillas de deporte","English bare plural -> bare plural in es"),
("5657","answer",None,"Está bendiciendo a la mujer en el barco.","Está bendiciendo a la mujer del barco.","'the woman on the boat' as identifier; 'en el barco' reads as where the blessing happens"),
("5667","phrases",1,"hacer un doble pulgar hacia abajo","poner los dos pulgares hacia abajo","calque; natural gesture phrase"),
("5670","nouns",0,"una guirnalda de luces","guirnaldas de luces","English bare plural 'string lights' -> bare plural"),
("5689","nouns",1,"unos auriculares","auriculares","English bare plural -> bare plural in es"),
("5701","phrases",0,"mostrar una pizarra","tender una pizarra","'hold out' = tender, not 'show'"),
("5705","phrases",0,"mostrar la llave de su coche","levantar la llave de su coche","'hold up' here = raise high, not 'show'"),
("6815","nouns",1,"unas gafas de protección","gafas de protección","English bare plural -> bare plural in es"),
("6823","phrases",2,"bloquear la estrecha calle","bloquear la calle estrecha","natural adjective position"),
("6829","nouns",3,"el letrero de una tienda","un letrero de tienda","English 'a shop sign' -> indefinite article on the head noun"),
]
lines=[]
for vid,field,i,b,a,why in fixes:
    cur=d[vid][field] if i is None else d[vid][field][i]
    assert cur==b,(vid,field,cur)
    if i is None: d[vid][field]=a
    else: d[vid][field][i]=a
    lines.append(f"- {vid}, {field}{'' if i is None else '['+str(i)+']'}: \"{b}\" -> \"{a}\" ({why})")
json.dump(d,open(f,'w'),ensure_ascii=False,indent=2)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('verify_es.md','w').write(f"""# Verify es, batch b023

Texts checked: {n} ({len(d)} videos)

## Fixes ({len(fixes)})
"""+"\n".join(lines)+"""

## Doubts left unchanged
- 5607 phrases[1] "ser pasto de las llamas": correct idiom for 'go up in flames'; plainer "arder en llamas" possible.
- 5613 phrases[2] "esforzarse bajo el peso": acceptable, slightly stiff.
- 5619 phrases[2] "saltear comida en una sartén": 'flip' rendered as sautéing with tossing; acceptable.
- 5641 "un paraguas dado la vuelta": colloquial; "vuelto del revés" also possible.
- 5685 nouns[0] "un público": grammatical, kept to match "ante el público" in the phrase.
- 5703 "atacar su helado": colloquial for 'dig into', kept.
""")
print(n)
