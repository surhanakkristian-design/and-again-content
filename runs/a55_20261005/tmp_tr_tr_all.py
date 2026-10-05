# helper for native tr, learning de/es/fr
import json, os
H=os.path.dirname(os.path.abspath(__file__))
# per lang: vid -> (phrases, nouns, q, a, captions(list in source order), answer_recall, extra recall map)
T={'de':{
'8055':(["bir adamı taşımak","bir ip tutmak","bir ipe asılı durmak"],["sıcak hava balonu","bulutlar","ip","adam"],"Adam ne yapıyor?","Büyük bir sıcak hava balonuna asılı duruyor.",["sıcak hava balonuyla uçmak","bir sıcak hava balonunu indirmek","sıcak hava balonunun sepeti"],"büyük bir sıcak hava balonuna asılı duruyor",{}),
'236':(["denizde yüzmek","havaya sıçramak","suya geri düşmek"],["gökyüzü","yunus","kuyruk yüzgeci","su"],"Yunus ne yapıyor?","Sudan dışarı sıçrıyor.",["bir grup yunus","bir yunusla yüzmek","bir yunusu beslemek"],"sudan dışarı sıçrıyor",{}),
'624':(["bir şapkanın peşinden koşmak","rüzgârda uçmak","bir şapka yakalamak"],["ağaçlar","şapka","kız","çimen"],"Kız ne yapıyor?","Bir şapkanın peşinden koşuyor.",["bir şapkanın peşinden koştu","bir şapkanın peşinden koşacak","otobüse koşmak"],"bir şapkanın peşinden koşuyor",{}),
'7071':(["altın bir taç takmak","çamurun içinden geçmek","gri gökyüzünü yansıtmak"],["taç","kral","ATV","su birikintisi"],"Kral ne yapıyor?","ATV'yi bir su birikintisinden geçiriyor.",["genç bir kral","kral ve kraliçe","kralın önünde eğilmek"],"ATV'yi bir su birikintisinden geçiriyor",{"das Quad":"ATV"}),
'4265':(["odaya dalmak","kanepede tembellik etmek","öfkeli bir arkadaşı sakinleştirmek"],["kapı","kanatlar","papağan","kanepe"],"Mavi papağan ne yapıyor?","Öfkeli papağanı sarılarak sakinleştiriyor.",["bir şövalye tarafından sakinleştirildi","havlayan bir köpeği sakinleştirmek","ağlayan bir bebeği sakinleştirmek"],"öfkeli papağanı sarılarak sakinleştiriyor",{}),
'461':(["bir mankeni giydirmek","boynuna bir atkı takmak","mankenin pozunu taklit etmek"],["atkı","gömlek","kedi","manken"],"Adam ne yapıyor?","Mankenin pozunu taklit ediyor.",["bir manken taşımak","vitrindeki manken","bir mankeni giydirmek"],"mankenin pozunu taklit ediyor",{}),
'62':(["ağır bir çantayı kaldırmak","yiyecekle dolu olmak","güneş gözlüğü takmak"],["gömlek","ekmek","elmalar","çanta"],"Adam ne yapıyor?","Çantaya yiyecek koyuyor.",["bir çantayı düşürmek","plaj çantası","spor çantası"],"çantaya yiyecek koyuyor",{}),
'8039':(["küreyle dar bir yol açmak","yol boyunca koşmak","pencerenin arkasında el kol hareketleri yapmak"],["kar","kürek","köpek","yol"],"Kadın dışarıda ne yapıyor?","Karda küreyle bir yol açıyor.",["geçidi kapatmak","dar geçit","bir geçit aramak"],"karda küreyle bir yol açıyor",{}),
'432':(["gruba ormanda yol göstermek","karanlıkta parlamak","yuvarlak metal çerçeveli gözlük takmak"],["fener","vadi","ceket","sırt çantası"],"Kadın ne yapıyor?","Bir fenerle gruba yol gösteriyor.",["şövalyeleri bir kaleye götürdü","Mars'ta robotlara yol gösterecek","bir atı yönlendirmek"],"bir fenerle gruba yol gösteriyor",{}),
'8056':(["bir kitap okumak","adama doğru yukarı bakmak","bir bankta oturmak"],["ağaçlar","kitap","bank","köpek"],"Adam ne yapıyor?","Bir bankta kitap okuyor.",["ağırlık sehpası","bir bankı boyamak","bir bankı paylaşmak"],"bir bankta kitap okuyor",{}),
},'es':{
'8055':(["bir adamı taşımak","bir ip tutmak","bir ipe asılı durmak"],["balon","bulutlar","ip","adam"],"Adam ne yapıyor?","Büyük bir balona asılı duruyor.",["balonla uçmak","bir balonu indirmek","balonun sepeti"],"büyük bir balona asılı duruyor",{}),
'236':(["denizde yüzmek","çok yükseğe sıçramak","suya düşmek"],["gökyüzü","yunus","kuyruk","su"],"Yunus ne yapıyor?","Sudan dışarı sıçrıyor.",["bir grup yunus","bir yunusla yüzmek","bir yunusu beslemek"],"sudan dışarı sıçrıyor",{}),
'624':(["bir şapkanın peşinden koşmak","rüzgârla uçmak","bir şapka yakalamak"],["ağaçlar","şapka","kız","çimen"],"Kız ne yapıyor?","Bir şapkanın peşinden koşuyor.",["bir şapkanın peşinden koştu","bir şapkanın peşinden koşacak","otobüse yetişmek için koşmak"],"bir şapkanın peşinden koşuyor",{}),
'7071':(["altın bir taçla boy göstermek","çamurda ilerlemek","gri gökyüzünü yansıtmak"],["taç","kral","ATV","su birikintisi"],"Kral ne yapıyor?","ATV'ye binmiş, bir su birikintisinden geçiyor.",["genç bir kral","kral ve kraliçe","kralın önünde reverans yapmak"],"ATV'ye binmiş, bir su birikintisinden geçiyor",{"el quad":"ATV"}),
'4265':(["odaya dalmak","kanepeye yayılmış olmak","öfkeli bir arkadaşı sakinleştirmek"],["kapı","kanatlar","papağan","kanepe"],"Mavi papağan ne yapıyor?","Öfkeli papağanı sarılarak sakinleştiriyor.",["bir şövalye tarafından sakinleştirildi","havlayan bir köpeği sakinleştirmek","ağlayan bir bebeği sakinleştirmek"],"öfkeli papağanı sarılarak sakinleştiriyor",{}),
'461':(["bir mankeni giydirmek","boynuna bir fular takmak","mankenin pozunu taklit etmek"],["fular","gömlek","kedi","manken"],"Genç adam ne yapıyor?","Mankenin pozunu taklit ediyor.",["omzunda bir manken taşımak","vitrin mankeni","bir mankeni giydirmek"],"mankenin pozunu taklit ediyor",{}),
'62':(["ağır bir çantayı kaldırmak","yiyecekle dolu olmak","güneş gözlüğü takmak"],["gömlek","ekmek","elmalar","çanta"],"Adam ne yapıyor?","Çantayı yiyecekle dolduruyor.",["bir çantayı düşürmek","plaj çantası","spor çantası"],"çantayı yiyecekle dolduruyor",{}),
'8039':(["karda bir yol açmak","açılmış yolda koşmak","camın arkasından işaret etmek"],["kar","kürek","köpek","yol"],"Dışarıdaki kız ne yapıyor?","Karda bir yol açıyor.",["geçidi kapatmak","dar geçit","bir geçit aramak"],"karda bir yol açıyor",{}),
'432':(["gruba yol göstermek","karanlıkta parlamak","yuvarlak çerçeveli gözlük takmak"],["fener","vadi","ceket","sırt çantası"],"Kız ne yapıyor?","Bir fenerle gruba yol gösteriyor.",["birkaç şövalyeyi bir kaleye götürüyordu","Mars'ta birkaç robota yol gösterecek","bir atı yönlendirmek"],"bir fenerle gruba yol gösteriyor",{}),
'8056':(["bir kitap okumak","adama bakmak","bir bankta oturmak"],["ağaçlar","kitap","bank","köpek"],"Adam ne yapıyor?","Bir bankta kitap okuyor.",["ağırlık sehpası","bir bankı boyamak","bir bankı paylaşmak"],"bir bankta kitap okuyor",{}),
},'fr':{
'8055':(["bir adamı taşımak","bir ip tutmak","bir ipe asılı olmak"],["sıcak hava balonu","bulutlar","ip","adam"],"Adam ne yapıyor?","Büyük bir sıcak hava balonuna asılı duruyor.",["sıcak hava balonuyla uçmak","bir sıcak hava balonunu indirmek","sıcak hava balonunun sepeti"],"büyük bir sıcak hava balonuna asılı duruyor",{}),
'236':(["denizde yüzmek","havaya sıçramak","suya geri düşmek"],["gökyüzü","yunus","kuyruk","su"],"Yunus ne yapıyor?","Sudan dışarı sıçrıyor.",["bir grup yunus","bir yunusla yüzmek","bir yunusu beslemek"],"sudan dışarı sıçrıyor",{}),
'624':(["bir şapkanın peşinden koşmak","rüzgârla uçup gitmek","bir şapka yakalamak"],["ağaçlar","şapka","kız","çimen"],"Kız ne yapıyor?","Bir şapkanın peşinden koşuyor.",["bir şapkanın peşinden koştu","bir şapkanın peşinden koşacak","otobüse yetişmek için koşmak"],"bir şapkanın peşinden koşuyor",{}),
'7071':(["altın bir taçla boy göstermek","çamur sıçratmak","gri gökyüzünü yansıtmak"],["taç","kral","ATV","su birikintisi"],"Kral ne yapıyor?","ATV ile bir su birikintisinden geçiyor.",["genç bir kral","kral ve kraliçe","kralın önünde eğilmek"],"ATV ile bir su birikintisinden geçiyor",{"le quad":"ATV"}),
'4265':(["odaya hızla dalmak","kanepede keyif yapmak","öfkeli bir arkadaşı sakinleştirmek"],["kapı","kanatlar","papağan","kanepe"],"Mavi papağan ne yapıyor?","Öfkeli papağanı sarılarak sakinleştiriyor.",["bir şövalye tarafından sakinleştirildi","havlayan bir köpeği sakinleştirmek","ağlayan bir bebeği sakinleştirmek"],"öfkeli papağanı sarılarak sakinleştiriyor",{}),
'461':(["bir mankeni giydirmek","bir atkıya sarılı olmak","mankenin pozunu taklit etmek"],["atkı","gömlek","kedi","manken"],"Genç adam ne yapıyor?","Mankenin pozunu taklit ediyor.",["bir manken taşımak","vitrin mankeni","bir mankeni giydirmek"],"mankenin pozunu taklit ediyor",{}),
'62':(["ağır bir çantayı kaldırmak","yiyecekle dolu olmak","güneş gözlüğü takmak"],["polo tişört","baget","elmalar","çanta"],"Adam ne yapıyor?","Çantayı yiyecekle dolduruyor.",["bir çantayı düşürmek","plaj çantası","spor çantası"],"çantayı yiyecekle dolduruyor",{}),
'8039':(["bir geçit açmak","geçit boyunca koşmak","camın arkasında el kol hareketleri yapmak"],["kar","kürek","köpek","geçit"],"Kadın dışarıda ne yapıyor?","Karda bir geçit açıyor.",["geçidi kapatmak","dar geçit","bir geçit aramak"],"karda bir geçit açıyor",{}),
'432':(["gruba yol göstermek","patikayı aydınlatmak","yuvarlak çerçeveli gözlük takmak"],["fener","vadi","ceket","sırt çantası"],"Genç kadın ne yapıyor?","Bir fenerle gruba yol gösteriyor.",["şövalyeleri bir kaleye götürüyordu","Mars'ta robotlara yol gösterecek","bir atı yönlendirmek"],"bir fenerle gruba yol gösteriyor",{}),
'8056':(["bir kitap okumak","adama bakmak","bir bankta oturmak"],["ağaçlar","kitap","bank","köpek"],"Adam ne yapıyor?","Bir bankta kitap okuyor.",["ağırlık sehpası","bir bankı boyamak","bir bankı paylaşmak"],"bir bankta kitap okuyor",{}),
}}
for l,d in T.items():
    src=json.load(open(f'{H}/tr/source_{l}.json')); out={}
    for vid,s in src.items():
        P,N,Q,A,C,AR,X=d[vid]
        assert len(P)==len(s['phrases']) and len(N)==len(s['nouns']) and len(C)==len(s['captions'])
        m={p['text']:t for p,t in zip(s['phrases'],P)}; caps=dict(zip(s['captions'],C)); m.update(caps); m.update(X)
        rec=[]
        for r in s['recall']:
            rec.append(m[r] if r in m else AR)
        assert sum(1 for r in s['recall'] if r not in m)==1, (l,vid)
        out[vid]={'phrases':P,'nouns':N,'question':Q,'answer':A,'captions':caps,'recall':rec}
    json.dump(out,open(f'{H}/tr/{l}/tr.json','w'),ensure_ascii=False,indent=1)
