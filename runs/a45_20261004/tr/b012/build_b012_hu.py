import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = """
4166|odamenni az autóhoz;kinyitni az autó ajtaját;beszállni a piros autóba|férfi;autó;fa;bokor|Mit csinál a férfi?|Beszáll a piros autóba.
4167|előbukkanni a barlangból;a tengerpart fölé magasodni;világítani a sötétben|kijárat;barlangfal;ló|Merre tart a ló?|A barlang kijárata felé tart.
4168|a hátán aludni;nagyon lassan menni;a levegőben repülni|a hold;nyúl;pillangó;teknős|Mit csinál a teknős?|Nagyon lassan megy.
4169|ránézni a medvére;egy csónakban ülni;a csónak közelében úszni|fák;folyó;sapka;medve|Mit csinál a férfi?|Egy pillantást vet a medvére.
4170|megmenteni egy kis csibét;a vízbe ugrani;egy fehér virágot vinni|tyúk;csibék;virág;jég|Mit csinál a tyúk?|Megment egy kis csibét.
4171|a bokrok között lopakodni;letenni a fejét;oltalmazni a csibéit|erdőtűz;vízesés;tyúk;csibék|Mit csinál a farkas?|A bokrok között lopakodik.
4172|a vízben gázolni;a köveken feküdni;a mezőn égni|domb;fészek;tyúk;folyó|Mit csinál a tyúk?|Egy fészket visz át a folyón.
4173|kivillantani a fogait;a ködbe zuhanni;a kötélbe kapaszkodni|farkas;tyúk;deszkák|Mit csinál a farkas?|A hídon át üldözi a tyúkot.
4174|szélesre tárni mindkét szárnyát;a füvön összebújni;a fák teteje fölött világítani|a hold;fenyőfák;róka;csibék|Mit csinál a tyúk?|A három csibéjét védi.
4175|elosonni egy hóbucka mellett;éles fogakat villantani;a horizont felé süllyedni|hóbucka;farkasok;zsák;lábnyomok|Mit csinál a tyúk?|A tyúk eloson a farkasok mellett.
4176|egy befőttesüveget szorongatni;megölelni a csibét;az éjszakai égen függeni|szentjánosbogár;csőr;befőttesüveg|Mi világít a befőttesüvegben?|Egy szentjánosbogár világít a befőttesüvegben.
4177|megmászni egy magas sziklát;kinyitni a szájukat;egy nagy zsákot vinni|csirke;száj;fészek;szikla|Mit csinálnak a madárfiókák?|Kinyitják a szájukat.
4178|belesni az üregbe;a tyúk alatt állni;világítani a sötétben|tyúk;gyertya;kukorica|Mit csinál a tyúk?|Megosztja a kukoricát az egerekkel.
4179|elfújni a gyertyákat;a falon lógni;három gyertyája van|napszemüveg;ing;gyertyák;torta|Mit csinál a nő?|Elfújja a születésnapi gyertyáit.
4180|egy piros pórázt markolni;egy kiskutyát a karjában tartani;a járdán mászni|nő;kiskutya;póráz;aligátor|Mit csinál a nő?|Egy aligátort sétáltat pórázon.
4181|egy piros robogón menni;a kamerába mosolyogni;egy fehér tányéron állni|nő;gyertyák;torta;tányér|Mit csinál a nő?|Egy piros robogón megy.
4182|festeni a füvet;a füvön feküdni;a nő fölött repülni|nő;férfi;fa;fű|Mit csinál a férfi?|A füvet festi.
4183|kinyitni a nagy dobozt;szélesre tárni a karját;eltakarni a száját|ajándék;nő;férfi|Mit kap az idős nő?|Egy nagy ajándékot kap.
4184|visszahozni a labdát;a labda után futni;eldobni a labdát|kutya;labda;kanapé;szőnyeg|Mit csinál a kutya?|Odaviszi a labdát a géphez.
4185|laposra nyomni az egeret;kikukucskálni alóla;málna van a tetején|bögre;gofrik;farok;tányéralátét|Mit csinál a bögre?|Laposra nyomja a játékegeret.
4186|a labda után futni;visszahozni a labdát;megütni egy teniszlabdát|fák;háló;kutya;gép|Mit csinál a kutya?|Visszaviszi a labdát a géphez.
4187|egy kék játékot tartani;a hátán feküdni;utolsóként eldőlni|függönyök;papagájok;kanapé;kéz|Mit csinálnak a papagájok?|Halottnak tettetik magukat a kanapén.
4188|leereszkedni egy meredek lejtőn;porhavat felverni;a csúcsok fölött izzani|csúcsok;a nap;lejtő|Mit csinál a síelő?|Lesíel egy meredek lejtőn.
4189|egy tálból enni;a padlón ülni;a tálban maradni|kutya;tál;tabletta;ajtó|Mi van az üres tálban?|Egy fehér tabletta van benne.
4191|fel-le ugrálni;a férfi fölé magasodni;felemelni mindkét karját|az ég;rakéta;a nap;épület|Mit csinál a férfi?|Egy rakéta előtt ugrál.
4192|a hullámok fölött siklani;szélesre tárni a szárnyait;a karmaival halászni|szárny;csőr;hal;a tenger|Mit csinál a sas?|A sas kikap egy halat a tengerből.
4193|behajtani egy föld alatti garázsba;zsanérokon felbillenni;narancssárga lámpák alatt csillogni|fák;csapóajtó;sportautó;térkő|Mit csinál az autó?|Behajt egy föld alatti garázsba.
4194|egy rózsaszín autót vezetni;a nő mögött nőni;behajlítani a térdét|az ég;fa;autó;fű|Mit csinál a nő?|Autókázik egyet.
4195|darabokra hullani;az égen ragyogni;átgurulni az úton|kerék;kosár;cipők;az út|Mi történik a robogóval?|A robogó darabokra hullik.
4196|egy gyertyát nézni;egy ágyban aludni;az időt mutatni|vödör;gyertya;férfi|Mi van a vödörben?|Egy gyertya van a vödörben.
4197|későn felébredni;a levegőben repülni;az ablak mellett lógni|telefon;takaró;függöny;párna|Mit csinál a férfi?|Későn ébred fel.
4198|mélyre zuhanni;belül sötét van;csillogni a napfényben|lyuk;a tenger;kéz;cipő|Hová zuhan a személy?|A személy mélyre zuhan egy lyukba.
4199|húzni a lábát;a rétre omlani;figyelni a leszállást|siklóernyős;vízpermet;tükörkép;part|Mit csinál a pilóta?|A vízben húzza a lábát.
4200|egy fa alatt állni;az öböl felé zuhanni;aranyszínűre festeni a tengert|boltív;szirt;hab;az ég|Mit csinál a nap?|Aranyszínűre festi a tengert.
4201|függőlegesen tartani a motorjukat;a part mentén sorakozni;visszatükrözni a rózsaszín felhőket|krosszmotorok;pálmafák;tükörkép;felhők|Mit csinálnak a motorosok?|Függőlegesen tartják a motorjukat.
4202|a hátukon feküdni;egy konyhai eszközt tartani;odamenni a kutyákhoz|has;fül;kéz|Mit csinál a két kutya?|A hátukon fekszenek.
4203|megmenteni egy partra vetett cápát;kiúszni a tengerre;megmarkolni egy cápa farkát|cápa;fürdőnadrág;homok;a tenger|Mit csinál a férfi?|Megment egy partra vetett cápát.
4205|egy fehér virágot vinni;a földre esni;becsukni a szemét|hörcsög;virág;a föld|Mit visz a hörcsög?|Egy fehér virágot visz.
4207|kiszállítani egy pizzát;egy telefonon görgetni;egy kanapén heverészni|masni;lámpaernyő;pizzásdoboz;szőnyeg|Mit csinál a szemüveges hörcsög?|Egy pizzát szállít ki.
4208|egy hamburgert enni;a hátán feküdni;egy polcról lógni|hamburger;pohár;kanapé;növény|Mit eszik a hörcsög?|Sok nassolnivalót eszik.
4211|szívószállal inni;megmosni az arcát;megérinteni az orcáját|masni;orca;doboz|Mit csinál a hörcsög?|Megmossa az arcát.
4212|egy kis táskát vinni;magas sarkú cipőt viselni;megigazítani az ingujját|nő;férfi;táska;kanapé|Mit visz a nő?|Egy kis táskát visz.
4213|a barátnőjére mutatni;megérinteni a barátnője vállát;egy zöld nyakláncot viselni|nyaklánc;ruha;táska;fal|Mit visel a két nő?|Hosszú ruhát viselnek.
4214|egy kis táskát tartani;rövid fekete haja van;egy cserépben nőni|nő;férfi;táska;fa|Mit tart a nő?|Egy kis táskát tart.
4215|egy narancssárga felsőt viselni;narancssárga nadrágot viselni;egy hosszú szoknyát viselni|ing;felső;táska;kanapé|Mit tart a nő?|Egy kis táskát tart.
4216|egy fehér ruhát viselni;egy fekete inget viselni;magas sarkú cipőt viselni|ruha;ing;nadrág;kanapé|Mit visel a nő?|Egy fehér ruhát visel.
4217|egy zöld autóban ülni;követni a kutyát;közelebb jönni|az ég;rendőrautó;kutya;út|Mit csinál a rendőrautó?|Követi a kutyát.
4218|egy rozsdás traktort kormányozni;fekete füstöt pöfékelni;az úton gurulni|füst;szőlőskert;kipufogócső;traktor|Mit csinál a kutya?|Egy rozsdás traktort kormányoz.
4219|elfordítani a szarvakat viselő fejét;megmarkolni a bőrnyerget;lezúdulni a sziklákon|az ég;fenevad;fjord;kesztyű|Mit csinál a fenevad?|A fenevad leveti magát egy szirtről.
4220|tisztítani a fehér autót;egy fekete táskát tartani;végighajtani az úton|dombok;férfi;autó;kerék|Mit csinál a férfi?|A fehér autót tisztítja.
4221|egy tálat vinni;felmászni a kanapéra;a tálból enni|kanapé;gyík;tál;takaró|Hol ül a gyík?|A kanapén ül.
4223|lenyelni egy csípős chilipaprikát;tüzet fújni;megtölteni egy sekély tálat|gekkó;chilipaprikák;tál|Mit eszik a gekkó?|Egy csípős chilipaprikát eszik.
4224|a vécére menni;kinyílni és becsukódni;a padlón feküdni|gyík;ajtó;szőnyeg;növény|Hová megy a gyík?|A gyík a vécére megy.
4225|egy tálkából enni;a doboz mögött állni;felül kinyílni|hörcsög;tálka;doboz|Mit csinál a narancssárga hörcsög?|A narancssárga hörcsög egy tálkából eszik.
4226|a folyó mellett kuporogni;a dinoszauruszba kapaszkodni;lezúdulni a sziklafalon|dinoszaurusz;krokodil;vízesés;hab|Mire vadásznak a krokodilok?|A krokodilok egy hatalmas dinoszauruszra vadásznak.
4227|egy sárga biciklit tekerni;megsimogatni egy bolyhos kutyát;egy hátizsák tetején ülni|láda;rendőr;rendőrautó;bicikli|Mit csinál a rendőr?|Egy barátságos kutyát simogat.
4228|szélesre tárni a karját;beszállni egy helikopterbe;egy serpenyőbe esni|hegy;tó;asztal;a part|Hol eszik a férfi?|Tojást eszik a parton.
4229|kiszabadítani egy megfagyott majmot;jégbe zárva ülni;leugrani a korlátról|jégcsapok;majom;kalapács|Mit csinál a személy?|A személy kiszabadít egy megfagyott majmot.
4230|fogni a kormánykereket;egy narancssárga sapkát viselni;piros ajtaja van|ülés;narancssárga sapka;kormánykerék;ajtó|Hol ül a nagy kutya?|A vezetőülésben ül.
4231|feltenni a mancsait;egy piros sapkát viselni;piros ajtaja van|ablak;kutyák;ülés;ajtó|Mit csinálnak a kutyák?|Kinéznek az ablakon.
4232|egy nagy labdát tartani;nagyon magasra ugrani;a fejét fogni|delfin;labda;fák;az ég|Mit tart a férfi?|Egy nagy labdát tart.
4233|áthaladni a hídon;lehullani a sziklákon;kőből készült|vonat;híd;víz;fák|Mit csinál a vonat?|Áthalad egy kőhídon.
4234|a magasba lendíteni a karját;kiüríteni az egész gardróbot;egy hatalmas kupacot alkotni|ruhák;pizsama;pulóverek|Min áll a férfi?|Egy ruhakupacon áll.
4235|bedobni egy horgászzsinórt;mezítláb állni a füvön;türkiz horgászzsinór van rajta|horgászbot;fiú;tó;fű|Mit csinál a fiú?|Bedob egy horgászzsinórt a tóba.
4236|a járdán sétálgatni;csípőre tett kézzel állni;ledobni a kesztyűjét|furgon;televízió;kézitáska;magas sarkú cipő|Ki vonja magára a férfiak figyelmét?|A magas sarkú cipős nő vonja magára a figyelmüket.
4237|egy répát kínálni;áthajolni a boksz fölött;zsúfolásig tele van répával|ló;répa;farmernadrág;boksz|Mit csinál a férfi?|A lovat eteti az istállóban.
4238|tűz fölött sülni;egy narancssárga pumpát használni;egy szürke inget viselni|hús;asztal;szőnyeg|Mi sül a tűz fölött?|A hús sül a tűz fölött.
4239|teherhajók között siklani;kiugrani a vízből;letekinteni a kikötőre|az ég;világítótorony;sirály;gyeplő|Mit csinál a sirály?|A kikötő fölött siklik.
4240|a hátán hemperegni;a kiskutya fölé magasodni;megérinteni a társa mellkasát|függöny;kiskutya;szőnyeg;okostelefon|Mit csinál a kiskutya?|A kiskutya a hátán hempereg.
4241|egy zöld fejhallgatót viselni;a repülőgép alatt lebegni;felfestett jelzései vannak|fejhallgató;mikrofon;biztonsági öv;nyakkendő|Mit csinál a férfi?|A repülőgépet vezeti.
4242|átugrani a kapu fölött;átmenni egy ajtón;zárva maradni|kapu;fal;macska;a padló|Mit csinál a szürke macska?|Átmegy egy kis ajtón.
4244|az autó felé rontani;távolról figyelni;hátravetni a fejét|fa;kecske;bika;kavics|Mit csinál a bika?|Az autó felé ront.
4245|a hasán csúszni;átzúdulni a falon;sekély vízen át sprintelni|vízesés;pálmafa;moha;az ég|Mit csinál a türkiz ruhás férfi?|A hasán csúszik.
4246|egy nagy madarat tartani;kék nyaka van;sokat nevetni|madár;sapka;póló;fák|Mit tart a nő?|Egy nagy kék madarat tart.
4247|a vízbe ugrani;a kútnál véget érni;egy sorban állni|kút;fiúk;ösvény;az ég|Mit csinálnak a fiúk?|Beugranak a kútba.
4248|nagy hullámokban úszni;a medence mellett állni;egy fehér sapkát viselni|úszó;lámpák;emberek;víz|Hol úszik a férfi?|Egy fedett medencében úszik.
4249|tüzet fújni;erősen kapaszkodni;a tóba zuhanni|a nap;tó;hát;kezek|Mit csinál a sárkány?|Egy tó fölött repül.
4250|egy targoncát kezelni;a kamerába bámulni;a mancsával jelezni|raktár;targonca;védősisak;mellény|Mit csinál a golden retriever?|Egy targoncát kezel egy raktárban.
4251|üres polcokra mutatni;a férfira vigyorogni;hitetlenkedve bámulni|polc;konty;zoknik;pulóverek|Mire mutat a nő?|Az üres polcokra mutat.
4252|egy narancssárga italt kortyolgatni;egy kefével súrolni;szétterülni a betonon|medence;szőnyeg;hab;beton|Mi terül szét a betonon?|Szappanos hab terül szét a betonon.
4253|egy motoron ülni;tisztítani a sisakot;mosni a motort|sisak;sapka;motor|Mi történik a motorral?|Egy férfi mossa a motort.
4254|a pulton ülni;dühösen meredni a galambra;a levegőben lebegni|galamb;szakácssapka;kötény;pult|Hol van a galamb?|A galamb a fémpulton ül.
4256|vakargatni a kenguru mellkasát;elterülni a füvön;nekidőlni a kéznek|kenguru;ruhaujj;az ég;fű|Mit csinál a kéz?|A kenguru mellkasát vakargatja.
4257|szorosan átölelni a teknőst;egy nagy ölelést kapni;a vízből figyelni|panda;teknős;hal;víz|Mit csinál a panda?|Szorosan átöleli a teknőst.
4258|feltápászkodni;visszatükrözni a halvány eget;a rét fölé magasodni|acél;őzgida;rét;erdő|Mit csinál az őzgida?|Egy acélcsúszdán fekszik.
4259|kinyitni a száját;egy narancssárga sálat viselni;mérges arcot vágni|arc;sál;az ég;gyapjú|Mit csinál a birka?|Mérges arcot vág.
4260|egy táblagépre vigyorogni;a gazdája mellett pihenni;az ajtóban ólálkodni|alak;lámpa;táblagép;takaró|Ki áll az ajtóban?|Egy sötét alak áll az ajtóban.
4261|egy piros labdát tolni;a barátja mögött úszni;a vízen lebegni|kutya;labda;fák;víz|Mit csinálnak a kutyák?|Egy napsütéses napon úsznak.
4262|kitárni a szárnyait;a bocsok fölött repdesni;a bocsai fölé magasodni|holló;bocsok;hó;hegyoldal|Mit csinál a holló?|A bocsok fölött repdes.
4263|végigsétálni a bolton;elsőként kinyitni a szemét;elvörösödni|zöld madár;kék madár;polcok;a padló|Mit csinál a két kis madár?|A rózsaszín madarat csodálják.
4264|a levegőben repülni;fehér nadrágot viselni;aranygyűrűket viselni|röplabda;nő;autó;felhők|Mit csinál a nő?|Röplabdázik az úton.
4266|végigfutni a tengerparton;kilógatni a nyelvét;a hátán hemperegni|kutya;az ég;homok;fű|Mit csinál a kutya?|Végigfut a tengerparton.
4267|kilógatni a nyelvét;szorosan behunyni a szemét;közrefogni a kutya állát|olló;nyelv;pázsit;asztal|Mit csinál a kutya?|Kilógó nyelvvel liheg.
4268|egy labdával ülni;a kanapén feküdni;egy focimeccset mutatni|tévé;virágok;csészék;asztal|Mit néz a kutya?|Egy focimeccset néz.
4269|vizet önteni;kerti kesztyűt viselni;benedvesedni|nő;kancsó;csésze;növény|Mit csinál a nő?|Vizet önt a száraz földre.
4270|markolni a kormánykereket;lelassítani a gokartot;áttotyogni a pályán|molinó;kacsa;kormánykerék;gumiabroncs|Mit csinál a sofőr?|A sofőr lelassít egy kacsa miatt.
4271|elkezdeni egy versenyt;nagyon gyorsan futni;nagyokat lépni|atléta;az ég;fű;futópálya|Mit csinál az atléta?|Nagyon gyorsan fut.
4272|arany fülbevalót felvenni;egy nagy kalapot viselni;két táskát vinni|kalap;sál;öv;nadrág|Mit visel a nő?|Egy nagy kalapot visel.
4274|markolni a kormánykereket;feltolni a szemüvegét;nekiütközni egy autónak|sérülés;fényszóró;az ég;hátsó lámpa|Mit csinál a férfi és a nő?|A sérült autó fölé hajolnak.
4275|az autóra mutatni;felvenni egy darabot;tollal írni|furgon;nő;kerék;az ég|Mit csinál a nő?|Az autó miatt panaszkodik.
"""
out = {}
for line in DATA.strip().splitlines():
    i, p, n, q, a = line.split('|')
    out[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
src = json.load(open(f'{HERE}/source.json'))
out = {i: out[i] for i in src}
json.dump(out, open(f'{HERE}/hu.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
