import json
p='tr/b031/hu.json'
d=json.load(open(p))
def s(i,f,idx,old,new):
    cur=d[i][f][idx] if idx is not None else d[i][f]
    assert cur==old,(i,f,cur)
    if idx is None: d[i][f]=new
    else: d[i][f][idx]=new
s('8035','phrases',1,'kézfertőtlenítőt nyomni a kezére','kézfertőtlenítőt nyomni')
s('8035','nouns',2,'papír zsebkendők','zsebkendők')
s('8041','phrases',0,'két kölyökkutyát mérlegelni','két kölyökkutyát méregetni')
s('8041','answer',None,'Két kölyökkutyát mérlegel.','Két kölyökkutyát méreget.')
s('8048','answer',None,'Habozik a platform szélén.','Habozik a platform peremén.')
s('8024','nouns',3,'edzőcipők','sportcipők')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
