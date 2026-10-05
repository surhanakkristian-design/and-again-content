import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """443|držať baterku;mať na sebe modrý sveter;vyzerať ako kôň|svetlo;žena;krabice;hračkársky kôň|Čo preniká cez okno?|Cez okno preniká svetlo.
444|zakrývať si tvár;mať na sebe sivé tričko;osvetliť oblohu|blesk;oblaky;strom;okuliare|Na čo sa pozerajú?|Pozerajú sa na blesk.
445|kráčať v zelených čižmách;mať na hlave modrú šiltovku;byť dlhá a biela|čiara;žena;tráva;kopec|Na čom stojí žena?|Stojí na bielej čiare.
446|otvoriť tlamu dokorán;kráčať trávou;mať plochú korunu|lev;strom;tráva|Čo robí lev?|Otvára tlamu dokorán.
447|držať balzam na pery;vyskúšať jej balzam na pery;mať na sebe modrý kabátik|sneh;pes;šál;balzam na pery|Čo robí žena?|Nanáša si balzam na pery.
448|nanášať ružový lesk na pery;poklepať si na spodnú peru;pozerať sa ponad slnečné okuliare|zábradlie;miska;lesk na pery|Čo robí žena vo fialovom?|Nanáša si lesk na pery.
450|sedieť na slnku;zdvihnúť hlavu;liezť hore po múre|kaktus;tieň;jašterica;kameň|Čo robí jašterica?|Lezie hore po múre.
451|zamknúť dvere;odísť;vsunúť sa do zámky|vlasy;kľúč;kabát;taška|Čo robí žena?|Zamyká dvere kľúčom.
452|načrtnúť logo;mať hustú bradu;driemať na stole|logo;okuliare;notebook;stôl|Čo kreslí žena?|Načrtáva logo na papier.
453|jesť zelený hrášok;držať vidličku;sedieť sám|chlapec;hrášok;telefón;okná|Čo chlapec je?|Je zelený hrášok sám.
454|spať na jeho pleci;sedieť pod dekou;objímať ženu|muž;polievka;deka;čižmy|Čo robí muž?|Objíma spiacu ženu.
455|zhlboka dýchať;nafúknuť červený balón;dosiahnuť obrovskú veľkosť|balón;tričko;legíny;trávnik|Čo robí žena?|Nafukuje obrovský červený balón.
456|obracať stránky;spať na stoličke;mať na sebe modrý top|okno;rastlina;mačka;časopisy|Čo robia tie dve ženy?|Prezerajú si časopis.
458|bežať za vtákmi;niesť veľkú debnu;mať tmavú kravatu|obloha;budova;muž;vtáky|Čo robí mladý muž?|Beží za vtákmi.
459|písať na podložku s klipom;ukázať palec hore;mať oholenú hlavu|manažérka;podložka s klipom;debničky;kvety|Čo robí manažérka?|Píše na podložku s klipom.
462|mať na hlave červenú čiapku;bežať s mapou;letieť vzduchom|čiapka;okuliare;košeľa;mapa|Na čo sa pozerajú?|Pozerajú sa na mapu.
464|používať ružovú fixku;mať na sebe modré tričko;mať čierny chvost|muž;žena;fixka;stôl|Čím kreslí žena?|Kreslí ružovou fixkou.
465|niesť košík;predávať paradajky;krájať syr|žena;syr;paradajky;košík|Čo robí žena v modrom?|Nesie košík na trhu.
466|nanášať čiernu riasenku;stáť v pozadí;vykúkať z košíka|riasenka;pohár na víno;štetce na líčenie|Čo robí ryšavá žena?|Nanáša si riasenku na mihalnice.
467|tvarovať vysokú vázu;rozhodiť rukami;týčiť sa nad ostatnými|majster;hrnčiarsky kruh;vrkoč;tienidlo|Čo tvaruje starý majster?|Tvaruje vysokú vázu.
468|položiť fialovú podložku;priniesť zelenú podložku;sedieť na múriku|obloha;rastliny;žena;podložka|Čo robia muž a žena?|Cvičia jogu na svojich podložkách.
469|zapáliť zápalku;mať čiernu bradu;ležať na podlahe|zápalky;miska;pes;stôl|Čo robí žena?|Zapaľuje lampu zápalkou.
470|mať dlhý vrkoč;nosiť margarétku;vliezť do maku|obloha;štít;lúka;vrkoč|Kde leží ten pár?|Leží na rozkvitnutej lúke.
471|piecť mäso;niesť drevenú dosku;sedieť na tráve|stromy;mäso;pes;tráva|Čo nesie muž?|Nesie mäso na doske.
473|hrýzť do zlatej medaily;zdvihnúť ruky;tlieskať|medaila;strom;vlajky;hodinky|Čo robí bežkyňa?|Hryzie do zlatej medaily.
474|siahať po telefóne;meditovať bez trička;spočívať na drevenom stojane|spievajúca misa;terasa;palmy;drdol|Čo robí skupina?|Meditujú na drevenej terase.
475|počúvať mušľu;zapínať si kolieskové korčule;kĺzať sa po chodbe|kolieskové korčule;náramok;dlaždice;krabica|Čo si dievča zapína?|Zapína si kolieskové korčule.
476|nastavovať zaostrovaciu skrutku;nazerať do okuláru;zväčšovať list|mikroskop;ceruzka;šošovky|Čo robí študent?|Nazerá do mikroskopu.
477|vybrať tanier;stáť za mužom;ohrievať jedlo|mikrovlnka;tanier;vidlička;lampa|Čo vyberá muž?|Vyberá tanier z mikrovlnky.
478|otvoriť fľašu;mať bradu;piť z misky|mlieko;mačka;kvety;okno|Čo robí mačka?|Pije mlieko z misky.
479|poklepať si na spánok;zosunúť sa na šachovnicu;vznášať sa nad jej hlavou|myšlienková bublina;okuliare;šachové figúrky;kučeravé vlasy|Čo si dievča predstavuje?|Predstavuje si v mysli šachovnicu.
480|otvoriť fľašu;piť vodu;mať na sebe modré tričko|minerálna voda;fľaša;stôl;muž|Čo nalieva žena?|Nalieva minerálnu vodu do pohára.
481|pokrčiť kolená;mať na sebe sivé šortky;mať na sebe fialové tričko|zrkadlo;ventilátor;činky|Čo robí mladý muž?|Pozerá sa do zrkadla.
483|liezť na veľký strom;žrať banán;mávať klobúkom|opica;banány;schody;stôl|Čo žerie opica?|Opica žerie banán.
485|opierať sa o balvan;vyžmýkať vodu;sedieť v dutine|mach;vrkoče;päsť;konáre|Čo robí žena?|Opiera si líce o mach.
486|stúpať na horu;mať na sebe červenú bundu;mať na sebe žltú bundu|obloha;hora;oblaky;sneh|Kde stoja tí dvaja ľudia?|Stoja na hore.
487|žrať syr;vbehnúť do diery;vydávať žlté svetlo|myš;syr;diera|Čo robí myš?|Myš žerie syr.
488|mať ryšavé vlasy;tlieskať;mať na sebe čierny top|sval;brada;činky|Čo robí muž v čiernom?|Ukazuje svoje veľké svaly.
489|ukazovať na hubu;držať košík;byť červená a biela|klobúk;huba;košík;listy|Na čo ukazuje žena?|Ukazuje na hubu.
490|hrať na gitare;spievať pieseň;mať vnútri mince|hudobník;gitara;bábätko;mince|Čo robí hudobník?|Hrá na gitare.
491|ochutnať horčicu;držať mašľovačku;niesť plech|horčica;miska;muž;okno|Čo ochutnáva muž?|Ochutnáva horčicu z misky.
492|lakovať si nechty;smiať sa zo svojej kamarátky;držať malý štetček|lak na nechty;pohár;stôl;vták|Čo robí žena v žltom?|Lakuje si nechty.
495|žrať trávu;mať na sebe sivú bundu;mať na sebe zelenú bundu|jelene;rieka;kamene;tráva|Čo robia jelene?|Žerú trávu pri rieke.
496|nasadiť si náhrdelník;stáť za kamarátkou;mať na sebe bielu košeľu|náhrdelník;zrkadlo;kvety;košeľa|Čo má na sebe žena v bielom?|Má na sebe farebný náhrdelník.
498|napiť sa vody;ukazovať na pódium;niesť gitaru|svetlá;ľudia;muž;gitara|Kto je nervózny?|Nervózny je muž s gitarou.
499|schovávať sa za novinami;mať na sebe zelenú košeľu;zložiť noviny|noviny;káva;croissant;stôl|Za čím sa žena schováva?|Schováva sa za veľkými novinami.
500|driblovať okolo obrancu;blokovať útočníkovi cestu;šprintovať k bránke|reflektor;bránka;obranca;futbalová lopta|Čo robí útočník?|Dribluje okolo obrancu.
501|otvoriť modré dvere;usmievať sa na ženu;chodiť po štyroch nohách|mesiac;muž;mačka|Čo robí muž?|Kráča v noci po ulici.
502|držať kompas;mať na hlave modrú čiapku;ležať v jej dlani|obloha;muž;slnko;žena|Čo ukazuje kompas?|Kompas ukazuje cestu na sever.
503|písať do zošita;tlieskať;obracať stránky|zošit;pohár;perá;stôl|Čo robí žena vo fialovom?|Píše do nového zošita.
505|otvoriť orech;mať dlhé vlasy;byť plná orechov|muž;žena;orechy;stôl|Čo robí muž?|Otvára orech.
506|rozbiť vajce;schmatnúť svoj batoh;byť posypaný bobuľovým ovocím|dvere;servírovací tanier;mango;ovsené vločky|Čo pripravujú muž a žena?|Pripravujú servírovací tanier s čerstvými surovinami.
507|pozorovať hmyz zblízka;sedieť na trstine;čupieť pri potoku|lupa;vážka;potok;cop|Čo robí dievča?|Pozoruje vážku cez lupu.
508|skákať pri lodi;mať na sebe žltú bundu;mať na sebe červenú bundu|obloha;oceán;delfíny;loď|Čo robia delfíny?|Vyskakujú z oceánu.
509|nalievať olej;namáčať chlieb do oleja;jesť chlieb|chlieb;olej;paradajky;okno|Čo muž je?|Je chlieb s olejom.
511|krájať cibuľu;nasadiť si plavecké okuliare;tlieskať|cibuľa;plavecké okuliare;okno;žena|Čo krája muž?|Krája cibuľu.
512|pozerať sa do zrkadla;mať na sebe zelené tričko;zdvihnúť topánku|bunda;nohavice;topánky;klobúk|Čo robí žena?|Pozerá sa v zrkadle na svoj outfit.
513|kráčať po rohoži;stáť pod stolom;mať sivú strechu|obloha;dom;hrniec;tráva|Kde jedia ľudia?|Jedia vonku pred domom.
514|zakryť si vlasy;mať bradu;piecť sa v rúre|okno;rúra;chlieb;rukavica|Čo robia?|Vyberajú chlieb z rúry.
516|zatvoriť kohútik;stáť v mláke;pretekať mydlovou vodou|uterák;kohútik;práčka;mláka|Čo nie je v poriadku s drezom?|Drez preteká na podlahu.
519|baliť tašku;stáť vedľa kníh;zdvihnúť tašku|knihy;fľaša;taška;posteľ|Čo robí tá osoba?|Tá osoba balí knihy do tašky.
520|pádlovať na kanoe;driemať pod klobúkom;týčiť sa nad riekou|bambus;bralá;pádlo;klobúk proti slnku|Čo robí mladá žena?|Pádluje na kanoe popri bralách.
521|niesť kôš;stáť pod oknom;držať si nohu|okno;posteľ;kôš;oblečenie|Čo robí muž?|Od bolesti si drží nohu.
522|maľovať more;tlieskať;ležať na múriku|obloha;obraz;mačka;žena|Čo robí žena?|Maľuje more.
523|držať veľkú panvicu;pripravovať zeleninu;tlieskať|panvica;tanier;okno;muž|Čo robí muž?|Pripravuje zeleninu na panvici.
524|horúčkovito si prehmatávať vrecká;prehrabávať sa v taške;chytiť sa za hlavu|plátenná taška;peňaženka;kefa na vlasy;kľúče|Čo robí žena?|Prehrabáva sa vo svojej plátennej taške.
525|zopnúť stránky dokopy;mať obdĺžnikové okuliare;odfúknuť hárky|kancelárska spinka;sklenená miska;stolový ventilátor;závesná rastlina|Čo robí žena?|Zopína stránky kancelárskou spinkou.
527|otvoriť balík;mať na sebe oranžovú košeľu;pozerať sa cez bránku|balík;pes;dom;obloha|Čo robí žena?|Otvára balík.
530|roztiahnuť červené krídlo;otočiť hlavu;stáť na plote|papagáj;kvety;listy;plot|Čo robí papagáj?|Papagáj stojí na plote.
532|streliť gól;mať na sebe sivé tričko;kotúľať sa po zemi|žena;lopta;bránka;obloha|Čo robia hráči?|Prihrávajú si loptu.
533|pobozkať svoj pas;skontrolovať jej pas;ťahať kufor|pas;slnečné okuliare;bunda;prepážka|Čo bozkáva žena?|Bozkáva svoj pas.
535|variť cestoviny;jesť z taniera;ležať pri okne|cestoviny;tanier;mačka;žena|Čo žena je?|Je cestoviny z taniera.
536|uvelebiť sa v hojdacej sieti;vyliezť jej do lona;stáť na stolčeku|hojdacia sieť;ryšavá mačka;hrnček;palmový list|Čo robí žena?|Oddychuje v hojdacej sieti.
537|šúpať červené jablko;používať malý nôž;stáť na podlahe|jablko;košík;strom;oblaky|Čo robí dievča?|Šúpe červené jablko.
538|usmievať sa do kamery;zanechať modrú čiaru;ležať na stole|pero;čiapka;košeľa|Čo drží muž?|Drží zelené pero.
541|kresliť ceruzkou;tlieskať;sedieť v okne|ceruzka;mačka;ovocie;zošit|Čo robí žena?|Kreslí ceruzkou.
542|kráčať po snehu;kĺzať sa po bruchu;plávať pod ľadom|obloha;voda;tučniak;sneh|Čo robí tučniak?|Kĺže sa po snehu.
543|dať korenie na cestoviny;kýchnuť si do lakťa;ukázať svoje cestoviny|okno;muž;cestoviny|Čo robí muž?|Dáva si korenie na cestoviny.
545|žonglovať s farebnými kužeľmi;sedieť vedľa divákov;mať na sebe rifľovú bundu|diváci;žongléri;klobúk;dlažobné kocky|Čo robia žongléri?|Žonglujú s kužeľmi počas pouličného vystúpenia.
546|nastriekať si parfum;privoňať k parfumu;mať žltú šatku|strom;žena;parfum;stôl|Čo robí žena v modrom?|Strieka si parfum na ruku.
547|telefonovať;nosiť okuliare;mávať rukou|telefón;stôl;kvety|Čo robí žena bez okuliarov?|Telefonuje.
548|pozerať sa cez hľadáčik;pózovať pri stene;ukazovať na displej|fotoaparát;dlažobné kocky;obloha;muž|Čo robí muž?|Pózuje pri stene.
549|vložiť zlatý krúžok;povaľovať sa na posteli;ukazovať na ušný lalôčik|piercing;kučery;žiarovka;podnos na šperky|Čo robí žena?|Vkladá si krúžok do piercingu v uchu.
550|ležať v blate;stáť za prasaťom;piť z vedra|prasa;vedro;muž;plot|Z čoho pije prasa?|Prasa pije z vedra.
551|chodiť pomedzi stoličky;letieť ponad fontánu;pristáť na streche|obloha;holub;strecha;múr|Kde pristáva holub?|Pristáva na streche.
553|kosiť ihrisko;zapichnúť rohovú zástavku;trénovať v pozadí|plochá čiapka;hráči;ihrisko;rohová zástavka|Čo robí správca ihriska?|Správca ihriska kosí ihrisko.
554|niesť podložku;hľadať miesto;sedieť na podložke|slnečník;more;žena;podložka|Čo hľadá žena?|Hľadá miesto na sedenie.
555|ukazovať na list;čistiť veľký list;zdvihnúť predné labky|okno;žena;rastliny;mačka|Na čo ukazuje žena?|Ukazuje na rastlinu.
556|zdvihnúť prst;otvoriť malú krabičku;nalepiť náplasť|náplasť;mačka;okno;kniha|Čo robí muž?|Lepí jej náplasť na prst.
557|čistiť tanier;niesť veľký tanier;sedieť pri stole|tanier;cestoviny;panvica|Čo nesie muž?|Nesie veľký tanier cestovín.
559|bežať s loptou;padnúť na kolená;kotúľať sa po tráve|hráč;lopta;bránka;tráva|Čo robí hráč v žltom?|Beží s loptou.
560|robiť si selfie;otvoriť ústa dokorán;byť plná vody|fontána;socha;obloha|Čo robí žena?|Robí si selfie.
561|ponúknuť mu kúsok;prijať malý kúsok;zvierať papierové vrecko|dredy;čiapka;croissant;šál|Čo robí žena?|S veľkým pôžitkom je croissant.
562|zdvihnúť zástrčku;držať modrú šálku;osvetliť miestnosť|žena;zástrčka;šálka;ruka|Čo drží žena?|Drží bielu zástrčku.
563|hľadať vo vreckách;držať dva poháre s kávou;sedieť na múriku|vták;kľúče;pohár;vrecko|Čo robí ryšavý muž?|Hľadá vo svojich vreckách.
564|postrčiť najvyšší blok;vojensky zasalutovať;obsadiť najvyšší stupeň|strop;tepláková súprava;päsť;stupne víťazov|Kde stojí víťazka?|Stojí hore na stupňoch víťazov.
565|potriasť kuchárovi rukou;zdvihnúť obe päste;zotrieť zelenú farbu|kupola;plátno;maliarsky stojan;dlažobné kocky|Čo robia tí dvaja kandidáti?|Podávajú si ruky pred davom.
566|vyprázdniť hrdzavý sud;zdvihnúť kovové vedro;vznášať sa nad vodou|cop;pršiplášť;rieka;vedro|Čo robí muž?|Vyprázdňuje sud do rieky.
567|ukazovať na ryby;sedieť na liste;plávať pod vodou|kvety;slimák;jazierko;kamene|Na čo ukazuje žena?|Ukazuje na ryby v jazierku.
568|ležať na oranžovom kolese;bežať k bazénu;skočiť za kamarátom|kvety;stoličky;koleso;bazén|Čo robia tí dvaja muži?|Skáču do bazéna."""
src = json.load(open(f'{H}/source.json')); rows = {}
for line in D.strip().split('\n'):
    i, p, n, q, a = line.split('|')
    rows[i] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/sk.json', 'w'), ensure_ascii=False, indent=1)
print(len(out), [i for i in rows if i not in src])
