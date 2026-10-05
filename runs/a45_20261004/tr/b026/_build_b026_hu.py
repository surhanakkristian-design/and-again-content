import json, os
H=os.path.dirname(os.path.abspath(__file__))
R='''7070|kortyolgatni a whiskyjét;megdörzsölni a fáradt szemét;aggódva figyelni őt|pultoslány;feles poharak;földimogyorók;részeg|Mit csinál a férfi?|A whiskyjét kortyolgatja.
7072|elkapni egy guruló dobozt;megszaglászni a kalapdobozt;a lépcsőről figyelni|kúria;gróf;ír farkaskutyák;kalapdoboz|Mit csinál a fiatalember?|Elkap egy guruló kalapdobozt.
7073|megtámasztani egy ólomüveg ablakot;letérdelni egy párnázott takaróra;megragadni a fenti állványzatot|ólomüveg ablak;takaró;kötél;vízmérték|Mit csinál a nő?|Egy ólomüveg ablakot támaszt meg.
7074|egy gőzölgő paellát vinni;megigazítani a szalmakalapját;az asztal alatt pihenni|szalmakalap;paella;cipó;kutya|Mit csinál a nő?|Egy gőzölgő paellát visz.
7075|jegyzeteket lefirkantani;odanyújtani egy hagymát;karba tenni a kezét|függő mérleg;krétatábla;írótábla;hagymák|Mit csinál a fiatal nő?|Jegyzeteket ír egy írótáblára.
7076|a perem mentén sétálni;kitárni a karját;kétrét görnyedni a nevetéstől|vászonsátor;flamingók;kavics;perem|Mit csinál a nő?|A perem mentén sétál.
7077|a műszerfalra mutatni;tiltakozva felemelni a kezét;megtölteni a pohártartókat|visszapillantó tükör;légfrissítő;kormány;jeges kávék|Mit csinál a sofőr?|A műszerfalra mutat.
7079|megvizsgálni a borostyánszínű üveget;letenni az üveget;kis üvegdarabokat elrendezni|ólomüveg tábla;szöges bádogdoboz;tekercs;forrasztópáka|Mit csinál a férfi?|Egy borostyánszínű üvegdarabot vizsgál.
7080|egy nagy növényt vinni;kiszállni a liftből;feltartani a táskáját|növény;lift;kutya;lépcső|Mit visz a fiatal nő?|Egy nagy növényt visz.
7081|a hordágy mellett rohanni;felhúzni a kesztyűjét;lélegeztetőballont nyomkodni|hordágy;ápolónő;orvos;kerekesszék|Mit csinál az ápolónő?|A hordágy mellett rohan.
7082|nekitámaszkodni a kapunak;megsimogatni egy birka fejét;figyelni az elhaladó nyájat|szalmakalap;kapu;birkák;kutya|Minek támaszkodik neki a nő?|Egy fakapunak támaszkodik neki.
7083|hitetlenkedve levegő után kapni;egy automata pórázt tartani;megkocogtatni a homlokát|sál;ereszcsatorna;tulipánok;corgik|Mit csinál a férfi?|Megkocogtatja a homlokát.
7085|felhúzni a redőnyt;sorban állni az esőben;gőzölögni|redőny;vállalkozó;állólétra;bárszék|Mit csinál a nő?|Felhúzza a redőnyt.
7086|beleengedni az alvadékot a kádba;savótól csöpögni;egy mérőkanalat tartani|sajtformák;alvadéktömb;rézkád;sajtkendő|Mi csöpög az alvadékból?|Savó csöpög az alvadékból.
7087|egy köteg levelet vinni;a libák mögött ügetni;a kőfalon ücsörögni|quad;macska;collie;liba|Mit csinálnak a libák?|A libák kísérik a nőt.
7089|nekifeszülni egy óriási szivacsnak;a nő fölé tornyosulni;a telefonjával filmezni|napellenző;faláda;hordó;macskakövek|Mit csinál az elefánt alakú szivacs?|Az elefánt alakú szivacs egyre nagyobbra duzzad.
7090|szélesre tárni a karját;mezítláb állni egy sziklán;beárnyékolni a szemét|vízesés;fürdőruha;moha;szikla|Mit csinál a nő?|Szélesre tárja a karját.
7091|vezetni a versenyt;az élen haladó mögött lemaradni;kinyújtani a karját|nyárfák;sisak;nézők;szénabálák|Mit csinál az elöl haladó kerékpáros?|Vezeti a versenyt.
7092|egy fekete kendőt tartani;rávigyorogni a szoborra;elolvadni a tűző napon|jégszobor;simlis sapka;mellény;turista|Mit csinál a fiatalember?|Rávigyorog az olvadó szoborra.
7093|lesütni a szemét;lehunyni a szemét;a magasba tartani egy esernyőt|ponyva;statiszta;esernyő;macskakövek|Mit csinál az elöl álló nő?|Statiszták sorában áll.
7094|kirántani a csizmáját;egy sáros pocsolyában landolni;láthatósági mellényt viselni|rendező;sátor;pocsolya;halászsapka|Mit csinál a nő?|Kirántja a csizmáját a sárból.
7095|elkorcsolyázni a koronggal;piros mezt viselni;a nézők között ülni|lámpás;kutya;dob;hókupac|Mit csinál a kék mezes játékos?|Elkorcsolyázik a koronggal.
7096|eltakarni az arcát;a volánnál ülni;egy papírlapot tartani|házak;szökőkút;papírlap;autó|Mit csinál a nő?|Eltakarja az arcát.
7097|dörzsölni a mellszobor arcát;kételkedve összeráncolni a homlokát;írni egy írótáblára|laborköpeny;mellszobor;tégely;fültisztító pálcikák|Mit csinál az elöl álló nő?|Egy fültisztító pálcikával dörzsöli a mellszobrot.
7099|hangversenyzongorán játszani;egy mély szurdokba zuhanni;kék esőponcsót viselni|vízesés;szivárvány;korlát;hangversenyzongora|Mit csinál a fiatalember?|Hangversenyzongorán játszik.
7100|rögtönzött vitorlát készíteni;a fókát nézni;kidugni a fejét|vitorla;jéghegy;fóka;tengeri kajak|Mit csinál a nő?|Rögtönzött vitorlát készít.
7101|odaadni neki az ételt;magasba emelni a zacskót;nevetni örömében|gyorskaja;bukósisak;kutya;robogó|Mit tart a nő?|Egy zacskó gyorskaját tart.
7102|sisteregni a forró zsírban;a tűzhelyre csöpögni;egy vágódeszkán pihenni|zsír;öntöttvas serpenyő;fakanalak;bárd|Mi csöpög a tűzhelyre?|Olvadt zsír csöpög a tűzhelyre.
7103|tortát tartani;a hátsó lábain állni;rózsaszín inget viselni|lámpa;torta;asztal;kutya|Mit csinál a nagy kutya?|A hátsó lábain áll.
7104|egy szürke lovon lovagolni;buborékot fújni;vezetni a szürke lovat|ég;fák;tömeg;ló|Mit csinál a zöld ruhás férfi?|Egy szürke lovon lovagol.
7105|felfelé emelni az állát;aranyfüstöt felvinni;pelyheket fújni a levegőbe|estélyi ruha;ruhaállvány;hajszárító;sminkecset|Mit csinál a modell?|Felfelé emeli az állát.
7106|kapaszkodni a korlátba;nagyra tátani a száját;megérinteni a mellkasát|ég;tenger;férfi;kötél|Mit csinál a férfi?|Kapaszkodik a korlátba.
7107|elkapni a hulló hópelyheket;hátrahajtani a fejét;szorosan lehunyni a szemét|domboldal;lávakövek;hőforrás;fürdőruha|Mit csinál a nő?|A kezével kapja el a hulló hópelyheket.
7108|valakinek a vállán ülni;megtartani a barátnője súlyát;könnyekig meghatódni|épületek;sál;farmerdzseki;kartontábla|Mit csinál a felül ülő nő?|A barátnője vállán ül.
7110|visszaverni a nőket;az ágyon térdelni;nyugodtan ülni a padlón|ágytámla;éjjeli lámpa;fényfüzérek;kutya|Mit csinál a férfi?|Egy párnával veri vissza a nőket.
7111|ütést bevinni;piros sortot viselni;körbejárni a ringet|bokszoló;vezetőbíró;emberek;lámpa|Mit csinál a vezetőbíró?|Körbejárja a ringet.
7112|egy apró figurát festeni;egy sámlin szunyókálni;meleg fényt árasztani|figura;asztali lámpa;üvegbura;macska|Mit csinál a fiatalember?|Egy apró figurát fest.
7113|kitölteni egy űrlapot;sárga dzsekit viselni;mutatni az időt|óra;dzseki;űrlap;gép|Mit csinál a sárga ruhás nő?|Kitölt egy űrlapot.
7114|felemelni egy fémkeretet;szivárványszínekben csillogni;mérni a szélsebességet|felhőkarcolók;víztorony;szappanhártya;vályú|Mit csinál a sárga ruhás nő?|Egy nagy fémkeretet emel fel.
7116|lecsúszni egy sárgaréz rúdon;kihajtani a tűzoltóságról;a harangtoronyban lógni|tűzoltóság;harang;ég;hó|Mit csinál a tűzoltóautó?|Kihajt a tűzoltóságról.
7117|elevezni az ajtótól;sárga esőkabátot viselni;kihajolni az ablakokon|evezős csónak;árvíz;kanapé;ég|Mit csinál a sárga ruhás nő?|Elevez az ajtótól.
7118|a feje fölé emelni a csellóját;mélyen meghajolni a csellója fölött;tapsolni a karmesteri emelvényről|cselló;karmester;csellótok;vonó|Mit csinál a karmester?|A karmesteri emelvényről tapsol.
7120|a tetőn állni;egy piros deszkán feküdni;esernyőt tartani|busz;esernyő;szerszámok;út|Mit csinálnak a kutyák?|A kutyák egy régi buszt javítanak.
7121|erős fénysugarat kibocsátani;a sziklákhoz csapódni;feltekerve feküdni a mólón|világítótorony;szirt;sziklák;kötél|Mit csinál a világítótorony?|A világítótorony villog a viharban.
7122|a vízben futni;a víz fölött repülni;beborítani az eget|ég;lovak;víz;fű|Mit csinálnak a lovak?|A vízben futnak.
7123|felnyitni egy egész lazacot;simára igazítani a húst;a pultra támaszkodni|kés;gumikesztyű;hús;halfej|Mit csinál a nő?|Simára igazítja az élénk narancssárga húst.
7125|elkapni egy pénzérmét a levegőben;a zongorának támaszkodni;integetni egy kapualjból|pénzérme;erkély;zongora;hevederek|Mit csinál a fiatal nő?|Feldob egy pénzérmét.
7127|átvenni egy zacskó kenyeret;felnyúlni az ablakig;felnézni a kenyérre|labda;almák;csónak;kutya|Mi van az utcán?|Árvíz van az utcán.
7129|a zongora mellett állni;a levegőben lógni;ruhát vasalni|ég;zongora;épület|Hol van a zongora?|A zongora a levegőben lóg.
7131|egy medencében állni;feltartani egy nagy tortát;fehér ruhát viselni|medence;flamingó;torta;menyasszony|Mit csinál a napszemüveges férfi?|Egy medencében áll.
7132|büszkén megmutatni a felvételét;a mezők fölé tornyosulni;a kamera kijelzőjére mutatni|tornádó;pickup;felvétel;esőkabát|Mit mutat a sárga ruhás nő?|A tornádóról készült felvételt mutatja.
7134|elkapni a labdát;futni a labdával;kék dzsekit viselni|ég;labda;futballista;fű|Mit csinál a fehér mezes játékos?|Két kézzel elkapja a labdát.
7135|megmarkolni egy piros kart;táblagéppel filmezni;a görögdinnyékbe csapódni|daru;bontógolyó;táblagép;görögdinnyék|Mit csinál a göndör hajú férfi?|Egy piros kart markol.
7136|átdübörögni a folyón;kézen fogva átgázolni;az égbe gomolyogni|gleccser;sátor;túrázók;terepjáró|Mit csinálnak a túrázók?|Kézen fogva gázolnak át a folyón.
7137|átkelni egy sekély folyón;a gázlóköveken várni;a túlpartról figyelni|birkák;facölöp;gázlókövek;gumicsizma|Mit csinál a terepjáró?|Átkel egy sekély folyón.
7138|átcsapni a vastag falakon;alakzatban állni;ringatózni a viharos tengeren|napsugár;füst;katonák;erőd|Mit csinál a hatalmas hullám?|Átcsap a vastag falakon.
7139|szélesre tárni a karját;feltartani egy halat;a hajó fölött repülni|háló;ég;hajó;halak|Mit csinál a nő?|Rengeteg hal között áll.
7140|beszédet mondani a tömegnek;gesztikulálni a székéből;karba tenni a kezét|utcai lámpa;makett;párna;dokumentumok|Mit csinál a fiatal nő?|Beszédet mond a tömegnek a téren.
7141|felpróbálni egy szemüveget;nevetni a szemüvegén;egy íróasztalnál dolgozni|szemüvegkeretek;ablak;szekrény;pult|Mit csinál a nő?|Nevet a szemüvegén.
7142|megigazítani egy díszes keretet;elragadtatva tapsolni;érett citromokat ábrázolni|gérvágó fűrész;keret;befőttesüveg;munkapad|Mit csinál az idős férfi?|Elragadtatva tapsol.
7143|izgatottan vigyorogni;besietni a szobába;egy minihűtőt gurítani|elsőéves;kartondoboz;matrac;hűtő|Mit visz az elsőéves?|Egy kartondobozt visz.
7144|kiüríteni egy sütőkosarat;felszolgálni a sült krumplit;a sült krumpli után nyúlni|villanykörték;bandana;sült krumpli;olajsütő|Mit csinál a szakács?|Felszolgálja a sült krumplit egy vendégnek.
7146|egy kikötőkötelet tartani;a rakparton kóborolni;ringatózni a hullámokon|teherhajó;horgony;halászhajó;német juhászkutya|Mit tart a munkás?|Egy kikötőkötelet tart.
7147|a tábortűz mellett guggolni;elkapni egy serpenyőt a levegőben;átsétálni a homokon|serpenyő;palacsinta;keverőtál;tábortűz|Mit kap el a férfi?|Egy serpenyőt kap el a levegőben.
7148|görkorcsolyázni a verandán;szélesre tárni a karját;a padlódeszkákon feküdni|mennyezeti ventilátor;páfrány;kutya;galéria|Mit csinál a nő?|Görkorcsolyázik a verandán.
7149|megtankolni egy sáros autót;levenni a bukósisakját;csupa sárnak lenni|benzinkút;porvihar;raliautó;ördögszekér|Mit csinál a benzinkutas?|Megtankol egy sáros raliautót.
7150|megtankolni egy aggregátort;kikukucskálni egy ablakon;világítani az aggregátoron|benzineskanna;benzin;lámpás;aggregátor|Mit tölt a férfi?|Benzint tölt egy tölcsérbe.
7153|guggolni a színpadon;kezelni a ködgépet;sűrű ködöt pumpálni|világítási állvány;dobfelszerelés;ködgép;palack|Mit csinál a nő?|Egy ködgép mellett guggol.
7155|átmászni a falon;a fogai között tartani a szandálját;a gyepről figyelni|ég;borostyán;szatén ruha;vendégek|Mit csinál az ezüst ruhás nő?|Átmászik egy borostyánnal benőtt falon.
7156|lenyelni egy hot dogot;vizet önteni egy kancsóból;felfújni az arcát|zászlófüzér;grill;üvegtál;hot dogok|Mit csinál a sortos nő?|Vizet önt egy kancsóból.
7157|felvenni egy kabátot;lecsúszni egy rúdon;fekete foltosnak lenni|tűzoltóautó;kabát;kutya;rúd|Mit csinál a nő?|Öltözködik a tűzoltóságon.
7158|teli torokból énekelni egy dalt;lehuppanni a kanapéra;befogni a fülét|partisapka;mikrofon;sörösüveg;csörgődob|Mit csinál az énekesnő?|Teli torokból énekel egy karaokedalt.
7159|esernyőt tartani;kulccsal kinyitni a bejárati ajtót;felnézni a nőre|esernyő;kutya;bevásárlószatyrok;ajtó|Mit csinál a nő?|Kulccsal kinyitja a bejárati ajtót.
7160|térképet nézni;az utca vége felé mutatni;a földön ülni|kalap;ajtó;bőrönd;macska|Mit csinál a turista?|Térképet néz.
7161|magasra emelni egy kiskutyát;átnyúlni az asztalon;megszaglászni a félig megevett tortát|fényfüzérek;fonott kosár;torta;mancsnyomok|Mit csinál a mezítlábas nő?|Kiemel egy kiskutyát a kosárból.
7162|magához ölelni egy köteg gyapjút;seprűvel hadonászni;a karámok felé ügetni|gyapjú;seprű;birka;padlódeszkák|Mit csinál a nő?|Egy köteg gyapjút ölel magához.
7163|egy zsebkendőbe tüsszenteni;feljebb húzni a sálját;könyvet olvasni|kesztyűk;könyv;kenyér;táska|Mit csinál a fehér ruhás nő?|Egy zsebkendőbe tüsszent.
7164|szánkót húzni;a szánkóban utazni;pórázon sétálni|ház;fák;szánkó;kesztyű|Mit húz a nő?|Egy kutyákkal teli szánkót húz.
7166|fellépni a csúcsra;egyensúlyozni a gerincen;megigazítani a védőszemüvegét|védőszemüveg;felhők;jégcsákány;kötél|Hol áll a hegymászó?|A havas csúcson áll.
7167|egy felfújható flamingót vonszolni;szélesre tárni a karját;megölelni a csuromvizes kutyát|felfújható flamingó;golden retriever;kötött pulóver;nedves homok|Mit csinál a kutya?|A kutya egy felfújható flamingót vonszol.
7168|nyitva tartani az ajtót;beszállni az anyósülésre;égő fényszórókkal állni|templomtorony;veterán autó;szalag;szirmok|Mit csinál a férfi?|Nyitva tartja neki az ajtót.
7169|a medencében térdelni;a medence fölé hajolni;egy kis zseblámpát tartani|fényfüzérek;szülőlabda;orvosi táska;szülőmedence|Mit csinál a várandós nő?|Egy szülőmedencében térdel.
7170|a völgy fölött szárnyalni;libasorban haladni;a hegyoldalon állni|szivárvány;völgy;patak;marhák|Mit csinálnak a marhák?|Libasorban haladnak.
7172|felragasztani egy apró alkatrészt;felugrani örömében;összekulcsolt kézzel figyelni|templom;házikó;ragasztótubus|Mit csinál a sárga ruhás nő?|Egy apró alkatrészt ragaszt egy házikóra.
7173|ragasztópisztolyt tartani;feldíszíteni egy régi csónakot;egy kagylót vinni|evezős csónak;ragasztópisztoly;láda;sirály|Mit csinál a nő?|Kagylókat ragaszt egy régi csónakra.
7174|nagy hátizsákot vinni;átölelni egymást;a padlón ülni|hajó;útlevél;hátizsák;padló|Mit csinál a pár?|Átölelik egymást.
7175|belenyúlni a patakba;megmarkolni egy mohás gyökeret;megszagolni a vizet|lámpás;ültetőkanál;patak;lehullott levelek|Mit mutat a nagy kutyának?|Egy sötét rögöt mutat a nagy kutyának.
7176|levenni a kalapját;nyakörvet viselni;egy tyúkot tartani|kecske;kalap;kosár;ablak|Mit csinál a fiatal nő?|Leveszi a kalapját.
7177|kötélen leereszkedni egy sziklafalon;megmarkolni a kötelet;hátradőlni a beülőjében|sisak;vízesés;sziklafal;medence|Mit csinál a nő?|Kötélen ereszkedik le egy sziklafalon.
7178|elkapni a leeső papírokat;egy írótáblát tartani;a recepción ülni|írótábla;blézer;nyakkendő|Mit tart a szemüveges nő?|Egy írótáblát tart.
7182|vinni a forró ételt;egy csónakban ülni;összetenni a kezét|ég;házak;asztal;víz|Mit visz a fiatalember?|A vacsorát viszi az asztalhoz.
7183|egy kirakatra mutatni;bevásárlószatyrokat vinni;biciklizni|esernyő;póni;bicikli;kirakat|Mit csinál a sárga ruhás nő?|Egy pónival megy vásárolni.
7184|zöld pólót viselni;a férfi mögött ülni;elrepülni|templom;bicikli;galamb;fagylalt|Mit csinál a férfi és a nő?|Biciklivel városnéznek.
7185|átugrani a detektoron;írni egy írótáblára;felkapni a bokacsizmáját|fémdetektor;bokacsizma;farmerdzseki;ananász|Mit csinál a zoknis nő?|Átugrik a fémdetektoron.
7186|felmászni az ágyra;megvilágítani az ágyat;magára húzni a takarót|ég;lámpa;ágy;takaró|Mit csinál a nő?|A fák között fekszik le aludni.
7187|elaludni;elejteni egy könyvet;egy függőágyban feküdni|fák;férfi;könyv;kötél|Mit csinál a férfi?|Elalszik egy függőágyban.
7188|a jég alatt siklani;felfelé nyújtani az egyik karját;fekete búvárruhát viselni|jéghegy;napsugarak;buborékok;búvár|Mit csinál a búvár?|A jég alatt siklik.
7191|felkapni egy kávét;átnyújtani egy csészét;izgatottan felugrani|napellenző;kávéfőző;felhők;kutya|Mit csinál a siklóernyős?|Felkap egy kávét a bódénál.
7192|felpattanni;feltartani egy diplomát;a levegőbe bokszolni|diploma;lufik;végzős;pódium|Mit csinál a végzős?|Egy diplomát tart a feje fölé.
7194|egy lepkés nyomatot tartani;kisimítani a lapot;egy állólétrán állni|grafikák;ablak;állólétra;ecsetek|Mit csinál az elöl álló nő?|Egy lepkés nyomatot tűz ki a helyére.'''
out={}
for line in R.strip().split('\n'):
    i,p,n,q,a=line.split('|')
    out[i]={'phrases':p.split(';'),'nouns':n.split(';'),'question':q,'answer':a}
src=json.load(open(f'{H}/source.json'))
out={k:out[k] for k in src}
json.dump(out,open(f'{H}/hu.json','w'),ensure_ascii=False,indent=1)
