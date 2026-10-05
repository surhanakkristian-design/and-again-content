import json, os
H = os.path.dirname(os.path.abspath(__file__))
DATA = """
4744|číst časopis;mít na hlavě velký klobouk;mít na sobě černé plavky|klobouk;časopis;chodidla;kopce|Co dělá žena vepředu?|Čte si ve vodě časopis.
4745|dřepět na oblázcích;nechat se unášet po proudu;klenout se nad řekou|kamenný most;peřeje;papírová lodička;tráva|Kudy teče řeka?|Teče pod kamenným mostem.
4746|ukazovat na letadlo;fotit letadla;letět nad muži|letadlo;fotograf;bunda;obloha|Co dělají fotografové?|Fotí letadlo.
4747|držet kousek chleba;usmívat se na ptáky;létat kolem muže|racek;čepice;chléb;moře|Co dělají racci?|Létají kolem muže.
4748|zakrývat zemi pod sebou;patřit letadlu;zůstat jasná a modrá|mraky;křídlo;obloha|Co zakrývá zemi?|Zemi zakrývají bílé mraky.
4749|držet se za ruce ve formaci;plachtit nad alpským údolím;opírat se o proutěný koš|horkovzdušný balon;slunce;pole;proutěný koš|Co dělají parašutisté?|Drží se za ruce ve formaci.
4750|skládat tričko;sahat do koše;být plný oblečení|žena;koš;oblečení;postel|Co dělá žena?|Skládá oblečení na posteli.
4751|držet žlutý deštník;jezdit po kolejích;chodit po čtyřech nohách|deštník;tramvaj;pes;průvodkyně|Co drží průvodkyně?|Drží žlutý deštník.
4752|dělat zklamanou grimasu;vyhodit spálený toast;stát na sporáku|topinkovač;zástěra;obracečka;pánev|Co dělá muž?|Dělá grimasu nad svými spálenými sušenkami.
4753|pevně si zkřížit ruce;nabízet kávu s sebou;mít řídítka omotaná páskou|vousy;kelímek na kávu s sebou;cihlová zeď;sedlo|Co nabízí vousatý muž?|Nabízí mu kávu s sebou.
4754|ukazovat žlutou kartu;skácet se na hřiště;protestovat s otevřenými dlaněmi|žlutá karta;rozhodčí;dres;tráva|Co ukazuje rozhodčí hráči?|Ukazuje mu žlutou kartu.
4756|jezdit na kole;jíst croissant;sedět za ženou|věž;řeka;chléb;košík|Co jí žena?|Jí croissant.
4757|přeskočit bránu;roztáhnout ruce doširoka;svítit na obloze|obloha;pole;kolo;silnice|Co dělá chlapec?|Jede na kole dolů po silnici.
4758|otevřít dveře lednice;dávat jídlo do poliček;ležet v prázdném šuplíku|skříňka;muž;pizza;lednice|Na co se muž dívá?|Dívá se na plnou lednici.
4759|poslouchat bagetu;rovnat plechy s croissanty;shromáždit se před výlohou|pekař;bageta;zástěra;croissanty|Co dělá pekař?|Pekař si drží bagetu u ucha.
4761|rozklepnout vejce;přidat proužky slaniny;rozpalovat pánev|vousy;parka;slanina;plynový vařič|Co dělá muž?|Smaží slaninu na přenosném vařiči.
4762|svírat koženou aktovku;hledět vzhůru na plátno;pokrývat zadní stěnu|strop;socha;podstavec;aktovka|Co dělá muž?|V galerii hledí na obrazy.
4763|rozvalovat se na gauči;ťukat do svítící klávesnice;zobrazovat šampiona|hráč;ovladač;televize;gauč|Kdo se rozvaluje na gauči?|Na gauči se rozvaluje hráč.
4764|skákat na gauči;mít na sobě zelenou mikinu;být plná chipsů|gauč;žena;muž;mísa|Kde skáče žena?|Skáče na gauči.
4766|otevřít zahradní branku;dotýkat se červených rajčat;mít červenou střechu|obloha;dům;žena;květiny|Co otevírá žena?|Otevírá zahradní branku.
4767|stříhat keř;zalévat květiny;mít na sobě modrou zástěru|zahradnice;konev;květiny;stromy|Co dělá zahradnice?|Zalévá květiny.
4768|držet dárek;držet dvě karty;podívat se nahoru a zasmát se|karty;muž;krabice;okno|Co drží muž v hnědém?|Drží dvě červené karty.
4769|zakrýt si ústa;mít na hlavě modrou kšiltovku;dívat se přes plot|plot;obloha;kšiltovka;skály|Kde stojí žena?|Stojí u plotu.
4771|otevřít bránu;usmívat se do kamery;mít hodně oken|palác;brána;obloha;kabát|Co otevírá žena?|Otevírá bránu paláce.
4772|kroužit po obloze;ukazovat na hejno;svírat mu paži|hejno;baret;močál;zábradlí|Na co ukazuje žena?|Ukazuje na hejno ptáků.
4773|hrát na akordeon;mávat na muzikanta;ohlédnout se přes rameno|akordeon;pouzdro na nástroj;cop;dlažební kostky|Co dělají lidé?|Shromažďují se kolem muzikanta.
4775|chovat v náručí novorozence;spát zabalený v dece;mít na sobě tmavou mikinu|novorozenec;deka;polštář;rostliny v květináčích|Kdo je zabalený v dece?|V dece je zabalený novorozenec.
4777|zvednout šálu;otevřít deštník;nést hodně tašek|deštník;muž;žena;nákupní tašky|Co otevírá v dešti?|Otevírá černý deštník.
4778|seřizovat drobná mosazná ozubená kolečka;viset na dřevěném sloupu;tleskat svému kolegovi|kukačkové hodiny;maticové klíče;mladý muž;pracovní stůl|Na co ukazuje žena?|Ukazuje nahoru na vyřezávané kukačkové hodiny.
4779|udělat si selfie;mít nahoře koně;stát na kopci|hrad;stromy;muž;zeď|Co dělá muž?|Dělá si selfie v Německu.
4780|mít na sobě tmavou košili;mít na sobě bílou halenku;mít dlouhé hnědé vlasy|zeď;prsteny;stůl|Jak odcházejí z místnosti?|Odcházejí každý jinými dveřmi.
4781|mít na sobě bílý závoj;plakat radostí;usmívat se na svou nevěstu|strom;ženich;nevěsta|Co dělají muž a žena?|Berou se na zahradě.
4782|skákat přes švihadlo;dívat se na děti;odrážet míč|budova;dívka;žena;hřiště|Co dělá dívka se stuhami?|Skáče přes švihadlo.
4783|držet malý dort;hrát basketbal;držet nad hlavou ceduli|obloha;budova;pár|Co hraje muž?|Hraje basketbal.
4784|převzít velký dárek;dát jí nějaké sušenky;prohlížet si fotoalbum|stará žena;dárek;talíř|Co dostává stará žena?|Dostává velký dárek.
4785|zvednout prázdnou sklenici;mrknout do kamery;mít na sobě polokošili|keře;džbán;terasa|Co dělají se svými sklenicemi?|Ťukají si jimi.
4786|kreslit zářící spirálu;dřepět na okraji vody;tříštit se o břeh|žena;vlny;spirála;písek|Co dělá žena?|Kreslí do písku spirálu.
4789|razítkovat úřední dokument;podepsat dokument;podávat otevřenou složku|mapa;podnikatelka;šanon;psací stůl|Co dělá žena v zeleném?|Razítkuje úřední dokument.
4792|točit se na místě;tleskat radostí;držet v dlaních šálek|dívka;sazenice;zahradní lopatka;hlína|Co sází dívka?|Sází sazenici do hlíny.
4793|ukazovat dětem rukou;mrskat sebou na dřevěném molu;třepotat se nad parkem|vousy;ptačí budka;šroubovák;pracovní stůl|Co je na pracovním stole?|Na pracovním stole je dřevěná ptačí budka.
4794|držet horký plech;číst obrázkovou knížku;spát jí na rameni|strom;babička;čajová konvice;sušenky|Co čte babička?|Čte obrázkovou knížku.
4795|péct sušenky;číst knihu;spát jí na rameni|brýle;dívka;vlna;křeslo|Co babička upekla?|Upekla sušenky.
4796|běžet po štěrkové cestičce;udržovat hrací karty v rovnováze;vyhodit chlapce nahoru|kšiltovka;živý plot;hrací karta;piknikový stůl|Co chlapec udržuje v rovnováze?|Udržuje v rovnováze hrací karty.
4797|dávat sýr na špagety;usmívat se do kamery;zmizet pod sýrem|obloha;číšník;sklenice;sýr|Co dělá číšník?|Dává sýr na špagety.
4798|kráčet nahoru k chrámu;běžet dolů ulicí;držet slaměný klobouk|obloha;chrám;šaty;kameny|Kam kráčí žena?|Kráčí k chrámu.
4800|upravovat si motýlka;nakouknout ženichovi přes rameno;vyjít do zahrady|ženich;živý plot;host;růže|Co si ženich upravuje?|Upravuje si motýlka.
4801|zalévat rostliny;podívat se nahoru a usmát se;vyrůst hodně vysoko|slunečnice;obloha;žena;rajčata|Na co se žena dívá?|Dívá se na vysokou slunečnici.
4802|otevřít dveře;zkřížit si ruce;mít na sobě bílé tričko|strážce;dívka;podlaha|Co otevírá strážce?|Otevírá dveře.
4803|předat kytici;přivítat svého hosta;přijít s vínem|kytice;láhev vína;šála;pokojová rostlina|Co nese žena?|Nese kytici květin.
4804|vést skupinu turistů;pokynout turistům, ať jdou dál;táhnout dřevěný vozík|obloha;květináč;dav;plášť|Co dělá mladý muž?|Vede skupinu turistů.
4805|číst knihu;sedět na schodech;dívat se na město|kostel;fontána;brýle;kniha|Co dělá muž?|Čte knihu.
4806|listovat stránkami;svírat knihu;obdivovat výhled|kupole;střechy;zábradlí|Co dělá muž?|Obdivuje výhled na střechy.
4807|pít pomerančový džus;zvednout velký džbán;utřít si ústa|obloha;oranžové tílko;džbán;sklenice|Co pije muž?|Pije pomerančový džus.
4808|rozčesávat dlouhé vlasy;zaplétat hustý cop;pohodit dlouhými vlasy|okno;lahve šamponu;cop;kadeřnické křeslo|Co dělá kadeřnice?|Zaplétá hustý cop.
4810|zatlouct hřebík;utřít si čelo;podpírat drátěný plot|vysoký kůl;stromy;kladivo;díra|Co dělá muž?|Zatlouká kůl do země.
4811|mít na sobě zářivě oranžové tílko;mít na sobě růžový sportovní top;táhnout se přes hřiště|volejbalová síť;moře;ruce;písek|Co dělají hráči?|Skládají ruce na sebe uprostřed.
4812|úhledně pověsit košili;zapnout horní knoflík;otevřít posuvné dveře|police;ramínka;oranžová košile;pletená vesta|Co dělá muž?|Navléká košili na ramínko.
4813|opírat se o rezavý vyvazovací sloupek;vznášet se nad přístavem;nakládat kontejnerovou loď|jeřáby;kontejnerová loď;remorkér;vyvazovací sloupek|O co se opírá mladý muž?|Opírá se o rezavý vyvazovací sloupek.
4814|sbírat červené papriky;zvednout velkou bramboru;utrhnout velké rajče|žena;koš;brambory;kolečko|Co dělá žena?|Sbírá červené papriky.
4815|masírovat si spánky;zkřivit obličej;položit si hlavu|stropní světla;culík;klávesnice;papírový kelímek|Co dělá žena?|Masíruje si spánky.
4816|dotýkat se hrudi;ukázat mu hodinky;mít na sobě zelené tričko|žena;muž;hodinky;obloha|Co dělá žena?|Dotýká se hrudi.
4818|jít v čele;mít na sobě černé legíny;jít na konci|ukazováček;ponožka;jehlový podpatek;podlahová prkna|Co dělají ti tři lidé?|Zkoušejí chodit na jehlových podpatcích.
4820|křičet na kamarádku;plakat a smát se;usmívat se na kamarádku|vlasy;šaty;náramek;růžové světlo|Co dělají ty dvě ženy?|Objímají se.
4821|přibližovat se k autu;naklonit se k oknu;zářit nad obzorem|slunce;krabice od pizzy;letní šaty;asfalt|Co dělá bosá žena?|Přináší pizzu k autu.
4822|psát zprávu;usmívat se na telefon;schovat se pod deku|obraz;žena;telefon;postel|Co píše žena?|Píše zprávu.
4825|utřít pracovní desku;skládat špinavé misky na sebe;nastříkat špinavou varnou desku|police;vodovodní kohoutek;dřez;podlahová prkna|Co utírá žena?|Utírá špinavou pracovní desku.
4826|valit se přes přehradu;padat do údolí;pokrývat kopce|obloha;stromy;přehrada;voda|Co dělá voda?|Voda se valí přes přehradu.
4828|natírat zeď nazeleno;držet dlouhý váleček;mít na sobě zelené tričko|zeď;muž;váleček|Co dělá muž?|Natírá zeď nazeleno.
4829|svírat kovovou škrabku;přitlačit čepel ke dřevu;zasunout se pod popraskanou barvu|barva;dřevo;škrabka;ruka|Co dělá ruka?|Seškrabává starou barvu škrabkou.
4830|otočit se ve vodě;podívat se nahoru ke světlu;doplavat k hladině jako první|maska;voda;ploutve;lano|Co dělá muž dole?|Plave nahoru k hladině.
4831|máchnout hliníkovou pálkou;rozzářit se úsměvem;balancovat na odpalovacím stojanu|kšiltovka;plot;míček;odpalovací stojan|Co dělá mladý muž?|Posílá míček vysoko nad trávník.
4832|kráčet po úzkém hřebeni;svírat dvě trekové hole;jít po stopách|obloha;vrchol;mraky;hřeben|Co dělá horolezec?|Kráčí po úzkém hřebeni.
4833|jezdit na skateboardu;mít na hlavě černou helmu;dotýkat se silnice|kopec;moře;silnice;helma|Kde jezdí skateboardista?|Jezdí podél pobřeží.
4834|mít na sobě šedé tričko;mít na sobě bílé tričko;ležet na stole|tričko;hračka;mísa;stůl|Na co se chlapci dívají?|Dívají se na hračky v míse.
4835|běžet po ulici;mít na sobě bílé tričko;mít na sobě kraťasy|budova;pouliční lampa;auto;obchod|Co dělá muž?|Běží po ulici ve městě.
4836|propilovat kůru;svírat motorovou pilu;vynořovat se z kmene stromu|medvěd;motorová pila;piliny;kůra|Co dělá muž?|Vyřezává motorovou pilou medvěda.
4837|podat kousek pizzy;stát u stolu;mít na ruce hodinky|salát;pizza;kuře;stůl|Co dělají přátelé?|Jedí u velkého stolu.
4838|házet meloun;zvednout plážový míč;spadnout do písku|obloha;moře;plážový míč;písek|Co dělá žena?|Hází meloun.
4839|tlačit malé auto;přesouvat velkou krabici;sedět na houpačce|dům;strom;auto;silnice|Co dělá mladý muž?|Tlačí malé auto.
4840|schovávat se za závěsem;sedět pod stolem;schovávat se za stromem|okno;dveře;muž;krabice|Co dělá chlapec?|Schovává se za stromem.
4841|hledat klíč;vysypat košík;zvednout klíč|klíč;dveře;žena|Co hledá žena?|Hledá klíč.
4842|opravovat kohoutek;používat vrtačku;opravovat staré auto|obloha;dům;chlapec;auto|Co dělá chlapec?|Opravuje staré auto.
4843|stavět ptačí budku;stavět stan;zvedat dřevěnou stěnu|obloha;konstrukce;lidé;tráva|Co tlačí lidé?|Tlačí dřevěnou stěnu.
4844|krájet meloun;používat sekeru;krájet velkou dýni|obloha;žena;tráva;semínka|Co dělá žena v džínách?|Krájí velkou dýni napůl.
4845|přišívat knoflík;držet bílou látku;zvedat velkou deku|šicí stroj;ruka;látka|Co zvedají ženy?|Zvedají velkou deku.
4846|žehlit kalhoty;napařovat hedvábné šaty;žehlit hromádku ubrousků|noční lampa;zarámovaný obraz;žehlička;kalhoty|Co dělá muž?|Žehlí kalhoty.
4847|sedět na podlaze;uklízet mezi regály;utírat špinavou vodu|světla;dveře;žena;podlaha|Kde sedí žena?|Sedí na podlaze.
4848|přitlačovat hlínu;lít vodu na květiny;nést velkou dýni|obloha;žena;dýně;listy|Co drží žena?|Drží velkou dýni.
4849|držet konev;natahovat se ke květinám;běhat s dětmi|stromy;fontána;duha;tráva|Co dělá muž?|Muž běhá s dětmi.
4850|stát na trávě;jezdit na kole;ukázat palec nahoru|klobouk;fotoaparát;košile|Co drží mladý muž?|Drží velký fotoaparát.
4851|smetat písek štětcem;vypadat velmi překvapeně;mít dlouhé vousy|obloha;socha;písek|Na co se žena dívá?|Dívá se na starověkou sochu.
4853|mžourat na drobné ozubené kolečko;hledět vzhůru na obrovská ozubená kola;odhalovat ozubená kola za sklem|nástěnné hodiny;krbové hodiny;mosazná plechovka;pracovní stůl|Co žena zkoumá?|Zkoumá drobné mosazné ozubené kolečko.
4854|psát na tabuli;používat kalkulačku;stát čelem ke studentům|tabule;brýle;studenti;kalkulačka|Co dělá muž?|Píše na tabuli.
4855|číst kartičku;dotýkat se hlavy;pustit kartičku|brýle;sluchátka;knihy;kartičky|Co dělá muž?|Čte kartičku.
4856|držet červené pero;opravovat test;dotýkat se vlasů|učitelka;papíry;psací stůl|Co dělá učitelka?|Opravuje test.
4857|držet skener;skenovat krabici;utřít si obličej|regály;skener;skladník;krabice|Co dělá skladník?|Skenuje krabici.
4859|skládat velké puzzle;nosit velké brýle;zvednout ruce|okno;knihy;brýle;dílky|Co dělá žena?|Skládá velké puzzle.
4860|nevěřícně zírat;klesnout ke dnu;rozpustit se v obláček|bublinky;tableta;lžíce;pracovní deska|Co dělá žena?|Zírá na šumivou vodu.
4861|zvedat mikrofon;zpívat v lese;padat ze skal|stromy;vodopád;sluchátka;vesta|Co drží žena?|Drží dlouhý mikrofon.
4862|držet dvě jablka;nosit pestrý šátek na hlavě;zvednout ruce|šátek na hlavu;rajčata;taška;stůl|Co dělá žena?|Vybírá si mezi dvěma jablky.
"""
src = json.load(open(f'{H}/source.json'))
rows = {}
for line in DATA.strip().splitlines():
    i, p, n, q, a = line.split('|')
    rows[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/cz.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
