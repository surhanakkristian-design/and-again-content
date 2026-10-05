import json, os
H = os.path.dirname(os.path.abspath(__file__))
T = r"""
4611|bir resim göstermek;iki adamla dans etmek;kızına sarılmak|kız;anne;resim;kâse|Kız annesine ne gösteriyor?|Annesine bir resim gösteriyor.
4612|şeftali satmak;bir kutuyu doldurmak;meyvenin parasını ödemek|şeftaliler;kutu;adam|Yaşça büyük olan adam ne satıyor?|Bir kutu şeftali satıyor.
4613|siyah bir kova tutmak;toprağı kazmak;bahçede çalışmak|gökyüzü;kova;adam;toprak|Adam ne yapıyor?|Bahçede toprağı kazıyor.
4614|ayaklı bir merdivenin üstünde durmak;turuncu bir balonu şişirmek;tavandan sarkmak|süs şeritleri;kot ceket;ayaklı merdiven;balonlar|Tavandan ne sarkıyor?|Tavandan kâğıt süs şeritleri sarkıyor.
4615|bir balon şişirmek;kâğıttan bir zincir asmak;yerde durmak|merdiven;kanepe;balonlar;ışıklar|Yerde ne var?|Yerde rengârenk balonlar var.
4617|mavi bir kalkanı sıkıca kavramak;rüzgârda dalgalanmak;çimenlerin üzerinde hareketsiz yatmak|seyirciler;miğfer;kalkan;zırh|Adamlar ne yapıyor?|Adamlar seyircilerin önünde dövüşüyor.
4618|bir kalkanın arkasında sırıtmak;tribünü doldurmak;bir kılıcı zaferle havaya kaldırmak|kılıç;seyirciler;kalkan;sakal|Kel adam ne yapıyor?|Mavi bir kalkanın arkasında çömeliyor.
4619|çiğ bir tavuğu yıkamak;elinde büyük bir balık tutmak;lavabonun başında durmak|pencere;kazak;balık;lavabo|Adam ne yapıyor?|Çiğ bir tavuğu yıkıyor.
4621|başını kaldırıp ekranlara bakmak;yerde uyumak;ağzını kapatmak|battaniye;bavul;gökyüzü;yer|Kadın neye bakıyor?|Başını kaldırıp ekranlara bakıyor.
4622|tavana bakıp iç çekmek;saatine göz atmak;apronda durmak|bavul;uçak;boyun yastığı;çıplak ayaklar|Kadın neye göz atıyor?|Saatine göz atıyor.
4625|bastona dayanmak;mavi bir hastane forması giymek;havaya yumruk sallamak|oy sandığı;yağmurluk;rozet;pencereler|Sarılı kadın ne yapıyor?|Oy verdikten sonra havaya yumruk sallıyor.
4627|el sallayarak veda etmek;istasyondan ayrılmak;denizde yol almak|gemi;deniz;gökyüzü;adam|Gemi ne yapıyor?|Gemi limandan ayrılıyor.
4628|bir battaniyeye sarılmak;pencerenin yanında oturmak;çok üzgün görünmek|pencere;adam;battaniye;koltuk|Üzgün adam ne yapıyor?|Pencerenin yanında oturuyor.
4630|bir kurşun kalem tutmak;bir adamın saçını kesmek;yeni bir saç kesimi yaptırmak|saç kesimi;kulak;şişeler;el|Genç adam ne yaptırıyor?|Yeni bir saç kesimi yaptırıyor.
4631|bir kuş evi tasarlamak;tahta parçalarını birleştirmek;eskizini kaldırıp göstermek|saksı bitkisi;kuş evi;eskiz;önlük|Adam ne tasarladı?|Ahşap bir kuş evi tasarladı.
4632|çalışma alanını düzenlemek;masayı aydınlatmak;bir belgeyi göstermek|masa lambası;saksı bitkisi;dizüstü bilgisayar;kitap yığını|Kadın neyi düzenliyor?|Çalışma alanını düzenliyor.
4633|araba aküsüyle uğraşmak;kaldırıma çökmek;yolda kalmış sürücünün yanından geçmek|otobüs;yağmurluk;akü;far|Adam ne yapıyor?|Çaresiz adam araba aküsüyle uğraşıyor.
4635|gideceği yeri daire içine almak;denizi dalgın dalgın seyretmek;küçük binaların üzerinde yükselmek|gökyüzü;deniz feneri;uçurum;sırt çantası|Kız neyi daire içine alıyor?|Gideceği yeri daire içine alıyor.
4636|kollarını iki yana açmak;kulübenin üzerinde yükselmek;denizin üzerinde batmak|deniz feneri;güneş;deniz;kot ceket|Kız neyi hayranlıkla izliyor?|Gün batımında bir deniz fenerini hayranlıkla izliyor.
4637|bir telefonu havaya kaldırmak;büyük bir evi yıkmak;yere yıkılmak|gökyüzü;kask;telefon;tuğlalar|Sarı makine ne yapıyor?|Büyük bir evi yıkıyor.
4638|tuğla bir evi yıkmak;çöküp enkaza dönmek;yıkıntıları işaret etmek|enkaz;ekskavatör;baret;bariyer|Eve ne oluyor?|Çöküp enkaza dönüyor.
4640|deterjanı ölçmek;bir lekeye bakıp kaşlarını çatmak;çekmeceyi itip kapatmak|şişe;ölçü kabı;deterjan;çekmece|Adam ne yapıyor?|Çekmeceye deterjan döküyor.
4641|parmağıyla göstermek;yiyecekleri kutulara koymak;yüksek bir kule yapmak|donutlar;çilekler;pencere;tişört|Adam ne yapıyor?|Yiyecekleri kutulara koyuyor.
4642|kumu kürekle dışarı atmak;dilini dışarı çıkarmak;havaya kum atmak|çukur;kürek;tümsek;gökyüzü|Genç adam ne kazıyor?|Derin bir çukur kazıyor.
4643|havaya yumruk sallamak;vizörden bakmak;oyuncuların üzerinde asılı durmak|pencere;mikrofonlar;monitör;tripod|Kulaklıklı kadın ne yapıyor?|Bir film çekimini yönetiyor.
4644|bir telefon tutmak;masada yemek yemek;masada yanmak|adam;kapı;mum;masa|Aşçı ne yapıyor?|Masada yemek yiyor.
4645|iki parçayı birleştirmek;yüksek bir kule kurmak;deliklerle dolu olmak|halka;çubuk;tepsi|Eller ne yapıyor?|Eller yüksek bir kule kuruyor.
4647|bir ofis sandalyesinde dönmek;alnını tutmak;bir iş arkadaşının sendelemesini izlemek|kapı;beyaz tahta;masa;kot ceket|Adam ne yapıyor?|Bir ofis sandalyesinde dönüyor.
4650|mavi bir sıvı dökmek;tezgâhın üzerine taşmak;tavana doğru yükselmek|koruyucu gözlük;laboratuvar önlüğü;köpük;deney şişeleri|Köpük ne yapıyor?|Köpük tezgâhın üzerine taşıyor.
4652|zorlanarak bağırmak;dirseğe yastık olmak;plastik bir kapağı olmak|kalabalık;çiçek;bariyer;yastık|Masada ne oluyor?|İki kişi bilek güreşinde yarışıyor.
4653|paspasın üzerinde ayaklarını yere vurmak;koridora adım atmak;ardına kadar açık durmak|su geçirmez pantolon;lastik çizmeler;çamur;paspas|Adam ne yapıyor?|Ayaklarını yere vurarak çizmelerindeki çamuru çıkarıyor.
4654|kollarını kavuşturmak;kadının arkasında durmak;rafta kalmak|fincan;raf;kadın;bitki|Kadın ne yapıyor?|Fincanı rafa koyuyor.
4655|bir tişörtü çıkarmak;bir gömlek giymek;koyu renk bir takım elbise giymek|saç;kravat;ceket;tablolar|Adam ne yapıyor?|Koyu renk bir takım elbise giyiyor.
4656|tuğla duvarı delmek;bir dübel çakmak;ahşap bir raf monte etmek|tuğla duvar;raf;kitaplar;alet kemeri|Kadın ne yapıyor?|Tuğla bir duvara ahşap raflar monte ediyor.
4657|pipetle içmek;yeşil bir hindistancevizi tutmak;bir su şişesini açmak|saç;insanlar;pipet;hindistancevizi|Kadın ne yapıyor?|Pipetle içiyor.
4659|şehir içinde araba kullanmak;beyaz bir kamyonet kullanmak;ormanın içinden araba kullanmak|gökyüzü;deniz;kadın;araba|Beyaz kamyoneti kim kullanıyor?|Beyaz kamyoneti bir kadın kullanıyor.
4660|çok sayıda kutu taşımak;kutuları düşürmek;yerde yuvarlanmak|kadın;yer;şapka;yığın|Kadın ne taşıyor?|Bir yığın kutu taşıyor.
4661|savrulan yaprakları yakalamak;başını ovmak;sarı yapraklarını dökmek|gövde;sakal;ceket;yapraklar|Adam ne yapıyor?|Bir ağacın altında savrulan yaprakları yakalıyor.
4662|ahşap sandıklar atmak;gökyüzüne dalıp bakmak;çadırların yakınında otlamak|kayışlar;sandık;çadırlar;cüppe|Uçak ne yapıyor?|Paraşütle ahşap sandıklar atıyor.
4664|bir doz ölçmek;bir bardaktan yudumlamak;beyaz bir etiketi olmak|damlalık;kazak;bardak;şişe|Kadın ne yapıyor?|Bir doz yağ ölçüyor.
4665|bir dondurma tutmak;bir torba meyve tutmak;parçalara ayrılmak|torba;meyve;teneke kutu;yer|Karpuza ne oluyor?|Karpuz parçalara ayrılıyor.
4666|kenardan aşağı eğilmek;kocaman bir balkabağını itmek;bir toz bulutu kaldırmak|balkabağı;gökyüzü;gökdelenler;çıkıntı|Genç adam ne yapıyor?|Betonun üzerinde bir balkabağını parçalıyor.
4667|çadırların üzerinden uçmak;ahşap bir sandık atmak;kollarını iki yana açmak|uçak;çadır;atlar;kadın|Uçak ne yapıyor?|Gökyüzünden sandıklar atıyor.
4668|çamaşırları asmak;beyaz bir gömleği düzeltmek;temiz çamaşırları koklamak|gömlek;çamaşır ipi;önlük;kiremitler|Kadın ne yapıyor?|Yeni yıkanmış bir gömleği kokluyor.
4669|bir gömleği mandallamak;temiz çamaşırları sımsıkı tutmak;esintide dalgalanmak|mandal;çamaşır;önlük;karolar|Kadın ne yapıyor?|Çamaşırları ipe mandallıyor.
4670|bir gömlek asmak;beyaz bir çarşafa dokunmak;çatıda yürümek|gökyüzü;kilise;çatı;giysiler|Kadın ne yapıyor?|Çatıda giysileri asıyor.
4671|kapağı kapatmak;büyük bir battaniyeye sarılmak;çamaşır makinesinde dönmek|havlular;adam;çamaşır makinesi;battaniye|Adam ne yapıyor?|Çamaşır makinesinden bir battaniye çıkarıyor.
4674|altın bir saati temizlemek;yüksek bir rafa uzanmak;elini sallamak|pencere;raf;adam;koltuk|Adam ne yapıyor?|Rafları temizliyor.
4676|birlikte peynir taşımak;peyniri başının üzerine kaldırmak;şapkasını fırlatmak|şapka;peynir;bayrak|Adam ne kaldırıyor?|Peyniri başının üzerine kaldırıyor.
4678|uzun erişte yemek;çatalla yemek;iki eliyle yemek|saç;erişte;yumurta;kâse|Kadın ne yiyor?|Bir kâseden erişte yiyor.
4679|lezzetli bir tako yemek;gözlerini kapatmak;parmaklarını yalamak|şapka;tişört;takolar|Genç adam ne yiyor?|Lezzetli bir tako yiyor.
4681|deveye binmek;mavi bir lambaya dokunmak;kollarını iki yana açmak|lamba;el;eşarp;gömlek|Kadın neye dokunuyor?|Büyük mavi bir lambaya dokunuyor.
4683|büyük bir kâseyi doldurmak;kırmızı sos dökmek;bir zil çalmak|pirinç;şapka;aşçı|Aşçı ne yapıyor?|Büyük bir kâseyi yemekle dolduruyor.
4684|hardal rengi bir bere takmak;sarı at kuyruğu saçı olmak;iş arkadaşını işaret etmek|bere;dirsek;dizüstü bilgisayar;fare|İş arkadaşları birbirini nasıl selamlıyor?|Birbirleriyle dirsek tokuşturuyorlar.
4686|ışıkları onarmak;birkaç kablo tutmak;küçük bir fener tutmak|baret;adam;erkek çocuk;aletler|Aletli kadın ne yapıyor?|Işıkları onarıyor.
4688|yüzeyin altında süzülmek;denizden çıkmak;beyaz halatı kavramak|gökyüzü;balina;yağmurluk;köpük|Balina ne yapıyor?|Devasa balina denizden çıkıyor.
4689|balinaya bakmak;sarı bir mont giymek;sudan çıkmak|balina;dağlar;tekne;adam|Teknenin yanında ne var?|Teknenin yanında bir balina var.
4691|bir dokunmatik ekrana dokunmak;masasına yerleşmek;yumruklarını sıkmak|iş arkadaşı;sırt çantası;ofis sandalyesi|Genç adam kimi selamlıyor?|Bir iş arkadaşını selamlıyor.
4692|büyük bir koli taşımak;rafa teneke kutular koymak;bir kolinin üzerine basmak|koli;teneke kutular;kapı;adam|Adam ne yapıyor?|Rafa teneke kutular koyuyor.
4694|bir sözleşme imzalamak;omzuna hafifçe vurmak;kollarını iki yana açmak|sözleşme;kahve makinesi;dizüstü bilgisayar;blazer ceket|Genç adam ne imzalıyor?|Bir sözleşme imzalıyor.
4695|bir çekmeceyi boşaltmak;ıvır zıvırla dolmak;yere saçılmak|şapka;dolap;kanepe;oyuncaklar|Adam neyi boşaltıyor?|Oyuncaklarla dolu bir dolabı boşaltıyor.
4696|kırmızı bir tutamağı kavramak;sarkık bir duvara tırmanmak;tırmanıcıyı cesaretlendirmek|gözlük;magnezyum tozu;seyirciler;tırmanma duvarı|Seyirciler ne yapıyor?|Yaşlı kadını cesaretlendiriyorlar.
4698|başını tutmak;açık kalmak;güneşte parıldamak|raflar;far;tulum;motor|Adam ne üzerinde çalışıyor?|Bir scooter motoru üzerinde çalışıyor.
4700|bir vidayı sıkmak;bir kupadan yudumlamak;bir kupayı uzatmak|robot;dizüstü bilgisayar;kupa;kablolar|Robot ne yapıyor?|Bir kupayı uzatıyor.
4701|suya yıkılmak;kumdan kaleye bakmak;koyu renk bir şapka takmak|şapka;kumdan kale;deniz;gökyüzü|Kumdan kaleye ne oluyor?|Suya yıkılıyor.
4702|kapının arasından sıkışarak geçmek;çuvalların üzerine eğilmek;toprak yolda hızla koşmak|hasır şapka;çit;keçi;çuval|Keçi ne yapıyor?|Toprak bir yolda kaçıyor.
4703|yeşil bir bayrak çekmek;rüzgârda dalgalanmak;kurdeleyi kesmek|bayrak direği;merdiven;kurdele;basamaklar|Mavili adam ne çekiyor?|Yeşil bir bayrak çekiyor.
4704|sıcak tutan bir şapka takmak;ıslanmak;biraz su dökmek|şapka;pencere;havlu;taşlar|Adam ne yapıyor?|Taşların üzerine su döküyor.
4705|bir çeşmenin yanında sahne almak;bir tepsi içeceği dengede tutmak;polis üniforması giymek|müzik grubu;çeşme;sırt çantası;bebek arabası|Müzik grubu ne yapıyor?|Müzik grubu bir çeşmenin yanında sahne alıyor.
4706|çizgili bir atkı takmak;kollarını iki yana açmak;balkondan izlemek|kale;saha;seyirciler|Öndeki adam ne yapıyor?|Kollarını iki yana açmış bağırıyor.
4707|ağzının içine bakmak;ağzını kocaman açmak;sırada beklemek|hemşire;hasta;tabela;çadır|Hemşire ne yapıyor?|Hastanın ağzının içine bakıyor.
4709|bir bileti havaya kaldırmak;mavi denizi geçmek;kayalardan dökülmek|grup;şelale;ağaçlar;gökyüzü|Grup ne yapıyor?|Grup bir şelalenin yanında eğleniyor.
4711|küçük bir tekneyle kürek çekmek;büyük bir çaba göstermek;ağzını kocaman açmak|gökyüzü;insanlar;su;tekne|Adam ne yapıyor?|Küçük bir tekneyle kürek çekiyor.
4712|bir pencereye üflemek;bir pastanın üzerine eğilmek;beyaz bir standın üzerinde durmak|kadın;tişört;mumlar;pasta|Mavili adam ne yapıyor?|Mumları üflüyor.
4713|bir kayığa binmek;bir bavulun üzerine eğilmek;onu el sallayarak uğurlamak|köylüler;halat;rıhtım;kayık|Köylüler ne yapıyor?|Rıhtımdan el sallayarak veda ediyorlar.
4714|bir vazo tutmak;beyaz eldiven takmak;iki kişiyle konuşmak|insanlar;papyon;vazo;masa|Uzman ne tutuyor?|Uzman bir vazo tutuyor.
4715|bir şapka takmak;mavi bir gömlek giymek;küçük parçalara ayrılmak|karpuz;masa;adam;kadın|Karpuza ne oluyor?|Karpuz küçük parçalara ayrılıyor.
4716|cangılı keşfetmek;büyük bir bıçak tutmak;suya dökülmek|şelale;adam;kayalar|Adam ne yapıyor?|Cangılı keşfediyor.
4717|karanlıkta yürümek;kollarını iki yana açmak;suya dökülmek|şelale;adam;kaya|Adam ne yapıyor?|Karanlıkta yürüyor.
4718|kameraya gülümsemek;parmağıyla göstermek;gözünü açık tutmak|göz;kadın;gözlük|Kadın neyi gösteriyor?|Büyük bir gözü gösteriyor.
4720|yana bakmak;dilini çıkarmak;gözlerini kocaman açmak|gözlük;pencere;sandalye|Üç genç ne yapıyor?|Komik suratlar yapıyorlar.
4722|kanepede uzanmak;turuncu bir elbise giymek;mavi bir elbise giymek|çiçekler;ışıklar;güneş gözlüğü;çimen|Yelpazeli adam nerede?|Kanepede uzanıyor.
4723|sırtüstü düşmek;turuncu bir şort giymek;sırtüstü yatmak|saç bandı;şort;küpler|İnsanlar nereye düşüyor?|Küplerin içine düşüyorlar.
4724|gözlerini kapatmak;renkli bir pantolon giymek;baş aşağı dalmak|saat;pantolon;küpler|Kadınlar ne yapıyor?|Küplerin içinde gülüyorlar.
4725|hamuru havada tutmak;çocuğun üzerine un serpmek;yüzünde un olmak|kadın;pizza;fırın;masa|Kadın ne taşıyor?|Bir pizza taşıyor.
4726|havuç sökmek;ahşap bir kasa taşımak;büyük bir tekerleği olmak|çiftçi;havuçlar;ayçiçekleri;tekerlek|Çiftçi ne taşıyor?|Bir kasa havuç taşıyor.
4727|bebeği havaya kaldırmak;mavi bir bisiklete binmek;omuzlarında oturmak|baba;top;erkek çocuk;çimen|Babanın omuzlarında kim oturuyor?|Bebek onun omuzlarında oturuyor.
4728|ağzını kocaman açmak;ceketini çıkarmak;kanepede uyumak|duvar;kadın;telefon;kanepe|Kadın nerede uyuyor?|Kanepede uyuyor.
4729|arkadaşının koluna tutunmak;yeşil bir kapüşonlu giymek;kadınların arkasında durmak|gökyüzü;perde;kapüşonlu;ceket|İki kadın kendini nasıl hissediyor?|İskeletten korkuyorlar.
4731|bir ipi çekmek;ortada dalgalanmak;büyük bayrağı izlemek|gökyüzü;bina;bayraklar;insanlar|Grili kadınlar ne yapıyor?|İpleri çekiyorlar.
4732|ahşap bir çit yapmak;sarı bir çekiç kullanmak;çitin üzerinden bakmak|gökyüzü;ağaç;çit;çimen|Adam ne yapıyor?|Ahşap bir çit yapıyor.
4734|bir battaniyenin altında yatmak;onunla ilgilenmek;odayı aydınlatmak|lamba;yastık;battaniye|Yaşlı kadın ne yapıyor?|Genç kadınla ilgileniyor.
4735|alnını silmek;onu arkadan yakalamak;her yumruğu emmek|kalkan;eldiven;örgü;çamur|Kadın ne yapıyor?|Bir kalkana yumruk atıyor.
4736|dolgulu bir kalkana yumruk atmak;darbeleri emmek;minderlerin üzerine düşmek|kalkan;eldiven;minderler;gökyüzü|Öndeki kadın ne yapıyor?|Dolgulu bir kalkana yumruk atıyor.
4737|bir şişme havuzu doldurmak;sudan taşmak;yavaşça damlamak|kova;musluk;palmiye|Kadın ne yapıyor?|Bir kovaya su döküyor.
4738|yatağın altına bakmak;botlarını havaya kaldırmak;pasaportunu bulmak|pasaport;yatak;perde;giysiler|Giysiler nerede?|Giysiler her yerde.
4739|eski eşyaları karıştırmak;ahşap bir kutuyu açmak;ellerinde parıldamak|kadın;elmas;fotoğraf makinesi;kitap|Kadın ne yapıyor?|Bir kutudan bir elmas çıkarıyor.
4741|oltayı sertçe çekmek;bir kasa balığı kaldırmak;denizin üzerinde uçmak|gökyüzü;deniz;balık;kasa|Adam ne yapıyor?|Denizden bir balık çekiyor.
4742|iki ağır halatı sallamak;bir kutunun üzerine zıplamak;ellerini çırpmak|gökyüzü;kadın;adam;kutu|Kırmızılı kadın ne yapıyor?|Büyük bir kutunun üzerine zıplıyor.
4743|kameraya sırıtmak;büyük bir sevinçle alkışlamak;meyve suyuyla dolmak|kanat;bardak;bulutlar;servis arabası|Yolcu ne yapıyor?|Uçuş sırasında bir bardağı havaya kaldırıyor.
"""
src = json.load(open(f'{H}/source.json'))
out = {}
rows = {l.split('|')[0]: l.split('|') for l in T.strip().split('\n')}
for i in src:
    _, p, n, q, a = rows[i]
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
json.dump(out, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
