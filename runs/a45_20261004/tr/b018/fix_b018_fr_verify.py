import json
f=json.load(open('fr.json'))
fixes=[
("4973","phrases",0,"se pencher sur les épices","se pencher au-dessus des épices","'se pencher sur' = to study; physical leaning over is 'au-dessus de'"),
("4980","phrases",2,"écarter grand les bras","écarter largement les bras","'écarter grand' is not idiomatic"),
("5061","phrases",1,"écarter grand les bras","écarter largement les bras","'écarter grand' is not idiomatic"),
("5061","phrases",0,"monter par un escalator","monter en escalator","idiomatic preposition"),
("4985","nouns",2,"un cordon","un tour de cou","a badge lanyard is 'un tour de cou'"),
("5008","nouns",2,"un cordon","un tour de cou","a badge lanyard is 'un tour de cou'"),
("4991","phrases",2,"montrer une chemise bien lisse","montrer une chemise lisse","'bien' added nothing in the English"),
("5008","phrases",0,"ouvrir une boîte aux lettres en laiton","déverrouiller une boîte aux lettres en laiton","unlock, not open"),
("5008","answer",None,"Elle ouvre une boîte aux lettres en laiton.","Elle déverrouille une boîte aux lettres en laiton.","unlock, not open; same verb as phrase"),
("5026","phrases",2,"fixer les yeux écarquillés","regarder les yeux écarquillés","'fixer' needs an object; intransitive stare"),
("5028","phrases",0,"porter des livres lourds","porter de lourds livres","natural adjective position"),
("5028","answer",None,"Il porte des livres lourds.","Il porte de lourds livres.","natural adjective position; same as phrase"),
("5030","phrases",0,"porter une haute bannière","porter une grande bannière","'haute bannière' unidiomatic"),
("5030","phrases",2,"courir devant les tambours","passer devant les tambours en courant","run past, not run ahead of"),
("5083","phrases",2,"se lécher la pâte sur le doigt","lécher la pâte sur son doigt","awkward reflexive construction"),
("5089","phrases",1,"s'envoler dans les airs","monter dans les airs","'s'envoler' = fly away; the baby is lifted up"),
]
out=[]
for i,fld,idx,b,a,why in fixes:
    if idx is None:
        assert f[i][fld]==b,(i,fld); f[i][fld]=a
    else:
        assert f[i][fld][idx]==b,(i,fld,idx); f[i][fld][idx]=a
    out.append(f"- {i}, {fld}{'' if idx is None else '['+str(idx)+']'}: {b} -> {a} ({why})")
json.dump(f,open('fr.json','w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in f.values())
doubts="""- 4981 phrases[2] "brandir le poing" (pump her fist): acceptable, could read as threatening; left.
- 5035 nouns[2] "un pantalon" for "trousers": French singular is the dictionary equivalent of one pair; left.
- 5073 nouns[0] "un médicament" for mass "medicine": "du médicament" is unnatural; left.
- 5086 nouns[0] "des lumières du plafond": "des plafonniers" more dictionary-like, kept for consistency with the phrase.
- 5042 answer "se laisse tomber" for "lowering herself": kept same verb as the phrase "sink onto a bench".
- 4993 phrases[0] "pagayer dans un bateau rouge": slightly loose but natural; left.
"""
open('verify_fr.md','w').write(f"# verify fr b018\n\nTexts checked: {n} (100 videos)\n\n## Fixes ({len(out)})\n"+"\n".join(out)+"\n\n## Doubts left unchanged\n"+doubts)
print(n,len(out))
