import json, os
H = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(f'{H}/source.json'))
R = r'''
4973|baharatların üzerine eğilmek;tezgâhına göz kulak olmak;bahçelerin üzerinde yükselmek|anıt;gökyüzü;selvi ağaçları;havuz|Genç gezgin ne yapıyor?|Bir anıtın önünde poz veriyor.
4974|yüksekten çay dökmek;bardak bardak çay dağıtmak;ona tezahürat yapmak|satıcı;kalabalık;çelenk;çelik bardaklar|Satıcı ne yapıyor?|Yüksekten çay döküyor.
4975|portakal suyu içmek;kameraya gülümsemek;portakal suyu doldurmak|şapka;bardak;palto;makine|Mavili kadın ne içiyor?|Portakal suyu içiyor.
4977|tarlaların arasından yürümek;büyük bir salıncakta sallanmak;uzun bir kuyruğu olmak|gökyüzü;palmiye ağaçları;el;patika|Adam neyin yanında oturuyor?|Bir maymunun yanında oturuyor.
4978|bir yumurta kırmak;havaya uçmak;tavanın altında yanmak|aşçı;yumurta;pilav;tabak|Aşçı ne yapıyor?|Tavada pilav pişiriyor.
4979|ona bir kalem vermek;bir kalem almak;ona birkaç kâğıt uzatmak|adam;pencere;klavye;telefon|Ofis çalışanları ne yapıyor?|Burunlarını siliyorlar.
4980|kahvesini koklamak;çiçekleri koklamak;kollarını iki yana açmak|gökyüzü;tepeler;insanlar|Arkadaşlar ne yapıyor?|Derin bir nefes alıyorlar.
4981|omzunun üzerinden sırıtmak;deriyi delmek;yumruğunu havaya kaldırmak|atlet;pencere;hemşire;çöp kutusu|Genç adam ne yapıyor?|Üst koluna aşı oluyor.
4982|topa vurmak;ayak bileğini tutmak;bir bankta oturmak|kale;saç bandı;çimen;ayak bileği|Beyazlı adam neyi tutuyor?|Ayak bileğini tutuyor.
4983|bir pasaporta bakmak;bir bavulu kontrol etmek;bir minibüsün altında yatmak|minibüs;memur;el feneri;ayakkabı|Memur neyin altında yatıyor?|Bir minibüsün altında yatıyor.
4984|dizlik takmak;bir kaykayı sıkıca tutmak;takım elbiseyle kaykay yapmak|gökyüzü;palmiye ağaçları;evrak çantası;sahil yolu|İş adamı ne taşıyor?|Siyah bir evrak çantası taşıyor.
4985|şarjlı matkap kullanmak;bir seyyar merdivenin üzerinde durmak;tavana uzanmak|tavan;ekranlar;yaka kartı ipi;bluz|İki çalışan ne yapıyor?|Ekranı duvara sabitliyorlar.
4986|bir matkap tutmak;tavana dokunmak;kameraya gülümsemek|tavan;ekranlar;adam;kadın|Ekranlar ne renk?|Ekranlar parlak mavi.
4987|fikirlerini sunmak;bir tepsi kahve taşımak;masaya yığılmak|yapışkan notlar;karton bardaklar;örgüler;dizüstü bilgisayar|Adam ne taşıyor?|Bir tepsi dolusu paket kahve taşıyor.
4988|büyük bir bayrak taşımak;saldırıya önderlik etmek;savaşçıları izlemek|gökyüzü;bayraklar;çimen;çadırlar|Zırhlı adam ne taşıyor?|Büyük bir bayrak taşıyor.
4989|diğerlerinin önünde koşmak;telefonla çekim yapmak;tepenin altında durmak|bayraklar;tepe;çadır;ip|Adamlar nereye koşuyor?|Tepeden aşağı koşuyorlar.
4990|bir gömlek ütülemek;bir gömlek katlamak;kıyafetleri bir yığına koymak|çamaşır makinesi;kıyafetler;ütü;ütü masası|Adam ne yapıyor?|Bir gömlek ütülüyor.
4991|yüzünü buruşturmak;kırışık bir gömleğin üzerinde kaymak;kırışıksız bir gömleği kaldırıp göstermek|perde;saksı bitkisi;kıyafet yığını;yorgan|Adam ne ütülüyor?|Kırışık mavi bir gömlek ütülüyor.
4992|bir sürü kıyafet taşımak;bir dolabı açmak;mavi bir gömleği kaldırıp göstermek|pencere;kadın;ütü;gömlek|Kadın ne taşıyor?|Bir sürü kıyafet taşıyor.
4993|kırmızı bir tekneyle kürek çekmek;bir kayaya basmak;bir ağacın yanında durmak|gökyüzü;ağaç;tekne;göl|Kadın nerede duruyor?|Bir ağacın yanında duruyor.
4994|taze makarna yapmak;tahta kaşık kullanmak;büyük bir tabak taşımak|kadın;sarımsak;makarna;masa|Kadın ne taşıyor?|Büyük bir tabak makarna taşıyor.
4997|bir yana yatmak;bir gondoldan dışarı sarkmak;dev bir külahı sıkıca tutmak|çamaşırlar;köprü;kanal;gondol|Adam ne tutuyor?|Dev bir dondurma külahı tutuyor.
4998|uzun bir tünel oluşturmak;ramen eriştesini höpürdeterek yemek;tezgâhın üzerinde asılı durmak|fenerler;ceket;yemek çubukları;kâse|Adam ne yiyor?|Yemek çubuklarıyla ramen yiyor.
5000|ince dilimler kesmek;balığı pirincin üzerine koymak;şefi alkışlamak|adam;suşi;tabak|Adam ne kesiyor?|İnce balık dilimleri kesiyor.
5001|pencere kenarında oturmak;bir tepeye tırmanmak;sırt çantası taşımak|gökyüzü;dağlar;köy;sırt çantası|Kadın ne yapıyor?|Manzaraya bakıyor.
5002|suya ilk atlamak;kırmızı mayo giymek;mavi bikini giymek|gökyüzü;çam ağaçları;yüzücüler;iskele|İnsanlar ne yapıyor?|Alacakaranlıkta iskeleden atlıyorlar.
5005|dürbünle bakmak;tekneyi göstermek;suyun üzerinde ilerlemek|gökyüzü;tepe;koy;tekne|Kadın neyi gösteriyor?|Turuncu tekneyi gösteriyor.
5006|su ısıtıcısını doldurmak;kupalara su dökmek;su kaynatmak|pencere;su ısıtıcısı;kupalar;masa|Kadın ne yapıyor?|Kupalara su döküyor.
5008|pirinç bir posta kutusunun kilidini açmak;eski anahtarları tek tek gözden geçirmek;ardına kadar açılmak|gökyüzü;sarmaşık;yaka kartı ipi;saksılar|Kadın ne yapıyor?|Pirinç bir posta kutusunun kilidini açıyor.
5009|kaydıraktan kaymak;bir topa tekme atmak;havaya uçmak|gökyüzü;çocuk;top;çimen|Oğlan neye tekme atıyor?|Bir topa tekme atıyor.
5010|kırmızı halının üzerinde yürümek;bir tahtta oturmak;altın bir taç tutmak|bayrak;taç;kral;halı|Kral nerede oturuyor?|Bir tahtta oturuyor.
5011|kırmızı bir şapka takmak;yaşlı bir kadını öpmek;genç bir kadını öpmek|bina;araba;el;ceket|Yaşlı adam ne yapıyor?|Yaşlı bir kadını öpüyor.
5013|bir tencereyi karıştırmak;kurabiye pişirmek;siyah bir kazak giymek|kadın;kurabiyeler;su ısıtıcısı|Kadın ne yapıyor?|Fırından kurabiyeleri çıkarıyor.
5014|çorbanın tadına bakmak;sıcak bir yemek kabı tutmak;kollarını iki yana açmak|tavalar;şehir;adam;ocak|Kadın ne tutuyor?|Sıcak bir yemek kabı tutuyor.
5015|saçını uzun bir örgü yapmak;pas rengi bir önlük takmak;desenli bir başörtüsü takmak|hamur;başörtüsü;önlük;çömlekler|İki kadın ne yapıyor?|Birlikte hamur yoğuruyorlar.
5016|dizlerini bükmek;yuvarlak gözlük takmak;küçük bir çekiç tutmak|gözlük;dolap;doktor;diz|Doktor ne tutuyor?|Küçük bir çekiç tutuyor.
5017|kırmızı bir soğan doğramak;kameraya gülümsemek;önlük takmak|adam;havlu;sebzeler;bıçak|Adam ne yapıyor?|Bıçakla sebze doğruyor.
5019|ızgarada sığır eti pişirmek;bir marul yaprağı tutmak;gözlük takmak|adam;marul;sığır eti;ızgara|Garson ne yapıyor?|Izgarada sığır eti pişiriyor.
5020|merdivene tırmanmak;ampul değiştirmek;başparmağını kaldırmak|ampul;kadın;merdiven;adam|Kadın ne yapıyor?|Ampul değiştiriyor.
5021|biraz çay koymak;kameraya gülümsemek;ellerini silmek|şapka;hanımefendi;demlik;kekler|Hanımefendi ne yapıyor?|Fincana çay koyuyor.
5022|çalışma masasında oturmak;uzun bir lamba tutmak;uzun bir elbise giymek|lamba;kadın;kanepe;kitaplar|Adam ne yapıyor?|Çalışma masasında oturuyor.
5023|iki kolunu kaldırmak;bir direğin üzerinde durmak;adamın üzerinden uçmak|uçak;kuş;çimen;gökyüzü|Adamın üzerinden ne uçuyor?|Üzerinden büyük bir uçak uçuyor.
5024|kameraya el sallamak;ellerini birleştirmek;bir sürü kitap taşımak|sözlükler;bayrak;fincan|Kıvırcık saçlı kadın ne taşıyor?|Bir sürü sözlük taşıyor.
5025|telefonuna bakmak;beyaz tahtanın önünde durmak;yerde yatmak|öğretmen;beyaz tahta;dizüstü bilgisayar;yer|Öğretmen ne yapıyor?|Beyaz tahtanın önünde duruyor.
5026|gözyaşlarını silmek;başını geriye atmak;gözlerini kocaman açarak bakmak|beyaz tahta;dizüstü bilgisayar;kapüşonlu sweatshirt;akıllı telefon|Mavi saçlı öğrenci ne yapıyor?|Gülmekten ağlıyor.
5028|ağır kitaplar taşımak;tahta bir tokmak tutmak;yığının üzerinde açık durmak|kitaplar;gözlük;yargıç;tokmak|Genç adam ne taşıyor?|Ağır kitaplar taşıyor.
5030|uzun bir pankart taşımak;davullarıyla yürümek;davulcuların yanından koşarak geçmek|kostüm;direk;bayrak süsleri;balkonlar|Tüylü kostümlü kadın ne yapıyor?|Caddede bir pankart taşıyor.
5032|harita okumak;tepesinde kar olmak;yumruğunu kaldırmak|dağlar;kep;ceket;harita|Kırmızılı kadın ne yapıyor?|Harita okuyor.
5033|sokakta dans etmek;kollarını iki yana açmak;yolun üzerinde asılı durmak|bayraklar;kadın;davul;sokak|Kadın ne yapıyor?|Sokakta dans ediyor.
5034|lavabonun altına çömelmek;masaya akmak;bir kovaya damlamak|süt kutusu;bornoz;su birikintisi;masa|Kovaya ne damlıyor?|Borudan su damlıyor.
5035|üç topla jonglörlük yapmak;yerden bir top almak;çimenlerde oturmak|ağaçlar;tişört;pantolon;çimen|Sarışın kız ne yapıyor?|Üç topla jonglörlük yapıyor.
5036|jonglörlük yapmayı öğrenmek;el çırpmak;mavi bir ceket giymek|gökyüzü;binalar;adam;kadın|Adam ne yapıyor?|Jonglörlük yapmayı öğreniyor.
5037|bir bavulu çekmek;bir kapıyı açmak;bir misafire gülümsemek|bina;kadın;bavul;kaldırım|Paltolu kadın nerede?|Kaldırımda duruyor.
5038|arka bacak kasını esnetmek;merdivenlerden yukarı koşmak;sabit bir tempoyu korumak|gözetleme kulesi;kep;koşu ayakkabısı;korkuluk|Koşucu ne yapıyor?|Sabit bir tempoda koşuyor.
5039|bir kafes kapısının mandalını açmak;gür beyaz bir sakalı olmak;şehrin üzerinde daire çizmek|sürü;güneş;kalabalık;kafes|Yaşlı adam ne tutuyor?|Boş bir kafes tutuyor.
5040|pirinç bir lamba tutmak;tahta bir sandığı güçlükle kaldırmak;mobilyayla yüklü olmak|koltuk;sandık;yük bisikleti;ceket|İki kadın neyi kaldırıyor?|Kadife bir koltuğu kaldırıyorlar.
5042|kapıyı açık tutmak;lacivert bir crop top giymek;bir banka çökmek|ağaçlar;apartman;bank;kaldırım|Kıvırcık saçlı kadın ne yapıyor?|Kendini yavaşça bir banka bırakıyor.
5044|müzik dinlemek;bir kahve fincanı tutmak;kapıda kulak kabartmak|lamba;bardak;fincan;masa|Kulaklıklı adam ne yapıyor?|Müzik dinliyor.
5045|kulağına dokunmak;kulaklık takmak;iki büyük hoparlörü olmak|afiş;dükkân;radyo|Genç adam ne takıyor?|Büyük kulaklıklar takıyor.
5047|kumandayı tutmak;patlamış mısırı taşımak;bir battaniye getirmek|saat;lamba;patlamış mısır;battaniye|Ne yiyorlar?|Patlamış mısır yiyorlar.
5048|anahtarla uğraşmak;olgun bir karpuz tutmak;kulplardan sarkmak|başörtüsü;menteşe;asma kilit;anahtar destesi|Yaşlı kadın ne yapıyor?|Kocaman bir asma kilitle uğraşıyor.
5049|bisikletini kilitlemek;anahtarı çevirmek;kapının yanında parlamak|adam;ağaçlar;kilit;bahçe kapısı|Adam ne yapıyor?|Bisikletini kilitliyor.
5050|dehşetle nefesi kesilmek;yüzünü ellerine gömmek;bir pankartı indirmek|sütun grafik;balonlar;kravat;konfeti|Kır saçlı adam ne yapıyor?|Yüzünü ellerine gömüyor.
5051|sırt çantasını boşaltmak;ranzanın altını aramak;kıyafetlerini karıştırmak|ranza;pencere;sırt çantası;kıyafet yığını|Genç kadın ne yapıyor?|Kıyafetlerini karıştırıyor.
5054|ağır bir çantayı omuzlamak;yüklü bir bagaj arabasını itmek;bavulları bir minibüse yüklemek|gökyüzü;bavullar;soğutucu çanta;bagaj arabası|Adam ne kaldırıyor?|Bavulları bagaja kaldırıyor.
5056|bir çarşafı silkelemek;yastıkları kabartmak;havluları kuğu şeklinde katlamak|kat görevlisi;temizlik arabası;balkon;çiçek|Kat görevlisi ne katlıyor?|Havluları kuğu şeklinde katlıyor.
5058|üzgün bir surat yapmak;mektupları dağıtmak;mektupları çıkarmak|postacı;araba;posta kutusu;çimen|Postacı ne yapıyor?|Mektupları posta kutusuna koyuyor.
5059|posta kutusunu açmak;mektupları getirmek;posta kutusuna koşmak|mektup;koli;posta kutusu;kapüşonlu sweatshirt|Adam ne tutuyor?|Bir sürü mektup tutuyor.
5060|bir halka kule oyuncağına uzanmak;scooter sürmek;barfiks çekmek|müze;oyun parkı;yaşlı adam;bank|Mavili adam ne yapıyor?|Omuzlarında küçük bir çocuk taşıyor.
5061|yürüyen merdivenle yukarı çıkmak;kollarını iki yana açmak;suyun içinde süzülmek|akvaryum;tünel;korkuluk;buz pateni pisti|Genç adam neye bakıyor?|Başını kaldırıp köpekbalıklarına bakıyor.
5063|bandoya önderlik etmek;müzik çalmak;kır saçlı olmak|bayrak;ağaçlar;yürüyüş kolu;adam|Bando ne yapıyor?|Bando caddede yürüyüş yapıyor.
5064|trompetlerini üflemek;ulusal bayraklar sallamak;davullarını çalmak|bayraklar;davul;bulvar;trompet|Bandocular ne yapıyor?|Uzun bir bulvarda yürüyüş yapıyorlar.
5065|yeşil bir zeytin tatmak;koridorda dolaşmak;metal zincirlerden sarkmak|tavan;koridor;baharatlar;file çanta|Genç adam nerede yürüyor?|Uzun bir koridorda dolaşıyor.
5066|zeytin yemek;mavi bir önlük takmak;büyük bir kaşık tutmak|gökyüzü;cami;portakallar;poşet|Genç adam ne yiyor?|Yeşil bir zeytin yiyor.
5068|uzun bir duvak takmak;gelini öpmek;duvağını kaldırmak|güller;deniz;gelin;kum|Gelin ve damat ne yapıyor?|Plajda öpüşüyorlar.
5070|kenarına ilişmek;acıyla yüzünü buruşturmak;yatağın üzerine enlemesine yayılmak|pencereler;yatak başlığı;kadın;yatak|Kadın nerede yatıyor?|Kocaman bir yatağın üzerinde enlemesine yatıyor.
5071|kameraya sırıtmak;bijon somunlarını sıkmak;kaputu kapatmak|tamirci;kaput;raflar|Tamirci ne yapıyor?|Arabanın bakımını yapıyor.
5073|ilacını içmek;dilini çıkarmak;biraz su içmek|ilaç;kaşık;bardak;kapak|Kadın ne yapıyor?|İlacını içiyor.
5074|büyük bir kutu taşımak;birçok kişiyle tokalaşmak;arkasında durmak|ceket;kutu;sandalye;bilgisayar|Turunculu kadın ne taşıyor?|Büyük bir kutu taşıyor.
5075|damlayan bir külahı yalamak;ellerini yapış yapış yapmak;buz küpleriyle dolu olmak|dondurma;güneş gözlüğü;şemsiye;parke taşları|Adamın elleri nasıl?|Elleri yapış yapış.
5076|spor salonuna girmek;yeşil bir onay işareti göstermek;bir satranç taşını oynatmak|kitaplar;kadın;satranç tahtası;masa|Yaşlı kadın ne yapıyor?|Bir satranç taşını oynatıyor.
5077|cevapları hatırlamak;not almak;yumruğunu havaya savurmak|sütun;gözlük;kulaklık;bilgi kartları|Öğrenci ne yapıyor?|Cevapları hatırlamaya çalışıyor.
5078|kızarmış domuz etini dilimlemek;bir misket limonu sıkmak;gür bir sakalı olmak|domuz eti;önlük;misket limonu;tako|Aşçı ne yapıyor?|Kızarmış domuz etinden dilimler kesiyor.
5079|bir takoyu ısırmak;taş basamakları tırmanmak;sokağın üzerinde asılı durmak|gökyüzü;piramit;hasır çanta;basamaklar|Kadın ne yapıyor?|Sulu bir takoyu ısırıyor.
5080|aynaya bakmak;fotoğraf çekmek;hızla arkasını dönmek|telefon;bitki;sarı elbise;sepet|Kadın ne giyiyor?|Sarı bir elbise giyiyor.
5081|mavi bir kapüşonlu sweatshirt giymek;aynayı göstermek;mor bir elbise giymek|ayna;saç;mor elbise;halı|Morlu kadın ne yapıyor?|Aynaya bakıyor.
5082|saçına dokunmak;aynaya bakmak;sarı bir kolye takmak|ayna;saç modeli;kolye;turuncu bluz|Kadın ne yapıyor?|Aynaya bakıyor.
5083|bir kasede yumurta çırpmak;çırpılmış yumurtaları içine dökmek;parmağındaki hamuru yalamak|tahta kaşık;orman meyveleri;karıştırma kabı;un|İki kadın ne yapıyor?|Birlikte hamuru karıştırıyorlar.
5084|kameraya doğru yürümek;uzun yeşil bir elbise giymek;omzunun üzerinden bakmak|küpeler;elbise;telefonlar;zemin|Kadın ne giyiyor?|Uzun yeşil bir elbise giyiyor.
5085|tabelayı göstermek;sakalı olmak;telefonunu havaya kaldırmak|heykel;ağaçlar;tabela;telefon|Kadın neyi gösteriyor?|Tabelayı gösteriyor.
5086|cilalı zemini paspaslamak;iş toplantısı yapmak;tavan ışıklarını yansıtmak|tavan ışıkları;pencereler;lastik eldivenler;paspas|Temizlikçi ne yapıyor?|Parlak ofis zeminini paspaslıyor.
5087|mutfaktan geçmek;kirli zemini temizlemek;paspası yıkamak|dolap;kova;paspas;ayak izleri|Adam ne yapıyor?|Kirli zemini temizliyor.
5089|krep pişirmek;havaya yükselmek;dizi ağrımak|anne;buzdolabı;krep|Anne ne yapıyor?|Krep yapıyor.
5091|kameraya gülümsemek;yuvarlak bir farı olmak;kırmızı bir kask takmak|adam;motosiklet;deniz;gökyüzü|Adam neye biniyor?|Motosiklete biniyor.
5092|büyük bir kutu taşımak;kameraya gülümsemek;bitkileri sulamak|kamyon;yardımcı;kanepe;merdiven|Kadın ne taşıyor?|Büyük bir kutu taşıyor.
5093|çim biçme makinesini itmek;biçilen çimleri dışarı atmak;biçilmiş çimi sulamak|çim biçme makinesi;çit;fıskiye;uzun çimen|Adam ne yapıyor?|Uzamış çimleri biçiyor.
5094|zorlanarak yüzünü buruşturmak;kameraya ışıl ışıl gülümsemek;iki pazısını birden kasmak|kol saati;siyah atlet;ağırlık sehpası|Vücut geliştirmeci ne yapıyor?|İki pazısını birden kasıyor.
5095|eski madeni paraların eskizini çizmek;hayranlıkla yukarı bakmak;cam çatıdan sarkmak|cam çatı;iskelet;kadife gömlek;defter|Adam neye dikkatle bakıyor?|Dev bir iskelete dikkatle bakıyor.
5097|gitar çalmak;elini kaldırmak;bir bebek tutmak|gökyüzü;gitar;bebek;gitar kılıfı|Gitarist ne yapıyor?|Sokakta müzik çalıyor.
5098|kendini videoya çekmek;uzun bir atkı takmak;gökyüzünü kaplamak|bayrak;ışıklar;insanlar|Kızıl saçlı adam neye bakıyor?|Ulusal bayrağa bakıyor.
'''
out = {}
rows = {l.split('|')[0]: l.split('|') for l in R.strip().split('\n')}
for k in src:
    _, p, n, q, a = rows[k]
    out[k] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
json.dump(out, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
