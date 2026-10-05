import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """
209|kutunun içine bakmak;bir patisini içeri sokmak;kamerayı koklamak|kedi;kutu;kamera|Kedi ne yapıyor?|Meraklı kedi kutunun içine bakıyor.
142|bir sandalyede oturmak;sarı bir atkı takmak;siyah bir ceket giymek|gökyüzü;kale;köprü;su|İki kişi neyi ziyaret ediyor?|Büyük bir kaleyi ziyaret ediyorlar.
163|oğlana yardım etmek;yemeğini düşürmek;kollarını yukarı kaldırmak|lamba;yemek çubukları;el|Oğlan neyle yemek yiyor?|Yemek çubuklarıyla yemek yiyor.
429|çimene iniş yapmak;iki elini yukarı kaldırmak;mor bir ceket giymek|gökyüzü;kask;ceket;çimen|Pembeli kadın ne yapıyor?|Çimene iniş yapıyor.
531|bir partide dans etmek;çimende koşmak;havada uçmak|balon;ağaç;insanlar;köpek|İnsanlar ne yapıyor?|Bir partide dans ediyorlar.
4658|eski bir araba sürmek;sokak boyunca yürümek;koyu renk güneş gözlüğü takmak|gökyüzü;deniz;kadın;direksiyon|Kadın ne yapıyor?|Deniz kenarında araba sürüyor.
852|yemek tabakları taşımak;beyaz bir kolye takmak;restoranın içinden koşmak|lamba;garson;masa;sandalye|Garson ne yapıyor?|Masaya yemek taşıyor.
646|mor eldiven giymek;bardaktan çıkmak;ağzını kocaman açmak|eldiven;gözlük;önlük;masa|Kadının ellerinde ne var?|Ellerinde mor eldivenler var.
5580|onun ceketini düzeltmek;bir kutunun üzerinde durmak;bir tepsi tutmak|kadın;ceket;köpek;lamba|Kadın ne yapıyor?|Adamın ceketini düzeltiyor.
844|iki kolunu yukarı kaldırmak;vadiyi işaret etmek;turuncu bir ceket giymek|gökyüzü;vadi;nehir;kadın|Neye bakıyorlar?|Yeşil bir vadiye bakıyorlar.
5468|selfie çekmek;uzun bir sakalı olmak;gözlerini kocaman açmak|tabela;gökyüzü;kadın;adam|Kadın ne yapıyor?|Adamla selfie çekiyor.
5215|önde sürmek;bir köprünün üzerinden sürmek;renkli bir tişört giymek|dağ;kask;bisiklet;yol|Kadın ne yapıyor?|Yolda bisikletini sürüyor.
694|bir domates dilimlemek;bir dilimi havada tutmak;tahtanın üzerinde durmak|ceket;bıçak;domates;tahta|Adam ne yapıyor?|Bıçakla bir domates dilimliyor.
757|ona bir kutu vermek;kutuyu açmak;bir yavru köpek tutmak|gökyüzü;yavru köpek;kutu;masa|Kadın ne tutuyor?|Küçük bir yavru köpek tutuyor.
5456|pasaportunu açmak;bir kapıdan geçmek;üniforma giymek|ağaçlar;gözlük;eller;pasaport|Genç adam ne tutuyor?|Pasaportunu tutuyor.
118|matkap kullanmak;sakalı olmak;uzun saçları olmak|gökyüzü;adam;kadın;kuş|İki kişi ne yapıyor?|Büyük bir ahşap kutu yapıyorlar.
706|kırmızı bir mont giymek;yeşil bir mont giymek;büyük bir kar tanesi yakalamak|kar;eldiven;kadın;adam|Ne yapıyorlar?|Karda yatıyorlar.
395|bir kutu taşımak;anahtarları tutmak;çizgili bir tişört giymek|ev;gökyüzü;çimen;yol|Kadın ne taşıyor?|Eve bir kutu taşıyor.
4243|bir sosisli sandviçi havada tutmak;biraz sosis pişirmek;kartla ödemek|kedi;köpek;sosisli sandviç;sosisler|Kedi ne hazırlıyor?|Bir sosisli sandviç hazırlıyor.
617|mor paten giymek;yol boyunca paten kaymak;bir bankta oturmak|patenler;içecek;adam;bank|Kadın ne yapıyor?|Mor patenlerle kayıyor.
10|büyük bir yaprak tutmak;parlak yeşil renkte parlamak;yaprağın üzerine düşmek|gözlük;gömlek;yaprak;masa|Su nereye düşüyor?|Su yaprağın üzerine düşüyor.
792|sarı bir diş fırçası tutmak;tüpten çıkmak;dişlerini fırçalamak|saç;burun;diş macunu;diş fırçası|Kadın ne yapıyor?|Diş fırçasına diş macunu sürüyor.
7193|kırmızı bir traktör sürmek;beyaz bir elbise giymek;traktörün peşinden koşmak|gökyüzü;büyükanne;traktör;köpek|Büyükanne ne yapıyor?|Kırmızı bir traktör sürüyor.
365|tahta bir kaşık tutmak;mavi bir tişört giymek;buzdolabının üstünde yatmak|kedi;kulaklık;kaşık;elmalar|Kadın ne takıyor?|Büyük beyaz bir kulaklık takıyor.
5616|kollarını yukarı kaldırmak;ipleri tutmak;gökyüzünde uçmak|gökyüzü;balonlar;adam;araba|Araba neyle dolu?|Araba balonlarla dolu.
811|kupaya koşmak;kupayı kaldırmak;oyuncuları izlemek|ışıklar;kupa;masa;zemin|Oyuncular ne yapıyor?|Kupayı birlikte kaldırıyorlar.
7053|kirli bir tabağı yıkamak;bir tabağı kurulamak;beyaz bir elbise giymek|tabaklar;adam;kadın;lavabo|Ne yapıyorlar?|Bulaşık yıkıyorlar.
704|çok şiddetli hapşırmak;burnunu silmek;bir sepet taşımak|ağaç;kız;şapka;sepet|Adam ne yapıyor?|Çok şiddetli hapşırıyor.
247|kırmızı bir elma düşürmek;taşların üzerine düşmek;yere bakmak|oğlan;elma;çimen|Oğlan ne yapıyor?|Kırmızı bir elma düşürüyor.
775|bir satranç taşını oynatmak;ellerini çırpmak;masanın üzerinde yürümek|kadın;adam;kuş;masa|Adam ne yapıyor?|Bir sonraki hamlesini düşünüyor.
4710|ortada durmak;yeşil bir ceket giymek;gözlük takmak|ağaçlar;kol;adam|Üç kişi ne yapıyor?|Kollarını hareket ettiriyorlar.
4760|mavi bir ceket giymek;renkli bir elbise giymek;suyun kenarında sarılmak|gökyüzü;ceket;dondurma;elbise|İki arkadaş neyi paylaşıyor?|Bir dondurmayı paylaşıyorlar.
5007|anahtarlarını aramak;eve girmek;kilidin içinde dönmek|kilit;el;anahtarlar;kapı|Kadın ne arıyor?|Anahtarlarını arıyor.
659|adamın saçını yıkamak;lavabonun arkasında durmak;gözlerini kapatmak|şampuan;şişe;el;duvar|Kadın ne yapıyor?|Adamın saçını yıkıyor.
5609|farelerden korkmak;yerde oturmak;yan yatmak|fare;fincan;sandalye;pencere|Adam neyden korkuyor?|Fareden korkuyor.
4055|başını yukarı kaldırmak;iki oyuncağın arasında oturmak;kırmızı gözleri olmak|köpek;dinozor;yatak|Köpek nerede oturuyor?|İki dinozorun arasında oturuyor.
665|yeşil çimen yemek;ağzını kocaman açmak;çayır boyunca yürümek|koyun;duvar;gökyüzü;çimen|Koyun ne yapıyor?|Koyun çayır boyunca yürüyor.
518|bir dalda oturmak;başını çevirmek;ağaçların arasından uçmak|baykuş;dal;ağaç|Baykuş ne yapıyor?|Baykuş bir dalda oturuyor.
332|yeşil yaprak yemek;başını aşağı eğmek;biraz su içmek|zürafa;zebra;su;gökyüzü|Zürafa ne yapıyor?|Zürafa biraz su içiyor.
82|bir çiçeğin üzerinde durmak;çimenin üzerinden uçmak;bir kutunun içine girmek|arı;çiçek;yaprak|Arı ne yapıyor?|Arı bir çiçeğin üzerinde duruyor.
38|iki turuncu çubuk sallamak;adama doğru gelmek;gökyüzüne doğru uçmak|uçak;adam;kule;gökyüzü|Adam ne yapıyor?|Havalimanında iki turuncu çubuk sallıyor.
785|saatine bakmak;trenleri ve saatleri göstermek;istasyona varmak|tarife;oğlan;bank|Oğlan ne yapıyor?|Bir tarifeye bakıyor.
4058|kahverengi bir bavul hazırlamak;kırmızı bir şapka takmak;birçok bavul itmek|adam;kadın;bavullar;gökyüzü|Kadın ne yapıyor?|Birçok bavul itiyor.
7999|yatağın üstüne atlamak;sırtüstü yatmak;bavulları getirmek|köpek;kedi;yatak;pencere|Köpek ne yapıyor?|Yatakta yatıyor.
7180|havuza atlamak;bir içecek taşımak;yere düşmek|bavul;ağaçlar;gökyüzü;garson|Güneş gözlüklü adam ne yapıyor?|Havuza atlıyor.
449|bir parmağıyla işaret etmek;iki kulağını tutmak;uzun saçları olmak|ağaçlar;adam;kadın;patika|Adam ve kadın ne yapıyor?|Ağaçların altında dinliyorlar.
4568|bir haritanın üzerinde zıplamak;turuncu bir ceket giymek;kollarını iki yana açmak|kız;gökyüzü;kıta;ayakkabılar|Turunculu kız ne yapıyor?|Bir haritanın üzerinde zıplıyor.
721|çok gülmek;saçı olmamak;devrilmek|bardak;masa;kadın;oğlan|Masada ne devriliyor?|Masada bir bardak devriliyor.
7059|bir sosisli sandviç hazırlamak;ızgaranın başında durmak;ekmeğin yanında oturmak|köpek;kedi;sosisli sandviç;ekmek|Köpek ne yapıyor?|Köpek bir sosisli sandviç hazırlıyor.
5673|iki pastayı da tutmak;boş bir tabak tutmak;pencerenin yanında durmak|lamba;pencere;adam;ekmek|Kırmızılı kadın ne tutuyor?|İki pastayı da tutuyor.
670|bir alışveriş arabası itmek;ekmek ve süt satın almak;bozuk paraları almak|kadın;süt;alışveriş arabası;ekmek|Kadın ne yapıyor?|Bir alışveriş arabası itiyor.
155|biraz peynir kesmek;peynirli bir sandviç kızartmak;yerde yatmak|kadın;adam;peynir;köpek|Adam ne kızartıyor?|Peynirli bir sandviç kızartıyor.
5282|gitar çalmak;bir kaşığa şarkı söylemek;bir sahnede durmak|gökyüzü;kilise;mikrofon;gitar|Daha yaşlı adam ne yapıyor?|Gitarıyla bir şarkı söylüyor.
602|kalın bir kitap okumak;ağzını örtmek;bir fincandan içmek|pencere;kız;kitap;masa|Kız ne yapıyor?|Masada bir kitap okuyor.
4827|bir gün batımı resmetmek;bir fırça tutmak;turuncu boya kullanmak|bulutlar;boya;fırça;el|Kişi ne yapıyor?|Kişi turuncu boyayla resim yapıyor.
7853|vazoya gülümsemek;bir rafta oturmak;gümüş yüzükler takmak|lamba;kadın;kedi;vazo|Vazoya ne oluyor?|Vazo çok uzuyor.
144|kırmızı bir top yakalamak;havada uçmak;çimende koşmak|top;bulut;oğlan;çimen|Oğlan ne yapıyor?|Kırmızı bir top yakalıyor.
5012|arkadaşıyla gülmek;yaşlı bir kadını öpmek;sarışın bir kadına sarılmak|şapka;atkı;bardak;masa|Yaşlı adam ne yapıyor?|Yaşlı bir kadını öpüyor.
57|yukarı ilk çıkmak;bir parmağını kaldırmak;arkada yürümek|duvar;kadın;koltuklar|Üç kişi nerede oturuyor?|Arkada oturuyorlar.
5382|genç bir adamla konuşmak;daha yaşlı bir kadınla konuşmak;duvarda asılı durmak|ev;kadın;adam;masa|İnsanlar ne yapıyor?|Bir masada bir şey tartışıyorlar.
353|kapıyı açmak;yağmurda durmak;biraz su dökmek|misafir;çiçek;mum;pencere|Misafir ne getiriyor?|Misafir bir çiçek getiriyor.
5560|ona biraz çay vermek;sıcak çay içmek;basamakta oturmak|köpek;araba;kar;lamba|Adam ne içiyor?|Sıcak çay içiyor.
5506|bir topla oynamak;kaykay sürmek;kırmızı bir şapka takmak|gökyüzü;duvar;top;insanlar|İnsanlar ne yapıyor?|Sokakta dans ediyorlar.
4603|bisiklet sürmek;beyaz bir kask takmak;kollarını iki yana açmak|yol;gökyüzü;kask;bisiklet|Adam ne yapıyor?|Yolda bisikletini sürüyor.
122|bankta oturmak;bir alışveriş arabası tutmak;yol boyunca gitmek|otobüs durağı;bank;otobüs;yol|İnsanlar ne yapıyor?|Otobüs durağında bekliyorlar.
339|sokak boyunca gitmek;büyük bir çanta taşımak;evde kalmak|evler;araba;kız;sokak|Kız nereye gidiyor?|Sokak boyunca gidiyor.
368|dağların üzerinden uçmak;siyah bir sakalı olmak;uzun kır saçları olmak|helikopter;ev;adam;kutu|Dağların üzerinden ne uçuyor?|Dağların üzerinden kırmızı bir helikopter uçuyor.
5062|ofisin içinden yürümek;bir tablet tutmak;tahtaya çizmek|kadın;bilgisayar;telefon;fincan|Tahtaya kim çiziyor?|Patron tahtaya çiziyor.
472|bir araba tamir etmek;bir alet tutmak;kameraya gülümsemek|tamirci;araba;alet;zemin|Adam ne yapıyor?|Bir araba tamir ediyor.
680|bir şarkı söylemek;kulaklığına dokunmak;bir masada oturmak|şarkıcı;kulaklık;mikrofon;adam|Kadın ne yapıyor?|Mikrofona şarkı söylüyor.
4941|bir merdivene tırmanmak;bir ağaçta oturmak;kediye sarılmak|itfaiyeci;kedi;merdiven;ağaç|İtfaiyeci ne yapıyor?|Bir kediyi ağaçtan kurtarıyor.
3|tahtaya yazmak;bir fincandan içmek;arkasına dönüp gülümsemek|öğretmen;fincan;gözlük;tahta|Öğretmen ne yapıyor?|Tahtaya yazıyor.
30|sayfaları çevirmek;bir kitabın üzerinde uyumak;çok sayfası olmak|saç;gözlük;ders kitabı;çalışma masası|Kadın ne yapıyor?|Bir ders kitabının sayfalarını çeviriyor.
31|siyah bir çanta tutmak;dizüstü bilgisayar kullanmak;şapkasını ters takmak|ışıklar;öğrenciler;şapka;koltuklar|Öğrenciler nerede oturuyor?|Üniversitede oturuyorlar.
100|botunu bağlamak;dört bacağı olmak;gri bir ceket giymek|gökyüzü;köpek;bot;su|Kadın ne giyiyor?|Kahverengi botlar giyiyor.
288|beyaz bir takım elbise giymek;fotoğraf çekmek;gri bir kazak giymek|ağaçlar;kadın;adam;köpek|İki kişi ne giyiyor?|Büyük takım elbiseler giyiyorlar.
242|bir askıda asılı durmak;kendi etrafında dönüp durmak;ellerini çırpmak|limonlar;adam;elbise;ayna|Kadın ne yapıyor?|Kırmızı bir elbiseyle kendi etrafında dönüyor.
868|gittikçe büyümek;beyaz bir tişört giymek;koyu renk bir gömlek giymek|dalga;kadın;adam;kum|İki kişi ne yapıyor?|Büyük bir dalgadan kaçıyorlar.
4015|suyun üzerinden atlamak;koyunları izlemek;uzun ve ince olmak|ağaç;köpek;kıyı;su|Koyunlar ne yapıyor?|Suyun üzerinden atlıyorlar.
291|kollarını iki yana açmak;kadının arkasından koşmak;sıra hâlinde durmak|gökyüzü;ağaçlar;tarla;patika|Kadın ne yapıyor?|Bir tarlanın içinden koşuyor.
5108|bir tekneden el sallamak;bir evden el sallamak;davulların yakınında dans etmek|ev;çocuklar;su;tekne|Çocuklar ne yapıyor?|Bir evden el sallıyorlar.
5660|yolun karşısına geçmek;duvarı aydınlatmak;bir lambanın yanından yürüyüp geçmek|apartman;ağaç;köpek;gökyüzü|Köpek ne yapıyor?|Köpek yolun karşısına geçiyor.
807|koşu bandında koşmak;bir düğmeye basmak;yüzünü silmek|koşu bandı;tişört;pencereler;saç|Öndeki kadın ne yapıyor?|Koşu bandında koşuyor.
277|ayak parmaklarına dokunmak;bahçede zıplamak;iki başparmağını yukarı kaldırmak|tişört;bacaklar;ayakkabılar;çiçekler|Kadın ne yapıyor?|Bahçede egzersiz yapıyor.
571|bir çatal tutmak;parmağını kaldırmak;ateşin üzerinde durmak|pencere;masa;tencere;ateş|Ne pişiriyorlar?|Büyük bir tencerede patates pişiriyorlar.
4365|taze küçük ekmekler taşımak;meyveli bir turta tutmak;kırmızı bir önlük takmak|pencere;kadın;turta;küçük ekmekler|Yaşlı kadın ne taşıyor?|Taze küçük ekmekler taşıyor.
121|bir pankek yakmak;bir bez tutmak;bir tabakta durmak|adam;tava;ateş;pankek|Adam neyi yaktı?|Bir pankek yaktı.
5069|bir masajın tadını çıkarmak;bir koltukta oturmak;onun omuzlarını ovmak|bitkiler;kadın;adam;koltuk|Adam neyin tadını çıkarıyor?|Bir masajın tadını çıkarıyor.
4788|onun kulağına fısıldamak;bir sır duymak;bir çalışma masasında oturmak|bitki;kadın;bilgisayar;çalışma masası|Kadınlar nasıl görünüyor?|Kadınlar çok şoke olmuş görünüyor.
5129|bir duvarı boyamak;bandı çekip çıkarmak;turuncuya dönmek|kulaklık;örtü;duvar|Adam ne yapıyor?|Duvarı turuncuya boyuyor.
358|bir çiviye vurmak;bir çekiç tutmak;güneşte yatmak|ağaçlar;köpek;çekiç;kuş evi|Çekiç neye vuruyor?|Çekiç bir çiviye vuruyor.
819|bir şemsiye tutmak;şemsiyenin altına girmek;onun başının üzerinde açılmak|pencere;şemsiye;sokak;kadın|Kadın ne tutuyor?|Büyük kırmızı bir şemsiye tutuyor.
741|rüzgârda eğilmek;sokak boyunca yuvarlanmak;kısa bir sakalı olmak|gökyüzü;ağaç;deniz;yol|Ağaç ne yapıyor?|Ağaç fırtınada eğiliyor.
690|beyaz bir gömlek giymek;mavi bir gömlek giymek;uzun saçları olmak|gökyüzü;çimen;kadın;adam|Neye bakıyorlar?|Mavi gökyüzüne bakıyorlar.
225|çalışma masasında oturmak;mavi bir tişört giymek;çalışma masasının üzerinden yürüyüp geçmek|kitaplar;bitki;defter;çalışma masası|Kadın nerede oturuyor?|Çalışma masasında oturuyor.
92|büyük bir battaniye fırlatmak;battaniyeyi çekmek;sarı saçları olmak|pencere;kanepe;battaniye;masa|Kadın ne yapıyor?|Büyük bir battaniyenin altında oturuyor.
7809|bir dolar almak;turtanın parasını ödemek;adama gülümsemek|kadın;içecek;turta;dolarlar|Kadın ne alıyor?|Bir dolar alıyor.
731|birçok pul tutmak;bir mektup postalamak;posta kutusunun üzerinde oturmak|kuş;adam;kadın;pullar|Kadın ne yapıyor?|Bir mektup postalıyor.
800|topla koşmak;ellerini çırpmak;elini kaldırmak|gökyüzü;ışık;top;çimen|Sarılı adam ne yapıyor?|Topla koşuyor.
558|filenin üzerinden uçmak;çimende yatmak;topu havada tutmak|top;file;ağaçlar;çimen|İnsanlar ne yapıyor?|Bir topla oynuyorlar.
"""
src = json.load(open(f'{H}/source.json')); rows = {}
for l in D.strip().split('\n'):
    i, p, n, q, a = l.split('|'); rows[i] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
