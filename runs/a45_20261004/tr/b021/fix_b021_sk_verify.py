import json
p='sk.json'; d=json.load(open(p))
fx=[('5351','answer',None,'S úžasom hľadí nahor na svetelné reťaze.','Hľadí nahor na svetelné reťaze.'),
('5352','answer',None,'Frustrovane sa chytá za hlavu.','Od frustrácie sa chytá za hlavu.'),
('5396','phrases',0,'skloniť sa nad mapu','skloniť sa nad mapou'),
('5409','question',None,'Čo je mladá žena?','Čo práve je mladá žena?'),
('5409','answer',None,'Je červené jablko.','Práve je červené jablko.'),
('5412','phrases',1,'niesť zelenú plátennú tašku','niesť zelenú plátenú tašku'),
('5448','phrases',2,'zdvíhať pochodeň','držať zdvihnutú pochodeň'),
('5471','question',None,'Kam si muž opiera ruky?','O čo si muž opiera ruky?')]
for k,f,i,a,b in fx:
    if i is None:
        assert d[k][f]==a,(k,f); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
