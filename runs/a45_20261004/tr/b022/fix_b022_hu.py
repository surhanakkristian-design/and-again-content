import json
p='tr/b022/hu.json'; h=json.load(open(p))
def fix(i,f,idx,old,new):
    cur=h[i][f] if idx is None else h[i][f][idx]
    assert cur==old,(i,f,cur)
    if idx is None: h[i][f]=new
    else: h[i][f][idx]=new
fix('5488','answer',None,'Integetve búcsúzik a komptól.','Búcsút int a kompnak.')
fix('5509','phrases',2,'egy csomó havat leejteni','egy hócsomót leejteni')
fix('5532','nouns',3,'hot dog jelmez','hot dog-jelmez')
fix('5537','phrases',1,'egy zöld kabátot viselni','egy zöld dzsekit viselni')
json.dump(h,open(p,'w'),ensure_ascii=False,indent=2)
