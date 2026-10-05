import json
d=json.load(open('de.json'))
fixes=[
('5238','phrases',0,'den gemeißelten Stein streicheln','über den gemeißelten Stein streichen'),
('5238','answer',None,'Er streichelt den gemeißelten Stein.','Er streicht über den gemeißelten Stein.'),
('5268','phrases',2,'breit zu grinsen anfangen','zu grinsen anfangen'),
('5270','phrases',0,'Müslipackungen greifen','Müslipackungen schnappen'),
('5290','question',None,'Wozu blickt die Frau hinauf?','Wohin blickt die Frau hinauf?'),
('5292','phrases',0,'auf seiner Tastatur zusammensacken','auf seine Tastatur sacken'),
('5312','phrases',1,'über die Spieße hochschlagen','über den Spießen hochschlagen'),
('5327','nouns',1,'ein Creole-Ohrring','eine Creole'),
('5340','answer',None,'Sie tragen eine große Kiste.','Sie tragen einen großen Karton.'),
]
for i,f,k,b,a in fixes:
    if k is None:
        assert d[i][f]==b,(i,f); d[i][f]=a
    else:
        assert d[i][f][k]==b,(i,f,k); d[i][f][k]=a
json.dump(d,open('de.json','w'),ensure_ascii=False,indent=1)
