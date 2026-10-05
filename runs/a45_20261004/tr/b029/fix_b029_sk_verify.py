import json
p='sk.json'; d=json.load(open(p))
fixes=[
('7759','phrases',1,'zmoknúť do nitky','premoknúť do nitky'),
('7763','answer',None,'Drží žabu v rukách v rukaviciach.','Drží žabu v rukách s rukavicami.'),
('7765','phrases',0,'krájať svoje palacinky','krájať si palacinky'),
('7765','answer',None,'Podáva kopu palaciniek.','Podáva kôpku palaciniek.'),
('7774','phrases',0,'vysypať pohár mincí','vysypať dózu s mincami'),
('7774','answer',None,'Vysýpa pohár mincí.','Vysýpa dózu s mincami.'),
('7797','phrases',2,'nakoniec skončiť v sede','skončiť v sede'),
('7828','phrases',1,'niesť surf','niesť surfovú dosku'),
('7856','nouns',2,'pec na drevo','piecka na drevo'),
('7874','phrases',1,'chichotať sa za rukou','chichotať sa do dlane'),
]
for i,f,k,a,b in fixes:
    if k is None: assert d[i][f]==a,(i,f); d[i][f]=b
    else: assert d[i][f][k]==a,(i,f,k); d[i][f][k]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
s=json.load(open('source.json'))
print(sum(3+len(v['nouns'])+2 for v in s.values()))
