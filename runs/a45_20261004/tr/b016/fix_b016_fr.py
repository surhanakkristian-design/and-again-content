import json
p='tr/b016/fr.json'; d=json.load(open(p))
fixes=[('4753','phrases',0,'croiser les bras fermement','croiser fermement les bras','adverb placement: natural French order'),
('4753','question',None,"Qu'est-ce que l'homme barbu lui offre ?","Qu'offre l'homme barbu ?",'English has no object pronoun; lui was added'),
('4778','answer',None,"Elle montre du doigt, en haut, l'horloge à coucou sculptée.","Elle montre du doigt l'horloge à coucou sculptée, en haut.",'awkward inserted adverbial; natural order'),
('4796','question',None,'Que fait tenir le garçon en équilibre ?',"Qu'est-ce que le garçon fait tenir en équilibre ?",'inverted order with causative faire is ambiguous/unnatural'),
('4812','phrases',0,'suspendre une chemise soigneusement','suspendre soigneusement une chemise','adverb placement: natural French order'),
('4815','phrases',1,'plisser le visage','faire la grimace','"plisser le visage" is not idiomatic for "screw up her face"'),
('4832','phrases',2,'suivre une trace de pas','suivre des traces de pas','a trail of footprints = des traces de pas (one "trace de pas" is a single footprint)'),
('4860','answer',None,"Elle fixe l'eau pétillante.","Elle fixe l'eau effervescente.",'"eau pétillante" = sparkling water; fizzing from a tablet = effervescente')]
for k,f,i,b,a,w in fixes:
    if i is None:
        assert d[k][f]==b,(k,f); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,i); d[k][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
lines=['# verify fr b016','','Texts checked: %d'%sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values()),'','## Fixes']
for k,f,i,b,a,w in fixes: lines.append(f'- {k} {f}{"" if i is None else "["+str(i)+"]"}: {b} -> {a} ({w})')
lines+=['','## Doubts left unchanged',
'- 4831 phrases[0] "balancer une batte en aluminium": swing a bat; acceptable but slightly loose, no clearly better infinitive entry.',
'- 4855/4861 nouns "des écouteurs" for headphones: over-ear would be "un casque", kept plural per the plural rule.',
'- 4818 answer "Elles essaient...": agrees with "les trois personnes" (fem.), mixed group; grammatically correct.',
'- 4851 phrases[1] "avoir l\'air très surpris": agreement with "air"; "surprise" also possible for the woman.',
'- 4812 nouns "une chemise orange": the clip shows a blue shirt; mirrors the English source.']
open('tr/b016/verify_fr.md','w').write('\n'.join(lines)+'\n')
