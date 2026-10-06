import json,os
H=os.path.dirname(os.path.abspath(__file__))
D=r'''
620|přivonět k růži;zavřít oči;zářit na obloze|žena;růže;košík;slunce|Co dělá žena?|Voní k růži.|voní k růži
5310|obejmout chlapce;mít na sobě šedé tričko;letět před garáží|chlapec;míč;muž|Co dělá žena?|Objímá svého syna.|objímá svého syna
41|držet kladivo;mít černé vlasy;viset na zdi|obraz;kladivo;žena;muž|Co dělají muž a žena?|Hádají se.|hádají se
5499|mít na sobě červené šaty;běžet po ulici;zalévat květiny|žena;květiny;okno;zeď|Co dělá stará paní?|Zalévá květiny.|žena;zalévá květiny
119|vydávat teplé světlo;držet hrnek;mít šedou srst|žárovka;kočka;miska;knihy|Co dělá muž?|Nasazuje novou žárovku.|nasazuje novou žárovku
166|nakreslit velký kruh;držet dlouhou hůl;tvořit kruh|žena;obloha;kruh;moře|Co kreslí žena?|Kreslí kruh do písku.|kreslí kruh do písku
596|vyhrát závod;mít na sobě žlutý top;mít na sobě fialový top|běžci;tráva;dráha|Kdo vyhrává závod?|Závod vyhrává běžkyně ve žlutém.|vyhrává závod
484|umýt podlahu;uklouznout na mokré podlaze;být plný vody|žena;mop;kbelík;podlaha|Co dělá žena?|Myje podlahu mopem.|myje podlahu mopem
68|natáhnout ruku;nosit brýle;ovinout zápěstí|brýle;palec;obvaz;lavička|Co dělá muž?|Obvazuje mu zápěstí.|obvazuje mu zápěstí
5149|mít červený nos;vylézt na vysoký žebřík;zářit jasně zeleně|kříž;lahve;šála;krabička|Co dělá muž v bílém?|Leze na vysoký žebřík.|leze na vysoký žebřík
457|zavřít oči;mít na sobě zelený top;ležet za ženami|žárovka;zrcadlo;pes;make-up|Kde leží pes?|Pes leží za ženami.|make-up;leží za ženami
36|mazlit se se svou zrzavou kočkou;viset ve vzduchu;zvednout svého mazlíčka|květináč;kočka;polštář;svetr|Co dělá žena?|Mazlí se s kočkou, kterou zbožňuje.|mazlí se s kočkou, kterou zbožňuje
676|fotografovat památky;řídit gondolu;tyčit se nad náměstím|zvonice;kopule;fotoaparát;gondola|Co dělají ti dva turisté?|Poznávají město z gondoly.|poznávají město z gondoly
7962|držet krabici od pizzy;obsahovat zbytky pizzy;viset nad střechou|světelné řetězy;komín;krabice od pizzy;koberec|Co obsahuje krabice od pizzy?|Obsahuje zbytek pizzy.|obsahuje zbytek pizzy
7858|udržovat rovnováhu na slackline;chránit si oči před sluncem;mávat z útesu|obloha;útes;řeka;fleecová mikina|Kde je žena v oranžovém?|Je v polovině cesty mezi oběma útesy.|je v polovině cesty mezi oběma útesy
7124|opatrně scházet po schodech;jásat z balkonu;stát na podnose|hosté;svatební dort;smoking;schodiště|Po čem schází mladý muž?|Schází po řadě kamenných schodů.|schází po řadě kamenných schodů
6849|pomalu sjíždět dlážděnou uličkou;svírat košík plný chleba;přidržovat své kolo|staré auto;košík;prádlo;dlažební kostky|Co dělá červené auto?|Auto sjíždí po kamenných schodech.|staré auto;sjíždí po kamenných schodech
4206|zívat, až praská v čelisti;nechat natéct kávu;rozsvítit se jasně zeleně|průkaz;hodiny;kancelářské křeslo;papíry|Co nosí křeček na krku?|Křeček nosí na šňůrce průkaz.|nosí na šňůrce průkaz
234|rozpustit se ve vodě;míchat vodu lžičkou;vhodit kostku cukru|lžička;zástěra;sklenice;kostka cukru|Co se stane s kostkou cukru?|Kostka cukru se úplně rozpustí.|úplně se rozpustí
5273|kráčet po molu;upravit si sluneční brýle;dát vyniknout své bundě|model;diváci;molo;strop|Co dělá model?|Kráčí po molu.|model;kráčí po molu
7835|valit se ze svahu;rudě žhnout na vrcholu;viset nad obzorem|lávový proud;kráter;stromy;mrak|Co se děje na sopce?|Ze zasněženého svahu se valí lávový proud.|valí se ze zasněženého svahu
8032|natahovat klobouk;ucuknout leknutím;chytit kamarádku za paži|zvonice;fontána;holubi;sukně|Co dělá bronzový muž?|Natahuje klobouk k mladé ženě.|natahuje klobouk k mladé ženě
278|zvedat se nad stromy;mít dlouhý cop;mít na sobě tmavě zelené legíny|slunce;palma;cop;trávník|Jaký cvik skupina dělá?|Dělají na trávníku dřepy.|dělají na trávníku dřepy
93|rozmixovat ovoce;olíznout si prst;zvednout palec|mixér;džbán;jahody;čelenka|Co připravuje muž?|Připravuje v mixéru smoothie.|připravuje v mixéru smoothie
7239|usrkávat pěnivý nápoj;mít na sobě pláštěnku;otírat se mu o hlavu|kartáč;pes;papírový kelímek;čelní sklo|Co dělá muž?|Usrkává pěnivý nápoj.|usrkává pěnivý nápoj
5712|ukazovat na doličný předmět;upustit list papíru;stát na stojanu|advokát;kolo;bláto;krabice|Co dělá advokát?|Ukazuje na zablácené kolo.|ukazuje na zablácené kolo
406|třímat těžké kladivo;připevňovat železnou spirálu;být posetý hroty|kovadlina;železná tyč;ochranné brýle;okno|Co dělá kovář?|Buší do rozžhaveného železa na kovadlině.|buší do rozžhaveného železa na kovadlině
378|sedět na zábradlí;přelétat nad střechami;vrhat dlouhé zlaté paprsky|pták;obloha;střechy|Co dělá pták?|Přelétá nad střechami při východu slunce.|přelétá nad střechami při východu slunce
6|třít si bolavá záda;zvednout palec;tvořit velmi vysokou hromadu|vousy;vesta;květináč;polštář|Co dělá muž?|Skládá si na klín polštáře.|skládá si na klín polštáře
7946|vybírat poštovní schránku;nést poštovní pytel;vystrčit hlavu z okna|stromy;poštovní schránka;dodávka;pytel|Co dělá černý pes?|Vybírá poštovní schránku do poštovního pytle.|vybírá poštovní schránku do poštovního pytle
7932|zavěsit se na obroučku;mít na sobě tmavě modrý dres;křičet radostí se zvednutýma rukama|basketbalový míč;síťka;tílko|Co dělá muž v bílém?|Visí na obroučce koše.|visí na obroučce koše
7996|jasně vyčnívat;otáčet se ve vánku;být opřený o zábradlí|stromy;větrný mlýn;kolo;tulipány|Který tulipán na poli vyčnívá?|Na poli vyčnívá červený tulipán.|vyčnívá na poli
4209|ťukat do notebooku;být ponořený do hlubokého spánku;kouknout do kamery|tulipán;notebook;maska;kabelka|Co dělá křeček s maskou?|Tvrdě spí pod svou maskou.|tvrdě spí pod svou maskou
7844|mít na sobě krátký top;mít na sobě halenku s límečkem;viset nad oknem|měděné hrnce;mísa na salát;palačinky;pracovní deska|Kdo přehazuje palačinky?|Dvě generace žen přehazují palačinky.|přehazují palačinky
4156|stát mu na hrudi;skočit pro robota;natáhnout obě ruce|živý plot;plot;robot;trávník|Co dělá robot na začátku?|Blíží se po cestičce ke kameře.|blíží se po cestičce ke kameře
8036|přitisknout se ke zdi;zaplnit celou místnost;splývat z květináče|střešní okno;stínidlo;plameňák;podlaha|Co dělá plameňák?|Zabírá celý prostor místnosti.|zabírá celý prostor místnosti
515|šplhat po lezecké stěně;viset na konci lana;povzbuzovat lezkyni|okno;lezecká stěna;lezkyně;diváci|Co dělá lezkyně?|Šplhá po lezecké stěně.|šplhá po lezecké stěně
673|naplnit pračku;nevěřit vlastním očím;srazit se praním|pihy;svetr;laclové kalhoty;pračka|Co se stalo se svetrem?|Svetr se srazil v pračce.|srazil se v pračce
5458|vykulit oči;zbarvit se do oranžova;mít vitamínovou etiketu|skříňka;vitamínová tableta;mísa s ovocem;sklenice|Co dává do sklenice?|Dává do vody vitamínovou tabletu.|dává do vody vitamínovou tabletu
343|chytit potápěčský kroužek;ležet na dně bazénu;čvachtat se v mělké části|schody;potápěčský kroužek;potápěčská maska;plavky|Co chytá žena pod vodou?|Chytá potápěčský kroužek.|chytá potápěčský kroužek
5594|sedět na hřebeni;složit svá blanitá křídla;sklonit svou rohatou hlavu|vrcholy;mraky;drak;borovice|Co dělá drak?|Impozantní drak sedí na hřebeni.|sedí na hřebeni
94|uronit slzu;zatnout zuby;vítězně se usmívat|sluneční brýle;kruhová náušnice;milkshaky;klíče od auta|Čemu se muž snaží vyhnout?|Snaží se nemrkat.|snaží se nemrkat
7981|kousnout do jahody;mít vyhrnuté rukávy;podávat jahodu|markýza;zmrzlinový pohár;karafa|Co dělají tři kamarádi?|Dělí se o zmrzlinový pohár.|dělí se o zmrzlinový pohár
7145|schovat se za dveře;funět nozdrami;projít kolem lahví od mléka|vchodové dveře;župan;lahve od mléka;dlažební kostky|Co dělá muž?|Schovává se za své vchodové dveře.|schovává se za své vchodové dveře
70|zastřihovat hustý plnovous;obdivovat svůj nový účes;odrážet jeho nadšenou tvář|holič;zákazník;ruční zrcátko;lahvičky|Co dělá holič?|Zastřihuje zákazníkovi hustý plnovous.|holič;zastřihuje zákazníkovi hustý plnovous
747|chytat se za hlavu oběma rukama;tyčit se nad stolem;ukazovat čas|hrnek;podložka s klipem;papírování;hodiny|Co dělá žena?|Hroutí se pod pracovním stresem.|hroutí se pod pracovním stresem
7870|olizovat se;viset na vidličce;třpytit se v olivovníku|pes;špagety;náramek;kamenná zeď|Co dělá pes?|S nadějí upírá oči na špagety.|s nadějí upírá oči na špagety
7016|poplácat krávu po zádech;jít podél plotu;postupovat husím pochodem|branka;kravín;konve na mléko;krávy|Co dělá žena?|Vyhání krávy z mléčné farmy.|vyhání krávy z mléčné farmy
8001|roztáhnout křídla;projet na kole kolem husy;skákat po trávníku|husa;kolo;břečťan;štěrková cesta|Co dělá žena v kraťasech?|Drží se od husy stranou.|drží se od husy stranou
7744|vyskočit z vody;pevně držet pádlo;zůstat s otevřenou pusou|velryba;loděnice;pádlo;záchranná vesta|Co dělá velryba?|Najednou vyskočí z vody.|najednou vyskočí z vody
6820|hladit slůně po zádech;cupitat vedle dospělého slona;zvednout svůj malý chobot|dospělý slon;akácie;kly;slůně|Co dělá dospělý slon?|Hladí slůně po zádech.|hladí slůně po zádech
4222|zamávat do kamery;zkřížit ruce na prsou;naklonit se k objektivu|oči;jazyk;bříško;ocas|Co dělá gekon?|Mává do kamery.|mává do kamery
7845|jemně zvedat koš;držet se koše;skotačit v trávě|horkovzdušný balon;proutěný koš;pes;tráva|Co dělá žena v modrém?|Stoupá v proutěném koši.|stoupá v proutěném koši
7563|řídit motorku;sedět v sajdkáře;výskat radostí u brány|kamenný dům;brána;spacák;štěrk|Co dělá motorkář?|Vyráží na motorce na cestu.|vyráží na motorce na cestu
5053|připevnit visačku na zavazadlo;viset na kufru;převážet zavazadla|brýle;šátek;visačka;kufr|Co dělá žena?|Připevňuje na kufr visačku.|připevňuje na kufr visačku
8000|opírat se o pult;dívat se pobaveně na psa;zvedat těžký kufr|lustr;sloup;kufr;pult|Co dělá pes?|Pes se opírá o mramorový pult.|opírá se o mramorový pult
98|zůstat s otevřenou pusou;tisknout knihu k srdci;mít vínovou obálku|houpací síť;kopule;cop;květiny|Co dělá žena?|Čte si knihu v houpací síti.|čte si knihu v houpací síti
5272|dát si ruce kolem úst;mít hustý plnovous;mít na sobě klobouk se širokou krempou|turistka;batoh;kaňon;zábradlí|Co dělají turisté?|Turisté radostně výskají nad kaňonem.|turistka;radostně výskají nad kaňonem
4424|překročit namalovanou čáru;široce se usmát do kamery;natáhnout ruku z okna|pas;strážní budka;zábradlí;kulich|Co dělá cestovatel?|Přechází pěšky hranici.|přechází pěšky hranici
4408|vypít smoothie naráz;zvednout palec;být plný ovoce|mixér;špenát;smoothie;knír|Co dělá muž?|Vychutnává si chuť svého smoothie.|vychutnává si chuť svého smoothie
5636|naklonit se přes pult;vyprsknout smíchy;držet kornout zmrzliny|lustr;příborník;zástěra;zmrzlina|Co dělá zákaznice?|Naklání se přes pult.|naklání se přes pult
8028|ukázat prstem na hromádku;zakrýt si obličej;tyčit se na pultu|lampion;čelenka;talíře;hůlky|Co dělá kuchař?|Ukazuje na hromádku talířů.|ukazuje na hromádku talířů
637|rozvinout se jako květ;tvořit velkou hromadu;rozprostírat se nad kopci|obloha;nůž;palec;granátové jablko|Co se děje s granátovým jablkem?|Rozvíjí se jako květ.|granátové jablko;rozvíjí se jako květ
7739|kutálet bochník sýra;poklepávat na bochník kladívkem;lézt po žebříku|lucerna;okno;žebřík;kbelík|Co kutálí myš s kšiltovkou?|Kutálí těžký bochník sýra.|kutálí těžký bochník sýra
7813|bubnovat na obrácené kbelíky;mít na sobě růžový svetr;odrážet zatažené nebe|slunečníky;fontána;kbelíky;louže|Co dělá duo?|Duo bubnuje na modré kbelíky.|bubnuje na modré kbelíky
7997|být hvězdou představení;pokleknout na jedno koleno;tančit na vysokých podpatcích|závěsy;reflektor;večerní šaty;rampová světla|Co dělá žena ve zlatých šatech?|Je hvězdou představení.|je hvězdou představení
7748|malovat sochu draka;zívat při pití kávy;dřímat na modrém polštáři|drak;plechovky s barvou;krabice od pizzy;deka|Co dělá žena v laclových kalhotách?|Maluje sochu draka.|maluje sochu draka
7450|tvarovat velkou vázu;strčit ruku do vázy;pracovat v pozadí|pec;keramička;váza;houba|Co dělá keramička v popředí?|Tvaruje velkou hliněnou vázu.|keramička;tvaruje velkou hliněnou vázu
7040|kutálet se po herním plánu;držet se za hlavu oběma rukama;hodit kostkou|kostka;popcorn;herní plán;náhrdelníky|Co se kutálí po herním plánu?|Po herním plánu se kutálí bílá kostka.|kutálí se po herním plánu
5517|přijmout žádost o ruku;klečet na dece;nést rybářský prut|krabička na prsten;piknikový koš;deka;stopy|Co dělá žena?|Přijímá jeho žádost o ruku.|přijímá jeho žádost o ruku
4125|zatáhnout za závoj;vybuchnout v déšť okvětních lístků;zvednout chobot|reflektor;slon;kostým;jeviště|Co dělá šedý slon?|Zvedá na jevišti chobot.|zvedá na jevišti chobot
347|šeptat si drby;tlumit výkřik rukama;mít na sobě proužkovanou košili|markýza;kudrny;cop;stůl|Co dělá mladá žena s brýlemi?|Šeptá jí do ucha drby.|šeptá jí do ucha drby
7849|viset nad střešní terasou;tyčit se na obzoru;ležet na prkénku|světelné řetězy;hora;pizza;karafa|Co dělají kamarádi?|Dělí se o pizzu na střešní terase.|dělí se o pizzu na střešní terase
4920|zalévat mladé sazenice;být pruhovaný všemi barvami;tyčit se nad davem|obloha;cedule;chlapec;vyvýšený záhon|Co dělá světlovlasá žena?|Zalévá mladé sazenice v komunitní zahradě.|zalévá mladé sazenice v komunitní zahradě
4434|tisknout plyšového medvídka;lízat zmrzlinu;půjčit jí svou bundu|obloha;pouť;kornout zmrzliny;plyšový medvídek|Co dělá na pouti?|Tiskne obřího plyšového medvídka.|pouť;tiskne obřího plyšového medvídka
7154|udržovat rovnováhu na jednokolce;usrkávat kávu s sebou;šlapat za jednokolkou|patrový autobus;taxík;aktovka;jednokolka|Jak se podnikatel pohybuje?|Jezdí na jednokolce.|jezdí na jednokolce
5417|nastoupit do staré tramvaje;nabrat cestující;rozhlédnout se po depu|trolejové vedení;koleje;plátěná taška;cop|Co dělá na konci?|Rozhlíží se po depu.|rozhlíží se po depu
4918|vybíhat schody po čtyřech;s námahou nést těžké tašky;zvednout palec|schodiště;mikina s kapucí;džíny;papírová taška|Co nese mladý muž?|Nese po schodech papírové tašky.|nese po schodech papírové tašky
7369|objet velrybu na pádle;vyfukovat sloup páry;vztyčit ocas nad vodu|paddleboard;velryba;loď;hory|Co dělá žena?|Objíždí velkou velrybu.|objíždí velkou velrybu
5502|skládat krabice na sebe;převážet naloženou paletu;ovinout krabice fólií|krabice;paletový vozík;reflexní vesta;regály|Co dělá žena?|Skládá krabice na paletu.|skládá krabice na paletu
730|utírat kuchyňský pult;rozprostřít ubrus;podávat cappuccino|personál;hosté;ubrus;závěsná světla|Co dělá servírka?|Rozprostírá bílý ubrus.|personál;rozprostírá bílý ubrus
230|zvednout pěsti na znamení vítězství;mít na sobě pirátský kostým;stát na stativu|režisérka;kamera;skládací židle;slunce|Co dělá režisérka?|Zvedá pěsti na znamení vítězství.|režisérka;zvedá pěsti na znamení vítězství
7119|vytahovat těžkou síť;mít na sobě žlutou pláštěnku;přetékat stříbrnými rybami|racek;síť;bedna;rybářka|Co dělá rybářka v oranžovém?|Vytahuje těžkou síť.|rybářka;vytahuje těžkou síť
4930|nadšeně zvednout ruku;hrdě ukázat svůj sešit;třpytit se na stránce|zlatá hvězda;kroužkový sešit;bílá tabule|Jakou odměnu dívka dostává?|Dostává za odměnu zlatou hvězdu.|dostává za odměnu zlatou hvězdu
5358|nakouknout mezi dvěma hromádkami;skládat na sebe tlusté knihy;opřít si bradu o ruku|police;brýle;svetr;učebnice|Co dělá schovaná žena?|Nakukuje mezi knihami.|nakukuje mezi knihami
7|mávat svým diplomem;usmívat se od ucha k uchu;obejmout jiného absolventa|diplom;stadion;absolventská čepice;šerpa|Co dělá muž?|Mává diplomem na promoci.|mává diplomem na promoci
4360|nakouknout do tašky;nést tašky v natažených rukou;hrdě předvádět svou kabelku|papírové tašky;kabelka;cestovní taška;eskalátor|Co žena hrdě předvádí?|Předvádí svou kabelku na eskalátoru.|předvádí svou kabelku na eskalátoru
5379|vzít zákazníkovi míry;označit látku křídou;obléct si sako|stropní ventilátor;látky;sako;krejčovský metr|Co dělá krejčí?|Upravuje zákazníkovi sako.|upravuje zákazníkovi sako
798|zapnout si zip na bundě;zalévat květiny v květináčích;mít hustý knír|prádlo;skútr;tepláková souprava;konev|Co dělá mladá žena?|Tančí v tyrkysové teplákové soupravě.|tančí v tyrkysové teplákové soupravě
7200|řídit paraglidové křídlo;zvednout pilota do vzduchu;vlát ve větru|paraglidové křídlo;větrný rukáv;záliv;skalní římsa|Co dělá pilot?|Plachtí nad tyrkysovým zálivem.|plachtí nad tyrkysovým zálivem
376|valit se do soutěsky;vřít mezi skalami;tyčit se v dálce|les;útes;peřeje|Co dělá řeka?|Vine se divokou přírodou.|vine se divokou přírodou
5538|táhnout naložený přívěs;tyčit se na obzoru;zbarvit se do oranžova a růžova|sila;kombajn;traktor;pšenice|Co dělají stroje?|Sklízejí pšenici při západu slunce.|sklízejí pšenici při západu slunce
5117|listovat knihou v pevné vazbě;zůstat s otevřenou pusou;prohýbat se pod knihami|brýle;police;džínová bunda;kniha v pevné vazbě|Co dělá mladý muž?|Listuje v knihkupectví knihou v pevné vazbě.|listuje v knihkupectví knihou v pevné vazbě
6836|vytahovat gauč;viset na konci lana;zvednout pěst|bytový dům;gril;gauč;dodávka|Co dělá mladá žena?|Vytahuje gauč podél bytového domu.|vytahuje gauč podél bytového domu
5540|šplhat po stěně;dřepnout si na žíněnku;chytit se velkého chytu|copánky;culík;žíněnka;pytlík na magnézium|Co dělá žena s copánky?|Šplhá po stěně s pomocí jiné ženy.|šplhá po stěně s pomocí jiné ženy
5671|zvednout pěst;vyjet do kopce na kole;běžet vedle cyklistky|zasněžené vrcholy;helma;kamenná zeď;spadané listí|Co dělá muž?|Hlasitě povzbuzuje cyklistku.|hlasitě povzbuzuje cyklistku
124|kousnout do svého chleba;mít na sobě proužkovanou zástěru;rozpouštět se na chlebu|máslo;nůž;zástěra;pánve|Co dělá dívka?|Maže si chleba máslem.|maže si chleba máslem
4364|žasnout nad croissanty;mít na sobě květovanou zástěru;upéct croissanty dozlatova|těsto;mouka;zástěra;okno|Co dělají ty dvě ženy?|Tvarují kuličky z těsta.|tvarují kuličky z těsta
7453|přehazovat nudle;podávat talíř;olizovat dno woku|wok;plameny;naběračka;šátek|Co dělá kuchařka?|Připravuje smažené nudle ve woku.|připravuje smažené nudle ve woku
7883|klečet na cestě;olíznout ženě tvář;držet vodítko štěněte|štěně;kolo;lavička;pouliční lampa|Co dělá klečící žena?|Září radostí a mazlí se se štěnětem.|září radostí a mazlí se se štěnětem
'''
src=json.load(open(f'{H}/tr/b002/source_fr.json'))
out={};err=[]
for line in D.strip().split('\n'):
    k,p,n,q,a,x=line.split('|')
    P=p.split(';');N=n.split(';');X=x.split(';')
    s=src[k]
    if len(P)!=3 or len(N)!=len(s['nouns']) or len(P)+len(X)!=len(s['recall']): err.append(k)
    out[k]={'phrases':P,'nouns':N,'question':q,'answer':a,'captions':{},'recall':P+X}
print('err',err,'missing',set(src)-set(out))
out={k:out[k] for k in src if k in out}
json.dump(out,open(f'{H}/tr/b002/fr/cz.json','w'),ensure_ascii=False,indent=1)
