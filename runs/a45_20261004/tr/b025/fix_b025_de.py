import json
p='tr/b025/de.json'; d=json.load(open(p))
fx=[('6951','phrases',2,'ihre Haare berühren','sich an die Haare fassen'),
('7042','phrases',2,'ihre Haare berühren','sich an die Haare fassen'),
('6968','phrases',1,'seine Hand hochhalten','die Hand hochhalten'),
('6990','phrases',1,'seinen Rüssel ausstrecken','den Rüssel ausstrecken'),
('6994','phrases',0,'eine Rolle Baumwolle werfen','eine Rolle Baumwollstoff werfen'),
('6994','nouns',0,'Baumwolle','Baumwollstoff'),
('6994','answer',None,'Er wirft eine Rolle Baumwolle.','Er wirft eine Rolle Baumwollstoff.')]
for i,f,k,a,b in fx:
    if k is None: assert d[i][f]==a; d[i][f]=b
    else: assert d[i][f][k]==a; d[i][f][k]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
