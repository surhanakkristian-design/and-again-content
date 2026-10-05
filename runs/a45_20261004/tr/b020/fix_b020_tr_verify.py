import json
p='tr/b020/tr.json'
d=json.load(open(p))
fixes=[
('5227','phrases',2,'sürüye öncülük etmek','sürünün başını çekmek'),
('5232','phrases',2,'havaya yumruk sallamak','havaya yumruk atmak'),
('5238','question',None,'Uçurumda ne yapıyor?','Kayalığın önünde ne yapıyor?'),
('5238','nouns',3,'başörtüsü','puşi'),
('5243','phrases',1,'renkli sekmeleri olmak','renkli ayraçları olmak'),
('5246','question',None,'Kadın neyin içine bakıyor?','Kadın neyden dikkatle bakıyor?'),
('5246','answer',None,'Mikroskobun içine bakıyor.','Mikroskoptan dikkatle bakıyor.'),
('5252','phrases',1,'bir poşeti vermek','bir poşet vermek'),
('5255','answer',None,'Yukarıdaki yargıca dik dik bakıyor.','Başını kaldırıp yargıca bakakalıyor.'),
('5269','phrases',0,'iki çikolatayı sıkıca tutmak','iki tablet çikolatayı sıkıca tutmak'),
('5274','phrases',0,'suyun sıcaklığını denemek','suyun sıcaklığını kontrol etmek'),
('5278','phrases',0,'tebeşir resimlerinin önünden geçerek gezinmek','tebeşir resimlerinin önünden ağır ağır geçmek'),
('5278','answer',None,'Tebeşir resimlerinin önünden geçerek geziniyor.','Tebeşir resimlerinin önünden ağır ağır geçiyor.'),
('5292','answer',None,'Masasında uyukluyor.','Masasında uyuyakalıyor.'),
('5298','phrases',0,'bir kâğıt şeridi koklamak','bir kâğıt şerit koklamak'),
('5309','phrases',1,'bir kahve fincanı tutmak','bir kahve bardağı tutmak'),
('5309','nouns',1,'fincan','bardak'),
('5326','phrases',0,'acıyla ağlamak','acıdan ağlamak'),
('5327','phrases',1,'şekillendirici bir tarağı tutmak','bir şekillendirme tarağını sıkıca tutmak'),
('5342','phrases',1,'pastel boya bir resmi havaya kaldırmak','mum boya bir resmi havaya kaldırmak'),
]
for k,f,i,a,b in fixes:
    if i is None:
        assert d[k][f]==a,(k,f); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,i); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
