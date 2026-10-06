import json,os
H=os.path.dirname(os.path.abspath(__file__))
T="""209|benézni a dobozba;bedugni a mancsát a dobozba;megszaglászni a kamerát|macska;doboz;kamera|Mit csinál a macska?|A macska kíváncsian benéz a dobozba.|kíváncsian benéz a dobozba
142|a trónon ülni;sárga sálat viselni;fekete bőrdzsekit viselni|ég;vár;híd;víz|Mit néznek meg ők ketten?|Egy nagy várat néznek meg.|egy nagy várat néznek meg
163|segíteni a fiúnak;leejteni az ételét;a magasba nyújtani a karját|lámpa;evőpálcikák;kéz|Mivel eszik a fiú?|Evőpálcikával eszik.|evőpálcikával eszik
429|a fűben landolni;felemelni mindkét kezét;lila dzsekit viselni|ég;sisak;dzseki;fű|Mit csinál a rózsaszínbe öltözött nő?|A fűben landol.|a fűben landol
531|egy buliban táncolni;átszaladni a réten;repülni a levegőben|léggömb;fa;emberek;kutya|Mit csinálnak az emberek?|Egy buliban táncolnak.|egy buliban táncolnak
4658|egy régi autót vezetni;végigsétálni az utcán;sötét napszemüveget viselni|ég;tenger;nő;kormány|Mit csinál a nő?|A tenger mentén autózik.|a tenger mentén autózik
852|ételes tányérokat hozni;fehér nyakláncot viselni;átszaladni az éttermen|lámpa;pincér;asztal;szék|Mit csinál a pincér?|Az asztalhoz viszi az ételt.|az asztalhoz viszi az ételt
646|lila kesztyűt viselni;kijönni az üvegből;nagyra kinyitni a száját|kesztyű;szemüveg;köpeny;asztal|Mi van a nő kezén?|Lila kesztyűt visel.|lila kesztyűt visel
5580|begombolni a férfi dzsekijét;egy ládán állni;tálcát tartani|nő;dzseki;kutya;lámpa|Mit csinál a nő?|Begombolja a férfi dzsekijét.|begombolja a férfi dzsekijét
844|felemelni mindkét karját;a völgybe mutatni;narancssárga dzsekit viselni|ég;völgy;folyó;nő|Mit néznek?|Egy zöld völgyet néznek.|egy zöld völgyet néznek
5468|szelfit készíteni;hosszú szakállat viselni;nagy szemeket mereszteni|tábla;ég;nő;férfi|Mit csinál a nő?|Szelfit készít.|szelfit készít
5215|a többiek előtt kerekezni;átkerekezni egy hídon;színes mezt viselni|hegy;sisak;kerékpár;út|Mit csinál a nő?|Gyorsan kerékpározik.|gyorsan kerékpározik
694|szeletekre vágni egy paradicsomot;felmutatni egy szeletet;a vágódeszkán feküdni|dzseki;kés;paradicsom;vágódeszka|Mit csinál a férfi?|Szeletekre vág egy paradicsomot.|szeletekre vág egy paradicsomot
757|átadni neki egy dobozt;kinyitni a dobozt;egy kis kutyát tartani|ég;kutya;doboz;asztal|Mit tart a nő?|Egy kis kutyát tart.|egy kis kutyát tart
5456|kinyitni az útlevelét;átmenni az ellenőrzésen;egyenruhát viselni|fák;szemüveg;kezek;útlevél|Mit tart a fiatalember?|Az útlevelét tartja.|az útlevelét tartja
118|fúrógépet használni;szakállat viselni;hosszú hajat hordani|ég;férfi;nő;madár|Mit csinálnak ők ketten?|Egy nagy faládát szerelnek össze.|egy nagy faládát szerelnek össze
706|piros dzsekit viselni;zöld dzsekit viselni;elkapni egy nagy hópelyhet|hó;kesztyű;nő;férfi|Mit csinálnak ők ketten?|A hóban fekszenek.|a hóban fekszenek
395|egy dobozt cipelni;a kulcsot tartani;csíkos pólót viselni|ház;ég;fű;ösvény|Mit visz be a nő a házba?|Egy dobozt visz be a házba.|egy dobozt visz be a házba
4243|piros kötényt viselni;virslit grillezni;kártyával fizetni|macska;kutya;hotdog;virslik|Mit csinál a macska?|Hotdogot készít.|hotdogot készít
617|lila görkorcsolyát viselni;végiggurulni az ösvényen;egy padon ülni|görkorcsolya;ital;férfi;pad|Mit csinál a nő?|Lila görkorcsolyán gurul.|lila görkorcsolyán gurul
10|egy nagy levelet tartani;világoszölden világítani;a levélre esni|szemüveg;ing;levél;asztal|Hová esik a víz?|A víz a levélre esik.|a levélre esik
792|egy sárga fogkefét tartani;kijönni a tubusból;fogat mosni|haj;orr;fogkrém;fogkefe|Mit csinál a nő?|Fogkrémet nyom a fogkeféjére.|fogkrémet nyom a fogkeféjére
7193|egy piros traktort vezetni;fehér ruhát viselni;a traktor után futni|ég;nagyi;traktor;kutya|Mit csinál a nagyi?|Egy piros traktort vezet.|egy piros traktort vezet
365|fakanalat tartani;kék pólót viselni;a hűtőszekrény tetején feküdni|macska;fejhallgató;fakanál;almák|Mit visel a nő?|Nagy fehér fejhallgatót visel.|nagy fehér fejhallgatót visel
5616|a magasba emelni a karját;erősen fogni a zsinórokat;repülni az égen|ég;léggömbök;férfi;autó|Mivel van tele az autó?|Az autó tele van léggömbökkel.|tele van léggömbökkel
811|a trófeához futni;a magasba emelni a trófeát;nézni a játékosnőket|lámpák;trófea;asztal;padló|Mit csinálnak a játékosnők?|A magasba emelik a trófeát.|a magasba emelik a trófeát
7053|elmosogatni egy piszkos tányért;eltörölgetni egy tányért;fehér ruhát viselni|tányérok;férfi;nő;mosogató|Mit csinálnak ők ketten?|Elmosogatnak.|elmosogatnak
704|nagyon erősen tüsszenteni;megtörölni az orrát;kosarat vinni|fa;lány;kalap;kosár|Mit csinál a férfi?|Nagyon erősen tüsszent.|nagyon erősen tüsszent
247|leejteni egy piros almát;a kövekre esni;a földre nézni|fiú;alma;fű|Mit csinál a fiú?|Leejt egy piros almát.|leejt egy piros almát
775|sokáig gondolkodni;tapsolni;átsétálni az asztalon|nő;férfi;madár;asztal|Mit csinál a férfi?|A játékon gondolkodik.|a játékon gondolkodik
4710|középen állni;világoszöld dzsekit viselni;szemüveget viselni|fák;kar;férfi|Mit csinálnak ők hárman?|Mozgatják a karjukat.|mozgatják a karjukat
4760|kék dzsekit viselni;színes ruhát viselni;megölelni egymást a víz mellett|ég;dzseki;fagylalt;ruha|Min osztoznak ők ketten?|Egy fagylalton osztoznak.|egy fagylalton osztoznak
5007|keresni a kulcsait;bemenni a házba;elfordulni a zárban|zár;kéz;kulcsok;ajtó|Mit keres a nő?|A kulcsait keresi.|a kulcsait keresi
659|megmosni a férfi haját;a mosdó mögött állni;becsukni a szemét|sampon;flakon;kéz;fal|Mit csinál a nő?|Megmossa a férfi haját.|megmossa a férfi haját
5609|félni az egerektől;a földön ülni;az oldalán feküdni|egér;bögre;szék;ablak|Mitől fél a férfi?|Fél az egértől.|fél az egértől
4055|felemelni a fejét;két dinoszaurusz között ülni;piros szeműnek lenni|kutya;dinoszaurusz;ágy|Hol ül a kutya?|Két dinoszaurusz között ül.|két dinoszaurusz között ül
665|zöld füvet legelni;nagyra tátani a száját;átmenni a réten|birka;kőfal;ég;fű|Mit csinál a birka?|A birka átmegy a réten.|átmegy a réten
518|egy ágon ülni;elfordítani a fejét;átrepülni az erdőn|bagoly;ág;fa|Mit csinál a bagoly?|A bagoly egy ágon ül.|egy ágon ül
332|zöld leveleket enni;lehajtani a fejét;vizet inni|zsiráf;zebra;víz;ég|Mit csinál a zsiráf?|A zsiráf vizet iszik.|vizet iszik
82|egy virágon ülni;átrepülni a réten;bemászni a kaptárba|méh;virág;levél|Mit csinál a méh?|A méh egy virágon ül.|egy virágon ül
38|két pálcával integetni;a férfi felé gurulni;felrepülni az égbe|repülőgép;férfi;torony;ég|Mit csinál a férfi?|A repülőtéren két pálcával integet.|a repülőtéren két pálcával integet
785|felnézni a menetrendre;vonatokat és órákat mutatni;megérkezni a pályaudvarra|menetrend;fiú;pad|Mit csinál a fiú?|A menetrendet olvassa.|a menetrendet olvassa
4058|felnézni a bőröndökre;piros sapkát viselni;sok bőröndöt tolni|férfi;nő;bőröndök;ég|Mit csinál a nő?|Sok bőröndöt tol.|sok bőröndöt tol
7999|felugrani az ágyra;a hátán feküdni;behozni a bőröndöket|kutya;macska;ágy;ablak|Mit csinál a kutya?|Az ágyon fekszik.|az ágyon fekszik
7180|beugrani a medencébe;egy italt tartani;a földön feküdni|bőrönd;pálmafák;ég;pincér|Mit csinál a napszemüveges férfi?|Beugrik a medencébe.|beugrik a medencébe
449|az ujjával felfelé mutatni;mindkét kezét a füléhez tartani;hosszú hajat hordani|fák;férfi;nő;ösvény|Mit csinálnak a férfi és a nő?|Nagyon figyelmesen hallgatnak.|nagyon figyelmesen hallgatnak
4568|kontinensről kontinensre ugrálni;narancssárga dzsekit viselni;szélesre tárni a karját|lány;ég;kontinens;cipő|Mit csinál a narancssárgába öltözött lány?|A világtérképen ugrál.|a világtérképen ugrál
721|hangosan nevetni;kopasznak lenni;felborulni az asztalon|pohár;asztal;nő;fiú|Mi borul fel az asztalon?|Egy pohár borul fel az asztalon.|felborul az asztalon
7059|hotdogot készíteni;a grillnél állni;a zsemlék mellett ülni|kutya;macska;hotdog;zsemlék|Mit csinál a kutya?|A kutya hotdogot készít.|hotdogot készít
5673|a magasba tartani mindkét szelet süteményt;egy üres tányért tartani;az ablaknál állni|lámpa;ablak;férfi;zsemlék|Mit tart a piros ruhás nő?|Mindkét szelet süteményt tartja.|mindkét szelet süteményt tartja
670|bevásárlókocsit tolni;kenyeret és tejet vásárolni;elvenni az érméket|nő;tej;bevásárlókocsi;kenyér|Mit csinál a nő?|Bevásárlókocsit tol.|bevásárlókocsit tol
155|levágni egy darab sajtot;sajtos szendvicset sütni;a földön feküdni|nő;férfi;sajt;kutya|Mit süt a férfi?|Egy sajtos szendvicset süt.|egy sajtos szendvicset süt
5282|gitározni;egy fakanálba énekelni;egy színpadon állni|ég;templom;mikrofon;gitár|Mit csinál az idősebb férfi?|Egy dalt énekel a gitárjával.|egy dalt énekel a gitárjával
602|egy vastag könyvet olvasni;a szája elé tartani a kezét;egy bögréből inni|ablak;lány;könyv;asztal|Mit csinál a lány?|Egy vastag könyvet olvas.|egy vastag könyvet olvas
4827|naplementét festeni;ecsetet tartani;narancssárga festéket használni|felhők;festék;ecset;kéz|Mit csinál az illető?|Az illető naplementét fest.|naplementét fest
7853|rámosolyogni a vázára;egy polcon ülni;ezüstgyűrűket viselni|lámpa;nő;macska;váza|Mi történik a vázával?|A váza gyorsan a magasba nő.|gyorsan a magasba nő
144|elkapni egy piros labdát;repülni a levegőben;átfutni a füvön|labda;felhő;fiú;fű|Mit csinál a fiú?|Elkap egy piros labdát.|elkap egy piros labdát
5012|nevetni a barátnőjével;megcsókolni egy idős nőt;megölelni egy szőke nőt|sapka;sál;pohár;asztal|Mit csinál az idős férfi?|Megcsókol egy idős nőt.|megcsókol egy idős nőt
57|elsőként felmenni;felemelni az egyik ujját;a többiek mögött menni|fal;nő;ülések|Hol ülnek ők hárman?|Egészen hátul ülnek.|egészen hátul ülnek
5382|vitázni egy fiatalemberrel;válaszolni egy idősebb nőnek;a falon lógni|ház;nő;férfi;asztal|Mit csinálnak az emberek?|Az asztalnál ülnek és vitáznak.|az asztalnál ülnek és vitáznak
353|kinyitni az ajtót;az esőben állni;vizet tölteni|vendég;virág;gyertya;ablak|Mit hoz a vendég?|A vendég egy virágot hoz.|egy virágot hoz
5560|megköszönni neki;forró teát inni;a lépcsőn ülni|kutya;autó;hó;lámpaoszlop|Mit iszik a férfi?|Forró teát iszik.|forró teát iszik
5506|labdázni;gördeszkázni;piros sapkát viselni|ég;fal;labda;emberek|Mit csinálnak az emberek?|Táncbulit tartanak az utcán.|táncbulit tartanak az utcán
4603|kerékpározni;fehér sisakot viselni;kitárni a karját|út;ég;sisak;kerékpár|Mit csinál a férfi?|Kerékpárral megy az úton.|kerékpárral megy az úton
122|a padon ülni;egy bevásárlókocsit tartani;a buszmegállóhoz gurulni|buszmegálló;pad;busz;utca|Mit csinálnak az emberek?|A buszmegállóban várnak.|a buszmegállóban várnak
339|lemenni az utcán;egy nagy táskát vinni;a házban maradni|házak;autó;lány;utca|Hová megy a lány?|Lemegy az utcán.|lemegy az utcán
368|átrepülni a hegyek fölött;fekete szakállat viselni;hosszú ősz hajat hordani|helikopter;ház;férfi;láda|Mi repül a hegyek fölött?|Egy piros helikopter repül a hegyek fölött.|a hegyek fölött repül
5062|átsétálni az irodán;egy tabletet tartani;a táblára rajzolni|nő;számítógép;telefon;bögre|Ki rajzol a táblára?|A főnöknő rajzol a táblára.|a táblára rajzol
472|autót javítani;egy szerszámot tartani;a kamerába mosolyogni|autószerelő;autó;szerszám;padló|Mit csinál a férfi?|Egy autót javít.|egy autót javít
680|egy dalt énekelni;a fejhallgatójához nyúlni;a számítógépnél ülni|énekesnő;fejhallgató;mikrofon;férfi|Mit csinál a nő?|Egy mikrofonba énekel.|egy mikrofonba énekel
4941|felmászni egy létrán;a fán ülni;magához szorítani a macskát|tűzoltónő;macska;létra;fa|Mit csinál a tűzoltónő?|Kiment egy macskát a fáról.|kiment egy macskát a fáról
3|a táblára írni;egy bögréből inni;az osztály felé fordulni|tanárnő;bögre;szemüveg;tábla|Mit csinál a tanárnő?|A táblára ír.|a táblára ír
30|lapozni;elaludni a tankönyvön;sok oldalból állni|haj;szemüveg;tankönyv;asztal|Mit csinál a nő?|Egy vastag tankönyvet lapozgat.|egy vastag tankönyvet lapozgat
31|egy fekete hátizsákot tartani;laptopon dolgozni;fordítva hordani a sapkát|lámpák;egyetemisták;sapka;ülések|Hol ülnek az egyetemisták?|Az egyetemen ülnek.|az egyetemen ülnek
100|bekötni a csizmát;négylábúnak lenni;szürke dzsekit viselni|ég;kutya;csizma;víz|Mit visel a nő?|Barna csizmát visel.|barna csizmát visel
288|fehér öltönyt viselni;fehér sportcipőt viselni;szürke pulóvert viselni|fák;nő;férfi;kutya|Mit viselnek ők ketten?|Bő öltönyt viselnek.|bő öltönyt viselnek
242|egy vállfán lógni;körbe-körbe forogni;tapsolni|citromok;férfi;ruha;tükör|Mit csinál a nő?|Egy piros ruhában forog.|egy piros ruhában forog
868|egyre nagyobbá válni;fehér pólót viselni;sötét pólót viselni|hullám;nő;férfi;homok|Mit csinálnak ők ketten?|Elfutnak egy nagy hullám elől.|elfutnak egy nagy hullám elől
4015|átugrani a víz fölött;figyelni a birkákat;magasnak és vékonynak lenni|fa;kutya;part;víz|Mit csinálnak a birkák?|Átugranak a túlsó partra.|átugranak a túlsó partra
291|kitárni a karját;a nő mögött futni;sorban állni|ég;fák;mező;ösvény|Mit csinál a nő?|Átfut a mezőn.|átfut a mezőn
5108|integetni a csónakból;integetni egy házból;a dobok között táncolni|ház;gyerekek;víz;csónak|Mit csinálnak a gyerekek?|Egy házból integetnek.|egy házból integetnek
5660|átmenni az úttesten;megvilágítani a ház falát;elsétálni egy lámpaoszlop mellett|háztömb;fa;kutya;ég|Mit csinál a kutya?|A kutya átmegy az úttesten.|átmegy az úttesten
807|futópadon futni;megnyomni egy gombot;megtörölni a homlokát|futópad;póló;ablakok;haj|Mit csinál az elöl lévő nő?|A futópadon fut.|a futópadon fut
277|előrehajolni;ugrálni a kertben;feltartani mindkét hüvelykujját|póló;lábak;cipő;virágok|Mit csinál a nő?|Sportol.|sportol
571|nagy szemeket mereszteni;felemelni az ujját;a tűzön állni|ablak;asztal;fazék;tűz|Mit főznek?|Krumplit főznek.|krumplit főznek
4365|friss zsemléket kivenni a sütőből;egy gyümölcstortát tartani;piros kötényt viselni|ablak;nő;gyümölcstorta;zsemlék|Mit vesz ki az idős nő a sütőből?|Friss zsemléket vesz ki a sütőből.|friss zsemléket vesz ki a sütőből
121|odaégetni egy palacsintát;konyharuhát tartani;egy tányéron feküdni|férfi;serpenyő;tűz;palacsinta|Mit égetett oda a férfi?|Odaégetett egy palacsintát.|odaégetett egy palacsintát
5069|élvezni egy masszázst;egy fotelben ülni;megmasszírozni a vállát|növények;nő;férfi;fotel|Mit élvez a férfi?|Egy masszázst élvez.|egy masszázst élvez
4788|a fülébe súgni;meghallani egy titkot;a számítógépnél ülni|növény;nő;számítógép;pult|Hogy néznek ki a nők?|A nők nagyon döbbentnek tűnnek.|nagyon döbbentnek tűnnek
5129|kifesteni egy falat;lehúzni a ragasztószalagot;narancssárgává válni|fejhallgató;takarófólia;fal|Mit csinál a férfi?|Narancssárgára festi a falat.|narancssárgára festi a falat
358|beverni egy szöget;kalapácsot tartani;a napon feküdni|fák;kutya;kalapács;madárodú|Mit csinál a férfi a kalapáccsal?|Bever egy szöget.|bever egy szöget
819|esernyőt tartani;beállni az esernyő alá;távol tartani az esőt|ablak;esernyő;utca;nő|Mit tart a nő?|Egy nagy piros esernyőt tart.|egy nagy piros esernyőt tart
741|hajladozni a szélben;átgurulni az úton;rövid szakállat viselni|ég;fa;tenger;út|Mit csinál a fa?|Hajladozik a viharban.|hajladozik a viharban
690|fehér blúzt viselni;kék inget viselni;hosszú hajat hordani|ég;fű;nő;férfi|Hová néznek ők ketten?|Felnéznek a kék égre.|felnéznek a kék égre
225|az íróasztalnál ülni;kék pólót viselni;átsétálni az íróasztalon|könyvek;növény;jegyzetfüzet;íróasztal|Hol ül a nő?|Az íróasztalnál ül.|az íróasztalnál ül
92|feldobni egy nagy takarót;húzni a takarót;szőke hajúnak lenni|ablak;kanapé;takaró;asztal|Mit csinál a nő?|Egy nagy takaró alatt ül.|egy nagy takaró alatt ül
7809|elvenni egy dollárt;kifizetni a süteményt;rámosolyogni a férfira|nő;ital;sütemény;dollárok|Mit vesz el a nő?|Elvesz egy dollárt.|elvesz egy dollárt
731|sok bélyeget tartani;bedobni egy levelet;a postaládán ülni|madár;férfi;nő;bélyegek|Mit csinál a nő?|Bedob egy levelet.|bedob egy levelet
800|a labdával futni;tapsolni;felemelni a kezét|ég;lámpa;labda;fű|Mit csinál a sárgába öltözött férfi?|A labdával fut.|a labdával fut
558|átrepülni a háló fölött;a fűben feküdni;feltartani a labdát|labda;háló;fák;fű|Mit csinálnak az emberek?|Röplabdáznak.|röplabdáznak"""
src=json.load(open(f'{H}/tr/b001/source_de.json'))
out={}
for line in T.split('\n'):
    i,ph,no,q,a,rec=line.split('|'); ph=ph.split(';'); no=no.split(';')
    s=src[i]; assert len(ph)==3 and len(no)==len(s['nouns']),i
    m={p['text']:t for p,t in zip(s['phrases'],ph)}; m.update(zip(s['nouns'],no))
    r=[];extra=0
    for x in s['recall']:
        if x in m: r.append(m[x])
        else: r.append(rec); extra+=1
    assert extra==1,(i,extra)
    out[i]={'phrases':ph,'nouns':no,'question':q,'answer':a,'captions':{},'recall':r}
assert set(out)==set(src)
json.dump(out,open(f'{H}/tr/b001/de/hu.json','w'),ensure_ascii=False,indent=1)
