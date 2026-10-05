import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """569|odemknout vchodové dveře;mít hustý knír;mít culík|vedoucí pošty;klíče;balíky;vozík|Co dělá vedoucí pošty?|Tlačí vozík plný balíků.
572|kopat na zahradě;mít na sobě modrou šálu;sedět na plotě|pták;žena;brambory;kbelík|Co dělá žena?|Dává brambory do kbelíku.
573|nalévat pomerančový džus;držet velkou láhev;vzít sklenici|muž;žena;láhev;sklenice|Co dělá muž?|Nalévá pomerančový džus do sklenic.
574|otevřít ústa dokořán;dotýkat se své hrudi;mít krátké černé vlasy|strom;štětec;kelímek;pudr|Co je v kelímku?|V kelímku je pudr.
575|rozhodit rukama;přehrabovat se ve své tašce;zvednout powerbanku|powerbanka;holubi;růže;lavička|Do čeho zapojují telefon?|Zapojují ho do powerbanky.
576|modlit se u svého stolu;přitisknout dlaně k sobě;podívat se nahoru a plakat|žena;laptop;knihy;lampa|Co dělá žena?|Modlí se u svého stolu.
577|předpovědět déšť;vyprsknout smíchy;přinést náhlou přeháňku|bouřkový mrak;deštník;šál;tráva|Co dělá žena?|Schovává se pod žlutým deštníkem.
578|vytlačit motorku ven;leštit palivovou nádrž;poplácat ji po rameni|šátek;palivová nádrž;motor;dlažební kostky|Co dělá mechanička?|S hrdostí předvádí svou motorku.
579|psát nový kód;gestikulovat směrem k laptopu;sledovat nakreslenou dráhu|robot;laptop;culík;vousy|Co dělá žena?|Programuje malého robota.
580|držet zvednutý kabát;nést košík;nosit brýle|košík;kabát;obloha;brýle|Co dělá vysoká žena?|Chrání svou kamarádku před deštěm.
581|svírat slunečnici;nést transparent se stromem;třepotat se ve vánku|slunečnice;palma;obloha;dav|Co dělají lidé?|Protestují s malovanými transparenty.
582|sedět na židli;zkřížit si ruce;dotýkat se jejího ramene|židle;žena;okno;stůl|Jak se žena cítí?|Je hrdá na svou novou židli.
584|udělat stojku;dokázat mu, že se mýlí;zalapat po dechu úžasem|bosé nohy;legíny;lavička;pletená vesta|Co dělá mladá žena?|Dělá stojku, aby mu dokázala, že se mýlí.
585|hrát hudbu na veřejnosti;sedět na bedně;stříkat vodu vzhůru|pouliční lampa;muži;akordeon;kufr|Co dělá mladá žena?|Hraje na veřejnosti na akordeon.
588|mít na sobě červené holínky;mít na sobě černé holínky;stát daleko|žlutá pláštěnka;pták;červené holínky;louže|Co dělají ti dva lidé?|Skáčou do velké louže.
589|držet něco červeného;mít krátké vousy;běžet přes trávu|pes;tráva;muž;lano|Co dělají muž a žena?|Táhnou tlusté lano.
590|rozdávat rychlé údery;držet zvednuté lapy;viset na řetězu|cihlová zeď;boxovací pytel;boxerské rukavice;kraťasy|Co dělá žena?|Buší do lap.
591|rozdávat silné údery;přidržovat žebřík;houpat se pod stropem|řetěz;boxovací pytel;boxerské rukavice;kraťasy|Co dělá muž?|Buší do boxovacího pytle.
592|mít tmavé vousy;mít na sobě bílé tričko;jet dolů po silnici|obloha;dodávka;silnice|Co dělají ti dva muži?|Tlačí bílou dodávku.
593|mít krátké kudrnaté vlasy;mít dlouhé tmavé vlasy;spát na podlaze|okno;pyžamo;postel;pes|Co mají muž a žena na sobě?|Mají na sobě pyžamo.
594|překonat laťku;mávat zeleným praporkem;mávat zaťatými pěstmi|laťka;praporek;culík;žíněnka|Jak se dívka kvalifikuje?|Kvalifikuje se tím, že překoná laťku.
595|žrát zelené listy;mýt si obličej;skákat přes trávu|obloha;králík;tráva;listy|Co žere králík?|Žere zelené listy.
597|dívat se skrz raketu;stát za sítí;usmívat se do kamery|květiny;míček;síť;raketa|Co drží žena?|Drží černou raketu.
598|rozpřáhnout ruce doširoka;mít na sobě bílou košili;chodit po čtyřech nohách|střecha;strom;pes;lodička|Co dělá dívka?|Tančí v dešti.
599|driblovat s barevným míčem;atakovat muže v černém;ovládat bílý míč|branka;fotbalový míč;trávník;střecha|Co dělají ti dva muži?|Soupeří o míč.
600|stát na dvou nohách;táhnout kousek pizzy;mít velká černá kola|potkan;pizza;schody;okno|Co dělá potkan?|Táhne kousek pizzy.
601|holit se holicím strojkem;ukazovat na své hodinky;chodit po umyvadle|holicí strojek;lampa;zrcadlo;tričko|Co dělá muž v bílém?|Holí se holicím strojkem.
604|držet červené jablko;prodávat ovoce;tisknout dlouhou účtenku|účtenka;jablka;hrušky;láhve|Na co se dívá muž?|Dívá se na dlouhou účtenku.
606|sedět v kleci;mít černé vousy;mít kudrnaté vlasy|recept;pták;lívance;muž|Co jedí muž a žena?|Jedí lívance.
607|ležet na podlaze;dotýkat se ledničky;mít černé vousy|lednička;pes;muž;žena|Kde stojí muž a žena?|Stojí vedle ledničky.
608|svírat volant;smát se úlevou;ležet na čelním skle|volant;palubní deska;stěrač;mikina|Co svírá řidička?|Svírá volant.
609|nést červený batoh;zout si boty;mít na sobě modrou šálu|obloha;jezero;skála;batoh|Co dělají muž a žena?|Odpočívají na trávě.
610|nést tři stuhy;objímat velkou dýni;být velká a oranžová|stuha;dýně;klobouk;vlajky|Co je na velké dýni?|Na dýni je modrá stuha.
613|vlézt do ringu;mít na rukou modré rukavice;držet láhev s vodou|ring;muž;zeď|Co dělá muž?|Boxuje v ringu.
615|letět nad vodou;pohybovat se dolů po řece;růst u řeky|řeka;pták;listy;kameny|Co se pohybuje dolů po řece?|Dolů po řece se pohybují dva listy.
616|mít zrzavé vlasy;mít na sobě šedý svetr;být velká a kulatá|skála;obloha;řeka|Na čem stojí?|Stojí na velké skále.
618|uvázat lano;stát za vozem;mít velké kolo|strom;lano;kolo;bláto|Co dělá velký muž?|Táhne vůz lanem.
619|táhnout košík nahoru;čekat v uličce;procházet se po zdi|bylinky;pomeranče;košík;lano|Co dělá žena?|Táhne košík pomerančů.
621|stát vedle řady;mít na hlavě růžový klobouk;mít červený vršek|obloha;klobouk;rostliny;zem|Co dělají lidé?|Sázejí malé rostliny do řady.
622|natahovat gumičku;dotýkat se své tváře;jít po ulici|gumička;žena;muž;krabice|Co dělá žena?|Natahuje gumičku.
623|dívat se do telefonu;přinést mu kávu;dát si nohy nahoru|telefon;sluneční brýle;bota;vidlička|Co dělá mladý muž?|Dívá se do telefonu.
626|pít z kelímku;sledovat závod;dívat se na hodinky|kelímek;hodinky;obloha;běžkyně|Co dělá běžkyně?|Pije z kelímku.
627|vykračovat si po koberci;natáčet svou kamarádku;sedět úplně nehybně|koberec;světelný řetěz;krb;stojací lampa|Co dělá žena v modrém?|Vykračuje si po koberci.
628|balit knihy;držet knihu;plakat na podlaze|police;brýle;knihy;krabice|Co dělá žena?|Pláče na podlaze.
629|zavřít dveře;pověsit bundu;mít na sobě žlutou bundu|žena;muž;hrnky;dřevo|Co zavírá žena?|Zavírá velké dřevěné dveře.
630|táhnout dlouhé lano;držet velké kormidlo;zvednout obě ruce|námořnice;kormidlo;lano;plachta|Co dělá námořnice?|Táhne dlouhé lano.
631|krájet okurku;míchat salát;jíst malé rajče|žena;muž;salát;stůl|Co připravuje muž?|Připravuje salát.
632|sypat sůl na rajčata;mít krátké tmavé vlasy;stát venku za oknem|pták;sůl;rajčata;chléb|Co dělá žena?|Sype sůl na rajčata.
634|sypat suchý písek;kreslit klackem;zakrýt kresbu|žena;muž;vlna;písek|Co dělá muž?|Sype si písek do ruky.
635|obout si sandály;mít na sobě zelené kraťasy;stát na lavičce|obloha;pták;lavička;sandály|Co mají na nohou?|Na nohou mají sandály.
636|připravovat sendvič;krájet sendvič;stát za košíkem|stromy;kachna;košík;sendvič|Co připravuje žena?|Připravuje sendvič.
638|lít zelenou omáčku;jíst bramboru;sedět na trávě|muž;žena;pes;omáčka|Co dělá muž?|Lije zelenou omáčku.
639|obracet klobásky;jíst hot dog;ležet na pánvi|klobouk;stan;pták;klobásky|Co jí žena?|Jí hot dog.
640|zvednout dvě činky;ukazovat své velké paže;ukazovat na váhu|muž;žena;podlaha;váha|Na čem stojí muž?|Stojí na váze.
641|sypat trochu mouky;mít dlouhý cop;sedět na váze|měděné pánve;mourovatá kočka;mísa na míchání;kuchyňská váha|Kde sedí kočka?|Sedí na kuchyňské váze.
642|ukazovat na své předloktí;mít husté vousy;ukazovat svou zjizvenou holeň|trenčkot;žárovka;jizva;hrnky|Co ukazuje blonďatý muž?|Ukazuje jizvu na holeni.
644|zakrýt si ústa;nést bílou tašku;držet zvednutý telefon|brýle;vlasy;taška;podlaha|Co dělá vyděšená žena?|Zakrývá si ústa.
645|kreslit kruh;držet černé pero;mít na ruce hodinky|rozvrh;muž;zápisník;šanony|Co kreslí muž?|Kreslí do rozvrhu kruh.
647|stříhat vlasy nůžkami;dívat se do zrcadla;sedět na židli|nůžky;hřeben;ručník;brýle|Co dělá žena s brýlemi?|Stříhá vlasy nůžkami.
649|hubovat mladého muže;svírat slaměný klobouk;založit si ruce|šátek;zástěra;branka;hlávky zelí|Co dělá stará žena?|Hubuje mladého muže.
650|lézt po podlaze;mít dlouhý cop;nakukovat přes krabici|šroub;kartonová krabice;zlatý retrívr;palec|Co hledá muž?|Hledá chybějící šroub.
651|utahovat šroub;přidržovat dřevěnou polici;sedět na pohovce|šroubovák;knihy;kočka;pokojová rostlina|Co dělá žena?|Utahuje šroub šroubovákem.
652|narážet do skal;mít na sobě bílou košili;mít krátké vlasy|moře;žena;muž;skály|Co dělají?|Skáčou do moře.
653|zvednout polštář;ukazovat na klíče;ležet u dveří|klíče;dveře;kočka;muž|Na co ukazuje muž?|Ukazuje na klíče ve dveřích.
654|šeptat tajemství;poslouchat svou kamarádku;dívat se přes zeď|obloha;lampa;hora;brýle|Co dělá žena ve žlutém?|Šeptá své kamarádce tajemství.
655|malovat černou čáru;vběhnout do místnosti;troubit na malou trumpetku|klobouk;brýle;papír;stůl|Co dělá žena v modrém?|Maluje na papír černou čáru.
656|zmáčknout šachové hodiny;mít na sobě khaki bundu;zvednout obě zaťaté pěsti|oblouková okna;lano;šachové hodiny;šachovnice|Co dělá šachistka?|Po svém tahu mačká šachové hodiny.
657|podávat jídlo;nalévat trochu vody;dívat se na své jídlo|žena;sklenice;vidlička;stůl|Co dělá žena?|Podává muži jídlo.
660|mydlit vlasy své kamarádce;naklánět se nad lavor;zachytávat mýdlovou vodu|banánové listy;kohoutek;lavor;stolička|Co dělá žena v zeleném?|Mydlí vlasy své kamarádce.
661|otevírat svou velkou tlamu;připlout velmi blízko;plavat ve skupině|ryby;žralok;voda|Co dělá žralok?|Žralok otevírá svou velkou tlamu.
662|kreslit hvězdu;mít krátké vlasy;žrát trávu|kůň;ořezávátko;zápisník;miska|Co kreslí žena?|Kreslí hvězdu.
663|nanášet si pěnu na holení;dívat se do zrcadla;sledovat svého kamaráda|lampy;zrcadlo;pěna na holení;kohoutek|Co dělá muž v modrém?|Nanáší si na obličej pěnu na holení.
664|holit muži obličej;ležet v křesle;sedět u okna|láhve;kočka;muž;miska|Co dělá žena?|Holí muži obličej.
666|oblékat si košili;sledovat muže;zapínat si košili|pták;žena;košile|Co dělá muž?|Obléká si modrou košili.
667|držet se za hlavu;ležet na chodníku;zalapat po dechu šokem|chodec;helma;skútr;chodník|Co dělá žena?|V šoku se drží za hlavu.
668|zavazovat si boty;držet kelímky s kávou;jít vodou|dveře;kalhoty;boty;zem|Co dělá žena?|Zavazuje si hnědé boty.
669|nést košík;podat jí chléb;platit mincemi|lampa;brýle;chléb;klobouk|Co dělá žena?|Kupuje v obchodě chléb.
671|mít krátké vousy;nést modrý batoh;mít dlouhý krk|obloha;lama;muž;žena|Co dělají ti dva lidé?|Křičí poblíž lamy.
672|držet ručník;mít na sobě modré tričko;stát na sprše|pták;sprcha;ručník;muž|Co dělá žena?|Sprchuje se na pláži.
674|smrkat;přinést jí šálek;růst u okna|rostlina;šálek;deka;stůl|Co dělá žena?|Nemocná žena smrká.
675|sklánět se nad kbelíkem;nosit brýle;zbarvit se do zářivě modré|loď;síť;muž;kbelíky|Co dělá blonďatý muž?|Natírá bok lodi.
678|držet zvednuté hedvábí;mít vlasy po ramena;krčit se na pultu|ventilátor;hedvábí;kočka;pult|Co dělá žena v béžovém?|Tiskne si hedvábí k tváři.
679|čistit stříbro;nasadit si náušnice;viset nad její hlavou|lampa;stříbro;žena|Co dělá žena?|Čistí stříbro hadříkem.
681|dívat se do kamery;řídit auto;být dlouhá a rovná|zrcátko;silnice;muž;žena|Co dělají?|Zpívají v autě.
683|pustit vodu;držet žlutou houbičku;ukazovat čistý talíř|muž;žena;dřez;talíře|Co myjí ve dřezu?|Myjí ve dřezu talíře.
684|sedět u stolu;otevřít dveře;obejmout obě dívky|dveře;dívka;lžíce;vidlička|Co dělají ty dvě sestry?|Ty dvě sestry se objímají.
685|zkoušet si klobouky;držet malé zrcátko;prodávat klobouky|obloha;klobouk;vlasy;šaty|Co dělá dívka?|Zkouší si klobouky.
687|jezdit na skateboardu;vyskočit do vzduchu;svítit nad městem|slunce;domy;chlapec;skateboard|Co dělá chlapec?|Jede na skateboardu.
688|nanášet si krém na obličej;třít si paži;dotýkat se svých tváří|pokožka;obloha;rostliny;tričko|Co dělá žena?|Nanáší si krém na pokožku.
689|držet si sukni;otočit se dokola;mít na sobě bílé boty|sukně;tričko;ptáci;stromy|Co má žena na sobě?|Má na sobě žlutou sukni.
691|hlídat šedé auto;ohánět se dřevěnou holí;být zaparkované venku|voják;ostnatý drát;betonová zeď;polní cesta|Co dělá voják?|S holí hlídá auto.
692|zvednout ruce;spát pod dekou;číst knihu|kočka;lampa;deka;polštář|Co dělá muž?|Spí pod dekou.
693|mnout si oči;spát u okna;ležet na jejím klíně|okno;sedadlo;svetr;zápisník|Jak se žena cítí?|Cítí se velmi ospalá.
695|opírat se o svou ruku;mít na sobě zelenou šálu;létat nad lodí|slunce;ptáci;loď;moře|Co dělají lidé?|Usmívají se na lodi.
696|smát se muži;odhánět kouř;stoupat k obloze|kouř;žena;muž;listy|Co dělá muž?|Odhání kouř.
697|mít na sobě červenou bundu;mít černé vousy;zapálit cigaretu|lampa;cigareta;bunda|Co dělá muž v červeném?|Kouří cigaretu.
698|nalévat smoothie;přidat více ovoce;mixovat ovoce|smoothie;banány;jahody;žena|Co dělá žena v oranžovém?|Nalévá smoothie do sklenice.
699|pašovat sýr;zvednout závoru;být naložený senem|strážný;seno;závora;vůz|Co pašuje farmář?|Pašuje sýr pod senem.
700|pohybovat se velmi pomalu;lézt na list;ležet na cestičce|hlemýžď;list;tráva|Co dělá hlemýžď?|Leze na list.
701|pohybovat se po písku;vypláznout jazyk;ležet pod hadem|had;skála;písek;obloha|Kde leží had?|Leží na černé skále."""
out = {}
for line in D.split("\n"):
    i, p, n, q, a = line.split("|")
    out[i] = {"phrases": p.split(";"), "nouns": n.split(";"), "question": q, "answer": a}
json.dump(out, open(os.path.join(H, "cz.json"), "w"), ensure_ascii=False, indent=1)
print(len(out))
