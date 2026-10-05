import json, os
H=os.path.dirname(os.path.abspath(__file__))
D="""7323|ustlať posteľ|skočiť na posteľ|piť zo šálky|okno;muž;mačka;posteľ|Čo robí žena?|Ustiela posteľ.
7324|opaľovať sa na lehátku|natáčať ho na svoj mobil|sedieť na zasneženej rímse|mrakodrapy;holub;lehátko;bazénik|Čo robí bosý muž?|Naplno si užíva slnko.
7325|mávať kusom naplaveného dreva|štekať na rozprávačku|usrkávať z hrnčeka|naplavené drevo;deka;táborák;gitara|Čo robí stojaca žena?|Rozpráva dramatický príbeh.
7327|zoskočiť z vozíka|stáť vedľa vozíka|štekať na jelene|obloha;samec;vozík;jablká|Čo robí jeleň?|Zoskakuje z vozíka.
7328|bežať so zdvihnutým chvostom|kráčať s palicou|bežať v ružovom tričku|ovce;pes;lampa;stromy|Čo robí pes?|Pes beží vedľa oviec.
7329|nakláňať sa cez bariéru|škeriť sa na ženu|tlieskať páru|usporiadateľ;pončo;fotograf;reflektory|Čo robí žena?|Nakláňa sa cez bariéru.
7332|pridržiavať predné koleso|obsluhovať akumulátorovú vŕtačku|visieť na montážnej linke|skrutky;vŕtačka;pneumatiky;sedlo|Čo robí žena?|Obsluhuje akumulátorovú vŕtačku.
7334|chytiť dosku skejtbordu|hladkať hladkú dosku|driemať pod pracovným stolom|javor;hrnček;pes;piliny|Čo robí žena?|Hladká javorovú dosku.
7336|pádlovať cez marínu|balansovať s podnosom s raňajkami|nakláňať sa cez zábradlie|jachta;mólo;podnos;pádlo|Čo robí muž v slnečných okuliaroch?|Pádluje cez marínu.
7337|nechať vtáka odletieť|kľačať v tráve|sedieť jej na hlave|vták;bunda;krabica;tráva|Čo robí kľačiaca žena?|Drží v rukách vtáka.
7338|pádlovať pozdĺž kanála|kľačať na doske|pásť sa v diaľke|plameniaky;strážna veža;paddleboard;trstina|Čo robí žena?|Pádluje cez močiar.
7339|niesť hmyz|pristáť pri hniezde|strčiť hlavu dovnútra|belorítka;hniezdo;strecha;pole|Čo robí belorítka?|Nesie hmyz do svojho hniezda.
7340|nakláňať sa cez zábradlie|ukazovať na remorkér|nosiť čiapku so šiltom|žeriav;čiapka so šiltom;remorkér;termoska|Čo robí žena?|Hovorí do vysielačky.
7342|tlačiť sa na membránu|mať zatvorené oči|v šoku si zakryť ústa|drevený rám;membrána;muž;stojacia lampa|Čo robí žena?|Tlačí tvár do membrány.
7344|odovzdať obálku|bicyklovať po chodníku|vojsť do otočných dverí|kuriér;žltý taxík;obálka;otočné dvere|Čo robí žena?|Doručuje mužovi obálku.
7345|roztiahnuť ruky doširoka|balansovať na krátkych lyžiach|ťahať lyžiara|drevená chata;diváci;lano;kôň|Kde je uviazané lano?|Je uviazané okolo jeho pása.
7347|hojdať sa na lane|otáčať sa pod prúdiacou vodou|stáť zapriahnutý do voza|múka;mlyn;kôň;vodné koleso|Čo robí žena?|Hojdá sa nad vodným kolesom.
7348|šmýkať sa dolu po hrubom lane|chytiť západku okenice|sypať múku do vreca|ozubené koleso;okno;mlynár;mlynské kamene|Čo robí žena pokrytá múkou?|Šmýka sa dolu po hrubom lane.
7349|viesť rad žien|niesť jazvečíka|nosiť niekoľko zlatých retiazok|vila;jazvečík;milionár;uterák|Čo robí milionár?|Vedie rad žien.
7352|kráčať po mokrom móle|nosiť reflexnú bundu|nosiť oranžovú minisukňu|reflektory;lietadlo;minisukňa;hostia|Čo robí modelka?|Kráča po mokrom móle.
7359|naháňať idúci vlak|zvierať svoje lyže|vykláňať sa z dverí|pouličná lampa;drevená chatka;sprievodca;lyžiarska palica|Čo robí žena?|Naháňa idúci vlak.
7362|chytiť spŕšku smotany|oblizovať sa|šľahať čokoládové cesto|miska na miešanie;bígl;kuchynská minútka;žĺtok|Čo robí bígl?|Chytá spŕšku smotany.
7363|držať telefón hore|stáť na veľkom kameni|jesť sendvič|mobilný telefón;obloha;batoh;mapa|Čo robí žena?|Drží telefón nad hlavou.
7364|stáť na rebríku|držať rebrík|otáčať sa vo vzduchu|presklená strecha;závesná plastika;taška na náradie;rebrík|Čo robí závesná plastika?|Otáča sa vo vzduchu.
7365|zoškrabávať hlinu z auta|tvarovať kus hliny|fotiť v pozadí|hlinený model;otočný stôl;odrezky;stropné svetlá|Čo robí žena?|Zoškrabáva hlinu z auta.
7367|našpúliť pery|predvádzať svoju obrovskú plutvu|driemať na pohovke|molinézia;akvárium;naplavené drevo;sieťka na ryby|Čo robí žena?|Špúli pery ako ryba.
7368|pobozkať ho na líce|pustiť svoju veľkú tašku|vyskakovať na nich|okno;lampa;taška;pes|Čo robí žena?|Bozkáva ho na líce.
7370|pádlovať o život|škľabiť sa od námahy|zrútiť sa do mora|ľadovec;spŕška;prilba;kajak|Čo robí muž vpredu?|Pádluje preč od ľadovca.
7372|vytiahnuť ťažký balík|krčiť sa vedľa lampáša|pridržiavať lano zdola|opica;karimatka;kartónová krabica|Čo robí žena?|Vyťahuje ťažký balík na verandu.
7373|vtesnať sa do úzkej plavebnej komory|kráčať po nábreží|mávať obrovskej lodi|výletná loď;diváci;zábradlie;kamenná chatka|Čo robí výletná loď?|Vtesnáva sa do úzkej plavebnej komory.
7376|plávať v čiernom neopréne|kopať dlhými plutvami|pohupovať sa na hladine|loď;delfín;potápač;húf|Čo robí žena?|Kĺže sa cez húf rýb.
7377|vystúpať po točitom schodisku|natiahnuť sa hore po rondone|podávať kuchársky rondon|kuchársky rondon;točité schodisko;hrniec na vývar|Čo robí mladý muž?|Stúpa po točitom schodisku.
7378|prázdno hľadieť pred seba|vzlykať do kabáta|zvierať mužovi rameno|vrah;vysoké okno;džbán na vodu;spis|Čo robí žena za ním?|Vzlyká do tmavého kabáta.
7379|roztiahnuť ruky doširoka|zdvihnúť obe ruky vysoko|zvierať kovový hrnček|rozprávač;lampáše;stočené lano;taniere|Čo robí stojaci muž?|Rozťahuje ruky doširoka.
7381|ťahať za laso|byť vlečený|žiariť svetlom ohňa|sob;plátenný stan;brezy;laso|Čo robí mladá žena?|Ťahá soba cez sneh.
7382|kľačať na ľade|zakloniť hlavu|vystreliť k oblohe|plameň;drevená chata;plynová fľaša;zamrznuté bubliny|Čo robí žena v červenom?|Kľačí na tmavom ľade.
7383|natiahnuť sa po pohári|spať na pohovke|ležať na zemi|muž;klobúk;podnos;pohár|Čo robí žena?|Naťahuje sa po pohári vody.
7386|zacloniť si oči|šprintovať k svojmu kamarátovi|stáť na stráži pri dverách|basa;dozorca;igelitová taška|Kde stojí strážnik?|Stojí vo dverách basy.
7387|predviesť trik s mincou|zacloniť si oči|zakloniť hlavu|vinič;kamenný múr;minca;broskyne|Čo robí plešatý muž?|Vyťahuje jej mincu spoza ucha.
7389|rozmachovať sa sekerou|visieť na háku|stáť na dreve|prilba;hák;sekera;dub|Čo seká muž?|Seká drevo sekerou.
7392|naolejovať drevený stôl|prechádzať sa po stole|stáť v mláke|plechovka;rukavice;mačka;stolička|Čo robí muž vpredu?|Olejuje dlhý drevený stôl.
7393|nalievať olivový olej|držať okrúhly bochník|držať hore veľký džbán|džbán;osol;chlieb;olivy|Čo robí žena?|Nalieva olivový olej na chlieb.
7394|potiahnuť železnú páku|preplávať medzerou|vystrieť jednu nohu|padací most;plachetnica;pletená čiapka;dlažobné kocky|Čo robí žena?|Ťahá železnú páku.
7395|pádlovať na červenom kajaku|pohupovať sa v diaľke|preraziť cez otvor|otvor;maják;prilba;pena|Čo robí žena?|Pádluje cez úzky otvor.
7396|pozorovať z vysokej trávy|otáčať sa v hmle|odrážať žiariace svetlá|kolotoč;ruské koleso;líška;mláka|Čo robí líška?|Líška pozoruje žiariaci kolotoč.
7398|zdvihnúť cievku s páskou nad hlavu|obsluhovať lis|prevážať vinylové platne|dav;cievka s páskou;dopravníkový pás;vozík|Čo robí žena v rukaviciach?|Zdvíha cievku s páskou nad hlavu.
7401|dýchať cez masku|postaviť sa na nohy|držať kyslíkovú masku|vrchol;oblaky;kapucňa;kyslíková fľaša|Čo robí žena v žltom?|Pritláča mu kyslíkovú masku na tvár.
7402|zbaliť veľkú tašku|niesť čižmu|sedieť vpredu|piesok;zrkadlo;taška;fľaša|Čo robí žena?|Balí veľkú tašku.
7403|nasilu zatvoriť dvere dodávky|sedieť na chladiacom boxe|trčať z dodávky|surfovacie dosky;frisbee;plážová lopta;chladiaci box|Čo robí muž v slnečných okuliaroch?|Nasilu zatvára dvere dodávky.
7406|sušiť sa na slnku|hýbať sa vo vetre|visieť na šnúre na prádlo|obloha;balkón;nohavičky|Čo robia nohavičky?|Sušia sa na slnku.
7407|zakloniť hlavu|škeriť sa z dverí|ležať na nástupišti|sprievodca;kabát ťavej farby;kufor;plátenná taška|Čo robí žena?|Objíma muža na nástupišti.
7408|držať psa|stáť na stoličke|pracovať za barom|muž;noviny;pes;stolička|Čo robí muž?|Dáva psa na stoličku.
7409|zdvihnúť kus ľadu|mať na sebe lezecký postroj|týčiť sa v pozadí|ľadovec;čelenka;kus ľadu;postroj|Čo drží žena?|Drží veľký kus ľadu.
7410|brodiť sa do rieky|upraviť si plavecké okuliare|držať hore podložku s klipom|tabuľa;dav;vodotesný vak;lano|Čo robí bosý muž?|Brodí sa do rieky.
7411|vstať zo stoličky|utešovať mladú ženu|chytať sa za hlavu|hodiny;sudca;notebook;šanón|Čo robí muž v sivom?|Drží sa rukami za hlavu.
7412|vyskočiť do vzduchu|kričať od radosti|sedieť v aute|obloha;dom;autá;cesta|Čo robí žena?|Skáče vedľa auta.
7415|znova naplniť smaltovaný hrnček|nakláňať sa nad novinami|letmo sa pozrieť na hodinky|zákazník;várnica na vodu;slanina;krížovka|Čo robí žena?|Nalieva čaj do smaltovaného hrnčeka.
7416|hladkať draka po nose|niesť prútený košík|túliť sa k lícu ženy|drak;jaskyňa;prútený košík;vychádzková palica|Čo robí drak?|Túli sa k lícu ženy.
7419|okoreniť cestoviny|vybuchnúť smiechom|zdvihnúť obočie|čašník;cestoviny;karafa;obrus|Čo robí žena?|Korení cestoviny.
7420|ukazovať cez pole|ľahnúť si do trávy|utekať pred psom|stan;žena;pes;ovce|Čo robí žena?|Ukazuje cez pole.
7421|dupať po zaprášenom pódiu|pohodiť dlhými vlasmi|brnkať na akustickú gitaru|reflektor;šunky;účinkujúci;gitara|Čo robí tanečník?|Dupe po zaprášenom pódiu.
7422|ťahať za drevený kohútik|pretekať penou|ležať na dláždenej podlahe|sad;sud;hruškové víno;hrušky|Čo sa deje s drevenou kaďou?|Preteká penivým hruškovým vínom.
7425|tryskať z ventilu|pretekať surovou ropou|rozlievať sa po zemi|ventil;hadica;vedro;ropa|Čo sa deje s kovovým vedrom?|Preteká surovou ropou.
7427|točiť sa v slnečnom svetle|roztiahnuť ruky doširoka|opierať sa o zárubňu|oblúkové okno;paleta;fúrik;sutiny|Čo robí žena?|Točí sa v slnečnom svetle.
7428|dotknúť sa kusu skaly|nakloniť sa nad skalu|zacloniť si oči|obloha;klobúk;nákladné auto;kus skaly|Čo robí žena v rukaviciach?|Dotýka sa kusu skaly.
7429|pritlačiť prístrešok|natiahnuť sa po letiacom uteráku|nosiť džínsové šortky|slamený klobúk;more;plážový prístrešok;stanové kolíky|Čo robí žena v bielom?|Pritláča prístrešok k piesku.
7430|vyhodiť celého lososa|letieť vzduchom|sedieť na bielej debničke|losos;pruhovaná mačka;prepravky;mušle|Čo robí žena s konským chvostom?|Vyhadzuje lososa do vzduchu.
7434|šmýkať sa blatom|kričať od radosti|roztiahnuť ruky doširoka|obloha;rukavica;meta;blato|Čo robí žena v pruhovanom drese?|Šmýka sa blatom.
7439|prehrabať oheň|skryť sa za vankúš|držať strieborný podnos|rímsa krbu;pohrabáč;polená;kliešte|Čo robí mladý muž?|Prehrabáva oheň pohrabáčom.
7440|hrabať labou po autobuse|mávať cez okno|pozorovať z diaľky|obloha;pletená čiapka;ľadový medveď;sneh|Čo robí veľký ľadový medveď?|Kráča popri autobuse.
7442|jazdiť bez sedla|niesť bosú jazdkyňu|široko sa usmievať|útes;plot;poník;rieka|Čo robí mladá žena?|Jazdí na poníkovi cez rieku.
7444|ležať pod motorkou|pozerať sa na ňu zhora|jasne svietiť|lampa;náradie;motorka;pes|Čo robí žena?|Leží pod motorkou.
7449|vyhodiť ruky hore|urobiť bolestnú grimasu|stáť v rade na záchod|sprchový záves;záchod;papierový pohár;blato|Čo robí ryšavá žena?|Robí bolestnú grimasu.
7454|predierať sa snehom|zvierať riadidlá|sedieť na skale|prilba;kamenná chata;svišť;cestný bicykel|Čo robí muž v čiernom?|Prediera sa snehom.
7472|ťahať úzku loď|zdvihnúť hrnček|stáť v hmle|tehlový most;volavka;úzka loď;navijak|Čo ťahá muž v kockovanej košeli?|Ťahá úzku loď po kanáli.
7473|pohybovať rukoväťou pumpy|piť z koryta|pretekať vodou|chalupy;pumpa;koryto;vedro|Čo pumpuje žena?|Pumpuje vodu do vedra.
7476|ťahať za nitky bábky|pokloniť sa holubovi|hľadieť na bábku|prizerajúci;bábka;holub;omrvinky|Na čo hľadí holub?|Holub hľadí na bábku.
7478|povaľovať sa na parapete|nechať visieť prednú labku|prechádzať sa po parapete|mačička;parapet;prútený košík;klbko vlny|Čo robí mačička?|Mačička sa prechádza po parapete.
7480|s námahou zatvoriť dvere|zaprieť sa nohami|zabuchnúť sa|stropné svietidlo;dvere trezoru;diamant;vozík|Čo muž s námahou zatvára?|S námahou zatvára dvere trezoru.
7481|pevne sa držať lana|držať zapálenú fakľu|visieť v popruhu|strešné okno;hlinený džbán;skladací rebrík;podstavec|Kam opice kladú džbán?|Kladú ho späť na podstavec.
7482|spustiť drevený blok|krčiť sa za zábradlím|zakrývať si ústa|postroj;balóny;veža;dav|Čo robí žena?|Spúšťa blok na vežu.
7483|dosadnúť na trávu|rozvíriť trávu|prejsť okolo veterného rukáva|veterný rukáv;ľadovec;lietadlo;ovce|Čo robí lietadlo?|Dosadá na trávu.
7488|naklásť vajíčko|byť väčšia ako ostatné|lesknúť sa na slnku|kráľovná;vajíčko;med|Čo robí kráľovná?|Kladie vajíčko.
7492|chŕliť dažďovú vodu|opierať sa o stenu|stáť pod igelitovou fóliou|dážď;markíza;bicykle;barel|Čo sa leje zo strechy?|Z plechovej strechy sa leje silný dážď.
7502|oddeliť dvoch boxerov|roztiahnuť obe ruky|nosiť hnedé boxerské rukavice|rozhodca;diváci;laná|Čo robí rozhodca?|Oddeľuje dvoch boxerov.
7529|oboplávať obrovskú bóju|zdvíhať spŕšku vody|pohupovať sa na rozbúrenom mori|bója;plachta;trup;vlny|Čo robí jachta?|Oboplávava obrovskú bóju.
7738|ťahať sane|mať tmavú bradu|kráčať popri rieke|obloha;mamut;sane;sneh|Čo robí žena?|Ťahá sane.
7740|pozrieť sa cez plece|skúmať pôdu|roztiahnuť krídla|stromy;traktor;pluh;jastrab|Čo robí muž?|Skúma hrsť pôdy.
7741|uskočiť od prekvapenia|vbehnúť do chodby|niesť zabalený darček|lampáš;slnečnice;župan;dlaždice|Čo robí žena v orgovánovom?|Uskakuje od prekvapenia.
7742|visieť na žltom chyte|neveriacky sa chytiť za hlavu|čupieť na modrej žinenke|strešné okno;vrkoč;lezecká stena;dopadová žinenka|Čo robí lezkyňa?|Visí na žltom chyte.
7743|niesť bielu surfovaciu dosku|pridržiavať si kuchársku čiapku|zapínať si krémové sako|čajka;pouličná lampa;surfovacia doska;spadané lístie|Čo robí kuchárka?|Pridržiava si kuchársku čiapku.
7746|mať na sebe biele šaty|mať na sebe sako|visieť na stene|lampa;okno;ruže;torta|Čo krájajú?|Krájajú bielu tortu.
7747|mať na sebe hnedú bundu|mať na sebe tmavomodrú bundu|mať na sebe biele topánky|obloha;domy;loď;voda|Môžu sa ich ruky dotknúť?|Nie, sú od seba príliš ďaleko.
7749|hádzať farbu na plátno|stáť na rebríku|zakloniť hlavu|plátno;rebrík;plechovka farby;lampa|Čo robí žena vpredu?|Hádže farbu na plátno.
7750|hodiť starú pneumatiku|držať hore tabuľu|nasadiť koleso|obloha;žena;koleso;auto|Čo robí žena vpredu?|Mení koleso.
7752|skočiť mu do náručia|tlačiť vozíky|držať kvety|strom;kufor;šálky;kabát|Čo robí žena?|Skáče mu do náručia.
7753|dávať jedlo na tanier|krájať zelenú zeleninu|tlačiť na dvere|žena;panvica;utierka;lampa|Čo robí žena?|Dáva jedlo na tanier.
7754|hrať na gitare|dať peniaze do puzdra|sedieť vedľa puzdra|gitara;pes;bicykel;obloha|Čo robí muž?|Hrá na gitare.
7755|skicovať do plánov|mať na sebe orgovánový kardigán|mať na sebe džínsovú košeľu|izbová rastlina;sako;džbán;technický výkres|Čo robí žena v modrom?|Skicuje do stavebných plánov.
7757|kropiť paradajky|držať hore zrelé paradajky|preplávať okolo záhrady|výletná loď;paradajky;lehátko;krhla|Čo robí muž?|Kropí paradajky hadicou."""
src=json.load(open(f'{H}/source.json'))
out={}
rows={l.split('|')[0]:l.split('|') for l in D.strip().split('\n')}
for k in src:
    r=rows[k]; assert len(r)==7,k
    out[k]={"phrases":r[1:4],"nouns":r[4].split(';'),"question":r[5],"answer":r[6]}
json.dump(out,open(f'{H}/sk.json','w'),ensure_ascii=False,indent=1)
