import json
p='tr/b014/fr.json'; d=json.load(open(p))
def sub(i,f,idx,old,new):
    if idx is None:
        assert d[i][f]==old,(i,f,d[i][f]); d[i][f]=new
    else:
        assert d[i][f][idx]==old,(i,f,d[i][f][idx]); d[i][f][idx]=new
sub('4472','nouns',1,'une chapka','un chapeau en fourrure')
sub('4488','phrases',0,'abattre un tampon','donner un grand coup de tampon')
sub('4488','answer',None,'Il abat un tampon sur un document.','Il donne un grand coup de tampon sur un document.')
sub('4583','phrases',0,"s'agripper le mollet",'agripper son propre mollet')
sub('4591','answer',None,"Elle tire une valise jusqu'à un navire.","Elle tire une valise à bord d'un navire.")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
