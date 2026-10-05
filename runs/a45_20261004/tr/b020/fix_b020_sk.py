import json
p='tr/b020/sk.json'
d=json.load(open(p))
fixes=[
('5259','phrases',0,'triasť hustou bielou srsťou','otriasať si hustú bielu srsť'),
('5259','answer',None,'Trasie hustou bielou srsťou.','Otriasa si hustú bielu srsť.'),
('5298','phrases',1,'siahnuť po ďalšej fľaštičke','siahnuť po ďalšom flakóne'),
('5312','phrases',1,'šľahať nad špízy','šľahať nad špízmi'),
('5314','phrases',0,'držať snehovú guľu','držať sklenenú snehovú guľu'),
('5316','answer',None,'Upíja pohár červeného vína.','Upíja z pohára červeného vína.'),
('5322','phrases',2,'vypľuť plné ústa','vypľuť dúšok'),
('5327','answer',None,'Strieka lak na vlasy na vysoký účes.','Strieka vysoký účes lakom na vlasy.'),
]
for k,f,i,a,b in fixes:
    if i is None:
        assert d[k][f]==a,(k,f); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,i); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('ok')
