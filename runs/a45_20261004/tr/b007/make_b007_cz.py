import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """443|držet baterku;mít na sobě modrý svetr;vypadat jako kůň|světlo;žena;krabice;hračkový kůň|Co proniká oknem?|Oknem proniká světlo.
444|zakrývat si obličej;mít na sobě šedé tričko;ozářit oblohu|blesk;mraky;strom;brýle|Na co se dívají?|Dívají se na blesk.
445|chodit v zelených holínkách;mít na hlavě modrou kšiltovku;být dlouhá a bílá|čára;žena;tráva;kopec|Na čem žena stojí?|Stojí na bílé čáře.
446|otevřít tlamu dokořán;procházet trávou;mít plochou korunu|lev;strom;tráva|Co dělá lev?|Otevírá tlamu dokořán.
447|držet balzám na rty;vyzkoušet její balzám na rty;mít na sobě modrý kabátek|sníh;pes;šála;balzám na rty|Co dělá žena?|Nanáší si balzám na rty.
448|nanášet růžový lesk na rty;poklepat si na spodní ret;dívat se přes sluneční brýle|zábradlí;miska;lesk na rty|Co dělá žena ve fialovém?|Nanáší si lesk na rty.
450|sedět na slunci;zvednout hlavu;lézt nahoru po zdi|kaktus;stín;ještěrka;kámen|Co dělá ještěrka?|Leze nahoru po zdi.
451|zamknout dveře;odejít;zasunout se do zámku|vlasy;klíč;kabát;taška|Co dělá žena?|Zamyká dveře klíčem.
452|načrtnout logo;mít hustý plnovous;dřímat na stole|logo;brýle;notebook;stůl|Co kreslí žena?|Načrtává logo na papír.
453|jíst zelený hrášek;držet vidličku;sedět sám|chlapec;hrášek;telefon;okna|Co chlapec jí?|Jí sám zelený hrášek.
454|spát na jeho rameni;sedět pod dekou;objímat ženu|muž;polévka;deka;boty|Co dělá muž?|Objímá spící ženu.
455|zhluboka dýchat;nafouknout červený balonek;dosáhnout obří velikosti|balonek;tričko;legíny;trávník|Co dělá žena?|Nafukuje obrovský červený balonek.
456|otáčet stránky;spát na židli;mít na sobě modrý top|okno;rostlina;kočka;časopisy|Co dělají ty dvě ženy?|Prohlížejí si časopis.
458|běžet za ptáky;nést velkou bednu;mít tmavou kravatu|obloha;budova;muž;ptáci|Co dělá mladý muž?|Běží za ptáky.
459|psát na podložku s klipem;ukázat palec nahoru;mít oholenou hlavu|manažerka;podložka s klipem;bedýnky;květiny|Co dělá manažerka?|Píše na podložku s klipem.
462|mít na hlavě červenou čepici;běžet s mapou;letět vzduchem|čepice;brýle;košile;mapa|Na co se dívají?|Dívají se na mapu.
464|používat růžový fix;mít na sobě modré tričko;mít černý ocas|muž;žena;fix;stůl|Čím žena kreslí?|Kreslí růžovým fixem.
465|nést košík;prodávat rajčata;krájet sýr|žena;sýr;rajčata;košík|Co dělá žena v modrém?|Nese košík na trhu.
466|nanášet černou řasenku;stát v pozadí;vykukovat z košíku|řasenka;sklenice na víno;štětce na líčení|Co dělá zrzavá žena?|Nanáší si řasenku na řasy.
467|tvarovat vysokou vázu;rozhodit rukama;tyčit se nad ostatními|mistr;hrnčířský kruh;cop;stínidlo|Co tvaruje starý mistr?|Tvaruje vysokou vázu.
468|položit fialovou podložku;přinést zelenou podložku;sedět na zídce|obloha;rostliny;žena;podložka|Co dělají muž a žena?|Cvičí jógu na svých podložkách.
469|zapálit sirku;mít černý plnovous;ležet na podlaze|sirky;miska;pes;stůl|Co dělá žena?|Zapaluje lampu sirkou.
470|mít dlouhý cop;nosit kopretinu;vlézt do máku|obloha;štít;louka;cop|Kde ten pár leží?|Leží na rozkvetlé louce.
471|péct maso;nést dřevěné prkno;sedět na trávě|stromy;maso;pes;tráva|Co nese muž?|Nese maso na prkně.
473|kousat do zlaté medaile;zvednout ruce;tleskat|medaile;strom;vlajky;hodinky|Co dělá běžkyně?|Kouše do zlaté medaile.
474|sahat po telefonu;meditovat bez trička;spočívat na dřevěném stojanu|zpívající mísa;terasa;palmy;drdol|Co dělá skupina?|Meditují na dřevěné terase.
475|poslouchat mušli;zapínat si kolečkové brusle;klouzat chodbou|kolečkové brusle;náramek;dlaždice;krabice|Co si dívka zapíná?|Zapíná si kolečkové brusle.
476|nastavovat zaostřovací šroub;nahlížet do okuláru;zvětšovat list|mikroskop;tužka;čočky|Co dělá student?|Nahlíží do mikroskopu.
477|vyndat talíř;stát za mužem;ohřívat jídlo|mikrovlnka;talíř;vidlička;lampa|Co muž vyndává?|Vyndává talíř z mikrovlnky.
478|otevřít láhev;mít plnovous;pít z misky|mléko;kočka;květiny;okno|Co dělá kočka?|Pije mléko z misky.
479|poklepat si na spánek;sesunout se na šachovnici;vznášet se nad její hlavou|myšlenková bublina;brýle;šachové figurky;kudrnaté vlasy|Co si dívka představuje?|Představuje si v duchu šachovnici.
480|otevřít láhev;pít vodu;mít na sobě modré tričko|minerální voda;láhev;stůl;muž|Co žena nalévá?|Nalévá minerální vodu do sklenice.
481|pokrčit kolena;mít na sobě šedé šortky;mít na sobě fialové tričko|zrcadlo;ventilátor;činky|Co dělá mladý muž?|Dívá se do zrcadla.
483|lézt na velký strom;jíst banán;mávat kloboukem|opice;banány;schody;stůl|Co opice jí?|Opice jí banán.
485|opírat se o balvan;vymačkat vodu;sedět v dutině|mech;copy;pěst;větve|Co dělá žena?|Opírá si tvář o mech.
486|stoupat na horu;mít na sobě červenou bundu;mít na sobě žlutou bundu|obloha;hora;mraky;sníh|Kde ti dva lidé stojí?|Stojí na hoře.
487|jíst sýr;vběhnout do díry;vydávat žluté světlo|myš;sýr;díra|Co dělá myš?|Myš jí sýr.
488|mít zrzavé vlasy;tleskat;mít na sobě černý top|sval;plnovous;činky|Co dělá muž v černém?|Ukazuje své velké svaly.
489|ukazovat na houbu;držet košík;být červená a bílá|klobouk;houba;košík;listy|Na co žena ukazuje?|Ukazuje na houbu.
490|hrát na kytaru;zpívat písničku;mít uvnitř mince|hudebník;kytara;miminko;mince|Co dělá hudebník?|Hraje na kytaru.
491|ochutnat hořčici;držet mašlovačku;nést plech|hořčice;miska;muž;okno|Co muž ochutnává?|Ochutnává hořčici z misky.
492|lakovat si nehty;smát se své kamarádce;držet malý štěteček|lak na nehty;sklenice;stůl;pták|Co dělá žena ve žlutém?|Lakuje si nehty.
495|jíst trávu;mít na sobě šedou bundu;mít na sobě zelenou bundu|jeleni;řeka;kameny;tráva|Co dělají jeleni?|Jedí trávu u řeky.
496|nasadit si náhrdelník;stát za kamarádkou;mít na sobě bílou košili|náhrdelník;zrcadlo;květiny;košile|Co má na sobě žena v bílém?|Má na sobě barevný náhrdelník.
498|napít se vody;ukazovat na pódium;nést kytaru|světla;lidé;muž;kytara|Kdo je nervózní?|Nervózní je muž s kytarou.
499|schovávat se za novinami;mít na sobě zelenou košili;složit noviny|noviny;káva;croissant;stůl|Za čím se žena schovává?|Schovává se za velkými novinami.
500|driblovat kolem obránce;blokovat útočníkovi cestu;sprintovat k brance|reflektor;branka;obránce;fotbalový míč|Co dělá útočník?|Dribluje kolem obránce.
501|otevřít modré dveře;usmívat se na ženu;chodit po čtyřech nohách|měsíc;muž;kočka|Co dělá muž?|Jde v noci po ulici.
502|držet kompas;mít na hlavě modrou čepici;ležet v její dlani|obloha;muž;slunce;žena|Co ukazuje kompas?|Kompas ukazuje cestu na sever.
503|psát do sešitu;tleskat;otáčet stránky|sešit;sklenice;pera;stůl|Co dělá žena ve fialovém?|Píše do nového sešitu.
505|otevřít ořech;mít dlouhé vlasy;být plná ořechů|muž;žena;ořechy;stůl|Co dělá muž?|Otevírá ořech.
506|rozklepnout vejce;popadnout svůj batoh;být posypaný bobulovým ovocem|dveře;servírovací talíř;mango;ovesné vločky|Co připravují muž a žena?|Připravují servírovací talíř s čerstvými surovinami.
507|pozorovat hmyz zblízka;sedět na rákosu;dřepět u potoka|lupa;vážka;potok;culík|Co dělá dívka?|Pozoruje vážku lupou.
508|skákat u lodi;mít na sobě žlutou bundu;mít na sobě červenou bundu|obloha;oceán;delfíni;loď|Co dělají delfíni?|Vyskakují z oceánu.
509|nalévat olej;namáčet chléb do oleje;jíst chléb|chléb;olej;rajčata;okno|Co muž jí?|Jí chléb s olejem.
511|krájet cibuli;nasadit si plavecké brýle;tleskat|cibule;plavecké brýle;okno;žena|Co muž krájí?|Krájí cibuli.
512|dívat se do zrcadla;mít na sobě zelené tričko;zvednout botu|bunda;kalhoty;boty;klobouk|Co dělá žena?|Dívá se v zrcadle na svůj outfit.
513|jít po rohoži;stát pod stolem;mít šedou střechu|obloha;dům;hrnec;tráva|Kde lidé jedí?|Jedí venku před domem.
514|zakrýt si vlasy;mít plnovous;péct se v troubě|okno;trouba;chléb;rukavice|Co dělají?|Vyndávají chléb z trouby.
516|zavřít kohoutek;stát v louži;přetékat mýdlovou vodou|ručník;kohoutek;pračka;louže|Co není v pořádku s dřezem?|Dřez přetéká na podlahu.
519|balit tašku;stát vedle knih;zvednout tašku|knihy;láhev;taška;postel|Co ta osoba dělá?|Ta osoba balí knihy do tašky.
520|pádlovat na kánoi;dřímat pod kloboukem;tyčit se nad řekou|bambus;útesy;pádlo;klobouk proti slunci|Co dělá mladá žena?|Pádluje na kánoi kolem útesů.
521|nést koš;stát pod oknem;držet si nohu|okno;postel;koš;oblečení|Co dělá muž?|Bolestí si drží nohu.
522|malovat moře;tleskat;ležet na zídce|obloha;obraz;kočka;žena|Co dělá žena?|Maluje moře.
523|držet velkou pánev;připravovat zeleninu;tleskat|pánev;talíř;okno;muž|Co dělá muž?|Připravuje zeleninu na pánvi.
524|horečně si prohmatávat kapsy;prohrabávat se v tašce;chytit se za hlavu|plátěná taška;peněženka;kartáč na vlasy;klíče|Co dělá žena?|Prohrabává se ve své plátěné tašce.
525|sepnout stránky k sobě;mít obdélníkové brýle;odfouknout listy|kancelářská sponka;skleněná miska;stolní ventilátor;závěsná rostlina|Co dělá žena?|Spíná stránky kancelářskou sponkou.
527|otevřít balík;mít na sobě oranžovou košili;dívat se skrz branku|balík;pes;dům;obloha|Co dělá žena?|Otevírá balík.
530|roztáhnout červené křídlo;otočit hlavu;stát na plotě|papoušek;květiny;listy;plot|Co dělá papoušek?|Papoušek stojí na plotě.
532|dát gól;mít na sobě šedé tričko;kutálet se po zemi|žena;míč;branka;obloha|Co dělají hráči?|Přihrávají si míč.
533|políbit svůj pas;zkontrolovat její pas;táhnout kufr|pas;sluneční brýle;bunda;přepážka|Co žena líbá?|Líbá svůj pas.
535|vařit těstoviny;jíst z talíře;ležet u okna|těstoviny;talíř;kočka;žena|Co žena jí?|Jí těstoviny z talíře.
536|uvelebit se v houpací síti;vylézt jí na klín;stát na stoličce|houpací síť;zrzavá kočka;hrnek;palmový list|Co dělá žena?|Odpočívá v houpací síti.
537|loupat červené jablko;používat malý nůž;stát na podlaze|jablko;košík;strom;mraky|Co dělá dívka?|Loupe červené jablko.
538|usmívat se do kamery;zanechat modrou čáru;ležet na stole|pero;čepice;košile|Co muž drží?|Drží zelené pero.
541|kreslit tužkou;tleskat;sedět v okně|tužka;kočka;ovoce;sešit|Co dělá žena?|Kreslí tužkou.
542|chodit po sněhu;klouzat po břiše;plavat pod ledem|obloha;voda;tučňák;sníh|Co dělá tučňák?|Klouže po sněhu.
543|dát pepř na těstoviny;kýchnout si do lokte;ukázat své těstoviny|okno;muž;těstoviny|Co dělá muž?|Dává si pepř na těstoviny.
545|žonglovat s barevnými kužely;sedět vedle diváků;mít na sobě džínovou bundu|diváci;žongléři;klobouk;dlažební kostky|Co dělají žongléři?|Žonglují s kužely při pouličním vystoupení.
546|nastříkat si parfém;přivonět k parfému;mít žlutý šátek|strom;žena;parfém;stůl|Co dělá žena v modrém?|Stříká si parfém na ruku.
547|telefonovat;nosit brýle;mávat rukou|telefon;stůl;květiny|Co dělá žena bez brýlí?|Telefonuje.
548|dívat se hledáčkem;pózovat u zdi;ukazovat na displej|fotoaparát;dlažební kostky;obloha;muž|Co dělá muž?|Pózuje u zdi.
549|vložit zlatý kroužek;povalovat se na posteli;ukazovat na ušní lalůček|piercing;kudrny;žárovka;podnos na šperky|Co dělá žena?|Vkládá si kroužek do piercingu v uchu.
550|ležet v blátě;stát za prasetem;pít z kbelíku|prase;kbelík;muž;plot|Z čeho prase pije?|Prase pije z kbelíku.
551|chodit mezi židlemi;letět nad fontánou;přistát na střeše|obloha;holub;střecha;zeď|Kde holub přistává?|Přistává na střeše.
553|sekat hřiště;zapíchnout rohový praporek;trénovat v pozadí|placatá čepice;hráči;hřiště;rohový praporek|Co dělá správce hřiště?|Správce hřiště seká hřiště.
554|nést podložku;hledat místo;sedět na podložce|slunečník;moře;žena;podložka|Co žena hledá?|Hledá místo k sezení.
555|ukazovat na list;čistit velký list;zvednout přední tlapky|okno;žena;rostliny;kočka|Na co žena ukazuje?|Ukazuje na rostlinu.
556|zvednout prst;otevřít malou krabičku;nalepit náplast|náplast;kočka;okno;kniha|Co dělá muž?|Lepí jí náplast na prst.
557|čistit talíř;nést velký talíř;sedět u stolu|talíř;těstoviny;pánev|Co muž nese?|Nese velký talíř těstovin.
559|běžet s míčem;padnout na kolena;kutálet se po trávě|hráč;míč;branka;tráva|Co dělá hráč ve žlutém?|Běží s míčem.
560|dělat si selfie;otevřít ústa dokořán;být plná vody|fontána;socha;obloha|Co dělá žena?|Dělá si selfie.
561|nabídnout mu kousek;přijmout malý kousek;svírat papírový sáček|dredy;čepice;croissant;šála|Co dělá žena?|S velkým požitkem jí croissant.
562|zvednout zástrčku;držet modrý hrnek;osvětlit místnost|žena;zástrčka;hrnek;ruka|Co žena drží?|Drží bílou zástrčku.
563|hledat v kapsách;držet dva kelímky s kávou;sedět na zídce|pták;klíče;kelímek;kapsa|Co dělá zrzavý muž?|Hledá ve svých kapsách.
564|postrčit nejvyšší blok;vojensky zasalutovat;obsadit nejvyšší stupeň|strop;tepláková souprava;pěst;stupně vítězů|Kde stojí vítězka?|Stojí nahoře na stupních vítězů.
565|potřást kuchaři rukou;zvednout obě pěsti;setřít zelenou barvu|kupole;plátno;malířský stojan;dlažební kostky|Co dělají ti dva kandidáti?|Podávají si ruce před davem.
566|vyprázdnit rezavý sud;zvednout kovový kbelík;vznášet se nad vodou|culík;pláštěnka;řeka;kbelík|Co dělá muž?|Vyprazdňuje sud do řeky.
567|ukazovat na ryby;sedět na listu;plavat pod vodou|květiny;šnek;jezírko;kameny|Na co žena ukazuje?|Ukazuje na ryby v jezírku.
568|ležet na oranžovém kruhu;běžet k bazénu;skočit za kamarádem|květiny;židle;kruh;bazén|Co dělají ti dva muži?|Skáčou do bazénu."""
src = json.load(open(f'{H}/source.json')); rows = {}
for line in D.strip().split('\n'):
    i, p, n, q, a = line.split('|')
    rows[i] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/cz.json', 'w'), ensure_ascii=False, indent=1)
print(len(out), [i for i in rows if i not in src])
