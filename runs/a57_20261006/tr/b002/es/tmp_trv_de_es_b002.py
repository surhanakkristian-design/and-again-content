import json
p='es/de.json'; d=json.load(open(p))
fix=[('484','phrases',1,'kurz davor sein, hinzufallen'),('484','recall',1,'kurz davor sein, hinzufallen'),
('406','answer',None,'Er hämmert das glühende Eisen auf dem Amboss.'),('406','recall',3,'Er hämmert das glühende Eisen auf dem Amboss'),
('8036','answer',None,'Der Flamingo füllt fast das ganze Zimmer aus.'),('8036','recall',3,'füllt fast das ganze Zimmer aus'),
('5636','phrases',0,'sich über die Theke beugen'),('5636','recall',0,'sich über die Theke beugen'),
('7997','phrases',2,'auf hohen Absätzen tanzen'),('7997','recall',2,'auf hohen Absätzen tanzen'),
('5417','question',None,'Was macht die junge Frau am Ende?'),
('4918','phrases',1,'mit den Tüten nicht zurechtkommen'),('4918','recall',1,'mit den Tüten nicht zurechtkommen'),
('7200','phrases',1,'den Piloten in die Luft heben'),('7200','recall',1,'den Piloten in die Luft heben'),
('376','nouns',1,'die Felswand')]
for k,f,i,v in fix:
    if i is None: print(k,f,d[k][f],'->',v); d[k][f]=v
    else: print(k,f,i,d[k][f][i],'->',v); d[k][f][i]=v
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
