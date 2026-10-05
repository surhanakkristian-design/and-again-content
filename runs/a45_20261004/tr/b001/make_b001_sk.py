import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = """209|pozerať sa do krabice;vložiť labku dovnútra;ovoniavať kameru|mačka;krabica;kamera|Čo robí mačka?|Zvedavá mačka sa pozerá do krabice.
142|sedieť na stoličke;mať na sebe žltý šál;mať na sebe čiernu bundu|obloha;hrad;most;voda|Čo navštevujú tí dvaja ľudia?|Navštevujú veľký hrad.
163|pomáhať chlapcovi;upustiť svoje jedlo;zdvihnúť ruky|lampa;paličky;ruka|Čím je chlapec?|Je paličkami.
429|pristáť na tráve;zdvihnúť obe ruky;mať na sebe fialovú bundu|obloha;prilba;bunda;tráva|Čo robí žena v ružovom?|Pristáva na tráve.
531|tancovať na oslave;behať po tráve;lietať vo vzduchu|balón;strom;ľudia;pes|Čo robia ľudia?|Tancujú na oslave.
4658|šoférovať staré auto;kráčať dolu ulicou;mať tmavé slnečné okuliare|obloha;more;žena;volant|Čo robí žena?|Šoféruje auto pri mori.
852|niesť taniere s jedlom;mať na krku biely náhrdelník;bežať cez reštauráciu|lampa;čašník;stôl;stolička|Čo robí čašník?|Nesie jedlo k stolu.
646|mať na rukách fialové rukavice;vychádzať z pohára;otvoriť ústa dokorán|rukavica;okuliare;plášť;stôl|Čo má žena na rukách?|Na rukách má fialové rukavice.
5580|upravovať mu sako;stáť na debničke;držať tácku|žena;sako;pes;lampa|Čo robí žena?|Upravuje mužovi sako.
844|zdvihnúť obe ruky;ukazovať na údolie;mať na sebe oranžovú bundu|obloha;údolie;rieka;žena|Na čo sa pozerajú?|Pozerajú sa na zelené údolie.
5468|robiť si selfie;mať dlhú bradu;otvoriť oči dokorán|tabuľa;obloha;žena;muž|Čo robí žena?|Robí si selfie s mužom.
5215|jazdiť vpredu;jazdiť cez most;mať na sebe farebný dres|hora;prilba;bicykel;cesta|Čo robí žena?|Jazdí na svojom bicykli po ceste.
694|krájať paradajku na plátky;držať plátok hore;ležať na doske|rondón;nôž;paradajka;doska|Čo robí muž?|Nožom krája paradajku na plátky.
757|dať jej krabicu;otvoriť krabicu;držať šteňa|obloha;šteňa;krabica;stôl|Čo drží žena?|Drží malé šteňa.
5456|otvoriť svoj pas;prejsť bránou;mať na sebe uniformu|stromy;okuliare;ruky;pas|Čo drží mladý muž?|Drží svoj pas.
118|používať vŕtačku;mať bradu;mať dlhé vlasy|obloha;muž;žena;vták|Čo robia tí dvaja ľudia?|Stavajú veľkú drevenú debnu.
706|mať na sebe červenú bundu;mať na sebe zelenú bundu;chytiť veľkú snehovú vločku|sneh;palčiak;žena;muž|Čo robia?|Ležia v snehu.
395|niesť krabicu;držať kľúče;mať na sebe pruhované tričko|dom;obloha;tráva;chodník|Čo nesie žena?|Nesie krabicu do domu.
4243|držať hot dog hore;opekať párky;platiť kartou|mačka;pes;hot dog;párky|Čo robí mačka?|Robí hot dog.
617|mať na nohách fialové kolieskové korčule;korčuľovať sa po chodníku;sedieť na lavičke|kolieskové korčule;nápoj;muž;lavička|Čo robí žena?|Korčuľuje sa na fialových kolieskových korčuliach.
10|držať veľký list;žiariť jasnou zelenou farbou;padať na list|okuliare;košeľa;list;stôl|Kam padá voda?|Voda padá na list.
792|držať žltú zubnú kefku;vychádzať z tuby;umývať si zuby|vlasy;nos;zubná pasta;zubná kefka|Čo robí žena?|Dáva si zubnú pastu na zubnú kefku.
7193|šoférovať červený traktor;mať na sebe biele šaty;bežať za traktorom|obloha;babka;traktor;pes|Čo robí babka?|Šoféruje červený traktor.
365|držať drevenú lyžicu;mať na sebe modré tričko;ležať na chladničke|mačka;slúchadlá;lyžica;jablká|Čo má žena nasadené?|Má nasadené veľké biele slúchadlá.
5616|zdvihnúť ruky;držať šnúrky;lietať na oblohe|obloha;balóny;muž;auto|Čoho je auto plné?|Auto je plné balónov.
811|bežať k poháru;zdvihnúť trofej;sledovať hráčky|svetlá;trofej;stôl;podlaha|Čo robia hráčky?|Spoločne dvíhajú trofej.
7053|umývať špinavý tanier;utierať tanier;mať na sebe biele šaty|taniere;muž;žena;drez|Čo robia?|Umývajú riad.
704|veľmi silno kýchnuť;utrieť si nos;niesť košík|strom;dievča;klobúk;košík|Čo robí muž?|Veľmi silno kýcha.
247|pustiť červené jablko;padať na kamene;pozerať sa na zem|chlapec;jablko;tráva|Čo robí chlapec?|Púšťa červené jablko.
775|pohnúť šachovou figúrkou;tlieskať rukami;chodiť po stole|žena;muž;vták;stôl|Čo robí muž?|Premýšľa o svojom ďalšom ťahu.
4710|stáť v strede;mať na sebe zelenú bundu;nosiť okuliare|stromy;ruka;muž|Čo robia tí traja ľudia?|Hýbu rukami.
4760|mať na sebe modrú bundu;mať na sebe farebné šaty;objímať sa pri vode|obloha;bunda;zmrzlina;šaty|O čo sa delia tí dvaja kamaráti?|Delia sa o zmrzlinu.
5007|hľadať svoje kľúče;vojsť do domu;otáčať sa v zámke|zámka;ruka;kľúče;dvere|Čo hľadá žena?|Hľadá svoje kľúče.
659|umývať mužovi vlasy;stáť za umývadlom;zavrieť oči|šampón;fľaša;ruka;stena|Čo robí žena?|Umýva mužovi vlasy.
5609|báť sa myší;sedieť na podlahe;ležať na boku|myš;šálka;stolička;okno|Čoho sa muž bojí?|Bojí sa myši.
4055|zdvihnúť hlavu;sedieť medzi dvoma hračkami;mať červené oči|pes;dinosaurus;posteľ|Kde sedí pes?|Sedí medzi dvoma dinosaurami.
665|jesť zelenú trávu;otvoriť papuľu dokorán;ísť cez pole|ovca;múr;obloha;tráva|Čo robí ovca?|Ovca ide cez pole.
518|sedieť na konári;otáčať hlavou;letieť pomedzi stromy|sova;konár;strom|Čo robí sova?|Sova sedí na konári.
332|jesť zelené listy;skloniť hlavu;piť vodu|žirafa;zebra;voda;obloha|Čo robí žirafa?|Žirafa pije vodu.
82|sedieť na kvete;letieť nad trávou;vojsť do debničky|včela;kvet;list|Čo robí včela?|Včela sedí na kvete.
38|mávať dvoma oranžovými paličkami;prichádzať k mužovi;letieť na oblohu|lietadlo;muž;veža;obloha|Čo robí muž?|Na letisku máva dvoma oranžovými paličkami.
785|pozerať sa na svoje hodinky;ukazovať vlaky a hodiny;prichádzať na stanicu|cestovný poriadok;chlapec;lavička|Čo robí chlapec?|Pozerá sa na cestovný poriadok.
4058|baliť hnedý kufor;mať na hlave červenú šiltovku;tlačiť veľa kufrov|muž;žena;kufre;obloha|Čo robí žena?|Tlačí veľa kufrov.
7999|vyskočiť na posteľ;ležať na chrbte;priniesť kufre|pes;mačka;posteľ;okno|Čo robí pes?|Leží na posteli.
7180|skočiť do bazéna;niesť nápoj;spadnúť na zem|kufor;stromy;obloha;čašník|Čo robí muž v slnečných okuliaroch?|Skáče do bazéna.
449|ukazovať jedným prstom;držať si obe uši;mať dlhé vlasy|stromy;muž;žena;chodník|Čo robia muž a žena?|Počúvajú pod stromami.
4568|skákať po mape;mať na sebe oranžovú bundu;roztiahnuť ruky doširoka|dievča;obloha;kontinent;topánky|Čo robí dievča v oranžovom?|Skáče po mape.
721|veľa sa smiať;nemať vlasy;prevrátiť sa|pohár;stôl;žena;chlapec|Čo sa prevracia na stole?|Na stole sa prevracia pohár.
7059|robiť hot dog;stáť pri grile;sedieť pri chlebe|pes;mačka;hot dog;chlieb|Čo robí pes?|Pes robí hot dog.
5673|držať obe torty;držať prázdny tanier;stáť pri okne|lampa;okno;muž;chlieb|Čo drží žena v červenom?|Drží obe torty.
670|tlačiť nákupný vozík;kupovať chlieb a mlieko;vziať mince|žena;mlieko;vozík;chlieb|Čo robí žena?|Tlačí nákupný vozík.
155|krájať syr;smažiť syrový sendvič;ležať na podlahe|žena;muž;syr;pes|Čo smaží muž?|Smaží syrový sendvič.
5282|hrať na gitare;spievať do lyžice;stáť na pódiu|obloha;kostol;mikrofón;gitara|Čo robí starší muž?|Spieva pieseň s gitarou.
602|čítať hrubú knihu;zakryť si ústa;piť zo šálky|okno;dievča;kniha;stôl|Čo robí dievča?|Číta knihu pri stole.
4827|maľovať západ slnka;držať štetec;používať oranžovú farbu|oblaky;farba;štetec;ruka|Čo robí ten človek?|Ten človek maľuje oranžovou farbou.
7853|usmievať sa na vázu;sedieť na polici;nosiť strieborné prstene|lampa;žena;mačka;váza|Čo sa deje s vázou?|Váza rastie do veľkej výšky.
144|chytiť červenú loptu;letieť vzduchom;behať po tráve|lopta;oblak;chlapec;tráva|Čo robí chlapec?|Chytá červenú loptu.
5012|smiať sa so svojou kamarátkou;bozkávať starú ženu;objímať plavovlasú ženu|klobúk;šál;pohár;stôl|Čo robí starý muž?|Bozkáva starú ženu.
57|ísť hore ako prvá;zdvihnúť jeden prst;ísť vzadu|múr;žena;sedadlá|Kde sedia tí traja ľudia?|Sedia vzadu.
5382|rozprávať sa s mladým mužom;rozprávať sa so staršou ženou;visieť na stene|dom;žena;muž;stôl|Čo robia ľudia?|Pri stole o niečom diskutujú.
353|otvoriť dvere;stáť v daždi;nalievať vodu|hosť;kvetina;sviečka;okno|Čo prináša hosť?|Hosť prináša kvetinu.
5560|dať mu čaj;piť horúci čaj;sedieť na schode|pes;auto;sneh;lampa|Čo pije muž?|Pije horúci čaj.
5506|hrať sa s loptou;jazdiť na skateboarde;mať na hlave červenú šiltovku|obloha;stena;lopta;ľudia|Čo robia ľudia?|Tancujú na ulici.
4603|jazdiť na bicykli;mať na hlave bielu prilbu;roztiahnuť ruky doširoka|cesta;obloha;prilba;bicykel|Čo robí muž?|Jazdí na svojom bicykli po ceste.
122|sedieť na lavičke;držať nákupný vozík;ísť po ceste|autobusová zastávka;lavička;autobus;cesta|Čo robia ľudia?|Čakajú na autobusovej zastávke.
339|ísť dolu ulicou;niesť veľkú tašku;zostať v dome|domy;auto;dievča;ulica|Kam ide dievča?|Ide dolu ulicou.
368|letieť nad horami;mať čiernu bradu;mať dlhé sivé vlasy|vrtuľník;dom;muž;debna|Čo letí nad horami?|Nad horami letí červený vrtuľník.
5062|kráčať cez kanceláriu;držať tablet;kresliť na tabuľu|žena;počítač;telefón;šálka|Kto kreslí na tabuľu?|Na tabuľu kreslí šéfka.
472|opravovať auto;držať nástroj;usmievať sa do kamery|automechanik;auto;nástroj;podlaha|Čo robí muž?|Opravuje auto.
680|spievať pieseň;dotýkať sa svojich slúchadiel;sedieť za stolom|speváčka;slúchadlá;mikrofón;muž|Čo robí žena?|Spieva do mikrofónu.
4941|liezť hore po rebríku;sedieť na strome;objímať mačku|hasička;mačka;rebrík;strom|Čo robí hasička?|Zachraňuje mačku zo stromu.
3|písať na tabuľu;piť zo šálky;otočiť sa a usmiať sa|učiteľka;šálka;okuliare;tabuľa|Čo robí učiteľka?|Píše na tabuľu.
30|otáčať strany;spať na knihe;mať veľa strán|vlasy;okuliare;učebnica;písací stôl|Čo robí žena?|Otáča strany učebnice.
31|držať čiernu tašku;používať notebook;nosiť šiltovku naopak|svetlá;študenti;šiltovka;sedadlá|Kde sedia študenti?|Sedia na univerzite.
100|zaväzovať si topánku;mať štyri nohy;mať na sebe sivú bundu|obloha;pes;topánka;voda|Čo má žena obuté?|Má obuté hnedé topánky.
288|mať na sebe biely oblek;fotiť;mať na sebe sivý sveter|stromy;žena;muž;pes|Čo majú tí dvaja ľudia na sebe?|Majú na sebe veľké obleky.
242|visieť na vešiaku;točiť sa stále dokola;tlieskať rukami|citróny;muž;šaty;zrkadlo|Čo robí žena?|Točí sa dokola v červených šatách.
868|byť čoraz väčšia;mať na sebe biele tričko;mať na sebe tmavú košeľu|vlna;žena;muž;piesok|Čo robia tí dvaja ľudia?|Utekajú pred veľkou vlnou.
4015|skákať cez vodu;sledovať ovce;byť vysoký a tenký|strom;pes;breh;voda|Čo robia ovce?|Skáču cez vodu.
291|roztiahnuť ruky doširoka;bežať za ženou;stáť v rade|obloha;stromy;pole;chodník|Čo robí žena?|Beží cez pole.
5108|mávať z člna;mávať z domu;tancovať pri bubnoch|dom;deti;voda;čln|Čo robia deti?|Mávajú z domu.
5660|prechádzať cez cestu;svietiť na stenu;prechádzať okolo lampy|bytový dom;strom;pes;obloha|Čo robí pes?|Pes prechádza cez cestu.
807|bežať na bežiacom páse;stlačiť tlačidlo;utrieť si tvár|bežiaci pás;tričko;okná;vlasy|Čo robí žena vpredu?|Beží na bežiacom páse.
277|dotknúť sa prstov na nohách;skákať v záhrade;ukázať dva palce hore|tričko;nohy;topánky;kvety|Čo robí žena?|Cvičí v záhrade.
571|držať vidličku;zdvihnúť prst;stáť na ohni|okno;stôl;hrniec;oheň|Čo varia?|Varia zemiaky vo veľkom hrnci.
4365|niesť čerstvé žemle;držať ovocný koláč;mať na sebe červenú zásteru|okno;žena;koláč;žemle|Čo nesie stará žena?|Nesie čerstvé žemle.
121|spáliť palacinku;držať utierku;ležať na tanieri|muž;panvica;oheň;palacinka|Čo muž spálil?|Spálil palacinku.
5069|vychutnávať si masáž;sedieť v kresle;masírovať mu plecia|rastliny;žena;muž;kreslo|Čo si muž vychutnáva?|Vychutnáva si masáž.
4788|šepkať jej do ucha;počuť tajomstvo;sedieť za stolom|rastlina;žena;počítač;stôl|Ako vyzerajú ženy?|Ženy vyzerajú veľmi šokovane.
5129|maľovať stenu;strhnúť pásku;sfarbiť sa na oranžovo|slúchadlá;plachta;stena|Čo robí muž?|Maľuje stenu na oranžovo.
358|udierať do klinca;držať kladivo;ležať na slnku|stromy;pes;kladivo;vtáčia búdka|Do čoho udiera kladivo?|Kladivo udiera do klinca.
819|držať dáždnik;prísť pod dáždnik;otvoriť sa nad jej hlavou|okno;dáždnik;ulica;žena|Čo drží žena?|Drží veľký červený dáždnik.
741|ohýbať sa vo vetre;kotúľať sa dolu ulicou;mať krátku bradu|obloha;strom;more;cesta|Čo robí strom?|Strom sa ohýba v búrke.
690|mať na sebe bielu košeľu;mať na sebe modrú košeľu;mať dlhé vlasy|obloha;tráva;žena;muž|Na čo sa pozerajú?|Pozerajú sa na modrú oblohu.
225|sedieť pri písacom stole;mať na sebe modré tričko;prechádzať cez písací stôl|knihy;rastlina;zošit;písací stôl|Kde sedí žena?|Sedí pri písacom stole.
92|hodiť veľkú deku;ťahať deku;mať blond vlasy|okno;pohovka;deka;stôl|Čo robí žena?|Sedí pod veľkou dekou.
7809|vziať si jeden dolár;zaplatiť za koláč;usmievať sa na muža|žena;nápoj;koláč;doláre|Čo si žena berie?|Berie si jeden dolár.
731|držať veľa známok;poslať list;sedieť na poštovej schránke|vták;muž;žena;známky|Čo robí žena?|Posiela list.
800|bežať s loptou;tlieskať rukami;zdvihnúť ruku|obloha;svetlo;lopta;tráva|Čo robí muž v žltom?|Beží s loptou.
558|letieť ponad sieť;ležať na tráve;držať loptu hore|lopta;sieť;stromy;tráva|Čo robia ľudia?|Hrajú sa s loptou."""
src = json.load(open(f'{H}/source.json')); rows = {}
for l in D.split('\n'):
    i, p, n, q, a = l.split('|'); assert i not in rows; rows[i] = {'phrases': p.split(';'), 'nouns': n.split(';'), 'question': q, 'answer': a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/sk.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
