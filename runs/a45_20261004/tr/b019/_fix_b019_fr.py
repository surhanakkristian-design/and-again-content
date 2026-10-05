import json
p='tr/b019/fr.json'; d=json.load(open(p))
fx=[('5103','phrases',0,'toucher son cou','se toucher le cou'),
('5123','phrases',2,'se prendre la tête','se tenir la tête'),
('5123','answer',None,'Il se prend la tête à deux mains.','Il se tient la tête à deux mains.'),
('5127','phrases',0,'emballer ses vêtements','ranger ses vêtements'),
('5140','phrases',2,'exhiber son passeport','montrer fièrement son passeport'),
('5177','phrases',2,'être alignés en rang','être alignés'),
('5179','phrases',2,"luire d'orange à l'intérieur","briller d'une lueur orange à l'intérieur"),
('5193','phrases',0,'gratter son bras qui démange','se gratter le bras qui démange'),
('5203','phrases',0,"ouvrir la marche vers l'intérieur",'entrer le premier'),
('5207','phrases',1,"boire de l'eau à grandes gorgées à la bouteille","boire de grandes gorgées d'eau à la bouteille"),
('5209','phrases',2,"être allongé à plat dans l'herbe","être allongé de tout son long dans l'herbe")]
for k,f,i,a,b in fx:
  if i is None: assert d[k][f]==a; d[k][f]=b
  else: assert d[k][f][i]==a; d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
