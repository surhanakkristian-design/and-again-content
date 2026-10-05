import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """209|dívat se do krabice;strčit tlapku dovnitř;očichávat kameru|kočka;krabice;kamera|Co dělá kočka?|Zvědavá kočka se dívá do krabice.
142|sedět na židli;mít na sobě žlutou šálu;mít na sobě černou bundu|obloha;hrad;most;voda|Co navštěvují ti dva lidé?|Navštěvují velký hrad.
163|pomáhat chlapci;upustit své jídlo;zvednout ruce|lampa;hůlky;ruka|Čím jí chlapec?|Jí hůlkami.
429|přistát na trávě;zvednout obě ruce;mít na sobě fialovou bundu|obloha;helma;bunda;tráva|Co dělá žena v růžovém?|Přistává na trávě.
531|tančit na oslavě;běhat po trávě;létat ve vzduchu|balonek;strom;lidé;pes|Co dělají lidé?|Tančí na oslavě.
4658|řídit staré auto;jít ulicí dolů;mít tmavé sluneční brýle|obloha;moře;žena;volant|Co dělá žena?|Řídí auto u moře.
852|nést talíře s jídlem;mít na krku bílý náhrdelník;běžet přes restauraci|lampa;číšník;stůl;židle|Co dělá číšník?|Nese jídlo ke stolu.
646|mít na rukou fialové rukavice;vycházet ze sklenice;otevřít ústa dokořán|rukavice;brýle;plášť;stůl|Co má žena na rukou?|Na rukou má fialové rukavice.
5580|upravovat mu sako;stát na bedýnce;držet tác|žena;sako;pes;lampa|Co dělá žena?|Upravuje muži sako.
844|zvednout obě ruce;ukazovat na údolí;mít na sobě oranžovou bundu|obloha;údolí;řeka;žena|Na co se dívají?|Dívají se na zelené údolí.
5468|fotit si selfie;mít dlouhé vousy;otevřít oči dokořán|cedule;obloha;žena;muž|Co dělá žena?|Fotí si selfie s mužem.
5215|jet vepředu;jet přes most;mít na sobě barevný dres|hora;helma;kolo;silnice|Co dělá žena?|Jede na svém kole po silnici.
694|krájet rajče na plátky;držet plátek nahoře;ležet na prkénku|rondon;nůž;rajče;prkénko|Co dělá muž?|Nožem krájí rajče na plátky.
757|dát jí krabici;otevřít krabici;držet štěně|obloha;štěně;krabice;stůl|Co drží žena?|Drží malé štěně.
5456|otevřít svůj pas;projít bránou;mít na sobě uniformu|stromy;brýle;ruce;pas|Co drží mladý muž?|Drží svůj pas.
118|používat vrtačku;mít vousy;mít dlouhé vlasy|obloha;muž;žena;pták|Co dělají ti dva lidé?|Staví velkou dřevěnou bednu.
706|mít na sobě červenou bundu;mít na sobě zelenou bundu;chytit velkou sněhovou vločku|sníh;palčák;žena;muž|Co dělají?|Leží ve sněhu.
395|nést krabici;držet klíče;mít na sobě pruhované tričko|dům;obloha;tráva;cestička|Co nese žena?|Nese krabici do domu.
4243|držet hot dog nahoře;opékat párky;platit kartou|kočka;pes;hot dog;párky|Co dělá kočka?|Dělá hot dog.
617|mít na nohou fialové kolečkové brusle;bruslit po cestičce;sedět na lavičce|kolečkové brusle;nápoj;muž;lavička|Co dělá žena?|Bruslí na fialových kolečkových bruslích.
10|držet velký list;zářit jasně zelenou barvou;padat na list|brýle;košile;list;stůl|Kam padá voda?|Voda padá na list.
792|držet žlutý zubní kartáček;vycházet z tuby;čistit si zuby|vlasy;nos;zubní pasta;zubní kartáček|Co dělá žena?|Dává si zubní pastu na zubní kartáček.
7193|řídit červený traktor;mít na sobě bílé šaty;běžet za traktorem|obloha;babička;traktor;pes|Co dělá babička?|Řídí červený traktor.
365|držet dřevěnou lžíci;mít na sobě modré tričko;ležet na lednici|kočka;sluchátka;lžíce;jablka|Co má žena nasazené?|Má nasazená velká bílá sluchátka.
5616|zvednout ruce;držet provázky;létat na obloze|obloha;balonky;muž;auto|Čeho je auto plné?|Auto je plné balonků.
811|běžet k poháru;zvednout trofej;sledovat hráčky|světla;trofej;stůl;podlaha|Co dělají hráčky?|Společně zvedají trofej.
7053|mýt špinavý talíř;utírat talíř;mít na sobě bílé šaty|talíře;muž;žena;dřez|Co dělají?|Myjí nádobí.
704|velmi silně kýchnout;utřít si nos;nést košík|strom;dívka;klobouk;košík|Co dělá muž?|Velmi silně kýchá.
247|pustit červené jablko;padat na kameny;dívat se na zem|chlapec;jablko;tráva|Co dělá chlapec?|Pouští červené jablko.
775|táhnout šachovou figurkou;tleskat rukama;chodit po stole|žena;muž;pták;stůl|Co dělá muž?|Přemýšlí o svém dalším tahu.
4710|stát uprostřed;mít na sobě zelenou bundu;nosit brýle|stromy;ruka;muž|Co dělají ti tři lidé?|Hýbají rukama.
4760|mít na sobě modrou bundu;mít na sobě barevné šaty;objímat se u vody|obloha;bunda;zmrzlina;šaty|O co se dělí ti dva kamarádi?|Dělí se o zmrzlinu.
5007|hledat své klíče;vejít do domu;otáčet se v zámku|zámek;ruka;klíče;dveře|Co hledá žena?|Hledá své klíče.
659|mýt muži vlasy;stát za umyvadlem;zavřít oči|šampon;lahev;ruka;zeď|Co dělá žena?|Myje muži vlasy.
5609|bát se myší;sedět na podlaze;ležet na boku|myš;hrnek;židle;okno|Čeho se muž bojí?|Bojí se myši.
4055|zvednout hlavu;sedět mezi dvěma hračkami;mít červené oči|pes;dinosaurus;postel|Kde sedí pes?|Sedí mezi dvěma dinosaury.
665|jíst zelenou trávu;otevřít tlamu dokořán;jít přes pole|ovce;zeď;obloha;tráva|Co dělá ovce?|Ovce jde přes pole.
518|sedět na větvi;otáčet hlavou;letět mezi stromy|sova;větev;strom|Co dělá sova?|Sova sedí na větvi.
332|jíst zelené listy;sklonit hlavu;pít vodu|žirafa;zebra;voda;obloha|Co dělá žirafa?|Žirafa pije vodu.
82|sedět na květu;letět nad trávou;vlézt do bedýnky|včela;květ;list|Co dělá včela?|Včela sedí na květu.
38|mávat dvěma oranžovými tyčkami;přijíždět k muži;letět na oblohu|letadlo;muž;věž;obloha|Co dělá muž?|Na letišti mává dvěma oranžovými tyčkami.
785|dívat se na své hodinky;ukazovat vlaky a hodiny;přijíždět na nádraží|jízdní řád;chlapec;lavička|Co dělá chlapec?|Dívá se na jízdní řád.
4058|balit hnědý kufr;mít na hlavě červenou kšiltovku;tlačit hodně kufrů|muž;žena;kufry;obloha|Co dělá žena?|Tlačí hodně kufrů.
7999|vyskočit na postel;ležet na zádech;přinést kufry|pes;kočka;postel;okno|Co dělá pes?|Leží na posteli.
7180|skočit do bazénu;nést nápoj;spadnout na zem|kufr;stromy;obloha;číšník|Co dělá muž ve slunečních brýlích?|Skáče do bazénu.
449|ukazovat jedním prstem;držet si obě uši;mít dlouhé vlasy|stromy;muž;žena;pěšina|Co dělají muž a žena?|Poslouchají pod stromy.
4568|skákat po mapě;mít na sobě oranžovou bundu;rozpřáhnout ruce doširoka|dívka;obloha;kontinent;boty|Co dělá dívka v oranžovém?|Skáče po mapě.
721|hodně se smát;nemít vlasy;převrhnout se|sklenice;stůl;žena;chlapec|Co se převrhuje na stole?|Na stole se převrhuje sklenice.
7059|dělat hot dog;stát u grilu;sedět u chleba|pes;kočka;hot dog;chléb|Co dělá pes?|Pes dělá hot dog.
5673|držet oba dorty;držet prázdný talíř;stát u okna|lampa;okno;muž;chléb|Co drží žena v červeném?|Drží oba dorty.
670|tlačit nákupní vozík;kupovat chléb a mléko;vzít mince|žena;mléko;vozík;chléb|Co dělá žena?|Tlačí nákupní vozík.
155|krájet sýr;smažit sýrový sendvič;ležet na podlaze|žena;muž;sýr;pes|Co smaží muž?|Smaží sýrový sendvič.
5282|hrát na kytaru;zpívat do lžíce;stát na pódiu|obloha;kostel;mikrofon;kytara|Co dělá starší muž?|Zpívá píseň s kytarou.
602|číst tlustou knihu;zakrýt si ústa;pít z hrnku|okno;dívka;kniha;stůl|Co dělá dívka?|Čte knihu u stolu.
4827|malovat západ slunce;držet štětec;používat oranžovou barvu|mraky;barva;štětec;ruka|Co dělá ten člověk?|Ten člověk maluje oranžovou barvou.
7853|usmívat se na vázu;sedět na polici;nosit stříbrné prsteny|lampa;žena;kočka;váza|Co se děje s vázou?|Váza roste do velké výšky.
144|chytit červený míč;letět vzduchem;běhat po trávě|míč;mrak;chlapec;tráva|Co dělá chlapec?|Chytá červený míč.
5012|smát se se svou kamarádkou;líbat starou ženu;objímat blonďatou ženu|klobouk;šála;sklenice;stůl|Co dělá starý muž?|Líbá starou ženu.
57|jít nahoru jako první;zvednout jeden prst;jít vzadu|zeď;žena;sedadla|Kde sedí ti tři lidé?|Sedí vzadu.
5382|mluvit s mladým mužem;mluvit se starší ženou;viset na zdi|dům;žena;muž;stůl|Co dělají lidé?|U stolu o něčem diskutují.
353|otevřít dveře;stát v dešti;nalévat vodu|host;květina;svíčka;okno|Co přináší host?|Host přináší květinu.
5560|dát mu čaj;pít horký čaj;sedět na schodu|pes;auto;sníh;lampa|Co pije muž?|Pije horký čaj.
5506|hrát si s míčem;jezdit na skateboardu;mít na hlavě červenou kšiltovku|obloha;zeď;míč;lidé|Co dělají lidé?|Tančí na ulici.
4603|jet na kole;mít na hlavě bílou helmu;rozpřáhnout ruce doširoka|silnice;obloha;helma;kolo|Co dělá muž?|Jede na svém kole po silnici.
122|sedět na lavičce;držet nákupní vozík;jet po silnici|autobusová zastávka;lavička;autobus;silnice|Co dělají lidé?|Čekají na autobusové zastávce.
339|jít ulicí dolů;nést velkou tašku;zůstat v domě|domy;auto;dívka;ulice|Kam jde dívka?|Jde ulicí dolů.
368|letět nad horami;mít černé vousy;mít dlouhé šedé vlasy|vrtulník;dům;muž;bedna|Co letí nad horami?|Nad horami letí červený vrtulník.
5062|jít přes kancelář;držet tablet;kreslit na tabuli|žena;počítač;telefon;hrnek|Kdo kreslí na tabuli?|Na tabuli kreslí šéfová.
472|opravovat auto;držet nástroj;usmívat se do kamery|automechanik;auto;nástroj;podlaha|Co dělá muž?|Opravuje auto.
680|zpívat píseň;dotýkat se svých sluchátek;sedět u stolu|zpěvačka;sluchátka;mikrofon;muž|Co dělá žena?|Zpívá do mikrofonu.
4941|lézt nahoru po žebříku;sedět na stromě;objímat kočku|hasička;kočka;žebřík;strom|Co dělá hasička?|Zachraňuje kočku ze stromu.
3|psát na tabuli;pít z hrnku;otočit se a usmát se|učitelka;hrnek;brýle;tabule|Co dělá učitelka?|Píše na tabuli.
30|otáčet stránky;spát na knize;mít hodně stránek|vlasy;brýle;učebnice;psací stůl|Co dělá žena?|Otáčí stránky učebnice.
31|držet černou tašku;používat notebook;nosit kšiltovku obráceně|světla;studenti;kšiltovka;sedadla|Kde sedí studenti?|Sedí na univerzitě.
100|zavazovat si botu;mít čtyři nohy;mít na sobě šedou bundu|obloha;pes;bota;voda|Co má žena obuté?|Má obuté hnědé boty.
288|mít na sobě bílý oblek;fotit;mít na sobě šedý svetr|stromy;žena;muž;pes|Co mají ti dva lidé na sobě?|Mají na sobě velké obleky.
242|viset na ramínku;točit se pořád dokola;tleskat rukama|citrony;muž;šaty;zrcadlo|Co dělá žena?|Točí se dokola v červených šatech.
868|být větší a větší;mít na sobě bílé tričko;mít na sobě tmavou košili|vlna;žena;muž;písek|Co dělají ti dva lidé?|Utíkají před velkou vlnou.
4015|skákat přes vodu;sledovat ovce;být vysoký a tenký|strom;pes;břeh;voda|Co dělají ovce?|Skáčou přes vodu.
291|rozpřáhnout ruce doširoka;běžet za ženou;stát v řadě|obloha;stromy;pole;pěšina|Co dělá žena?|Běží přes pole.
5108|mávat z lodi;mávat z domu;tančit u bubnů|dům;děti;voda;loď|Co dělají děti?|Mávají z domu.
5660|přecházet silnici;svítit na zeď;procházet kolem lampy|bytový dům;strom;pes;obloha|Co dělá pes?|Pes přechází silnici.
807|běžet na běžeckém pásu;zmáčknout tlačítko;utřít si obličej|běžecký pás;tričko;okna;vlasy|Co dělá žena vepředu?|Běží na běžeckém pásu.
277|dotknout se prstů u nohou;skákat na zahradě;ukázat dva palce nahoru|tričko;nohy;boty;květiny|Co dělá žena?|Cvičí na zahradě.
571|držet vidličku;zvednout prst;stát na ohni|okno;stůl;hrnec;oheň|Co vaří?|Vaří brambory ve velkém hrnci.
4365|nést čerstvé housky;držet ovocný koláč;mít na sobě červenou zástěru|okno;žena;koláč;housky|Co nese stará žena?|Nese čerstvé housky.
121|spálit palačinku;držet utěrku;ležet na talíři|muž;pánev;oheň;palačinka|Co muž spálil?|Spálil palačinku.
5069|užívat si masáž;sedět v křesle;masírovat mu ramena|rostliny;žena;muž;křeslo|Co si muž užívá?|Užívá si masáž.
4788|šeptat jí do ucha;slyšet tajemství;sedět u stolu|rostlina;žena;počítač;stůl|Jak ženy vypadají?|Ženy vypadají velmi šokovaně.
5129|malovat zeď;strhnout pásku;zbarvit se do oranžova|sluchátka;plachta;zeď|Co dělá muž?|Maluje zeď na oranžovo.
358|tlouct do hřebíku;držet kladivo;ležet na slunci|stromy;pes;kladivo;ptačí budka|Do čeho tluče kladivo?|Kladivo tluče do hřebíku.
819|držet deštník;přijít pod deštník;otevřít se nad její hlavou|okno;deštník;ulice;žena|Co drží žena?|Drží velký červený deštník.
741|ohýbat se ve větru;kutálet se ulicí dolů;mít krátké vousy|obloha;strom;moře;silnice|Co dělá strom?|Strom se ohýbá v bouři.
690|mít na sobě bílou košili;mít na sobě modrou košili;mít dlouhé vlasy|obloha;tráva;žena;muž|Na co se dívají?|Dívají se na modrou oblohu.
225|sedět u psacího stolu;mít na sobě modré tričko;přecházet přes psací stůl|knihy;rostlina;sešit;psací stůl|Kde sedí žena?|Sedí u psacího stolu.
92|hodit velkou deku;tahat za deku;mít blond vlasy|okno;pohovka;deka;stůl|Co dělá žena?|Sedí pod velkou dekou.
7809|vzít si jeden dolar;zaplatit za koláč;usmívat se na muže|žena;nápoj;koláč;dolary|Co si žena bere?|Bere si jeden dolar.
731|držet hodně známek;poslat dopis;sedět na poštovní schránce|pták;muž;žena;známky|Co dělá žena?|Posílá dopis.
800|běžet s míčem;tleskat rukama;zvednout ruku|obloha;světlo;míč;tráva|Co dělá muž ve žlutém?|Běží s míčem.
558|letět přes síť;ležet na trávě;držet míč nahoře|míč;síť;stromy;tráva|Co dělají lidé?|Hrají si s míčem."""
src = json.load(open(f'{H}/source.json')); rows = {}
for l in D.split('\n'):
    i, p, n, q, a = l.split('|'); assert i not in rows; rows[i] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/cz.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
