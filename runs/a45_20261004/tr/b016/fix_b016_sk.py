import json
p='sk.json'; d=json.load(open(p))
def fx(i,f,idx,old,new):
    cur=d[i][f] if idx is None else d[i][f][idx]
    assert cur==old,(i,f,cur)
    if idx is None: d[i][f]=new
    else: d[i][f][idx]=new
fx('4772','phrases',2,'zvierať mu rameno','zvierať mu ruku')
fx('4785','answer',None,'Štrngajú si nimi.','Štrngajú si pohármi.')
fx('4860','phrases',2,'rozpustiť sa v oblak','rozpustiť sa na oblak')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
