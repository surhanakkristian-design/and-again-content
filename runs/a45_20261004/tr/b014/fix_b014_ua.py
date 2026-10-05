import json
p='ua.json'; d=json.load(open(p))
def s(i,f,k,old,new):
    cur=d[i][f][k] if k is not None else d[i][f]
    assert cur==old,(i,f,cur)
    if k is None: d[i][f]=new
    else: d[i][f][k]=new
s('4504','phrases',1,'сидіти на своїх руках','сидіти на їхніх руках')
s('4512','phrases',0,'писати в списку','писати на списку')
s('4512','question',None,'Де пише чоловік?','На чому пише чоловік?')
s('4512','answer',None,'Він пише в списку.','Він пише на списку.')
s('4503','nouns',0,'капелюх','ковпак')
s('4527','nouns',0,'шапка','ковпак')
s('4532','nouns',0,"пов'язка на голову",'тюрбан')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
