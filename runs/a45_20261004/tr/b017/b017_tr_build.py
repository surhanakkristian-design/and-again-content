import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """
4863|bir not yapıştırmak;bir deftere yazmak;yukarı bakıp gülümsemek|takvim;not;kalem;defter|Kadın neye yazıyor?|Bir deftere yazıyor.
4864|bir parmağını kaldırmak;kadının arkasında gülümsemek;büyük bir kutu taşımak|bitki;trompet;üniforma;el|İkinci adam ne taşıyor?|Büyük bir kutu taşıyor.
4865|bir gül çalısının yanına çömelmek;başparmağını kaldırmak;fotoğraf makinesini desteklemek|saat kulesi;objektif;gül;spor ayakkabı|Fotoğrafçı yakından neyi fotoğraflıyor?|Narin, pembe bir gülü fotoğraflıyor.
4866|bir telefon sabitleyicisi tutmak;tarlanın üzerinde havada asılı durmak;birden alkışlamaya başlamak|gökyüzü;dron;tarla|Dron ne yapıyor?|Dron tarlanın üzerinde alçakta havada asılı duruyor.
4867|bir tavayı yukarı kaldırmak;iki başparmağını kaldırmak;gözleri kapalı şarkı söylemek|başparmak;battaniye;tişört|Kız ne yapıyor?|İki başparmağını kaldırıyor.
4868|yumruğunu sıkmak;dizüstü bilgisayarın ekranını işaret etmek;ana ekranda belirmek|pencereler;kapüşonlu sweatshirt;dizüstü bilgisayar;bilgisayar faresi|Kot gömlekli kadın ne yapıyor?|Dizüstü bilgisayarın ekranını işaret ediyor.
4869|tablete çizim yapmak;kameraya gülümsemek;renkli bir poster göstermek|raflar;kadın;lamba;renk kartları|Kadın neye çizim yapıyor?|Tablete çizim yapıyor.
4870|elektrikli sakal düzeltme makinesi kullanmak;müşterinin üzerine eğilmek;iki başparmağını kaldırmak|kulak;kirli sakal;köpük;ustura|Berber ne yapıyor?|Müşterinin üzerine eğiliyor.
4871|bir isim kartını almak;bir isim kartı vermek;başparmağını kaldırmak|kuyruk;damga;formlar;kayıt defteri|Gözlüklü kadın ne yapıyor?|Konuğa bir isim kartı veriyor.
4872|mavi bir kalemle yazmak;biraz yemek yemek;kartlara yıldız damgalamak|kasket;kıskaçlı not altlığı;damga;kartlar|Kadın ne yapıyor?|Kartlara yıldız damgalıyor.
4873|bir kitabın sayfalarını karıştırmak;yapışkan nota bir şeyler karalamak;yapışkan notu havaya kaldırmak|evrak;yapışkan not;açık kitap|Kadın ne yapıyor?|Yapışkan nota bir şeyler karalıyor.
4874|bisikletin üzerinde oturmak;bir koşucunun arkasından yürümek;mavi kot pantolon giymek|binalar;trafik ışığı;köpek;yaya geçidi|Köpek ne yapıyor?|Köpek caddeden karşıya geçiyor.
4875|yüzünü silmek;mavi bir şapka takmak;kutularla dolu olmak|gökyüzü;kamyon;kutular;şort|Şortlu kadın ne yapıyor?|Kamyona kutu taşıyor.
4877|gözlerini kapamak;koltuğunda arkasına yaslanmak;kot ceket giymek|insanlar;kazak;kot pantolon;koltuk|Beyazlı kadın ne yapıyor?|Koltuğunda oturuyor.
4878|tek başına suya atlayış yapmak;yan yana suya dalmak;aynı anda atlamak|gökyüzü;gençler;iskele;su|Gençler ne yapıyor?|İskeleden atlıyorlar.
4879|devasa bir kaya kaldırmak;kabukla kaplı olmak;gümüş alaşım jantları olmak|gökyüzü;araba;halterci;minder|Halterci ne yapıyor?|Bir yarışmada ağır nesneler kaldırıyor.
4880|bir karpuzu aşağı bırakmak;kollarını kaldırmak;mavi bir kapağı olmak|gökyüzü;adam;şişe;duvar|Adam ne yapıyor?|Çatıdan aşağı bir şişe bırakıyor.
4881|gözlerini kapamak;230 numaralı olmak;büyük bir taşı itmek|gökyüzü;otobüs;insanlar;sokak|İnsanlar ne yapıyor?|Büyük bir otobüsü itiyorlar.
4882|bir pikabı sürüklemek;askerî bir uçağı çekmek;devasa jet motorları olmak|uçak;jet motoru;halat;pist|İnsanlar ne yapıyor?|Bir uçağı pist boyunca sürüklüyorlar.
4883|iki büyük kapıyı açmak;kameraya gülümsemek;kollarını kaldırmak|gökyüzü;kapı;tepeler;kadın|Kadın ne yapıyor?|İki büyük kapıyı açıyor.
4884|gökyüzünü ilk işaret eden olmak;ağzını kocaman açmak;eski meydanı doldurmak|gökyüzü;bina;şemsiyeler;kalabalık|İnsanlar ne yapıyor?|Gökyüzünü işaret ediyorlar.
4885|küçük bir bayrağı havaya kaldırmak;gruba önderlik etmek;kadını takip etmek|gökyüzü;bayrak;insanlar;sokak|Kadın ne yapıyor?|Sokak boyunca yürüyor.
4886|dik bir yokuşa tırmanmak;yürüyüş batonlarına yaslanmak;hantal bir sırt çantası taşımak|zirveler;vadi;yürüyüşçü;patika|Yürüyüşçü ne yapıyor?|Dik bir yokuşa tırmanıyor.
4887|kayalardan aşağı inmek;sağlam yürüyüş botları giymek;boğaza doğru inmek|uçurumlar;gökyüzü;patika;iri kaya|Yürüyüşçü ne yapıyor?|Dar bir patikadan aşağı iniyor.
4888|sade beyaz bir yazlık elbise giymek;kalabalığa önderlik etmek;doğrudan objektife bakmak|gökyüzü;yazlık elbise;dalgalar;kum|Beyazlı kadın ne yapıyor?|Kıyı boyunca kalabalığa önderlik ediyor.
4889|taburede dönmek;uzun saçlarını savurmak;bej bir tişört giymek|ışıklar;kalabalık;kanepe;zemin|Beyazlı kadın ne yapıyor?|Taburede dönüyor.
4890|tek ayak üstünde zıplamak;bacağını savurmak;bacağının altında dönmek|gökdelen;sokak lambası direği;topaç;parke taşları|Oğlan neyin etrafında dönüyor?|Bir topacın etrafında dönüyor.
4891|bir yana eğilmek;ağaçların çok üzerinde yükselmek;yeşil yaprakları olmak|gökyüzü;çimen;ağaçlar;öğrenciler|Öğrenciler ne yapıyor?|Bir yana eğiliyorlar.
4892|renkli bir şort giymek;su kaydırağında gülmek;kamerayı tutmak|gökyüzü;palmiye;ayaklar;şort|Adam ne giyiyor?|Renkli bir şort giyiyor.
4893|gözlerini kameraya dikmek;araba desenli bir tişört giymek;yeşil bir forma giymek|üst tribün;seyirciler;korkuluk|Stadyum ne kadar dolu?|Stadyum seyircilerle dolup taşıyor.
4894|önde durmak;siyah çizginin üzerinde durmak;kapıların üzerinde asılı durmak|ışıklar;basketbol potası;öğrenciler;zemin|Öğrenciler ne yapıyor?|Kıpırdamadan duruyorlar.
4895|sırt çantası taşımak;saç tokası takmak;gri saçlı olmak|gökyüzü;cam bina;zemin|İnsanlar nerede duruyor?|Karşı karşıya duruyorlar.
4896|meydan boyunca koşmak;gökyüzünde parlamak;büyük bir kubbesi olmak|gökyüzü;kilise;insanlar;gölge|İnsanlar ne yapıyor?|Meydan boyunca koşuyorlar.
4897|kahverengi bir çanta taşımak;kahverengi bir ceket giymek;yuvarlak bir çatısı olmak|gökyüzü;eski bina;kalabalık;ceket|İnsanlar ne yapıyor?|Büyük bir grup sarılmasına katılıyorlar.
4898|yükseltilmiş bir tarhta çiçek açmak;güneş ışığında parıldamak;ormanın üzerinde yükselmek|cam panel;gökyüzü;çiçekler;çakıl|Bahçıvanlar ne yapıyor?|Bir çerçeveye cam paneller yerleştiriyorlar.
4899|saçları örgülü olmak;gözlerini kapamak;koca bir ağacı kaldırmak|hasır şapka;turp;kökler|Bahçıvanlar ne yapıyor?|Devasa bir ağacı kaldırıyorlar.
4900|çimenlerin üzerinde yuvarlanmak;çimenlere yiyecekleri dökmek;çöküp bir yığına dönüşmek|istif;gökyüzü;kadın;çimen|Yüksek istif ne yapıyor?|İstif çöküp bir yığına dönüşüyor.
4901|kameraya gülümsemek;ayakları önde suya atlamak;birlikte suya dalmak|gökyüzü;insanlar;kayalar;deniz|Arkadaşlar ne yapıyor?|Mavi denize dalıyorlar.
4902|yavaşça su yüzüne çıkmak;havaya sıçramak;şiddetle suya geri düşmek|gökyüzü;ufuk;denizaltı;su|Balina ne yapıyor?|Balina sudan sıçrıyor.
4903|ortada toplanmak;giderek yoğunlaşmak;meydana bakmak|cam çatı;giriş;parke taşları|İnsanlar ne yapıyor?|Meydanın ortasında toplanıyorlar.
4904|slackline üzerinde dengede durmak;gökyüzüne karşı sallanmak;bir insan kulesi oluşturmak|ağaç gövdesi;slackline;spor ayakkabıları;çimenlik|Adamlardan oluşan grup ne yapıyor?|Adamlar bir insan kulesi oluşturuyor.
4905|alüminyum bir merdiveni tutmak;merdiveni uzatılmış olmak;derin bir kanyonun üzerinden geçmek|gökyüzü;çelik köprü;nehir;uçurum|Adam ne tutuyor?|Alüminyum bir merdiven tutuyor.
4906|bir uyarı etiketi taşımak;ağırlıklarla sabitlenmiş olmak;ortasından bükülmek|çadır;pencere;direk;çimenlik|Çadıra ne oluyor?|Çadır çimenliğin üzerine çöküyor.
4907|tahta zemin üzerinde titreşmek;kaslı bir kola darbeler indirmek;çakıla darbe indirmek|genç adam;hoparlör;su dolu bardak;masa|Masaj tabancası ne yapıyor?|Kaslı bir kola darbeler indiriyor.
4908|S şeklinde bükülmek;sırtını geriye bükmek;bir kirişe bastırmak|yapraklar;dal;çit;çimenlik|Kız ne yapıyor?|Sırtını geriye büküyor.
4909|bir sokak lambası direğine tırmanmak;kalabalığın üzerinde durmak;telefonlarını havaya kaldırmak|gökyüzü;güneş;binalar;insanlar|Kadın ne yapıyor?|Bir sokak lambası direğine tırmanıyor.
4910|kameraya bağırmak;yüzü boyalı olmak;taraftarların üzerinde dalgalanmak|saç;göz;ağız;atkı|Adam ne yapıyor?|Kameraya bağırıyor.
4911|anahtarlarını havaya kaldırmak;önlük takmak;kapıda asılı durmak|pencereler;kahve makinesi;kadın;tezgâh|Kadın ne takıyor?|Bir önlük takıyor.
4912|tahta bir levhayı uzatmak;levhayı ikiye kırmak;siyah kuşak takmak|eğitmen;öğrenciler;tahta levha;siyah kuşak|Eğitmen ne yapıyor?|Tahta bir levha uzatıyor.
4913|arkadaşını sırtına almak;arkadaşının sırtına binmek;sarı at kuyruğu olmak|gökyüzü;bilezikler;kısa bluz;yazlık elbise|Kotlu kadın ne yapıyor?|Arkadaşını sırtına alıyor.
4914|gitar çalmak;sokakta koşmak;dans edip gülmek|binalar;ağaçlar;gitar;bank|Genç adam ne yapıyor?|Gitar çalıyor.
4915|gri bir kapüşonlu giymek;renkli bir elbise giymek;bir telefonu bırakmak|gökyüzü;kapüşonlu;elbise;fayanslar|Beş arkadaş ne yapıyor?|Havaya zıplıyorlar.
4916|kendi etrafında dönmek;kadını yakalamak;geriye yaslanmak|güneş;bisiklet;elbise;tişört|Neye biniyorlar?|Bisiklete biniyorlar.
4917|mavili adamı vurmak;bir duvarın üzerinden tırmanmak;dizlerinin üzerine çökmek|gökyüzü;çit;silah;boya|Kırmızılı adam ne yapıyor?|Mavili adamı vuruyor.
4919|bir üyelik formu imzalamak;dilini çıkarmak;kot ceket giymek|süs bayrakları;pankart;kot ceket;kıskaçlı not altlığı|Üç öğrenci ne yapıyor?|Fotoğraf makinelerini başlarının üzerine kaldırıyorlar.
4921|bir su şişesi fırlatmak;havada bir şişe yakalamak;gri bir kapüşonlu giymek|ladin ağaçları;gökyüzü;patika;su şişesi|İki adam ne yapıyor?|Dik bir orman patikasında yukarı yürüyorlar.
4922|paltoları taşımak;gözlük takmak;sıcak bir kazak giymek|ev sahibi;makarna;salata;ekmek|Ev sahibi ne taşıyor?|Paltoları taşıyor.
4923|menüleri taşımak;büyük bir kitap okumak;beyaz bir elbise giymek|garson;pencere;mum;masa|Garson ne taşıyor?|Menüleri taşıyor.
4924|telefonuna bakmak;kot ceket giymek;büyük bir kazak giymek|kadın;adam;sokak;bitki|Kadın neye bakıyor?|Telefonuna bakıyor.
4925|bir malzeme arabasını itmek;bileğini sargıyla sarmak;yatakta yastıklara yaslanmış yatmak|meyve suyu kutusu;cerrahi forma;hasta önlüğü;bandaj|Hemşire ne itiyor?|Koridorda bir malzeme arabasını itiyor.
4926|eldiven giymek;koltukta yatmak;başparmağını kaldırmak|diş hekimi;ayna;pencere;adam|Diş hekimi ne tutuyor?|Bir ayna tutuyor.
4927|basamakları çıkmak;bir kâğıt imzalamak;bir evrak çantası taşımak|avukat;kitaplar;evrak çantası;masa|Avukat ne taşıyor?|Bir evrak çantası taşıyor.
4928|gider borusunu sıkmak;damlayan suyu toplamak;kameraya sırıtmak|kafa lambası;tulum;musluk bataryası;mutfak lavabosu|Adam neyi tamir ediyor?|Sızdıran bir boruyu tamir ediyor.
4929|derse koşmak;bir deftere yazmak;iyi bir not almak|kapüşonlu;not;sıra|Öğrenci nereye koşuyor?|Derse koşuyor.
4931|amfiye uzun adımlarla girmek;şemayı işaret etmek;hayretle bakmak|şema;gözlük;blazer ceket;ahşap paneller|Kadın neyi işaret ediyor?|Tebeşirle çizilmiş şemayı işaret ediyor.
4932|trafiğin içinden aracı sürmek;arka koltukta gülmek;yaya geçidinde fren yapmak|kasket;sokak tabelası;yelek;kapı kolu|Kadın ne yapıyor?|Taksiyi trafiğin içinden sürüyor.
4933|otobüs kullanmak;kırmızı bir düğmeye basmak;şoföre el sallamak|direksiyon;kravat;kapı;yolcular|Şoför ne tutuyor?|Direksiyonu tutuyor.
4934|tekerlekli bir valizi çekmek;mikrofonlu kulaklığını takmak;başparmağını kaldırmak|siperlikli şapka;mikrofonlu kulaklık;emniyet kemeri|Pilot ne takıyor?|Yeşil bir mikrofonlu kulaklık takıyor.
4935|teknenin dümenini kullanmak;dürbünle dikkatle bakmak;gökyüzünde süzülmek|pusula;manivela;kol|Kadın neyle bakıyor?|Bir dürbünle dikkatle bakıyor.
4936|yeşillik doğramak;sosun tadına bakmak;öpücük göndermek|şapka;tencereler;şişeler;tava|Aşçı neyin tadına bakıyor?|Sosun tadına bakıyor.
4937|bir yumurta kırmak;pankeklerin üzerine tereyağı koymak;bir zil çalmak|adam;pencere;pankekler;zil|Adam ne çalıyor?|Bir zil çalıyor.
4938|yemek tabakları taşımak;sipariş yazmak;birlikte kahve içmek|garson;çiçekler;masa|Garson ne taşıyor?|Yemek tabakları taşıyor.
4939|hamura bastırmak;alnını silmek;bir tepside durmak|kruvasanlar;tepsi;önlük|Adam ne tutuyor?|Altın sarısı bir somun ekmek tutuyor.
4940|sosisleri kancalara asmak;paketi iple bağlamak;pirinç bir terazide durmak|kasap;paket;teşhir tezgâhı;kavanozlar|Kasap ne yapıyor?|Bifteği kahverengi kâğıda sarıyor.
4942|bir spor çantası taşımak;siperlikli şapkasını hafifçe kaldırmak;uzun, krem rengi bir palto giymek|bagaj;üniforma;cam kapılar|Asker ne taşıyor?|Omzunda bir spor çantası taşıyor.
4943|şok olmuş bir surat yapmak;eğilerek selam vermek;yumruğunu havaya savurmak|spot ışığı;ekip üyeleri;kazak|Ekip ne yapıyor?|Genç adama tezahürat yapıyorlar.
4944|makyajını tazelemek;gece elbisesiyle dönmek;güllerin üzerine eğilerek selam vermek|perde;buket;gece elbisesi|Kadın ne tutuyor?|Bir buket kırmızı gül tutuyor.
4945|mikrofona şarkı söylemek;kulaklık takmak;el çırpmak|ışıklar;mikrofon;kulaklık;tişört|Kadın ne yapıyor?|Mikrofona şarkı söylüyor.
4946|tahta tutamağa yaslanmak;yere çömelmek;at kuyruğunu sallamak|ayna;at kuyruğu;kapüşonlu;eşofman altı|Kadın ne giyiyor?|Kısa bir kapüşonlu giyiyor.
4947|bir boya tüpünü sıkmak;tuvale hafif dokunuşlarla boya sürmek;parlak yeşil gözleri olmak|portre;tulum;fırçalar;palet|Kadın ne resmediyor?|Rengârenk bir portre resmediyor.
4948|fırçayla pudra sürmek;şaşkınlıkla kaşlarını kaldırmak;ufuk boyunca uzanmak|şehir silueti;makyaj fırçası;pudriyer;sabahlık|Kadın ne yapıyor?|Yüzüne pudra sürüyor.
4949|mavi bir sırt çantası taşımak;yokuş yukarı adamı takip etmek;vadinin üzerinde yükselmek|gökyüzü;karlı zirveler;buzul;kayalar|Yürüyüşçüler ne yapıyor?|Kayalık bir yamaca tırmanıyorlar.
4950|kameraya sırıtmak;yüzünü ciddi tutmak;fırfırlı kırmızı bir etek giymek|tavan lambası;kısa bluz;kalça;fırfırlı etek|Genç adam ne yapıyor?|Ellerini kalçalarına dayıyor.
4952|yatakta yatmak;adamın üzerine zıplamak;önlük takmak|lamba;yastık;adam;yatak|Genç adam ne yapıyor?|Yatakta yatıyor.
4953|bir saksıyı sulamak;ellerini gergin bir şekilde kenetlemek;topraktan baş göstermek|örgü;filiz;saksı;pencere pervazı|Saksıda ne büyüyor?|Saksıda minicik bir filiz büyüyor.
4954|biraz çiçek taşımak;el çırpmak;havada süzülmek|pencere;balon;çiçekler;yatak|Yataktaki kadın ne yapıyor?|El çırpıyor.
4956|büyük bir sırt çantası taşımak;bir dünya haritasına dokunmak;şehrin üzerinde batmak|ekran;sırt çantası;resepsiyon masası|Gezgin ne taşıyor?|Büyük bir sırt çantası taşıyor.
4957|büyük bir sırt çantası taşımak;bir valiz çekmek;bastonla yürümek|otel;çeşme;baston;halı|Yaşlı adam ne yapıyor?|Bastonla yürüyor.
4958|harap bir kulübeyi işaret etmek;kollarını iki yana açmak;lüks bir villayı tanıtmak|villa;çeşme;havuz;çakıl taşları|Krem rengi kıyafetli kadın ne yapıyor?|Lüks bir villayı tanıtıyor.
4959|kapı aralığından dışarı sarkmak;başparmağını kaldırmak;yansıtma havuzunun yanında poz vermek|kır evi;kırmızı kapı;çalı çit;bahçe kapısı|Yaşlı adam ne yapıyor?|Kapı aralığından dışarı sarkıyor.
4960|hardal rengi bir ceket giymek;yüzünü gömmek;şaşkınlıkla nefesi kesilmek|sütun;varış tabelası;hardal rengi ceket;el çantası|Kızıl saçlı kadın ne yapıyor?|Koyu saçlı bir kadına sarılıyor.
4961|oyuncak bir fareyi yakalamak;ağzını kapatmak;ellerini kaldırmak|bitki;masa;evcil hayvan;oyuncak fare|Kedi ne yapıyor?|Oyuncak bir fareyle oynuyor.
4962|çamurlu bir ayak izini işaret etmek;dürbünle dikkatle bakmak;sisin içinde dolaşmak|bere;dürbün;ayak izi;sis|Adam neyi işaret ediyor?|Çamurlu bir ayak izini işaret ediyor.
4963|ağrıyan parmağını sıkmak;çıplak ayağını tutmak;yaralı kolunu kavramak|pencere;karton kutu;parmak;İngiliz anahtarı|Kadın neyi sıkıyor?|Ağrıyan parmağını sıkıyor.
4964|ona bir kaşık yedirmek;bir buket sunmak;sevinçle nefesi kesilmek|pencere;kurulama bezi;kepçe;tencere|Adam kadına ne veriyor?|Ona bir buket veriyor.
4965|dişlerini fırçalamak;ellerini yıkamak;yüzünü kurulamak|pencere;diş fırçası;musluk;lavabo|Oğlan neyi fırçalıyor?|Dişlerini fırçalıyor.
4968|bir kartı almak;fotoğraf çekmek;el çırpmak|kâğıtlar;telefon;kart;bilgisayar|Kızıl saçlı kız ne tutuyor?|Üzerinde kendi fotoğrafı olan bir kart tutuyor.
4969|kitap okumak;kahve içmek;ona telefonunu göstermek|ağaç;kitap;gazete;çanta|Yaşlı kadın ne yapıyor?|Bir kafede kitap okuyor.
4971|bayrağı göndere çekmek;kubbenin üzerinde patlamak;maytap ve bayrak sallamak|havai fişekler;bayrak direği;kubbe;kalabalık|Subay ne yapıyor?|Bayrağı göndere çekiyor.
4972|ulusal bayrağı göndere çekmek;yüzü boyalı olmak;kubbenin arkasında patlamak|havai fişekler;bayrak direği;kubbe;kalabalık|Kadının yanaklarında ne var?|Yanaklarında vatansever bir yüz boyası var.
"""
src = json.load(open(f'{H}/source.json'))
rows = {}
for line in D.strip().splitlines():
    i, p, n, q, a = line.split('|')
    rows[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
