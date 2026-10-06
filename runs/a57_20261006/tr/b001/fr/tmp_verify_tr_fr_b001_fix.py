import json
p='tr/b001/fr/tr.json'; d=json.load(open(p))
fixes=[('142','tahta oturmak','tahtın üzerine oturmak'),
('7193','beyaz bir gelinlik giymek','beyaz bir elbise giymek'),
('5580','bir kasanın üzerinde durmak','bir sandığın üzerinde durmak'),
('57','basamakları ilk çıkan olmak','basamakları herkesten önce çıkmak'),
('5506','kaykay yapmak','kaykay kaymak'),
('785','trenleri ve saatleri göstermek','trenler ve saatler göstermek'),
('5609','Adam neden korkuyor?','Adam neyden korkuyor?')]
n=0
for k,a,b in fixes:
  v=d[k]
  for f in ('phrases','recall'):
    for i,x in enumerate(v[f]):
      if x==a: v[f][i]=b; n+=1
  if v['question']==a: v['question']=b; n+=1
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(n)
