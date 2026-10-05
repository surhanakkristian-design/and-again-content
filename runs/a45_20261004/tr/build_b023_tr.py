import json, os
H = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(f'{H}/b023/source.json'))
R = """5607|kuru otlarda otlamak;alev alev yanmak;rüzgârda dalgalanmak|kale;at;sancak;kalkanlar|At ne yapıyor?|At savaş alanında otluyor.
5608|dizlerini bükmek;kollarını iki yana açmak;atlayıcıya işaret vermek|mayo;tramplen;antrenör;kulvar halatı|Atlayıcı ne yapmak üzere?|Havuza atlamak üzere.
5610|kanepeye atlamak;yanına uzanmak;köpeği okşamak|şömine;tablo;köpek;kanepe|Kadın ne yapıyor?|Köpeği okşuyor.
5613|kameraya sırıtmak;omzunun üzerinden işaret etmek;ağırlığın altında zorlanmak|kaya;kemerler;örgü;çit|Siyahlı kadın ne taşıyor?|Omzunda bir kaya taşıyor.
5614|sarı bir çanta taşımak;yeşil meyve suyu içmek;arkada yürümek|bitki;çiçekler;pencereler;çanta|Sarılı kadın ne giyiyor?|Sarı bir takım elbise giyiyor.
5615|erişteyi havaya atmak;tavada erişte pişirmek;bardaklara çorba dökmek|fenerler;insanlar;tava;bardaklar|Aşçı ne yapıyor?|Tavada erişte pişiriyor.
5617|tahta kesmek;tahta bir çekiç tutmak;aletine gülümsemek|testere;çekiç;tahta;önlük|Sakallı adam ne yapıyor?|Tahta kesiyor.
5618|arkadaşını havada döndürmek;arkadaşlarını alkışlamak;buzlu kahve dökmek|zeytin ağacı;çatılar;minder;sürahi|Mavili kadın ne yapıyor?|Arkadaşını yerden kaldırıyor.
5619|kolunu havaya kaldırmak;bir yemek daha getirmek;tavadaki yemeği havada çevirmek|bakır tencereler;sarkıt lamba;kızarmış tavuk;damalı zemin|Baş aşçı ne yapıyor?|Kolunu havaya kaldırıyor.
5620|onu havaya kaldırmak;yüzüne dokunmak;kırmızı bir palto giymek|vitrin;kırmızı palto;adam|Kadın ne giyiyor?|Kırmızı bir palto giyiyor.
5621|çoraplarıyla parmak uçlarında yürümek;kollarını kavuşturup oturmak;koltuğun yanında oturmak|çerçeveli baskılar;ayaklı lamba;ayakkabılar;halı|Kadın ne yapıyor?|Kollarını kavuşturmuş oturuyor.
5622|teleskoptan bakmak;kollarını kavuşturmak;kolundan çekmek|gökyüzü;teleskop;lamba;kum|Kadın neyden bakıyor?|Teleskoptan bakıyor.
5623|bir deste plağı sıkıca tutmak;tahta kasaların yanında diz çökmek;karton bir kutuyu karıştırmak|kulaklık;duvar lambası;karton kutu;tahta kasalar|Kadın ne tutuyor?|Bir deste plağı sıkıca tutuyor.
5624|kanatlarını açmak;bir çay bardağı tutmak;ayakta duran adamı işaret etmek|tavan vantilatörü;fener;papağan;nane çayı|Papağan nerede tünüyor?|Adamın omzunda tünüyor.
5625|hindistan cevizinden içmek;hamakta uzanmak;kumda uyumak|hamak;köpek;bavul;plaj barı|Adam ne yapıyor?|Hamakta uzanıyor.
5627|rafta kıvrılıp yatmak;ağzını kocaman açarak esnemek;kediye doğru uzanmak|pirinç lamba;kedi;mozaik karolar|Kedi nerede yatıyor?|Kavanozların arasındaki boşlukta yatıyor.
5628|yeri süpürmek;patenlerini çıkarmak;tavandan sarkmak|disko topu;kadın;süpürge;balonlar|Adam ne yapıyor?|Yeri süpürüyor.
5630|katlı bir pastayı dengede tutmak;ayaklarının dibine çömelmek;ışık zincirlerinin altında dans etmek|asmalar;katlı pasta;panjurlar;hasır koltuk|Krem rengi giyen kadın ne taşıyor?|Katlı bir pasta taşıyor.
5631|birbirlerini işaret etmek;birbirlerine sarılmak;terasın üzerinde asılı durmak|ışıklar;kapı;lamba;kanepe|İki kadın ne yapıyor?|Birbirlerini işaret ediyorlar.
5632|hamakta keyif yapmak;göğsünde kıvrılmak;yukarıdan ona kaşlarını çatarak bakmak|çit;boya kutusu;saksı;hamak|Adam nerede keyif yapıyor?|İpten bir hamakta keyif yapıyor.
5633|üzerine bir ceket örtmek;bankta büzülerek oturmak;çatının altında parlamak|fener;bank;köpek;şemsiye|Kadın ne yapıyor?|Üzerine bir ceket örtüyor.
5634|aynada selfie çekmek;bir çekmeceyi karıştırmak;yorganın üzerinde durmak|avize;köpek;havlu;kıyafetler|Adam ne yapıyor?|Bir çekmeceyi karıştırıyor.
5635|bir şeker parçası yerleştirmek;kollarını kavuşturmak;boyalı tavandan sarkmak|avize;pasta;masa örtüsü;parke zemin|Şef ne yapıyor?|Pastaya bir şeker parçası yerleştiriyor.
5637|geçen trene gözünü dikip bakmak;mısır gevreğini iştahla yemek;pencere pervazında uyuklamak|tren;kedi;sandalye;döşeme tahtaları|Kadın neye gözünü dikmiş bakıyor?|Geçen trene gözünü dikmiş bakıyor.
5638|bir örümceği yakalamak;pembe bir askılı saten elbise giymek;bir kâğıt tutmak|örümcek;saksı bitkisi;raf;minder|Kırmızılı kadın ne yapıyor?|Bir bardakla örümceği yakalıyor.
5640|havaya yumruk sallamak;kollarını iki yana açmak;kayalık bir çıkıntıda durmak|dağ keçisi;su şişesi;yürüyüş botları;sırt çantaları|Adam ne yapıyor?|Kollarını iki yana açıyor.
5641|kuru kalmak;sırılsıklam olmak;ters dönmüş bir şemsiye tutmak|balkon;sokak lambası;taksi;deri ceket|Adam ne tutuyor?|Ters dönmüş bir şemsiye tutuyor.
5643|kadına yalvarmak;bir el arabası itmek;büyük bir çanta taşımak|önlük;kutular;çanta;çatı|Öndeki adam ne yapıyor?|Kadına yalvarıyor.
5644|göz alıcı mavi bir şerit boyamak;merdiveni sabit tutmak;başını kaldırıp ona bakmak|gökyüzü;boya rulosu;şerit;merdiven|Adam ne yapıyor?|Göz alıcı mavi bir şerit boyuyor.
5645|kollarını sallamak;sevinçle bağırmak;zeminde kayarak ilerlemek|kitaplar;tabela;sırt çantası;araba|Kıvırcık saçlı kadın ne yapıyor?|Kitap arabasının üstünde gidiyor.
5646|ona arkadan sarılmak;geriye doğru ona yaslanmak;saz çatıdan sarkmak|fener;palmiyeler;yalıçapkını;minder|Adam ne yapıyor?|Ona arkadan sarılıyor.
5647|köpeğin yüzünü avuçlarına almak;biraz ekmek uzatmak;merdivenden aşağı eğilmek|önlük;köpek;merdiven;kâseler|Genç kadın ne yapıyor?|Köpeğin yüzünü avuçlarına alıyor.
5648|tavana yakın tırmanmak;siyah bir tişört giymek;siyah tayt giymek|pencereler;kutular;kâse;kadın|Yukarıdaki adam ne yapıyor?|Tavana yakın bir yerde tırmanıyor.
5649|kaykayı havaya kaldırmak;el çırpmak;bacağına dokunmak|gökyüzü;palmiyeler;şişe|Mavili adam ne yapıyor?|El çırpıyor.
5650|merdiveni göstermek;kısa kollu bir tişört giymek;crop top giymek|tırabzan;banknotlar;kaykay|Adam neyi gösteriyor?|Merdiveni gösteriyor.
5651|tarak tutmak;çok şaşırmış görünmek;pencerenin yanında uyumak|raf;kedi;tarak;saç|Kedi ne yapıyor?|Pencerenin yanında uyuyor.
5653|dev bir balkabağını itmek;küçük bir balkabağının yanında dev gibi durmak;gözlerini elleriyle gölgelemek|seyirciler;kara tahta;dev balkabağı;palet|Kadın ne yapıyor?|Dev bir balkabağını paletin üzerine itiyor.
5654|kürsüde surat asmak;altın madalyayı havaya kaldırmak;kollarını kavuşturmak|projektör;buket;gümüş madalya;kürsü|Mavili kadın nasıl hissediyor?|Gümüş madalyası yüzünden içi buruk.
5655|çizgili bir çorap taşımak;kahkahayı basmak;bir havlu çıkarmak|çorap;at;çamaşır makinesi;spor ayakkabılar|At ne taşıyor?|At çizgili bir çorap taşıyor.
5657|kutsal su serpmek;avuçlarını birleştirmek;kadını kutsamak|kilise;rahip;ağlar;balıkçı teknesi|Rahip ne yapıyor?|Teknedeki kadını kutsuyor.
5658|tezgâha yaslanmak;sevinçle havaya yumruk sallamak;tabağı öne itmek|duvar fayansları;tencereler;tabak;önlük|Mavili aşçı ne yapıyor?|Sevinçle havaya yumruk sallıyor.
5659|telefonunu bırakmak;telefonunu havaya kaldırmak;bir kruvasan almak|kadın;adam;kahve;kruvasan|Dışarıdaki adam ne yapıyor?|Telefonunu tutuyor.
5662|ellerini havaya kaldırmak;blenderin kapağını tutmak;yüzündeki sosu silmek|baharat kavanozları;blender;domates sosu;kesme tahtası|Adamın üstü neyle kaplı?|Üstü domates sosuyla kaplı.
5663|kum torbasına yumruk atmak;kum torbasını sabit tutmak;zincirlerle asılı durmak|duvar;pencere;kum torbası;şişe|Gri giyen adam ne yapıyor?|Kum torbasına yumruk atıyor.
5664|kollarını kaldırmak;bir taşı oynatmak;lambanın yanında oturmak|masa oyunu;kedi;lamba;bitki|Üç arkadaş ne yapıyor?|Masa oyunu oynuyorlar.
5665|bir kalasın üzerinde yürümek;çelik bir halatı tutmak;çıkıntıdan izlemek|emniyet kemeri;sis;uçurum;kalas|Tırmanıcı ne yapıyor?|Dar bir kalasın üzerinde yürüyor.
5667|ayağa fırlamak;iki başparmağını aşağı çevirmek;sahnede öne eğilmek|spot ışığı;kâğıt uçak;garson;bira dolu bardak|Turuncu giyen adam ne yapıyor?|Sahnedeki komedyeni yuhalıyor.
5668|bir masayı göstermek;sandalyeyi çekmek;kalem tutmak|bitki;çiçekler;masa;kitap|Kadın nereyi gösteriyor?|Pencere kenarındaki bir masayı gösteriyor.
5669|avuçlarını birleştirmek;kapı koluna uzanmak;bordo bir bluz giymek|fener;cam kapı;sürahi;masa örtüsü|Siyahlı adam ne yapıyor?|Avuçlarını birleştiriyor.
5670|iki parmağını kaldırmak;yeşil saten bir bluz giymek;kontrbas tutmak|ışık zincirleri;kemerli pencere;kontrbas;keten takım elbise|Adam ve kadın ne yapıyor?|Geniş bir salonda tokalaşıyorlar.
5672|tahtayı göstermek;gözlerini kocaman açmak;lacivert bir tişört giymek|pencere;bitki;kahve fincanı;defter|Genç adam ne yapıyor?|Sırasında uyuyor.
5674|sineği kovalamak;bir sandviçi sıkıca tutmak;sinirle kaşlarını çatmak|kum tepesi;sandviç;termos;hurmalar|Kadını ne rahatsız ediyor?|Onu bir sinek rahatsız ediyor.
5675|sandalyeye bağlı oturmak;büyük pembe bir fiyonk bağlamak;kurdeleyi sıkıca çekmek|direk;fiyonk;katlanır sandalye|Sarılı kadın ne yapıyor?|Başına bir fiyonk bağlıyor.
5677|zaferle iki kolunu kaldırmak;pisti göstermek;şaşkınlıkla arkasını dönmek|neon tabela;lobutlar;oluk;bowling pisti|Kadın ne yapıyor?|Zaferle iki kolunu kaldırıyor.
5678|ayak tırnaklarını boyamak;saatine kaşlarını çatarak bakmak;kadife kanepede uzanmak|ayaklı lamba;kedi;oje;sehpa|Adam ne yapıyor?|Saatine kaşlarını çatarak bakıyor.
5679|koluna nazikçe dokunmak;boş bir kasayı sıkıca tutmak;ona bir belge göstermek|sokak lambası;gökyüzü;baraka;tahta kasa|Adam ne tutuyor?|Boş bir tahta kasa tutuyor.
5680|kahkahalarla gülmeye başlamak;çay masasının başında diz çökmek;masanın üzerinde paytak paytak yürümek|fener;bambu;ördek;alçak masa|Kadın ne yapıyor?|Kahkahalarla gülmeye başlıyor.
5681|kollarını başının üstüne doğru germek;şaşkınlıktan nefesi kesilmek;kolunu dümdüz uzatmak|disko topu;spot ışıkları;dans pisti|Kıvırcık saçlı kadın ne yapıyor?|Şaşkınlıktan nefesi kesiliyor.
5682|su altında yavaşça nefes vermek;dalgıcın yanından yüzüp geçmek;yüzeye doğru yükselmek|kabarcıklar;balık;ağırlık;deniz tabanı|Kadın ne yapıyor?|Ağzından kabarcıklar çıkarıyor.
5683|çenesini eline dayamak;blazer ceketini çıkarmak;kumu bitmek|kum saati;mermer masa;beyaz gömlek;yeşil bluz|Adam ne yapıyor?|Blazer ceketini çıkarıyor.
5685|kalabalığa eğilerek selam vermek;kollarını iki yana açmak;el çırpmak|kalabalık;bayrak;adam;gül|Adam ne yapıyor?|Kalabalığa eğilerek selam veriyor.
5686|yavru köpeği kucağında tutmak;yavru köpeğin çenesini kaşımak;yavru köpeğe doğru eğilmek|üzümler;fener;yavru köpek;su kabı|Adam ne yapıyor?|Yavru köpeğin çenesini kaşıyor.
5687|taze somun ekmek teslim etmek;kargo bisikletinden inmek;somun ekmeklerle dolu olmak|ışık zincirleri;bisikletli;somun ekmekler;kasa|Bisikletli kadın ne yapıyor?|Taze somun ekmek teslim ediyor.
5689|sürgüleri ayarlamak;mikrofona konuşmak;kapının üstünde yanmak|radyo direği;kulaklık;mikrofon;mikser masası|Adam ne yapıyor?|Mikrofona konuşuyor.
5691|aynada selfie çekmek;kanatlarını çırpmak;alnını ovuşturmak|avize;papağan;hasır sandalye;etek|Papağan ne yapıyor?|Yüzünün hemen yanında kanatlarını çırpıyor.
5695|kumlu yolu geçmek;takla demirini sıkıca tutmak;dikenli çalıların yanında durmak|çalılık;termit tepesi;antilop;takla demiri|Antilop ne yapıyor?|Kumlu yolu geçiyor.
5696|çiçeklerin parasını ödemek;parayı almak;masanın altında uyumak|pencere;adam;masa;köpek|Kotlu kız ne satın alıyor?|Çiçek satın alıyor.
5697|bir demet yıldız çiçeğine sarılmak;banknota uzanmak;sırasını beklemek|cam çatı;asma terazi;buket;ambalaj kâğıdı|Koyu saçlı kadın ne yapıyor?|Bir demet yıldız çiçeği satın alıyor.
5698|topu istemek;atışını bloklamaya çalışmak;topu başının üzerinde tutmak|basketbol topu;pota;crop top;çit|Kadın ne yapıyor?|Topu istiyor.
5699|ona gel diye el sallamak;ona doğru ağır ağır yürümek;kıyıda durmak|gökyüzü;lamba direği;tekne;kum|Adam ne yapıyor?|Ona gel diye el sallıyor.
5700|kapıyı açık tutmak;gidonu sıkıca kavramak;verandada dolaşmak|fener;kapı;bisiklet;saksı|Adam ne yapıyor?|Gidonu sıkıca kavrıyor.
5701|bir arduvaz parçası uzatmak;heyecanla seslenmek;dik çatıda diz çökmek|fırtına bulutları;deniz;arduvaz;kiremitler|Kadın ne yapıyor?|Çatıdan sesleniyor.
5702|gözlerini kapatmak;omzuna dokunmak;yavaşça nefes vermek|lamba;adam;kadın;motosiklet|Adam ne yapıyor?|Gözlerini kapatıyor.
5703|dondurmasını iştahla kaşıklamak;inanamayarak el kol hareketi yapmak;battaniyenin altına sokulmak|sarkıt lamba;el çantası;battaniye;kanepe|Pijamalı kadın ne yapıyor?|Dondurmasını iştahla kaşıklıyor.
5704|çelik bir kirişi havada tutmak;sarkan bir kayışı tutmak;çömeldiği yerden doğrulmak|çelik kiriş;vinç kancası;pelerin;gökdelenler|Süper kahraman ne yapıyor?|Kocaman bir çelik kirişi kaldırıyor.
5705|araba anahtarını havaya kaldırmak;arabaların arasında yürümek;bir arabanın üzerinde oturmak|lamba;araba;kedi;kadın|Kadın ne yapıyor?|Arabaların arasında yürüyor.
5706|zaferle kolunu kaldırmak;gözlerini devirmek;masanın altında yatmak|bagaj rafı;karton bardaklar;iskambil kâğıtları;spaniel|Adam ne yapıyor?|Gözlerini deviriyor.
5707|kaplumbağayı kucağında tutmak;bir çilek uzatmak;bir çileği kemirmek|göl;kaplumbağa;çiçek tarhı;kâse dolusu çilek|Adam ne yapıyor?|Kaplumbağaya çilek yediriyor.
5708|paltosunu iki yana açmak;ıslak bir köpeği sıkıca tutmak;bir alışveriş arabasının arkasında durmak|sokak lambası;alışveriş arabası;köpek;asfalt|Genç kadın ne yapıyor?|Islak köpeği göğsüne bastırıyor.
5711|yavru filin başını okşamak;şişeden kana kana süt içmek;hortumunu yukarı kıvırmak|akasya ağaçları;çit;süt şişesi;battaniye|Adam ne yapıyor?|Yavru fili şişeyle besliyor.
5714|bir çam kozalağını kemirmek;mezar taşından atlamak;kırağılı çimenlerde koşuşturmak|çam ağaçları;sincap;mezar taşı;çimen|Sincap ne yapıyor?|Sincap bir çam kozalağını kemiriyor.
5715|el yazısı bir mektubu kesmek;metal bir cetveli sabit tutmak;bazı kâğıtları incelemek|taş kemer;masa lambası;zarflar;mektup|Öndeki kadın ne yapıyor?|Bir bıçakla mektubu kesiyor.
5716|geçen penguenleri göstermek;kıyı boyunca paytak paytak yürümek;bir kutunun etrafında toplanmak|bere;buzdağı;penguenler;sırt çantası|Kadın ne yapıyor?|Kıyıdaki penguenleri sayıyor.
5717|durmadan dönmek;kollarını açık tutmak;duvarların üzerinden uçmak|gökyüzü;kadın;kum;daire|Kadın ne yapıyor?|Ortada dönüyor.
5718|tahta bir blok çekmek;tabanı sabit tutmak;telaşla iki elini kaldırmak|ampul;kule;kitap;kupa|Kadın ne yapıyor?|Telaşla iki elini kaldırıyor.
5719|pirinç bir mührü bastırmak;sertifikayı havaya kaldırmak;sevinçle gülümsemek|avize;saksı bitkisi;hırka;sertifika|Genç kadın ne yapıyor?|Sevinçle gülümsüyor.
6814|geçit yolu boyunca gitmek;şapkasını tutmak;kayalık bir adada durmak|manastır;hasır şapka;yağmurluk;bisiklet|Kadın ne yapıyor?|Geçit yolu boyunca bisiklet sürüyor.
6815|yarım limonu sıkmak;telefonuyla çekim yapmak;kalabalığın üzerinde yükselmek|aslan;koruyucu gözlük;test şeridi;kâse|Gözlüklü kadın ne yapıyor?|Yarım limonu sıkıyor.
6816|gözlerini eliyle gölgelemek;duvar piyanosu çalmak;bir sulama kabını eğmek|sulama kabı;elektrikli vantilatör;duvar piyanosu;tahta sandalye|Oyuncu ne yapıyor?|Sahnede bir fırtınayı canlandırıyor.
6817|megafonla bağırmak;yolda diz çökmek;yanan bir dünyayı göstermek|polis memuru;aktivist;bayrak;kamyon|Aktivist ne yapıyor?|Megafonla bağırıyor.
6818|ofisin içinden patenle geçmek;ağır klasörler taşımak;yeşil bir kazak giymek|idari görevli;klasörler;eski bilgisayar;patenler|İdari görevli ne yapıyor?|Ofisin içinden patenle geçiyor.
6819|bir platformda durmak;mavi bir dosya tutmak;rüzgârda dalgalanmak|bayrak;römorkör;amiral;platform|Amiral nerede duruyor?|Ahşap bir platformda duruyor.
6821|cüzdanına göz atmak;bir deniz ürünleri tabağı taşımak;şampanyayı doldurmak|avize;ıstakoz;menü;cüzdan|Garson ne getiriyor?|Kocaman bir deniz ürünleri tabağı getiriyor.
6823|şok içinde yukarı bakmak;kaldırıma fışkırmak;dar sokağı kapatmak|balıkçı teknesi;köpek;kasa;deniz yosunu|Kadın neye bakıyor?|Karaya oturmuş bir tekneye bakıyor.
6825|beyaz bir yorganı silkelemek;yastıkları düzeltmek;bir yastığın üzerinde dinlenmek|kilise kulesi;sardunyalar;yorgan;kilim|Genç kadın ne yapıyor?|Balkondan yorganı silkeliyor.
6826|bankta keyif yapmak;yerde yuvarlanmak;duvarın üzerinden eğilmek|perdeler;rüzgâr çanı;hasır şapka;kedi|Adam ne yapıyor?|Mavi bir minderde keyif yapıyor.
6827|beyaz bir yastıkta uyumak;başını kaldırmak;bir gazetenin üzerinde durmak|kadın;yastık;çalar saat;bardak|Kadın ne yapıyor?|Beyaz bir yastıkta uyuyor.
6828|kollarını iki yana açmak;sıra halindeki işçilere öncülük etmek;kıskaçlı bir not altlığı taşımak|alarm zili;uyarı lambası;tavan;baret|Kadın ne yapıyor?|Kollarını iki yana açıyor.
6829|bir rehber kitabı incelemek;başını kaldırıp tabelalara bakmak;kâğıt bir poşet uzatmak|fener;rehber kitap;bavul;dükkân tabelası|Sarışın kadın ne yapıyor?|Bir rehber kitabı inceliyor.
6830|halatlarla asılı durmak;havada yavaşça dönmek;kapıların yanında boşta durmak|alüminyum;oluklu çatı;forklift;baret|Tekne gövdesi ne yapıyor?|Gövde halatlarla asılı duruyor."""
out = {}
for line in R.strip().split('\n'):
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: out[i] for i in src}
json.dump(out, open(f'{H}/b023/tr.json', 'w'), ensure_ascii=False, indent=1)
