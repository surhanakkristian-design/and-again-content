import json
p='tr.json'; d=json.load(open(p))
fixes=[
('7334','phrases',0,'kaykay tahtasını yakalamak','bir kaykay tahtası yakalamak'),
('7336','phrases',1,'kahvaltı tepsisini dengede tutmak','bir kahvaltı tepsisini dengede tutmak'),
('7336','phrases',2,'korkuluktan eğilmek','korkuluğun üzerinden eğilmek'),
('7340','phrases',0,'korkuluktan eğilmek','korkuluğun üzerinden eğilmek'),
('7342','phrases',2,'şoktan ağzını kapatmak','şok içinde ağzını kapatmak'),
('7386','phrases',1,'arkadaşına doğru koşmak','arkadaşına doğru hızla koşmak'),
('7387','phrases',1,'gözlerini siper etmek','elini gözlerine siper etmek'),
('7403','phrases',1,'taşınabilir buzluğun üstünde oturmak','taşınabilir bir buzluğun üstünde oturmak'),
('7403','phrases',2,'minibüsten dışarı taşmak','minibüsten dışarı sarkmak'),
('7442','answer',None,'Midilliyle nehrin içinden geçiyor.','Midilliye binerek nehrin içinden geçiyor.'),
('7480','phrases',2,'kapanmak','dönerek kapanmak'),
('7481','phrases',2,'bir ip askıda sallanmak','bir askıda sallanmak'),
('7738','phrases',1,'koyu renk sakalı olmak','koyu renk bir sakalı olmak'),
('7740','phrases',0,'omzunun üzerinden bakmak','omzunun üzerinden göz atmak'),
('7750','phrases',1,'bir tabela kaldırmak','bir tabelayı havaya kaldırmak'),
]
for k,f,i,b,a in fixes:
    if i is None:
        assert d[k][f]==b,(k,f); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,i); d[k][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
s=json.load(open('source.json'))
print(sum(len(v['phrases'])+len(v['nouns'])+2 for v in s.values()))
