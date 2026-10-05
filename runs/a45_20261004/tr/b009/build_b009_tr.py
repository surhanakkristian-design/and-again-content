import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """
702|spor ayakkabılarını giymek;ayakkabılarını bağlamak;merdivenlerden zıplayarak çıkmak|spor ayakkabılar;çoraplar;bacaklar;gökyüzü|Kadın ne yapıyor?|Spor ayakkabılarını giyiyor.
705|çiçekleri koklamak;burnuna dokunmak;gri bir kapüşonlu sweatshirt giymek|çiçekler;ceket;adam;kot pantolon|Kadın ne yapıyor?|Koluna hapşırıyor.
707|bir snowboard takmak;tepeden aşağı kaymak;koyu renk bir ceket giymek|snowboard;kask;kar;gökyüzü|Mavili adam ne yapıyor?|Snowboardla tepeden aşağı kayıyor.
708|sabunu eline almak;ellerini yıkamak;ellerine bakmak|sabun;musluk;baloncuk;eller|Adam ne yapıyor?|Ellerini sabunla yıkıyor.
710|bir kalıp sabunu köpürtmek;köpüğü durulamak;sevinçle alkışlamak|köpük;musluk;kalıp sabun;önlük|Kadın ne yapıyor?|Ellerindeki köpüğü duruluyor.
711|bir şarj aletini takmak;bir buzlu kahve yudumlamak;pencere pervazında uyuklamak|priz;telefon;kablo;ev bitkisi|Adam ne yapıyor?|Şarj aletini prize takıyor.
712|bir teneke kutudan içmek;portakallı gazoz koymak;arkadaşına gülmek|teneke kutu;buz;gazoz|Mavili adam ne yapıyor?|Bir bardağa gazoz koyuyor.
713|fideleri sulamak;bir solucanı incelemek;küreğin üzerine tünemek|toprak;kürek;süzgeçli kova;kızılgerdan|Kadın ne yapıyor?|Topraktaki fideleri suluyor.
714|bir kapıdan geçmek;ailesine koşmak;omzundan sarkmak|şapka;asker;çanta;ayakkabılar|Asker ne yapıyor?|Ailesine koşuyor.
715|sarı bir not tutmak;kahvesini içmek;klavyede yazı yazmak|not;fincan;kadın;klavye|Kadın ne tutuyor?|Sarı bir not tutuyor.
716|sebze çorbası içmek;adamın arkasında oturmak;masanın üzerinde yanmak|çorba;el;ekmek;çorba kaşığı|Adam ne içiyor?|Sebze çorbası içiyor.
717|bir tencerede çorba pişirmek;bir kâseden yemek;adamın yanında uyumak|pencere;çorba;adam;kedi|Adam ne yapıyor?|Bir kâseden çorba içiyor.
718|kuşları işaret etmek;gökyüzünde uçmak;tarlanın üzerinde parlamak|gökyüzü;kuşlar;güneş;duvar|Kadın neyi işaret ediyor?|Kuşları işaret ediyor.
719|mor bir kazak giymek;gri bir kazak giymek;karanlıkta parlamak|yıldızlar;kız;oğlan|Neye bakıyorlar?|Yıldızlara bakıyorlar.
720|kırmızı baharatı serpmek;kâğıt külahı koklamak;yemeklik yağı ısıtmak|başörtüsü;sakal;baharat;tava|Baharatla ne yapıyor?|Onu tavaya serpiyor.
723|belini sıkıca tutmak;omurgayı işaret etmek;metal bir ayaklıkta asılı durmak|kürek kemiği;kaburgalar;omurga;parmak|Doktor neyi işaret ediyor?|Omurgayı işaret ediyor.
724|havuza atlamak;çok yükseğe çıkmak;suda gülmek|su sıçraması;güneş;kule;şemsiyeler|Havuzda ne görebilirsin?|Havuzda büyük bir su sıçraması var.
726|parmağıyla işaret etmek;ceketini çıkarmak;göleti yüzerek geçmek|çiçekler;çimen;kadın;adam|Adam ne çıkarıyor?|Ceketini çıkarıyor.
727|sprinti kazanmak;soluklanmak;bitiş çizgisini işaretlemek|kurdele;saç örgüsü;spor ayakkabılar;koşu pisti|Koşucu ne yapıyor?|Bitiş çizgisine doğru depar atıyor.
729|bir ağaca tırmanmak;bir fındık yemek;bir dal boyunca koşmak|sincap;fındık;dal;yapraklar|Sincap ne yiyor?|Sincap bir fındık yiyor.
734|eti kesmek;adamı izlemek;çatalla yemek|çatal;köpek;biftek;bıçak|Adam ne yapıyor?|Bıçakla bir biftek kesiyor.
735|gözlüğünü çıkarmak;kapağı geri koymak;pencerenin yanında yatmak|buhar;adam;çaydanlık;tencere|Tencereden ne çıkıyor?|Tencereden buhar çıkıyor.
736|damadı öpmek;gelini öpmek;çilli bir yüzü olmak|ahşap tabela;güller;gelin;yeşil takım elbise|Gelin ne yapıyor?|Düğünlerinde damadı öpüyor.
738|buzdolabını açmak;buzdolabının üzerinde asılı durmak;siyah bir çanta taşımak|yapışkan not;adam;çanta;buzdolabı|Yapışkan not nerede?|Yapışkan not buzdolabının üzerinde.
739|sokak boyunca yürümek;“dur” kelimesini göstermek;biraz pizza yemek|adam;fırın;pizza;tekerlek|Adam ne yapıyor?|Bir dilim pizza yiyor.
740|pistte depar atmak;sprinterin süresini tutmak;kadrana gözünü dikmek|kronometre;başparmak;ip;yen|Adam ne yapıyor?|Kronometreyle sprinterin süresini tutuyor.
742|tahta bir kaşık tutmak;bir çaydanlık tutmak;pencerenin altında oturmak|ocak;çaydanlık;kedi;pencere|Ne yapıyorlar?|Ocakta yemek pişiriyorlar.
743|yolu işaret etmek;mavi bir gömlek giymek;bir gözünü kapatmak|gökyüzü;kep;yol;ayakkabı|Kadın neyi işaret ediyor?|Düz bir yolu işaret ediyor.
744|bir şemsiye tutmak;kâğıtlarını düşürmek;otobüse binmek|şemsiye;otobüs;adam;kâğıtlar|Adam ne tutuyor?|Onun üzerine bir şemsiye tutuyor.
746|suyu sıçratmak;küçük bir kayık tutmak;bir kayanın üzerinde durmak|gökyüzü;kadın;dere;çimen|Neyin üzerinden atlıyorlar?|Bir derenin üzerinden atlıyorlar.
749|onun bacağına dokunmak;yeşil bir tişört giymek;suyun kenarında yürümek|ağaçlar;ördek;su;çimen|Ne yapıyorlar?|Ağaçların altında esneme hareketleri yapıyorlar.
750|ipi bağlamak;kutuyu yukarı çekmek;pencerenin yanında oturmak|kuş;ip;kadın;kutu|Kadın ne yapıyor?|Bir kutuyu iple bağlıyor.
751|kendinden emin bir poz vermek;bej ceketi reddetmek;uzun bir at kuyruğu olmak|atkı;kareli ceket;platform botlar;ayna|Mavi saçlı kız ne yapıyor?|Kendinden emin bir poz veriyor.
752|sade kahve içmek;beyaz bir tişört giymek;şekerle dolu olmak|fincan;şeker;masa;pencere|Kadın ne içiyor?|Bir fincan sade kahve içiyor.
753|mavi bir ceket giymek;aynaya bakmak;adamın koluna dokunmak|takım elbise;ayna;elbise;ayakkabılar|Adamın üzerinde ne var?|Üzerinde mavi bir takım elbise var.
754|metal çubuğu kavramak;barfiks çekmekte zorlanmak;arkadaşının ayaklarını desteklemek|barfiks demiri;kapüşonlu sweatshirt;askılı atlet;topuz|Grili kadın ne yapıyor?|Arkadaşının ayaklarını destekliyor.
755|talaşı süpürmek;pencereleri yansıtmak;cilalı taşın üzerinde yuvarlanmak|ahşap tekerlek;önlük;taş yüzey;ağaçlar|Ahşap tekerlek ne yapıyor?|Taş yüzeyin üzerinde yuvarlanıyor.
756|bir sörf tahtası taşımak;bir dalganın üzerinde kaymak;kadını izlemek|sörf tahtası;kadın;adam;gökyüzü|Kadın ne taşıyor?|Bir sörf tahtası taşıyor.
758|tüylerini temizlemek;kanatlarını açmak;suyun üzerinde koşmak|kuğu;su;ağaçlar;gökyüzü|Kuğu ne yapıyor?|Suyun üzerinde koşuyor.
759|bir kazak giymek;pencereden dışarı bakmak;kadına bakmak|kazak;fincan;köpek;pencere|Kadının üzerinde ne var?|Üzerinde büyük bir kazak var.
760|bir çorabı çekip çıkarmak;şişmiş bir ayak bileğini dürtmek;içme suyu içermek|ayak bileği;buz torbası;askılı atlet;ağaçlar|Ayak bileğine ne oluyor?|Ayak bileği şişiyor.
761|şokla nefesi kesilmek;acıyla yüzünü buruşturmak;onun ayaklarını desteklemek|buz torbası;gözlük;şişlik;yastık|Adam ne yapıyor?|Şişliğin üzerine bir buz torbası koyuyor.
762|bir tişört giymek;yatağın üzerinde oturmak;ellerini çırpmak|tişört;kadın;pencere;yatak|Adam ne yapıyor?|Bir tişört giyiyor.
763|havada süzülmek;masanın üzerinde dolaşmak;denizin üzerinde batmak|masa örtüsü;vazo;deniz;güneş|Ne yapıyorlar?|Masa örtüsünü masanın üzerine seriyorlar.
764|bir tablet tutmak;parmağıyla çizmek;pencerenin dışında büyümek|tablet;kaktüs;fincan;gözlük|Adam ne çiziyor?|Tablette bir kaktüs çiziyor.
766|koluna bakmak;göğsüne dokunmak;bir çizim göstermek|dövme;kâğıt;bitki;gözlük|Kadın neye bakıyor?|Yeni dövmesine bakıyor.
767|çayı koymak;çayına üflemek;yerde yatmak|çay;tepsi;bitki;atkı|Adam ve kadın ne içiyor?|Küçük bardaklardan çay içiyorlar.
768|beyaz bir şapka takmak;havaya yükselmek;gölün üzerinde parlamak|takım;tekne;güneş;göl|Takım ne yapıyor?|Takım bir gölde teknede kürek çekiyor.
769|pencerenin yanında uyumak;sakalı olmak;uzun saçları olmak|çay kaşığı;kedi;şeker;çay|Adam ne tutuyor?|Bir çay kaşığı tutuyor.
770|yere düşmek;turuncu bir gömlek giymek;siyah kıyafetler giymek|top;raket;ağaçlar;file|Kadın ne yapıyor?|Tenis oynuyor.
771|yürüyen merdivenle yukarı çıkmak;uçakları seyretmek;apronda beklemek|yürüyen merdiven;saksı bitkisi;bavul;hırka|Kadın ne çekiyor?|Terminal boyunca bir bavul çekiyor.
772|bir yastığa sıkıca sarılmak;gözyaşlarını silmek;kâğıt mendilleri uzatmak|yastık;saç bandı;hırka;kâğıt mendiller|Genç kadın neye sıkıca sarılıyor?|Kucağındaki bir yastığa sıkıca sarılıyor.
776|bir şişeyi başına dikmek;susuzluktan muzdarip olmak;uzaktaki bir tarlaya su püskürtmek|plastik şişe;tel sepet;bisiklet zili|Bisikletçi neden muzdarip?|Susuzluktan muzdarip.
777|bir bardaktan içmek;ağzını silmek;boş bir şişe tutmak|bardak;şişe;domatesler;gömlek|Susamış adam ne yapıyor?|Bir bardaktan su içiyor.
778|bir makarayı yukarıda tutmak;ipliği kesmek;masanın üzerinde dolaşmak|iplik;sepet;mezura|Bejli kadın ne tutuyor?|Uzun kırmızı bir iplik tutuyor.
779|bir kola sokulmak;huzur içinde uyuyakalmak;tüylü bir yanağı okşamak|su samuru;kol;başparmak;yen|Su samuru ne yapıyor?|Bir kola sokuluyor.
780|solda durmak;iki patisini de yukarı kaldırmak;dört ayak üzerinde yürümek|kediler;kapı;yatak|Üç kedi ne yapıyor?|Bir yatağın üzerinde duruyorlar.
781|ekmek yapmak;sağda oturmak;masanın altında yatmak|pencere;mum;masa;köpek|Köpek ne yapıyor?|Masanın altında yatıyor.
782|bir kravat bağlamak;beyaz bir gömlek giymek;pencerenin dışında oturmak|kuş;kadın;gömlek;kravat|Kadın ne yapıyor?|Adamın kravatını bağlıyor.
783|otların arasında yürümek;suyun içinde durmak;ağzını açmak|ağaçlar;kaplan;su|Kaplan ne yapıyor?|Suyun içinde duruyor.
784|plaj şemsiyesini eğmek;sandalyesine yerleşmek;biraz gölge sağlamak|plaj şemsiyesi;güneş gözlüğü;tulum;şezlong|Kadın ne yapıyor?|Plaj şemsiyesini eğiyor.
786|ağır bir kutu taşımak;oturup dinlenmek;ahşaptan yapılmış olmak|duvar;kum;adam;kutu|Adam nasıl hissediyor?|Çok yorgun.
787|kaşlarını kaldırmak;beyaz bir bluz giymek;bir kol saati takmak|sütun;güneş gözlüğü;bilezik;kol saati|Siyahlı kadın ne yapıyor?|Arkadaşına bakıp kaşlarını kaldırıyor.
789|kızarmış ekmeğini ısırmak;ekmeği ısıtmak;yerde oturmak|sakal;reçel;ekmek;ekmek kızartma makinesi|Adamlar neye bakıyor?|Ekmek kızartma makinesine bakıyorlar.
790|bir domates kesmek;gri bir atkı takmak;bitkilerin arasında yürümek|domates;güneş;adam|Adam ne kesiyor?|Kırmızı bir domates kesiyor.
791|bir alet almak;bir aleti işaret etmek;bisikletin arkasında durmak|aletler;el;adam;duvar|Pembeli adam ne alıyor?|Duvardan bir alet alıyor.
793|büyük bir taş kaldırmak;en üste taşlar koymak;kollarını açmak|kadın;taşlar;gökyüzü;çimen|Kadın ne yapıyor?|En üste bir taş koyuyor.
794|ahşap portreleri yeniden dizmek;şampiyonu taşımak;dev bir rakibi yenmek|fenerler;sakal;önlük;kalabalık|Sakallı adam ne yapıyor?|Şampiyonu omuzlarında taşıyor.
797|uzun sarı saçları olmak;beyaz bir üstle koşmak;kollarını iki yana açmak|gökyüzü;güneş;çimen;pist|Nerede koşuyorlar?|Bir pistte koşuyorlar.
801|yukarı aşağı zıplamak;ellerini çırpmak;çimenlerin üzerinde yürümek|adam;kadın;trambolin;çimen|Kadın ne yapıyor?|Bir trambolinde zıplıyor.
802|bir mikrofon tutmak;kâğıttan bir top atmak;dört bacağı olmak|pencere;köpek;çöp kutusu|Adam kâğıdı nereye koyuyor?|Onu çöp kutusuna koyuyor.
804|iki pasaport tutmak;koltukların arasında yürümek;pencerenin dışında olmak|gökyüzü;arabalar;çimen;yol|Gülümseyen kadın nasıl seyahat ediyor?|Uçakla seyahat ediyor.
805|bir sırt çantası taşımak;şort giymek;istasyonda beklemek|dağlar;sırt çantası;harita;kol saati|Ne tutuyorlar?|Bir harita tutuyorlar.
806|dolu bir tepsi taşımak;tepsiyi bırakmak;barın arkasında durmak|kadın garson;cezve;tepsi;masa|Kadın garson ne taşıyor?|Dolu bir tepsi taşıyor.
808|mavi bir ceket giymek;kırmızı bir tişört giymek;bir tarlada büyümek|ağaç;kadın;adam;çimen|Nereye yürüyorlar?|Büyük bir ağaca doğru yürüyorlar.
809|eliyle ağzını kapatıp kıkırdamak;bir şapka denemek;sokak boyunca tıpış tıpış yürümek|tente;yoldan geçen biri;tezgâh;corgi|Genç adam ne deniyor?|Sarı bir balıkçı şapkası deniyor.
812|bir ipten sarkmak;ipi aşağıdan emniyete almak;kollarını iki yana açmak|ip;tırmanış kemeri;uçurum;ağaçlar|Tırmanıcı ne yapıyor?|Bir ipten sarkıyor.
813|büyük kuyruğunu göstermek;ağzını kocaman açmak;kuru otların üzerinde durmak|hindi;kuyruk;çit;kuru ot|Hindi ne yapıyor?|Kuru otların üzerinde duruyor.
814|vantilatörü kapatmak;yavaşlayıp durmak;çatıdan sarkmak|lamba;pencere;vantilatör;kız|Kız ne yapıyor?|Vantilatörü kapatıyor.
815|kumun üzerinde yürümek;denize girmek;suyun altında yüzmek|gökyüzü;kaplumbağa;kum|Kaplumbağa nereye gidiyor?|Denize giriyor.
816|bir ceketi iliklemek;kendi yansımasına hayranlıkla bakmak;zümrüt yeşili bir gece elbisesi giymek|ayna;papyon;smokin;gece elbisesi|Adam ne yapıyor?|Aynada smokinine hayranlıkla bakıyor.
817|kabarık beyaz tüyleri olmak;siyah bir kuyruğu sallamak;ufukta parıldamak|gökyüzü;ufuk;dalgalar;beton blok|İki kedi ne yapıyor?|Yan yana oturuyorlar.
818|iki kolunu da havaya savurmak;koyu renk bir sakalı olmak;pencerenin yanında yürümek|pencere;kedi;klavye;masa|Kadın ne yapıyor?|Klavyede yazı yazıyor.
821|iç çamaşırı giymek;bir ceketin fermuarını çekmek;iki başparmağını da yukarı kaldırmak|pencere;iç çamaşırı;çekmece|Adam ne giyiyor?|Sıcak tutan kıyafetler giyiyor.
823|ekranı işaret etmek;renkli grafikler göstermek;bir klavye kullanmak|ekran;klavye;fare;bitki|El neyi işaret ediyor?|El ekranı işaret ediyor.
825|bir eli yalamak;bir köpek kayışı tutmak;dağların üzerinde asılı durmak|dağlar;köpek;ayakkabı;çimen|Köpek neye bakıyor?|Köpek dağlara bakıyor.
826|sahneyi çekmek;bir boom mikrofonu havaya kaldırmak;kamera karşısında rol yapmak|stüdyo ışığı;kamera;çalışma masası;kablolar|Kameraman ne yapıyor?|Çalışma masasındaki bir oyuncuyu çekiyor.
827|bir dalda oturmak;bir ağaçtan yemek;bir domuzun yakınında oturmak|inek;zürafa;köpek;fil|Hangi hayvan bir dalda oturuyor?|Baykuş bir dalda oturuyor.
828|çok şaşırmış görünmek;ağzını kocaman açmak;masaya yaslanmak|kazak;ceket;pasta;masa|Sarışın kadın nasıl görünüyor?|Çok şaşırmış görünüyor.
830|eliyle tableti göstermek;bir dijital kalemi sıkıca tutmak;başını kaldırıp ona göz atmak|blazer ceket;kitaplar;tablet;dijital kalem|Kır saçlı kadın ne yapıyor?|Tablette bir şey açıklıyor.
831|bir konuşma yapmak;tek eliyle el hareketi yapmak;konuşmacıyı dinlemek|dinleyiciler;mikrofon;kürsü;blazer ceket|Kadın ne yapıyor?|Dinleyicilere bir konuşma yapıyor.
832|bavulunu boşaltmak;yatağın üzerinde oturmak;yerde durmak|kıyafetler;havlu;bavul;atkı|Adam ne yapıyor?|Bavulunu boşaltıyor.
833|bavulu açmak;bir şapka takmak;kıyafetlerin üzerinde yürümek|şapka;kıyafetler;bavul;ayakkabılar|Adam ne yapıyor?|Bir bavuldan kıyafetler çıkarıyor.
834|bir hindi kızartması servis etmek;bir sürahiden su dökmek;başını geriye yatırmak|perdeler;ev sahibesi;hindi;salata|Ev sahibesi ne döküyor?|Bir misafirin ağzına su döküyor.
835|büyük bir somun anahtarını kavramak;iki eliyle el hareketi yapmak;lavabonun altında su sızdırmak|boru;tesisatçı;somun anahtarı;klozet|Tesisatçı ne yapıyor?|Lavabonun altında bir somun anahtarını kavrıyor.
836|kocaman bir sırt çantasını güçlükle taşımak;bir uyku tulumunun üzerine yığılmak;kollarını kavuşturmak|kitaplar;sırt çantası;gözlük;kapüşonlu sweatshirt|Öndeki oğlan ne taşıyor?|Kocaman bir sırt çantasını güçlükle taşıyor.
837|direksiyonu tutmak;başını çevirmek;iki duvarın arasından geçmek|taksi;duvar;yol;ayna|Adam ne yapıyor?|Sarı bir taksi sürüyor.
838|saçına dokunmak;bir selfie çekmek;adama gülümsemek|pilot;uçak;gökyüzü;yer|Güneş gözlüklü adam ne yapıyor?|Saçına dokunuyor.
839|bir yemek masasını uzatmak;yüzüstü yatmak;kollarını iki yana açmak|yemek masası;bank;kazak;tavan|Adam ne yapıyor?|Yemek masasını uzatıyor.
840|botlarının bağcıklarını bağlamak;bir çıkıntıya ilişmek;çakılların üzerinde park edilmiş olmak|gökyüzü;vadi;bere;sırt çantası|Adam nerede doğa yürüyüşü yapıyor?|Dağlarda doğa yürüyüşü yapıyor.
"""
out = {}
for line in D.strip().split('\n'):
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
json.dump(out, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
