import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """
5223|tozlu bir patikada koşmak;işaretli rotayı göstermek;patikanın kenarında durmak|gökyüzü;vadi;saç bandı;rota|Kadın ne tutuyor?|Üzerinde rota işaretlenmiş bir harita tutuyor.
5224|altın bir taç takmak;bir tepsi yemek taşımak;kralın önünde eğilmek|mumlar;taç;muhafız;sandalye|Kalabalık ne yapıyor?|Kralın önünde eğiliyorlar.
5225|bir bardaktan içmek;saatine bakmak;koşucuyu alkışlamak|gökyüzü;insanlar;koşucu;koni|Koşucu ne yapıyor?|Yarışı bitiriyor.
5226|peron boyunca koşturmak;bir spor çantasını sıkıca tutmak;şu anki saati göstermek|cam çatı;saat;vagon;spor çantası|Adam ne yapıyor?|Peron boyunca koşturuyor.
5227|birkaç köpekle koşu yapmak;kollarını havaya kaldırmak;sürüye öncülük etmek|gökyüzü;plaj;koşucu;parke taşları|Kadın ne yapıyor?|Birkaç köpekle koşu yapıyor.
5230|sıcak çay içmek;bir çörek yemek;küçük bir oyuncak bebeği açmak|ışıklar;şapka;oyuncak bebek;palto|Kadın neyi açıyor?|Küçük bir oyuncak bebeği açıyor.
5231|dumanı tüten mantı servis etmek;bir bardak çay doldurmak;bacasından buhar çıkarmak|semaver;mantılar;turşular;krepler|Yaşlı kadın ne servis ediyor?|Dumanı tüten mantı servis ediyor.
5232|bir halata asılmak;bir vinci çevirmek;havaya yumruk sallamak|yelken;dağ;yat;halat kangalı|Kadın ne tutuyor?|Bir halat kangalı tutuyor.
5233|askerlerin önünde durmak;bariyerlerin arkasından izlemek;rüzgârda dalgalanmak|gökyüzü;askerler;subay;seyirciler|Seyirciler ne yapıyor?|Askerî geçit törenini izliyorlar.
5234|beyaz eldivenlerle selam vermek;tribünlerden izlemek;rüzgârda dalgalanmak|bayraklar;seyirciler;saflar|Üniformalı kadınlar ne yapıyor?|Düzgün saflar hâlinde selam veriyorlar.
5235|sevkiyat belgelerini mühürlemek;bir mührü başının üstüne kaldırmak;görevliyi dikkatle izlemek|gökyüzü;konteynerler;sandıklar;görevli|Kadın ne yapıyor?|Ahşap kargo sandıklarını mühürlüyor.
5237|eski duvara dokunmak;sıcak çay doldurmak;karanlıkta yanmak|yıldızlar;fincan;adam;ateş|Adam ne tutuyor?|Küçük bir fincan çay tutuyor.
5238|oymalı taşı okşamak;kum tepesinin ardında batmak;kamp ateşinin yanında çömelmek|gökyüzü;güneş;kum tepesi;başörtüsü|Uçurumda ne yapıyor?|Oymalı taşı okşuyor.
5240|başının üstünde bir yem sallamak;kanatlarını iyice açmak;şahine et yedirmek|kanat;şahin;eldiven;kamyonet|Doğancı ne yapıyor?|Şahine et yediriyor.
5242|sisin içinden yürümek;düzgün sıralar hâlinde durmak;saçlarını geriye atmak|çatılar;kolye;sabahlık;parfüm şişeleri|Kadın neyin içinden yürüyor?|Parfüm sisinin içinden yürüyor.
5243|yapışkan notlar yapıştırmak;renkli sekmeleri olmak;not almak|bitki;yapışkan notlar;vantilatör;defter|Kadın neyi notlarla kaplıyor?|Takvimi yapışkan notlarla kaplıyor.
5244|bir sandviç tutmak;kırmızı bir elmayı havaya kaldırmak;çimenlerin üzerinde yuvarlanmak|sınıf arkadaşı;elma;sandviç;bank|Sarışın çocuk ne tutuyor?|Kırmızı bir elma tutuyor.
5246|cam bir deney şişesini çalkalamak;not almak;kameraya sırıtmak|deney şişesi;mikroskop;koruyucu gözlük;laboratuvar önlüğü|Kadın neyin içine bakıyor?|Mikroskobun içine bakıyor.
5247|parmağını sallamak;çamurlu yeri paspaslamak;duvarın yanında uslu uslu oturmak|ayak izleri;paspas;kask;önlük|Genç adam ne yapıyor?|Çamurlu ayak izlerini paspaslıyor.
5248|telefonuna bakmak;deniz kenarında ilerlemek;uzun bir sıra hâlinde durmak|gökyüzü;deniz;ceket;scooterlar|Kadın neye bakıyor?|Telefonuna bakıyor.
5249|kirli bir tavayı yıkamak;ağır bir tavayı kaldırmak;yeşil eldiven giymek|pencere;adam;musluk;tava|Adam ne yapıyor?|Kirli bir tavayı yıkıyor.
5251|telefonla konuşmak;bir deftere yazmak;bir mühür kullanmak|pencere;klasörler;klavye;defter|Kadın ne yapıyor?|Telefonla konuşuyor.
5252|olgun mangoları tartmak;bir poşeti vermek;bir ananası öne uzatmak|hasır şapka;asma terazi;rambutanlar;mangolar|Seyyar satıcı ne yapıyor?|Tropik meyve satıyor.
5253|gri bir kasket takmak;turuncu çiçeklere dokunmak;bisiklet sürmek|ağaçlar;adam;bisiklet;yol|Yaşlılar ne yapıyor?|Ağaçların altında dans ediyorlar.
5254|kasketine dokunmak;çiçekleri koklamak;bisiklet sürmek|ağaçlar;bisiklet;kadın;çiçekler|Yaşlılar ne yapıyor?|Partnerleriyle dans ediyorlar.
5255|tokmağı vurmak;bir belgeyi incelemek;şok içinde yukarı bakakalmak|arma;yargıç;tokmak;mikrofon|Genç adam ne yapıyor?|Yukarıdaki yargıca dik dik bakıyor.
5256|mahkemeye hitap etmek;notlarından okumak;yargıca dönük durmak|arma;yargıç;kürsü|Kırmızılı yargıç ne yapıyor?|Mahkemeye hitap ediyor.
5258|kahkahayla gülmek;uzun kıvırcık saçlı olmak;barın üzerinde asılı durmak|ışıklar;kadın;bar;bardak|Kadın ne yapıyor?|Barda içki hazırlıyor.
5259|kalın beyaz tüylerini silkelemek;şaşkınlıkla soluğu kesilmek;ıslak tahtaların üzerinden koşuşturmak|tüy;kahve fincanı;sosis köpek;göl|Büyük beyaz köpek ne yapıyor?|Kalın beyaz tüylerini silkeliyor.
5260|çilekli pastayı silip süpürmek;kollarını kavuşturup durmak;utançtan başını öne eğmek|çatal;hırka;bir dilim pasta;tabak|Kadın ne yapıyor?|Kollarını kavuşturup duruyor.
5261|pizzasını herkesle paylaşmak;çimenlerde koşu yapmak;tasmalı iki köpeği gezdirmek|palmiye;bir dilim pizza;beyaz köpek;pizza|Pembe saçlı kadın ne yapıyor?|Pizzasını herkesle paylaşıyor.
5263|kitapları rafa koymak;büyük bir bitkiyi kaldırmak;kameraya gülümsemek|bitki;fotoğraf;kitaplar;kadın|Kadın ne yapıyor?|Kitapları rafa koyuyor.
5264|ağır kanepeyi kaydırmak;büyük bir tuval asmak;kanepeye uzanmak|sarkıt lamba;kanepe;sehpa;halı|Kadın önce ne yapıyor?|Kanepeyi yerde kaydırıyor.
5265|dürbünle bakmak;küçük bir tekne kullanmak;gemiye doğru yukarı bakmak|gökyüzü;konteynerler;dürbün;su|Genç adam ne yapıyor?|Dürbünüyle bakıyor.
5267|bir minderin üzerinde yatmak;hedeflere ateş etmek;yumruklarını havaya kaldırmak|hedefler;kar;şapka;tüfek|Kadın ne yapıyor?|Hedeflere ateş ediyor.
5268|hedeflere nişan almak;bariyerlerin arkasından izlemek;sırıtmaya başlamak|seyirciler;hedefler;saç bandı;tüfek|Sporcu neye nişan alıyor?|Tüfeğiyle hedeflere nişan alıyor.
5269|iki çikolatayı sıkıca tutmak;zeytin yeşili bir ceket satın almak;öpücük göndermek|yürüyen merdivenler;bere;cam kapı;hediye çantası|Kadın ne yapıyor?|Zeytin yeşili bir ceket satın alıyor.
5270|mısır gevreği kutularını kapmak;büyük bir alışveriş arabasını doldurmak;kasada çalışmak|ışıklar;raflar;adam;alışveriş arabası|Genç kadın ne yapıyor?|Süpermarkette alışveriş yapıyor.
5271|ellerini ağzına siper edip bağırmak;mavi bir tişört giymek;büyük bir şapka takmak|gökyüzü;kayalar;şapka;kadın|Üç kişi ne yapıyor?|Kollarını açmış bağırıyorlar.
5274|suyun sıcaklığını denemek;saçını köpürtmek;su fışkırtmak|duş başlığı;fayanslar;köpük;duş hortumu|Genç adam ne yapıyor?|Sırılsıklam saçını köpürtüyor.
5276|battaniyeyi başının üstüne kaldırmak;hardal sarısı bir tişört giymek;granit tezgâhın üzerinde durmak|kardeşler;damla çikolatalı kurabiye;karton tabak;granit tezgâh|Kardeşler neyi paylaşıyor?|Kardeşler damla çikolatalı bir kurabiyeyi paylaşıyor.
5277|kot pantolon giymek;elbise giymek;çimenlerin üzerinde yatmak|erkek çocuk;kız çocuk;kurabiye;tabak|Çocuklar nerede yatıyor?|Çocuklar çimenlerin üzerinde yatıyor.
5278|tebeşir resimlerinin önünden geçerek gezinmek;kulaklığı boynunda taşımak;yolda bisiklet sürmek|kot ceket;yaya geçidi;yangın musluğu;çöp kutusu|Genç adam ne yapıyor?|Tebeşir resimlerinin önünden geçerek geziniyor.
5279|dev bir parşömeni imzalamak;evrak işlerini halletmek;yeşil bir dosya tutmak|avize;Fransız bayrağı;parşömen;ahşap masa|Genç adam neyi imzalıyor?|Dev bir parşömeni imzalıyor.
5280|iki kolunu havaya kaldırmak;başını kaldırıp tabelalara bakmak;farklı yönleri göstermek|yön tabelası;su şişesi;deniz;çimen|Kadın ne yapıyor?|İki kolunu havaya kaldırıyor.
5283|tabakları yıkamak;lavaboyu silmek;lavabonun içinde durmak|kadın;pencere;kule|Kadın ne yapıyor?|Tabakları yıkıyor.
5286|arkadaşının saçını yapmak;telefonu tutmak;başparmağını kaldırmak|sweatshirt;telefon;ışıklar|Kızıl saçlı kız ne yapıyor?|Arkadaşının saçını yapıyor.
5287|arkadaşının saçını yapmak;parıltılı bir bluz giymek;yerde oturmak|ışıklar;lamba;pencere;kıyafetler|Kahverengi saçlı kız ne yapıyor?|Arkadaşının saçını yapıyor.
5290|hayranlıkla yukarı bakmak;uzun örgülerini savurmak;mavi gökyüzüne yükselmek|gökdelen;palmiyeler;bariyer direkleri;trençkot|Kadın başını kaldırıp neye bakıyor?|Başını kaldırıp kocaman bir gökdelene bakıyor.
5291|ağzı açık uyumak;gri bir kapüşonlu giymek;kapüşonu başında uyumak|tavan;boyun yastığı;koltuklar;iş adamı|Sarışın kadın ne yapıyor?|Ağzı açık uyuyor.
5292|klavyesinin üzerine yığılmak;açık bir kitabın üzerine salyasını akıtmak;kanepeye yayılmak|kanepe;çalar saat;akıllı telefon;sehpa|Ofis çalışanı ne yapıyor?|Masasında uyukluyor.
5293|toprakta kaymak;iyice eğilmek;yüz maskesi takmak|duvar;kep;eldiven;çimen|Koşucu ne yapıyor?|Toprakta kayıyor.
5294|kendine sarılmak;koridorda yürümek;kameraya gülümsemek|kadın;terlikler;kapı|Kadın ne yapıyor?|Terlikleriyle yürüyor.
5296|tahta kaşıkla karıştırmak;bir parça peynir tutmak;büyük bir kazanda kaynamak|şapka;kaşık;kâse;masa|Genç adam ne yapıyor?|Geleneksel bir yemek pişiriyor.
5297|Arnavut kaldırımlı bir yoldan yukarı yürümek;kollarını açmak;turkuaz suyu sıçratmak|gökyüzü;harabe;sırt çantası;Arnavut kaldırımlı yol|Kadın nereye yürüyor?|Eski bir harabeye doğru yürüyor.
5298|bir kâğıt şeridi koklamak;başka bir şişeye uzanmak;şaşkınlıkla soluğu kesilmek|at kuyruğu;beyaz bluz;blazer ceket;parfüm şişeleri|Kadın ne yapıyor?|Bir mağazada parfüm deniyor.
5299|cam bir kavanoz tutmak;bavulu açmak;memura gülümsemek|sucuklar;bavul;kavanoz;başörtüsü|Yaşlı kadın ne tutuyor?|Cam bir kavanoz tutuyor.
5301|ellerinin içine hapşırmak;göğsüne dokunmak;sırt çantası taşımak|gökyüzü;el;çiçekler;elbise|Sarılı kadın ne yapıyor?|Ellerinin içine hapşırıyor.
5302|başını geriye atmak;burnunu sıkmak;patika boyunca gezinmek|çiçek;park bankı;karton bardak;kapüşonlu ceket|Genç adam ne yapıyor?|Çiçek açmış bir ağacın altında hapşırıyor.
5303|kar tanelerini yakalamak;kollarını açmak;birlikte yürümek|kilise;şapka;atkı;kar|Sarılı kadın ne yapıyor?|Eliyle kar tanelerini yakalıyor.
5304|kirli avuçlarını göstermek;kiri ovarak çıkarmak;lavaboya su akıtmak|kir;lavabo;fayanslar;dolap|Kadın ne yapıyor?|Ellerindeki kiri ovarak çıkarıyor.
5306|kahverengi bir koltukta oturmak;kadının kucağında oturmak;yumruğunu kaldırmak|fotoğraflar;adam;erkek çocuk;yastık|Küçük çocuk ne yapıyor?|Kadının kucağında oturuyor.
5307|beyaz bir kupadan yudumlamak;pastel renkli pijama giymek;petrol mavisi bir mindere yaslanmak|düz ekran televizyon;köşe koltuk;döşeme tahtaları|Herkes nerede oturuyor?|Geniş bir köşe koltukta oturuyorlar.
5308|kurabiye yemek;kapıyı açmak;büyük ayçiçekleri getirmek|ayçiçekleri;kurabiye;kask;kapı|Adam ne tutuyor?|Büyük ayçiçekleri tutuyor.
5309|küçük bir nota bakmak;bir kahve fincanı tutmak;ofiste etrafına bakınmak|gözlük;fincan;not;klavye|Kadın neye bakıyor?|Küçük bir nota bakıyor.
5311|acıyla yüzünü buruşturmak;kalın bir battaniyenin altında uyuklamak;açık mavi bir kapüşonlu giymek|süs ışıkları;saksı bitkisi;minder;püskül|Arkadaşlar ne yapıyor?|Sıcacık battaniyelerin altında birbirlerine sokuluyorlar.
5312|halka şeklinde bir sucuğu ızgarada pişirmek;şişlerin üzerinde sıçramak;bir kutudan yudumlamak|soğutucu çanta;maşa;şişler;sucuk|Yeşilli adam ne yapıyor?|Halka şeklinde bir sucuğu ızgarada pişiriyor.
5313|dökümlü bir elbiseyle dönmek;bir pirinç kekini ısırmak;parmaklarıyla kalp yapmak|neon tabelalar;yaya geçidi;kot ceket;bariyer direği|Kadın ne yiyor?|Şişte bir pirinç keki yiyor.
5314|bir kar küresi tutmak;büyük bir sepet taşımak;iki şapka tutmak|şemsiye;şapkalar;kartpostallar;sepet|Genç kadın ne taşıyor?|Büyük bir sepet taşıyor.
5315|kırmızı bir şapkayı denemek;birçok kartpostal tutmak;el çırpmak|adam;şapkalar;kartpostallar;fotoğraf makinesi|Kadın ne tutuyor?|Birçok kartpostal tutuyor.
5316|katlanır bir yelpaze sallamak;kırmızı şarap yudumlamak;kollarını iki yana açmak|bukleler;şarap kadehi;patatesler;kurutulmuş jambon|Kadın ne içiyor?|Bir kadeh kırmızı şarap yudumluyor.
5317|fırfırlı eteğini savurmak;ayaklarını yere vurmak;gitar tıngırdatmak|ampuller;gökyüzü;fırfırlar;ahşap sahne|Dansçı ne yapıyor?|Fırfırlı eteğini savuruyor.
5318|mikrofona konuşmak;çenesine dokunmak;yumruğunu kaldırmak|gökyüzü;binalar;kadın;insanlar|Kadın ne yapıyor?|Mikrofona konuşuyor.
5320|bir omurga modelini çevirmek;belinin alt kısmına bastırmak;iki kolunu başının üstünde germek|jaluzi;tişört;omurga modeli;tedavi masası|Kadın adama ne gösteriyor?|Ona bir omurga modeli gösteriyor.
5321|durmadan dönmek;kollarını açmak;bir bacağını kaldırmak|mavi çizgi;patenci;buz|Patenci ne yapıyor?|Durmadan dönüyor.
5322|yeşil çorbanın tadına bakmak;dilini çıkarmak;ağzındakini tükürmek|bir kâse çorba;kupa;sos;mutfak tezgâhı|Adam ne yapıyor?|Tezgâhın üzerine sıvı tükürüyor.
5323|büyük bir taş fırlatmak;göle atlamak;gri bir şapka takmak|taş;göl;adam|Adam ne fırlatıyor?|Büyük bir taş fırlatıyor.
5324|kirli bir tavayı yıkamak;bir süngeri sıkmak;renkli bir tişört giymek|kadın;tava;sünger;lavabo|Kadın ne yapıyor?|Süngerle bir tavayı yıkıyor.
5326|acıyla ağlamak;bandaj sarmak;gri bir tişört giymek|kız;antrenör;bandaj;minder|Antrenör ne yapıyor?|Bandaj sarıyor.
5327|müşterinin topuzuna sprey sıkmak;şekillendirici bir tarağı tutmak;gösterişli bir topuzu olmak|topuz;halka küpe;kuaför önlüğü|Kuaför ne yapıyor?|Topuza saç spreyi sıkıyor.
5328|bileğine parfüm sıkmak;bileğini koklamak;kıyafetlere sprey sıkmak|bluz;pencere;kadın|Kadın ne yapıyor?|Kıyafetlere sprey sıkıyor.
5329|minicik bir tohum tutmak;küçük bir bitkiye dokunmak;bitkilerin arkasında durmak|gökyüzü;adam;tarla;bitkiler|Adam ne tutuyor?|Minicik bir tohum tutuyor.
5330|bir gazeteyi açıp kaldırmak;fotoğraf çekmek;tepsi taşımak|casus;gazete;fincan;masa|Casus ne yapıyor?|Gazetenin arkasına saklanıyor.
5331|bir portakal sıkmak;bir karpuzu ezmek;damlayan meyve suyunu toplamak|saman çatı;spor atleti;sürahi;yumruk|Güçlü kadın neyi eziyor?|Çıplak elleriyle bir karpuzu eziyor.
5332|bir tabak uzatmak;bardağa su doldurmak;kapuçino servis etmek|çıkış tabelası;kapı boşluğu;şişe;masa örtüsü|Kır saçlı adam ne yapıyor?|Bardağa su dolduruyor.
5333|merdiven çıkmak;tırabzana tutunmak;hayranlıkla yukarı bakmak|balkonlar;tırabzan;merdiven;sırt çantası|Genç adam ne yapıyor?|Merdiven çıkıyor.
5334|rulo yapılmış pankartlar taşımak;gür beyaz bir sakalı olmak;stadyumu aydınlatmak|Amerikan bayrağı;kot ceket;kapüşonlu;kol saati|Kot ceketli adam ne taşıyor?|Rulo yapılmış pankartlar taşıyor.
5335|koltuğundan fırlamak;kolları havada alkışlamak;stadyumun üzerinde parlamak|kot ceket;kot pantolon;seyirciler|Kot ceketli kadın ne yapıyor?|Kolları havada alkışlıyor.
5336|kasketini çıkarmak;kasketini sıkıca tutmak;stadyumu aydınlatmak|projektörler;bayrak;sakal;kasket|Kır sakallı adam ne yapıyor?|Kasketini sıkıca göğsüne bastırıyor.
5337|kendini videoya çekmek;başını kaldırıp çatıya bakmak;istasyona girmek|cam çatı;raylar;omuz çantası;peron|Genç adam neye bakıyor?|Başını kaldırıp cam çatıya bakıyor.
5338|ranzaya tırmanmak;ayakkabılarını çıkarmak;uzun bir elbise giymek|gökyüzü;deniz;telefon;yatak|Genç adam ne yapıyor?|Ranzaya tırmanıyor.
5339|direksiyonu sıkıca kavramak;kocaman direksiyona sırıtmak;kot gömlek giymek|sürücü koltuğu;otobüs;kot gömlek;direksiyon|Kadın ne yapıyor?|Kocaman bir direksiyonu sıkıca kavrıyor.
5340|bir top çıkarmak;tornavida kullanmak;kırmızı bir kapüşonlu giymek|garaj;çimen;yatak;çit|Çocuklar ne taşıyor?|Büyük bir kutu taşıyorlar.
5342|pembe kremanın tadına bakmak;pastel boya bir resmi havaya kaldırmak;kızın saçını örmek|dil;sıkma torbası;önlük;cupcake'ler|Kız neyin tadına bakıyor?|Pembe kremanın tadına bakıyor.
5343|lacivert bir ceket giymek;batik desenli bir kapüşonlu giymek;baskılı bir tişört giymek|priz;batik desenli kapüşonlu;boncuklar;tek kişilik yataklar|Kızlar neyin üzerinde oturuyor?|Tek kişilik yatakların üzerinde oturuyorlar.
5344|sarkan bir ipliği kesmek;beyaz keteni süslemek;gururla havaya kaldırılmak|yamalı yorgan;makaralar;pencere;halı|Kadınlar ne gösteriyor?|Yamalı bir yorgan gösteriyorlar.
5345|korkuluğa yaslanmak;böğrünü tutmak;yüzünü buruşturmak|gökyüzü;at kuyruğu;şort;korkuluk|Kadın ne yapıyor?|Korkuluğa yaslanıyor.
5346|karnını tutmak;spagetti yemek;bir kâse tutmak|karın;çatal;spagetti;kâse|Genç adam ne yiyor?|Bir kâse spagetti yiyor.
5347|trafiği durdurmak;elini kaldırmak;kollarını uzatmak|gökyüzü;otobüs;polis memuru;yol|Polis memuru ne yapıyor?|Trafiği durduruyor.
5348|kâğıtları toplamak;şemsiye tutmak;otobüse binmek|telefon kulübesi;taksi;yol;kâğıtlar|Yaşlı adam ne tutuyor?|Siyah bir şemsiye tutuyor.
"""
src = json.load(open(f'{H}/source.json')); rows = {}
for line in D.strip().splitlines():
    i, p, n, q, a = line.split('|'); rows[i] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
