import json
p='fr.json'; d=json.load(open(p))
fixes=[
('7083','nouns',1,'une gouttière','un tuyau de descente'),
('7089','answer',None,"L'éponge éléphant grossit.","L'éponge éléphant gonfle."),
('7101','nouns',0,'de la restauration rapide','du fast-food'),
('7101','answer',None,'Elle tient un sac de restauration rapide.','Elle tient un sac de fast-food.'),
('7105','answer',None,'Il relève le menton.','Le mannequin relève le menton.'),
('7108','question',None,'Que fait la femme du dessus ?','Que fait la femme en haut ?'),
('7110','nouns',2,'une guirlande lumineuse','des guirlandes lumineuses'),
('7161','nouns',0,'une guirlande lumineuse','des guirlandes lumineuses'),
('7169','nouns',0,'une guirlande lumineuse','des guirlandes lumineuses'),
('7162','nouns',3,'un plancher','des lattes de plancher'),
('7135','phrases',2,"s'écraser dans les pastèques","s'écraser contre les pastèques"),
('7138','question',None,'Que fait la vague énorme ?',"Que fait l'énorme vague ?"),
('7155','question',None,'Que fait la femme en argent ?','Que fait la femme en robe argentée ?'),
('7191','answer',None,'Elle attrape un café au passage à la cabane.','Elle attrape au passage un café à la cabane.'),
]
for i,f,k,a,b in fixes:
    cur=d[i][f] if k is None else d[i][f][k]
    assert cur==a,(i,f,cur)
    if k is None: d[i][f]=b
    else: d[i][f][k]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
s=json.load(open('source.json'));print(sum(3+len(v['nouns'])+2 for v in s.values()), len(s))
