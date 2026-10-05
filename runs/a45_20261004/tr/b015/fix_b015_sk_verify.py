import json
p='sk.json'; d=json.load(open(p))
def rep(i,f,old,new,idx=None):
    if idx is None:
        assert d[i][f]==old,(i,f); d[i][f]=new
    else:
        assert d[i][f][idx]==old,(i,f,idx); d[i][f][idx]=new
rep('4631','phrases','zložiť drevené diely','poskladať drevené diely',1)
rep('4637','phrases','zbúrať veľký dom','zničiť veľký dom',1)
rep('4637','answer','Búra veľký dom.','Ničí veľký dom.')
rep('4653','phrases','byť dokorán otvorený','byť dokorán otvorené',2)
rep('4654','phrases','prekrížiť si ruky','založiť si ruky',0)
rep('4666','phrases','zdvihnúť oblak prachu','zvíriť oblak prachu',2)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
