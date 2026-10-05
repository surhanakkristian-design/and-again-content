import json, os
H = os.path.dirname(os.path.abspath(__file__))
rows = r"""
5099|egy csíkos inget viselni;egy fényképezőgépet vinni;hozzátenni a fotóját|nő;fotó;térkép|Mit csinál a szőke nő?|Hozzáteszi a fotóját a térképhez.
5100|feltűzni egy zöld zászlót;egy piros pulóvert viselni;felragasztani egy fotót Ázsiára|fényfüzérek;térkép;póló;fényképezőgép|Mit csinál a sárga ruhás férfi?|Felragaszt egy fotót Ázsiára.
5101|megkapaszkodni a korlátban;tengeribeteg lenni;lerogyni egy padra|utasok;a tenger;pad;fonat|Mit csinál a nő?|A szájára szorítja a kezét.
5102|átpréselni magát egy férfi mellett;a levegőbe öklözni;sötét napszemüveget viselni|lámpás;napellenző;hátizsák;sikátor|Mit csinál a nő?|Átpréseli magát egy férfi mellett a sikátorban.
5103|megérinteni a nyakát;megkötni egy sálat;lehajtani a hosszú nyakát|nyak;fák;sál;kerítés|Mit csinál a zsiráf?|Lehajtja a hosszú nyakát.
5106|biciklizni egy csatorna mentén;beleharapni egy gofriba;forgatni a lapátjait|az ég;szélmalom;esőkabát;tulipánok|Mit eszik a nő?|Egy ragacsos karamellás gofrit eszik.
5107|ringatni egy újszülöttet;gyönyörködni a babájukban;egymás mellett aludni|göndör haj;újszülött;jegygyűrű|Mit csinál a férfi és a nő?|Egy újszülött babát ringatnak.
5109|egy tálcát vinni;bekopogni az ajtón;elvenni egy muffint|ajtó;növény;muffinok;asztal|Mit visz a nő?|Egy tálca muffint visz.
5113|a plakátra mutatni;feltartani a hüvelykujját;megérinteni a vállát|plakát;paradicsomok;tej;hal|Mire mutat a nő?|A plakátra mutat.
5114|belenézni egy távcsőbe;jegyzeteket írni;felröppenni|az ég;flamingók;tó;nádszálak|Mit csinálnak a flamingók?|Felröppennek a tó fölött.
5115|egy rovart tanulmányozni;egy nagyítót használni;rajzolni egy jegyzetfüzetbe|sapka;virágok;nagyító;farönk|Mit csinál a fiatal nő?|Egy kis rovart tanulmányoz.
5116|elhúzni a függönyöket;kinyitni az erkélyajtót;kimenni az erkélyre|az ég;függöny;erkély;a padló|Mit nyit ki a fiatalember?|Kinyitja az erkélyajtót.
5118|kinyitni az ablakot;mosolyogni a kamerába;állni az erkélyen|az ég;napfény;háztetők;férfi|Hol áll a férfi?|Az erkélyen áll.
5119|mosolyogni a kamerába;lengetni a karjait;lassan kinyílni|bejárat;kapu;emberek;piros ruha|Mit csinál a piros ruhás nő?|Mosolyog a kamerába.
5120|a beteg fölé hajolni;kijelezni a pulzust;egy darab gézt tartani|műtőlámpa;sebész;beteg|Mit csinál a középső sebész?|A beteg fölé hajol.
5121|kivenni egy tálca muffint;kihúzni egy sütőtepsit;frissen sült cipókat vinni|cipók;sütő;pék|Mit vesz ki a nő?|Egy tálca muffint vesz ki.
5122|megmászni egy falat;nehéz súlyokat emelni;átlépni a célvonalat|az ég;fák;futó;futópálya|Mit emel a férfi?|Nehéz súlyokat emel.
5123|túlcsordulni a kávétól;berohanni a fürdőszobába;a fejét fogni|zuhanyfüggöny;kapucnis pulóver;hab;fürdőkád|Mit csinál a férfi?|Két kézzel fogja a fejét.
5124|egyenesen előre bámulni;tapsolni a korlátok mögött;egy sárga mellényt viselni|erkély;nézők;macskakövek|Mit csinálnak a nézők?|Tapsolnak a korlátok mögött.
5125|leesni a székéről;magasra emelni egy sisakot;tapsolni|sisak;emberek;férfi;matrac|Mit tart a nő?|Egy sisakot tart a feje fölött.
5127|bepakolni a ruháit;ráülni a bőröndre;tele lenni ruhákkal|plakátok;ajtó;ruhák;bőrönd|Mit csinál a nő?|Próbálja becsukni a bőröndöt.
5128|fogni a térdét;nekidőlni a falnak;ülni a padlón|ablak;növény;szekrény;kanapé|Mit csinál a férfi?|A padlón ül.
5130|megérinteni a teherautót;kinézni az ablakon;egy piros sárkányt eregetni|az ég;sárkány;a nap;férfi|Mit csinál a fiatalember?|Egy piros sárkányt ereget.
5132|megolvadni a forró serpenyőben;tésztát önteni egy merőkanálból;felemelni a serpenyőt|sapka;merőkanál;serpenyő;tészta|Mit önt a férfi?|A palacsintatésztát önti a serpenyőbe.
5133|lefilmezni magát nevetés közben;egy mintás pólót viselni;terpeszugrást csinálni|fenyőfa;lámpaoszlop;pad;fű|Mit csinál a fehér ruhás férfi?|Nevet a kamerába.
5134|etetni a babát;egy könyvet olvasni;kanálból enni|férfi;nő;torony;szőnyeg|Mit csinál az anya?|Eteti a babát.
5135|kihajolni az ablakon;bepréselődni egy szűk helyre;feltartani egy újságot|napellenző;újság;hátsó lámpa;csatornafedél|Mit csinál a nő?|Beparkol egy szűk helyre.
5137|két kézzel gesztikulálni;az ülő képviselők között állni;a szónoki emelvényről beszélni|erkély;lépcsők;szónoki emelvény|Mi történik a szónoki emelvénynél?|Egy férfi beszél a szónoki emelvényről.
5138|az ablak mellett ülni;egy narancssárga sapkát viselni;segíteni a bőrönddel|vonat;sapka;jegy;bőrönd|Hol ül a nő?|Az ablak mellett ül.
5139|kinyitni az útlevelét;becsukni a szemét;mosolyogni a kamerába|lámpák;útlevél;hátizsák;asztal|Mit tart a férfi?|Egy útlevelet tart.
5140|lepecsételni egy útlevelet;tányérsapkát viselni;büszkén mutogatni az útlevelét|tányérsapka;sor;gumibélyegző;útlevél|Mit csinál a tiszt?|Lepecsételi az utas útlevelét.
5141|kinyitni a száját;megmutatni az izmait;átadni neki egy kártyát|plakát;szekrény;orvos;ágy|Mit nyit ki a fiatalember?|Kinyitja a száját.
5142|elsimítani egy zászlót;átszaladni a gyepen;integetni a kertjükből|zászlófüzér;szomszédok;kantáros nadrág;léckerítés|Mit csinál a kislány?|Átszalad a gyepen.
5144|a vállán sírni;egy bézs öltönyt viselni;az emlékmű fölött szárnyalni|galambok;emlékmű;iskolás lányok;fonott kosár|Mit csinálnak a fehér galambok?|Az emlékmű fölött szárnyalnak.
5145|megnyomni egy gombot;ránézni az órájára;kék ajtókkal rendelkezni|épület;villamos;dzseki;farmer|Mit csinál a fiatalember?|Ránéz az órájára.
5146|meghámozni egy piros almát;az ölében pihenni;a térdén túl lelógni|muskátlik;kötény;tál;héjcsík|Mit csinál a nő?|Egy almát hámoz egyetlen hosszú csíkban.
5147|egy fehér szatyrot vinni;nézni az ételt;megtölteni az egész utcát|az ég;képernyő;emberek|Mit csinálnak az emberek?|Átkelnek egy forgalmas utcán.
5148|elrepülni;inni egy üvegből;átmenni az utcán|az ég;közlekedési lámpa;utca|Mit csinálnak a madarak?|A madarak elrepülnek.
5150|odanyújtani egy receptet;átkutatni a polcokat;világítani az ajtó fölött|polcok;gyógyszerész;recept;pult|Mit csinál a gyógyszerész?|A gyógyszerész a receptjét olvassa.
5151|feltartani egy képet;egy kalapácsot használni;egy fehér házat ábrázolni|szemüveg;hegyek;ház;keret|Mit csinál az idős férfi?|Felakaszt egy új képet.
5152|letenni egy fehér párnát;párnákat dobálni az ágyra;belezuhanni a párnákba|függöny;fal;nő;párnák|Mit csinál a nő?|Párnákat dobál az ágyra.
5153|hosszú sötét hajat viselni;egy kék rövidnadrágot viselni;egy fehér inget viselni|az ég;fák;férfi;ágyás|Mit csinál a férfi?|Kis növényeket ültet az ágyásba.
5154|elültetni egy apró palántát;gyönyörködni a növényekben;hosszú kiöntővel rendelkezni|a mennyezet;páfrány;férfi;szobanövények|Mit csinál a férfi?|Egy apró palántát locsol.
5155|letenni egy nagy tányért;széttárni a karját;tésztát tenni a tányérra|ablak;virágok;tányérok;villa|Mit csinál a kék ruhás nő?|Letesz egy nagy tányért az asztalra.
5156|elcselezni egy védő mellett;térdelni a pályán;megölelni a gólszerzőt|kapu;futballista;nézők;fehér vonal|Mit csinál a gólszerző?|Térdel a pályán.
5157|dekázni egy focilabdával;kisietni az utcára;kétrét görnyedni a nevetéstől|domb;parkoló autó;focilabda;macskakövek|Mit csinálnak a férfiak?|Fociznak egy macskaköves utcán.
5158|bedugni egy kábelt;világítani a feje fölött;ámulva bámulni|monitor;hangszóró;redőny;kábelek|Mit csinál a fiatalember?|Kábeleket csatlakoztat a számítógépéhez.
5161|nekitámaszkodni egy korlátnak;szétrebbenni a téren;megkóstolni egy sült gombócot|katedrális;galambok;hátizsák;macskakövek|Mit eszik a fiatalember?|Sült gombócokat eszik.
5162|széttárni a karját;felrepülni az égbe;villával enni|hegyek;fák;tó;férfi|Mit csinál az asztalnál?|Villával eszik.
5164|elsimítani egy plakátot;kampánytáblákat feltartani;boldogan vigyorogni|reflektorok;képernyő;szónoki pult;közönség|Mit csinál az ecsettel?|Elsimít egy kampányplakátot.
5165|kihalászni egy palackot;szürke füstöt ontani;kétségbeesetten sírni|kémény;cső;nő;műanyag|Mi úszik a folyón?|Műanyag szemét úszik a folyón.
5167|megérinteni a csempés falat;cukorral meghintve lenni;ízlelgetni egy szelet süteményt|ablak;csempék;ing;kéz|Mit érint meg a férfi?|Megérinti a csempés falat.
5168|kis süteményeket sütni;enni egy kis süteményt;egy nagy tálcát vinni|kislány;emberek;nő;adag|Mit csinál a kislány?|Egy kis süteményt eszik.
5169|feladni egy képeslapot;kiválasztani néhány képeslapot;élénksárgára festettnek lenni|az ég;szemüveg;kardigán;postaláda|Mit csinál a postaládánál?|Felad egy képeslapot.
5170|kézbesíteni egy csomagot;kotorászni a táskájában;meglocsolni az előkertet|sapka;csomag;téglafal;kerékpár|Mit csinál a postás?|Kézbesít egy csomagot.
5171|beletenni némi zöldséget;rátenni a fedőt;megkavarni a levest|kötény;leves;fazék|Mit tesz bele a fazékba?|Némi zöldséget tesz bele.
5172|beleöklözni a tésztába;verni egy dobot;összezúzni a fűszereket|tészta;kés;steak;szárított chilik|Mit csinál a farmerruhás nő?|Egy dobot ver.
5173|megtölteni egy palackot;megérinteni a vizet;lezúdulni a sziklákról|vízesés;hátizsák;esőkabát;sziklák|Mit visel a nő?|Egy piros esőkabátot visel.
5174|magasra emelni a kancsót;megtapsolni a fiatal nőt;nyírt fehér szakállat viselni|kancsó;mintás ruha;rizs;saláta|Mit csinál a fiatal nő?|Narancslevet tölt egy pohárba.
5175|a feje fölé emelni a kancsót;letenni egy karaffát;megtelni teával|bajusz;fémkancsó;kötény;karaffa|Mit csinál a pincér?|Teát tölt egy kis pohárba.
5176|megtelni kávéval;a palacsintatésztát tartalmazni;toronyba rakva állni|bögre;kávé;kávéskanna|Mi kerül a bögrébe?|Fekete kávé kerül a bögrébe.
5177|teát tölteni egy csészébe;vörös fonatokat viselni;sorban állni|teáskanna;csésze;nő;asztal|Mit tölt a csészébe?|Teát tölt a csészébe.
5178|kinyitni a sütő ajtaját;betolni a tepsit;a pulton pihenni|fejkendő;mikrohullámú sütő;sütőrács;kekszek|Mit visel a fején?|Egy sötétkék fejkendőt visel.
5179|a sütő felé nyúlni;egy tepsit vinni;belül narancssárgán izzani|szekrény;sütő;fejkendő;tészta|Merre nyúl a kezével?|A forró sütő felé nyúl.
5181|kiszállni egy limuzinból;aláírni egy hivatalos dokumentumot;diadalmasan a magasba emelni a karjait|aláírás;töltőtoll;zászló;íróasztal|Mit ír alá a nő?|Egy hivatalos dokumentumot ír alá.
5182|felvinni az utolsó ecsetvonásokat;megtörölni a homlokát;lemászni a létráról|falfestmény;kantáros nadrág;létra;a járda|Mit néz a nő?|Felnéz a falfestményére.
5184|fél térdre ereszkedni;odanyújtani egy eljegyzési gyűrűt;sírva fakadni|torony;harmonika;gyűrűsdoboz;ruha|Mit tart a férfi?|Egy eljegyzési gyűrűt tart.
5185|szorongatni egy papírzacskót;megvédeni őt az esőtől;átkarolni őt|esernyő;bagettek;papírzacskó;esőkabát|Mit tart az idős férfi?|Egy zacskó bagettet szorongat.
5187|húzni egy vastag kötelet;összeszorítani a fogát;üresen állni a réten|az ég;póló;szekér;fű|Mit csinál a fiú?|Egy vastag kötelet húz.
5188|küszködni egy horgászbottal;egy merítőhálót vinni;a stégen landolni|az ég;merítőháló;gumicsizma;stég|Mit fogott a szakállas férfi?|Egy zöld gumicsizmát fogott.
5189|kinyújtani a kezét;kinyitni egy piros esernyőt;mosolyogni a kamerába|sapka;esernyő;kabát;utca|Mit tart az idős férfi?|Egy piros esernyőt tart.
5190|felhúzni a kapucniját;szélesre tárni a karjait;mosolyogni a kamerába|az ég;esőkabát;a tenger;csizmák|Mit csinál a tenger mellett?|Szélesre tárja a karjait.
5191|felkúszni a rúdra;lobogni a szélben;felemelni az öklét|zászló;az ég;kabát;hó|Mit csinálnak az emberek?|Zászlót vonnak fel a hóban.
5192|lobogni a szélben;sapka nélkül menni;a láthatáron állni|zászló;zászlórúd;kunyhó;a láthatár|Mit csinálnak az emberek?|Felvonnak egy piros zászlót.
5193|megvakarni a viszkető karját;megnyomni egy tubus krémet;az ölében pihenni|kiütés;tubus;kertészkesztyűk;bokrok|Mit csinál a sötét hajú nő?|Krémet ken a kiütésre.
5194|egy regényt olvasni;lapozni egyet;becsukni a könyvét|regény;kanapé;ablak;függönyök|Mit csinál a nő?|Egy regényt olvas.
5195|egy padon ülni;felemelni egy nagy könyvet;a pad mögött állni|pad;madár;sapka;fák|Mit csinál a férfi?|Egy padon ül.
5196|megkapaszkodni egy fémrúdban;elfojtani egy ásítást;pislákolni a sötétben|konty;szemüveg;pad;galamb|Hogyan hordja a haját a nő?|Kontyban hordja a haját.
5197|felmászni az íróasztalára;dühösen meredni a kollégáira;letépni a nyakkendőjét|forgószék;gyűrűs iratrendezők;asztali telefon;mennyezeti lámpák|Mit csinál a dühös nő?|Dühösen mered a kollégáira.
5199|egy kézzel írt receptet követni;koktélparadicsomot szeletelni;olívaolajat csorgatni|fejkendő;kötény;salátástál;piros paprika|Mit követ a nő?|Egy kézzel írt receptet követ.
5200|egy takaró alatt ülni;kiugrani egy székből;fekvőtámaszokat csinálni|növény;ajtó;szék;csésze|Mit csinálnak a fiatalok?|Összecsapják a tenyerüket.
5201|megérinteni a vizet;elsétálni;visszatükrözni az eget|az ég;nő;hegy;víz|Mit érint meg a nő?|Megérinti a vizet.
5202|kinyitni a hűtőt;mosolyogni a kamerába;ételt tenni a polcokra|nő;tej;gyümölcslé;hűtő|Mit nyit ki a nő?|Kinyitja a hűtőt.
5203|elöl menni befelé;egy letakart tortát vinni;egy epres tetejű tortát tartani|csokor;fogas;szökőkút;pezsgőspoharak|Mit csinálnak a rokonok?|Koccintásra emelik a poharukat.
5204|letépni a tapétát a falról;egy kalapácsot használni;kifesteni a falat|növény;szerszámöv;festőhenger;csempék|Mit tart a nő?|Egy festőhengert tart.
5205|esküt tenni;egy bőrkötésű könyvet tartani;szélesre tárni a karjait|kupola;oszlopok;vállszalag;fotósok|Miért emeli fel a kezét a nő?|Esküt tesz.
5206|jegyzeteket tűzni a táblára;lapozni;a táblát nézni|zsineg;szemüveg;számítógép;könyv|Mi van a nő szájában?|Egy toll van a szájában.
5207|elterülni egy fapadon;nagy kortyokban vizet inni egy palackból;túrabotokra támaszkodni|csúcsok;rét;pad;vizespalack|Mit tart a szakállas férfi?|Két túrabotot tart.
5208|ámulva bámulni;egy műanyag asztalon landolni;felemelni egy tajine fedelét|a városi látkép;gyertya;öltöny;steak|Mit csinál a férfi?|Ámulva bámul.
5209|lerogyni egy kanapéra;egy jeges italt szürcsölni;hanyatt feküdni a fűben|a nap;a tenger;függőágy;homok|Mit csinál a nő a naplementében?|Egy függőágyban heverészik.
5210|kiterjeszteni a szárnyait;szorongatni egy szendvicset;elfoglalni a pokrócot|tavacska;pad;liba;szendvicsek|Mit csinálnak a barátok?|Hátrálnak a liba elől.
5211|behúzni egy bőröndöt;rávetődni az ágyára;a zárban lógni|könyvespolc;kanapé;szőnyeg;bőrönd|Mit húz maga után a lány?|Egy matricákkal borított bőröndöt húz.
5212|egy nagy táskát vinni;egy táblát tartani;egy sapkát tartani|tető;óra;vonat;tábla|Mit visz a fiatal nő?|Egy nagy táskát visz.
5213|feltartani egy kartontáblát;valakinek a karjaiba ugrani;egy baseballsapkát viselni|üvegtető;vasút;csokor;peron|Mit csinál a fiú?|Egy kartontáblát tart a feje fölött.
5214|rollerezni;egy tevén ülni;mosolyogni a kamerába|a nap;nő;tevék;sivatag|Mit csinál a sivatagban?|Egy tevén ül.
5216|megérinteni egy omladozó falat;egy virágárus stand mögött állni;szélesre tárni a karjait|villanyvezetékek;lámpás;omladozó fal;filmes fényképezőgép|Mit csinál a tetőn?|Szélesre tárja a karjait.
5217|megérinteni a tetőt;egy sárga mellényt viselni;mosolyogni a kamerába|az ég;torony;mellény;tető|Mit visel a férfi?|Egy sárga mellényt visel.
5218|kinyitni egy ajtót;bemenni egy nagy szobába;felnézni a mennyezetre|a mennyezet;ablakok;lány;a padló|Mit csinál a lány?|Felnéz a mennyezetre.
5219|kavarni a tésztát;izgatottan integetni a kezével;chipset nassolni|a mennyezet;póló;kapucnis pulóver;chips|Mit csinál a göndör hajú férfi?|Fakanállal kavarja a tésztát.
5222|végigkövetni egy útvonalat;elfutni egy szikla mellett;felmászni a kőlépcsőn|az ég;hátizsák;lépcsők;fű|Mire mászik fel a túrázó?|Egy hosszú kőlépcsőn mászik fel.
"""
src = json.load(open(f'{H}/source.json'))
d = {}
for line in rows.strip().splitlines():
    i, p, n, q, a = line.split('|')
    d[i] = {"phrases": p.split(';'), "nouns": n.split(';'), "question": q, "answer": a}
out = {i: d[i] for i in src}
json.dump(out, open(f'{H}/hu.json', 'w'), ensure_ascii=False, indent=1)
