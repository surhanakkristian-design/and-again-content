import json,os
H=os.path.dirname(os.path.abspath(__file__))
src=json.load(open(os.path.join(H,'source.json')))
R=r'''
7323|yatağı toplamak;yatağın üstüne atlamak;fincandan içmek|pencere;adam;kedi;yatak|Kadın ne yapıyor?|Yatağı topluyor.
7324|şezlongda güneşlenmek;onu telefonuyla çekmek;karlı bir çıkıntıya tünemek|gökdelenler;güvercin;şezlong;şişme havuz|Yalınayak adam ne yapıyor?|Güneşin tadını sonuna kadar çıkarıyor.
7325|bir parça deniz odunu sallamak;anlatıcıya havlamak;kupadan yudumlamak|deniz odunu;battaniye;kamp ateşi;gitar|Ayakta duran kadın ne yapıyor?|Dramatik bir hikâye anlatıyor.
7327|seyyar arabadan atlamak;seyyar arabanın yanında durmak;geyiğe havlamak|gökyüzü;erkek;seyyar araba;elmalar|Erkek geyik ne yapıyor?|Seyyar arabadan atlıyor.
7328|kuyruğu havada koşmak;bastonla yürümek;pembe bir üstle koşmak|koyunlar;köpek;lamba;ağaçlar|Köpek ne yapıyor?|Köpek koyunların yanında koşuyor.
7329|bariyerin üzerinden eğilmek;kadına sırıtmak;çifti alkışlamak|görevli;panço;fotoğrafçı;projektörler|Kadın ne yapıyor?|Bariyerin üzerinden eğiliyor.
7332|ön tekerleği sabit tutmak;şarjlı matkap kullanmak;montaj hattında asılı durmak|cıvatalar;matkap;lastikler;sele|Kadın ne yapıyor?|Şarjlı matkap kullanıyor.
7334|kaykay tahtasını yakalamak;pürüzsüz tahtayı okşamak;tezgâhın altında uyuklamak|akçaağaç;kupa;köpek;talaş|Kadın ne yapıyor?|Akçaağaç tahtayı okşuyor.
7336|kürek çekerek marinayı geçmek;kahvaltı tepsisini dengede tutmak;korkuluktan eğilmek|yat;iskele;tepsi;kürek|Güneş gözlüklü adam ne yapıyor?|Kürek çekerek marinayı geçiyor.
7337|bir kuşu uçmaya bırakmak;çimenlerde diz çökmek;başının üstünde oturmak|kuş;ceket;kutu;çimen|Diz çökmüş kadın ne yapıyor?|Ellerinde bir kuş tutuyor.
7338|kanal boyunca kürek çekmek;tahtanın üstünde diz çökmek;uzakta otlamak|flamingolar;gözetleme kulesi;SUP tahtası;sazlar|Kadın ne yapıyor?|Bataklıkta kürek çekiyor.
7339|bir böcek taşımak;yuvaya konmak;başını içeri sokmak|pencere kırlangıcı;yuva;çatı;tarla|Pencere kırlangıcı ne yapıyor?|Yuvasına bir böcek taşıyor.
7340|korkuluktan eğilmek;römorkörü işaret etmek;siperli şapka takmak|vinç;siperli şapka;römorkör;termos|Kadın ne yapıyor?|Telsizle konuşuyor.
7342|membrana bastırmak;gözlerini kapalı tutmak;şoktan ağzını kapatmak|ahşap çerçeve;membran;adam;lambader|Kadın ne yapıyor?|Yüzünü membrana bastırıyor.
7344|zarf teslim etmek;kaldırımda pedal çevirmek;döner kapıdan girmek|kurye;sarı taksi;zarf;döner kapı|Kadın ne yapıyor?|Bir adama zarf teslim ediyor.
7345|kollarını iki yana açmak;kısa kayaklarla dengede durmak;bir kayakçıyı çekmek|ahşap kulübe;seyirciler;ip;at|İp nereye bağlı?|Belinin etrafına bağlı.
7347|ipte sallanmak;çağlayan suyun altında dönmek;arabaya koşulmuş halde durmak|un;değirmen;at;su çarkı|Kadın ne yapıyor?|Su çarkının üzerinde sallanıyor.
7348|kalın bir ipten aşağı kaymak;kepenk mandalını kavramak;çuvala un dökmek|dişli çark;pencere;değirmenci;değirmen taşları|Una bulanmış kadın ne yapıyor?|Kalın bir ipten aşağı kayıyor.
7349|bir sıra kadının önünde yürümek;bir dachshund taşımak;birkaç altın zincir takmak|villa;dachshund;milyoner;havlu|Milyoner ne yapıyor?|Bir sıra kadının önünde yürüyor.
7352|ıslak podyumda uzun adımlarla yürümek;reflektörlü ceket giymek;turuncu mini etek giymek|projektörler;uçak;mini etek;konuklar|Model ne yapıyor?|Islak podyumda uzun adımlarla yürüyor.
7359|hareket eden bir treni kovalamak;kayaklarını sıkıca tutmak;kapıdan dışarı sarkmak|lamba direği;ahşap kulübe;kondüktör;kayak batonu|Kadın ne yapıyor?|Hareket eden bir treni kovalıyor.
7362|sıçrayan kremayı yakalamak;dudaklarını yalamak;çikolatalı hamuru çırpmak|karıştırma kabı;beagle;mutfak zamanlayıcısı;yumurta sarısı|Beagle ne yapıyor?|Sıçrayan kremayı yakalıyor.
7363|telefonunu havaya kaldırmak;büyük bir kayanın üstünde durmak;sandviç yemek|cep telefonu;gökyüzü;sırt çantası;harita|Kadın ne yapıyor?|Telefonunu başının üzerinde tutuyor.
7364|merdivende durmak;merdiveni tutmak;havada dönmek|cam çatı;mobil heykel;alet çantası;merdiven|Mobil heykel ne yapıyor?|Havada dönüyor.
7365|arabadan kil kazımak;bir parça kile şekil vermek;arka planda fotoğraf çekmek|kil model;döner tabla;talaş;tavan lambaları|Kadın ne yapıyor?|Arabadan kil kazıyor.
7367|dudaklarını büzmek;kocaman yüzgecini göstermek;kanepede uyuklamak|moli balığı;akvaryum;akvaryum kökü;balık kepçesi|Kadın ne yapıyor?|Balık gibi dudaklarını büzüyor.
7368|yanağından öpmek;büyük çantasını yere atmak;üzerlerine atlamak|pencere;lamba;çanta;köpek|Kadın ne yapıyor?|Onu yanağından öpüyor.
7370|canını kurtarmak için kürek çekmek;zorlanarak yüzünü buruşturmak;denize çökmek|buzul;serpinti;kask;kano|Öndeki adam ne yapıyor?|Buzuldan uzağa kürek çekiyor.
7372|ağır bir bohçayı yukarı çekmek;fenerin yanında çömelmek;ipi aşağıdan sabit tutmak|maymun;uyku matı;karton kutu|Kadın ne yapıyor?|Ağır bir bohçayı verandaya çekiyor.
7373|dar bir kanal havuzuna sıkışarak girmek;rıhtım boyunca uzun adımlarla yürümek;dev gemiye el sallamak|kruvaziyer gemisi;seyirciler;korkuluk;taş kulübe|Kruvaziyer gemisi ne yapıyor?|Dar bir kanal havuzuna sıkışarak giriyor.
7376|siyah dalış kıyafetiyle yüzmek;uzun paletlerle ayak vurmak;su yüzeyinde durmak|tekne;yunus;dalgıç;balık sürüsü|Kadın ne yapıyor?|Bir balık sürüsünün içinden süzülerek geçiyor.
7377|döner merdivenden çıkmak;cekete uzanmak;aşçı ceketini uzatmak|aşçı ceketi;döner merdiven;büyük tencere|Genç adam ne yapıyor?|Döner merdivenden çıkıyor.
7378|boş gözlerle ileriye bakmak;bir paltoya hıçkırarak ağlamak;adamın kolunu kavramak|katil;yüksek pencere;su sürahisi;dosya|Arkasındaki kadın ne yapıyor?|Koyu renk bir paltoya hıçkırarak ağlıyor.
7379|kollarını iki yana açmak;iki kolunu havaya kaldırmak;metal bir kupayı sıkıca tutmak|anlatıcı;fenerler;sarılmış ip;tabaklar|Ayakta duran adam ne yapıyor?|Kollarını iki yana açıyor.
7381|kementi çekmek;sürüklenmek;ateş ışığıyla parlamak|ren geyiği;kanvas çadır;huş ağaçları;kement|Genç kadın ne yapıyor?|Bir ren geyiğini karda sürüklüyor.
7382|buzun üstünde diz çökmek;başını geriye atmak;göğe fışkırmak|alev;ahşap kulübe;gaz tüpü;donmuş baloncuklar|Kırmızılı kadın ne yapıyor?|Karanlık buzun üstünde diz çökmüş duruyor.
7383|bardağa uzanmak;kanepede uyumak;yerde yatmak|adam;şapka;tepsi;bardak|Kadın ne yapıyor?|Bir bardak suya uzanıyor.
7386|elini gözlerine siper etmek;arkadaşına doğru koşmak;kapıda nöbet tutmak|kodes;memur;naylon poşet|Gardiyan nerede duruyor?|Kodesin kapısında duruyor.
7387|madeni para numarası yapmak;gözlerini siper etmek;başını geriye atmak|asmalar;taş duvar;madeni para;şeftaliler|Kel adam ne yapıyor?|Kulağının arkasından madeni para çıkarıyor.
7389|balta sallamak;kancada asılı durmak;ahşabın üstünde durmak|baret;kanca;balta;meşe|Adam neyi kesiyor?|Ahşabı baltayla kesiyor.
7392|ahşap bir masayı yağlamak;masanın üstünde gezinmek;bir su birikintisinde durmak|teneke kutu;eldivenler;kedi;sandalye|Öndeki adam ne yapıyor?|Uzun ahşap bir masayı yağlıyor.
7393|zeytinyağı dökmek;yuvarlak bir somun tutmak;büyük bir testiyi havaya kaldırmak|testi;eşek;ekmek;zeytinler|Kadın ne yapıyor?|Ekmeğin üzerine zeytinyağı döküyor.
7394|demir bir kolu güçlükle çekmek;aralıktan süzülerek geçmek;bir bacağını uzatmak|açılır köprü;yelkenli gemi;örgü bere;arnavut kaldırımı|Kadın ne yapıyor?|Demir bir kolu güçlükle çekiyor.
7395|kırmızı bir kanoyla kürek çekmek;uzakta suda süzülmek;açıklıktan fırlayarak geçmek|açıklık;deniz feneri;kask;köpük|Kadın ne yapıyor?|Dar bir açıklıktan kürek çekerek geçiyor.
7396|uzun otların arasından izlemek;sisin içinde dönmek;parlayan ışıkları yansıtmak|atlıkarınca;dönme dolap;tilki;su birikintisi|Tilki ne yapıyor?|Tilki parlayan atlıkarıncayı izliyor.
7398|bir bant makarasını başının üstüne kaldırmak;pres makinesi kullanmak;plakları taşımak|kalabalık;bant makarası;taşıma bandı;taşıma arabası|Eldivenli kadın ne yapıyor?|Bant makarasını başının üstüne kaldırıyor.
7401|maskeyle nefes almak;ayağa kalkmak;oksijen maskesi tutmak|zirve;bulutlar;kapüşon;oksijen tüpü|Sarı giyinmiş kadın ne yapıyor?|Oksijen maskesini adamın yüzüne bastırıyor.
7402|büyük bir çanta hazırlamak;bir bot taşımak;önde oturmak|kum;ayna;çanta;şişe|Kadın ne yapıyor?|Büyük bir çanta hazırlıyor.
7403|minibüsün kapısını zorla kapatmak;taşınabilir buzluğun üstünde oturmak;minibüsten dışarı taşmak|sörf tahtaları;frizbi;plaj topu;taşınabilir buzluk|Güneş gözlüklü adam ne yapıyor?|Minibüsün kapısını zorla kapatıyor.
7406|güneşte kurumak;rüzgârda sallanmak;çamaşır ipinde asılı durmak|gökyüzü;balkon;külotlar|Külotlar ne yapıyor?|Güneşte kuruyorlar.
7407|başını geriye atmak;kapıdan sırıtmak;peronda yerde durmak|kondüktör;deve tüyü palto;bavul;bez çanta|Kadın ne yapıyor?|Peronda adama sarılıyor.
7408|bir köpek tutmak;taburenin üstünde durmak;barın arkasında çalışmak|adam;gazete;köpek;tabure|Adam ne yapıyor?|Köpeği tabureye koyuyor.
7409|bir buz parçası kaldırmak;tırmanış emniyet kemeri takmak;arka planda yükselmek|buzul;saç bandı;buz parçası;emniyet kemeri|Kadın ne tutuyor?|Büyük bir buz parçası tutuyor.
7410|nehre yürüyerek girmek;gözlüğünü düzeltmek;bir kıskaçlı not altlığını havaya kaldırmak|kara tahta;kalabalık;su geçirmez çanta;ip|Yalınayak adam ne yapıyor?|Nehre yürüyerek giriyor.
7411|sandalyesinden kalkmak;genç kadını teselli etmek;başını tutmak|saat;hâkim;dizüstü bilgisayar;klasör|Gri giyinmiş adam ne yapıyor?|Elleriyle başını tutuyor.
7412|havaya zıplamak;sevinçle bağırmak;arabada oturmak|gökyüzü;ev;arabalar;yol|Kadın ne yapıyor?|Arabanın yanında zıplıyor.
7415|emaye bir kupayı yeniden doldurmak;gazetenin üzerine eğilmek;saatine göz atmak|müşteri;su kazanı;domuz pastırması;bulmaca|Kadın ne yapıyor?|Emaye bir kupaya çay dolduruyor.
7416|ejderhanın burnunu okşamak;hasır bir sepet taşımak;kadının yanağına burnunu sürtmek|ejderha;mağara;hasır sepet;baston|Ejderha ne yapıyor?|Kadının yanağına burnunu sürtüyor.
7419|makarnaya karabiber serpmek;kahkahayı basmak;kaşlarını kaldırmak|garson;makarna;sürahi;masa örtüsü|Kadın ne yapıyor?|Makarnaya karabiber serpiyor.
7420|tarlanın öbür tarafını işaret etmek;çimenlere uzanmak;köpekten kaçmak|çadır;kadın;köpek;koyunlar|Kadın ne yapıyor?|Tarlanın öbür tarafını işaret ediyor.
7421|tozlu sahnede ayak vurmak;uzun saçlarını savurmak;akustik gitar tıngırdatmak|spot ışığı;jambonlar;sanatçı;gitar|Dansçı ne yapıyor?|Tozlu sahnede ayak vuruyor.
7422|ahşap musluğu çekiştirmek;köpükle taşmak;arnavut kaldırımlı zeminde yatmak|meyve bahçesi;fıçı;armut şarabı;armutlar|Ahşap leğene ne oluyor?|Köpüklü armut şarabıyla taşıyor.
7425|vanadan fışkırmak;ham petrolle taşmak;yere yayılmak|vana;hortum;kova;petrol|Metal kovaya ne oluyor?|Ham petrolle taşıyor.
7427|güneş ışığında dönmek;kollarını iki yana açmak;kapı pervazına yaslanmak|kemerli pencere;palet;el arabası;moloz|Kadın ne yapıyor?|Güneş ışığında dönüyor.
7428|bir kaya parçasına dokunmak;kayanın üzerine eğilmek;elini gözlerine siper etmek|gökyüzü;şapka;kamyon;kaya parçası|Eldivenli kadın ne yapıyor?|Bir kaya parçasına dokunuyor.
7429|gölgeliği yere sabitlemek;uçan havluya uzanmak;kot şort giymek|hasır şapka;deniz;plaj gölgeliği;çadır kazıkları|Beyazlı kadın ne yapıyor?|Gölgeliği kuma sabitliyor.
7430|bütün bir somonu fırlatmak;havada süzülmek;beyaz bir kutunun üstüne tünemek|somon;tekir kedi;kasalar;midyeler|At kuyruklu kadın ne yapıyor?|Bir somonu havaya fırlatıyor.
7434|çamurda kaymak;sevinçle çığlık atmak;kollarını iki yana açmak|gökyüzü;eldiven;ev plakası;çamur|Çizgili kadın ne yapıyor?|Çamurda kayıyor.
7439|ateşi karıştırmak;bir yastığın arkasına saklanmak;gümüş bir tepsi tutmak|şömine rafı;şömine demiri;odunlar;maşa|Genç adam ne yapıyor?|Şömine demiriyle ateşi karıştırıyor.
7440|pençesiyle otobüse vurmak;pencereden el sallamak;uzaktan izlemek|gökyüzü;örgü bere;kutup ayısı;kar|Büyük kutup ayısı ne yapıyor?|Otobüsün yanında yürüyor.
7442|eyersiz ata binmek;yalınayak bir biniciyi taşımak;kocaman sırıtmak|uçurum;çit;midilli;nehir|Genç kadın ne yapıyor?|Midilliyle nehrin içinden geçiyor.
7444|motosikletin altında yatmak;ona yukarıdan bakmak;parıl parıl yanmak|lamba;aletler;motosiklet;köpek|Kadın ne yapıyor?|Motosikletin altında yatıyor.
7449|kollarını havaya kaldırmak;acı çeker gibi yüzünü buruşturmak;tuvalet için sıra beklemek|duş perdesi;tuvalet;karton bardak;çamur|Kızıl saçlı kadın ne yapıyor?|Acı çeker gibi yüzünü buruşturuyor.
7454|karda inatla ilerlemek;gidonu sıkıca kavramak;bir kayanın üstüne tünemek|kask;taş kulübe;dağ sıçanı;yol bisikleti|Siyahlı adam ne yapıyor?|Karda inatla ilerliyor.
7472|bir kanal teknesini çekmek;kupasını kaldırmak;siste durmak|tuğla köprü;balıkçıl;kanal teknesi;bocurgat|Ekoseli adam neyi çekiyor?|Bir kanal teknesini kanal boyunca çekiyor.
7473|pompa kolunu çalıştırmak;yalaktan su içmek;suyla taşmak|kır evleri;pompa;yalak;kova|Kadın ne pompalıyor?|Kovaya su pompalıyor.
7476|kuklanın iplerini çekmek;güvercine eğilerek selam vermek;kuklaya dik dik bakmak|seyirciler;kukla;güvercin;kırıntılar|Güvercin neye dik dik bakıyor?|Güvercin kuklaya dik dik bakıyor.
7478|pencere pervazında uzanmak;ön patisini sarkıtmak;pencere pervazında gezinmek|kedicik;pencere pervazı;hasır sepet;yün yumağı|Kedicik ne yapıyor?|Kedicik pencere pervazında geziniyor.
7480|kapıyı güçlükle kapatmak;bacaklarıyla destek almak;kapanmak|tavan lambası;kasa kapısı;elmas;taşıma arabası|Adam neyi güçlükle kapatıyor?|Kasa kapısını güçlükle kapatıyor.
7481|ipe tutunmak;yanan bir meşale tutmak;bir ip askıda sallanmak|çatı penceresi;kil küp;seyyar merdiven;kaide|Maymunlar küpü nereye koyuyor?|Onu tekrar kaidenin üstüne koyuyorlar.
7482|ahşap bir bloğu indirmek;korkuluğun arkasına çömelmek;ağızlarını kapatmak|emniyet kemeri;balonlar;kule;kalabalık|Kadın ne yapıyor?|Bir bloğu kulenin üstüne indiriyor.
7483|çimenlere iniş yapmak;çimenleri havaya savurmak;rüzgâr tulumunun yanından geçmek|rüzgâr tulumu;buzul;uçak;koyunlar|Uçak ne yapıyor?|Çimenlere iniş yapıyor.
7488|yumurta bırakmak;diğerlerinden büyük olmak;güneşte parlamak|kraliçe arı;yumurta;bal|Kraliçe arı ne yapıyor?|Yumurta bırakıyor.
7492|yağmur suyu fışkırtmak;duvara yaslanmak;plastik örtünün altında durmak|sağanak;tente;bisikletler;petrol varili|Çatıdan ne akıyor?|Teneke çatıdan şiddetli yağmur akıyor.
7502|iki boksörü ayırmak;iki kolunu uzatmak;kahverengi boks eldivenleri giymek|hakem;seyirciler;halatlar|Hakem ne yapıyor?|İki boksörü ayırıyor.
7529|dev bir şamandıranın etrafından dönmek;su serpintisi sıçratmak;dalgalı denizde inip kalkmak|şamandıra;yelken;tekne gövdesi;dalgalar|Yat ne yapıyor?|Dev bir şamandıranın etrafından dönüyor.
7738|kızak çekmek;koyu renk sakalı olmak;nehir boyunca yürümek|gökyüzü;mamut;kızak;kar|Kadın ne yapıyor?|Kızak çekiyor.
7740|omzunun üzerinden bakmak;toprağı incelemek;kanatlarını açmak|ağaçlar;traktör;pulluk;şahin|Adam ne yapıyor?|Bir avuç toprağı inceliyor.
7741|şaşkınlıkla geri sıçramak;koridora koşarak girmek;paketlenmiş bir hediye taşımak|fener;ayçiçekleri;bornoz;fayanslar|Lila giyinmiş kadın ne yapıyor?|Şaşkınlıkla geri sıçrıyor.
7742|sarı bir tutamaktan sarkmak;inanamayarak başını tutmak;mavi minderin üstünde çömelmek|çatı penceresi;saç örgüsü;tırmanma duvarı;düşme minderi|Tırmanıcı ne yapıyor?|Sarı bir tutamaktan sarkıyor.
7743|beyaz bir sörf tahtası taşımak;aşçı şapkasını sıkıca tutmak;krem rengi ceketini iliklemek|martı;lamba direği;sörf tahtası;dökülmüş yapraklar|Aşçı ne yapıyor?|Aşçı şapkasını sıkıca tutuyor.
7746|beyaz bir elbise giymek;ceket giymek;duvarda asılı durmak|lamba;pencere;güller;pasta|Ne kesiyorlar?|Beyaz bir pasta kesiyorlar.
7747|kahverengi bir ceket giymek;lacivert bir ceket giymek;beyaz ayakkabı giymek|gökyüzü;evler;tekne;su|Elleri birbirine değebilir mi?|Hayır, birbirlerinden çok uzaktalar.
7749|tuvale boya fırlatmak;seyyar merdivende durmak;başını geriye atmak|tuval;seyyar merdiven;boya kutusu;lamba|Öndeki kadın ne yapıyor?|Tuvale boya fırlatıyor.
7750|eski bir lastiği fırlatmak;bir tabela kaldırmak;tekerlek takmak|gökyüzü;kadın;tekerlek;araba|Öndeki kadın ne yapıyor?|Tekerlek değiştiriyor.
7752|kollarına atlamak;bagaj arabalarını itmek;çiçek tutmak|ağaç;bavul;bardaklar;palto|Kadın ne yapıyor?|Onun kollarına atlıyor.
7753|tabağa yemek koymak;yeşil sebze doğramak;kapıları itmek|kadın;tava;havlu;lamba|Kadın ne yapıyor?|Tabağa yemek koyuyor.
7754|gitar çalmak;kılıfa para koymak;kılıfın yanında oturmak|gitar;köpek;bisiklet;gökyüzü|Adam ne yapıyor?|Gitar çalıyor.
7755|planların üzerine eskiz çizmek;lila bir hırka giymek;kot gömlek giymek|saksı bitkisi;blazer ceket;sürahi;teknik çizim|Mavili kadın ne yapıyor?|Bina planlarının üzerine eskiz çiziyor.
7757|domates bitkilerine su püskürtmek;olgun domatesleri havaya kaldırmak;bahçenin yanından süzülerek geçmek|kruvaziyer gemisi;domatesler;şezlong;sulama kabı|Adam ne yapıyor?|Hortumla domates bitkilerine su püskürtüyor.
'''
out={}
rows={l.split('|')[0]:l.split('|') for l in R.strip().split('\n')}
for k,v in src.items():
    r=rows[k]; ph=r[1].split(';'); no=r[2].split(';')
    assert len(ph)==len(v['phrases']) and len(no)==len(v['nouns']),k
    out[k]={'phrases':ph,'nouns':no,'question':r[3],'answer':r[4]}
json.dump(out,open(os.path.join(H,'tr.json'),'w'),ensure_ascii=False,indent=1)
