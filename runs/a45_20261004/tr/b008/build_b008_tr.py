import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """
569 # ön kapının kilidini açmak | gür bir bıyığı olmak | saçını at kuyruğu yapmak # postane müdürü | anahtarlar | koliler | yük arabası # Postane müdürü ne yapıyor? # Kolilerle dolu bir yük arabasını itiyor.
572 # bahçede toprak kazmak | mavi bir atkı takmak | bir çitin üzerinde tünemek # kuş | kadın | patatesler | kova # Kadın ne yapıyor? # Patatesleri bir kovaya koyuyor.
573 # portakal suyu koymak | büyük bir şişe tutmak | bir bardağı eline almak # adam | kadın | şişe | bardaklar # Adam ne yapıyor? # Bardaklara portakal suyu koyuyor.
574 # ağzını kocaman açmak | göğsüne dokunmak | kısa siyah saçları olmak # ağaç | fırça | kavanoz | pudra # Kavanozda ne var? # Kavanozda pudra var.
575 # ellerini havaya kaldırmak | çantasını karıştırmak | bir taşınabilir şarj cihazını havaya kaldırmak # taşınabilir şarj cihazı | güvercinler | güller | bank # Telefonu neye takıyorlar? # Onu bir taşınabilir şarj cihazına takıyorlar.
576 # masasında dua etmek | ellerini birleştirmek | yukarı bakıp ağlamak # kadın | dizüstü bilgisayar | kitaplar | lamba # Kadın ne yapıyor? # Masasında dua ediyor.
577 # yağmuru tahmin etmek | kahkahayı patlatmak | ani bir sağanak getirmek # fırtına bulutu | şemsiye | şal | çimen # Kadın ne yapıyor? # Sarı bir şemsiyenin altına sığınıyor.
578 # bir motosikleti iterek dışarı çıkarmak | yakıt deposunu parlatmak | onun omzuna hafifçe vurmak # bandana | yakıt deposu | motor | parke taşları # Tamirci ne yapıyor? # Motosikletini gururla sergiliyor.
579 # yeni kod yazmak | dizüstü bilgisayarı işaret etmek | çizilmiş pisti takip etmek # robot | dizüstü bilgisayar | at kuyruğu | sakal # Kadın ne yapıyor? # Küçük bir robotu programlıyor.
580 # bir paltoyu yukarıda tutmak | bir sepet taşımak | gözlük takmak # sepet | palto | gökyüzü | gözlük # Uzun boylu kadın ne yapıyor? # Arkadaşını yağmurdan koruyor.
581 # bir ayçiçeğini sımsıkı tutmak | ağaç resimli bir pankart taşımak | esintide dalgalanmak # ayçiçeği | palmiye ağacı | gökyüzü | kalabalık # İnsanlar ne yapıyor? # Boyanmış pankartlarla protesto ediyorlar.
582 # bir sandalyede oturmak | kollarını kavuşturmak | onun omzuna dokunmak # sandalye | kadın | pencere | masa # Kadın nasıl hissediyor? # Yeni sandalyesiyle gurur duyuyor.
584 # amuda kalkmak | onun yanıldığını kanıtlamak | hayretle nefesini tutmak # çıplak ayaklar | tayt | bank | örgü yelek # Genç kadın ne yapıyor? # Onun yanıldığını kanıtlamak için amuda kalkıyor.
585 # halka açık bir yerde müzik çalmak | bir kutunun üzerinde oturmak | suyu yukarı fışkırtmak # sokak lambası | adamlar | akordeon | kutu # Genç kadın ne yapıyor? # Halka açık bir yerde akordeon çalıyor.
588 # kırmızı çizme giymek | siyah çizme giymek | uzakta durmak # sarı yağmurluk | kuş | kırmızı çizmeler | su birikintisi # İki kişi ne yapıyor? # Büyük bir su birikintisine atlıyorlar.
589 # kırmızı bir şey tutmak | kısa bir sakalı olmak | çimenlerin üzerinde koşmak # köpek | çimen | adam | halat # Adam ve kadın ne yapıyor? # Kalın bir halatı çekiyorlar.
590 # hızlı yumruklar atmak | boks lapalarını yukarıda tutmak | bir zincire asılı durmak # tuğla duvar | kum torbası | boks eldivenleri | şort # Kadın ne yapıyor? # Boks lapalarına yumruk atıyor.
591 # güçlü yumruklar atmak | merdiveni sabit tutmak | tavandan sallanmak # zincir | kum torbası | boks eldivenleri | şort # Adam ne yapıyor? # Kum torbasına yumruk atıyor.
592 # koyu renk bir sakalı olmak | beyaz bir tişört giymek | yol boyunca yuvarlanıp gitmek # gökyüzü | minibüs | yol # İki adam ne yapıyor? # Beyaz bir minibüsü itiyorlar.
593 # kısa kıvırcık saçları olmak | uzun koyu renk saçları olmak | yerde uyumak # pencere | pijama | yatak | köpek # Adam ve kadın ne giyiyor? # Pijama giyiyorlar.
594 # çıtayı aşmak | yeşil bir bayrak sallamak | yumruklarını havada sallamak # çıta | bayrak | at kuyruğu | minder # Kız nasıl tur atlıyor? # Çıtayı aşarak tur atlıyor.
595 # yeşil yapraklar yemek | yüzünü yıkamak | çimenlerin üzerinden atlamak # gökyüzü | tavşan | çimen | yapraklar # Tavşan ne yiyor? # Yeşil yapraklar yiyor.
597 # bir raketin içinden bakmak | filenin arkasında durmak | kameraya gülümsemek # çiçekler | top | file | raket # Kadın ne tutuyor? # Siyah bir raket tutuyor.
598 # kollarını iki yana açmak | beyaz bir gömlek giymek | dört ayak üzerinde yürümek # çatı | ağaç | köpek | kayık # Kız ne yapıyor? # Yağmurda dans ediyor.
599 # renkli bir topu sürmek | siyahlı adama müdahale etmek | beyaz bir topu kontrol etmek # kale | futbol topu | çim | çatı # İki adam ne yapıyor? # Top için mücadele ediyorlar.
600 # iki ayağı üzerinde durmak | bir pizza dilimini çekmek | büyük siyah tekerlekleri olmak # sıçan | pizza | merdivenler | pencere # Sıçan ne yapıyor? # Bir pizza dilimini çekiyor.
601 # tıraş makinesiyle tıraş olmak | saatini işaret etmek | lavabonun üzerinde yürümek # tıraş makinesi | lamba | ayna | tişört # Beyazlı adam ne yapıyor? # Tıraş makinesiyle tıraş oluyor.
604 # kırmızı bir elma tutmak | meyve satmak | uzun bir fiş yazdırmak # fiş | elmalar | armutlar | şişeler # Adam neye bakıyor? # Uzun bir fişe bakıyor.
606 # bir kafesin içinde durmak | siyah bir sakalı olmak | kıvırcık saçları olmak # yemek tarifi | kuş | pankekler | adam # Adam ve kadın ne yiyor? # Pankek yiyorlar.
607 # yerde yatmak | buzdolabına dokunmak | siyah bir sakalı olmak # buzdolabı | köpek | adam | kadın # Adam ve kadın nerede duruyor? # Buzdolabının yanında duruyorlar.
608 # direksiyonu sımsıkı tutmak | rahatlayarak gülmek | ön camın üzerinde durmak # direksiyon | gösterge paneli | silecek | sweatshirt # Sürücü neyi sımsıkı tutuyor? # Direksiyonu sımsıkı tutuyor.
609 # kırmızı bir sırt çantası taşımak | botlarını çıkarmak | mavi bir atkı takmak # gökyüzü | göl | kaya | sırt çantası # Adam ve kadın ne yapıyor? # Çimenlerin üzerinde dinleniyorlar.
610 # üç kurdele taşımak | büyük bal kabağına sarılmak | büyük ve turuncu olmak # kurdele | bal kabağı | şapka | bayraklar # Büyük bal kabağının üzerinde ne var? # Bal kabağının üzerinde mavi bir kurdele var.
613 # ringe çıkmak | mavi eldiven takmak | bir su şişesi tutmak # ring | adam | duvar # Adam ne yapıyor? # Ringde boks yapıyor.
615 # suyun üzerinde uçmak | nehirde aşağı doğru ilerlemek | nehir kıyısında yetişmek # nehir | kuş | yapraklar | taşlar # Nehirde aşağı doğru ne ilerliyor? # İki yaprak nehirde aşağı doğru ilerliyor.
616 # kızıl saçları olmak | gri bir kazak giymek | büyük ve yuvarlak olmak # kaya | gökyüzü | nehir # Neyin üzerinde duruyorlar? # Büyük bir kayanın üzerinde duruyorlar.
618 # bir ip bağlamak | yük arabasının arkasında durmak | büyük bir tekerleği olmak # ağaç | ip | tekerlek | çamur # İri adam ne yapıyor? # Bir yük arabasını iple çekiyor.
619 # bir sepeti yukarı çekmek | ara sokakta beklemek | bir duvarın üzerinde gezinmek # otlar | portakallar | sepet | ip # Kadın ne yapıyor? # Portakal dolu bir sepeti yukarı çekiyor.
621 # sıranın yanında durmak | pembe bir şapka takmak | kırmızı bir tepesi olmak # gökyüzü | şapka | bitkiler | yer # İnsanlar ne yapıyor? # Küçük bitkileri sıra hâlinde dikiyorlar.
622 # bir paket lastiğini çekmek | yüzüne dokunmak | sokakta yürümek # paket lastiği | kadın | adam | kutu # Kadın ne yapıyor? # Bir paket lastiğini çekiyor.
623 # telefonuna bakmak | ona bir kahve getirmek | ayaklarını masaya uzatmak # telefon | güneş gözlüğü | bot | çatal # Genç adam ne yapıyor? # Telefonuna bakıyor.
626 # bir bardaktan içmek | yarışı izlemek | saatine bakmak # bardak | saat | gökyüzü | koşucu # Koşucu ne yapıyor? # Bir bardaktan içiyor.
627 # halı boyunca çalımla yürümek | arkadaşını videoya çekmek | hiç kıpırdamadan oturmak # halı | peri ışıkları | şömine | lambader # Mavili kadın ne yapıyor? # Halı boyunca çalımla yürüyor.
628 # birkaç kitap paketlemek | bir kitap tutmak | yerde ağlamak # raflar | gözlük | kitaplar | kutular # Kadın ne yapıyor? # Yerde ağlıyor.
629 # kapıyı kapatmak | bir mont asmak | sarı bir mont giymek # kadın | adam | fincanlar | odun # Kadın neyi kapatıyor? # Büyük ahşap kapıyı kapatıyor.
630 # uzun bir halatı çekmek | büyük dümeni tutmak | iki kolunu da kaldırmak # denizci | dümen | halat | yelken # Denizci ne yapıyor? # Uzun bir halatı çekiyor.
631 # bir salatalık kesmek | salatayı karıştırmak | küçük bir domates yemek # kadın | adam | salata | masa # Adam ne hazırlıyor? # Bir salata hazırlıyor.
632 # domateslere tuz serpmek | kısa koyu renk saçları olmak | pencerenin dışında durmak # kuş | tuz | domatesler | ekmek # Kadın ne yapıyor? # Domateslere tuz serpiyor.
634 # kuru kum dökmek | bir çubukla çizim yapmak | çizimi örtmek # kadın | adam | dalga | kum # Adam ne yapıyor? # Avucuna kum döküyor.
635 # sandaletlerini giymek | yeşil bir şort giymek | bir bankın üzerinde durmak # gökyüzü | kuş | bank | sandaletler # Ayaklarında ne var? # Ayaklarında sandalet var.
636 # bir sandviç hazırlamak | sandviçi kesmek | sepetin arkasında durmak # ağaçlar | ördek | sepet | sandviç # Kadın ne hazırlıyor? # Bir sandviç hazırlıyor.
638 # yeşil sos dökmek | bir patates yemek | çimenlerin üzerinde oturmak # adam | kadın | köpek | sos # Adam ne yapıyor? # Yeşil sos döküyor.
639 # sosisleri çevirmek | bir sosisli sandviç yemek | bir tavanın içinde durmak # şapka | çadır | kuş | sosisler # Kadın ne yiyor? # Bir sosisli sandviç yiyor.
640 # iki ağırlığı eline almak | iri kollarını göstermek | tartıyı işaret etmek # adam | kadın | zemin | tartı # Adam neyin üzerinde duruyor? # Bir tartının üzerinde duruyor.
641 # biraz un dökmek | uzun bir saç örgüsü olmak | tartının üzerine tünemek # bakır tavalar | tekir kedi | karıştırma kabı | mutfak tartısı # Kedi nereye tünemiş? # Mutfak tartısının üzerine tünemiş.
642 # ön kolunu işaret etmek | gür bir sakalı olmak | yara izli kaval kemiğini göstermek # trençkot | ampul | yara izi | kupalar # Sarışın adam ne gösteriyor? # Kaval kemiğindeki bir yara izini gösteriyor.
644 # ağzını kapatmak | beyaz bir çanta taşımak | bir telefonu havaya kaldırmak # gözlük | saç | çanta | zemin # Korkmuş kadın ne yapıyor? # Ağzını kapatıyor.
645 # bir daire çizmek | siyah bir kalem tutmak | saat takmak # program | adam | defter | dosyalar # Adam ne çiziyor? # Programın üzerine bir daire çiziyor.
647 # makasla saç kesmek | aynaya bakmak | bir sandalyede oturmak # makas | tarak | havlu | gözlük # Gözlüklü kadın ne yapıyor? # Makasla saç kesiyor.
649 # genç adamı azarlamak | bir hasır şapkayı sımsıkı tutmak | kollarını kavuşturmak # başörtüsü | önlük | bahçe kapısı | lahanalar # Yaşlı kadın ne yapıyor? # Genç adamı azarlıyor.
650 # yerde emeklemek | uzun bir saç örgüsü olmak | kutunun üzerinden bakmak # vida | karton kutu | golden retriever | başparmak # Adam ne arıyor? # Eksik bir vidayı arıyor.
651 # bir vidayı sıkmak | ahşap rafı sabit tutmak | kanepenin üzerine tünemek # tornavida | kitaplar | kedi | ev bitkisi # Kadın ne yapıyor? # Tornavidayla bir vidayı sıkıyor.
652 # kayalara çarpmak | beyaz bir gömlek giymek | kısa saçları olmak # deniz | kadın | adam | kayalar # Ne yapıyorlar? # Denize atlıyorlar.
653 # bir yastığı kaldırmak | anahtarları işaret etmek | kapının yanında yatmak # anahtarlar | kapı | kedi | adam # Adam neyi işaret ediyor? # Kapıdaki anahtarları işaret ediyor.
654 # bir sır fısıldamak | arkadaşını dinlemek | duvarın üzerinden bakmak # gökyüzü | lamba | dağ | gözlük # Sarılı kadın ne yapıyor? # Arkadaşına bir sır fısıldıyor.
655 # siyah bir çizgi çekmek | odaya koşarak girmek | küçük bir düdük çalmak # şapka | gözlük | kâğıt | masa # Mavili kadın ne yapıyor? # Kâğıda siyah bir çizgi çekiyor.
656 # satranç saatine basmak | haki bir ceket giymek | sıkılmış iki yumruğunu da kaldırmak # kemerli pencereler | halat | satranç saati | satranç tahtası # Satranç oyuncusu ne yapıyor? # Hamlesinden sonra satranç saatine basıyor.
657 # yemeği servis etmek | biraz su koymak | yemeğine bakmak # kadın | bardak | çatal | masa # Kadın ne yapıyor? # Adama yemek servis ediyor.
660 # arkadaşının saçını köpürtmek | leğenin üzerine eğilmek | sabunlu suyu toplamak # muz yaprakları | musluk | leğen | tabure # Yeşilli kadın ne yapıyor? # Arkadaşının saçını köpürtüyor.
661 # büyük ağzını açmak | çok yakına gelmek | sürü hâlinde yüzmek # balıklar | köpek balığı | su # Köpek balığı ne yapıyor? # Köpek balığı büyük ağzını açıyor.
662 # bir yıldız çizmek | kısa saçları olmak | ot yemek # at | kalemtıraş | defter | kâse # Kadın ne çiziyor? # Bir yıldız çiziyor.
663 # tıraş köpüğü sürmek | aynaya bakmak | arkadaşını izlemek # lambalar | ayna | tıraş köpüğü | musluk # Mavili adam ne yapıyor? # Yüzüne tıraş köpüğü sürüyor.
664 # adamın yüzünü tıraş etmek | bir koltukta uzanmak | pencerenin yanında oturmak # şişeler | kedi | adam | kâse # Kadın ne yapıyor? # Adamın yüzünü tıraş ediyor.
666 # bir gömlek giymek | adamı izlemek | gömleğini iliklemek # kuş | kadın | gömlek # Adam ne yapıyor? # Mavi bir gömlek giyiyor.
667 # başını tutmak | kaldırımda yatmak | şok içinde nefesini tutmak # yaya | kask | scooter | kaldırım # Kadın ne yapıyor? # Şok içinde başını tutuyor.
668 # ayakkabılarını bağlamak | kahve bardakları tutmak | suyun içinden yürümek # kapı | pantolon | ayakkabılar | yer # Kadın ne yapıyor? # Kahverengi ayakkabılarını bağlıyor.
669 # bir sepet taşımak | ona ekmeği vermek | madeni paralarla ödemek # lamba | gözlük | ekmek | şapka # Kadın ne yapıyor? # Bir dükkânda ekmek satın alıyor.
671 # kısa bir sakalı olmak | mavi bir sırt çantası taşımak | uzun bir boynu olmak # gökyüzü | lama | adam | kadın # İki kişi ne yapıyor? # Bir lamanın yanında bağırıyorlar.
672 # bir havlu tutmak | mavi bir tişört giymek | duşun üzerinde durmak # kuş | duş | havlu | adam # Kadın ne yapıyor? # Plajda duş alıyor.
674 # burnunu sümkürmek | ona bir fincan getirmek | pencerenin yanında yetişmek # bitki | fincan | battaniye | masa # Kadın ne yapıyor? # Hasta kadın burnunu sümkürüyor.
675 # bir kovanın üzerine eğilmek | gözlük takmak | parlak maviye dönmek # tekne | ağ | adam | kovalar # Sarışın adam ne yapıyor? # Teknenin yan tarafını boyuyor.
678 # ipeği havaya kaldırmak | omuz hizasında saçları olmak | tezgâhın üzerinde çömelmek # vantilatör | ipek | kedi | tezgâh # Bejli kadın ne yapıyor? # İpeği yanağına bastırıyor.
679 # gümüşü temizlemek | küpe takmak | başının üzerinde asılı durmak # lamba | gümüş | kadın # Kadın ne yapıyor? # Gümüşü bir bezle temizliyor.
681 # kameraya bakmak | arabayı sürmek | uzun ve düz olmak # ayna | yol | adam | kadın # Ne yapıyorlar? # Arabada şarkı söylüyorlar.
683 # suyu açmak | sarı bir sünger tutmak | temiz bir tabak göstermek # adam | kadın | evye | tabaklar # Evyede ne yıkıyorlar? # Evyede tabakları yıkıyorlar.
684 # masada oturmak | kapıyı açmak | iki kıza sarılmak # kapı | kız | kaşık | çatal # İki kız kardeş ne yapıyor? # İki kız kardeş birbirine sarılıyor.
685 # şapka denemek | küçük bir ayna tutmak | şapka satmak # gökyüzü | şapka | saç | elbise # Kız ne yapıyor? # Şapka deniyor.
687 # kaykay sürmek | havaya zıplamak | şehrin üzerinde parlamak # güneş | evler | oğlan | kaykay # Oğlan ne yapıyor? # Kaykay sürüyor.
688 # yüz kremi sürmek | kolunu ovmak | yanaklarına dokunmak # cilt | gökyüzü | bitkiler | tişört # Kadın ne yapıyor? # Cildine krem sürüyor.
689 # eteğini tutmak | kendi etrafında dönmek | beyaz ayakkabı giymek # etek | tişört | kuşlar | ağaçlar # Kadın ne giyiyor? # Sarı bir etek giyiyor.
691 # gri bir arabayı korumak | tahta bir sopa sallamak | dışarıda park edilmiş olmak # asker | dikenli tel | beton duvar | toprak yol # Asker ne yapıyor? # Arabayı bir sopayla koruyor.
692 # kollarını yukarı kaldırmak | bir battaniyenin altında uyumak | bir kitap okumak # kedi | lamba | battaniye | yastık # Adam ne yapıyor? # Bir battaniyenin altında uyuyor.
693 # gözlerini ovuşturmak | pencerenin yanında uyumak | onun kucağında durmak # pencere | koltuk | kazak | defter # Kadın nasıl hissediyor? # Kendini çok uykulu hissediyor.
695 # eline yaslanmak | yeşil bir atkı takmak | teknenin üzerinde uçmak # güneş | kuşlar | tekne | deniz # İnsanlar ne yapıyor? # Teknede gülümsüyorlar.
696 # adama gülmek | dumanı eliyle dağıtmak | gökyüzüne yükselmek # duman | kadın | adam | yapraklar # Adam ne yapıyor? # Dumanı eliyle dağıtıyor.
697 # kırmızı bir ceket giymek | siyah bir sakalı olmak | bir sigara yakmak # lamba | sigara | ceket # Kırmızılı adam ne yapıyor? # Bir sigara içiyor.
698 # smoothie koymak | daha fazla meyve eklemek | meyveleri karıştırmak # smoothie | muzlar | çilekler | kadın # Turunculu kadın ne yapıyor? # Bir bardağa smoothie koyuyor.
699 # kaçak olarak biraz peynir geçirmek | bariyeri kaldırmak | samanla yüklü olmak # muhafız | saman | bariyer | yük arabası # Çiftçi kaçak olarak ne geçiriyor? # Samanın altında kaçak olarak peynir geçiriyor.
700 # çok yavaş hareket etmek | bir yaprağın üzerine tırmanmak | patikanın üzerinde durmak # salyangoz | yaprak | çimen # Salyangoz ne yapıyor? # Bir yaprağın üzerine tırmanıyor.
701 # kumun üzerinde ilerlemek | dilini dışarı çıkarmak | yılanın altında durmak # yılan | kaya | kum | gökyüzü # Yılan nerede yatıyor? # Siyah bir kayanın üzerinde yatıyor.
"""
out = {}
for line in D.strip().splitlines():
    i, p, n, q, a = [x.strip() for x in line.split(' # ')]
    out[i] = {'phrases': [x.strip() for x in p.split(' | ')], 'nouns': [x.strip() for x in n.split(' | ')], 'question': q, 'answer': a}
src = json.load(open(f'{H}/source.json'))
out = {i: out[i] for i in src}
json.dump(out, open(f'{H}/tr.json', 'w'), ensure_ascii=False, indent=1)
