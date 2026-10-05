import json, os
H = os.path.dirname(os.path.abspath(__file__))
R = """
306|hosszú haja van|rövid szakálla van|a felhők fölött ragyogni|a nap;felhők;nő;férfi|Mi fölött repülnek?|A felhők fölött repülnek.
307|piros sapkát viselni|besétálni a ködbe|fehér gyapja van|köd;juh;sapka;fű|Hová sétál a férfi?|Besétál a ködbe.
308|hosszú, göndör haja van|az asztal mellett állni|felnézni rájuk|sajt;szőlő;nő;fal|Mi van az asztalon?|Az asztal tele van étellel.
309|gólt lőni|a labdáért ugrani|a kapuba repülni|focilabda;férfi;a tenger;homok|Mit játszanak?|A homokon fociznak.
310|megérinteni egy nagy fát|szürke dzsekit viselni|átsütni a fák között|az ég;fák;fű;nő|Hol sétálnak?|Egy erdőben sétálnak.
311|feltartani egy villát|nagyra nyitni a szemét|az asztalon égni|villa;gyertya;saláta;tészta|Mit csinál a nő?|Villával tésztát eszik.
312|vezetni a labdát|szabálytalanságot elkövetni|belefújni a sípba|a mennyezet;csuklópánt;jelvény|Mit csinál a játékvezető?|Szabálytalanság miatt belefúj a sípba.
313|eldolgozni az alapozót|oldalra fordítani a fejét|visszatükrözni mindkét nőt|papagájok;fonatok;tükör;alapozó|Mit csinál a fehér ruhás nő?|Szivaccsal dolgozza el az alapozót.
314|a fűben sétálni|nagyon magasra ugrani|megrázni a testét|róka;fa;fű|Mit csinál a róka?|A hideg fűben sétál.
315|szabadrúgást elvégezni|védekező sorfalat alkotni|a labdáért vetődni|focilabda;védők;domb;a pálya|Mit csinál a piros mezes játékos?|Szabadrúgást végez el.
316|kinyitni a fagyasztót|a borsót tartani|a fagylaltot tartani|kanál;fagylalt;sapka;fagyasztó|Mit tart a nő?|Egy zacskó borsót tart.
317|hasábburgonyát készíteni|hasábburgonyát enni|fekete sapkát viselni|hasábburgonya;sapka;biciklik;fények|Mit csinál a szakács?|Hasábburgonyát készít.
318|nagyon szomorúnak tűnni|megosztani a fagylaltját|a földön heverni|lány;az ég;a tenger;fagylalt|Mit csinál a zöld ruhás lány?|Megosztja a fagylaltját a barátnőjével.
319|egy kövön ülni|egy levélre ugrani|a vízben úszni|béka;kő;hal|Mit csinál a béka?|Egy kövön ül.
320|letörölni a deres padot|megérinteni egy fagyott levelet|két oszlop között lógni|pókháló;pad;a nap|Mit töröl le a nő?|A deret törli le a padról.
321|egy őszibarackot enni|egy kosarat vinni|az asztal mögött állni|ananász;szőlő;őszibarack;kosár|Mit eszik a nő?|Egy őszibarackot eszik.
322|hatalmas tétet megtenni|aggódva eltakarni a szemét|nagy sebességgel forogni|zsetonok;fülbevaló;szakáll|Mit csinál a nő?|Hatalmas tétet tesz meg.
323|pattogtatni a labdát|felemelni a nőt|a levegőben repülni|labda;az ég;háló;fák|Mit játszanak a barátok?|Egy kosárlabdameccset játszanak.
326|megszagolni egy rózsaszín rózsát|egy faládát vinni|a férfi közelében sétálni|rózsa;nő;ház;az ég|Mit szagol a nő?|Egy rózsaszín rózsát szagol.
327|egy piros paradicsomot enni|kalapot viselni|a virágok közelében repülni|az ég;kalap;férfi;méh|Mit eszik a férfi?|Egy piros paradicsomot eszik.
328|meghámozni a fokhagymát|a konyhában ülni|besétálni a konyhába|fazék;kés;fokhagyma|Mit szagol a nő?|A fokhagymát szagolja.
329|egy fehér vízforralót tartani|bekapcsolni a gázt|olajat önteni a serpenyőbe|nő;fazék;vízforraló;tűz|Mit tart a férfi?|Egy fehér vízforralót tart.
331|felvenni egy narancsot|egy kosarat vinni|levenni a kalapját|esernyő;úriember;nő;kosár|Mit visz az idős nő?|Egy kosár narancsot visz.
333|átugrani egy kötelet|sárga pólót viselni|felemelni a kezét|nő;fal;lány|Mit csinál a farmeres lány?|Átugrik egy kötelet.
334|fehér inget viselni|sötét szakálla van|egy tálban heverni|pohár;kancsó;citromok;az ég|Mit csinál a nő?|Limonádét iszik egy pohárból.
336|megtisztítani a szemüvegét|kék dzsekit viselni|a vízben úszni|szemüveg;levelek;víz;ujj|Mit tisztít a nő?|A szemüvegét tisztítja.
338|egy kontinensre mutatni|az állványán forogni|az íróasztal fölött világítani|földgömb;lámpaernyő;fülbevaló;pulóver|Mit csinál a nő?|Egy kontinensre mutat a földgömbön.
340|egy padon ülni|a földön feküdni|a kapuba repülni|kapu;az ég;kövek;nő|Hová repül a labda?|A labda a kapuba repül.
341|felmászni egy kőfalra|beleharapni egy fehér ingbe|a tetőn állni|az ég;kecske;tető;fal|Mibe harap bele a kecske?|Egy fehér ingbe harap bele.
342|kék úszószemüveget felvenni|az ujjával mutatni|a víz alatt úszni|sapka;úszószemüveg;víz;fürdőruha|Mit vesz fel a lány?|Kék úszószemüveget vesz fel.
344|felemelni valami nehezet|megtisztítani egy aranyrudat|aranyláncot viselni|szemüveg;zakó;aranyrúd;lánc|Mit tisztít a nő?|Egy aranyrudat tisztít.
346|golfozni|egy piros zászlót tartani|a füvön gurulni|az ég;zászló;labda;lyuk|Mit csinál a nő?|Golfozik.
348|lepecsételni egy hivatalos dokumentumot|széttárt karral gesztikulálni|három színes oszlopot mutatni|flipchart;gumibélyegző;mutatópálca|Mit csinál a lila ruhás nő?|Lepecsétel egy hivatalos dokumentumot.
349|sapkát viselni|kék pólót viselni|a fafelületen feküdni|nagyapa;fiú;asztal;fák|Ki játszik a fiúval?|A nagyapja játszik vele.
350|egy hátizsákot vinni|az ajtóhoz sétálni|egy fotelben ülni|unoka;nagymama;fotel|Kit ölel meg a nagymama?|Az unokáját öleli meg.
351|sárga pólót viselni|sötétkék rövidnadrágot viselni|rövid haja van|fű;madár;lány;fiú|Hol fekszenek?|A füvön fekszenek.
352|kinyújtani a kezét|feltartani egy ujját|sötét csíkjai vannak|virágok;asztal;gyertya;grillsütő|Mi van a grillsütőn?|Sajt és zöldségek vannak a grillsütőn.
355|a kezébe temetni az arcát|hosszú repedés van rajta|rizs és ragu van rajta|képkeret;kerámia;kanapé;tányér|Hogyan mutatja ki a férfi a bűntudatát?|A kezébe temeti az arcát.
356|egy nagy táskát vinni|körülnézni az edzőteremben|a válláról lógni|a mennyezet;súlyok;póló;táska|Mit visz a nő?|Egy táskát visz be az edzőterembe.
357|kifésülni a hosszú haját|tapsolni|a virágok mellett feküdni|függöny;ablak;virágok;hajkefe|Ki tartja a hajkefét?|A hosszú hajú nő tartja a hajkefét.
359|egy kerékben futni|magokat enni|tele lenni magokkal|hörcsög;kerék;tál|Mit csinál a hörcsög?|Magokat eszik egy tálból.
360|átnézni az ülés fölött|fekete szakálla van|a férfi mellett ülni|kézfertőtlenítő;kutya;férfi;asztal|Mit tesznek a kezükre?|Kézfertőtlenítőt tesznek a kezükre.
361|nyalókákat papírba csomagolni|egy kupacban heverni|mosolygós arca van|nyalókák;csokor;szalag|Mit csinálnak a kezek?|Nyalókákat csomagolnak papírba.
362|az utcán táncolni|egy őszibarackot enni|odamenni a nőhöz|őszibarack;kutya;hajó;cipők|Milyennek tűnik a nő?|Nagyon boldognak tűnik.
363|jegyzeteket írni|megvilágítani az íróasztalt|megjeleníteni egy dokumentumot|asztali lámpa;kardigán;laptop;öntapadós jegyzetlapok|Mit csinál a férfi?|Kutatómunkát végez az íróasztalánál.
364|papírra rajzolni|egy narancssárga ceruzát tartani|a kamerába mosolyogni|arc;póló;ceruza;rajz|Mit csinál a férfi?|Egy narancssárga ceruzával rajzol.
366|levenni egy kötést|megmarkolni egy tornagyűrűt|az öklével a levegőbe csapni|ruhaujj;ököl;kávéscsésze;autókulcsok|Mit markol meg a nő?|Egy tornagyűrűt markol meg.
367|egy jégnyalókát enni|egy legyezőt tartani|a földön feküdni|az ég;szökőkút;ing;ruha|Mit eszik a férfi?|Egy narancssárga jégnyalókát eszik.
369|elhajtani a motorkerékpár mellett|két tükre van|az égen lebegni|autó;út;motorkerékpár;az ég|Mit csinál az autó?|Elhajt a motorkerékpár mellett.
370|felvenni egy bukósisakot|egy gördeszkát tartani|egy poharat tartani|bukósisak;nadrág;gördeszka;az ég|Mit vesz fel a lány?|Egy piros bukósisakot vesz fel.
371|megdörzsölni a bazsalikomleveleket|fűszernövényeket szórni a spagettire|felhúzni a szemöldökét|fűszernövények;szakáll;spagetti;tányér|Mit csinál a nő?|Fűszernövényeket szór a spagettire.
372|dekázni egy focilabdával|kézenállást bemutatni|a levegőben pörögni|felhőkarcolók;focilabda;árnyék|Mit csinál a férfi?|Trükköket mutat be egy focilabdával.
373|besétálni egy stadionba|piros mezt viselni|lemenni a lépcsőn|az ég;stadion;férfi;lépcsők|Mit csinál a szőke férfi?|Besétál egy stadionba.
374|az út mentén kocogni|egyenletes tempót tartani|tetovált lába van|utcai lámpa;az ég;kocogó;út|Mit csinál a férfi?|Az út mentén kocog.
375|becsatolni a sisakja pántját|végigszáguldani a pályán|megmarkolni a kormányt|a nap;lelátó;versenyautó;aszfalt|Mit csinál a versenyautó?|Végigszáguld a pályán.
377|a kamerának szerepelni|a dobfelszerelésen játszani|egy kanapén heverészni|reflektor;előadó;dobfelszerelés;kanapé|Mit csinál a nő?|A kamerának szerepel.
379|a kamerába integetni|hátratűrni a haját|egy vlogot felvenni|függönyök;figurák;szeplők;laptop|Mit csinál a fiatal nő?|Egy vlogot vesz fel a hálószobájában.
380|áthaladni egy forgókapun|egy fafelületen állni|távol tartani az esőt|hátizsák;szemüveg;okostelefon;ablak|Min halad át a nő?|Egy metró forgókapuján halad át.
381|egy zöld szőlőszemet tartani|nagyon ijedtnek tűnni|sok fényképet mutatni|haj;szőlőszem;fényképek;mosdókagyló|Mit tart a férfi?|A megijedt férfi egy szőlőszemet tart.
382|megtisztítani egy ablakot|egy sárga szerszámot tartani|nagyon magasan függeni|sisak;az ég;a város|Mit csinál a nő?|Egy magasan lévő ablakot tisztít.
386|fekete szakálla van|megmutatni neki a hajóit|egy dobozban feküdni|férfi;nő;macska;hajók|Mit mutat neki a férfi?|A kis hajóit mutatja meg neki.
387|a szőnyegen pihenni|felébreszteni a gazdáját|egy paplan alatt aludni|szőnyeg;paplan;párna;éjjeliszekrény|Mit csinál a kutya?|A kutya megpróbálja felébreszteni a gazdáját.
388|a házi feladatát írni|kerek szemüveget viselni|tollal írni|haj;szemüveg;toll;házi feladat|Mit csinál a lány?|A házi feladatát írja.
389|mézet tenni a kenyérre|mézes kenyeret enni|egy falon feküdni|nő;férfi;kenyér;méz|Mit eszik a férfi?|Mézes kenyeret eszik.
390|felhúzni a kapucniját|piros kapucnis pulóvert viselni|a vízben úszni|víz;biciklik;kapucnis pulóver;kacsák|Mit csinál a férfi?|A fejére húzza a kapucniját.
391|felmászni a falra|felemelni a karját|a tengeren hajózni|nő;hajó;a tenger;fal|Mit néz a nő?|Egy hajót néz.
392|egy lovon lovagolni|vinni a nőt|felülni a lóra|az ég;nő;ló;fű|Mit csinál a nő?|Egy lovon lovagol.
393|átadni egy kulcsot|megmarkolni a falétrát|chipset nyújtani|lépcső;recepciós;pult;kulcs|Mit kínál a vörös hajú nő?|Egy zacskó chipset kínál.
394|megtörölni az arcát|egy vizespalackot tartani|levegőt fújni rá|tető;fal;ventilátor;törölköző|Mit csinál a férfi?|Törölközővel törli meg az arcát.
396|egy kis ajándékot tartani|a férfihoz futni|négy lábon járni|ablakok;ölelés;kutya;a padló|Mit csinál a férfi és a nő?|Megölelik egymást.
397|távcsövön át kémlelni|kötött sapkát viselni|a fák között legelni|fatörzsek;szarvasbika;lehullott levelek|Mit csinál a férfi és a nő?|Egy szarvasbikára vadásznak az erdőben.
398|kiöblíteni a száját|beszappanozni a kezét|szárazra törölgetni az arcát|tükör;pizsama;hab;mosdókagyló|Mit csinál a fiú?|A mosdókagyló fölött szappanozza be a kezét.
399|nyalni a fagylaltot|nagy kalapot viselni|a falon állni|az ég;madár;kalap;fagylalt|Mit csinál a férfi?|A fagylaltját nyalja.
400|korcsolyával megkerülni egy bóját|fehér sisakot viselni|az üveg mögött kiabálni|szurkolók;kapu;jég|Mit csinálnak a lányok?|Jégkorongoznak.
404|a kamerába nézni|hátul verekedni|együtt nevetni|függönyök;plakátok;táblagép;iskolapad|Mit csinálnak a mögötte lévő fiúk?|Verekednek az osztályteremben.
405|elsőként bejönni|egy forró fazekat vinni|nagyon rövid haja van|lámpa;ablak;tűz;asztal|Mit csinálnak az emberek?|Bejönnek a hóból.
407|szélesre tárni a karját|hosszú haja van|a fák fölött repülni|madarak;sziget;férfi;víz|Mit csinálnak a madarak?|A sziget fölött repülnek.
408|felvenni egy dzsekit|a férfira mosolyogni|a kerítésen állni|dzseki;nő;madár;az ég|Mit visel a férfi?|Egy barna dzsekit visel.
410|kinyitni egy lekvárosüveget|nézni a nőt|az ablak mellett állni|lekvár;vaj;kosár;macska|Mit csinál a nő?|Lekvárt tesz a kenyérre.
411|karba tett kézzel mogorván nézni|megnyerni a piros szalagot|átadni a díjat|szalag;harisnyanadrág;balettcipő;tükör|Milyennek tűnik a türkiz ruhás táncos?|Féltékenynek tűnik a másik táncosra.
412|széthajtogatni egy focimezt|átadni egy mezt|felhúzni egy mezt|mez;póló;lófarok;futballcipő|Mit csinál a göndör hajú nő?|Széthajtogat egy focimezt.
413|felvágni egy piros gyümölcsöt|elvenni a poharat|a földön sétálni|gyümölcslé;tál;fa;madár|Mit iszik a férfi?|Egy pohár gyümölcslevet iszik.
414|a pályán futni|átugrani a lécet|a matracra esni|az ég;matrac;fák;nő|Mit csinál az elöl lévő nő?|Átugorja a lécet.
415|átugrálni a homokon|az anyjával maradni|egy kölyköt vinni|kenguru;a nap;fű;az ég|Mit visz a nagy kenguru?|A kölykét viszi.
418|szétfeszíteni egy karikát|vigyorogva tapsolni|megpörgetni egy kulcstartót|kulcstartó;árus;vödör;ruhaujj|Mit csinál a nő?|Megpörget egy kulcstartót az ujján.
422|rúgni egy nagy zsákot|köteleken lógni|magasra emelni az egyik lábát|nő;zsák;felhők;a padló|Mit csinál a nő?|Egy nagy zsákot rúg.
423|csókot dobni|megcsókolni a kezét|nagy kalapot viselni|kalap;férfi;kosár;palack|Mit csinál a férfi?|Megcsókolja a nő kezét.
424|felvágni a kenyeret|megtörölni a kezét|paradicsomos szendvicset enni|kés;kutya;paradicsom;nő|Mit csinál a férfi?|Késsel kenyeret vág.
426|felmászni egy létrára|leszedni egy piros almát|mozdulatlanul tartani a létrát|létra;juh;fa;almák|Mit csinál a nő?|Felmászik egy létrára.
427|felmászni a fűszálon|kinyitni a szárnyait|az égbe repülni|katicabogár;virág;az ég;fű|Mit csinál a katicabogár?|Felmászik a fűszálon.
428|eldobni egy követ|szürke pulóvert viselni|piros pulóvert viselni|az ég;hegy;csónak;tó|Mit csinál a férfi?|Egy követ dob a tóba.
430|egy barna táskát vinni|egy ládán ülni|fehér szakálla van|házak;lány;kosár;hajó|Mit visz a lány?|Egy barna táskát visz.
431|a kanapén feküdni|a fal mellett állni|elvenni a távirányítót|ablak;seprű;férfi;asztal|Mit csinál a férfi?|A kanapén fekszik.
435|lekefélni egy bőrövet|felvenni egy dzsekit|az asztal alatt feküdni|nő;dzseki;öv;asztal|Mit visel a férfi?|Egy bőrdzsekit visel.
436|hosszú, ősz haja van|sárga szoknyát viselni|rózsaszín virágai vannak|az ég;fa;a tenger;szoknya|Merre mutatnak az emberek?|Balra mutatnak.
437|feltenni a lábát|felfutni a lépcsőn|a dombon állni|az ég;lépcsők;cipő;láb|Mit csinál a nő?|Felfut a lépcsőn.
438|beleharapni egy citromba|sötét szakálla van|a falon feküdni|citrom;kés;kéz|Mit csinál a nő?|Beleharap egy citromba.
439|hideg limonádét inni|a padlón feküdni|egy cserépben nőni|limonádé;virágok;kutya;nő|Mit csinál a nő?|Hideg limonádét iszik.
440|nehéz súlyokat emelni|széles övet viselni|a végén mosolyogni|férfi;öv;ablak|Mit csinál a férfi?|Nehéz súlyokat emel.
442|küszködni egy dobozzal|segítő kezet nyújtani|egy doboz mögött guggolni|macska;kartondobozok;szakáll;fapadló|Mit csinál a férfi és a nő?|Együtt egymásra rakják a kartondobozokat.
"""
out = {}
for line in R.strip().split('\n'):
    i, p1, p2, p3, n, q, a = line.split('|')
    out[i] = {"phrases": [p1, p2, p3], "nouns": n.split(';'), "question": q, "answer": a}
src = json.load(open(f'{H}/source.json'))
out = {k: out[k] for k in src}
json.dump(out, open(f'{H}/hu.json', 'w'), ensure_ascii=False, indent=1)
