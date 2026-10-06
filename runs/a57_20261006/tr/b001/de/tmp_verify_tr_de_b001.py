import json
p='tr/b001/de/tr.json'; t=json.load(open(p))
fixes=[('4658','answer',None,'Deniz kenarında araba sürüyor.','Deniz kıyısı boyunca araba sürüyor.'),
('4658','recall',3,'deniz kenarında araba sürüyor','deniz kıyısı boyunca araba sürüyor'),
('5215','answer',None,'Hızlı bisiklet sürüyor.','Hızla bisiklet sürüyor.'),
('5215','recall',3,'hızlı bisiklet sürüyor','hızla bisiklet sürüyor'),
('10','phrases',1,'açık yeşil parlamak','açık yeşil renkte parlamak'),
('10','recall',1,'açık yeşil parlamak','açık yeşil renkte parlamak'),
('5609','question',None,'Adam neden korkuyor?','Adam neyden korkuyor?'),
('82','phrases',2,'kovanın içine girmek','sürünerek kovanın içine girmek'),
('82','recall',2,'kovanın içine girmek','sürünerek kovanın içine girmek'),
('4788','answer',None,'Kadınlar çok şaşkın görünüyor.','Kadınlar çok şok olmuş görünüyor.'),
('4788','recall',3,'çok şaşkın görünüyorlar','çok şok olmuş görünüyorlar')]
for k,f,i,a,b in fixes:
    if i is None: assert t[k][f]==a,(k,f); t[k][f]=b
    else: assert t[k][f][i]==a,(k,f,i); t[k][f][i]=b
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
