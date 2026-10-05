import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = """
620|egy rózsaszín rózsát szagolni;becsukni a szemét;ragyogni az égen|nő;rózsa;kosár;nap|Mit csinál a nő?|Egy rózsaszín rózsát szagol.
5310|átölelni a fiút;szürke pólót viselni;elrepülni a garázs előtt|fiú;labda;férfi|Mit csinál a nő?|Átöleli a fiút.
41|egy kalapácsot tartani;fekete hajúnak lenni;a falon lógni|kép;kalapács;nő;férfi|Mit csinál a férfi és a nő?|Veszekednek.
5499|piros ruhát viselni;végigfutni az utcán;locsolni a virágokat|nő;virágok;ablak;fal|Mit csinál az idős nő?|A virágokat locsolja.
119|meleg fényt adni;egy csészét tartani;szürke bundájúnak lenni|villanykörte;macska;tál;könyvek|Mit tart a nő?|Egy csészét tart.
166|egy nagy kört rajzolni;egy hosszú botot tartani;körben állni|nő;ég;kör;tenger|Mit rajzol a nő?|Egy kört rajzol a homokba.
596|megnyerni a versenyt;sárga felsőt viselni;lila felsőt viselni|futók;fű;futópálya|Ki nyeri a versenyt?|A sárga ruhás futó nyeri a versenyt.
484|tisztítani a padlót;majdnem elesni;tele lenni vízzel|nő;felmosó;vödör;padló|Mit csinál a nő?|A padlót tisztítja egy felmosóval.
68|a kamerába mosolyogni;szemüveget viselni;a keze köré tekeredni|szemüveg;hüvelykujj;kötés;pad|Mit csinál a férfi?|Kötést tesz a nő kezére.
5149|egy papírzacskót vinni;felmászni egy magas létrára;élénkzölden világítani|kereszt;üvegek;sál;doboz|Mit csinál a fehér ruhás férfi?|Egy magas létrára mászik fel.
457|becsukni a szemét;zöld felsőt viselni;a nők mögött feküdni|lámpa;tükör;kutya;smink|Hol fekszik a kutya?|A kutya a nők mögött fekszik.
36|ölelgetni a vörös macskáját;a levegőben lógni;felkapni a házi kedvencét|virágcserép;macska;párna;kardigán|Mit csinál a nő?|A macskát ölelgeti, amelyet imád.
676|fényképezni a látnivalókat;kormányozni a gondolát;a tér fölé magasodni|harangtorony;kupola;fényképezőgép;gondola|Mit csinál a két turista?|Városnézésen vannak egy gondolában.
7962|tartani a kartondobozt;tartalmazni a maradék pizzát;a háztető fölött lógni|fényfüzérek;kémény;pizzásdoboz;szőnyeg|Mit tartalmaz a pizzásdoboz?|A pizza maradékát tartalmazza.
7858|egy slackline-on egyensúlyozni;beárnyékolni a szemét;integetni a szirtről|ég;szirt;folyó;polárpulóver|Hol egyensúlyoz a narancssárga ruhás nő?|Félúton egyensúlyoz a szurdok fölött.
7124|lemenni a kőlépcsőkön;éljenezni az erkélyről;egy tálcán nyugodni|vendégek;esküvői torta;szmoking;lépcső|Min megy le a fiatal férfi?|Egy kőlépcsősoron megy le.
6849|lemenni a kőlépcsőkön;egy kenyereskosarat szorongatni;egy kerékpárba kapaszkodni|gépkocsi;kosár;kiteregetett ruhák;macskakövek|Mit csinál a piros gépkocsi?|A gépkocsi a kőlépcsőkön megy le.
4206|ásítani az íróasztalnál;friss kávét adagolni;élénkzölden világítani|belépőkártya;óra;irodai szék;papírmunka|Mi lóg a hörcsög nyakában?|Egy belépőkártya lóg a nyakában.
234|feloldódni a vízben;egy kanállal kavarni;beleejteni egy kockacukrot|kanál;kötény;pohár;kockacukor|Mi történik a kockacukorral?|A kockacukor éppen feloldódik a vízben.
5273|nagy léptekkel végigmenni a kifutón;megigazítani a napszemüvegét;büszkén mutogatni a dzsekijét|modell;nézők;kifutó;mennyezet|Mit csinál a modell?|Nagy léptekkel megy végig a kifutón.
7835|lefelé ömleni a lejtőn;izzani a csúcson;a horizont fölött lebegni|lávafolyam;kráter;fák;felhő|Mi történik a vulkánon?|Egy lávafolyam ömlik lefelé a lejtőn.
8032|előrenyújtani a kalapját;ijedtében hátraugrani;megragadni a barátnője karját|óratorony;szökőkút;galambok;szoknya|Mit csinál a bronzszínű férfi?|Egy nőnek kínálja a kalapját.
278|a fák koronája fölé emelkedni;hosszú hajfonatot viselni;sötétzöld leggingset viselni|nap;pálmafa;hajfonat;pázsit|Milyen gyakorlatot végez a csoport?|Guggolásokat végeznek a pázsiton.
93|körbepörgetni a gyümölcsöt;lenyalni az ujját;feltartani a hüvelykujját|turmixgép;kancsó;eprek;fejpánt|Mit készít a férfi?|Turmixot készít egy turmixgépben.
7239|egy habos italt kortyolgatni;vízhatlan dzsekit viselni;a fejének nyomódni|kefe;kutya;papírpohár;szélvédő|Mit csinál a férfi?|Egy habos italt kortyolgat.
5712|a bizonyítékra mutatni;elejteni egy különálló papírlapot;egy állványon állni|ügyvéd;kerékpár;sár;kartondobozok|Mit csinál az ügyvéd?|A sáros kerékpárra mutat.
406|egy nehéz kalapácsot lendíteni;felerősíteni egy vasspirált;hegyes tüskékkel rendelkezni|üllő;vasrúd;védőszemüveg;ablak|Mit csinál a kovács?|Forró vasat kalapál egy üllőn.
378|egy korláton ülni;a háztetők fölött szárnyalni;hosszú, aranyló sugarakat vetni|madár;ég;háztetők|Mit csinál a madár?|Napkeltekor a háztetők fölött szárnyal.
6|dörzsölni a fájó hátát;feltartani a hüvelykujját;magasra tornyosulni|szakáll;kardigán;virágcserép;párna|Mit csinál a férfi?|Párnákat halmoz az ölébe.
7946|kiüríteni a postaládát;egy postazsákot vinni;kidugni a fejét|fák;postaláda;furgon;zsák|Mit csinál a fekete kutya?|A piros postaládát üríti ki.
7932|a gyűrűn lógni;sötétkék mezt viselni;felemelt karral éljenezni|kosárlabda;háló;atlétatrikó|Mit csinál a fehér ruhás férfi?|A gyűrűn lóg.
7996|egyértelműen kitűnni;forogni a szellőben;a korlátnak dőlni|fák;szélmalom;kerékpár;tulipánok|Melyik tulipán tűnik ki a mezőn?|A piros tulipán tűnik ki a mezőn.
4209|egy laptopon gépelni;mélyen aludva feküdni;a kamerába pillantani|tulipán;laptop;arcmaszk;kézitáska|Mit csinál a maszkos hörcsög?|Alszik egy kicsit arcmaszkban.
7844|a tűzhely felé fordulni;galléros inget viselni;az ablak fölött lógni|rézserpenyők;keverőtál;palacsinták;konyhapult|Ki forgat palacsintákat?|Nők két nemzedéke forgat palacsintákat.
4156|a mellkasán állni;a robot után vetődni;előrenyújtani mindkét kezét|sövény;kerítés;robot;pázsit|Mit csinál a robot eleinte?|Az ösvényen közeledik a kamerához.
8036|a falhoz préselődni;betölteni az egész szobát;egy cserépből lecsüngeni|tetőablak;lámpaernyő;flamingó;padlódeszkák|Mit csinál a flamingó?|Betölti a szoba teljes térfogatát.
515|megmászni egy mászófalat;egy kötélen lógni;lentről éljenezni|ablak;mászófal;falmászó;nézők|Mit csinál a nő?|Egy mászófalat mászik meg.
673|megpakolni a mosógépet;hitetlenkedve bámulni;összemenni a mosásban|szeplők;pulóver;kantáros nadrág;mosógép|Mi történt a pulóverrel?|A pulóver összement a mosógépben.
5458|felhajtani az italt;pezsegni és narancssárgává válni;vitaminos címkével rendelkezni|konyhaszekrény;vitamintabletta;gyümölcsöstál;pohár|Mit ejt a pohárba?|Egy vitamintablettát ejt bele.
343|megragadni egy búvárkarikát;az alján feküdni;sekély vízben gázolni|lépcsők;búvárkarika;búvármaszk;fürdőruha|Mit ragad meg a nő a víz alatt?|Egy búvárkarikát ragad meg.
5594|egy hegygerincen ülni;összecsukni a bőrszerű szárnyait;lehajtani a szarvas fejét|csúcsok;felhők;sárkány;fenyőfák|Mit csinál a sárkány?|A lenyűgöző sárkány egy hegygerincen ül.
94|egy könnycseppet ejteni;összeszorítani a fogát;diadalittasan vigyorogni|napszemüveg;karika fülbevaló;tejturmixok;autókulcsok|Mit próbál elkerülni a férfi?|A pislogást próbálja elkerülni.
7981|beleharapni egy eperbe;feltűrt ingujjat viselni;egy epret kínálni|napellenző;fagylaltkehely;kancsó|Mit csinál a három barát?|Egy fagylaltkelyhen osztoznak.
7145|visszahúzódni az ajtó mögé;ráhorkantani a férfira;elsétálni a tejesüvegek mellett|bejárati ajtó;fürdőköpeny;tejesüvegek;macskakövek|Mit csinál a férfi?|Visszahúzódik a bejárati ajtaja mögé.
70|egy sűrű szakállt nyírni;megcsodálni az új frizuráját;visszatükrözni az elragadtatott arcát|borbély;vendég;kézitükör;üvegek|Mit csinál a borbély?|A vendég sűrű szakállát nyírja.
747|a fejét fogni;az íróasztal fölé tornyosulni;az időt mutatni|bögre;csipeszes írótábla;papírmunka;óra|Mit csinál a nő?|A fejét fogja az íróasztalánál.
7870|megnyalni a szája szélét;a villáról lelógni;a fán világítani|kutya;spagetti;karkötő;kőfal|Mit csinál a kutya?|A lelógó spagettit bámulja.
7016|megveregetni egy tehén hátát;a kerítés mentén sétálni;libasorban menni|kapu;pajta;tejeskannák;tehenek|Mit csinál a nő?|Egy tejelő tehén hátát veregeti meg.
8001|kitárni a szárnyait;elkerékpározni a liba mellett;a fűre ugrani|liba;kerékpár;borostyán;kavicsos ösvény|Mit csinál a rövidnadrágos nő?|Távol tartja magát a libától.
7744|a vízbe csapódni;egy evezőt markolni;ijedtében levegő után kapni|bálna;csónakház;evező;mentőmellény|Mit csinál a bálna?|A vízbe csapódik.
6820|simogatni a borjú hátát;a felnőtt mellett ügetni;felemelni a rövid ormányát|felnőtt;akáciafa;agyarak;borjú|Mit csinál a felnőtt elefánt?|A borjú hátát simogatja.
4222|a kamerába integetni;összefonni a karját;a lencse felé hajolni|szemek;nyelv;has;farok|Mit csinál a gekkó?|A kamerába integet.
7845|finoman megemelni a kosarat;markolni a fonott kosarat;végigszáguldani a füvön|hőlégballon;fonott kosár;kutya;fű|Mit csinál a kék ruhás nő?|Egy fonott kosárban utazik.
7563|egy motorkerékpárt kormányozni;az oldalkocsiban ülni;a kapunál éljenezni|vidéki házikó;kapu;hálózsák;kavics|Mit csinál a motoros?|Útnak indul egy motorkerékpáron.
5053|egy poggyászcímkét rögzíteni;egy bőröndről lógni;szállítani a poggyászt|szemüveg;fejkendő;címke;bőrönd|Mit csinál a nő?|Egy címkét rögzít a bőröndjére.
8000|a pultra támaszkodni;a kutyára vigyorogni;egy nehéz bőröndöt vonszolni|csillár;oszlop;bőrönd;recepciós pult|Mit csinál a kutya?|A kutya a márványpultra támaszkodik.
98|az elképedéstől levegő után kapni;szorosan behunyni a szemét;bordó borítójúnak lenni|függőágy;kupola;hajfonat;virágok|Mit csinál a nő?|Egy könyvet olvas egy függőágyban.
5272|a társára mutatni;bozontos szakállúnak lenni;széles karimájú kalapot viselni|túrázó;hátizsák;kanyon;korlát|Mit csinálnak a túrázók?|A túrázók a kanyon fölött éljeneznek.
4424|átlépni egy festett csíkot;a kamerába vigyorogni;benyúlni egy ablakon|útlevél;fülke;korlát;kötött sapka|Mit csinál az utazó?|Gyalog kel át a határon.
4408|felhajtani egy turmixot;feltartani a hüvelykujját;tele lenni gyümölccsel|turmixgép;spenót;turmix;bajusz|Mit csinál a férfi?|Egy friss gyümölcsturmixot kóstol.
5636|a pult fölé hajolni;nevetésben kitörni;egy ostyatölcsért tartani|csillár;vitrin;kötény;fagylalt|Mit csinál a vásárló nő?|A fagylaltpult fölé hajol.
8028|a halomra mutatni;eltakarni az arcát;a pult fölé tornyosulni|lampion;fejpánt;tányérok;evőpálcikák|Mit csinál a séf?|A tányérhalomra mutat.
637|kinyílni, mint egy virág;egy kupacban heverni;zöld dombok fölött elnyúlni|ég;kés;hüvelykujj;gránátalma|Mi történik a gránátalmával?|Kinyílik, mint egy virág.
7739|egy sajtkorongot gurítani;egy kalapáccsal kopogtatni;felmászni a létrán|lámpás;ablak;létra;vödör|Mit gurít az egér?|Egy nehéz sajtkorongot gurít.
7813|felfordított vödrökön dobolni;rózsaszín pulóvert viselni;visszatükrözni a felhős eget|esernyők;szökőkút;vödrök;pocsolya|Mit csinál a duó?|A duó kék vödrökön dobol.
7997|főszerepet játszani egy előadásban;fél térden térdelni;magas sarkú cipőben táncolni|függönyök;reflektor;estélyi ruha;rivaldalámpák|Mit csinál az aranyruhás nő?|Főszerepet játszik egy előadásban.
7748|egy sárkányszobrot festeni;a kávéja fölött ásítani;egy kék párnán szundikálni|sárkány;festékesdobozok;pizzásdoboz;takaró|Mit csinál a kantáros nadrágos nő?|Egy sárkányszobrot fest.
7450|egy magas vázát formázni;benyúlni a vázába;a háttérben dolgozni|égetőkemence;fazekas;váza;szivacs|Mit csinál az elöl lévő fazekas?|Egy magas agyagvázát formáz.
7040|végiggurulni a táblán;a fejét fogni;eldobni egy dobókockát|dobókocka;popcorn;társasjáték;nyakláncok|Mi gurul végig a táblán?|Egy fehér dobókocka gurul végig a táblán.
5517|elfogadni egy házassági ajánlatot;egy takarón térdelni;egy horgászbotot vinni|gyűrűsdoboz;piknikkosár;takaró;lábnyomok|Mit csinál a nő?|Elfogadja a férfi házassági ajánlatát.
4125|egy leplet rángatni;szirmokká szétrobbanni;felemelni az ormányát|reflektor;elefánt;öltöny;színpad|Mit csinál a szürke elefánt?|Az ormányát emeli fel a színpadon.
347|egy kis pletykát suttogni;a keze mögött levegő után kapni;csíkos inget viselni|napellenző;göndör haj;hajfonat;asztal|Mit csinál a szemüveges nő?|Egy kis pletykát suttog a férfi fülébe.
7849|a háztető fölött lógni;a horizonton magasodni;egy deszkán nyugodni|fényfüzérek;hegy;pizza;kancsó|Mit csinálnak a barátok?|Egy pizzán osztoznak egy háztetőn.
4920|locsolni a palántákat;színes csíkosnak lenni;a tömeg fölé emelkedni|ég;tábla;fiú;magaságyás|Mit csinál a szőke nő?|A palántákat locsolja a közösségi kertben.
4434|egy plüssmacit ölelgetni;egy fagylaltot nyalni;kibújni a dzsekijéből|ég;vidámpark;fagylalttölcsér;plüssmaci|Mit csinál a vidámparkban?|Egy óriási plüssmacit ölelget.
7154|egy egykerekűn egyensúlyozni;egy elviteles kávét kortyolgatni;az egykerekű mögött tekerni|emeletes busz;taxi;aktatáska;egykerekű|Hogyan közlekedik az üzletember?|Egykerekűn halad a forgalomban.
5417|felszállni egy nosztalgiavillamosra;felvenni egy utast;körülnézni a remízben|felsővezetékek;sínek;vászontáska;hajfonat|Mit csinál a végén?|Körülnéz a villamosremízben.
4918|felrohanni a lépcsőn;nehéz szatyrokkal küszködni;feltartani a hüvelykujját|lépcső;kapucnis pulóver;farmernadrág;papírzacskó|Mit visz a fiatal férfi?|Papírzacskókat visz fel a lépcsőn.
7369|egy bálna körül evezni;párás vízsugarat fújni;felemelni a farkát|SUP-deszka;bálna;csónak;hegyek|Mit csinál a nő?|A nagy bálna körül mozog.
5502|kartondobozokat egymásra rakni;egy megrakott raklapot vinni;dobozokat fóliába csomagolni|kartondobozok;raklapemelő kocsi;láthatósági mellény;polcok|Mit csinál a nő?|Kartondobozokat rak egymásra egy raklapon.
730|letörölni a konyhapultot;leteríteni egy abroszt;felszolgálni egy cappuccinót|személyzet;vendégek;abrosz;függőlámpák|Mit csinál a pincérnő?|Egy fehér abroszt terít le.
230|diadalmasan felemelni az ökleit;kalózjelmezt viselni;egy háromlábú állványon állni|rendező;filmkamera;összecsukható szék;nap|Mit csinál a rendező?|Diadalmasan emeli fel az ökleit.
7119|felhúzni egy nehéz hálót;sárga esőruhát viselni;ezüstös halaktól duzzadni|sirály;háló;láda;halász|Mit csinál a narancssárga ruhás halász?|Egy nehéz hálót húz fel.
4930|lelkesen felemelni a kezét;büszkén mutogatni a füzetét;csillogni a lapon|aranycsillag;spirálfüzet;fehér tábla|Milyen jutalmat kap a lány?|Egy aranycsillagot kap.
5358|egy résen át kukucskálni;nehéz könyveket egymásra rakni;a kezére támaszkodni|könyvespolcok;szemüveg;kardigán;tankönyv|Mit csinál az elrejtőzött nő?|A könyvek közötti résen át kukucskál.
7|felemelni a diplomáját;a kamerába vigyorogni;átölelni egy másik végzőst|diploma;stadion;diplomaosztó sapka;vállszalag|Mit csinál a férfi?|A diplomáját emeli fel a diplomaosztóján.
4360|belenézni egy táskába;több bevásárlótáskát vinni;büszkén mutogatni a kézitáskáját|papírtáskák;kézitáska;utazótáska;mozgólépcső|Mit mutogat büszkén a nő?|A kézitáskáját mutogatja büszkén egy mozgólépcsőn.
5379|levenni egy ügyfél méreteit;krétával megjelölni a szövetet;belebújni egy zakóba|mennyezeti ventilátor;szövet;zakó;mérőszalag|Mit csinál a szabó?|Egy zakót igazít át egy ügyfélnek.
798|behúzni egy dzseki cipzárját;locsolni a cserepes növényeket;sűrű bajuszúnak lenni|kiteregetett ruhák;robogó;melegítő;locsolókanna|Mit csinál a fiatal nő?|Türkizkék melegítőben táncol.
7200|egy siklóernyőt irányítani;felfelé emelni a pilótát;lobogni a szellőben|siklóernyő;szélzsák;öböl;sziklapárkány|Mit csinál a pilóta?|Egy türkizkék öböl fölött siklik.
376|végigrohanni a szurdokon;a sziklákon habzani;a távolban magasodni|erdő;szirt;zúgók|Mit csinál a folyó?|Végigrohan a vadonon.
5538|egy megrakott pótkocsit vontatni;a horizonton állni;narancssárgán és rózsaszínen ragyogni|silók;kombájn;traktor;búza|Mit csinálnak a gépek?|Búzát aratnak naplementekor.
5117|egy keménytáblás könyvet lapozgatni;az ámulattól levegő után kapni;zsúfolásig tele lenni könyvekkel|szemüveg;könyvespolcok;farmerdzseki;keménytáblás könyv|Mit csinál a fiatal férfi?|Egy keménytáblás könyvet lapozgat egy könyvesboltban.
6836|felhúzni egy kanapét;egy kötélen lógni;felemelni az ökölbe szorított kezét|társasház;grillsütő;kanapé;furgon|Mit csinál a fiatal nő?|Egy kanapét húz fel az erkélyére.
5540|megmászni a mászófalat;a matracon guggolni;megmarkolni egy nagy fogást|hajfonatok;lófarok;matrac;magnéziazsák|Mit csinál a hajfonatos nő?|Egy meredek mászófalat mászik meg.
5671|a levegőbe csapni az öklével;felfelé tekerni a dombon;egy kerékpáros mellett futni|havas csúcsok;sisak;kőfal;lehullott levelek|Mit csinál a férfi?|Biztatja a kerékpárost.
124|beleharapni a kenyérbe;csíkos kötényt viselni;olvadni a kenyéren|vaj;kés;kötény;serpenyők|Mit csinál a lány?|Vajat ken a kenyérre.
4364|a croissant-ok láttán levegő után kapni;virágmintás kötényt viselni;izzani a hőtől|tészta;liszt;kötény;ablak|Mit csinál a két nő?|Tésztagolyókat formáznak.
7453|forgatni a tésztát;előrenyújtani egy tányért;a wok alatt égni|wok;lángok;merőkanál;kendő|Mit csinál a szakács?|Tésztát készít egy wokban.
7883|az ösvényen térdelni;megnyalni a nő arcát;tartani a kiskutya pórázát|kiskutya;kerékpár;pad;lámpaoszlop|Mit csinál a térdelő nő?|Örömében átöleli a kiskutyát.
"""
out = {}
for line in DATA.strip().split('\n'):
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
src = json.load(open(f'{HERE}/source.json'))
out = {i: out[i] for i in src}
json.dump(out, open(f'{HERE}/hu.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
