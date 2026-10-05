import json, os
H = os.path.dirname(os.path.abspath(__file__))
DATA = """
4744|čítať časopis;mať na hlave veľký klobúk;mať na sebe čierne plavky|klobúk;časopis;chodidlá;kopce|Čo robí žena vpredu?|Číta časopis vo vode.
4745|čupieť na kamienkoch;unášať sa dolu prúdom;klenúť sa nad riekou|kamenný most;pereje;papierová loďka;tráva|Kade tečie rieka?|Tečie pod kamenným mostom.
4746|ukazovať na lietadlo;fotiť lietadlá;letieť nad mužmi|lietadlo;fotograf;bunda;obloha|Čo robia fotografi?|Fotia lietadlo.
4747|držať kúsok chleba;usmievať sa na vtáky;lietať okolo muža|čajka;čiapka;chlieb;more|Čo robia čajky?|Lietajú okolo muža.
4748|zakrývať zem pod sebou;patriť lietadlu;zostať jasná a modrá|oblaky;krídlo;obloha|Čo zakrýva zem?|Zem zakrývajú biele oblaky.
4749|držať sa za ruky vo formácii;plachtiť nad alpským údolím;opierať sa o prútený kôš|teplovzdušný balón;slnko;polia;prútený kôš|Čo robia parašutisti?|Držia sa za ruky vo formácii.
4750|skladať tričko;siahať do koša;byť plný oblečenia|žena;kôš;oblečenie;posteľ|Čo robí žena?|Skladá oblečenie na posteli.
4751|držať žltý dáždnik;jazdiť po koľajniciach;chodiť po štyroch nohách|dáždnik;električka;pes;sprievodkyňa|Čo drží sprievodkyňa?|Drží žltý dáždnik.
4752|robiť sklamanú grimasu;vyhodiť spálený toast;stáť na sporáku|hriankovač;zástera;obracačka;panvica|Čo robí muž?|Robí grimasu nad svojimi spálenými sušienkami.
4753|pevne si prekrížiť ruky;ponúkať kávu so sebou;mať riadidlá omotané páskou|brada;pohár na kávu so sebou;tehlový múr;sedlo|Čo ponúka bradatý muž?|Ponúka mu kávu so sebou.
4754|ukazovať žltú kartu;zvaliť sa na ihrisko;protestovať s otvorenými dlaňami|žltá karta;rozhodkyňa;dres;tráva|Čo ukazuje rozhodkyňa hráčovi?|Ukazuje mu žltú kartu.
4756|jazdiť na bicykli;jesť croissant;sedieť za ženou|veža;rieka;chlieb;košík|Čo je žena?|Je croissant.
4757|preskočiť bránu;roztiahnuť ruky doširoka;svietiť na oblohe|obloha;pole;bicykel;cesta|Čo robí chlapec?|Ide na bicykli dolu cestou.
4758|otvoriť dvere chladničky;dávať jedlo do poličiek;ležať v prázdnej zásuvke|skrinka;muž;pizza;chladnička|Na čo sa muž pozerá?|Pozerá sa na plnú chladničku.
4759|počúvať bagetu;ukladať plechy s croissantmi;zhromaždiť sa pred výkladom|pekár;bageta;zástera;croissanty|Čo robí pekár?|Pekár si drží bagetu pri uchu.
4761|rozbiť vajce;pridať pásiky slaniny;zohrievať panvicu|brada;parka;slanina;plynový varič|Čo robí muž?|Na prenosnom variči smaží slaninu.
4762|zvierať koženú aktovku;hľadieť hore na plátno;pokrývať zadnú stenu|strop;socha;podstavec;aktovka|Čo robí muž?|V galérii hľadí na obrazy.
4763|rozvaľovať sa na pohovke;ťukať do svietiacej klávesnice;zobrazovať šampióna|hráč;ovládač;televízor;pohovka|Kto sa rozvaľuje na pohovke?|Na pohovke sa rozvaľuje hráč.
4764|skákať na pohovke;mať na sebe zelenú mikinu;byť plná čipsov|pohovka;žena;muž;misa|Kde skáče žena?|Skáče na pohovke.
4766|otvoriť záhradnú bránku;dotýkať sa červených paradajok;mať červenú strechu|obloha;dom;žena;kvety|Čo otvára žena?|Otvára záhradnú bránku.
4767|strihať ker;polievať kvety;mať na sebe modrú zásteru|záhradníčka;krhla;kvety;stromy|Čo robí záhradníčka?|Polieva kvety.
4768|držať darček;držať dve karty;pozrieť sa hore a zasmiať sa|karty;muž;krabica;okno|Čo drží muž v hnedom?|Drží dve červené karty.
4769|zakryť si ústa;mať na hlave modrú šiltovku;pozerať sa cez plot|plot;obloha;šiltovka;skaly|Kde stojí žena?|Stojí pri plote.
4771|otvoriť bránu;usmievať sa do kamery;mať veľa okien|palác;brána;obloha;kabát|Čo otvára žena?|Otvára bránu paláca.
4772|krúžiť po oblohe;ukazovať na kŕdeľ;zvierať mu rameno|kŕdeľ;baretka;močiar;zábradlie|Na čo ukazuje žena?|Ukazuje na kŕdeľ vtákov.
4773|hrať na akordeóne;mávať hudobníkovi;pozrieť sa cez plece|akordeón;puzdro na nástroj;vrkoč;dlažobné kocky|Čo robia ľudia?|Zhromažďujú sa okolo hudobníka.
4775|držať v náručí novorodenca;spať zabalený v deke;mať na sebe tmavú mikinu|novorodenec;deka;vankúš;rastliny v kvetináčoch|Kto je zabalený v deke?|V deke je zabalený novorodenec.
4777|zdvihnúť šál;otvoriť dáždnik;niesť veľa tašiek|dáždnik;muž;žena;nákupné tašky|Čo otvára v daždi?|Otvára čierny dáždnik.
4778|nastavovať drobné mosadzné ozubené kolieska;visieť na drevenom stĺpe;tlieskať svojmu kolegovi|kukučkové hodiny;maticové kľúče;mladý muž;pracovný stôl|Na čo ukazuje žena?|Ukazuje hore na vyrezávané kukučkové hodiny.
4779|urobiť si selfie;mať navrchu kone;stáť na kopci|hrad;stromy;muž;múr|Čo robí muž?|Robí si selfie v Nemecku.
4780|mať na sebe tmavú košeľu;mať na sebe bielu blúzku;mať dlhé hnedé vlasy|stena;prstene;stôl|Ako odchádzajú z miestnosti?|Odchádzajú každý inými dverami.
4781|mať na sebe biely závoj;plakať od radosti;usmievať sa na svoju nevestu|strom;ženích;nevesta|Čo robia muž a žena?|Berú sa v záhrade.
4782|skákať cez švihadlo;pozerať sa na deti;odrážať loptu|budova;dievča;žena;ihrisko|Čo robí dievča so stužkami?|Skáče cez švihadlo.
4783|držať malú tortu;hrať basketbal;držať nad hlavou ceduľu|obloha;budova;pár|Čo hrá muž?|Hrá basketbal.
4784|prevziať veľký darček;dať jej nejaké sušienky;pozerať si fotoalbum|stará žena;darček;tanier|Čo dostáva stará žena?|Dostáva veľký darček.
4785|zdvihnúť prázdny pohár;žmurknúť do kamery;mať na sebe polokošeľu|kríky;džbán;terasa|Čo robia so svojimi pohármi?|Štrngajú si nimi.
4786|kresliť žiariacu špirálu;čupieť na okraji vody;tríštiť sa o breh|žena;vlny;špirála;piesok|Čo robí žena?|Kreslí do piesku špirálu.
4789|pečiatkovať úradný dokument;podpísať dokument;podávať otvorenú zložku|mapa;podnikateľka;šanón;písací stôl|Čo robí žena v zelenom?|Pečiatkuje úradný dokument.
4792|točiť sa na mieste;tlieskať od radosti;držať v dlaniach šálku|dievča;sadenica;záhradná lopatka;zemina|Čo sadí dievča?|Sadí sadenicu do zeminy.
4793|ukazovať deťom rukou;mrskať sa na drevenom móle;trepotať sa nad parkom|brada;vtáčia búdka;skrutkovač;pracovný stôl|Čo je na pracovnom stole?|Na pracovnom stole je drevená vtáčia búdka.
4794|držať horúci plech;čítať obrázkovú knihu;spať jej na pleci|strom;stará mama;čajník;sušienky|Čo číta stará mama?|Číta obrázkovú knihu.
4795|piecť sušienky;čítať knihu;spať jej na pleci|okuliare;dievča;vlna;kreslo|Čo upiekla stará mama?|Upiekla sušienky.
4796|bežať po štrkovom chodníku;udržiavať hracie karty v rovnováhe;vyhodiť chlapca hore|šiltovka;živý plot;hracia karta;piknikový stôl|Čo chlapec udržiava v rovnováhe?|Udržiava v rovnováhe hracie karty.
4797|dávať syr na špagety;usmievať sa do kamery;zmiznúť pod syrom|obloha;čašník;pohár;syr|Čo robí čašník?|Dáva syr na špagety.
4798|kráčať hore k chrámu;bežať dolu ulicou;držať slamený klobúk|obloha;chrám;šaty;kamene|Kam kráča žena?|Kráča k chrámu.
4800|upravovať si motýlika;nakuknúť ženíchovi cez plece;vyjsť do záhrady|ženích;živý plot;hosť;ruža|Čo si ženích upravuje?|Upravuje si motýlika.
4801|polievať rastliny;pozrieť sa hore a usmiať sa;vyrásť veľmi vysoko|slnečnica;obloha;žena;paradajky|Na čo sa žena pozerá?|Pozerá sa na vysokú slnečnicu.
4802|otvoriť dvere;prekrížiť si ruky;mať na sebe biele tričko|strážnik;dievča;podlaha|Čo otvára strážnik?|Otvára dvere.
4803|odovzdať kyticu;privítať svojho hosťa;prísť s vínom|kytica;fľaša vína;šál;izbová rastlina|Čo nesie žena?|Nesie kyticu kvetov.
4804|viesť skupinu turistov;kývať turistom, aby šli ďalej;ťahať drevený vozík|obloha;kvetináč;dav;plášť|Čo robí mladý muž?|Vedie skupinu turistov.
4805|čítať knihu;sedieť na schodoch;pozerať sa na mesto|kostol;fontána;okuliare;kniha|Čo robí muž?|Číta knihu.
4806|listovať stránkami;zvierať knihu;obdivovať výhľad|kupola;strechy;zábradlie|Čo robí muž?|Obdivuje výhľad na strechy.
4807|piť pomarančový džús;zdvihnúť veľký džbán;utrieť si ústa|obloha;oranžové tielko;džbán;poháre|Čo pije muž?|Pije pomarančový džús.
4808|rozčesávať dlhé vlasy;zapletať hrubý vrkoč;pohodiť dlhými vlasmi|okno;fľaše šampónu;vrkoč;kadernícke kreslo|Čo robí kaderníčka?|Zapletá hrubý vrkoč.
4810|zatĺcť klinec;utrieť si čelo;podopierať drôtený plot|vysoký kôl;stromy;kladivo;jama|Čo robí muž?|Zatĺka kôl do zeme.
4811|mať na sebe jasne oranžové tielko;mať na sebe ružový športový top;tiahnuť sa cez ihrisko|volejbalová sieť;more;ruky;piesok|Čo robia hráči?|Kladú ruky na seba v strede.
4812|úhľadne zavesiť košeľu;zapnúť horný gombík;otvoriť posuvné dvere|polica;vešiaky;oranžová košeľa;pletená vesta|Čo robí muž?|Navlieka košeľu na vešiak.
4813|opierať sa o hrdzavý úväzný stĺpik;vznášať sa nad prístavom;nakladať kontajnerovú loď|žeriavy;kontajnerová loď;remorkér;úväzný stĺpik|O čo sa opiera mladý muž?|Opiera sa o hrdzavý úväzný stĺpik.
4814|zbierať červené papriky;zdvihnúť veľký zemiak;odtrhnúť veľkú paradajku|žena;kôš;zemiaky;fúrik|Čo robí žena?|Zbiera červené papriky.
4815|masírovať si spánky;skriviť tvár;položiť si hlavu|stropné svetlá;konský chvost;klávesnica;papierový pohár|Čo robí žena?|Masíruje si spánky.
4816|dotýkať sa hrude;ukázať mu hodinky;mať na sebe zelené tričko|žena;muž;hodinky;obloha|Čo robí žena?|Dotýka sa hrude.
4818|ísť na čele;mať na sebe čierne legíny;ísť na konci|ukazovák;ponožka;ihlový podpätok;podlahové dosky|Čo robia tí traja ľudia?|Skúšajú chodiť na ihlových podpätkoch.
4820|kričať na kamarátku;plakať a smiať sa;usmievať sa na kamarátku|vlasy;šaty;náramok;ružové svetlo|Čo robia tie dve ženy?|Objímajú sa.
4821|približovať sa k autu;nakloniť sa k oknu;žiariť nad obzorom|slnko;krabica od pizze;letné šaty;asfalt|Čo robí bosá žena?|Prináša pizzu k autu.
4822|písať správu;usmievať sa na telefón;schovať sa pod deku|obraz;žena;telefón;posteľ|Čo píše žena?|Píše správu.
4825|utrieť pracovnú dosku;ukladať špinavé misky na seba;nastriekať špinavú varnú dosku|police;vodovodný kohútik;drez;podlahové dosky|Čo utiera žena?|Utiera špinavú pracovnú dosku.
4826|valiť sa cez priehradu;padať do údolia;pokrývať kopce|obloha;stromy;priehrada;voda|Čo robí voda?|Voda sa valí cez priehradu.
4828|natierať stenu nazeleno;držať dlhý valček;mať na sebe zelené tričko|stena;muž;valček|Čo robí muž?|Natiera stenu nazeleno.
4829|zvierať kovovú škrabku;pritlačiť čepeľ k drevu;zasunúť sa pod popraskanú farbu|farba;drevo;škrabka;ruka|Čo robí ruka?|Oškrabuje starú farbu škrabkou.
4830|otočiť sa vo vode;pozrieť sa hore na svetlo;doplávať k hladine ako prvý|maska;voda;plutvy;lano|Čo robí muž dole?|Pláva hore k hladine.
4831|švihnúť hliníkovou pálkou;zaškeriť sa;balansovať na odpaľovacom stojane|šiltovka;plot;loptička;odpaľovací stojan|Čo robí mladý muž?|Posiela loptičku vysoko nad trávnik.
4832|kráčať po úzkom hrebeni;zvierať dve trekingové palice;ísť po stopách|obloha;vrchol;oblaky;hrebeň|Čo robí horolezec?|Kráča po úzkom hrebeni.
4833|jazdiť na skejtborde;mať na hlave čiernu prilbu;dotýkať sa cesty|kopec;more;cesta;prilba|Kde jazdí skejtbordista?|Jazdí pozdĺž pobrežia.
4834|mať na sebe sivé tričko;mať na sebe biele tričko;ležať na stole|tričko;hračka;misa;stôl|Na čo sa chlapci pozerajú?|Pozerajú sa na hračky v mise.
4835|bežať po ulici;mať na sebe biele tričko;mať na sebe kraťasy|budova;pouličná lampa;auto;obchod|Čo robí muž?|Beží po ulici v meste.
4836|prepíliť kôru;zvierať motorovú pílu;vynárať sa z kmeňa stromu|medveď;motorová píla;piliny;kôra|Čo robí muž?|Vyrezáva motorovou pílou medveďa.
4837|podať kúsok pizze;stáť pri stole;mať na ruke hodinky|šalát;pizza;kurča;stôl|Čo robia priatelia?|Jedia pri veľkom stole.
4838|hádzať melón;zdvihnúť plážovú loptu;spadnúť do piesku|obloha;more;plážová lopta;piesok|Čo robí žena?|Hádže melón.
4839|tlačiť malé auto;presúvať veľkú krabicu;sedieť na hojdačke|dom;strom;auto;cesta|Čo robí mladý muž?|Tlačí malé auto.
4840|skrývať sa za závesom;sedieť pod stolom;skrývať sa za stromom|okno;dvere;muž;krabica|Čo robí chlapec?|Skrýva sa za stromom.
4841|hľadať kľúč;vysypať košík;zdvihnúť kľúč|kľúč;dvere;žena|Čo hľadá žena?|Hľadá kľúč.
4842|opravovať kohútik;používať vŕtačku;opravovať staré auto|obloha;dom;chlapec;auto|Čo robí chlapec?|Opravuje staré auto.
4843|stavať vtáčiu búdku;stavať stan;zdvíhať drevenú stenu|obloha;konštrukcia;ľudia;tráva|Čo tlačia ľudia?|Tlačia drevenú stenu.
4844|krájať melón;používať sekeru;krájať veľkú tekvicu|obloha;žena;tráva;semienka|Čo robí žena v džínsoch?|Krája veľkú tekvicu na polovicu.
4845|prišívať gombík;držať bielu látku;zdvíhať veľkú deku|šijací stroj;ruka;látka|Čo zdvíhajú ženy?|Zdvíhajú veľkú deku.
4846|žehliť nohavice;naparovať hodvábne šaty;žehliť kopu servítok|nočná lampa;zarámovaný obraz;žehlička;nohavice|Čo robí muž?|Žehlí nohavice.
4847|sedieť na podlahe;upratovať medzi policami;utierať špinavú vodu|svetlá;dvere;žena;podlaha|Kde sedí žena?|Sedí na podlahe.
4848|pritláčať zeminu;liať vodu na kvety;niesť veľkú tekvicu|obloha;žena;tekvica;listy|Čo drží žena?|Drží veľkú tekvicu.
4849|držať krhlu;naťahovať sa ku kvetom;behať s deťmi|stromy;fontána;dúha;tráva|Čo robí muž?|Muž behá s deťmi.
4850|stáť na tráve;jazdiť na bicykli;ukázať palec hore|klobúk;fotoaparát;košeľa|Čo drží mladý muž?|Drží veľký fotoaparát.
4851|zmetať piesok štetcom;vyzerať veľmi prekvapene;mať dlhú bradu|obloha;socha;piesok|Na čo sa žena pozerá?|Pozerá sa na starovekú sochu.
4853|žmúriť na drobné ozubené koliesko;hľadieť hore na obrovské ozubené kolesá;odhaľovať ozubené kolesá za sklom|nástenné hodiny;krbové hodiny;mosadzná plechovka;pracovný stôl|Čo žena skúma?|Skúma drobné mosadzné ozubené koliesko.
4854|písať na tabuľu;používať kalkulačku;stáť čelom k študentom|tabuľa;okuliare;študenti;kalkulačka|Čo robí muž?|Píše na tabuľu.
4855|čítať kartičku;dotýkať sa hlavy;pustiť kartičku|okuliare;slúchadlá;knihy;kartičky|Čo robí muž?|Číta kartičku.
4856|držať červené pero;opravovať test;dotýkať sa vlasov|učiteľka;papiere;písací stôl|Čo robí učiteľka?|Opravuje test.
4857|držať skener;skenovať krabicu;utrieť si tvár|police;skener;skladník;krabice|Čo robí skladník?|Skenuje krabicu.
4859|skladať veľké puzzle;nosiť veľké okuliare;zdvihnúť ruky|okno;knihy;okuliare;dieliky|Čo robí žena?|Skladá veľké puzzle.
4860|neveriacky hľadieť;klesnúť na dno;rozpustiť sa v oblak|bublinky;tableta;lyžica;pracovná doska|Čo robí žena?|Hľadí na šumivú vodu.
4861|zdvíhať mikrofón;spievať v lese;padať zo skál|stromy;vodopád;slúchadlá;vesta|Čo drží žena?|Drží dlhý mikrofón.
4862|držať dve jablká;nosiť pestrú šatku na hlave;zdvihnúť ruky|šatka na hlavu;paradajky;taška;stôl|Čo robí žena?|Vyberá si medzi dvoma jablkami.
"""
src = json.load(open(f'{H}/source.json'))
rows = {}
for line in DATA.strip().splitlines():
    i, p, n, q, a = line.split('|')
    rows[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: rows[i] for i in src}
json.dump(out, open(f'{H}/sk.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
