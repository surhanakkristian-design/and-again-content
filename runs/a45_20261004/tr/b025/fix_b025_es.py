import json
p='tr/b025/es.json'
d=json.load(open(p))
fixes=[
('6951','phrases',1,'echar el humo','echar humo','entry form: "blow out smoke" has no article; bare "echar humo" is the natural entry'),
('6953','nouns',0,'cuernos','astas','a moose has antlers = astas/cornamenta; "cuernos" are horns'),
('6977','nouns',3,'unas tenazas','tenazas','English bare plural "tongs" -> Spanish bare plural per brief'),
('6982','phrases',1,'garabatear en una tablilla','garabatear en un portapapeles','clipboard = portapapeles; "tablilla" is not the usual word'),
('6982','answer',None,'Está garabateando en una tablilla.','Está garabateando en un portapapeles.','same word as the phrase'),
('6990','nouns',2,'una copia','una réplica','a life-size model elephant is "una réplica"; "copia" reads as a document copy'),
('6999','phrases',2,'contemplar el castillo','alzar la vista hacia el castillo','"gaze up" lost the "up"'),
('6999','question',None,'¿Qué está mirando la mujer hacia arriba?','¿Hacia qué está alzando la vista la mujer?','awkward word order; same verb as phrase and answer'),
('6999','answer',None,'Está contemplando el castillo de hielo.','Está alzando la vista hacia el castillo de hielo.','"gaze up at" lost the "up"; same verb as phrase'),
('7005','phrases',1,'llevar sus tacones','llevar sus tacones en la mano','"llevar sus tacones" reads as wearing them; she carries them in her hand'),
('7034','nouns',1,'unas gafas protectoras','gafas protectoras','English bare plural "goggles" -> Spanish bare plural per brief'),
]
log=[]
for k,f,i,b,a,why in fixes:
    if i is None:
        assert d[k][f]==b,(k,f,d[k][f]); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,d[k][f][i]); d[k][f][i]=a
    log.append(f'- {k}, {f}{"" if i is None else "["+str(i)+"]"}: "{b}" -> "{a}" ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('tr/b025/fixlog_b025_es.txt','w').write(str(n)+'\n'+'\n'.join(log)+'\n')
print(n)
