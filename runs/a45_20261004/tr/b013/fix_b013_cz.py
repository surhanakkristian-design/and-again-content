import json
F='cz.json'; d=json.load(open(F,encoding='utf-8'))
fixes=[
('4277','phrases',1,'osvětlovat nepořádný stůl','osvětlovat přeplněný stůl'),
('4290','phrases',1,'chladit obývák','chladit obývací pokoj'),
('4299','phrases',1,'chovat chlupatou kočku','chovat chlupatou kočku v náručí'),
('4301','phrases',0,'protáhnout se škvírou','protáhnout se mezerou'),
('4301','nouns',1,'škvíra','mezera'),
('4301','answer',None,'Protahuje se úzkou škvírou.','Protahuje se úzkou mezerou.'),
('4377','phrases',0,'šklebit se do kamery','zubit se do kamery'),
('4377','question',None,'Co dělá šklebící se muž?','Co dělá zubící se muž?'),
('4383','phrases',2,'vejít do obchodu','vejít do holičství'),
('4390','answer',None,'Poskakuje vzrušením.','Poskakuje nadšením.'),
('4403','phrases',1,'navrstvit na sebe vlněné vrstvy','nakupit na sebe vlněné vrstvy'),
('4403','answer',None,'Vrší na sebe další deky.','Kupí na sebe vrstvy dek.'),
('4406','phrases',0,'rozmazat ostré pruhy','rozetřít ostré pruhy'),
('4406','answer',None,'Rozmazává ostré pruhy.','Roztírá ostré pruhy.'),
('4409','phrases',0,'vrávorat dveřmi','proklopýtat dveřmi'),
('4412','phrases',2,'tlačit se na dodávku','tisknout se k dodávce'),
('4413','phrases',0,'přivonět ke květinám','čichat ke květinám'),
('4416','phrases',0,'číst si jízdenku','číst si letenku'),
('4416','phrases',1,'vytisknout jízdenku','vytisknout letenku'),
('4416','nouns',0,'jízdenka','letenka'),
('4416','answer',None,'Čte si jízdenku.','Čte si letenku.'),
('4429','phrases',1,'nabírat nudle','brát nudle'),
('4429','answer',None,'Nabírá hůlkami nudle.','Bere hůlkami nudle.'),
('4432','phrases',1,'nést kávu s sebou','nést kávu na cestu'),
('4432','nouns',0,'plakát s výprodejem','výprodejový plakát'),
]
for vid,f,i,old,new in fixes:
    if i is None:
        assert d[vid][f]==old,(vid,f,d[vid][f]); d[vid][f]=new
    else:
        assert d[vid][f][i]==old,(vid,f,d[vid][f][i]); d[vid][f][i]=new
json.dump(d,open(F,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(fixes))
