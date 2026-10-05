import json
H='tr'
fixes={'de':[('62','nouns',1,'chleba','chléb'),('8056','phrases',1,'vzhlížet k muži','dívat se nahoru na muže'),('8056','recall',1,'vzhlížet k muži','dívat se nahoru na muže')],
 'es':[('62','nouns',1,'chleba','chléb')],
 'fr':[('8039','phrases',1,'běžet podél průchodu','běžet průchodem'),('8039','recall',1,'běžet podél průchodu','běžet průchodem')]}
for l,fs in fixes.items():
    p=f'{H}/{l}/cz.json'; d=json.load(open(p))
    for vid,f,i,a,b in fs:
        assert d[vid][f][i]==a,(l,vid,f,i,d[vid][f][i]); d[vid][f][i]=b
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
