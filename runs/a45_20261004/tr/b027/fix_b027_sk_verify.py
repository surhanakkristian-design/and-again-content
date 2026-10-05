import json
p='sk.json'; t=json.load(open(p))
def rep(i,f,old,new,idx=None):
    if idx is None:
        assert t[i][f]==old,(i,f,t[i][f]); t[i][f]=new
    else:
        assert t[i][f][idx]==old,(i,f,t[i][f][idx]); t[i][f][idx]=new
rep('7216','phrases','mávať bielou palčiakou','mávať bielym palčiakom',1)
rep('7225','answer','Telefón je upevnený v držiaku.','Telefón je uchytený v držiaku.')
rep('7237','answer','Vybuchne do obrovskej ohnivej gule.','Zmení sa na obrovskú ohnivú guľu.')
rep('7278','phrases','visieť cez konár','visieť prevesená cez konár',2)
rep('7296','answer','Nalieva číry destilát do tekvice.','Nalieva číry destilát do nádoby z tekvice.')
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
