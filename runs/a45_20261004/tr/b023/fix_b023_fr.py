import json
p='tr/b023/fr.json'; d=json.load(open(p))
fixes=[
('5607','phrases',1,"partir en fumée","s'embraser","'partir en fumée' = go up in smoke (fail); the cart literally burns"),
('5613','phrases',1,"montrer quelque chose par-dessus son épaule","pointer du doigt par-dessus son épaule","'quelque chose' added, not in English"),
('5615','phrases',1,"cuire des nouilles dans une poêle","faire cuire des nouilles dans une poêle","transitive cooking = faire cuire; matches the answer"),
('5617','phrases',1,"tenir un maillet en bois","tenir un marteau en bois","same word as noun 'un marteau' in this video"),
('5622','phrases',2,"tirer sur son bras","le tirer par le bras","natural French for pulling someone's arm"),
('5628','phrases',2,"pendre du plafond","pendre au plafond","French: pendre à, not de (anglicism)"),
('5635','phrases',2,"pendre du plafond peint","pendre au plafond peint","pendre à, not de"),
('5646','phrases',2,"pendre du toit de chaume","pendre au toit de chaume","pendre à, not de"),
('5662','phrases',2,"essuyer la sauce sur son visage","essuyer la sauce de son visage","wipe off = enlever de; 'sur' reads as wiping onto"),
('5667','phrases',1,"faire deux pouces vers le bas","pointer les deux pouces vers le bas","'faire deux pouces' is not idiomatic"),
('5672','answer',None,"Il dort sur son bureau.","Il dort à son bureau.","at his desk = à son bureau; 'sur' = lying on top of it"),
('5677','nouns',2,"une gouttière","une rigole","bowling gutter is 'rigole'; gouttière = roof gutter (wrong sense)"),
('5680','phrases',1,"être agenouillé à la table à thé","être agenouillé devant la table à thé","kneel at a table = devant"),
('5683','phrases',2,"être à court de sable","se vider","'être à court de' is for people/supplies; an hourglass empties"),
('6814','phrases',1,"tenir son chapeau","retenir son chapeau","hold on (against wind) = retenir"),
('6816','phrases',0,"se protéger les yeux du soleil","se protéger les yeux de la main","stage scene, no sun; 'du soleil' added"),
('6819','phrases',2,"flotter au vent","claquer au vent","flap = claquer (flutter = flotter, used elsewhere)"),
]
log=[]
for vid,f,i,b,a,why in fixes:
    cur=d[vid][f] if i is None else d[vid][f][i]
    assert cur==b,(vid,cur)
    if i is None: d[vid][f]=a
    else: d[vid][f][i]=a
    log.append(f"- {vid} {f}{'' if i is None else '['+str(i)+']'}: {b} -> {a} ({why})")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('tr/b023/fix_b023_fr.log','w').write("\n".join(log))
