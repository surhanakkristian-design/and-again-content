import json,os
H=os.path.dirname(os.path.abspath(__file__))
src=json.load(open(f'{H}/tr/b002/source_es.json'))
# id: phrases | nouns | question | answer | extra recall (non-phrase, non-noun rows, in order)
D=r"""
620|čichat k růži;zavřít oči;svítit na obloze|žena;růže;košík;slunce|Co dělá žena?|Žena čichá k růži.|čichá k růži
5310|obejmout svého syna;mít na sobě šedé tričko;letět před garáží|chlapec;míč;muž|Co dělá žena?|Žena objímá svého syna.|objímá svého syna
41|držet kladivo;mít černé vlasy;viset na zdi|obraz;kladivo;žena;muž|Co dělají muž a žena?|Hádají se.|Hádají se
5499|mít na sobě červené šaty;běžet po ulici;zalévat květiny|žena;květiny;okno;zeď|Co dělá starší žena?|Starší žena zalévá květiny.|zalévá květiny
119|vydávat teplé světlo;držet šálek;mít šedou srst|žárovka;kočka;miska;knihy|Co drží žena?|Žena drží šálek.|drží šálek
166|nakreslit velký kruh;držet dlouhou hůl;vytvořit kruh|žena;obloha;kruh;moře|Co kreslí žena?|Kreslí kruh do písku.|Kreslí kruh do písku
596|vyhrát závod;být ve žlutém;být ve fialovém|běžci;tráva;dráha|Kdo vyhrává závod?|Běžkyně ve žlutém vyhrává závod.|vyhrává závod
484|vytírat podlahu;málem upadnout;být plný vody|žena;mop;kbelík;podlaha|Co dělá žena?|Vytírá podlahu mopem.|Vytírá podlahu mopem
68|usmívat se do kamery;nosit brýle;obepínat zápěstí|brýle;palec;obvaz;lavička|Co dělá muž?|Dává jí obvaz na zápěstí.|Dává jí obvaz na zápěstí
5149|nést papírovou tašku;lézt po vysokém žebříku;svítit zeleně|kříž;lahvičky;šála;krabice|Co dělá muž v bílém?|Leze po vysokém žebříku.|Leze po vysokém žebříku
457|zavřít oči;mít na sobě zelené tričko;ležet za ženami|světlo;zrcadlo;pes;make-up|Kde leží pes?|Pes leží za ženami.|leží za ženami
36|mazlit se se svou zrzavou kočkou;zůstat viset ve vzduchu;vzít svého mazlíčka do náruče|květináč;kočka;polštář;kardigan|Co dělá žena?|Mazlí se s kočkou, kterou zbožňuje.|Mazlí se s kočkou, kterou zbožňuje
676|fotografovat památky;řídit gondolu veslem;tyčit se nad náměstím|zvonice;kupole;fotoaparát;gondola|Co dělají ti dva turisté?|Prohlížejí si město z gondoly.|Prohlížejí si město z gondoly
7962|držet kartonovou krabici;obsahovat zbytek pizzy;viset nad střešní terasou|světelný řetěz;komín;krabice od pizzy;koberec|Co obsahuje krabice od pizzy?|Obsahuje zbytek pizzy.|Obsahuje zbytek pizzy
7858|balancovat na laně;clonit si oči rukou;mávat z útesu|obloha;útes;řeka;fleecová mikina|Kde balancuje žena v oranžovém?|Balancuje v půli cesty mezi oběma útesy.|Balancuje v půli cesty mezi oběma útesy
7124|sejít po schodišti;jásat z balkonu;spočívat na stříbrném podnose|hosté;svatební dort;smoking;schodiště|Po čem schází mladý muž?|Schází po kamenném schodišti.|Schází po kamenném schodišti
6849|sjíždět dlážděnou uličkou;vyklánět se s košíkem chleba;držet kolo|automobil;košík;prádlo na šňůře;dlažební kostky|Co dělá červený automobil?|Automobil sjíždí dlážděnou uličkou.|sjíždí dlážděnou uličkou
4206|nepokrytě zívat;nalévat čerstvě uvařenou kávu;rozsvítit se zeleně|visačka;hodiny;kancelářská židle;papíry|Co má křeček na krku?|Křeček má na krku visačku.|má na krku visačku
234|rozpouštět se ve vodě;míchat lžičkou;hodit do vody kostku cukru|lžička;zástěra;sklenice;kostka cukru|Co se děje s kostkou cukru?|Kostka cukru se rozpouští ve vodě.|rozpouští se ve vodě
5273|kráčet po molu;upravit si sluneční brýle;předvádět svou džínovou bundu|model;diváci;molo;strop|Co dělá model?|Model kráčí po molu.|kráčí po molu
7835|stékat po svahu;zářit na vrcholu;vznášet se nad obzorem|lávový proud;kráter;stromy;mrak|Co se děje na sopce?|Po svahu stéká lávový proud.|stéká po svahu
8032|podávat svůj klobouk;uskočit leknutím;chytit kamarádku za paži|hodinová věž;fontána;holubi;sukně|Co dělá bronzový muž?|Nečekaně nabízí dívce svůj klobouk.|Nečekaně nabízí dívce svůj klobouk
278|vykukovat nad stromy;mít dlouhý cop;mít na sobě tmavě zelené legíny|slunce;palma;cop;trávník|Jaký cvik dělá skupina?|Dělají dřepy na trávníku.|Dělají dřepy na trávníku
93|rozmixovat ovoce;olíznout si prst;zvednout palec|mixér;džbán;jahody;čelenka|Co připravuje muž?|Připravuje v mixéru koktejl.|Připravuje v mixéru koktejl
7239|usrkávat zpěněný nápoj;mít na sobě žlutou pláštěnku;třít mu hlavu|kartáč;pes;papírový kelímek;čelní sklo|Co dělá muž?|Usrkává svůj nápoj se zavřenýma očima.|Usrkává svůj nápoj se zavřenýma očima
5712|ukázat na důkaz;upustit list papíru;stát na stojanu|právník;kolo;bláto;kartonové krabice|Co dělá právník?|Ukazuje na zablácené kolo.|Ukazuje na zablácené kolo
406|máchat těžkým kladivem;připevnit železnou spirálu;mít ostré hroty|kovadlina;železná tyč;ochranné brýle;okno|Co dělá kovář?|Buší do rozžhaveného železa na kovadlině.|Buší do rozžhaveného železa na kovadlině
378|usednout na zábradlí;přelétat nad střechami;vrhat dlouhé zlaté paprsky|pták;obloha;střechy|Co dělá pták?|Za úsvitu přelétá nad střechami.|Za úsvitu přelétá nad střechami
6|třít si bolavá záda;zvednout palec;vršit se jeden na druhý|vousy;pletený svetr;květináč;polštář|Co dělá muž?|Vrší si polštáře na klín.|Vrší si polštáře na klín
7946|vyprázdnit poštovní schránku;nést na zádech poštovní pytel;vystrčit hlavu z okénka|stromy;poštovní schránka;dodávka;pytel|Co dělá černý pes?|Vyprazdňuje červenou poštovní schránku do pytle.|Vyprazdňuje červenou poštovní schránku do pytle
7932|zavěsit se na obroučku;mít na sobě tmavomodrý dres;jásat se zdviženýma rukama|míč;síťka;tílko|Co dělá chlapec v bílém?|Po smeči se věší na obroučku.|Po smeči se věší na obroučku
7996|vyčnívat mezi ostatními;otáčet se ve větru;být opřené o zábradlí|stromy;větrný mlýn;kolo;tulipány|Který tulipán vyčnívá na poli?|Na poli vyčnívá červený tulipán.|vyčnívá na poli
4209|psát na notebooku;spát tvrdým spánkem;kouknout do kamery|tulipán;notebook;maska;kabelka|Co dělá křeček s maskou?|Je ponořený do hlubokého spánku.|Je ponořený do hlubokého spánku
7844|mít na sobě krátký top;nosit košili s límečkem;viset nad oknem|měděné rendlíky;mísa;palačinky;kuchyňská linka|Kdo obrací palačinky?|Palačinky obracejí dvě generace žen.|obracejí palačinky
4156|postavit se mu na hruď;vrhnout se po robotovi;natáhnout obě ruce|živý plot;plot;robot;trávník|Co dělá robot na začátku?|Blíží se po cestě ke kameře.|Blíží se po cestě ke kameře
8036|mačkat se ke zdi;zabírat celý pokoj;viset z květináče|střešní okno;stínidlo lampy;plameňák;podlahová prkna|Co dělá plameňák?|Plameňák zabírá téměř celý objem pokoje.|zabírá téměř celý objem pokoje
515|šplhat po lezecké stěně;zůstat viset na laně;povzbuzovat zdola|okno;lezecká stěna;lezkyně;diváci|Co dělá lezkyně?|Lezkyně šplhá po stěně.|šplhá po stěně
673|naplnit pračku;dívat se nevěřícně;srazit se v praní|pihy;svetr;laclové kalhoty;pračka|Co se stalo se svetrem?|Svetr se v pračce srazil.|srazil se v pračce
5458|napít se ze sklenice;šumět a zoranžovět;mít etiketu s vitamíny|skříňka;vitamínová tableta;mísa na ovoce;sklenice|Co žena vhazuje do sklenice?|Vhazuje do ní vitamínovou tabletu.|Vhazuje do ní vitamínovou tabletu
343|chytit potápěčský kroužek;ležet na dně;brodit se mělkou vodou|schody;potápěčský kroužek;potápěčské brýle;plavky|Co žena chytá pod vodou?|Chytá potápěčský kroužek.|Chytá potápěčský kroužek
5594|usednout na skalnatý hřeben;složit křídla;sklonit hlavu|štíty;mraky;drak;borovice|Co dělá drak?|Úžasný drak usedá na hřeben.|usedá na hřeben
94|uronit slzu;zatnout zuby;vítězoslavně se usmívat|sluneční brýle;kruhová náušnice;mléčné koktejly;klíčky od auta|Čemu se chlapec snaží vyhnout?|Chlapec se snaží nemrknout.|snaží se nemrknout
7981|vychutnávat zmrzlinu se zavřenýma očima;mít vyhrnuté rukávy;nabízet jahodu|markýza;zmrzlinový pohár;džbán|Co dělají tři přátelé?|Tři přátelé se dělí o zmrzlinový pohár.|dělí se o zmrzlinový pohár
7145|schovat se za vchodovými dveřmi;funět na chlapce;procházet se kolem lahví|vchodové dveře;župan;lahve od mléka;dlažební kostky|Co dělá chlapec?|Chlapec se schovává za vchodovými dveřmi.|schovává se za vchodovými dveřmi
70|zastřihovat hustý plnovous;obdivovat svůj nový účes;odrážet nadšenou tvář zákazníka|holič;zákazník;ruční zrcátko;lahvičky|Co dělá holič?|Holič zastřihuje zákazníkovi hustý plnovous.|zastřihuje zákazníkovi hustý plnovous
747|chytat se za hlavu;vršit se na stole;ukazovat čas|hrnek;psací podložka;papíry;hodiny|Co dělá žena?|Ze stresu se chytá za hlavu.|Ze stresu se chytá za hlavu
7870|dívat se s nadějí na jídlo;viset z vidličky;svítit v olivovníku|pes;špagety;náramek;kamenná zídka|Co dělá pes?|Upřeně hledí na špagety na vidličce.|Upřeně hledí na špagety na vidličce
7016|poplácávat krávu;procházet se podél plotu;jít husím pochodem|branka;kravín;konve na mléko;krávy|Co dělá žena?|Na mléčné farmě poplácává krávu.|Na mléčné farmě poplácává krávu
8001|roztáhnout křídla;šlapat na kole vedle husy;skočit na trávník|husa;kolo;břečťan;štěrková cesta|Co dělá žena v kraťasech?|Drží se od husy dál.|Drží se od husy dál
7744|náhle vyskočit z vody;pevně sevřít pádlo;zůstat s otevřenou pusou|velryba;loděnice;pádlo;záchranná vesta|Co dělá velryba?|Dopadá do vody.|Dopadá do vody
6820|hladit mládě po hřbetě;klusat vedle dospělého;zvedat svůj krátký chobot|dospělý jedinec;akácie;kly;mládě|Co dělá dospělý slon?|Hladí mládě po hřbetě.|Hladí mládě po hřbetě
4222|mávat do kamery;založit si ruce;přiblížit se k objektivu|oči;jazyk;bříško;ocas|Co dělá gekon?|Mává do kamery.|Mává do kamery
7845|jemně zvedat koš;držet se proutěného koše;pobíhat po trávě|horkovzdušný balon;proutěný koš;pes;tráva|Co dělá žena v modrém?|Vzlétá v proutěném koši.|Vzlétá v proutěném koši
7563|řídit motorku;sedět v sajdkáře;jásat u brány|chalupa;brána;spacák;štěrk|Co dělá motorkář?|Vyráží na své motorce na cestu.|Vyráží na své motorce na cestu
5053|připevnit zavazadlový štítek;viset na kufru;přepravovat zavazadla|brýle;šátek;štítek;kufr|Co dělá žena?|Připevňuje na svůj kufr štítek.|Připevňuje na svůj kufr štítek
8000|opírat se o pult;pukat smíchy se psem;tahat těžký kufr|lustr;sloup;kufr;recepční pult|Co dělá pes?|Pes se opírá o mramorový pult.|opírá se o mramorový pult
98|zakrýt si ústa v úžasu;tisknout knihu k hrudi;mít vínově červené desky|houpací síť;kupole;cop;květiny|Co dělá dívka?|Čte knihu v houpací síti.|Čte knihu v houpací síti
5272|dát si dlaně kolem úst;mít hustý plnovous;nosit klobouk se širokou krempou|turistka;batoh;kaňon;zábradlí|Co dělají turisté?|Turisté radostně křičí u kaňonu.|radostně křičí u kaňonu
4424|přejít namalovaný pruh;usmívat se od ucha k uchu;vystrčit ruku z okénka|pas;budka;zábradlí;čepice|Co dělá cestovatel?|Cestovatel přechází hranici pěšky.|přechází hranici pěšky
4408|připravit ovocný koktejl;zvednout palec;být po okraj plný ovoce|mixér;špenát;koktejl;knír|Co dělá chlapec?|Chlapec si vychutnává chuť svého koktejlu.|vychutnává si chuť svého koktejlu
5636|naklonit se přes pult;rozesmát se;držet kornout|lustr;vitrína;zástěra;zmrzlina|Co dělá zákaznice?|Naklání se přes pult se zmrzlinou.|Naklání se přes pult se zmrzlinou
8028|ukázat na hromadu talířů;mávat rukama;tyčit se nad barem|lampion;čelenka;talíře;hůlky|Co dělá kuchař?|Ukazuje na hromadu talířů.|Ukazuje na hromadu talířů
637|otevřít se jako květ;tvořit hromadu;rozprostírat se nad zelenými kopci|obloha;nůž;palec;granátové jablko|Co se děje s granátovým jablkem?|Granátové jablko se otevírá jako květ.|otevírá se jako květ
7739|kutálet bochník sýra;ťukat kladívkem;šplhat po žebříku|lucerna;okno;žebřík;kbelík|Co myš kutálí?|Myš kutálí bochník sýra.|kutálí bochník sýra
7813|bubnovat na obrácené kbelíky;mít na sobě růžový svetr;odrážet zatažené nebe|slunečníky;fontána;kbelíky;kaluž|Co dělá duo?|Duo bubnuje na modré kbelíky.|bubnuje na modré kbelíky
7997|hrát hlavní roli v představení;pokleknout na jedno koleno;tančit na vysokých podpatcích|opona;reflektor;večerní šaty;rampová světla|Co dělá žena ve zlatém?|Hraje hlavní roli v představení.|Hraje hlavní roli v představení
7748|malovat sochu draka;zívat s kávou v ruce;podřimovat na modrém polštáři|drak;plechovky od barvy;krabice od pizzy;deka|Co dělá dívka v laclových kalhotách?|Maluje sochu draka.|Maluje sochu draka
7450|tvarovat vysokou vázu;vložit ruce do vázy;pracovat v zadní části dílny|pec;keramička;váza;houba|Co dělá keramička vpředu?|Keramička tvaruje hliněnou vázu.|tvaruje hliněnou vázu
7040|kutálet se po hrací desce;chytat se za hlavu;hodit kostkou|kostka;popcorn;hrací deska;náhrdelníky|Co se kutálí po hrací desce?|Po hrací desce se kutálí bílá kostka.|kutálí se po hrací desce
5517|přijmout žádost o ruku;klečet na dece;nést rybářský prut|krabička na prsten;piknikový koš;deka;stopy|Co dělá dívka?|Přijímá jeho žádost o ruku.|Přijímá jeho žádost o ruku
4125|táhnout za látku;rozpadnout se v okvětní lístky;zvednout chobot|reflektor;slon;oblek;jeviště|Co dělá šedý slon?|Na jevišti zvedá chobot.|Na jevišti zvedá chobot
347|šeptat drby do ucha;zakrýt si ústa rukama;mít na sobě pruhovanou košili|markýza;kudrnaté vlasy;cop;stůl|Co dělá dívka s brýlemi?|Šeptá mu do ucha drby.|Šeptá mu do ucha drby
7849|viset nad střešní terasou;tyčit se na obzoru;ležet na dřevěném prkénku|světelné řetězy;hora;pizza;džbán|Co dělají přátelé?|Dělí se o pizzu, která vystačí pro všechny.|Dělí se o pizzu, která vystačí pro všechny
4920|zalévat sazenice;mít barevné pruhy;tyčit se nad skupinou|obloha;cedule;chlapec;vyvýšený záhon|Co dělá blonďatá dívka?|Zalévá sazenice v komunitní zahradě.|Zalévá sazenice v komunitní zahradě
4434|obejmout plyšového medvídka;lízat zmrzlinu;sundat si bundu|obloha;pouť;kornout;plyšový medvídek|Co dělá dívka na pouti?|Objímá obřího plyšového medvídka.|Objímá obřího plyšového medvídka
7154|udržovat rovnováhu na jednokolce;usrkávat kávu;šlapat za jednokolkou|patrový autobus;taxík;aktovka;jednokolka|Jak se podnikatel přepravuje?|Přepravuje se na jednokolce.|Přepravuje se na jednokolce
5417|nastoupit do historické tramvaje;nabrat cestující;rozhlédnout se po vozovně|trolejové dráty;koleje;plátěná taška;cop|Co dělá dívka na konci?|Prohlíží si tramvaje ve vozovně.|Prohlíží si tramvaje ve vozovně
4918|rychle vyběhnout po schodech;neunést tašky;zvednout palec|schody;mikina;džíny;papírová taška|Co nese chlapec?|Nese papírové tašky nahoru po schodech.|Nese papírové tašky nahoru po schodech
7369|pádlovat kolem velryby;vypustit proud vody;vystrčit ocas z vody|paddleboard;velryba;loď;hory|Co dělá dívka?|Objíždí na svém prkně obrovskou velrybu.|Objíždí na svém prkně obrovskou velrybu
5502|stohovat kartonové krabice;převážet naloženou paletu;balit krabice do fólie|kartonové krabice;paletový vozík;reflexní vesta;regály|Co dělá žena?|Stohuje kartonové krabice na paletu.|Stohuje kartonové krabice na paletu
730|otírat linku hadrem;rozprostřít ubrus;podávat cappuccino na baru|personál;strávníci;ubrus;závěsná světla|Co dělá servírka?|Servírka rozprostírá bílý ubrus.|rozprostírá bílý ubrus
230|dávat herci pokyny;mít na sobě pirátský kostým;být upevněná na stativu|filmová režisérka;filmová kamera;skládací židle;slunce|Co dělá režisérka?|Režisérka vítězoslavně zvedá pěsti.|vítězoslavně zvedá pěsti
7119|vytáhnout síť na palubu;mít na sobě žluté nepromokavé oblečení;přetékat stříbrnými rybami|racek;síť;bedna;rybářka|Co dělá rybářka v oranžovém?|Rybářka táhne síť plnou ryb.|táhne síť plnou ryb
4930|nadšeně zvednout ruku;hrdě ukázat svůj sešit;zářit na stránce|zlatá hvězdička;kroužkový sešit;bílá tabule|Jakou odměnu dostává žákyně?|Žákyně dostává jako odměnu zlatou hvězdičku.|dostává jako odměnu zlatou hvězdičku
5358|vykukovat mezi knihami;skládat na sebe těžké knihy;opírat si hlavu o ruku|regály;brýle;kardigan;učebnice|Co dělá schovaná dívka?|Dívka vykukuje mezerou mezi knihami.|vykukuje mezerou mezi knihami
7|zvednout diplom;usmívat se od ucha k uchu;obejmout jiného absolventa|diplom;stadion;absolventská čapka;šerpa|Co dělá chlapec?|Na své promoci zvedá diplom.|Na své promoci zvedá diplom
4360|nahlédnout do tašky;nést několik nákupních tašek;chlubit se svou kabelkou|papírové tašky;kabelka;cestovní taška;eskalátor|Čím se žena chlubí?|Na eskalátoru se chlubí svou kabelkou.|Na eskalátoru se chlubí svou kabelkou
5379|vzít zákazníkovi míry;označit látku křídou;vyzkoušet si sako|stropní ventilátor;látka;sako;krejčovský metr|Co dělá krejčí?|Upravuje sako pro zákazníka.|Upravuje sako pro zákazníka
798|zapnout si zip na bundě;zalévat květináče;mít hustý knír|prádlo na šňůře;motorka;tepláková souprava;konev|Co dělá dívka?|Tančí v tyrkysové teplákové soupravě.|Tančí v tyrkysové teplákové soupravě
7200|létat na paraglidu;zvedat pilota;vlát ve větru|paraglidový padák;větrný rukáv;záliv;skalní výstupek|Co dělá pilot?|Plachtí nad tyrkysovým zálivem.|Plachtí nad tyrkysovým zálivem
376|razit si cestu soutěskou;pěnit mezi skalami;tyčit se v dálce|les;útes;peřeje|Co dělá řeka?|Řeka protéká divokou přírodou.|protéká divokou přírodou
5538|táhnout přívěs plný obilí;rýsovat se na obzoru;zbarvit se do oranžova a růžova|sila;kombajn;traktor;pšenice|Co dělají stroje?|Stroje sklízejí zlatou pšenici.|sklízejí zlatou pšenici
5117|listovat knihou v pevné vazbě;zůstat s otevřenou pusou;být plný knih|brýle;regály;džínová bunda;kniha v pevné vazbě|Co dělá chlapec?|Chlapec listuje knihou v knihkupectví.|listuje knihou v knihkupectví
6836|vytáhnout gauč na balkon;viset na laně;zvednout pěst|bytový dům;gril;gauč;dodávka|Co dělá dívka?|Dívka vytahuje gauč na svůj balkon.|vytahuje gauč na svůj balkon
5540|šplhat po stěně;dřepnout si na žíněnku;chytit se velkého chytu|copy;culík;žíněnka;pytlík na magnézium|Co dělá dívka s copy?|Leze po stěně s pomocí své parťačky.|Leze po stěně s pomocí své parťačky
5671|zvednout pěst;vyjet na kole do kopce;běžet vedle cyklistky|zasněžené štíty;helma;kamenná zídka;spadané listí|Co dělá muž?|Povzbuzuje cyklistku.|Povzbuzuje cyklistku
124|kousnout do chleba;mít na sobě pruhovanou zástěru;rozpouštět se na chlebu|máslo;nůž;zástěra;pánve|Co dělá dívka?|Maže chleba máslem.|Maže chleba máslem
4364|užasle zírat na croissanty;mít na sobě květovanou zástěru;sálat teplem|těsto;mouka;zástěra;okno|Co dělají ty dvě ženy?|Tvarují kuličky z těsta.|Tvarují kuličky z těsta
7453|restovat nudle;držet talíř;plápolat pod wokem|wok;plameny;naběračka;šátek|Co dělá kuchařka?|Připravuje nudle ve woku.|Připravuje nudle ve woku
7883|klečet na cestičce;lízat dívku po tváři;držet štěně na vodítku|štěně;kolo;lavička;pouliční lampa|Co dělá klečící dívka?|Radostně objímá štěně.|Radostně objímá štěně
"""
out={}
for line in D.strip().split('\n'):
    vid,ph,no,q,a,ex=line.split('|')
    s=src[vid]; ph=ph.split(';'); no=no.split(';'); ex=ex.split(';')
    assert len(ph)==len(s['phrases']) and len(no)==len(s['nouns']), vid
    rec=[]; it=iter(ex)
    for r in s['recall']:
        pt=[p['text'] for p in s['phrases']]
        if r in pt: rec.append(ph[pt.index(r)])
        elif r in s['nouns']: rec.append(no[s['nouns'].index(r)])
        else: rec.append(next(it))
    assert next(it,None) is None, ('extra',vid)
    out[vid]=dict(phrases=ph,nouns=no,question=q,answer=a,captions={},recall=rec)
json.dump(out,open(f'{H}/tr/b002/es/cz.json','w'),ensure_ascii=False,indent=1)
