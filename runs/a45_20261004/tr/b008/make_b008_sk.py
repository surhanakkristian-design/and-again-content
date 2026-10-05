import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """569|odomknúť vchodové dvere;mať husté fúzy;mať vlasy v cope|vedúca pošty;kľúče;balíky;vozík|Čo robí vedúca pošty?|Tlačí vozík plný balíkov.
572|kopať v záhrade;mať na sebe modrý šál;sedieť na plote|vták;žena;zemiaky;vedro|Čo robí žena?|Dáva zemiaky do vedra.
573|nalievať pomarančový džús;držať veľkú fľašu;vziať pohár|muž;žena;fľaša;poháre|Čo robí muž?|Nalieva pomarančový džús do pohárov.
574|otvoriť ústa dokorán;dotýkať sa svojej hrude;mať krátke čierne vlasy|strom;štetec;téglik;púder|Čo je v tégliku?|V tégliku je púder.
575|vyhodiť ruky do vzduchu;prehrabávať sa vo svojej taške;zdvihnúť powerbanku|powerbanka;holuby;ruže;lavička|Do čoho zapájajú telefón?|Zapájajú ho do powerbanky.
576|modliť sa pri svojom stole;pritlačiť dlane k sebe;pozrieť sa hore a plakať|žena;laptop;knihy;lampa|Čo robí žena?|Modlí sa pri svojom stole.
577|predpovedať dážď;vybuchnúť do smiechu;priniesť náhlu prehánku|búrkový mrak;dáždnik;pléd;tráva|Čo robí žena?|Schováva sa pod žltým dáždnikom.
578|vytlačiť motorku von;leštiť palivovú nádrž;potľapkať ju po pleci|šatka;palivová nádrž;motor;dlažobné kocky|Čo robí mechanička?|S hrdosťou predvádza svoju motorku.
579|písať nový kód;gestikulovať smerom k laptopu;sledovať nakreslenú dráhu|robot;laptop;cop;brada|Čo robí žena?|Programuje malého robota.
580|držať zdvihnutý kabát;niesť košík;nosiť okuliare|košík;kabát;obloha;okuliare|Čo robí vysoká žena?|Chráni svoju kamarátku pred dažďom.
581|zvierať slnečnicu;niesť transparent so stromom;trepotať sa vo vánku|slnečnica;palma;obloha;dav|Čo robia ľudia?|Protestujú s maľovanými transparentmi.
582|sedieť na stoličke;prekrížiť si ruky;dotýkať sa jej pleca|stolička;žena;okno;stôl|Ako sa žena cíti?|Je hrdá na svoju novú stoličku.
584|urobiť stojku;dokázať mu, že sa mýli;zalapať po dychu od úžasu|bosé nohy;legíny;lavička;pletená vesta|Čo robí mladá žena?|Robí stojku, aby mu dokázala, že sa mýli.
585|hrať hudbu na verejnosti;sedieť na debne;striekať vodu nahor|pouličná lampa;muži;akordeón;kufor|Čo robí mladá žena?|Hrá na verejnosti na akordeóne.
588|mať na sebe červené čižmy;mať na sebe čierne čižmy;stáť ďaleko|žltý pršiplášť;vták;červené čižmy;mláka|Čo robia tí dvaja ľudia?|Skáču do veľkej mláky.
589|držať niečo červené;mať krátku bradu;bežať cez trávu|pes;tráva;muž;lano|Čo robia muž a žena?|Ťahajú hrubé lano.
590|rozdávať rýchle údery;držať zdvihnuté lapy;visieť na reťazi|tehlová stena;boxovacie vrece;boxerské rukavice;šortky|Čo robí žena?|Udiera do lapov.
591|rozdávať silné údery;pridržiavať rebrík;hojdať sa pod stropom|reťaz;boxovacie vrece;boxerské rukavice;šortky|Čo robí muž?|Udiera do boxovacieho vreca.
592|mať tmavú bradu;mať na sebe biele tričko;kotúľať sa dolu cestou|obloha;dodávka;cesta|Čo robia tí dvaja muži?|Tlačia bielu dodávku.
593|mať krátke kučeravé vlasy;mať dlhé tmavé vlasy;spať na podlahe|okno;pyžamo;posteľ;pes|Čo majú muž a žena na sebe?|Majú na sebe pyžamo.
594|prekonať latku;mávať zelenou zástavkou;mávať zaťatými päsťami|latka;zástavka;cop;žinenka|Ako sa dievča kvalifikuje?|Kvalifikuje sa tým, že prekoná latku.
595|žrať zelené listy;umývať si tvár;skákať cez trávu|obloha;králik;tráva;listy|Čo žerie králik?|Žerie zelené listy.
597|pozerať sa cez raketu;stáť za sieťou;usmievať sa do kamery|kvety;loptička;sieť;raketa|Čo drží žena?|Drží čiernu raketu.
598|roztiahnuť ruky doširoka;mať na sebe bielu košeľu;chodiť po štyroch nohách|strecha;strom;pes;loďka|Čo robí dievča?|Tancuje v daždi.
599|driblovať s farebnou loptou;atakovať muža v čiernom;ovládať bielu loptu|bránka;futbalová lopta;trávnik;strecha|Čo robia tí dvaja muži?|Súperia o loptu.
600|stáť na dvoch nohách;ťahať kúsok pizze;mať veľké čierne kolesá|potkan;pizza;schody;okno|Čo robí potkan?|Ťahá kúsok pizze.
601|holiť sa holiacim strojčekom;ukazovať na svoje hodinky;chodiť po umývadle|holiaci strojček;lampa;zrkadlo;tričko|Čo robí muž v bielom?|Holí sa holiacim strojčekom.
604|držať červené jablko;predávať ovocie;tlačiť dlhý bloček|bloček;jablká;hrušky;fľaše|Na čo sa pozerá muž?|Pozerá sa na dlhý bloček.
606|sedieť v klietke;mať čiernu bradu;mať kučeravé vlasy|recept;vták;lievance;muž|Čo jedia muž a žena?|Jedia lievance.
607|ležať na podlahe;dotýkať sa chladničky;mať čiernu bradu|chladnička;pes;muž;žena|Kde stoja muž a žena?|Stoja vedľa chladničky.
608|zvierať volant;smiať sa od úľavy;ležať na čelnom skle|volant;palubná doska;stierač;mikina|Čo zviera vodička?|Zviera volant.
609|niesť červený batoh;vyzuť si topánky;mať na sebe modrý šál|obloha;jazero;skala;batoh|Čo robia muž a žena?|Oddychujú na tráve.
610|niesť tri stuhy;objímať veľkú tekvicu;byť veľká a oranžová|stuha;tekvica;klobúk;vlajky|Čo je na veľkej tekvici?|Na tekvici je modrá stuha.
613|vyliezť do ringu;mať na rukách modré rukavice;držať fľašu s vodou|ring;muž;stena|Čo robí muž?|Boxuje v ringu.
615|letieť nad vodou;pohybovať sa dolu riekou;rásť pri rieke|rieka;vták;listy;kamene|Čo sa pohybuje dolu riekou?|Dolu riekou sa pohybujú dva listy.
616|mať ryšavé vlasy;mať na sebe sivý sveter;byť veľká a okrúhla|skala;obloha;rieka|Na čom stoja?|Stoja na veľkej skale.
618|uviazať lano;stáť za vozom;mať veľké koleso|strom;lano;koleso;blato|Čo robí veľký muž?|Ťahá voz lanom.
619|ťahať košík nahor;čakať v uličke;prechádzať sa po múre|bylinky;pomaranče;košík;lano|Čo robí žena?|Ťahá košík pomarančov.
621|stáť vedľa radu;mať na hlave ružový klobúk;mať červený vršok|obloha;klobúk;rastliny;zem|Čo robia ľudia?|Sadia do radu malé rastliny.
622|naťahovať gumičku;dotýkať sa svojej tváre;ísť po ulici|gumička;žena;muž;škatuľa|Čo robí žena?|Naťahuje gumičku.
623|pozerať sa do telefónu;priniesť mu kávu;vyložiť si nohy|telefón;slnečné okuliare;topánka;vidlička|Čo robí mladý muž?|Pozerá sa do telefónu.
626|piť z pohára;sledovať preteky;pozerať sa na hodinky|pohár;hodinky;obloha;bežkyňa|Čo robí bežkyňa?|Pije z pohára.
627|vykračovať si po koberci;natáčať svoju kamarátku;sedieť úplne nehybne|koberec;svetelná reťaz;kozub;stojacia lampa|Čo robí žena v modrom?|Vykračuje si po koberci.
628|baliť knihy;držať knihu;plakať na podlahe|police;okuliare;knihy;škatule|Čo robí žena?|Plače na podlahe.
629|zavrieť dvere;zavesiť bundu;mať na sebe žltú bundu|žena;muž;šálky;drevo|Čo zatvára žena?|Zatvára veľké drevené dvere.
630|ťahať dlhé lano;držať veľké kormidlo;zdvihnúť obe ruky|námorníčka;kormidlo;lano;plachta|Čo robí námorníčka?|Ťahá dlhé lano.
631|krájať uhorku;miešať šalát;jesť malú paradajku|žena;muž;šalát;stôl|Čo pripravuje muž?|Pripravuje šalát.
632|sypať soľ na paradajky;mať krátke tmavé vlasy;stáť vonku za oknom|vták;soľ;paradajky;chlieb|Čo robí žena?|Sype soľ na paradajky.
634|sypať suchý piesok;kresliť palicou;zakryť kresbu|žena;muž;vlna;piesok|Čo robí muž?|Sype si piesok do ruky.
635|obuť si sandále;mať na sebe zelené šortky;stáť na lavičke|obloha;vták;lavička;sandále|Čo majú na nohách?|Na nohách majú sandále.
636|pripravovať sendvič;krájať sendvič;stáť za košíkom|stromy;kačka;košík;sendvič|Čo pripravuje žena?|Pripravuje sendvič.
638|liať zelenú omáčku;jesť zemiak;sedieť na tráve|muž;žena;pes;omáčka|Čo robí muž?|Leje zelenú omáčku.
639|obracať klobásky;jesť hot dog;ležať na panvici|klobúk;stan;vták;klobásky|Čo práve je žena?|Práve je hot dog.
640|zdvihnúť dve činky;ukazovať svoje veľké paže;ukazovať na váhu|muž;žena;podlaha;váha|Na čom stojí muž?|Stojí na váhe.
641|sypať trochu múky;mať dlhý vrkoč;sedieť na váhe|medené panvice;tigrovaná mačka;misa na miešanie;kuchynská váha|Kde sedí mačka?|Sedí na kuchynskej váhe.
642|ukazovať na svoje predlaktie;mať hustú bradu;ukazovať svoju zjazvenú holeň|trenčkot;žiarovka;jazva;hrnčeky|Čo ukazuje blonďavý muž?|Ukazuje jazvu na holeni.
644|zakryť si ústa;niesť bielu tašku;držať zdvihnutý telefón|okuliare;vlasy;taška;podlaha|Čo robí vystrašená žena?|Zakrýva si ústa.
645|kresliť kruh;držať čierne pero;mať na ruke hodinky|rozvrh;muž;zápisník;zakladače|Čo kreslí muž?|Kreslí do rozvrhu kruh.
647|strihať vlasy nožnicami;pozerať sa do zrkadla;sedieť na stoličke|nožnice;hrebeň;uterák;okuliare|Čo robí žena s okuliarmi?|Strihá vlasy nožnicami.
649|hrešiť mladého muža;zvierať slamený klobúk;založiť si ruky|šatka;zástera;bránka;hlávky kapusty|Čo robí stará žena?|Hreší mladého muža.
650|liezť po podlahe;mať dlhý vrkoč;nazerať ponad škatuľu|skrutka;kartónová škatuľa;zlatý retriever;palec|Čo hľadá muž?|Hľadá chýbajúcu skrutku.
651|doťahovať skrutku;pridržiavať drevenú policu;sedieť na pohovke|skrutkovač;knihy;mačka;izbová rastlina|Čo robí žena?|Doťahuje skrutku skrutkovačom.
652|narážať do skál;mať na sebe bielu košeľu;mať krátke vlasy|more;žena;muž;skaly|Čo robia?|Skáču do mora.
653|zdvihnúť vankúš;ukazovať na kľúče;ležať pri dverách|kľúče;dvere;mačka;muž|Na čo ukazuje muž?|Ukazuje na kľúče vo dverách.
654|šepkať tajomstvo;počúvať svoju kamarátku;pozerať sa ponad múr|obloha;lampa;hora;okuliare|Čo robí žena v žltom?|Šepká svojej kamarátke tajomstvo.
655|maľovať čiernu čiaru;vbehnúť do miestnosti;trúbiť na malú trúbku|klobúk;okuliare;papier;stôl|Čo robí žena v modrom?|Maľuje na papier čiernu čiaru.
656|stlačiť šachové hodiny;mať na sebe kaki bundu;zdvihnúť obe zaťaté päste|oblúkové okná;lano;šachové hodiny;šachovnica|Čo robí šachistka?|Po svojom ťahu stláča šachové hodiny.
657|podávať jedlo;nalievať trochu vody;pozerať sa na svoje jedlo|žena;pohár;vidlička;stôl|Čo robí žena?|Podáva mužovi jedlo.
660|mydliť vlasy svojej kamarátke;nakláňať sa nad lavór;zachytávať mydlovú vodu|banánové listy;kohútik;lavór;stolček|Čo robí žena v zelenom?|Mydlí vlasy svojej kamarátke.
661|otvárať svoju veľkú tlamu;prísť veľmi blízko;plávať v skupine|ryby;žralok;voda|Čo robí žralok?|Žralok otvára svoju veľkú tlamu.
662|kresliť hviezdu;mať krátke vlasy;žrať trávu|kôň;strúhadlo;zápisník;miska|Čo kreslí žena?|Kreslí hviezdu.
663|nanášať si penu na holenie;pozerať sa do zrkadla;sledovať svojho kamaráta|lampy;zrkadlo;pena na holenie;kohútik|Čo robí muž v modrom?|Nanáša si na tvár penu na holenie.
664|holiť mužovi tvár;ležať v kresle;sedieť pri okne|fľaše;mačka;muž;miska|Čo robí žena?|Holí mužovi tvár.
666|obliekať si košeľu;sledovať muža;zapínať si košeľu|vták;žena;košeľa|Čo robí muž?|Oblieka si modrú košeľu.
667|držať sa za hlavu;ležať na chodníku;zalapať po dychu od šoku|chodec;prilba;skúter;chodník|Čo robí žena?|Od šoku sa drží za hlavu.
668|zaväzovať si topánky;držať poháre s kávou;kráčať cez vodu|dvere;nohavice;topánky;zem|Čo robí žena?|Zaväzuje si hnedé topánky.
669|niesť košík;podať jej chlieb;platiť mincami|lampa;okuliare;chlieb;klobúk|Čo robí žena?|Kupuje v obchode chlieb.
671|mať krátku bradu;niesť modrý batoh;mať dlhý krk|obloha;lama;muž;žena|Čo robia tí dvaja ľudia?|Kričia neďaleko lamy.
672|držať uterák;mať na sebe modré tričko;stáť na sprche|vták;sprcha;uterák;muž|Čo robí žena?|Sprchuje sa na pláži.
674|siakať si nos;priniesť jej šálku;rásť pri okne|rastlina;šálka;deka;stôl|Čo robí žena?|Chorá žena si siaka nos.
675|skláňať sa nad vedrom;nosiť okuliare;sfarbiť sa na žiarivo modro|loď;sieť;muž;vedrá|Čo robí blonďavý muž?|Natiera bok lode.
678|držať zdvihnutý hodváb;mať vlasy po plecia;čupieť na pulte|ventilátor;hodváb;mačka;pult|Čo robí žena v béžovom?|Pritláča si hodváb k lícu.
679|čistiť striebro;nasadiť si náušnice;visieť nad jej hlavou|lampa;striebro;žena|Čo robí žena?|Čistí striebro handričkou.
681|pozerať sa do kamery;šoférovať auto;byť dlhá a rovná|zrkadlo;cesta;muž;žena|Čo robia?|Spievajú v aute.
683|pustiť vodu;držať žltú špongiu;ukazovať čistý tanier|muž;žena;drez;taniere|Čo umývajú v dreze?|Umývajú v dreze taniere.
684|sedieť pri stole;otvoriť dvere;objať obe dievčatá|dvere;dievča;lyžica;vidlička|Čo robia tie dve sestry?|Tie dve sestry sa objímajú.
685|skúšať si klobúky;držať malé zrkadlo;predávať klobúky|obloha;klobúk;vlasy;šaty|Čo robí dievča?|Skúša si klobúky.
687|jazdiť na skateboarde;vyskočiť do vzduchu;svietiť nad mestom|slnko;domy;chlapec;skateboard|Čo robí chlapec?|Jazdí na skateboarde.
688|nanášať si krém na tvár;trieť si ruku;dotýkať sa svojich líc|pokožka;obloha;rastliny;tričko|Čo robí žena?|Nanáša si krém na pokožku.
689|držať si sukňu;otočiť sa dokola;mať na sebe biele topánky|sukňa;tričko;vtáky;stromy|Čo má žena na sebe?|Má na sebe žltú sukňu.
691|strážiť sivé auto;oháňať sa drevenou palicou;byť zaparkované vonku|vojak;ostnatý drôt;betónový múr;poľná cesta|Čo robí vojak?|S palicou stráži auto.
692|zdvihnúť ruky;spať pod dekou;čítať knihu|mačka;lampa;deka;vankúš|Čo robí muž?|Spí pod dekou.
693|šúchať si oči;spať pri okne;ležať na jej lone|okno;sedadlo;sveter;zápisník|Ako sa žena cíti?|Cíti sa veľmi ospalá.
695|opierať sa o svoju ruku;mať na sebe zelený šál;lietať nad loďou|slnko;vtáky;loď;more|Čo robia ľudia?|Usmievajú sa na lodi.
696|smiať sa na mužovi;odháňať dym;stúpať k oblohe|dym;žena;muž;listy|Čo robí muž?|Odháňa dym.
697|mať na sebe červenú bundu;mať čiernu bradu;zapáliť cigaretu|lampa;cigareta;bunda|Čo robí muž v červenom?|Fajčí cigaretu.
698|nalievať smoothie;pridať viac ovocia;mixovať ovocie|smoothie;banány;jahody;žena|Čo robí žena v oranžovom?|Nalieva smoothie do pohára.
699|pašovať syr;zdvihnúť závoru;byť naložený senom|strážnik;seno;závora;voz|Čo pašuje farmár?|Pašuje syr pod senom.
700|pohybovať sa veľmi pomaly;liezť na list;ležať na cestičke|slimák;list;tráva|Čo robí slimák?|Lezie na list.
701|pohybovať sa po piesku;vyplaziť jazyk;ležať pod hadom|had;skala;piesok;obloha|Kde leží had?|Leží na čiernej skale."""
out = {}
for line in D.split("\n"):
    i, p, n, q, a = line.split("|")
    out[i] = {"phrases": p.split(";"), "nouns": n.split(";"), "question": q, "answer": a}
json.dump(out, open(os.path.join(H, "sk.json"), "w"), ensure_ascii=False, indent=1)
print(len(out))
