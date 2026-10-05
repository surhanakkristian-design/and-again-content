import json
p='/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/tr/b019/es.json'
d=json.load(open(p))
def S(i,f,old,new,idx=None):
    x=d[i]
    if idx is None:
        assert x[f]==old,(i,f,x[f]); x[f]=new
    else:
        assert x[f][idx]==old,(i,f,x[f][idx]); x[f][idx]=new
S('5106','answer','Está comiendo un gofre de caramelo pegajoso.','Está comiendo un gofre pegajoso de caramelo.')
S('5114','phrases','apuntar notas','tomar notas',1)
S('5122','phrases','escalar un muro','escalar una pared',0)
S('5123','phrases','desbordarse de café','rebosar de café',0)
S('5124','phrases','llevar un chaleco amarillo','llevar una camiseta de tirantes amarilla',2)
S('5146','phrases','colgar por debajo de sus rodillas','colgar por debajo de las rodillas',2)
S('5146','nouns','una tira de cáscara','una tira de piel',3)
S('5172','question','¿Qué está haciendo la mujer vestida de vaquero?','¿Qué está haciendo la mujer con ropa vaquera?')
S('5182','answer','Está mirando hacia arriba su mural.','Está alzando la vista hacia su mural.')
S('5211','question','¿Qué está arrastrando la niña detrás de sí?','¿Qué está arrastrando la chica detrás de sí?')
S('5218','question','¿Qué está haciendo la niña?','¿Qué está haciendo la chica?')
S('5218','nouns','una niña','una chica',2)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
