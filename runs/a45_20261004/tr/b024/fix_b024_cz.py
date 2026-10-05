import json
p='cz.json'; d=json.load(open(p))
fixes=[
('6838','phrases',2,'houpat kadidelnicí','mávat kadidelnicí'),
('6838','answer',None,'Houpe kadidelnicí.','Mává kadidelnicí.'),
('6854','phrases',1,'plout vedle mola','pohupovat se vedle mola'),
('6861','phrases',2,'držet zvednutou sklenici na šampaňské','zvedat sklenici na šampaňské'),
('6870','phrases',0,'usadit se na střeše auta','trůnit na střeše auta'),
('6870','nouns',3,'gumáky','gumové holínky'),
('6885','phrases',0,'chytat se za zadek','sahat si na zadek'),
('6886','phrases',0,'sbíhat skoky z duny','sbíhat z duny dlouhými skoky'),
('6886','answer',None,'Sbíhá skoky z písečné duny.','Sbíhá z písečné duny dlouhými skoky.'),
('6896','phrases',1,'sahat po volném laně','sahat po volném vodítku'),
('6905','nouns',1,'kelímek','tavicí kelímek'),
('6906','phrases',1,'lhostejně ukazovat na polici','ledabyle ukazovat na polici'),
('6928','phrases',0,'smát se za dlaní','smát se do dlaně'),
('6928','answer',None,'Směje se za dlaní.','Směje se do dlaně.'),
('6939','phrases',1,'upustit zlaté sako na zem','upustit zlaté sako'),
('6942','phrases',2,'překlenout úzký kanál','překlenovat úzký kanál'),
('6945','phrases',0,'sundávat kovový prstenec','sundávat kovový kroužek'),
('6945','answer',None,'Sundává kovový prstenec ze šarloty.','Sundává kovový kroužek ze šarloty.'),
]
for k,f,i,a,b in fixes:
    if i is None:
        assert d[k][f]==a,(k,f,d[k][f]); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,i,d[k][f][i]); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
