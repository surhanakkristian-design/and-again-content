import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = r"""
4744~bir dergi okumak|büyük bir şapka takmak|siyah bir mayo giymek~şapka;dergi;ayaklar;tepeler~Öndeki kadın ne yapıyor?~Suda dergi okuyor.
4745~çakıl taşlarının üzerine çömelmek|akıntıyla sürüklenmek|nehrin üzerinden geçmek~taş köprü;hızlı akıntılar;kağıttan kayık;çimen~Nehir nereye akıyor?~Taş bir köprünün altından akıyor.
4746~uçağı göstermek|uçakların fotoğrafını çekmek|adamların üzerinden uçmak~uçak;fotoğrafçı;ceket;gökyüzü~Fotoğrafçılar ne yapıyor?~Bir uçağın fotoğrafını çekiyorlar.
4747~biraz ekmek tutmak|kuşlara gülümsemek|adamın etrafında uçmak~martı;kasket;ekmek;deniz~Martılar ne yapıyor?~Adamın etrafında uçuyorlar.
4748~aşağıdaki yeri gizlemek|bir uçağa ait olmak|açık ve mavi kalmak~bulutlar;kanat;gökyüzü~Yeri ne gizliyor?~Beyaz bulutlar yeri gizliyor.
4749~formasyon halinde el ele tutuşmak|bir Alp vadisinin üzerinde süzülmek|hasır bir sepete yaslanmak~sıcak hava balonu;güneş;tarlalar;hasır sepet~Paraşütçüler ne yapıyor?~Formasyon halinde el ele tutuşuyorlar.
4750~bir tişört katlamak|sepete uzanmak|kıyafetlerle dolu olmak~kadın;sepet;kıyafetler;yatak~Kadın ne yapıyor?~Yatağın üzerinde kıyafetleri katlıyor.
4751~sarı bir şemsiye tutmak|raylar üzerinde gitmek|dört ayak üzerinde yürümek~şemsiye;tramvay;köpek;rehber~Rehber ne tutuyor?~Sarı bir şemsiye tutuyor.
4752~hayal kırıklığıyla yüzünü buruşturmak|yanmış ekmeği dışarı fırlatmak|ocağın üzerinde durmak~ekmek kızartma makinesi;önlük;spatula;tava~Adam ne yapıyor?~Yanmış kurabiyelerine bakıp yüzünü buruşturuyor.
4753~kollarını sıkıca kavuşturmak|paket servis bir kahve ikram etmek|bantlı bir gidona sahip olmak~sakal;karton bardak;tuğla duvar;sele~Sakallı adam ne ikram ediyor?~Ona paket servis bir kahve ikram ediyor.
4754~sarı kart göstermek|sahaya yuvarlanmak|açık avuçlarla itiraz etmek~sarı kart;hakem;forma;çimen~Hakem oyuncuya ne gösteriyor?~Ona sarı kart gösteriyor.
4756~bisiklete binmek|kruvasan yemek|kadının arkasında oturmak~kule;nehir;ekmek;sepet~Kadın ne yiyor?~Kruvasan yiyor.
4757~bir kapının üzerinden atlamak|kollarını iki yana açmak|gökyüzünde parlamak~gökyüzü;tarla;bisiklet;yol~Çocuk ne yapıyor?~Yolda aşağı doğru bisiklet sürüyor.
4758~buzdolabının kapısını açmak|rafların üzerine yiyecek koymak|boş bir çekmecede durmak~dolap;adam;pizza;buzdolabı~Adam neye bakıyor?~Dolu bir buzdolabına bakıyor.
4759~bir bageti dinlemek|kruvasan tepsilerini dizmek|vitrinin önünde toplanmak~fırıncı;baget;önlük;kruvasanlar~Fırıncı ne yapıyor?~Fırıncı bir bageti kulağına tutuyor.
4761~bir yumurta kırmak|domuz pastırması dilimleri eklemek|bir tavayı ısıtmak~sakal;parka;domuz pastırması;gaz ocağı~Adam ne yapıyor?~Portatif bir ocakta domuz pastırması kızartıyor.
4762~deri bir evrak çantasını sıkıca tutmak|başını kaldırıp bir tuvale bakmak|uzaktaki duvarı kaplamak~tavan;heykel;kaide;evrak çantası~Adam ne yapıyor?~Bir galeride tablolara bakıyor.
4763~kanepeye yayılmak|ışıklı bir klavyeye dokunmak|şampiyonu göstermek~oyuncu;kumanda;televizyon;kanepe~Kanepeye kim yayılmış?~Bir oyuncu kanepeye yayılmış.
4764~kanepede zıplamak|yeşil bir kapüşonlu giymek|cipsle dolu olmak~kanepe;kadın;adam;kase~Kadın nerede zıplıyor?~Kanepede zıplıyor.
4766~bahçe kapısını açmak|kırmızı domateslere dokunmak|kırmızı bir çatısı olmak~gökyüzü;ev;kadın;çiçekler~Kadın neyi açıyor?~Bahçe kapısını açıyor.
4767~bir çalıyı budamak|çiçekleri sulamak|mavi bir önlük takmak~bahçıvan;sulama kabı;çiçekler;ağaçlar~Bahçıvan ne yapıyor?~Çiçekleri suluyor.
4768~bir hediye tutmak|iki kart tutmak|yukarı bakıp gülmek~kartlar;adam;kutu;pencere~Kahverengili adam ne tutuyor?~İki kırmızı kart tutuyor.
4769~ağzını kapatmak|mavi bir kasket takmak|çitin üzerinden bakmak~çit;gökyüzü;kasket;kayalar~Kadın nerede duruyor?~Bir çitin yanında duruyor.
4771~bir kapı açmak|kameraya gülümsemek|çok sayıda penceresi olmak~saray;kapı;gökyüzü;palto~Kadın neyi açıyor?~Sarayın kapısını açıyor.
4772~gökyüzünde daireler çizmek|sürüyü göstermek|onun kolunu sıkıca tutmak~sürü;bere;bataklık;korkuluk~Kadın neyi gösteriyor?~Bir kuş sürüsünü gösteriyor.
4773~akordeon çalmak|müzisyene el sallamak|omzunun üzerinden bakmak~akordeon;enstrüman kutusu;saç örgüsü;arnavut kaldırımı~İnsanlar ne yapıyor?~Bir müzisyenin etrafında toplanıyorlar.
4775~yeni doğmuş bir bebeği kucağında tutmak|battaniyeye sarılı uyumak|koyu renkli bir kapüşonlu giymek~yenidoğan;battaniye;minder;saksı bitkileri~Battaniyeye kim sarılı?~Yeni doğmuş bir bebek battaniyeye sarılı.
4777~bir atkıyı yerden almak|bir şemsiye açmak|çok sayıda poşet taşımak~şemsiye;adam;kadın;alışveriş poşetleri~Yağmurda ne açıyor?~Siyah bir şemsiye açıyor.
4778~minik pirinç dişlileri ayarlamak|ahşap bir direkte asılı durmak|iş arkadaşını alkışlamak~guguklu saat;İngiliz anahtarları;genç adam;tezgah~Kadın neyi gösteriyor?~Yukarıdaki oymalı guguklu saati gösteriyor.
4779~selfie çekmek|tepesinde atlar olmak|bir tepede durmak~kale;ağaçlar;adam;duvar~Adam ne yapıyor?~Almanya'da selfie çekiyor.
4780~koyu renk bir gömlek giymek|beyaz bir bluz giymek|uzun kahverengi saçları olmak~duvar;yüzükler;masa~Odadan nasıl çıkıyorlar?~Ayrı kapılardan çıkıyorlar.
4781~beyaz bir duvak takmak|sevinçten ağlamak|gelinine gülümsemek~ağaç;damat;gelin~Adam ve kadın ne yapıyor?~Bir bahçede evleniyorlar.
4782~ip atlamak|çocuklara göz kulak olmak|top sektirmek~bina;kız;kadın;oyun parkı~Kurdeleli kız ne yapıyor?~İp atlıyor.
4783~küçük bir pasta tutmak|basketbol oynamak|bir pankart kaldırmak~gökyüzü;bina;çift~Adam ne oynuyor?~Basketbol oynuyor.
4784~büyük bir hediye almak|ona biraz kurabiye vermek|bir fotoğraf albümüne bakmak~yaşlı kadın;hediye;tabak~Yaşlı kadın ne alıyor?~Büyük bir hediye alıyor.
4785~boş bir kadeh kaldırmak|kameraya göz kırpmak|polo tişört giymek~çalılar;sürahi;teras~Kadehleriyle ne yapıyorlar?~Kadeh tokuşturuyorlar.
4786~parlayan bir spiral çizmek|su kenarında çömelmek|kıyıya vurmak~kadın;dalgalar;spiral;kum~Kadın ne yapıyor?~Kumda bir spiral çiziyor.
4789~resmi bir belgeyi mühürlemek|bir belge imzalamak|açık bir klasör uzatmak~harita;iş kadını;klasör;masa~Yeşilli kadın ne yapıyor?~Resmi bir belgeyi mühürlüyor.
4792~olduğu yerde dönmek|sevinçle el çırpmak|bir çay fincanını iki eliyle tutmak~kız;fide;bahçe küreği;toprak~Kız ne dikiyor?~Toprağa bir fide dikiyor.
4793~çocuklara el işareti yapmak|ahşap iskelede çırpınmak|parkın üzerinde dalgalanmak~sakal;kuş evi;tornavida;tezgah~Tezgahın üzerinde ne var?~Tezgahın üzerinde ahşap bir kuş evi var.
4794~sıcak bir tepsi tutmak|resimli bir kitap okumak|onun omzunda uyumak~ağaç;büyükanne;demlik;kurabiyeler~Büyükanne ne okuyor?~Resimli bir kitap okuyor.
4795~kurabiye pişirmek|bir kitap okumak|onun omzunda uyumak~gözlük;kız;yün;koltuk~Büyükanne ne pişirmiş?~Kurabiye pişirmiş.
4796~çakıllı bir yolda koşmak|iskambil kağıtlarını dengede tutmak|çocuğu havaya kaldırmak~kasket;çalı çit;iskambil kağıdı;piknik masası~Çocuk neyi dengede tutuyor?~İskambil kağıtlarını dengede tutuyor.
4797~spagettinin üzerine peynir koymak|kameraya gülümsemek|peynirin altında kaybolmak~gökyüzü;garson;bardak;peynir~Garson ne yapıyor?~Spagettinin üzerine peynir koyuyor.
4798~tapınağa doğru yürümek|sokakta koşmak|hasır bir şapka tutmak~gökyüzü;tapınak;elbise;taşlar~Kadın nereye yürüyor?~Tapınağa doğru yürüyor.
4800~papyonunu düzeltmek|damadın omzunun üzerinden bakmak|bahçeye adım atmak~damat;çalı çit;davetli;gül~Damat neyi düzeltiyor?~Papyonunu düzeltiyor.
4801~bitkileri sulamak|yukarı bakıp gülümsemek|çok uzun boylu olmak~ayçiçeği;gökyüzü;kadın;domatesler~Kadın neye bakıyor?~Uzun bir ayçiçeğine bakıyor.
4802~kapıyı açmak|kollarını kavuşturmak|beyaz bir tişört giymek~güvenlik görevlisi;kız;zemin~Güvenlik görevlisi neyi açıyor?~Kapıyı açıyor.
4803~buketi vermek|misafirini karşılamak|şarapla gelmek~buket;şarap şişesi;atkı;ev bitkisi~Kadın ne taşıyor?~Bir çiçek buketi taşıyor.
4804~bir tur grubuna rehberlik etmek|turistlere devam etmelerini işaret etmek|ahşap bir araba çekmek~gökyüzü;saksı;kalabalık;cüppe~Genç adam ne yapıyor?~Bir tur grubuna rehberlik ediyor.
4805~bir kitap okumak|merdivenlerde oturmak|şehre bakmak~kilise;çeşme;gözlük;kitap~Adam ne yapıyor?~Bir kitap okuyor.
4806~sayfaları karıştırmak|kitabı sıkıca tutmak|manzaraya hayranlıkla bakmak~kubbe;çatılar;korkuluk~Adam ne yapıyor?~Çatıların üzerindeki manzaraya hayranlıkla bakıyor.
4807~portakal suyu içmek|büyük bir sürahiyi kaldırmak|ağzını silmek~gökyüzü;turuncu üst;sürahi;bardaklar~Adam ne içiyor?~Portakal suyu içiyor.
4808~uzun saçları taramak|kalın bir örgü örmek|uzun saçlarını savurmak~pencere;şampuan şişeleri;örgü;kuaför koltuğu~Kuaför ne yapıyor?~Kalın bir örgü örüyor.
4810~bir çivi çakmak|alnını silmek|tel çiti tutmak~uzun direk;ağaçlar;çekiç;çukur~Adam ne yapıyor?~Yere bir direk çakıyor.
4811~parlak turuncu bir atlet giymek|pembe bir spor üstü giymek|sahanın bir ucundan diğerine uzanmak~voleybol filesi;deniz;eller;kum~Oyuncular ne yapıyor?~Ellerini ortada üst üste koyuyorlar.
4812~bir gömleği düzgünce asmak|en üst düğmeyi iliklemek|sürgülü bir kapıyı açmak~raf;askılar;turuncu gömlek;örgü yelek~Adam ne yapıyor?~Gömleği bir askıya geçiriyor.
4813~paslı bir iskele babasına yaslanmak|limanın üzerinde süzülmek|bir konteyner gemisini yüklemek~vinçler;konteyner gemisi;römorkör;iskele babası~Genç adam neye yaslanıyor?~Paslı bir iskele babasına yaslanıyor.
4814~kırmızı biber toplamak|büyük bir patatesi havaya kaldırmak|büyük bir domates koparmak~kadın;sepet;patatesler;el arabası~Kadın ne yapıyor?~Kırmızı biber topluyor.
4815~şakaklarını ovmak|yüzünü buruşturmak|başını yaslamak~tavan lambaları;at kuyruğu;klavye;karton bardak~Kadın ne yapıyor?~Şakaklarını ovuyor.
4816~göğsüne dokunmak|ona saatini göstermek|yeşil bir tişört giymek~kadın;adam;saat;gökyüzü~Kadın ne yapıyor?~Göğsüne dokunuyor.
4818~önden gitmek|siyah tayt giymek|en arkadan gelmek~işaret parmağı;çorap;stiletto topuk;tahta zemin~Üç kişi ne yapıyor?~Stiletto topuklarla yürümeye çalışıyorlar.
4820~arkadaşına bağırmak|hem ağlamak hem gülmek|arkadaşına gülümsemek~saç;elbise;bilezik;pembe ışık~İki kadın ne yapıyor?~Birbirlerine sarılıyorlar.
4821~arabaya yaklaşmak|pencereye doğru eğilmek|ufkun üzerinde parlamak~güneş;pizza kutusu;yazlık elbise;asfalt~Yalınayak kadın ne yapıyor?~Arabaya pizza teslim ediyor.
4822~bir mesaj yazmak|telefonuna gülümsemek|battaniyenin altına saklanmak~tablo;kadın;telefon;yatak~Kadın ne yazıyor?~Bir mesaj yazıyor.
4825~tezgahı silmek|kirli kaseleri üst üste koymak|kirli ocağa sprey sıkmak~raflar;musluk;lavabo;tahta zemin~Kadın neyi siliyor?~Kirli tezgahı siliyor.
4826~barajın üzerinden dökülmek|vadiye düşmek|tepeleri kaplamak~gökyüzü;ağaçlar;baraj;su~Su ne yapıyor?~Su barajın üzerinden dökülüyor.
4828~duvarı yeşile boyamak|uzun bir rulo tutmak|yeşil bir tişört giymek~duvar;adam;rulo~Adam ne yapıyor?~Duvarı yeşile boyuyor.
4829~metal bir kazıyıcıyı sıkıca tutmak|bıçağı tahtaya bastırmak|çatlamış boyanın altına kaymak~boya;tahta;kazıyıcı;el~El ne yapıyor?~Bir kazıyıcıyla eski boyayı kazıyor.
4830~suda dönmek|yukarıdaki ışığa bakmak|yüzeye ilk ulaşmak~maske;su;paletler;halat~Alttaki adam ne yapıyor?~Yüzeye doğru yüzüyor.
4831~alüminyum bir sopa savurmak|sırıtmaya başlamak|vuruş sehpasında dengede durmak~kasket;çit;top;vuruş sehpası~Genç adam ne yapıyor?~Topu çimlerin üzerinden yükseğe gönderiyor.
4832~dar bir sırt boyunca yürümek|iki trekking batonunu sıkıca tutmak|ayak izlerini takip etmek~gökyüzü;zirve;bulutlar;sırt~Dağcı ne yapıyor?~Dar bir sırt boyunca yürüyor.
4833~kaykay sürmek|siyah bir kask takmak|yola dokunmak~tepe;deniz;yol;kask~Kaykaycı nerede kaykay sürüyor?~Sahil boyunca kaykay sürüyor.
4834~gri bir tişört giymek|beyaz bir tişört giymek|masanın üzerinde durmak~tişört;oyuncak;kase;masa~Çocuklar neyi izliyor?~Kasedeki oyuncakları izliyorlar.
4835~sokak boyunca koşmak|beyaz bir tişört giymek|şort giymek~bina;sokak lambası;araba;dükkan~Adam ne yapıyor?~Bir şehir sokağında koşuyor.
4836~ağaç kabuğunu testereyle kesmek|bir motorlu testereyi sıkıca tutmak|ağaç gövdesinden ortaya çıkmak~ayı;motorlu testere;talaş;ağaç kabuğu~Adam ne yapıyor?~Motorlu testereyle bir ayı oyuyor.
4837~biraz pizza uzatmak|masanın başında ayakta durmak|saat takmak~salata;pizza;tavuk;masa~Arkadaşlar ne yapıyor?~Büyük bir masada yemek yiyorlar.
4838~bir karpuz atmak|bir plaj topunu havaya kaldırmak|kuma düşmek~gökyüzü;deniz;plaj topu;kum~Kadın ne yapıyor?~Bir karpuz atıyor.
4839~küçük bir arabayı itmek|büyük bir kutuyu taşımak|salıncakta oturmak~ev;ağaç;araba;yol~Genç adam ne yapıyor?~Küçük bir arabayı itiyor.
4840~bir perdenin arkasına saklanmak|bir masanın altında oturmak|bir ağacın arkasına saklanmak~pencere;kapı;adam;kutu~Çocuk ne yapıyor?~Bir ağacın arkasına saklanıyor.
4841~bir anahtar aramak|bir sepeti boşaltmak|bir anahtarı havaya kaldırmak~anahtar;kapı;kadın~Kadın ne arıyor?~Bir anahtar arıyor.
4842~bir musluğu tamir etmek|matkap kullanmak|eski bir arabayı tamir etmek~gökyüzü;ev;çocuk;araba~Çocuk ne yapıyor?~Eski bir arabayı tamir ediyor.
4843~bir kuş evi yapmak|bir çadır kurmak|ahşap bir duvarı kaldırmak~gökyüzü;yapı;insanlar;çimen~İnsanlar neyi itiyor?~Ahşap bir duvarı itiyorlar.
4844~bir karpuz kesmek|balta kullanmak|büyük bir balkabağı kesmek~gökyüzü;kadın;çimen;çekirdekler~Kot pantolonlu kadın ne yapıyor?~Büyük bir balkabağını ikiye kesiyor.
4845~düğme dikmek|beyaz kumaşı tutmak|büyük bir battaniyeyi kaldırmak~dikiş makinesi;el;kumaş~Kadınlar neyi kaldırıyor?~Büyük bir battaniyeyi kaldırıyorlar.
4846~bir pantolonu ütülemek|ipek bir elbiseyi buharla ütülemek|bir yığın peçeteyi ütülemek~başucu lambası;çerçeveli resim;ütü;pantolon~Adam ne yapıyor?~Bir pantolonu ütülüyor.
4847~zeminde oturmak|rafların arasını temizlemek|kirli suyu temizlemek~lambalar;kapı;kadın;zemin~Kadın nerede oturuyor?~Zeminde oturuyor.
4848~toprağı bastırmak|çiçeklere su dökmek|büyük bir balkabağı taşımak~gökyüzü;kadın;balkabağı;yapraklar~Kadın ne tutuyor?~Büyük bir balkabağı tutuyor.
4849~bir sulama kabı tutmak|çiçeklere uzanmak|çocuklarla koşmak~ağaçlar;çeşme;gökkuşağı;çimen~Adam ne yapıyor?~Adam çocuklarla koşuyor.
4850~çimenlerin üzerinde durmak|bisiklete binmek|başparmağını kaldırmak~şapka;fotoğraf makinesi;gömlek~Genç adam ne tutuyor?~Büyük bir fotoğraf makinesi tutuyor.
4851~kumu fırçayla temizlemek|çok şaşırmış görünmek|uzun bir sakalı olmak~gökyüzü;heykel;kum~Kadın neye bakıyor?~Antik bir heykele bakıyor.
4853~küçücük bir dişliye gözlerini kısarak bakmak|dev dişlilere başını kaldırıp bakmak|camın arkasındaki dişlileri göstermek~duvar saatleri;şömine saati;pirinç kutu;tezgah~Kadın neyi inceliyor?~Küçücük pirinç bir dişliyi inceliyor.
4854~kara tahtaya yazmak|hesap makinesi kullanmak|öğrencilere dönük durmak~kara tahta;gözlük;öğrenciler;hesap makinesi~Adam ne yapıyor?~Kara tahtaya yazıyor.
4855~bir kart okumak|başına dokunmak|bir kartı düşürmek~gözlük;kulaklık;kitaplar;kartlar~Adam ne yapıyor?~Bir kart okuyor.
4856~kırmızı bir kalem tutmak|bir sınav kağıdını düzeltmek|saçına dokunmak~öğretmen;kağıtlar;masa~Öğretmen ne yapıyor?~Bir sınav kağıdını düzeltiyor.
4857~bir tarayıcı tutmak|bir kutuyu taramak|yüzünü silmek~raflar;tarayıcı;işçi;kutular~İşçi ne yapıyor?~Bir kutuyu tarıyor.
4859~büyük bir yapboz yapmak|büyük bir gözlük takmak|kollarını kaldırmak~pencere;kitaplar;gözlük;parçalar~Kadın ne yapıyor?~Büyük bir yapboz yapıyor.
4860~inanamayarak bakakalmak|dibe batmak|bir bulut halinde çözünmek~kabarcıklar;tablet;kaşık;tezgah~Kadın ne yapıyor?~Köpüren suya inanamayarak bakıyor.
4861~bir mikrofonu havaya kaldırmak|ormanda şarkı söylemek|kayalardan dökülmek~ağaçlar;şelale;kulaklık;yelek~Kadın ne tutuyor?~Uzun bir mikrofon tutuyor.
4862~iki elma tutmak|renkli bir başörtüsü takmak|kollarını kaldırmak~başörtüsü;domatesler;çanta;masa~Kadın ne yapıyor?~İki elma arasında seçim yapıyor.
"""
src = json.load(open(f'{HERE}/source.json'))
rows = {}
for line in T.strip().splitlines():
    i, p, n, q, a = line.split('~')
    rows[i] = {'phrases': p.split('|'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{HERE}/tr.json', 'w'), ensure_ascii=False, indent=1)
