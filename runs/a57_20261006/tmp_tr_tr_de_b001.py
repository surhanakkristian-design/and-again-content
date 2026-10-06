import json,os
H=os.path.expanduser('~/Projects/and-again-content/runs/a57_20261006/tr/b001')
D="""209|kutunun içine bakmak;patisini kutunun içine sokmak;kamerayı koklamak|kedi;kutu;kamera|Kedi ne yapıyor?|Kedi merakla kutunun içine bakıyor.|merakla kutunun içine bakıyor
142|tahtta oturmak;sarı bir atkı takmak;siyah deri bir ceket giymek|gökyüzü;kale;köprü;su|İkisi neyi geziyor?|Büyük bir kaleyi geziyorlar.|büyük bir kaleyi geziyorlar
163|oğlana yardım etmek;yemeğini düşürmek;kolunu havaya kaldırmak|lamba;yemek çubukları;el|Oğlan neyle yemek yiyor?|Yemek çubuklarıyla yiyor.|yemek çubuklarıyla yiyor
429|çimlere inmek;iki elini de kaldırmak;mor bir ceket giymek|gökyüzü;kask;ceket;çim|Pembeli kadın ne yapıyor?|Çimlere iniyor.|çimlere iniyor
531|bir partide dans etmek;çayırda koşmak;havada uçmak|balon;ağaç;insanlar;köpek|İnsanlar ne yapıyor?|Bir partide dans ediyorlar.|bir partide dans ediyorlar
4658|eski bir araba sürmek;yol boyunca yürümek;koyu renk güneş gözlüğü takmak|gökyüzü;deniz;kadın;direksiyon|Kadın ne yapıyor?|Deniz kenarında araba sürüyor.|deniz kenarında araba sürüyor
852|yemek dolu tabaklar getirmek;beyaz bir kolye takmak;restoranın içinde koşmak|lamba;garson;masa;sandalye|Garson ne yapıyor?|Yemeği masaya getiriyor.|yemeği masaya getiriyor
646|mor eldiven giymek;bardaktan çıkmak;ağzını kocaman açmak|eldiven;gözlük;önlük;masa|Kadının ellerinde ne var?|Mor eldiven giyiyor.|mor eldiven giyiyor
5580|adamın ceketinin düğmelerini iliklemek;bir sandığın üzerinde durmak;bir tepsi tutmak|kadın;ceket;köpek;lamba|Kadın ne yapıyor?|Adamın ceketinin düğmelerini ilikliyor.|adamın ceketinin düğmelerini ilikliyor
844|iki kolunu da kaldırmak;vadiyi göstermek;turuncu bir ceket giymek|gökyüzü;vadi;nehir;kadın|Neye bakıyorlar?|Yeşil bir vadiye bakıyorlar.|yeşil bir vadiye bakıyorlar
5468|selfie çekmek;uzun sakallı olmak;gözlerini kocaman açmak|tabela;gökyüzü;kadın;adam|Kadın ne yapıyor?|Selfie çekiyor.|selfie çekiyor
5215|diğerlerinin önünde gitmek;bir köprünün üzerinden geçmek;rengârenk bir forma giymek|dağ;kask;bisiklet;yol|Kadın ne yapıyor?|Hızlı bisiklet sürüyor.|hızlı bisiklet sürüyor
694|bir domatesi dilimlemek;bir dilimi havaya kaldırmak;kesme tahtasının üzerinde durmak|ceket;bıçak;domates;kesme tahtası|Adam ne yapıyor?|Bir domatesi dilimliyor.|bir domatesi dilimliyor
757|ona bir kutu vermek;kutuyu açmak;küçük bir köpek tutmak|gökyüzü;köpek;kutu;masa|Kadın ne tutuyor?|Küçük bir köpek tutuyor.|küçük bir köpek tutuyor
5456|pasaportunu açmak;kontrolden geçmek;üniforma giymek|ağaçlar;gözlük;eller;pasaport|Genç adam ne tutuyor?|Pasaportunu tutuyor.|pasaportunu tutuyor
118|matkap kullanmak;sakallı olmak;uzun saçlı olmak|gökyüzü;adam;kadın;kuş|İkisi ne yapıyor?|Büyük bir tahta sandık monte ediyorlar.|büyük bir tahta sandık monte ediyorlar
706|kırmızı bir ceket giymek;yeşil bir ceket giymek;büyük bir kar tanesi yakalamak|kar;eldiven;kadın;adam|İkisi ne yapıyor?|Karda yatıyorlar.|karda yatıyorlar
395|bir koli taşımak;anahtarı tutmak;çizgili bir tişört giymek|ev;gökyüzü;çim;yol|Kadın eve ne taşıyor?|Eve bir koli taşıyor.|eve bir koli taşıyor
4243|kırmızı bir önlük takmak;ızgarada sosis pişirmek;kartla ödemek|kedi;köpek;sosisli sandviç;sosisler|Kedi ne yapıyor?|Sosisli sandviç yapıyor.|sosisli sandviç yapıyor
617|mor tekerlekli paten giymek;yol boyunca paten kaymak;bir bankta oturmak|tekerlekli patenler;içecek;adam;bank|Kadın ne yapıyor?|Mor tekerlekli patenlerle kayıyor.|mor tekerlekli patenlerle kayıyor
10|büyük bir yaprak tutmak;açık yeşil parlamak;yaprağın üzerine düşmek|gözlük;gömlek;yaprak;masa|Su nereye düşüyor?|Su yaprağın üzerine düşüyor.|yaprağın üzerine düşüyor
792|sarı bir diş fırçası tutmak;tüpten çıkmak;dişlerini fırçalamak|saçlar;burun;diş macunu;diş fırçası|Kadın ne yapıyor?|Diş fırçasına diş macunu sıkıyor.|diş fırçasına diş macunu sıkıyor
7193|kırmızı bir traktör sürmek;beyaz bir elbise giymek;traktörün peşinden koşmak|gökyüzü;nine;traktör;köpek|Nine ne yapıyor?|Kırmızı bir traktör sürüyor.|kırmızı bir traktör sürüyor
365|tahta kaşık tutmak;mavi bir tişört giymek;buzdolabının üstünde yatmak|kedi;kulaklık;tahta kaşık;elmalar|Kadın ne takıyor?|Büyük beyaz bir kulaklık takıyor.|büyük beyaz bir kulaklık takıyor
5616|kollarını kaldırmak;ipleri sıkıca tutmak;gökyüzünde uçmak|gökyüzü;balonlar;adam;araba|Araba neyle dolu?|Araba balonlarla dolu.|balonlarla dolu
811|kupaya doğru koşmak;kupayı havaya kaldırmak;oyuncuları izlemek|lambalar;kupa;masa;zemin|Oyuncular ne yapıyor?|Kupayı havaya kaldırıyorlar.|kupayı havaya kaldırıyorlar
7053|kirli bir tabağı yıkamak;bir tabağı kurulamak;beyaz bir elbise giymek|tabaklar;adam;kadın;evye|İkisi ne yapıyor?|Bulaşıkları yıkıyorlar.|bulaşıkları yıkıyorlar
704|çok şiddetli hapşırmak;burnunu silmek;bir sepet taşımak|ağaç;kız;şapka;sepet|Adam ne yapıyor?|Çok şiddetli hapşırıyor.|çok şiddetli hapşırıyor
247|kırmızı bir elmayı düşürmek;taşların üzerine düşmek;yere bakmak|oğlan;elma;çim|Oğlan ne yapıyor?|Kırmızı bir elmayı düşürüyor.|kırmızı bir elmayı düşürüyor
775|uzun uzun düşünmek;ellerini çırpmak;masanın üzerinde yürümek|kadın;adam;kuş;masa|Adam ne yapıyor?|Oyun hakkında düşünüyor.|oyun hakkında düşünüyor
4710|ortada durmak;açık yeşil bir ceket giymek;gözlük takmak|ağaçlar;kol;adam|Üç kişi ne yapıyor?|Kollarını hareket ettiriyorlar.|kollarını hareket ettiriyorlar
4760|mavi bir ceket giymek;rengârenk bir elbise giymek;su kenarında birbirine sarılmak|gökyüzü;ceket;dondurma;elbise|İkisi neyi paylaşıyor?|Bir dondurmayı paylaşıyorlar.|bir dondurmayı paylaşıyorlar
5007|anahtarlarını aramak;eve girmek;kilidin içinde dönmek|kilit;el;anahtarlar;kapı|Kadın ne arıyor?|Anahtarlarını arıyor.|anahtarlarını arıyor
659|adamın saçını yıkamak;lavabonun arkasında durmak;gözlerini kapatmak|şampuan;şişe;el;duvar|Kadın ne yapıyor?|Adamın saçını yıkıyor.|adamın saçını yıkıyor
5609|farelerden korkmak;yerde oturmak;yan yatmak|fare;fincan;sandalye;pencere|Adam neden korkuyor?|Fareden korkuyor.|fareden korkuyor
4055|başını kaldırmak;iki dinozorun arasında oturmak;kırmızı gözlü olmak|köpek;dinozor;yatak|Köpek nerede oturuyor?|İki dinozorun arasında oturuyor.|iki dinozorun arasında oturuyor
665|yeşil ot yemek;ağzını kocaman açmak;çayırda yürümek|koyun;duvar;gökyüzü;ot|Koyun ne yapıyor?|Koyun çayırda yürüyor.|çayırda yürüyor
518|bir dalda oturmak;başını çevirmek;ormanın içinden uçmak|baykuş;dal;ağaç|Baykuş ne yapıyor?|Baykuş bir dalda oturuyor.|bir dalda oturuyor
332|yeşil yapraklar yemek;başını eğmek;su içmek|zürafa;zebra;su;gökyüzü|Zürafa ne yapıyor?|Zürafa su içiyor.|su içiyor
82|bir çiçeğin üzerinde durmak;çayırın üzerinde uçmak;kovanın içine girmek|arı;çiçek;yaprak|Arı ne yapıyor?|Arı bir çiçeğin üzerinde duruyor.|bir çiçeğin üzerinde duruyor
38|iki çubuk sallamak;adama doğru ilerlemek;gökyüzüne uçmak|uçak;adam;kule;gökyüzü|Adam ne yapıyor?|Havalimanında iki çubuk sallıyor.|havalimanında iki çubuk sallıyor
785|başını kaldırıp sefer tarifesine bakmak;trenleri ve saatleri göstermek;istasyona varmak|sefer tarifesi;oğlan;bank|Oğlan ne yapıyor?|Sefer tarifesini okuyor.|sefer tarifesini okuyor
4058|başını kaldırıp bavullara bakmak;kırmızı bir kep takmak;bir sürü bavul itmek|adam;kadın;bavullar;gökyüzü|Kadın ne yapıyor?|Bir sürü bavul itiyor.|bir sürü bavul itiyor
7999|yatağa atlamak;sırtüstü yatmak;bavulları getirmek|köpek;kedi;yatak;pencere|Köpek ne yapıyor?|Yatakta yatıyor.|yatakta yatıyor
7180|havuza atlamak;bir içecek tutmak;yerde yatmak|bavul;palmiyeler;gökyüzü;garson|Güneş gözlüklü adam ne yapıyor?|Havuza atlıyor.|havuza atlıyor
449|parmağıyla yukarıyı göstermek;iki elini de kulaklarına götürmek;uzun saçlı olmak|ağaçlar;adam;kadın;yol|Adam ile kadın ne yapıyor?|Çok dikkatli dinliyorlar.|çok dikkatli dinliyorlar
4568|kıtadan kıtaya atlamak;turuncu bir ceket giymek;kollarını iki yana açmak|kız;gökyüzü;kıta;ayakkabılar|Turunculu kız ne yapıyor?|Dünya haritasının üzerinde zıplıyor.|dünya haritasının üzerinde zıplıyor
721|kahkahayla gülmek;hiç saçı olmamak;masanın üzerinde devrilmek|bardak;masa;kadın;oğlan|Masanın üzerinde ne devriliyor?|Masanın üzerinde bir bardak devriliyor.|masanın üzerinde devriliyor
7059|sosisli sandviç yapmak;ızgaranın başında durmak;ekmeklerin yanında oturmak|köpek;kedi;sosisli sandviç;ekmekler|Köpek ne yapıyor?|Köpek sosisli sandviç yapıyor.|sosisli sandviç yapıyor
5673|iki pasta dilimini de havaya kaldırmak;boş bir tabak tutmak;pencerenin önünde durmak|lamba;pencere;adam;ekmekler|Kırmızılı kadın ne tutuyor?|İki pasta dilimini de tutuyor.|iki pasta dilimini de tutuyor
670|alışveriş arabası itmek;ekmek ve süt almak;bozuk paraları almak|kadın;süt;alışveriş arabası;ekmek|Kadın ne yapıyor?|Alışveriş arabası itiyor.|alışveriş arabası itiyor
155|bir parça peynir kesmek;peynirli bir sandviç kızartmak;yerde yatmak|kadın;adam;peynir;köpek|Adam ne kızartıyor?|Peynirli bir sandviç kızartıyor.|peynirli bir sandviç kızartıyor
5282|gitar çalmak;tahta kaşığa şarkı söylemek;bir sahnede durmak|gökyüzü;kilise;mikrofon;gitar|Yaşlıca adam ne yapıyor?|Gitarıyla bir şarkı söylüyor.|gitarıyla bir şarkı söylüyor
602|kalın bir kitap okumak;eliyle ağzını kapatmak;bir fincandan içmek|pencere;kız;kitap;masa|Kız ne yapıyor?|Kalın bir kitap okuyor.|kalın bir kitap okuyor
4827|bir gün batımı resmi yapmak;bir fırça tutmak;turuncu boya kullanmak|bulutlar;boya;fırça;el|Kişi ne yapıyor?|Kişi bir gün batımı resmi yapıyor.|bir gün batımı resmi yapıyor
7853|vazoya gülümsemek;bir rafta oturmak;gümüş yüzükler takmak|lamba;kadın;kedi;vazo|Vazoya ne oluyor?|Vazo hızla yukarı doğru uzuyor.|hızla yukarı doğru uzuyor
144|kırmızı bir top yakalamak;havada uçmak;çimlerin üzerinde koşmak|top;bulut;oğlan;çim|Oğlan ne yapıyor?|Kırmızı bir top yakalıyor.|kırmızı bir top yakalıyor
5012|arkadaşıyla gülmek;yaşlı bir kadını öpmek;sarışın bir kadına sarılmak|bere;atkı;bardak;masa|Yaşlı adam ne yapıyor?|Yaşlı bir kadını öpüyor.|yaşlı bir kadını öpüyor
57|yukarıya ilk çıkmak;bir parmağını kaldırmak;diğerlerinin arkasından yürümek|duvar;kadın;koltuklar|Üçü nerede oturuyor?|En arkada oturuyorlar.|en arkada oturuyorlar
5382|genç bir adamla tartışmak;yaşlıca bir kadına cevap vermek;duvarda asılı olmak|ev;kadın;adam;masa|İnsanlar ne yapıyor?|Masada oturup tartışıyorlar.|masada oturup tartışıyorlar
353|kapıyı açmak;yağmurda durmak;su doldurmak|misafir;çiçek;mum;pencere|Misafir yanında ne getiriyor?|Misafir yanında bir çiçek getiriyor.|yanında bir çiçek getiriyor
5560|ona teşekkür etmek;sıcak çay içmek;basamakta oturmak|köpek;araba;kar;sokak lambası|Adam ne içiyor?|Sıcak çay içiyor.|sıcak çay içiyor
5506|topla oynamak;kaykay sürmek;kırmızı bir kep takmak|gökyüzü;duvar;top;insanlar|İnsanlar ne yapıyor?|Sokakta dans partisi yapıyorlar.|sokakta dans partisi yapıyorlar
4603|bisiklet sürmek;beyaz bir kask takmak;kollarını iki yana açmak|yol;gökyüzü;kask;bisiklet|Adam ne yapıyor?|Yolda bisiklet sürüyor.|yolda bisiklet sürüyor
122|bankta oturmak;bir alışveriş arabası tutmak;otobüs durağına doğru gitmek|otobüs durağı;bank;otobüs;yol|İnsanlar ne yapıyor?|Otobüs durağında bekliyorlar.|otobüs durağında bekliyorlar
339|sokaktan aşağı gitmek;büyük bir çanta taşımak;evde kalmak|evler;araba;kız;sokak|Kız nereye gidiyor?|Sokaktan aşağı gidiyor.|sokaktan aşağı gidiyor
368|dağların üzerinden uçmak;siyah sakallı olmak;uzun gri saçlı olmak|helikopter;ev;adam;sandık|Dağların üzerinden ne uçuyor?|Kırmızı bir helikopter dağların üzerinden uçuyor.|dağların üzerinden uçuyor
5062|ofisin içinde yürümek;bir tablet tutmak;tahtaya çizmek|kadın;bilgisayar;telefon;fincan|Tahtaya kim çiziyor?|Kadın patron tahtaya çiziyor.|tahtaya çiziyor
472|bir araba tamir etmek;bir alet tutmak;kameraya gülümsemek|tamirci;araba;alet;zemin|Adam ne yapıyor?|Bir araba tamir ediyor.|bir araba tamir ediyor
680|bir şarkı söylemek;kulaklığına dokunmak;bilgisayarın başında oturmak|şarkıcı;kulaklık;mikrofon;adam|Kadın ne yapıyor?|Mikrofona şarkı söylüyor.|mikrofona şarkı söylüyor
4941|bir merdivene tırmanmak;ağaçta oturmak;kediyi göğsüne bastırmak|itfaiyeci kadın;kedi;merdiven;ağaç|İtfaiyeci kadın ne yapıyor?|Ağaçtan bir kedi kurtarıyor.|ağaçtan bir kedi kurtarıyor
3|tahtaya yazmak;bir fincandan içmek;sınıfa doğru dönmek|öğretmen;fincan;gözlük;tahta|Öğretmen ne yapıyor?|Tahtaya yazıyor.|tahtaya yazıyor
30|sayfaları çevirmek;ders kitabının üzerinde uyuyakalmak;çok sayfası olmak|saçlar;gözlük;ders kitabı;masa|Kadın ne yapıyor?|Kalın bir ders kitabının sayfalarını karıştırıyor.|kalın bir ders kitabının sayfalarını karıştırıyor
31|siyah bir sırt çantası tutmak;dizüstü bilgisayarda çalışmak;kepi ters takmak|lambalar;öğrenciler;kep;koltuklar|Öğrenciler nerede oturuyor?|Üniversitede oturuyorlar.|üniversitede oturuyorlar
100|botunu bağlamak;dört bacağı olmak;gri bir ceket giymek|gökyüzü;köpek;bot;su|Kadın ne giyiyor?|Kahverengi bot giyiyor.|kahverengi bot giyiyor
288|beyaz bir takım elbise giymek;beyaz spor ayakkabı giymek;gri bir kazak giymek|ağaçlar;kadın;adam;köpek|İkisi ne giyiyor?|Bol takım elbiseler giyiyorlar.|bol takım elbiseler giyiyorlar
242|bir askıda asılı durmak;kendi etrafında dönmek;ellerini çırpmak|limonlar;adam;elbise;ayna|Kadın ne yapıyor?|Kırmızı bir elbise içinde kendi etrafında dönüyor.|kırmızı bir elbise içinde kendi etrafında dönüyor
868|gittikçe büyümek;beyaz bir tişört giymek;koyu renk bir tişört giymek|dalga;kadın;adam;kum|İkisi ne yapıyor?|Büyük bir dalgadan kaçıyorlar.|büyük bir dalgadan kaçıyorlar
4015|suyun üzerinden atlamak;koyunları izlemek;uzun ve ince olmak|ağaç;köpek;kıyı;su|Koyunlar ne yapıyor?|Karşı kıyıya atlıyorlar.|karşı kıyıya atlıyorlar
291|kollarını iki yana açmak;kadının arkasından koşmak;bir sıra halinde durmak|gökyüzü;ağaçlar;tarla;yol|Kadın ne yapıyor?|Tarlanın içinden koşuyor.|tarlanın içinden koşuyor
5108|tekneden el sallamak;bir evden el sallamak;davulların arasında dans etmek|ev;çocuklar;su;tekne|Çocuklar ne yapıyor?|Bir evden el sallıyorlar.|bir evden el sallıyorlar
5660|yolun karşısına geçmek;binanın duvarını aydınlatmak;bir sokak lambasının önünden geçmek|apartman bloğu;ağaç;köpek;gökyüzü|Köpek ne yapıyor?|Köpek yolun karşısına geçiyor.|yolun karşısına geçiyor
807|koşu bandında koşmak;bir düğmeye basmak;alnını silmek|koşu bandı;tişört;pencereler;saçlar|Öndeki kadın ne yapıyor?|Koşu bandında koşuyor.|koşu bandında koşuyor
277|öne doğru eğilmek;bahçede zıplamak;iki başparmağını da kaldırmak|tişört;bacaklar;ayakkabılar;çiçekler|Kadın ne yapıyor?|Spor yapıyor.|spor yapıyor
571|gözlerini kocaman açmak;parmağını kaldırmak;ateşin üzerinde durmak|pencere;masa;tencere;ateş|Ne pişiriyorlar?|Patates pişiriyorlar.|patates pişiriyorlar
4365|fırından taze ekmekler çıkarmak;bir meyveli turta tutmak;kırmızı bir önlük takmak|pencere;kadın;meyveli turta;ekmekler|Yaşlı kadın fırından ne çıkarıyor?|Fırından taze ekmekler çıkarıyor.|fırından taze ekmekler çıkarıyor
121|bir pankeki yakmak;bir kurulama bezi tutmak;bir tabakta durmak|adam;tava;ateş;pankek|Adam neyi yaktı?|Bir pankeki yaktı.|bir pankeki yaktı
5069|masajın tadını çıkarmak;bir koltukta oturmak;onun omuzlarına masaj yapmak|bitkiler;kadın;adam;koltuk|Adam neyin tadını çıkarıyor?|Masajın tadını çıkarıyor.|masajın tadını çıkarıyor
4788|kulağına fısıldamak;bir sır duymak;bilgisayarın başında oturmak|bitki;kadın;bilgisayar;tezgâh|Kadınlar nasıl görünüyor?|Kadınlar çok şaşkın görünüyor.|çok şaşkın görünüyorlar
5129|bir duvarı boyamak;bandı sökmek;turuncu olmak|kulaklık;örtü;duvar|Adam ne yapıyor?|Duvarı turuncuya boyuyor.|duvarı turuncuya boyuyor
358|bir çivi çakmak;bir çekiç tutmak;güneşte yatmak|ağaçlar;köpek;çekiç;kuş evi|Çekiçli adam ne yapıyor?|Bir çivi çakıyor.|bir çivi çakıyor
819|bir şemsiye tutmak;şemsiyenin altına girmek;yağmuru engellemek|pencere;şemsiye;sokak;kadın|Kadın ne tutuyor?|Büyük kırmızı bir şemsiye tutuyor.|büyük kırmızı bir şemsiye tutuyor
741|rüzgârda eğilmek;yolun üzerinde yuvarlanmak;kısa sakallı olmak|gökyüzü;ağaç;deniz;yol|Ağaç ne yapıyor?|Fırtınada eğiliyor.|fırtınada eğiliyor
690|beyaz bir bluz giymek;mavi bir gömlek giymek;uzun saçlı olmak|gökyüzü;çim;kadın;adam|İkisi nereye bakıyor?|Mavi gökyüzüne bakıyorlar.|mavi gökyüzüne bakıyorlar
225|çalışma masasında oturmak;mavi bir tişört giymek;çalışma masasının üzerinde yürümek|kitaplar;bitki;defter;çalışma masası|Kadın nerede oturuyor?|Çalışma masasında oturuyor.|çalışma masasında oturuyor
92|büyük bir battaniyeyi havaya atmak;battaniyeyi çekmek;sarı saçlı olmak|pencere;kanepe;battaniye;masa|Kadın ne yapıyor?|Büyük bir battaniyenin altında oturuyor.|büyük bir battaniyenin altında oturuyor
7809|bir dolar almak;pastanın parasını ödemek;adama gülümsemek|kadın;içecek;pasta;dolarlar|Kadın ne alıyor?|Bir dolar alıyor.|bir dolar alıyor
731|bir sürü pul tutmak;bir mektubu postaya atmak;posta kutusunun üzerinde oturmak|kuş;adam;kadın;pullar|Kadın ne yapıyor?|Bir mektubu postaya atıyor.|bir mektubu postaya atıyor
800|topla koşmak;ellerini çırpmak;elini kaldırmak|gökyüzü;lamba;top;çim|Sarılı adam ne yapıyor?|Topla koşuyor.|topla koşuyor
558|filenin üzerinden uçmak;çimlerde yatmak;topu havaya kaldırmak|top;file;ağaçlar;çim|İnsanlar ne yapıyor?|Voleybol oynuyorlar.|voleybol oynuyorlar"""
src=json.load(open(f'{H}/source_de.json'));out={};err=[]
for line in D.split('\n'):
    k,p,n,q,a,r=line.split('|');p=p.split(';');n=n.split(';');s=src[k]
    assert len(p)==3 and len(n)==len(s['nouns']),k
    pm={x['text']:t for x,t in zip(s['phrases'],p)};nm=dict(zip(s['nouns'],n))
    rec=[];other=0
    for x in s['recall']:
        if x in pm: rec.append(pm[x])
        elif x in nm: rec.append(nm[x])
        else: rec.append(r);other+=1
    if other!=1: err.append(k)
    out[k]={'phrases':p,'nouns':n,'question':q,'answer':a,'captions':{},'recall':rec}
assert set(out)==set(src),set(src)-set(out)
print('err',err)
json.dump(out,open(f'{H}/de/tr.json','w'),ensure_ascii=False,indent=1)
