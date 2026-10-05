import json
p='/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/tr/b001/cz.json'
d=json.load(open(p))
F=[
('4658','phrases',1,'jít ulicí dolů','jít po ulici','"down the street" = along the street, not downhill'),
('4658','phrases',2,'mít tmavé sluneční brýle','mít nasazené tmavé sluneční brýle','"mít" alone = to have/own; wear needs "mít nasazené"'),
('852','phrases',2,'běžet přes restauraci','běžet restaurací','"přes" = across/over; through a room is the instrumental'),
('646','phrases',1,'vycházet ze sklenice','valit se ze sklenice','foam does not "vycházet" (calque); it surges out'),
('4243','question',None,'Co dělá kočka?','Co připravuje kočka?','"Co dělá" reads as "what is it doing"; the question asks what it is making'),
('4243','answer',None,'Dělá hot dog.','Připravuje hot dog.','same verb as the corrected question'),
('792','phrases',1,'vycházet z tuby','vytékat z tuby','toothpaste does not "vycházet" (calque of come out)'),
('38','phrases',2,'letět na oblohu','letět k obloze','"na oblohu" is not idiomatic for flying up into the sky'),
('5062','phrases',0,'jít přes kancelář','jít kanceláří','through a room = instrumental, not "přes"'),
('30','phrases',0,'otáčet stránky','obracet stránky','standard collocation for turning pages'),
('30','answer',None,'Otáčí stránky učebnice.','Obrací stránky učebnice.','same collocation as the phrase'),
('868','phrases',0,'být větší a větší','být čím dál větší','natural Czech for "get bigger and bigger"'),
('291','answer',None,'Běží přes pole.','Běží polem.','she runs through the field along a path, not across it'),
('741','phrases',1,'kutálet se ulicí dolů','kutálet se po ulici','"down the street" = along the street; natural wording'),
]
n=sum(3+len(v['nouns'])+2 for v in d.values())
L=[f'# verify b001 cz\n\nTexts checked: {n} ({len(d)} videos)\n\n## Fixes ({len(F)})\n']
for i,f,k,a,b,w in F:
    cur=d[i][f] if k is None else d[i][f][k]
    assert cur==a,(i,f,cur)
    if k is None: d[i][f]=b
    else: d[i][f][k]=b
    L.append(f'- {i} {f}{"" if k is None else "["+str(k)+"]"}: {a} -> {b} ({w})')
L.append('''
## Doubts left unchanged
- 339 phrases[0] + answer "jít ulicí dolů" / "Jde ulicí dolů.": may mean only "along the street"; kept because the question is "Kam jde dívka?" and needs a direction.
- 694 nouns[0] "rondon" for "a jacket": correct term for a chef's jacket but rare; "kuchařský kabátek" would be the plainer option.
- 775, 242, 800 "tleskat rukama": slightly pleonastic ("tleskat" suffices) but mirrors "clap his/her hands".
- 5468 "fotit si selfie": "dělat si selfie" is equally common.
- 5108 "loď" for the canoe ("a boat"): "loďka" would fit the picture better.
- 5215, 4603 "Jede na svém kole": "svém" is redundant in Czech but keeps "her/his bike".
- 122 "nákupní vozík" for the old woman's shopping trolley: follows the English "shopping cart".
- 694, 4243, 558 "držet ... nahoře" for "hold up": acceptable, "zvednout" would be an alternative.
''')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open(p.replace('cz.json','verify_cz.md'),'w').write('\n'.join(L))
print(n,len(F))
