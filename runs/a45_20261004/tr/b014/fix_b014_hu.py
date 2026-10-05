import json
p='hu.json'; d=json.load(open(p))
def rep(i,f,k,old,new):
    if k is None:
        assert d[i][f]==old,(i,f,d[i][f]); d[i][f]=new
    else:
        assert d[i][f][k]==old,(i,f,k,d[i][f][k]); d[i][f][k]=new
rep('4452','phrases',1,'leülni egy padra','egy padon ülni')
rep('4456','phrases',2,'fa ajtaja van','faajtaja van')
rep('4571','phrases',1,'fából van','fából készülni')
rep('4575','phrases',1,'elvenni a vizes palackot','elvenni a vizespalackot')
rep('4584','nouns',3,'nyomvonal','nyomsor')
rep('4584','answer',None,'Nyomvonalat hagynak a homokban.','Nyomsort hagynak a homokban.')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
