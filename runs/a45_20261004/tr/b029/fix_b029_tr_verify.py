import json
F='tr.json'; t=json.load(open(F))
fixes=[
('7772','phrases',2,'iki eliyle el kol hareketi yapmak','iki eliyle işaret etmek'),
('7774','phrases',0,'bir kavanoz bozuk parayı boşaltmak','bozuk para dolu bir kavanozu boşaltmak'),
('7774','answer',None,'Bir kavanoz bozuk parayı boşaltıyor.','Bozuk para dolu bir kavanozu boşaltıyor.'),
('7777','phrases',1,'bir donut almak','eline bir donut almak'),
('7781','answer',None,'Tilki çadıra çok yakın.','Tilki çadıra yakın.'),
('7804','phrases',1,'kollarını havaya fırlatmak','kollarını havaya kaldırmak'),
('7821','nouns',3,'balıkçı şapka','balıkçı şapkası'),
('7834','answer',None,'Gözleri kapalı bir şekilde takonun tadını çıkarıyor.','Gözleri kapalı halde takonun tadını çıkarıyor.'),
('7863','phrases',0,'bariyerin üstünden tırmanmak','bariyerin üstünden tırmanıp geçmek'),
('7865','phrases',2,'parlak bir şekilde yanmak','parlak alevlerle yanmak'),
('7872','phrases',0,'üstüne uymayan bir takım elbise giymek','üstüne oturmayan bir takım elbise giymek'),
('7872','answer',None,'Üstüne uymayan bir takım elbise giyiyor.','Üstüne oturmayan bir takım elbise giyiyor.'),
('7874','phrases',1,'elinin arkasında kıkırdamak','eliyle ağzını kapatıp kıkırdamak'),
]
for i,f,k,a,b in fixes:
    if k is None:
        assert t[i][f]==a,(i,f,t[i][f]); t[i][f]=b
    else:
        assert t[i][f][k]==a,(i,f,t[i][f][k]); t[i][f][k]=b
json.dump(t,open(F,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
