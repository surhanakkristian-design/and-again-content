import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = """
569|kulccsal kinyitni a bejárati ajtót|dús bajuszt viselni|lófarkat viselni|postamester;kulcsok;csomagok;kézikocsi|Mit csinál a postamester?|Egy csomagokkal teli kézikocsit tol.
572|ásni a kertben|kék sálat viselni|egy kerítésen ülni|madár;nő;krumplik;vödör|Mit csinál a nő?|Krumplikat tesz egy vödörbe.
573|narancslevet tölteni|egy nagy palackot tartani|felvenni egy poharat|férfi;nő;palack;poharak|Mit csinál a férfi?|Narancslevet tölt poharakba.
574|tágra nyitni a száját|megérinteni a mellkasát|rövid, fekete hajúnak lenni|fa;ecset;tégely;púder|Mi van a tégelyben?|Púder van a tégelyben.
575|a magasba lendíteni a kezét|kotorászni a táskájában|felemelni egy külső akkumulátort|külső akkumulátor;galambok;rózsák;pad|Mire csatlakoztatják a telefont?|Egy külső akkumulátorra csatlakoztatják.
576|az íróasztalánál imádkozni|összetenni a kezét|felnézni és sírni|nő;laptop;könyvek;lámpa|Mit csinál a nő?|Az íróasztalánál imádkozik.
577|megjósolni az esőt|nevetésben kitörni|hirtelen záport hozni|viharfelhő;esernyő;vállkendő;fű|Mit csinál a nő?|Egy sárga esernyő alatt húzódik meg.
578|kitolni egy motorkerékpárt|kifényesíteni az üzemanyagtartályt|megveregetni a vállát|bandána;üzemanyagtartály;motor;macskakövek|Mit csinál a szerelő?|Büszkén mutatja be a motorkerékpárját.
579|új kódot gépelni|a laptop felé inteni|követni a megrajzolt pályát|robot;laptop;lófarok;szakáll|Mit csinál a nő?|Egy kis robotot programoz.
580|a magasba tartani egy kabátot|egy kosarat vinni|szemüveget viselni|kosár;kabát;ég;szemüveg|Mit csinál a magas nő?|Az esőtől védi a barátnőjét.
581|egy napraforgót szorongatni|egy fát ábrázoló táblát vinni|lobogni a szellőben|napraforgó;pálmafa;ég;tömeg|Mit csinálnak az emberek?|Festett táblákkal tüntetnek.
582|egy széken ülni|keresztbe tenni a karját|megérinteni a vállát|szék;nő;ablak;asztal|Hogy érzi magát a nő?|Büszke az új székére.
584|kézenállást bemutatni|bebizonyítani, hogy téved|ámulatában levegő után kapni|meztelen lábak;leggings;pad;kötött mellény|Mit csinál a fiatal nő?|Kézenállást mutat be, hogy bebizonyítsa, hogy a férfi téved.
585|nyilvánosan zenélni|egy dobozon ülni|vizet lövellni a magasba|utcai lámpa;férfiak;harmonika;tok|Mit csinál a fiatal nő?|Nyilvánosan harmonikán játszik.
588|piros csizmát viselni|fekete csizmát viselni|messze állni|sárga esőkabát;madár;piros csizma;pocsolya|Mit csinál a két ember?|Beleugranak egy nagy pocsolyába.
589|valami pirosat tartani|rövid szakállt viselni|átfutni a füvön|kutya;fű;férfi;kötél|Mit csinál a férfi és a nő?|Egy vastag kötelet húznak.
590|gyors ütéseket bevinni|a magasba tartani a pontkesztyűket|egy láncon lógni|téglafal;bokszzsák;bokszkesztyű;rövidnadrág|Mit csinál a nő?|A pontkesztyűket üti.
591|erőteljes ütéseket bevinni|megtartani a létrát|a mennyezetről lógva lengeni|lánc;bokszzsák;bokszkesztyű;rövidnadrág|Mit csinál a férfi?|Ütéseket visz be a bokszzsákra.
592|sötét szakállt viselni|fehér pólót viselni|végiggurulni az úton|ég;furgon;út|Mit csinál a két férfi?|Egy fehér furgont tolnak.
593|rövid, göndör hajúnak lenni|hosszú, sötét hajúnak lenni|a padlón aludni|ablak;pizsama;ágy;kutya|Mit visel a férfi és a nő?|Pizsamát viselnek.
594|átugrani a lécet|egy zöld zászlót lengetni|diadalmasan rázni az öklét|léc;zászló;lófarok;szőnyeg|Hogyan jut tovább a lány?|Úgy jut tovább, hogy átugorja a lécet.
595|zöld leveleket enni|megmosni az arcát|átugrani a füvön|ég;nyúl;fű;levelek|Mit eszik a nyúl?|Zöld leveleket eszik.
597|átnézni egy ütőn|a háló mögött állni|a kamerába mosolyogni|virágok;labda;háló;ütő|Mit tart a nő?|Egy fekete ütőt tart.
598|szélesre tárni a karját|fehér inget viselni|négy lábon járni|tető;fa;kutya;hajó|Mit csinál a lány?|Az esőben táncol.
599|egy színes labdát vezetni|szerelni a feketébe öltözött férfit|egy fehér labdát uralni|kapu;futball-labda;gyep;tető|Mit csinál a két férfi?|A labdáért küzdenek.
600|két lábon állni|egy pizzaszeletet húzni|nagy, fekete kerekűnek lenni|patkány;pizza;lépcső;ablak|Mit csinál a patkány?|Egy pizzaszeletet húz.
601|borotvával borotválkozni|az órájára mutatni|a mosdókagylón sétálni|borotva;lámpa;tükör;póló|Mit csinál a fehér ruhás férfi?|Borotvával borotválkozik.
604|egy piros almát tartani|gyümölcsöt árulni|egy hosszú nyugtát nyomtatni|nyugta;almák;körték;palackok|Mit néz a férfi?|Egy hosszú nyugtát néz.
606|egy kalitkában ülni|fekete szakállt viselni|göndör hajúnak lenni|recept;madár;palacsinták;férfi|Mit eszik a férfi és a nő?|Palacsintákat esznek.
607|a padlón feküdni|megérinteni a hűtőszekrényt|fekete szakállt viselni|hűtőszekrény;kutya;férfi;nő|Hol áll a férfi és a nő?|A hűtőszekrény mellett állnak.
608|szorítani a kormánykereket|megkönnyebbülten nevetni|a szélvédőn pihenni|kormánykerék;műszerfal;ablaktörlő;melegítőfelső|Mit szorít a sofőr?|A kormánykereket szorítja.
609|egy piros hátizsákot vinni|levenni a bakancsát|kék sálat viselni|ég;tó;szikla;hátizsák|Mit csinál a férfi és a nő?|A füvön pihennek.
610|három szalagot vinni|megölelni a nagy tököt|nagynak és narancssárgának lenni|szalag;tök;kalap;zászlók|Mi van a nagy tökön?|Egy kék szalag van a tökön.
613|bemászni a ringbe|kék kesztyűt viselni|egy vizespalackot tartani|ring;férfi;fal|Mit csinál a férfi?|A ringben bokszol.
615|a víz fölött repülni|lefelé haladni a folyón|a folyó mellett nőni|folyó;madár;levelek;kövek|Mi halad lefelé a folyón?|Két levél halad lefelé a folyón.
616|vörös hajúnak lenni|szürke pulóvert viselni|nagynak és kereknek lenni|szikla;ég;folyó|Min állnak?|Egy nagy sziklán állnak.
618|megkötni egy kötelet|a szekér mögött állni|nagy kerekűnek lenni|fa;kötél;kerék;sár|Mit csinál a nagydarab férfi?|Egy szekeret húz egy kötéllel.
619|felhúzni egy kosarat|a sikátorban várni|végigsétálni egy falon|fűszernövények;narancsok;kosár;kötél|Mit csinál a nő?|Egy kosár narancsot húz fel.
621|a sor mellett állni|rózsaszín kalapot viselni|piros tetejűnek lenni|ég;kalap;növények;föld|Mit csinálnak az emberek?|Kis növényeket ültetnek egy sorba.
622|egy befőttesgumit húzni|megérinteni az arcát|az utcán sétálni|befőttesgumi;nő;férfi;doboz|Mit csinál a nő?|Egy befőttesgumit húz.
623|a telefonját nézni|hozni neki egy kávét|feltenni a lábát|telefon;napszemüveg;bakancs;villa|Mit csinál a fiatal férfi?|A telefonját nézi.
626|egy pohárból inni|nézni a versenyt|az órájára nézni|pohár;óra;ég;futó|Mit csinál a futó?|Egy pohárból iszik.
627|peckesen végigvonulni a szőnyegen|filmezni a barátnőjét|teljesen mozdulatlanul ülni|szőnyeg;fényfüzér;kandalló;állólámpa|Mit csinál a kék ruhás nő?|Peckesen vonul végig a szőnyegen.
628|összecsomagolni néhány könyvet|egy könyvet tartani|a padlón sírni|polcok;szemüveg;könyvek;dobozok|Mit csinál a nő?|A padlón sír.
629|becsukni az ajtót|felakasztani egy dzsekit|sárga dzsekit viselni|nő;férfi;csészék;tűzifa|Mit csuk be a nő?|A nagy faajtót csukja be.
630|egy hosszú kötelet húzni|a nagy kormánykereket fogni|felemelni mindkét karját|tengerész;kormánykerék;kötél;vitorla|Mit csinál a tengerész?|Egy hosszú kötelet húz.
631|felvágni egy uborkát|összekeverni a salátát|egy kis paradicsomot enni|nő;férfi;saláta;asztal|Mit készít a férfi?|Salátát készít.
632|sót szórni a paradicsomokra|rövid, sötét hajúnak lenni|az ablakon kívül állni|madár;só;paradicsomok;kenyér|Mit csinál a nő?|Sót szór a paradicsomokra.
634|száraz homokot önteni|egy bottal rajzolni|elborítani a rajzot|nő;férfi;hullám;homok|Mit csinál a férfi?|Homokot önt a kezébe.
635|felvenni a szandálját|zöld rövidnadrágot viselni|egy padon állni|ég;madár;pad;szandál|Mit viselnek a lábukon?|Szandált viselnek.
636|egy szendvicset készíteni|felvágni a szendvicset|a kosár mögött állni|fák;kacsa;kosár;szendvics|Mit készít a nő?|Egy szendvicset készít.
638|zöld szószt önteni|egy krumplit enni|a füvön ülni|férfi;nő;kutya;szósz|Mit csinál a férfi?|Zöld szószt önt.
639|megfordítani a kolbászokat|egy hot dogot enni|egy serpenyőben feküdni|sapka;sátor;madár;kolbászok|Mit eszik a nő?|Egy hot dogot eszik.
640|felvenni két súlyzót|megmutatni a nagy karját|a mérlegre mutatni|férfi;nő;padló;mérleg|Min áll a férfi?|Egy mérlegen áll.
641|egy kis lisztet önteni|hosszú hajfonatot viselni|a mérlegen kuporogni|rézserpenyők;cirmos macska;keverőtál;konyhai mérleg|Hol kuporog a macska?|A konyhai mérlegen kuporog.
642|az alkarjára mutatni|dús szakállt viselni|megmutatni a sebhelyes sípcsontját|ballonkabát;villanykörte;sebhely;bögrék|Mit mutat a szőke férfi?|Egy sebhelyet mutat a sípcsontján.
644|eltakarni a száját|egy fehér táskát vinni|a magasba tartani egy telefont|szemüveg;haj;táska;padló|Mit csinál a megrémült nő?|Eltakarja a száját.
645|egy kört rajzolni|egy fekete tollat tartani|órát viselni|ütemterv;férfi;jegyzetfüzet;mappák|Mit rajzol a férfi?|Egy kört rajzol az ütemtervre.
647|ollóval hajat vágni|belenézni egy tükörbe|egy széken ülni|olló;fésű;törölköző;szemüveg|Mit csinál a szemüveges nő?|Ollóval hajat vág.
649|szidni a fiatal férfit|egy szalmakalapot szorongatni|összefonni a karját|fejkendő;kötény;kapu;káposzták|Mit csinál az idős nő?|A fiatal férfit szidja.
650|végigmászni a padlón|hosszú hajfonatot viselni|átkukucskálni a doboz fölött|csavar;kartondoboz;golden retriever;hüvelykujj|Mit keres a férfi?|Egy hiányzó csavart keres.
651|meghúzni egy csavart|megtartani a fapolcot|a kanapén kuporogni|csavarhúzó;könyvek;macska;szobanövény|Mit csinál a nő?|Egy csavart húz meg egy csavarhúzóval.
652|a szikláknak csapódni|fehér inget viselni|rövid hajúnak lenni|tenger;nő;férfi;sziklák|Mit csinálnak?|A tengerbe ugranak.
653|felvenni egy párnát|a kulcsokra mutatni|az ajtó mellett feküdni|kulcsok;ajtó;macska;férfi|Mire mutat a férfi?|Az ajtóban lévő kulcsokra mutat.
654|egy titkot súgni|hallgatni a barátnőjét|átnézni a fal fölött|ég;lámpa;hegy;szemüveg|Mit csinál a sárga ruhás nő?|Egy titkot súg a barátnőjének.
655|egy fekete vonalat festeni|berohanni a szobába|egy kis kürtöt fújni|kalap;szemüveg;papír;asztal|Mit csinál a kék ruhás nő?|Egy fekete vonalat fest a papírra.
656|megnyomni a sakkórát|khakiszínű dzsekit viselni|felemelni mindkét ökölbe szorított kezét|boltíves ablakok;kötél;sakkóra;sakktábla|Mit csinál a sakkozó?|A lépése után megnyomja a sakkórát.
657|felszolgálni az ételt|egy kis vizet tölteni|az ételét nézni|nő;pohár;villa;asztal|Mit csinál a nő?|Ételt szolgál fel a férfinak.
660|beszappanozni a barátnője haját|a lavór fölé hajolni|összegyűjteni a szappanos vizet|banánlevelek;csap;lavór;hokedli|Mit csinál a zöld ruhás nő?|Beszappanozza a barátnője haját.
661|kinyitni a nagy száját|nagyon közel jönni|csoportban úszni|halak;cápa;víz|Mit csinál a cápa?|A cápa kinyitja a nagy száját.
662|egy csillagot rajzolni|rövid hajúnak lenni|füvet enni|ló;hegyező;jegyzetfüzet;tál|Mit rajzol a nő?|Egy csillagot rajzol.
663|borotvahabot kenni magára|a tükörbe nézni|figyelni a barátját|lámpák;tükör;borotvahab;csap|Mit csinál a kék ruhás férfi?|Borotvahabot ken az arcára.
664|borotválni a férfi arcát|egy székben feküdni|az ablak mellett ülni|palackok;macska;férfi;tál|Mit csinál a nő?|A férfi arcát borotválja.
666|felvenni egy inget|figyelni a férfit|begombolni az ingét|madár;nő;ing|Mit csinál a férfi?|Egy kék inget vesz fel.
667|a fejét fogni|a járdán feküdni|döbbenten levegő után kapni|gyalogos;sisak;robogó;járda|Mit csinál a nő?|Döbbenten fogja a fejét.
668|megkötni a cipőjét|kávéspoharakat tartani|átgyalogolni a vízen|ajtó;nadrág;cipő;föld|Mit csinál a nő?|A barna cipőjét köti meg.
669|egy kosarat vinni|odaadni neki a kenyeret|érmékkel fizetni|lámpa;szemüveg;kenyér;kalap|Mit csinál a nő?|Kenyeret vásárol egy boltban.
671|rövid szakállt viselni|egy kék hátizsákot vinni|hosszú nyakúnak lenni|ég;láma;férfi;nő|Mit csinál a két ember?|Egy láma közelében kiabálnak.
672|egy törölközőt tartani|kék pólót viselni|a zuhanyon állni|madár;zuhany;törölköző;férfi|Mit csinál a nő?|A tengerparton zuhanyozik.
674|kifújni az orrát|hozni neki egy csészét|az ablak mellett nőni|növény;csésze;takaró;asztal|Mit csinál a nő?|A beteg nő az orrát fújja.
675|egy vödör fölé hajolni|szemüveget viselni|élénkkék színűvé válni|hajó;háló;férfi;vödrök|Mit csinál a szőke férfi?|A hajó oldalát festi.
678|feltartani a selymet|vállig érő hajúnak lenni|a pulton kuporogni|ventilátor;selyem;macska;pult|Mit csinál a bézs ruhás nő?|Selymet szorít az arcához.
679|tisztítani az ezüstöt|fülbevalót felvenni|a feje fölött lógni|lámpa;ezüst;nő|Mit csinál a nő?|Ezüstöt tisztít egy kendővel.
681|a kamerába nézni|vezetni az autót|hosszúnak és egyenesnek lenni|tükör;út;férfi;nő|Mit csinálnak?|Az autóban énekelnek.
683|megnyitni a vizet|egy sárga szivacsot tartani|megmutatni egy tiszta tányért|férfi;nő;mosogató;tányérok|Mit mosnak a mosogatóban?|Tányérokat mosnak a mosogatóban.
684|az asztalnál ülni|kinyitni az ajtót|megölelni a két lányt|ajtó;lány;kanál;villa|Mit csinál a két lánytestvér?|A két lánytestvér öleli egymást.
685|kalapokat felpróbálni|egy kis tükröt tartani|kalapokat árulni|ég;kalap;haj;ruha|Mit csinál a lány?|Kalapokat próbál fel.
687|gördeszkázni|a levegőbe ugrani|a város fölött ragyogni|nap;házak;fiú;gördeszka|Mit csinál a fiú?|Gördeszkázik.
688|arckrémet kenni magára|dörzsölni a karját|megérinteni az orcáját|bőr;ég;növények;póló|Mit csinál a nő?|Krémet ken a bőrére.
689|a szoknyáját fogni|megfordulni|fehér cipőt viselni|szoknya;póló;madarak;fák|Mit visel a nő?|Sárga szoknyát visel.
691|egy szürke autót őrizni|egy fabotot lóbálni|kint parkolni|katona;szögesdrót;betonfal;földút|Mit csinál a katona?|Egy bottal őrzi az autót.
692|felemelni a karját|egy takaró alatt aludni|egy könyvet olvasni|macska;lámpa;takaró;párna|Mit csinál a férfi?|Egy takaró alatt alszik.
693|megdörzsölni a szemét|az ablak mellett aludni|az ölében feküdni|ablak;ülés;pulóver;jegyzetfüzet|Hogy érzi magát a nő?|Nagyon álmosnak érzi magát.
695|a kezére támaszkodni|zöld sálat viselni|a hajó fölött repülni|nap;madarak;hajó;tenger|Mit csinálnak az emberek?|Mosolyognak a hajón.
696|nevetni a férfin|elhessegetni a füstöt|felszállni az égbe|füst;nő;férfi;levelek|Mit csinál a férfi?|Elhessegeti a füstöt.
697|piros dzsekit viselni|fekete szakállt viselni|meggyújtani egy cigarettát|lámpa;cigaretta;dzseki|Mit csinál a piros ruhás férfi?|Egy cigarettát szív.
698|egy turmixot kitölteni|még több gyümölcsöt hozzáadni|összekeverni a gyümölcsöt|turmix;banánok;eprek;nő|Mit csinál a narancssárga ruhás nő?|Egy turmixot tölt egy pohárba.
699|egy kis sajtot csempészni|felemelni a sorompót|szénával megrakva lenni|őr;széna;sorompó;szekér|Mit csempész a gazda?|Sajtot csempész a széna alatt.
700|nagyon lassan haladni|felmászni egy levélre|az ösvényen feküdni|csiga;levél;fű|Mit csinál a csiga?|Felmászik egy levélre.
701|a homokon át haladni|kinyújtani a nyelvét|a kígyó alatt feküdni|kígyó;szikla;homok;ég|Hol fekszik a kígyó?|Egy fekete sziklán fekszik.
"""
out = {}
for line in DATA.strip().split('\n'):
    f = line.split('|'); assert len(f) == 7, line
    out[f[0]] = {"phrases": f[1:4], "nouns": f[4].split(';'), "question": f[5], "answer": f[6]}
src = json.load(open(f'{HERE}/source.json'))
out = {k: out[k] for k in src}
json.dump(out, open(f'{HERE}/hu.json', 'w'), ensure_ascii=False, indent=1)
