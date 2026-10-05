import json, os
H = os.path.dirname(os.path.abspath(__file__))
R = """
6831|bir mango dilimini havaya kaldırmak;omzuna konmak;bir tepsinin altına eğilmek|tente;palmiye ağaçları;mangolar;amazon papağanı|Adam ne yapıyor?|Bir tepsinin altına eğiliyor.
6832|kameraya kocaman gülümsemek;mühürlü bir zarf taşımak;saray merdivenleri boyunca dizilmek|merdivenler;atlar;zarf;tekerlek|Kadın ne tutuyor?|Mühürlü bir zarf tutuyor.
6833|kavisli bir çizgi çizmek;birkaç çıktıyı sıkıca tutmak;eğriyi göstermek|gözlük;yapışkan not;dizüstü bilgisayar;karton bardak|Adam ne çiziyor?|Kavisli bir çizgi çiziyor.
6834|açıyı ölçmek;bir merdivenin üzerinde durmak;bir kirişi desteklemek|açı;gönye;alet çantası;reflektörlü yelek|Kadın neyi ölçüyor?|Açıyı ölçüyor.
6835|minik tohumlar saçmak;ovada dörtnala koşmak;dağların üzerinde süzülmek|şahin;atlar;gelincikler;kaplumbağa|Atlar ne yapıyor?|Atlar ovada dörtnala koşuyor.
6837|bir yangını söndürmek;bir tabağı havaya kaldırmak;bir salata kâsesi tutmak|tabak;parti şapkası;bitki;mangal|Sarılı kadın ne yapıyor?|Bir yangını söndürüyor.
6838|kutsamak;uzun bir asayı havaya kaldırmak;bir buhurdanı sallamak|gül pencere;başpiskopos;kilise sıraları|Genç ayin yardımcısı ne yapıyor?|Bir buhurdanı sallıyor.
6839|kâğıttan bir maket tutmak;havai fişeklere bakmak;gökyüzünü aydınlatmak|havai fişekler;bina;maket;kadın|Kadın ne tutuyor?|Kâğıttan bir maket tutuyor.
6840|bir koliyi yere bırakmak;bir feribot bileti tutmak;yüklü bir bagaj arabasını itmek|feribot;kır evi;sırt çantası;koli|Kırmızılı kadın ne tutuyor?|Bir feribot bileti tutuyor.
6842|bir tekerlek göbeğini yerine yönlendirmek;tekerlek göbeğinden geri çekilmek;kamyondan izlemek|vinç;düzenek;lastik;palet|Genç işçi ne yapıyor?|Bir tekerlek göbeğini yerine yönlendiriyor.
6843|bir içeceği yudumlamak;kendini yelpazelemek;hasır şapka takmak|güneş şemsiyesi;el vantilatörü;seyyar merdiven;hasır şapka|Yukarıdaki adam ne yapıyor?|Bir içeceği yudumluyor.
6845|kocaman bir kayayı kaldırmak;dişlerini sıkmak;kasket takmak|bayrak süsü;fıçı;köpek;kaya|Genç adam ne yapıyor?|Kocaman bir kayayı kaldırmaya çalışıyor.
6846|bir sözleşme uzatmak;pantolonlu takım giymek;kanepede kıpırdanmak|avukat;perde;sözleşme;banknotlar|Avukat ne yapıyor?|Avukat kalın bir sözleşme uzatıyor.
6847|paslı zincirlerden sarkmak;uzun gümüş rengi saçları olmak;kabinde oturmak|mıknatıs;ekskavatör;hurda metal;çamur|Dev mıknatıs ne yapıyor?|Mıknatıs iki metal levhayı çekiyor.
6848|megafonla bağırmak;lacivert üniforma giymek;kırmızı bir bayrak taşımak|şemsiye;bayrak;megafon;cankurtaran kulesi|Üniformalı kadın ne yapıyor?|Megafonla bağırıyor.
6850|pastasını iştahla yemek;kameraya el sallamak;birbirine sokularak dans etmek|bekâr adam;dekoratif ışıklar;el çantası;pasta dilimi|Bekâr adam ne yapıyor?|Bir dilim pastayı iştahla yiyor.
6851|bir sabit diski etiketlemek;masanın üzerine eğilmek;bir ilerleme çubuğu göstermek|metal kutu;kupa;dizüstü bilgisayar;ahşap masa|Adam ne yapıyor?|Bir sabit diski etiketliyor.
6852|bir petri kabını havaya kaldırmak;şaşkınlıktan nefesi kesilmek;büyütülmüş bakterileri göstermek|bakteriler;UV lambası;laboratuvar önlüğü;eşofman üstü|Adam ne tutuyor?|Bir petri kabı tutuyor.
6853|birkaç ördek taşımak;kuyruğunu sallamak;gökyüzünde uçmak|kep;ördekler;köpek;çanta|Kadın ne taşıyor?|Birkaç ördek taşıyor.
6854|kırmızı banda hayranlıkla bakmak;iskelenin yanında suda süzülmek;nehre bakmak|kayıkhane;sandal;bant;kangal halat|Gülümseyen kadın ne yapıyor?|Kırmızı banda hayranlıkla bakıyor.
6855|çiçekleri birbirine bağlamak;çiçekleri yukarı kaldırmak;kep takmak|araba;bıçak;sicim;masa|Genç adam ne yapıyor?|Çiçekleri birbirine bağlıyor.
6856|kırmızı bir kurdele bağlamak;bir sürü ekmek taşımak;sakallı olmak|lamba;ekmek;masa;köpek|Güneş gözlüklü kadın ne yapıyor?|Kırmızı bir kurdele bağlıyor.
6858|belgeyi öne doğru kaydırmak;belgeyi açmak;büyük bir muhasebe defteri okumak|bankacı;muhasebe defteri;masa lambası;banknotlar|Sakallı adam ne yapıyor?|Belgeyi açıyor.
6859|bir saman balyasını itmek;kollarını çılgınca sallamak;otoyolda ilerlemek|saman balyası;sığırlar;çit kapısı;taş duvar|Genç adam ne yapıyor?|Bir saman balyasını itiyor.
6860|kapıyı ardına kadar açmak;bir deste anahtar tutmak;bir kek kutusu taşımak|şato;kek kutusu;katlanır masa;çakıl|Pembeli kadın ne taşıyor?|Bir kek kutusu taşıyor.
6861|gümüş bir tepsiye uzanmak;belden öne eğilmek;bir şampanya kadehini havaya kaldırmak|avize;gümüş tepsi;konuklar;kırmızı halı|Genç adam neye uzanıyor?|Gümüş bir tepsiye uzanıyor.
6862|kusursuz bir şekilde amuda kalkmak;bardan savrularak inmek;yumruklarını kaldırarak kutlamak|gökyüzü;adam;paralel bar;tuz|Adam ne yapıyor?|Barın üzerinde amuda kalkıyor.
6863|çuvalların üzerinde uyumak;fasulyeleri yemek;yere düşmek|kedi;tekerlek;tavuklar;fasulyeler|Tavuklar ne yiyor?|Fasulyeleri yiyorlar.
6864|samanın içinde diz çökmek;titrek bacaklarının üzerinde durmak;yeni doğmuş kuzuyu yalamak|fener;kova;kuzu;saman|Koyun ne yapıyor?|Yeni doğmuş kuzuyu yalıyor.
6865|bir düğün pastasını dengede tutmak;aşçının kolunu koklamak;çamurda devrilmiş halde yatmak|düğün pastası;büyük çadır;alışveriş arabası;çamur|Aşçı ne yapıyor?|Bir düğün pastasını başının üzerinde taşıyor.
6866|sudan çıkmak;büyük ineğin peşinden gitmek;suyun üzerinde uçmak|gökyüzü;ağaçlar;nehir;taşlar|Büyük inek ne yapıyor?|Sudan çıkıyor.
6868|direksiyonu sıkıca kavramak;dantel bir gelinlik giymek;uçuk pembe bir elbise giymek|tüyler;yastık;siperlikli kep;direksiyon|İki yolcu ne yapıyor?|Yastık savaşı yapıyorlar.
6870|bir arabanın tavanına tünemek;bir havucu kapmak;bir havuç uzatmak|teke;taş ev;klasik araba;lastik çizmeler|Teke neyin üzerinde duruyor?|Klasik bir arabanın üzerinde duruyor.
6871|piskoposun mitrasını kapmak;kutsamak;şaşkınlıkla elini ağzına kapamak|mitra;at;piskopos;keçi|At ne yapıyor?|Piskoposun mitrasını kapıyor.
6872|kocaman dişlerini göstermek;ağzından salya akıtmak;kahkahayı basmak|kask;gem;dişler;kum|At ne yapıyor?|Kocaman dişlerini gösteriyor.
6873|bir halatı çekiştirmek;buhar püskürtmek;düdüğe bağırmak|pirinç düdük;buhar;örgü bere;kangal halat|Pirinç düdük ne yapıyor?|Havaya buhar püskürtüyor.
6874|ağzı dolusu keki çiğnemek;klavyede durmadan yazmak;dizüstü bilgisayarın arkasına gizlenmek|blog yazarı;dekoratif ışıklar;dizüstü bilgisayar;karıştırma kabı|Blog yazarı ne yapıyor?|Ağzı dolusu keki çiğniyor.
6875|tansiyonunu ölçmek;kolunu uzatmak;kapı aralığında çömelmek|fener;gaz tüpü;acil durum battaniyesi;buz baltası|Kadın ne yapıyor?|Adamın tansiyonunu ölçüyor.
6876|küçük bir uçağa binmek;uçağa binmesine yardım etmek;bagajları yüklemek|pervane;rüzgâr tulumu;palmiye ağaçları;bagaj arabası|Kadın ne yapıyor?|Küçük bir uçağa biniyor.
6877|bir çivi çakmak;telaşla etrafına bakmak;gökyüzünü karartmak|büfe;toz fırtınası;çekiç;yaşlı adam|Genç adam ne yapıyor?|Pencereyi tahtalarla kapatıyor.
6879|bariyerler boyunca kaymak;buzun üzerinde boylu boyunca yatmak;yedek kulübesinden bağırmak|taraftarlar;antrenör;bariyerler;buz|Kayan oyuncu ne yapıyor?|Bariyerler boyunca kayıyor.
6882|dev bir davula vurmak;bageti başının üzerinde sallamak;sahnenin üzerinde parlamak|fenerler;davul;seyirciler;su birikintisi|Öndeki adam ne yapıyor?|Dev bir davula vuruyor.
6883|bir ses sürgüsünü yukarı itmek;kolunu kaldırarak tezahürat yapmak;kollarını kavuşturup durmak|spot ışıkları;kalabalık;kulaklık;mikser masası|Ses mühendisi ne yapıyor?|Mikser masasındaki bir ses sürgüsünü kaydırıyor.
6884|kahveyi yüksekten doldurmak;fincandan yalayarak içmek;masanın üzerine eğilmek|kahve demliği;önlük;separe;pankekler|Köpek ne yapıyor?|Fincandaki kahveyi yalayarak içiyor.
6885|poposuna dokunmak;dondurmasını düşürmek;bankı göstermek|ağaç;popo;bank;tabela|Adam ne yapıyor?|Bankı gösteriyor.
6886|kum tepesinden sıçrayarak inmek;ayaklarıyla kum savurmak;dik yamaçta oturmak|kum tepesi;eşarp;develer;yürüyüşçüler|Kadın ne yapıyor?|Kum tepesinden sıçrayarak iniyor.
6888|ipin üzerinden savrulmak;suya düşmek;pencerenin yanında yatmak|havlu;sütyen;bisiklet;kedi|Sütyen nerede asılı?|Sütyen ipte asılı.
6889|masa boyunca büyük adımlarla yürümek;satranç tahtalarını göstermek;ellerini başına götürmek|avize;göz bağı;perde;satranç saati|Kadın ne yapıyor?|Uzun masa boyunca büyük adımlarla yürüyor.
6890|pistte sert fren yapmak;bordür boyunca kaymak;ön planda üst üste yığılı durmak|spor araba;frenler;lastikler;projektör|Mavi araba ne yapıyor?|Araba bordür boyunca kayıyor.
6891|çamur düzlüklerinin üzerinde süzülmek;daha küçük derelere ayrılmak;karaya oturmuş halde durmak|kol;gölge;ahşap direkler;sandal|Uçağın gölgesi ne yapıyor?|Çamur düzlüklerinin üzerinde süzülüyor.
6892|ağır bir el arabasını boşaltmak;yığının üzerinde oturmak;kulaklarını kapatmak|önlük;teriyer;pirinç;el arabası|Kadın ne yapıyor?|Ağır bir el arabasını boşaltıyor.
6893|yumruğunu havaya savurmak;inanamayarak bakmak;yeni rekoru göstermek|skor tabelası;kalabalık;yüzme havuzu;yüzücü gözlüğü|Öndeki yüzücü ne yapıyor?|Sevinçle yumruğunu havaya savuruyor.
6894|motoru çıkarmak;ellerini kenetlemek;ellerini silmek|tenis filesi;bez;motor;yaylar|Tamirci ne yapıyor?|Motoru şasiden kaldırıp çıkarıyor.
6896|çimenlerin üzerinde hızla koşmak;boştaki ipe uzanmak;şapkasını başının üzerinde sallamak|inek;yular ipi;beyaz önlük;kova|Kaçak inek ne yapıyor?|Çimenlerin üzerinde hızla koşuyor.
6897|vana anahtarını çevirmek;bir çalı çitin üzerinden atlamak;kameraya bakmak|çardak;battaniye;gökkuşağı;parmak arası terlik|Çömelmiş adam ne yapıyor?|Vana anahtarını çeviriyor.
6898|havaya sıçramak;domuzun peşinden atılmak;kenardan tırmanarak geçmek|bulutlar;klipsli panolar;rozet;kuşak|Ödüllü domuz ne yapıyor?|Gösteri alanından kaçıyor.
6899|tipide tünemek;göğsünü kabartmak;korkuluğun altında sarkmak|göğüs;kanat;korkuluk;buz sarkıtları|Kızılgerdan ne yapıyor?|Kızılgerdan buzlu bir korkuluğa tünemiş duruyor.
6900|saçını düzgün bir topuz yapmak;ellerinin tozunu silkelemek;taşa dikkatle bakmak|kalabalık;kasket;taş levha;eldivenler|Genç kadın ne yapıyor?|Ağır bir taş levhayı indiriyor.
6901|bronz bir çanı indirmek;ahşap bir desteğin üzerine oturmak;iki elini kaldırmak|kilise kulesi;çan;örgü;kum torbaları|Genç kadın ne yapıyor?|Ağır bronz bir çanı indiriyor.
6902|bir kuzuyu yere bırakmak;yeni doğmuş kuzuyu koklamak;parmaklıkların yanında oturmak|koyun;kuzu;havlu;çoban köpeği|Koyun ne yapıyor?|Koyun yeni doğmuş kuzuyu kokluyor.
6903|bir tuvaldeki kiri silmek;küçük bir cam kavanozu tutmak;ahşap bir şövalenin üzerinde durmak|tablo;şövale;pamuklu çubuklar;renk kartelası|Kadın ne yapıyor?|Tablodaki kiri siliyor.
6904|burnunu kırıştırmak;bir masanın üzerine boylu boyunca uzanmak;bir kurulama bezini sıkıca tutmak|vişneli turta;sürahi;bayrak süsü;piyano|Kadın ne yapıyor?|Adamın burnunun dibine otlu bir turta tutuyor.
6905|erimiş metal dökmek;ahşap bir kaidenin üzerinde durmak;kıpkırmızı parlamak|bronz;pota;önlük;duman|Genç adam ne yapıyor?|Bir huninin içine erimiş metal döküyor.
6906|bir kitaplığa kaykılarak yaslanmak;bir rafı öylesine göstermek;bir deftere bir şeyler karalamak|göz atan müşteri;pencere;masa lambası;karton kutu|Adam ne yapıyor?|Bir kitaplığa kaykılarak yaslanıyor.
6907|kanepede dengede durmak;sıcak bir içeceği dökmek;kucaklarına boylu boyunca uzanmak|güneş;köpek;termos;kayak batonları|Köpek ne yapıyor?|Köpek kanepede dengede duruyor.
6909|çarşafın üzerinde yürümek;sırığın üzerinde oturmak;karanlıkta parlamak|lamba;kınkanatlı böcek;böcekler;kutu|Büyük kınkanatlı böcek ne yapıyor?|Çarşafın üzerinde yürüyor.
6910|elmadan hızla uzaklaşmak;patlayarak açılmak;sis salmak|altın varak;elma;kurşun;buz|Kurşun ne yapıyor?|Elmadan hızla uzaklaşıyor.
6911|başını korumak;bir pasta kutusunu sıkıca tutmak;gidonu sıkıca kavramak|otobüs durağı;kâğıt torba;pasta kutusu;otobüs|Sırılsıklam adam ne yapıyor?|Başını kâğıt torbayla koruyor.
6912|eşarpları havaya atmak;bir çekmeceyi karıştırmak;çizgili bir çorabı havaya kaldırmak|şifonyer;çorap;perde;laleler|Kadın neyi havaya kaldırıyor?|Çizgili bir çorabı başının üzerinde tutuyor.
6913|bir banktan atlamak;sırt çantasını takmak;bir koltukta uyumak|otobüs;bank;çiçekler;köpek|Yaşlı adam ne yapıyor?|Bir koltukta uyuyor.
6914|paslı bir kapıyı tekmelemek;başını arkaya atmak;bulut bulut buhar çıkarmak|buhar;falezler;yan ayna;yedek lastik|Arabadan ne fışkırıyor?|Arabadan buhar fışkırıyor.
6915|oltayı sıkıca kavramak;çekişe karşı geriye yaslanmak;derin bir yay çizerek bükülmek|olta;burun;dalgalar;kova|Kadın ne tutuyor?|Bükülmüş bir oltayı sıkıca kavrıyor.
6916|trenden dışarı sarkmak;metal bir tutamağı tutmak;çok parlak yanmak|makinist kabini;kasket;ateş;duman|Adam ne yapıyor?|Trenden dışarı sarkıyor.
6917|limana girmek;bir kangal halat fırlatmak;liman duvarının üzerinden aşmak|yelkenli gemi;deniz feneri;balıkçı tekneleri;liman duvarı|Yelkenli gemi ne yapıyor?|Küçük bir limana uğruyor.
6918|tek parmağıyla çağırmak;bir deste kâğıt tutmak;koridorda yürümek|güneş gözlüğü;portmanto;muz kostümü;kâğıtlar|Kadın ne yapıyor?|Tek parmağıyla çağırıyor.
6919|metal bir milin üzerinde dönmek;güneş ışınlarının arasından uçup gitmek;çatıların üzerinde asılı durmak|çan;kam;dişliler;yağdanlık|Büyük kam ne yapıyor?|Metal bir milin üzerinde dönüyor.
6920|bardaktan kahve yudumlamak;klozetin üzerinde yalınayak oturmak;tuz düzlüğünde durmak|klozet;güneş gözlüğü;saten elbise;tuz düzlüğü|Kadın ne yapıyor?|Klozetin üzerinde kahve yudumluyor.
6922|karla kaplı yolu temizlemek;kubbenin üzerinde dönüp durmak;karda terk edilmiş halde yatmak|meclis binası;kar küreme aracı;tırabzan;eldiven|Sarı kar küreme aracı ne yapıyor?|Karla kaplı yolu temizliyor.
6923|sıyrılmış bir dizi sarmak;acıyla yüzünü buruşturmak;ambalajları koklamak|bandaj;ilk yardım çantası;kasa;kaykay|Kadın ne yapıyor?|Adamın sıyrılmış dizini sarıyor.
6924|tepeden aşağı son hızla inmek;yumruğunu havaya savurmak;samanın içine atlamak|küvet;saman balyaları;kilise kulesi;balkon|Koruyucu gözlüklü kadın ne yapıyor?|Arnavut kaldırımlı sokaktan son hızla aşağı iniyor.
6925|ağır bir karpuzu yakalamak;ahşap bir arabayı çekmek;arabanın arkasından tırıs gitmek|karpuzlar;hasır şapka;araba;at|At ne yapıyor?|Ahşap bir arabayı çekiyor.
6926|gri bir dronu açmak;sert bir çantayı kapatmak;kar küremek|çadır;dron;kızak;çanta|Kadın ne yapıyor?|Gri bir dronu açıyor.
6927|biraz nakit çekmek;kuyruğa doğru dönmek;pullu bir palto giymek|ponponlu bere;pullu palto;bankamatik;kar|Kadın ne yapıyor?|Bankamatikten para çekiyor.
6928|eliyle ağzını kapatarak gülmek;uzun bir tırmık tutmak;siyah smokin giymek|oyun masası;el arabası;rulet çarkı|Yeşilli kadın ne yapıyor?|Eliyle ağzını kapatarak gülüyor.
6929|ağır bir çekiç sallamak;keyifle sırıtmak;yoğun ısıyla parlamak|zincirler;döküm;çekiç;kalıp|Gülümseyen adam ne yapıyor?|Kor gibi parlayan döküme bakıp sırıtıyor.
6930|otobüse atlamak;duraktan uzaklaşmak;bir su birikintisine düşmek|gökyüzü;otobüs;atkı;su birikintisi|Kadın ne yapıyor?|Kırmızı otobüse atlıyor.
6931|yol arkadaşlarına göz atmak;gri bir bisiklet forması giymek;ortada pedal çevirmek|dağlar;örgü;yol|Kadın ne yapıyor?|Yol arkadaşlarına göz atıyor.
6933|yastık savaşı başlatmak;darbeden irkilmek;bir koltuktan izlemek|pencere;gardırop;yastık;kruvasanlar|İki kadın ne yapıyor?|Yastık savaşı yapıyorlar.
6935|dik duvarda asılı durmak;bacaklarını sallamak;tırmanıcının altında sarkmak|çatı penceresi;kafe tezgâhı;merdiven;minderler|Kadın ne yapıyor?|Dik duvarda asılı duruyor.
6937|demir bir pranga tutmak;yumruğunu havaya savurmak;folyo bir battaniyeyi açmak|sokak lambası;ay;tekneler;zincirler|Siyahlı kadın ne yapıyor?|Demir bir pranga tutuyor.
6938|dişleriyle bir düdüğü sıkmak;inanamayarak nefesi kesilmek;kenarı üzerinde dengede durmak|projektörler;düdük;madeni para;çamur|Oyuncu ne yapıyor?|İnanamayarak nefesi kesiliyor.
6939|ceket giymek;altın rengi bir ceketi yere atmak;yerde diz çökmek|perde;kıyafetler;altın rengi ceket;ayakkabılar|Öndeki adam ne yapıyor?|Kıyafetlerini değiştiriyor.
6940|bir trene atlamak;bir bavul çekmek;yeşil bir bayrak sallamak|tren;köpek;elma;fincan|Kadın ne yapıyor?|Bir trene atlıyor.
6941|eski bir fotoğrafı havaya kaldırmak;yıkılmış kulübeyi göstermek;kayalara çarpmak|plaj kulübesi;kayalar;fotoğraf;kupa|Adam ne yapıyor?|Yıkılmış kulübeyi gösteriyor.
6942|açık savak kapağından coşkuyla akmak;köpüğün içinde yüzmek;dar kanalın üzerinden geçmek|savak kapağı;yaya köprüsü;kanal;zeytin ağaçları|Su ne yapıyor?|Açık savak kapağından coşkuyla akıyor.
6943|uzun bir sopayı kaldırmak;seyircilere bağırmak;siyah bir şapka takmak|deniz;miğfer;şapka;sopa|Oyuncu ne yapıyor?|Seyircilere bağırıyor.
6944|telefonunu şarj etmek;kameraya gülümsemek;gözlerini kapatmak|kadın;adam;fincan;yastık|Kadın ne yapıyor?|Telefonunu şarj ediyor.
6945|metal bir halkayı çıkarmak;şaşkınlıkla elini ağzına kapamak;masa örtüsünü sıkıca tutmak|şarlot;aşçı;masa örtüsü;kadife bluz|Aşçı ne yapıyor?|Şarlotun etrafındaki metal halkayı çıkarıyor.
6946|bir demet acı biberi havaya kaldırmak;acı bir biberi çiğnemek;kendi üzerine su dökmek|kuru acı biberler;sepet;hakem;boyun atkısı|Genç adam ne yapıyor?|Acı bir biberi çiğniyor.
6947|acı chili servis etmek;bir kutunun üzerinde oturmak;kâseyi almak|kadın;tencere;köpek;chili|Kadın ne yapıyor?|Acı chili servis ediyor.
"""
out = {}
for line in R.strip().splitlines():
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
src = json.load(open(f'{H}/source.json'))
out = {k: out[k] for k in src}
json.dump(out, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
