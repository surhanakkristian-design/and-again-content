import json,os
H=os.path.dirname(os.path.abspath(__file__))
T="""7891|rátenni egy kis levelet;felnézni a pincérnőre;felvágni a halat|férfi;pincérnő;tányér;asztal|Mi van a férfi tányérján?|Egy kis darab hal van rajta.
7892|elöl menni;deres védőszemüveget viselni;lemaradva követni a nőt|védőszemüveg;felhők;hágóvasak;hó|Mit csinál a nő?|Felfelé mászik egy havas gerincen.
7893|tükörszelfit készíteni;hátulról átölelni őt;átsétálni a padlón|függőlámpa;kartondobozok;kerékpár;macska|Mit csinál a pár?|Együtt tükörszelfit készítenek.
7894|inni egy csészéből;felmenni a lépcsőn;biciklizni|füst;repülőgép;lepedő;kutya|Hol lakik a nő?|Egy régi repülőgépben lakik.
7896|a kezébe tüsszenteni;fentről figyelni;nagyra tátani a száját|ablak;könyvek;papírok;asztal|Mit csinál a fehér ruhás férfi?|A kezébe tüsszent.
7897|lehunyni a szemét;a fűben állni;lehajtani a fejét|pajta;ló;kapu;fű|Mit csinál a férfi?|A ló arcát érinti.
7898|hátrahajolni a rúd alatt;letérdelni a cölöp mellé;a levegőbe bokszolni|az ég;nádtető;bambuszrúd;homok|Mit csinál a kék inges férfi?|Hátrahajol a bambuszrúd alatt.
7900|tükörszelfit készíteni;hitetlenkedve bámulni;beleolvadni a tapétába|tapéta;fali lámpa;cserepes pálma;szőnyeg|Mihez illik az új ruhája?|Az új ruhája a flamingós tapétához illik.
7901|szorongatni egy gitártokot;odanyújtani egy konyharuhát;guggolni a padlón|tetőablak;olajlámpa;gitártok;vödör|Mit csinál a nő?|A gitártokját szorongatja.
7902|feldobni egy palacsintát;felásni egy veteményeságyást;fehér kötényt viselni|függőlámpa;serpenyő;golden retriever;kötény|Mit csinál a férfi?|Feldob egy palacsintát a levegőbe.
7903|besiklani a képbe;sodródni a zavaros vízen;a korlát fölé magasodni|gyalogoshíd;hattyú;evezős csónak;lámpaoszlop|Mit csinál az elöl úszó hattyú?|A türkizkék vízen siklik.
7904|szelfivideót forgatni;kigombolt narancssárga inget viselni;beugrani a képbe|zászlófüzér;hőlégballon;szalmakalap;fű|Mit csinál az elöl álló nő?|Szelfivideót forgat.
7905|karba tenni a kezét;nevetésben kitörni;egyszerű fehér pólót viselni|mennyezeti lámpa;a hátsó ablak;farmersort;hosszú szoknya|Hol ül a sárga ruhás nő?|Középen szorong.
7906|hóangyalt csinálni;karba tenni a kezét;hanyatt feküdni a hóban|emeletes busz;kerékpárok;hó;pufidzseki|Mit csinál a piros ruhás nő?|Hóangyalt csinál.
7908|húzni egy bőröndöt;döbbenten bámulni;belefújni egy sípba|gömblámpa;vonat;ruhák;bőrönd|Mi történt éppen a nővel?|Éppen lekéste a vonatát.
7909|az ajtóban állni;ügyetlenül leguggolni;italos tálcát vinni|üvegtető;dinoszaurusz-jelmez;vonósnégyes;ezüst ruha|Mit visel a zöld ruhás férfi?|Felfújható dinoszaurusz-jelmezt visel.
7910|szaxofonon játszani;táncolni a zenére;aludni a zongorán|lámpa;macska;szaxofon;zongora|Mit csinál a férfi?|Szaxofonon játszik.
7911|üvegeket ütögetni egy kanállal;kanalakkal ütni a fazekakat;karba tenni a kezét|csészék;hűtő;fazék;üvegek|Mit csinál a piros ruhás nő?|Üvegeket ütöget egy kanállal.
7914|eláztatni a szomszédját;lombfúvót használni;a kerítésen kuporogni|kémény;lombfúvó;léckerítés;gumicsizma|Mit csinál a vörös hajú nő?|Eláztatja a szomszéd férfit.
7915|egy doboz tésztát tartani;főzni a tésztát;tizenkét órát mutatni|óra;az ég;épület;emberek|Mit tart az elöl álló férfi?|Egy doboz tésztát tart.
7917|csapkodni az erős szélben;kavarogni a sósíkság felett;a repedezett talajon terülni el|buszmegálló;pocsolya;hegyek;felhők|Hol van a buszmegálló?|A buszmegálló a semmi közepén áll.
7919|megbökni a fényes tárgyat;a fejét fogni;leguggolni a gömb mellé|tárgy;bot;hínár;az ég|Mi fekszik a tengerparton?|Egy hatalmas ezüst tárgy fekszik a tengerparton.
7920|egyenesre igazítani egy bekeretezett képet;összpontosítva ráncolni a homlokát;megkocogtatni a férfi vállát|vízmérték;földgömb;szekrény;ablak|Mit csinál a piros ruhás férfi?|Egyenesre igazít egy bekeretezett képet.
7921|hemperegni a sárban;lerázni a nedves bundáját;egy nagy törölközőt tartani|ház;kutya;törölköző;vödör|Mit csinál a kutya?|A kutya a sárban hempereg.
7922|szándékosan gyümölcslevet önteni;odanyújtani egy konyharuhát;hitetlenkedve felbámulni|szekrények;vízforraló;konyharuha;pocsolya|Mit csinál a nő?|Szándékosan gyümölcslevet önt.
7923|bicepszezni egy nehéz kézisúlyzóval;bámulni egy csokis fánkot;kóborolni az edzőteremben|függőlámpák;atlétatrikó;fánk;kézisúlyzó|Mit csinál az elöl álló férfi?|Egy csokis fánkot bámul.
7924|megpördülni az utcán;lóbálni egy bőr kézitáskát;zöld melegítőnadrágot viselni|zászlófüzér;kézitáska;hangszóró;macskakövek|Mit csinál a kék ruhás nő?|Egy helyben táncol.
7926|átugrani az ösvényen;megcsúszva lefékezni;ijedten felszisszenni|sisak;szarvasbika;hegyi kerékpár;lehullott levelek|Mit csinál a szarvasbika?|Átugrik az ösvényen.
7927|várni az ajtónál;vinni egy dobozt;tartani egy csészét|ajtó;nő;kutya;doboz|Mit csinál a kutya?|A kutya az ajtónál vár.
7928|túlórázni az íróasztalánál;jegyzeteket firkálni;dörzsölni a halántékát|kijárat tábla;elviteles doboz;bögre;dzseki|Mit csinál a nő?|Túlórázik az íróasztalánál.
7930|lesikálni egy poros lakóbuszt;vizet önteni egy vödörbe;leguggolni a lakóbusz mellé|szivacs;lakóbusz;kőfal;beton|Mit csinál a nő?|Egy poros lakóbuszt sikál.
7931|elkerekezni egy traktor mellett;sisakot viselni;traktort vezetni|az ég;hegyek;traktor;bicikli|Mit csinál a nő?|Elkerekezik egy traktor mellett.
7935|kiüríteni egy fémtálat;leengedni az átlátszó fedelet;vékony réteget alkotni|fémtál;műanyag fedél;vászonzsák;szobanövény|Mit csinál a férfi?|Piros labdákat borít ki egy tálból.
7936|apró tablettákat kiszámolni;a pultra támaszkodni;megragadni egy gyógyszeres üveget|havas ablak;csíkos sál;gyógyszeres üveg;márványpult|Mit csinál a macska?|A macska egy spatulával számolja a tablettákat.
7937|megérinteni a fémkupolát;megtekerni egy rézfogantyút;meglepetten felszisszenni|acélgerenda;téglafal;fémkupola;fehér edzőcipő|Mit érint a nő?|Egy fémkupolát érint.
7938|összetenni a kezét;odanyújtani egy tányért;elvenni egy croissant-t|az ég;fák;croissant;papírzacskó|Mit csinál a férfi?|Egy croissant-t ad neki.
7939|hintázni egy fa alatt;csokitortát enni;játszani a fűben|az ég;fa;kutya;pléd|Mit eszik a férfi?|Csokitortát eszik.
7940|egyensúlyozni egy halom dobozt;a homlokát fogni;befalni egy pizzát|sisak;szobanövény;dohányzóasztal;golden retriever|Mit csinál a kutya?|Befal egy egész pizzát.
7941|egyensúlyozni egy fémvödröt;megtartani a széket;végigsietni a folyosón|vödör;függőlámpa;faszék;kilincs|Mit egyensúlyoz a piros ruhás nő?|Egy vödröt egyensúlyoz az ajtón.
7942|kézben tartani egy házikedvenc kígyót;rémülten sikoltozni;a karfán kuporogni|kígyó;függő növény;díszpárna;szőnyeg|Mit csinál a férfi?|Egy házikedvenc kígyót tart a kezében.
7943|tartani a krétát;dörzsölni a kezét;tartani egy hosszú botot|pont;lámpa;nő|Mit tart a nő?|Egy darab krétát tart.
7944|benyúlni egy táskába;a csövek között állni;elkerekezni a szökőkút mellett|utcai lámpa;farmerdzseki;szökőkút;teniszlabdák|Mit csinál a kerékpáros?|Elkerekezik a szökőkút mellett.
7945|kiönteni a tejet;feltakarítani a rumlit;leugrani a pultról|papírlámpa;kötény;rongy;kiömlött tej|Mit csinál a barna ruhás férfi?|Egy ronggyal törli a pultot.
7947|áthajolni a mérleg fölött;fonott kosarat vinni;elcsenni a vajat|mosómedve;rézmérleg;vaj;fonott kosár|Mit visz a nő?|Egy fonott kosarat visz.
7949|magához szorítani egy apró kutyát;egy kutya fején ücsörögni;fogni egy kutya pórázát|virág;panelház;kiscica;rottweiler|Min áll a kiscica?|A rottweiler fején áll.
7950|a kupola fölé hajolni;feltartott karral ujjongani;bekukucskálni a kupolába|az ég;homokvár;tajték|Mit csinál a sárga ruhás nő?|Feltartott karral ujjong.
7951|mosolyogva tapsolni;megfeszíteni a bicepszét;feltartani a hüvelykujját|mennyezeti lámpa;tükör;atlétatrikó;súlyzórúd|Mit csinál a fehér ruhás férfi?|Megfeszíti a bicepszét.
7952|mindkét kezével gesztikulálni;figyelmesen hallgatni;elnyúlni egy kanapén|állólámpa;függöny;jegyzetfüzet;bársonykanapé|Hol fekszik a férfi?|Egy bársonykanapén fekszik.
7953|rángatni egy zárt ajtót;pörögni egy piros szoknyában;fekete aktatáskát vinni|aktatáska;zászlófüzér;szoknya;az ég|Mit csinál az üzletember?|Egy zárt ajtót rángat.
7954|felszolgálni egy szelet pitét;egy fehér tányért tartani;nevetni a kutyán|lámpa;sapka;negyed;a padló|Mit csinál a kutya?|Egy negyedet tesz a tányérra.
7955|a labdáért vetődni;a műfüvön landolni;a fejét fogni|kapufa;toronyházak;kapus;műfű|Mit csinál a kapus?|Vetődik a labdáért.
7956|letérdelni az autó mellé;feltartani egy kerek táblát;egy régi gumit vinni|az ég;tábla;kerék;a talaj|Mit csinál a nő?|Kereket cserél az autón.
7957|nehéz könyveket emelni;felmászni egy létrára;térden állni|könyvek;létra;asztal;a padló|Mit csinál a nő?|Nehéz könyveket emel.
7958|vinni egy dobozt;kinyitni egy üvegajtót;egy pult mögött állni|doboz;lámpa;szemetes;pult|Mit visz a nő?|Egy dobozt visz.
7960|mintás inget viselni;megdönteni egy gyümölcsleves dobozt;izgatottan tapsolni|kancsó;citromok;fényfüzér;üveg|Mit csinál a göndör hajú nő?|Izgatottan tapsol.
7961|elhúzni egy függönyt;megszaglászni az arcát;lepakolni egy éjjeliszekrényt|beagle;bögre;tulipánok;boltív|Mit csinál a beagle?|A göndör hajú nő arcát szaglássza.
7963|egyensúlyozni egy padon;kocogni az ösvényen;eltakarni az arcát|lámpaoszlop;uszkár;leggings;pad|Mit csinál az uszkár?|Az uszkár egy padon egyensúlyoz.
7964|megdönteni egy fa lapátot;lepotyogni a lapátról;rávigyorogni a kamerára|fonott kosár;lapát;kötény;sütőtepsi|Mit tart a kutya?|A kutya egy fa lapátot tart.
7965|elterülni a kanapén;leugrani a kanapéról;letenni a bögréjét|lámpaernyő;könyvespolcok;kanapé;vászontáska|Mit csinál a nő?|Elterül a bársonykanapén.
7967|rázni egy fehér zseblámpát;a falnak dőlni;kék dzsekit viselni|fal;kötél;táska;szikla|Mit tart a nő?|Egy fehér zseblámpát tart.
7968|felbámulni a mennyezetre;kikapni a vizsgadolgozatot;firkálni a vizsgadolgozatra|óra;faburkolat;vizsgadolgozat;hátizsák|Mit csinál a férfi?|Kikapja a vizsgadolgozatát.
7969|szelfit csinálni;a feje fölött tartani egy aktatáskát;egy rúdnak dőlni|kapaszkodók;aktatáska;kötött sapka;pufidzseki|Mit csinál az üzletember?|A feje fölött tartja az aktatáskáját.
7970|egy üres tölcsért tartani;megérinteni a vállát;megenni a fagylaltot|strandházikók;korlát;sirály;fagylalt|Mit eszik a sirály?|A fagylaltot eszi.
7971|megfeszíteni a bicepszét;beállítani a mérleget;a levegőbe bokszolni|bokszring;tömeg;szatén rövidnadrág;mérleg|Mit csinál a bokszolónő?|A mérlegen megfeszíti a bicepszét.
7972|a kilátásra mutatni;elragadtatva nevetni;aranykarkötőt viselni|az ég;dombok;kőhíd;háztetők|Mit csinál a fiatalember?|A toronyból csodálja a kilátást.
7973|kitárni az ajtót;szorongatni a könyveit;a hátizsákja pántjait markolni|az ég;lámpás;könyvek;őszi levelek|Mit tart a fiatal nő?|Egy halom könyvet szorongat.
7974|ráugrani egy nyugágyra;hason feküdni;hűtőtáskát vinni|vízimentő-torony;hűtőtáska;strandtörölköző;strandpapucs|Mit csinál a narancssárga ruhás nő?|Ráugrik egy nyugágyra.
7975|titokban megetetni a kutyát;megnyalni a villát;lelkesen tapsolni|csillár;pincér;kandeláber;kutya|Mit csinál a kék ruhás nő?|Hússal eteti a kutyát.
7977|kimutatni az ablakon;egy széken ülni;a szék mellett állni|madár;lámpa;szék;ablak|Mit csinál a nő?|Kimutat az ablakon.
7978|elsiklani az üveg mellett;az uszonyaival evezni;rövid kék pulóvert viselni|tengeri teknős;oszlop;páfrány;korlát|Mit csinál a tengeri teknős?|Elsiklik az üveg mellett.
7979|a ponyvának dőlni;a kesztyűje mögött kuncogni;a feje fölé emelni a sisakját|viharfelhő;klubház;pocsolya;határkötél|Mit csinál a fehér ruhás nő?|A kesztyűje mögött kuncog.
7980|fogni a ruháját;megérinteni a haját;italt tölteni|fények;az ég;fa;bárpult|Mit visel a két nő?|Ugyanazt a zöld ruhát viselik.
7982|elrántani a dobozt;átnyúlni az asztalon;a pulton kuporogni|pizzásdoboz;macska;szalvéta;függőlámpa|Mit tart a nő?|A mellkasához szorítja a pizzásdobozt.
7983|kifújni az orrát;felülni az ágyban;kihozni egy tálcát|szobanövény;tálca;golden retriever;klumpa|Mit csinál a kutya?|A kutya egy tálca levest hoz.
7984|kék bikinit viselni;átmutatni a medence túloldalára;törölközővel szárazra dörzsölni a haját|úszómester;ajtónyílás;bikini;úszómedence|Mit csinál a kék ruhás nő?|Beugrik az úszómedencébe.
7985|ásítozni a kanapén;a kanapé mögött állni;sétálni a polcon|lámpa;kép;könyvek;csésze|Mit csinál a három fiatal?|A kanapén ülnek.
7986|erősen rángatni a pórázt;nem mozdulni egy centit sem;átugrani a pórázon|bulldog;póráz;kőhíd;lámpaoszlop|Mit csinál a lila ruhás nő?|Erősen rángatja a pórázt.
7987|átkelni az utcán;várni a teknős mögött;nagyon lassan járni|teknős;autó;levél;fa|Hogyan jár a teknős?|A teknős nagyon lassan jár.
7988|kötélen sétálni;kitárni a karját;narancssárga rövidnadrágot viselni|férfi;folyó;fa;az ég|Hol sétál a férfi?|Egy kötélen sétál.
7989|a kezében vinni a cipőjét;aludni a kanapén;a padlón feküdni|férfi;kutya;ablak;cipők|Hogyan lépked a nő?|Halkan lépked.
7990|átkiabálni a mezőn;egy dobozon állni;végignézni a mezőn|az ég;ház;nő;virágok|Mit csinál a nő?|Egy fadobozon áll.
7993|gördeszkázni;a peremen ülni;a rádió mellett feküdni|az ég;férfi;kutya;üvegek|Mit csinál a nő?|Gördeszkázik.
7994|végigsétálni az utcán;lengetni a sálát;egy csészét tartani|az ég;bolt;fehér kabát;hó|Mit csinál a férfi?|Végigsétál az utcán.
7995|egykerekezni;a magasba lendíteni a karját;a feje fölött egyensúlyozni egy tálcát|napellenző;motor;pincér;macskakövek|Mit csinál a motoros?|A hátsó kerékre állva motorozik.
7998|egy lábon egyensúlyozni;a feje fölé emelni a karját;összetenni a tenyerét|az ég;toronyházak;teherautó;jógamatrac|Mit csinál a nő?|Egy lábon egyensúlyoz.
8002|tükörszelfit készíteni;rángatni a táska fülét;megszaglászni egy utazótáskát|mennyezeti lámpa;könyvespolc;tacskó;fogkefe|Mit csinál a tacskó?|Egy utazótáskát szaglász.
8003|összehajtani egy csíkos törölközőt;a korlátra támaszkodni;az ajtóban ülni|világítótorony;macska;fűszernövények;gumicsizma|Mit csinál a nő?|Összehajt egy csíkos törölközőt.
8005|ledobni egy sporttáskát;hálózsákot vinni;kinyitni egy hűtőtáskát|neoncsillag;lakóbusz;párna;hűtőtáska|Mit csinál a férfi?|A lakóbusz tetején térdel.
8007|befutni a pályára;lekullogni a pályáról;sáros mezt viselni|cserejátékos;jelölőmez;fák;az ég|Mit csinál a sáros játékos?|Lekullog a pályáról.
8008|a magasba lendíteni a kezét;szorongatni egy bagettet;a levegőbe lövellni a vizet|bagett;szalmakalap;piknikpléd;fák|Mit tart a férfi?|Egy bagettet szorongat.
8009|megoperálni egy plüssmackót;odanyújtani egy fémtálat;a műtőasztalon feküdni|műtőlámpa;csempék;plüssmackó;tálca|Mit csinál a nő?|Egy plüssmackót operál.
8010|összevarrni egy banánt;kesztyűs kézzel tapsolni;beállítani a műtőlámpát|műtőlámpa;banán;zsebkendős doboz;tálca|Mit csinál a bordó ruhás férfi?|Egy banánt varr össze.
8011|felmászni a hegyre;két jégcsákányt tartani;piros dzsekit viselni|az ég;nő;szikla;hó|Mit csinál a nő?|Felfelé mászik a hegyen.
8012|lenézni a földre;kortyolni egy csésze kávét;a macskaköveken ülni|napellenző;asztalterítő;bulldog;macskakövek|Mit csinál az ülő férfi?|Egy csésze kávét kortyol.
8013|szelfit készíteni;arcon csókolni őt;feltartani egy dzsekit|az ég;fa;dzseki;fű|Mit csinál a férfi?|Arcon csókolja őt.
8014|pózolni a portré mellett;a keze mögött kuncogni;a kandalló mellett feküdni|csillár;portré;kandalló;farkaskutya|Mit csinál a nő?|A keze mögött kuncog.
8015|pózolni egy tükörszelfihez;elfojtani egy ásítást;elterülni a szőnyegen|éjjeli lámpa;ágytakaró;szatén ruha;magas sarkú cipő|Mit csinál a zöld ruhás nő?|Egy tükörszelfihez pózol.
8016|dajkálni egy vörös kiscicát;odanyújtani egy törölközőt;világítani az ajtó fölött|lámpás;kiscica;fürdőlepedő;leggings|Mit csinál a nő?|Egy vörös kiscicát dajkál.
8017|egy rózsaszín italt tartani;úszni a víz alatt;strandlabdát tartani|az ég;labda;ital;medence|Mit tart a kék ruhás nő?|Egy rózsaszín italt tart.
8018|felemelni egy menyasszonyi csokrot;a levegőbe bokszolni;fogni a menyasszony kezét|üvegtető;csigalépcső;csokor;pálmafa|Mit csinál a vőlegény?|A levegőbe bokszol."""
src=json.load(open(f'{H}/source.json'));rows={}
for l in T.strip().split('\n'):
    i,p,n,q,a=l.split('|');rows[i]=dict(phrases=p.split(';'),nouns=n.split(';'),question=q,answer=a)
out={i:rows[i] for i in src}
json.dump(out,open(f'{H}/hu.json','w'),ensure_ascii=False,indent=1)
