import json
p='tr/b028/es.json'; d=json.load(open(p))
fixes=[
('7342','phrases',0,'presionar contra la membrana','apretarse contra la membrana','reflexive needed: she presses herself against it; bare "presionar contra" lacks an object'),
('7342','phrases',2,'taparse la boca del susto','taparse la boca de la impresión','"shock" here is surprise/impression, not fright (susto)'),
('7342','answer',None,'Está empujando la cara contra la membrana.','Está hundiendo la cara en la membrana.','"push her face into" = hundir en; empujar contra is unidiomatic for a face'),
('7345','answer',None,'Está atada alrededor de su cintura.','Está atada alrededor de la cintura.','body part takes the article, not the possessive'),
('7379','phrases',1,'levantar los dos brazos','levantar los dos brazos en alto','"high" was left out'),
('7407','phrases',2,'estar en el andén','estar tirada en el andén','"lie" was left out; a bag lying on the ground = estar tirada'),
('7410','phrases',2,'sostener en alto una tablilla','sostener en alto un portapapeles','clipboard = portapapeles; tablilla is ambiguous (splint/small board)'),
('7430','phrases',2,'posarse en una caja blanca','estar encaramado en una caja blanca','posarse is for birds; a cat perching = estar encaramado'),
('7454','phrases',2,'posarse en una roca','estar encaramada en una roca','posarse is for birds; a marmot perching = estar encaramada'),
('7753','phrases',1,'cortar verduras','cortar verduras verdes','"green" was left out'),
]
log=[]
for vid,f,i,b,a,why in fixes:
    cur=d[vid][f] if i is None else d[vid][f][i]
    assert cur==b,(vid,f,cur)
    if i is None: d[vid][f]=a
    else: d[vid][f][i]=a
    log.append(f'- {vid} {f}{"" if i is None else "["+str(i)+"]"}: "{b}" -> "{a}" ({why})')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('tr/b028/_fixlog_b028_es.txt','w').write('\n'.join(log))
print(len(d))
