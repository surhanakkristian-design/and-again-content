import json
p='tr/b031/tr.json'
d=json.load(open(p))
def s(i,f,idx,old,new):
    if idx is None:
        assert d[i][f]==old,(i,f); d[i][f]=new
    else:
        assert d[i][f][idx]==old,(i,f,idx); d[i][f][idx]=new
s('8021','phrases',0,'eşikten adım atmak','eşiğin üzerinden adım atmak')
s('8021','answer',None,'Onu kucağında eşikten taşıyor.','Onu kucağında eşikten geçiriyor.')
s('8041','phrases',1,'şüpheli bir yüz ifadesi takınmak','kuşkulu bir yüz ifadesi takınmak')
s('8041','question',None,'Sarılı kadın ne yapıyor?','Sarı giyen kadın ne yapıyor?')
s('8042','nouns',0,'vitray','vitray pencere')
s('8048','phrases',0,'aşağıya, dar vadiye bakmak','aşağıdaki kanyona gözlerini dikmek')
s('8049','phrases',2,'çakılların üstünde yayılıp yatmak','çakılların üstünde boylu boyunca uzanmak')
s('8050','phrases',1,'ellerini bırakıp paten kaymak','tutunmadan paten kaymak')
s('8050','answer',None,'Ellerini bırakıp paten kayıyor.','Tutunmadan paten kayıyor.')
s('8059','phrases',2,'koyu bir sakala sahip olmak','koyu renk sakallı olmak')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
