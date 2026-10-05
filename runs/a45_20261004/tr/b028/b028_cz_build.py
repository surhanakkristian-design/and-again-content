import json, os
H=os.path.dirname(os.path.abspath(__file__))
D="""7323|ustlat postel|skočit na postel|pít z hrnku|okno;muž;kočka;postel|Co dělá žena?|Stele postel.
7324|opalovat se na lehátku|natáčet ho na svůj mobil|sedět na zasněžené římse|mrakodrapy;holub;lehátko;bazének|Co dělá bosý muž?|Naplno si užívá slunce.
7325|mávat kusem naplaveného dřeva|štěkat na vypravěčku|usrkávat z hrnku|naplavené dřevo;deka;táborák;kytara|Co dělá stojící žena?|Vypráví dramatický příběh.
7327|seskočit z vozíku|stát vedle vozíku|štěkat na jeleny|obloha;samec;vozík;jablka|Co dělá jelen?|Seskakuje z vozíku.
7328|běžet se zdviženým ocasem|chodit s holí|běžet v růžovém tričku|ovce;pes;lampa;stromy|Co dělá pes?|Pes běží vedle ovcí.
7329|naklánět se přes bariéru|zubit se na ženu|tleskat páru|pořadatel;pončo;fotograf;reflektory|Co dělá žena?|Naklání se přes bariéru.
7332|přidržovat přední kolo|obsluhovat akumulátorovou vrtačku|viset na montážní lince|šrouby;vrtačka;pneumatiky;sedlo|Co dělá žena?|Obsluhuje akumulátorovou vrtačku.
7334|chytit desku skateboardu|hladit hladkou desku|dřímat pod pracovním stolem|javor;hrnek;pes;piliny|Co dělá žena?|Hladí javorovou desku.
7336|pádlovat přes marínu|balancovat s podnosem se snídaní|naklánět se přes zábradlí|jachta;molo;podnos;pádlo|Co dělá muž ve slunečních brýlích?|Pádluje přes marínu.
7337|nechat ptáka odletět|klečet v trávě|sedět jí na hlavě|pták;bunda;krabice;tráva|Co dělá klečící žena?|Drží v rukou ptáka.
7338|pádlovat podél kanálu|klečet na prkně|pást se v dálce|plameňáci;strážní věž;paddleboard;rákosí|Co dělá žena?|Pádluje přes bažinu.
7339|nést hmyz|přistát u hnízda|strčit hlavu dovnitř|jiřička;hnízdo;střecha;pole|Co dělá jiřička?|Nese hmyz do svého hnízda.
7340|naklánět se přes zábradlí|ukazovat na remorkér|nosit čepici se štítkem|jeřáb;čepice se štítkem;remorkér;termoska|Co dělá žena?|Mluví do vysílačky.
7342|tlačit se na membránu|mít zavřené oči|v šoku si zakrýt ústa|dřevěný rám;membrána;muž;stojací lampa|Co dělá žena?|Tlačí obličej do membrány.
7344|předat obálku|šlapat po chodníku|vejít do otáčivých dveří|kurýr;žluté taxi;obálka;otáčivé dveře|Co dělá žena?|Doručuje muži obálku.
7345|rozpřáhnout ruce doširoka|balancovat na krátkých lyžích|táhnout lyžaře|dřevěná chata;diváci;lano;kůň|Kde je lano uvázané?|Je uvázané kolem jeho pasu.
7347|houpat se na laně|otáčet se pod proudící vodou|stát zapřažený do vozu|mouka;mlýn;kůň;vodní kolo|Co dělá žena?|Houpe se nad vodním kolem.
7348|sjíždět po tlustém laně|chytit západku okenice|sypat mouku do pytle|ozubené kolo;okno;mlynář;mlýnské kameny|Co dělá žena pokrytá moukou?|Sjíždí po tlustém laně.
7349|vést řadu žen|nést jezevčíka|nosit několik zlatých řetízků|vila;jezevčík;milionář;ručník|Co dělá milionář?|Vede řadu žen.
7352|kráčet po mokrém molu|nosit reflexní bundu|nosit oranžovou minisukni|reflektory;letadlo;minisukně;hosté|Co dělá modelka?|Kráčí po mokrém molu.
7359|honit jedoucí vlak|svírat své lyže|vyklánět se ze dveří|pouliční lampa;dřevěná chatka;průvodčí;lyžařská hůlka|Co dělá žena?|Honí jedoucí vlak.
7362|chytit cákanec smetany|olizovat se|šlehat čokoládové těsto|mísa na míchání;bígl;kuchyňská minutka;žloutek|Co dělá bígl?|Chytá cákanec smetany.
7363|držet telefon nahoře|stát na velkém kameni|jíst sendvič|mobilní telefon;obloha;batoh;mapa|Co dělá žena?|Drží telefon nad hlavou.
7364|stát na žebříku|držet žebřík|otáčet se ve vzduchu|skleněná střecha;závěsná plastika;taška na nářadí;žebřík|Co dělá závěsná plastika?|Otáčí se ve vzduchu.
7365|seškrabávat hlínu z auta|tvarovat kus hlíny|fotit v pozadí|hliněný model;otočný stůl;odřezky;stropní světla|Co dělá žena?|Seškrabává hlínu z auta.
7367|našpulit rty|předvádět svou obrovskou ploutev|dřímat na gauči|molinézie;akvárium;naplavené dřevo;síťka na ryby|Co dělá žena?|Špulí rty jako ryba.
7368|políbit ho na tvář|upustit svou velkou tašku|vyskakovat na ně|okno;lampa;taška;pes|Co dělá žena?|Líbá ho na tvář.
7370|pádlovat o život|šklebit se námahou|zřítit se do moře|ledovec;tříšť;helma;kajak|Co dělá muž vepředu?|Pádluje pryč od ledovce.
7372|vytáhnout těžký balík|krčit se vedle lucerny|přidržovat lano zespodu|opice;karimatka;kartonová krabice|Co dělá žena?|Vytahuje těžký balík na verandu.
7373|vtěsnat se do úzké plavební komory|kráčet po nábřeží|mávat obrovské lodi|výletní loď;diváci;zábradlí;kamenná chatka|Co dělá výletní loď?|Vtěsnává se do úzké plavební komory.
7376|plavat v černém neoprenu|kopat dlouhými ploutvemi|pohupovat se na hladině|loď;delfín;potápěč;hejno|Co dělá žena?|Klouže hejnem ryb.
7377|vystoupat po točitém schodišti|natáhnout se nahoru pro rondon|podávat kuchařský rondon|kuchařský rondon;točité schodiště;hrnec na vývar|Co dělá mladý muž?|Stoupá po točitém schodišti.
7378|prázdně hledět před sebe|vzlykat do kabátu|svírat muži paži|vrah;vysoké okno;džbán na vodu;spis|Co dělá žena za ním?|Vzlyká do tmavého kabátu.
7379|rozpřáhnout ruce doširoka|zvednout obě ruce vysoko|svírat kovový hrnek|vypravěč;lucerny;stočené lano;talíře|Co dělá stojící muž?|Rozpřahuje ruce doširoka.
7381|tahat za laso|být vlečen|zářit světlem ohně|sob;plátěný stan;břízy;laso|Co dělá mladá žena?|Táhne soba sněhem.
7382|klečet na ledu|zaklonit hlavu|vystřelit k obloze|plamen;dřevěná chata;plynová láhev;zamrzlé bubliny|Co dělá žena v červeném?|Klečí na tmavém ledu.
7383|natáhnout se pro sklenici|spát na gauči|ležet na zemi|muž;klobouk;podnos;sklenice|Co dělá žena?|Natahuje se pro sklenici vody.
7386|zaclonit si oči|sprintovat ke svému kamarádovi|stát na stráži u dveří|kriminál;dozorce;igelitová taška|Kde stojí strážný?|Stojí ve dveřích kriminálu.
7387|předvést trik s mincí|zaclonit si oči|zaklonit hlavu|vinná réva;kamenná zeď;mince;broskve|Co dělá plešatý muž?|Vytahuje jí minci zpoza ucha.
7389|rozmáchnout se sekerou|viset na háku|stát na dřevě|helma;hák;sekera;dub|Co seká muž?|Seká dřevo sekerou.
7392|naolejovat dřevěný stůl|procházet se po stole|stát v louži|plechovka;rukavice;kočka;židle|Co dělá muž vepředu?|Olejuje dlouhý dřevěný stůl.
7393|nalévat olivový olej|držet kulatý bochník|držet nahoře velký džbán|džbán;osel;chléb;olivy|Co dělá žena?|Nalévá olivový olej na chléb.
7394|zatáhnout za železnou páku|proplout mezerou|natáhnout jednu nohu|padací most;plachetnice;pletená čepice;dlažební kostky|Co dělá žena?|Táhne za železnou páku.
7395|pádlovat na červeném kajaku|pohupovat se v dálce|prorazit otvorem|otvor;maják;helma;pěna|Co dělá žena?|Pádluje úzkým otvorem.
7396|pozorovat z vysoké trávy|otáčet se v mlze|odrážet zářící světla|kolotoč;ruské kolo;liška;louže|Co dělá liška?|Liška pozoruje zářící kolotoč.
7398|zvednout cívku s páskem nad hlavu|obsluhovat lis|převážet vinylové desky|dav;cívka s páskem;dopravníkový pás;vozík|Co dělá žena v rukavicích?|Zvedá cívku s páskem nad hlavu.
7401|dýchat přes masku|postavit se na nohy|držet kyslíkovou masku|vrchol;mraky;kapuce;kyslíková láhev|Co dělá žena ve žlutém?|Přitlačuje mu kyslíkovou masku k obličeji.
7402|sbalit velkou tašku|nést botu|sedět vepředu|písek;zrcadlo;taška;láhev|Co dělá žena?|Balí velkou tašku.
7403|násilím zavřít dveře dodávky|sedět na chladicím boxu|trčet z dodávky|surfová prkna;frisbee;plážový míč;chladicí box|Co dělá muž ve slunečních brýlích?|Násilím zavírá dveře dodávky.
7406|sušit se na slunci|hýbat se ve větru|viset na šňůře na prádlo|obloha;balkon;kalhotky|Co dělají kalhotky?|Suší se na slunci.
7407|zaklonit hlavu|zubit se ze dveří|ležet na nástupišti|průvodčí;velbloudí kabát;kufr;plátěná taška|Co dělá žena?|Objímá muže na nástupišti.
7408|držet psa|stát na stoličce|pracovat za barem|muž;noviny;pes;stolička|Co dělá muž?|Pokládá psa na stoličku.
7409|zvednout kus ledu|mít na sobě horolezecký úvazek|tyčit se v pozadí|ledovec;čelenka;kus ledu;úvazek|Co drží žena?|Drží velký kus ledu.
7410|brodit se do řeky|upravit si plavecké brýle|držet nahoře desky s klipem|tabule;dav;vodotěsný vak;lano|Co dělá bosý muž?|Brodí se do řeky.
7411|vstát ze židle|utěšovat mladou ženu|chytat se za hlavu|hodiny;soudce;notebook;šanon|Co dělá muž v šedém?|Drží se rukama za hlavu.
7412|vyskočit do vzduchu|křičet radostí|sedět v autě|obloha;dům;auta;silnice|Co dělá žena?|Skáče vedle auta.
7415|znovu naplnit smaltovaný hrnek|naklánět se nad novinami|letmo se podívat na hodinky|zákazník;várnice na vodu;slanina;křížovka|Co dělá žena?|Nalévá čaj do smaltovaného hrnku.
7416|hladit draka po nose|nést proutěný košík|tulit se k tváři ženy|drak;jeskyně;proutěný košík;vycházková hůl|Co dělá drak?|Tulí se k tváři ženy.
7419|opepřit těstoviny|vybuchnout smíchy|zvednout obočí|číšník;těstoviny;karafa;ubrus|Co dělá žena?|Opepřuje těstoviny.
7420|ukazovat přes pole|lehnout si do trávy|utíkat před psem|stan;žena;pes;ovce|Co dělá žena?|Ukazuje přes pole.
7421|dupat na zaprášeném pódiu|pohodit dlouhými vlasy|brnkat na akustickou kytaru|reflektor;šunky;účinkující;kytara|Co dělá tanečník?|Dupe na zaprášeném pódiu.
7422|tahat za dřevěný kohoutek|přetékat pěnou|ležet na dlážděné podlaze|sad;sud;hruškové víno;hrušky|Co se děje s dřevěnou kádí?|Přetéká pěnivým hruškovým vínem.
7425|tryskat z ventilu|přetékat surovou ropou|rozlévat se po zemi|ventil;hadice;kbelík;ropa|Co se děje s kovovým kbelíkem?|Přetéká surovou ropou.
7427|točit se ve slunečním světle|rozpřáhnout ruce doširoka|opírat se o zárubeň|obloukové okno;paleta;kolečko;suť|Co dělá žena?|Točí se ve slunečním světle.
7428|dotknout se kusu skály|naklonit se nad skálu|zaclonit si oči|obloha;klobouk;náklaďák;kus skály|Co dělá žena v rukavicích?|Dotýká se kusu skály.
7429|přitlačit přístřešek|natáhnout se po letícím ručníku|nosit džínové šortky|slaměný klobouk;moře;plážový přístřešek;stanové kolíky|Co dělá žena v bílém?|Přitlačuje přístřešek k písku.
7430|vyhodit celého lososa|letět vzduchem|sedět na bílé bedýnce|losos;mourovatá kočka;přepravky;slávky|Co dělá žena s culíkem?|Vyhazuje lososa do vzduchu.
7434|klouzat se bahnem|křičet radostí|roztáhnout ruce doširoka|obloha;rukavice;meta;bahno|Co dělá žena v proužkovaném dresu?|Klouže se bahnem.
7439|prohrábnout oheň|schovat se za polštář|držet stříbrný podnos|krbová římsa;pohrabáč;polena;kleště|Co dělá mladý muž?|Prohrabává oheň pohrabáčem.
7440|hrabat tlapou po autobusu|mávat z okna|pozorovat z dálky|obloha;pletená čepice;lední medvěd;sníh|Co dělá velký lední medvěd?|Kráčí podél autobusu.
7442|jezdit bez sedla|nést bosou jezdkyni|široce se usmívat|útes;plot;poník;řeka|Co dělá mladá žena?|Jede na poníkovi přes řeku.
7444|ležet pod motorkou|dívat se na ni shora|jasně svítit|lampa;nářadí;motorka;pes|Co dělá žena?|Leží pod motorkou.
7449|vyhodit ruce nahoru|udělat bolestnou grimasu|stát frontu na záchod|sprchový závěs;záchod;papírový kelímek;bahno|Co dělá zrzavá žena?|Dělá bolestnou grimasu.
7454|prodírat se sněhem|svírat řídítka|sedět na skále|helma;kamenná chata;svišť;silniční kolo|Co dělá muž v černém?|Prodírá se sněhem.
7472|táhnout úzkou loď|zvednout hrnek|stát v mlze|cihlový most;volavka;úzká loď;naviják|Co táhne muž v kostkované košili?|Táhne úzkou loď po kanálu.
7473|pohybovat rukojetí pumpy|pít z koryta|přetékat vodou|chalupy;pumpa;koryto;kbelík|Co pumpuje žena?|Pumpuje vodu do kbelíku.
7476|tahat za provázky loutky|uklonit se holubovi|zírat na loutku|přihlížející;loutka;holub;drobky|Na co zírá holub?|Holub zírá na loutku.
7478|povalovat se na parapetu|nechat viset přední tlapku|procházet se po parapetu|kočička;parapet;proutěný košík;klubko vlny|Co dělá kočička?|Kočička se prochází po parapetu.
7480|s námahou zavřít dveře|zapřít se nohama|zabouchnout se|stropní světlo;dveře trezoru;diamant;vozík|Co muž s námahou zavírá?|S námahou zavírá dveře trezoru.
7481|pevně se držet lana|držet zapálenou pochodeň|viset v popruhu|střešní okno;hliněný džbán;schůdky;podstavec|Kam opice dávají džbán?|Dávají ho zpátky na podstavec.
7482|spustit dřevěný blok|krčit se za zábradlím|zakrývat si ústa|postroj;balónky;věž;dav|Co dělá žena?|Spouští blok na věž.
7483|dosednout na trávu|rozvířit trávu|projet kolem větrného rukávu|větrný rukáv;ledovec;letadlo;ovce|Co dělá letadlo?|Dosedá na trávu.
7488|naklást vajíčko|být větší než ostatní|lesknout se na slunci|královna;vajíčko;med|Co dělá královna?|Klade vajíčko.
7492|chrlit dešťovou vodu|opírat se o zeď|stát pod igelitovou fólií|déšť;markýza;kola;barel|Co se lije ze střechy?|Z plechové střechy se lije prudký déšť.
7502|oddělit dva boxery|roztáhnout obě paže|nosit hnědé boxerské rukavice|rozhodčí;diváci;lana|Co dělá rozhodčí?|Odděluje dva boxery.
7529|obeplout obrovskou bóji|zvedat spršku vody|pohupovat se na rozbouřeném moři|bóje;plachta;trup;vlny|Co dělá jachta?|Obeplouvá obrovskou bóji.
7738|táhnout saně|mít tmavé vousy|kráčet podél řeky|obloha;mamut;saně;sníh|Co dělá žena?|Táhne saně.
7740|ohlédnout se přes rameno|zkoumat půdu|roztáhnout křídla|stromy;traktor;pluh;jestřáb|Co dělá muž?|Zkoumá hrst půdy.
7741|uskočit překvapením|vběhnout do chodby|nést zabalený dárek|lucerna;slunečnice;župan;dlaždice|Co dělá žena v lila?|Uskakuje překvapením.
7742|viset na žlutém chytu|nevěřícně se chytit za hlavu|dřepět na modré žíněnce|střešní okno;cop;lezecká stěna;dopadová žíněnka|Co dělá lezkyně?|Visí na žlutém chytu.
7743|nést bílé surfové prkno|přidržovat si kuchařskou čepici|zapínat si krémové sako|racek;pouliční lampa;surfové prkno;spadané listí|Co dělá kuchařka?|Přidržuje si kuchařskou čepici.
7746|mít na sobě bílé šaty|mít na sobě sako|viset na stěně|lampa;okno;růže;dort|Co krájejí?|Krájejí bílý dort.
7747|mít na sobě hnědou bundu|mít na sobě tmavě modrou bundu|mít na sobě bílé boty|obloha;domy;loď;voda|Mohou se jejich ruce dotknout?|Ne, jsou od sebe příliš daleko.
7749|házet barvu na plátno|stát na štaflích|zaklonit hlavu|plátno;štafle;plechovka barvy;lampa|Co dělá žena vepředu?|Hází barvu na plátno.
7750|hodit starou pneumatiku|držet nahoře ceduli|nasadit kolo|obloha;žena;kolo;auto|Co dělá žena vepředu?|Mění kolo.
7752|skočit mu do náruče|tlačit vozíky|držet květiny|strom;kufr;šálky;kabát|Co dělá žena?|Skáče mu do náruče.
7753|dávat jídlo na talíř|krájet zelenou zeleninu|tlačit na dveře|žena;pánev;utěrka;lampa|Co dělá žena?|Dává jídlo na talíř.
7754|hrát na kytaru|dát peníze do pouzdra|sedět vedle pouzdra|kytara;pes;kolo;obloha|Co dělá muž?|Hraje na kytaru.
7755|skicovat do plánů|mít na sobě lila kardigan|mít na sobě džínovou košili|pokojová rostlina;sako;džbán;technický výkres|Co dělá žena v modrém?|Skicuje do stavebních plánů.
7757|kropit rajčata|držet nahoře zralá rajčata|proplout kolem zahrady|výletní loď;rajčata;lehátko;konev|Co dělá muž?|Kropí rajčata hadicí."""
src=json.load(open(f'{H}/source.json'))
out={}
rows={l.split('|')[0]:l.split('|') for l in D.strip().split('\n')}
for k in src:
    r=rows[k]; assert len(r)==7,k
    out[k]={"phrases":r[1:4],"nouns":r[4].split(';'),"question":r[5],"answer":r[6]}
json.dump(out,open(f'{H}/cz.json','w'),ensure_ascii=False,indent=1)
