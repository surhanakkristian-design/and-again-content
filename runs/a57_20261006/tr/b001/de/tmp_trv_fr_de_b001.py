import json
p='tr/b001/de/fr.json'; d=json.load(open(p))
fx=[('82','phrases',2,'ramper dans la ruche','se glisser dans la ruche'),
('82','recall',2,'ramper dans la ruche','se glisser dans la ruche'),
('4941','phrases',0,'monter à une échelle','grimper à une échelle'),
('4941','recall',0,'monter à une échelle','grimper à une échelle'),
('819','phrases',1,'venir sous le parapluie','se mettre sous le parapluie'),
('819','recall',1,'venir sous le parapluie','se mettre sous le parapluie'),
('741','phrases',0,'se plier sous le vent','se courber sous le vent'),
('741','recall',0,'se plier sous le vent','se courber sous le vent'),
('741','answer',None,'Il se plie sous la tempête.','Il se courbe dans la tempête.'),
('741','recall',3,'se plie sous la tempête','se courbe dans la tempête'),
('5660','phrases',1,'éclairer le mur de la maison','éclairer la façade'),
('5660','recall',1,'éclairer le mur de la maison','éclairer la façade')]
for k,f,i,a,b in fx:
  if i is None: assert d[k][f]==a; d[k][f]=b
  else: assert d[k][f][i]==a,(k,f,i,d[k][f][i]); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
