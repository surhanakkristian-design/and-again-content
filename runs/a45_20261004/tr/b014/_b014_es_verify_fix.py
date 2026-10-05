import json
p='tr/b014/es.json'; d=json.load(open(p))
def fix(i,f,idx,old,new):
    cur=d[i][f][idx] if idx is not None else d[i][f]
    assert cur==old,(i,f,cur)
    if idx is None: d[i][f]=new
    else: d[i][f][idx]=new
fix('4461','phrases',0,'estar tumbado bajo la arena','estar enterrado en la arena')
fix('4461','answer',None,'Está tumbado bajo la arena.','Está enterrado en la arena.')
fix('4556','phrases',1,'llevar dos cafés para llevar','entregar dos cafés para llevar')
fix('4556','answer',None,'Todos están elogiando al hombre del portátil.','Están elogiando al hombre del portátil.')
fix('4571','answer',None,'Están empujando una barca grande.','La gente está empujando una barca grande.')
fix('4589','question',None,'¿Qué está haciendo la mujer de coral?','¿Qué está haciendo la mujer vestida de coral?')
fix('4593','question',None,'¿Dónde está caminando el hombre?','¿Por dónde está caminando el hombre?')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
