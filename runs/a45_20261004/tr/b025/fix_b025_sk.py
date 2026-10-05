import json
p='tr/b025/sk.json'; d=json.load(open(p))
fixes=[('6962',1,'vyštekovať rozkazy vojakom','vyštekávať rozkazy vojakom'),
       ('6992',2,'nakloniť sa cez balkón','vykloniť sa z balkóna'),
       ('7030',2,'preletieť po oblohe','preletieť oblohou'),
       ('7054',2,'zhíknuť od šoku','zalapať po dychu od šoku')]
for i,k,a,b in fixes:
    assert d[i]['phrases'][k]==a,(i,d[i]['phrases'][k]); d[i]['phrases'][k]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
