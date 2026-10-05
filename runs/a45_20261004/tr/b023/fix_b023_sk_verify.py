import json
f='sk.json'; d=json.load(open(f))
fx=[('5608','nouns',1,'odrazový mostík','skokanský mostík'),
('5633','phrases',0,'prehodiť cez neho bundu','prehodiť cezeň bundu'),
('5633','answer',None,'Prehadzuje cez neho bundu.','Prehadzuje cezeň bundu.'),
('5655','phrases',1,'vybuchnúť smiechom','vybuchnúť do smiechu'),
('5680','phrases',2,'kolísať sa po stole','kolembať sa po stole'),
('5716','phrases',1,'kolísať sa po brehu','kolembať sa po brehu')]
for i,fl,ix,a,b in fx:
    if ix is None: assert d[i][fl]==a; d[i][fl]=b
    else: assert d[i][fl][ix]==a; d[i][fl][ix]=b
json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
