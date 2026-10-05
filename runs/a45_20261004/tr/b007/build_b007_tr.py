import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
D = """
443|bir el feneri tutmak;mavi bir kazak giymek;bir ata benzemek|ışık;kadın;kutular;oyuncak at|Pencereden ne giriyor?|Pencereden ışık giriyor.
444|yüzünü saklamak;gri bir tişört giymek;gökyüzünü aydınlatmak|şimşek;bulutlar;ağaç;gözlük|Neye bakıyorlar?|Şimşeğe bakıyorlar.
445|yeşil çizmelerle yürümek;mavi bir kep takmak;uzun ve beyaz olmak|çizgi;kadın;çimen;tepe|Kadın neyin üzerinde duruyor?|Beyaz bir çizginin üzerinde duruyor.
446|ağzını kocaman açmak;otların arasında yürümek;düz bir tepesi olmak|aslan;ağaç;ot|Aslan ne yapıyor?|Ağzını kocaman açıyor.
447|dudak balmını tutmak;onun dudak balmını denemek;mavi bir mont giymek|kar;köpek;atkı;dudak balmı|Kadın ne yapıyor?|Dudaklarına dudak balmı sürüyor.
448|pembe dudak parlatıcısı sürmek;alt dudağına hafifçe dokunmak;güneş gözlüğünün üzerinden bakmak|korkuluk;kâse;dudak parlatıcısı|Morlu kadın ne yapıyor?|Dudaklarına dudak parlatıcısı sürüyor.
450|güneşte oturmak;başını kaldırmak;duvara tırmanmak|kaktüs;gölge;kertenkele;taş|Kertenkele ne yapıyor?|Duvara tırmanıyor.
451|kapıyı kilitlemek;yürüyüp gitmek;kilide girmek|saç;anahtar;palto;çanta|Kadın ne yapıyor?|Kapıyı bir anahtarla kilitliyor.
452|bir logo taslağı çizmek;gür bir sakalı olmak;masanın üzerinde uyuklamak|logo;gözlük;dizüstü bilgisayar;masa|Kadın ne çiziyor?|Kâğıda bir logo taslağı çiziyor.
453|yeşil bezelye yemek;bir çatal tutmak;yalnız oturmak|oğlan;bezelye;telefon;pencereler|Oğlan ne yiyor?|Tek başına yeşil bezelye yiyor.
454|onun omzunda uyumak;bir battaniyenin altında oturmak;kadına sarılmak|adam;çorba;battaniye;botlar|Adam ne yapıyor?|Uyuyan kadına sarılıyor.
455|derin nefesler almak;kırmızı bir balon şişirmek;devasa bir boyuta ulaşmak|balon;tişört;tayt;çimenlik|Kadın ne yapıyor?|Kocaman kırmızı bir balon şişiriyor.
456|sayfaları çevirmek;bir sandalyede uyumak;mavi bir üst giymek|pencere;bitki;kedi;dergiler|İki kadın ne yapıyor?|Bir dergiye bakıyorlar.
458|kuşların peşinden koşmak;büyük bir kutu taşımak;koyu renk bir kravat takmak|gökyüzü;bina;adam;kuşlar|Genç adam ne yapıyor?|Kuşların peşinden koşuyor.
459|bir klipsli altlığa yazmak;başparmağını kaldırmak;tıraşlı bir kafası olmak|müdür;klipsli altlık;kasalar;çiçekler|Müdür ne yapıyor?|Bir klipsli altlığa yazıyor.
462|kırmızı bir şapka takmak;bir haritayla koşmak;havada uçmak|şapka;gözlük;gömlek;harita|Neye bakıyorlar?|Bir haritaya bakıyorlar.
464|pembe bir keçeli kalem kullanmak;mavi bir tişört giymek;siyah bir kuyruğu olmak|adam;kadın;keçeli kalem;masa|Kadın neyle çiziyor?|Pembe bir keçeli kalemle çiziyor.
465|bir sepet taşımak;domates satmak;biraz peynir kesmek|kadın;peynir;domatesler;sepet|Mavili kadın ne yapıyor?|Pazarda bir sepet taşıyor.
466|siyah rimel sürmek;arka planda durmak;bir sepetin içinden gizlice bakmak|rimel;şarap kadehi;makyaj fırçaları|Kızıl saçlı kadın ne yapıyor?|Kirpiklerine rimel sürüyor.
467|uzun bir vazo şekillendirmek;ellerini havaya kaldırmak;diğerlerinin üzerinde yükselmek|usta;çömlekçi çarkı;saç örgüsü;abajur|Yaşlı usta neyi şekillendiriyor?|Uzun bir vazo şekillendiriyor.
468|mor bir mat sermek;yeşil bir mat getirmek;duvarın üzerinde oturmak|gökyüzü;bitkiler;kadın;mat|Adam ve kadın ne yapıyor?|Matlarının üzerinde yoga yapıyorlar.
469|bir kibrit yakmak;siyah bir sakalı olmak;yerde yatmak|kibritler;kâse;köpek;masa|Kadın ne yapıyor?|Bir kibritle lamba yakıyor.
470|uzun bir saç örgüsü olmak;bir papatya takmak;bir gelinciğin içine girmek|gökyüzü;zirve;çayır;saç örgüsü|Çift nerede yatıyor?|Çiçek açmış bir çayırda yatıyorlar.
471|eti pişirmek;ahşap bir tahta taşımak;çimenin üzerinde oturmak|ağaçlar;et;köpek;çimen|Adam ne taşıyor?|Eti bir tahtanın üzerinde taşıyor.
473|altın bir madalyayı ısırmak;kollarını havaya kaldırmak;ellerini çırpmak|madalya;ağaç;bayraklar;kol saati|Koşucu ne yapıyor?|Altın bir madalyayı ısırıyor.
474|telefonuna uzanmak;gömleksiz meditasyon yapmak;ahşap bir altlığın üzerinde durmak|ses çanağı;teras;palmiyeler;topuz|Grup ne yapıyor?|Ahşap bir terasta meditasyon yapıyorlar.
475|bir deniz kabuğunu dinlemek;tekerlekli patenlerini bağlamak;koridor boyunca kaymak|tekerlekli patenler;bilezik;karolar;kutu|Kız neyi bağlıyor?|Tekerlekli patenlerini bağlıyor.
476|odak düğmesini ayarlamak;okülerden bakmak;bir yaprağı büyütmek|mikroskop;kurşun kalem;mercekler|Öğrenci ne yapıyor?|Mikroskoba bakıyor.
477|tabağı çıkarmak;adamın arkasında durmak;yemeği ısıtmak|mikrodalga fırın;tabak;çatal;lamba|Adam neyi çıkarıyor?|Tabağı mikrodalga fırından çıkarıyor.
478|şişeyi açmak;sakalı olmak;bir kâseden içmek|süt;kedi;çiçekler;pencere|Kedi ne yapıyor?|Bir kâseden süt içiyor.
479|şakağına hafifçe vurmak;satranç tahtasının üzerine yığılmak;onun başının üzerinde süzülmek|düşünce balonu;gözlük;satranç taşları;kıvırcık saç|Kız neyi gözünde canlandırıyor?|Satranç tahtasını zihninde canlandırıyor.
480|şişeyi açmak;suyu içmek;mavi bir tişört giymek|maden suyu;şişe;masa;adam|Kadın ne döküyor?|Bir bardağa maden suyu döküyor.
481|dizlerini bükmek;gri bir şort giymek;mor bir tişört giymek|ayna;vantilatör;ağırlıklar|Genç adam ne yapıyor?|Aynaya bakıyor.
483|büyük bir ağaca tırmanmak;bir muz yemek;bir şapka sallamak|maymun;muzlar;merdivenler;masa|Maymun ne yiyor?|Maymun bir muz yiyor.
485|kayaya yaslanmak;suyu sıkıp çıkarmak;bir kovukta tünemek|yosun;saç örgüleri;yumruk;dallar|Kadın ne yapıyor?|Yanağını yosuna yaslıyor.
486|dağa doğru çıkmak;kırmızı bir mont giymek;sarı bir mont giymek|gökyüzü;dağ;bulutlar;kar|İki kişi nerede duruyor?|Bir dağın üzerinde duruyorlar.
487|peyniri yemek;bir deliğe koşmak;sarı ışık vermek|fare;peynir;delik|Fare ne yapıyor?|Fare peyniri yiyor.
488|kızıl saçlı olmak;ellerini çırpmak;siyah bir atlet giymek|kas;sakal;ağırlıklar|Siyahlı adam ne yapıyor?|Büyük kaslarını gösteriyor.
489|bir mantarı işaret etmek;bir sepet tutmak;kırmızı ve beyaz olmak|şapka;mantar;sepet;yapraklar|Kadın neyi işaret ediyor?|Bir mantarı işaret ediyor.
490|gitar çalmak;bir şarkı söylemek;içinde madeni paralar olmak|müzisyen;gitar;bebek;madeni paralar|Müzisyen ne yapıyor?|Gitar çalıyor.
491|hardalı tatmak;bir fırça tutmak;bir tepsi taşımak|hardal;kâse;adam;pencere|Adam neyi tadıyor?|Bir kâseden hardal tadıyor.
492|tırnaklarını boyamak;arkadaşına gülmek;küçük bir fırça tutmak|oje;bardak;masa;kuş|Sarılı kadın ne yapıyor?|Tırnaklarını boyuyor.
495|otları yemek;gri bir mont giymek;yeşil bir mont giymek|geyikler;nehir;taşlar;ot|Geyikler ne yapıyor?|Bir nehrin kenarında ot yiyorlar.
496|bir kolye takmak;arkadaşının arkasında durmak;beyaz bir gömlek giymek|kolye;ayna;çiçekler;gömlek|Beyazlı kadın ne takıyor?|Renkli bir kolye takıyor.
498|biraz su içmek;sahneyi işaret etmek;bir gitar taşımak|ışıklar;insanlar;adam;gitar|Kim gergin?|Gitarlı adam gergin.
499|bir gazetenin arkasına saklanmak;yeşil bir gömlek giymek;gazeteyi katlamak|gazete;kahve;kruvasan;masa|Kadın neyin arkasına saklanıyor?|Büyük bir gazetenin arkasına saklanıyor.
500|savunma oyuncusunu çalımla geçmek;hücum oyuncusunun yolunu kesmek;kaleye doğru depar atmak|projektör;kale;savunma oyuncusu;futbol topu|Hücum oyuncusu ne yapıyor?|Savunma oyuncusunu çalımla geçiyor.
501|mavi kapıyı açmak;kadına gülümsemek;dört ayak üzerinde yürümek|ay;adam;kedi|Adam ne yapıyor?|Gece vakti sokak boyunca yürüyor.
502|bir pusula tutmak;mavi bir şapka takmak;onun elinde durmak|gökyüzü;adam;güneş;kadın|Pusula neyi gösteriyor?|Pusula kuzeye giden yolu gösteriyor.
503|bir deftere yazmak;ellerini çırpmak;sayfaları çevirmek|defter;bardak;kalemler;masa|Morlu kadın ne yapıyor?|Yeni bir deftere yazıyor.
505|bir ceviz kırmak;uzun saçlı olmak;cevizlerle dolu olmak|adam;kadın;cevizler;masa|Adam ne yapıyor?|Bir ceviz kırıyor.
506|bir yumurta kırmak;sırt çantasını kapmak;üzerinde orman meyveleri olmak|kapı aralığı;servis tabağı;mango;yulaf|Adam ve kadın ne hazırlıyor?|Taze malzemelerden oluşan bir servis tabağı hazırlıyorlar.
507|bir böceği yakından gözlemlemek;bir kamışa konmak;bir derenin yanında çömelmek|büyüteç;yusufçuk;dere;at kuyruğu|Kız ne yapıyor?|Bir yusufçuğu büyüteçle gözlemliyor.
508|teknenin yakınında zıplamak;sarı bir mont giymek;kırmızı bir mont giymek|gökyüzü;okyanus;yunuslar;tekne|Yunuslar ne yapıyor?|Okyanustan dışarı zıplıyorlar.
509|yağı dökmek;ekmeği yağa batırmak;biraz ekmek yemek|ekmek;yağ;domatesler;pencere|Adam ne yiyor?|Yağla ekmek yiyor.
511|bir soğan kesmek;koruyucu gözlük takmak;ellerini çırpmak|soğan;koruyucu gözlük;pencere;kadın|Adam ne kesiyor?|Bir soğan kesiyor.
512|aynaya bakmak;yeşil bir tişört giymek;bir ayakkabıyı yerden almak|ceket;pantolon;ayakkabılar;şapka|Kadın ne yapıyor?|Aynada kıyafetine bakıyor.
513|hasırın üzerinde yürümek;masanın altında durmak;gri bir çatısı olmak|gökyüzü;ev;tencere;çimen|İnsanlar nerede yemek yiyor?|Evin dışında yemek yiyorlar.
514|saçını örtmek;sakalı olmak;fırında pişmek|pencere;fırın;ekmek;eldiven|Ne yapıyorlar?|Ekmeği fırından çıkarıyorlar.
516|musluğu kapatmak;bir su birikintisinin içinde durmak;sabunlu suyla taşmak|havlu;musluk;çamaşır makinesi;su birikintisi|Lavabonun nesi var?|Lavabo taşıyor ve su yere akıyor.
519|bir çanta hazırlamak;kitapların yanında durmak;çantayı kaldırmak|kitaplar;şişe;çanta;yatak|Kişi ne yapıyor?|Kişi kitapları bir çantaya yerleştiriyor.
520|kanoyla kürek çekmek;bir şapkanın altında uyuklamak;nehrin üzerinde yükselmek|bambu;kayalıklar;kürek;güneş şapkası|Genç kadın ne yapıyor?|Kanoyla kürek çekerek kayalıkların yanından geçiyor.
521|bir sepet taşımak;pencerenin altında durmak;ayağını tutmak|pencere;yatak;sepet;giysiler|Adam ne yapıyor?|Acı içinde ayağını tutuyor.
522|denizin resmini yapmak;ellerini çırpmak;duvarın üzerinde yatmak|gökyüzü;tablo;kedi;kadın|Kadın ne yapıyor?|Denizin resmini yapıyor.
523|büyük bir tava tutmak;sebze pişirmek;ellerini çırpmak|tava;tabak;pencere;adam|Adam ne yapıyor?|Bir tavada sebze pişiriyor.
524|telaşla ceplerini yoklamak;çantasını karıştırmak;başını ellerinin arasına almak|bez çanta;cüzdan;saç fırçası;anahtarlar|Kadın ne yapıyor?|Bez çantasını karıştırıyor.
525|sayfaları birbirine tutturmak;dikdörtgen gözlük takmak;kâğıtları uçurmak|ataş;cam kap;masa vantilatörü;askılı bitki|Kadın ne yapıyor?|Sayfaları bir ataşla tutturuyor.
527|bir paket açmak;turuncu bir gömlek giymek;bahçe kapısının arasından bakmak|paket;köpek;ev;gökyüzü|Kadın ne yapıyor?|Bir paket açıyor.
530|kırmızı bir kanadını açmak;başını çevirmek;bir çitin üzerinde durmak|papağan;çiçekler;yapraklar;çit|Papağan ne yapıyor?|Papağan bir çitin üzerinde duruyor.
532|gol atmak;gri bir tişört giymek;yerde yuvarlanmak|kadın;top;kale;gökyüzü|Oyuncular ne yapıyor?|Topla paslaşıyorlar.
533|pasaportunu öpmek;onun pasaportunu kontrol etmek;bir bavul çekmek|pasaport;güneş gözlüğü;ceket;banko|Kadın neyi öpüyor?|Pasaportunu öpüyor.
535|makarnayı pişirmek;bir tabaktan yemek;pencerenin yanında yatmak|makarna;tabak;kedi;kadın|Kadın ne yiyor?|Bir tabaktan makarna yiyor.
536|bir hamağa yerleşmek;onun kucağına tırmanmak;bir taburenin üzerinde durmak|hamak;sarman kedi;kupa;palmiye yaprağı|Kadın ne yapıyor?|Bir hamakta dinleniyor.
537|kırmızı bir elma soymak;küçük bir bıçak kullanmak;yerde durmak|elma;sepet;ağaç;bulutlar|Kız ne yapıyor?|Kırmızı bir elma soyuyor.
538|kameraya gülümsemek;mavi bir çizgi bırakmak;masanın üzerinde durmak|tükenmez kalem;şapka;gömlek|Adam ne tutuyor?|Yeşil bir tükenmez kalem tutuyor.
541|bir kurşun kalemle çizmek;ellerini çırpmak;pencerede oturmak|kurşun kalem;kedi;meyve;defter|Kadın ne yapıyor?|Bir kurşun kalemle çiziyor.
542|karın üzerinde yürümek;karnının üzerinde kaymak;buzun altında yüzmek|gökyüzü;su;penguen;kar|Penguen ne yapıyor?|Karın üzerinde kayıyor.
543|makarnaya karabiber koymak;koluna hapşırmak;makarnasını göstermek|pencere;adam;makarna|Adam ne yapıyor?|Makarnasına karabiber koyuyor.
545|renkli lobutlarla jonglörlük yapmak;seyircilerin yanında oturmak;kot bir ceket giymek|seyirciler;jonglörler;şapka;parke taşları|Jonglörler ne yapıyor?|Bir sokak gösterisinde lobutlarla jonglörlük yapıyorlar.
546|parfüm sıkmak;parfümü koklamak;sarı bir eşarp takmak|ağaç;kadın;parfüm;masa|Mavili kadın ne yapıyor?|Koluna parfüm sıkıyor.
547|telefonda konuşmak;gözlük takmak;elini sallamak|telefon;masa;çiçekler|Gözlüksüz kadın ne yapıyor?|Telefonda konuşuyor.
548|vizörden bakmak;duvarın önünde poz vermek;ekranı işaret etmek|fotoğraf makinesi;parke taşları;gökyüzü;adam|Adam ne yapıyor?|Duvarın önünde poz veriyor.
549|altın bir halka takmak;yatağın üzerinde uzanmak;kulak memesini işaret etmek|piercing;bukleler;ampul;takı tepsisi|Kadın ne yapıyor?|Kulağındaki piercinge bir halka takıyor.
550|çamurda yatmak;domuzun arkasında durmak;bir kovadan içmek|domuz;kova;adam;çit|Domuz neyden içiyor?|Domuz bir kovadan içiyor.
551|sandalyelerin arasında yürümek;bir çeşmenin üzerinden uçmak;bir çatıya konmak|gökyüzü;güvercin;çatı;duvar|Güvercin nereye konuyor?|Bir çatıya konuyor.
553|sahayı biçmek;bir korner bayrağı dikmek;arka planda antrenman yapmak|kasket;oyuncular;saha;korner bayrağı|Saha görevlisi ne yapıyor?|Saha görevlisi sahayı biçiyor.
554|bir hasır taşımak;bir yer aramak;bir hasırın üzerinde oturmak|şemsiye;deniz;kadın;hasır|Kadın ne arıyor?|Oturacak bir yer arıyor.
555|bir yaprağı işaret etmek;büyük bir yaprağı temizlemek;ön ayaklarını kaldırmak|pencere;kadın;bitkiler;kedi|Kadın neyi işaret ediyor?|Bir bitkiyi işaret ediyor.
556|bir parmağını havaya kaldırmak;küçük bir kutu açmak;bir yara bandı yapıştırmak|yara bandı;kedi;pencere;kitap|Adam ne yapıyor?|Onun parmağına bir yara bandı yapıştırıyor.
557|bir tabağı temizlemek;büyük bir tabak taşımak;bir masada oturmak|tabak;makarna;tava|Adam ne taşıyor?|Büyük bir tabak makarna taşıyor.
559|topla koşmak;dizlerinin üzerine düşmek;çimenin üzerinde yuvarlanmak|oyuncu;top;kale;çimen|Sarılı oyuncu ne yapıyor?|Topla koşuyor.
560|bir selfie çekmek;ağzını kocaman açmak;suyla dolu olmak|çeşme;heykel;gökyüzü|Kadın ne yapıyor?|Bir selfie çekiyor.
561|ona bir parça ikram etmek;küçük bir parçayı kabul etmek;bir kese kâğıdını sıkıca tutmak|rastalar;bere;kruvasan;atkı|Kadın ne yapıyor?|Büyük bir zevkle kruvasan yiyor.
562|bir fişi havaya kaldırmak;mavi bir fincan tutmak;odayı aydınlatmak|kadın;fiş;fincan;el|Kadın ne tutuyor?|Beyaz bir fiş tutuyor.
563|ceplerine bakmak;iki kahve bardağı tutmak;bir duvarın üzerinde oturmak|kuş;anahtarlar;bardak;cep|Kızıl saçlı adam ne yapıyor?|Ceplerine bakıyor.
564|en yüksek bloğu itmek;asker selamı vermek;en üst basamakta yer almak|tavan;eşofman;yumruk;kürsü|Kazanan nerede duruyor?|Kürsünün en üstünde duruyor.
565|bir aşçının elini sıkmak;iki yumruğunu da kaldırmak;yeşil boyayı silmek|kubbe;tuval;şövale;parke taşları|İki aday ne yapıyor?|Kalabalığın önünde el sıkışıyorlar.
566|paslı bir varili boşaltmak;metal bir kova kaldırmak;suyun üzerinde havada durmak|at kuyruğu;yağmurluk;nehir;kova|Adam ne yapıyor?|Bir varili nehre boşaltıyor.
567|balıkları işaret etmek;bir yaprağın üzerinde oturmak;suyun altında yüzmek|çiçekler;salyangoz;gölet;taşlar|Kadın neyi işaret ediyor?|Göletteki balıkları işaret ediyor.
568|turuncu bir simidin üzerinde yatmak;havuza koşmak;arkadaşının ardından atlamak|çiçekler;sandalyeler;simit;havuz|İki adam ne yapıyor?|Havuza atlıyorlar.
"""
out = {}
for line in D.strip().splitlines():
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
src = json.load(open(f'{HERE}/source.json'))
out = {i: out[i] for i in src}
json.dump(out, open(f'{HERE}/tr.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
