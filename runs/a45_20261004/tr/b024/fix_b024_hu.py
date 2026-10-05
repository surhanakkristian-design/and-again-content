import json
p='tr/b024/hu.json'
d=json.load(open(p))
fixes=[('6832','phrases',0,'szélesen vigyorogni a kamerába','a kamerába vigyorogni'),
('6896','phrases',1,'az elszabadult kötél után nyúlni','a szabadon lengő kötél után nyúlni'),
('6904','phrases',0,'felhúzni az orrát','ráncolni az orrát'),
('6907','phrases',1,'kilöttyinteni egy forró italt','kiloccsantani egy forró italt'),
('6912','answer',None,'Egy csíkos zoknit tart a feje fölé.','Egy csíkos zoknit tart a feje fölött.'),
('6915','phrases',2,'mély ívbe hajolni','mély ívben meghajlani')]
for k,f,i,a,b in fixes:
    if i is None: assert d[k][f]==a; d[k][f]=b
    else: assert d[k][f][i]==a; d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
