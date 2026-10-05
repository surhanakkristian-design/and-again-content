import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = 'cz'
DATA = """
52 # nést tašky | fotit | stát na skále # asistent | fotoaparát | taška | šaty # Kdo nese tašky? # Tašky nese asistent.
53 # přeskakovat překážku | skákat do písku | vrhat těžkou kouli # překážky | výsledková tabule | mraky | běžecká dráha # Co dělá žena v zeleném? # Přeskakuje překážku.
55 # přihazovat s číslem devatenáct | objímat dřevěnou cedulku | mít na sobě pruhovaný top # stojací hodiny | bekovka | cedulka | okno # Co dělá zrzavá žena? # Přihazuje v aukci.
56 # skákat do listí | chytat list | držet hrábě # listí | hrábě | kabát | stromy # Co dělá žena? # Skáče do listí.
58 # balit si oblečení | nasadit si batoh | jít nahoru po schodech # dívka | oblečení | láhev | batoh # Co dělá dívka? # Balí si oblečení do batohu.
61 # mít na sobě dlouhou šálu | sedět na lavičce | pozorovat lidi # lampa | muž | lavička | kachna # Co dělají ti dva lidé? # Jdou pozpátku.
65 # skládat zeleninu | ochutnávat pečený brambor | ležet na podlahových prknech # husky | chňapka | kostkovaná košile | plech na pečení # Co dělá muž? # Ochutnává pečený brambor.
66 # vytahovat chléb | mít krátké vousy | ležet u okna # okno | muž | žena | chléb # Co dělá žena? # Peče v kuchyni chléb.
67 # loupat banán | ukazovat na banán | jíst banán # muž | banán | papoušek # Co dělá muž? # Jí banán.
69 # zvedat těžkou činku | mít husté vousy | narovnat nohy # svah | cop | vousy | činka # Co dělá blondýnka? # Zvedá těžkou činku.
71 # klepat na kmen | držet se kmene | odlupovat březovou kůru # kůra | muž | žena | datel # Co dělá žena? # Odlupuje kůru z břízy.
74 # držet pálku | letět vzduchem | sedět na trávě # strom | pálka | tričko | tráva # Co drží žena? # Drží pálku.
75 # mávat kožnatými křídly | rojit se po obloze | odrážet západ slunce # netopýr | obloha | stromy | jezero # Co dělá velký netopýr? # Mává křídly nad jezerem.
76 # držet baterku | mít na sobě šedou čepici | vkládat nové baterie # baterie | šálek | čepice | žena # Co drží žena? # Drží baterku.
78 # držet žlutý kyblík | kopat lopatkou | být z písku # kyblík | lopatka | hrad z písku | obloha # Co stavějí? # Stavějí na pláži hrad z písku.
79 # kráčet v řece | stát na dvou nohách | letět nad stromy # medvěd | pták | stromy | řeka # Co dělá medvěd? # Kráčí v řece.
80 # česat si dlouhé vousy | držet telefon | mít na sobě bílou košili # vousy | hřeben | čaj | květiny # Co dělá muž v bílém? # Češe si dlouhé vousy.
81 # tančit v šatech | mít na sobě modrou košili | svítit nad mořem # slunce | moře | žena | muž # Co dělá žena? # Tančí v bílých šatech.
83 # nalévat pivo | mít dlouhé vlasy | spát pod stolem # pivo | chléb | pes | lampy # Co dělá muž? # Nalévá pivo do sklenice.
84 # přidržovat si kalhoty | nasadit si pásek | šťastně tančit # košile | pásek | kalhoty | židle # Co má muž na sobě? # Má na sobě hnědý pásek.
85 # padat do sena | sebevědomě si založit ruce | šibalsky se zubit # cypřiše | drdol | lacláče | balík sena # Co dělá muž? # Padá do sena.
86 # rozkládat dlouhý účet | odpočítávat bankovky | mít na sobě černou zástěru # číšník | účet | bankovky | karafa # Co dělá žena? # Rozkládá dlouhý účet.
87 # zpívat píseň | sedět na větvi | letět nad trávou # pták | větev | tráva | obloha # Co dělá pták? # Pták zpívá na větvi.
88 # dívat se do kamery | otáčet hlavu | mít dlouhé uši # pes | obloha | dům # Co dělá pes? # Pes se dívá do kamery.
89 # skákat z věže | sedět pod jinou kočkou | viset ze stropu # kočka | provaz | dveře | zrcadlo # Co dělá černá kočka? # Skáče z věže.
90 # stát na dvou nohách | tančit ve vodě | ukazovat růžový jazyk # štěně | voda | lahve # Co dělá štěně? # Tančí ve vodě.
91 # obviňovat chlapce | zkřížit si ruce | olizovat si tlapku # zástěra | otisky tlapek | mikina s kapucí | sluchátka # Co dělá žena? # Obviňuje chlapce z nepořádku.
96 # skenovat palubní vstupenku | vítat cestující na palubě | listovat časopisem # časopis | závěsy | ulička # Co dělá žena ve žlutém? # Nastupuje do letadla.
97 # nalévat horkou vodu | vřít v hrnci | hořet pod hrncem # dívka | hrnec | oheň | hora # Co dělá dívka? # Vaří vodu v hrnci.
99 # číst zelenou knihu | držet velký šálek | spát na dece # okno | kniha | kočka | deka # Co dělá zrzavá žena? # Čte zelenou knihu.
101 # hrát si s klíči | vypadat velmi znuděně | ukazovat čas # hodiny | klíče | kniha | židle # Jak žena vypadá? # Vypadá velmi znuděně.
103 # rozvalit se přes židle | točit se na pultu | viset nad bílou tabulí # hodiny | bílá tabule | pračky | sandály # Kde leží muž? # Leží přes židle v prádelně.
104 # plavat ke dnu | zvednout kámen | držet kámen nahoře # maska | kámen | dno # Co dělá žena? # Bere kámen ze dna.
106 # mířit na terč | sloužit jako terč | pozorovat mladého lukostřelce # luk | balík sena | šíp | lukostřelec # Co dělá lukostřelec? # Míří na balík sena.
107 # brát modrou misku | pít z misky | ležet na stole # brýle | miska | lžíce | stůl # Co dělá chlapec? # Pije mléko z misky.
110 # nést velkou krabici | dotýkat se kočičích zad | sedět na krabici # police | kočka | žena | krabice # Co dělá žena? # Balí velkou krabici.
111 # bít do velkého pytle | držet dvě černé lapy | viset na řetězech # pytel | okno | žena | rukavice # Co dělá žena? # Bije do velkého pytle.
112 # roztáhnout křídla | kráčet k huse | nést muže # husa | dívka | strom | košík # Co dělá dívka? # Kráčí k huse.
114 # klepat na chléb | hořet v peci | stát na podlaze # chléb | muž | žena | stůl # Co dělá muž? # Klepe na chléb.
115 # rozbít vejce | jíst toast s vejcem | stát na plotě # strom | plot | toast | mléko # Co dělají? # Snídají na zahradě.
116 # držet kladivo | šťastně se smát | padat na podlahu # kladivo | muž | dlaždice | okno # Co dělá muž? # Rozbíjí dlaždice kladivem.
117 # balit talíře do látky | ukazovat hotovou mozaiku | sedět na polici # mozaika | kočka | palička | šátek # Co ukazuje muž? # Ukazuje hotovou mozaiku.
120 # péct maso | jíst velký burger | sedět u stolu # žena | ruka | burger # Co jí žena? # Jí velký burger.
123 # sbírat bobule | stát za ženou | vyletět z keře # ruka | miska | keř # Co sbírá žena? # Sbírá bobule z keře.
125 # jíst chléb s máslem | dotýkat se másla | sedět u okna # muž | kočka | máslo | chléb # Co jí žena? # Jí chléb s máslem.
126 # mít na sobě modrou košili | upravovat mužovu košili | ležet na polici # knoflík | okno | prst # Co dělá žena? # Upravuje mužovu košili.
127 # ukazovat na trny | mít na sobě khaki košili | tyčit se nad dvojicí # kaktus | trny | klobouk proti slunci | obloha # Na co ukazuje žena? # Ukazuje na trnitý kaktus.
128 # sfouknout svíčky | dívat se na stůl | mít navrchu bobule # dort | pes | balonek | koruna # Na co se dívá pes? # Pes se dívá na dort.
129 # mluvit do kamery | mít na sobě šedou mikinu s kapucí | ukazovat čísla # stůl | kalkulačka | ruka # Co mačká muž? # Mačká tlačítko na kalkulačce.
130 # držet červenou voskovku | mít na sobě žlutý svetr | viset na zdi # okno | kalendář | srdce | žena # Na co se dívá žena? # Dívá se na velký kalendář.
131 # mluvit po telefonu | smát se na balkoně | sedět na židli # obloha | květiny | telefon | šálek # Co dělá žena? # Telefonuje.
132 # šlapat na rotopedu | kontrolovat stopky | osvětlovat místnost # žárovka | stopky | rotoped | kbelík # Co dělá muž? # Spaluje kalorie na rotopedu.
133 # kráčet po písku | lehnout si na písek | dívat se do kamery # velbloud | slunce | písek | obloha # Co dělá velbloud? # Velbloud leží na písku.
134 # používat kladivo | ležet ve stanu | viset ve stanu # stan | stromy | tráva # Co dělají ti dva lidé? # Stanují v lese.
135 # zatínat pěst | zubit se radostí | zobrazovat textovou zprávu # kudrnaté vlasy | svetr | chytrý telefon # Co dělá muž? # Zubí se a zatíná pěst.
136 # hořet na stole | mít dlouhé vlasy | ležet na lavici # svíčka | kočka | kouř | žena # Co hoří na stole? # Na stole hoří svíčka.
138 # zakrývat si oči | dát mu kšiltovku | otočit si kšiltovku # kšiltovka | tričko | strom # Co dělá muž? # Otáčí si kšiltovku.
139 # jít do kopce | svítit na mapě | držet mapu # obloha | město | chlapec | mapa # Co drží chlapec? # Drží mapu.
140 # pokrývat podlahu | mít kudrnaté vlasy | mít na sobě modrý svetr # koberec | podlaha | muž | žena # Na čem leží? # Leží na zeleném koberci.
141 # vytahovat mrkev | lít vodu | stát v kleci # obloha | žena | mrkev | králík # Co jí žena? # Jí velkou mrkev.
145 # padat na písek | mít na sobě černé plavky | letět vzduchem # obloha | moře | míč | písek # Co dělá muž? # Chytá míč.
146 # lézt po listu | letět lesem | viset z větve # větev | motýl | housenka | list # Co dělá housenka? # Housenka leze po listu.
147 # vejít do jeskyně jako první | mít na sobě žlutou helmu | mít na sobě modrou bundu # listy | jeskyně | skála # Kam jdou ti dva lidé? # Vcházejí do tmavé jeskyně.
148 # sfouknout svíčky | přinést dort | mít na sobě košili # lampy | chlapec | dort | stůl # Co dělají ti tři kamarádi? # Slaví narozeniny s dortem.
149 # cenzurovat dopis | svírat slaměný klobouk | být otevřený dokořán # dopis | zásuvka | slaměný klobouk | stínidlo # Co dělá žena? # Cenzuruje mužův dopis.
150 # jíst lžící | nalévat mléko | zavřít oči # cereálie | lžíce | láhev | stůl # Co jí muž? # Jí cereálie lžící.
151 # držet těžký řetěz | stát za bránou | sedět na zdi # řetěz | kočka | brána | zeď # Co dělají ti dva muži? # Zamykají bránu řetězem.
152 # rozpřáhnout ruce doširoka | zkřížit si ruce | ležet u okna # židle | kočka | muž | žena # Co dělá žena? # Sedí na židli.
153 # chladit se v kbelíku s ledem | plnit se šampaňským | toulat se po terase # šampaňské | tác | ubrousek | žárovka # Čím se plní sklenice? # Sklenice se plní šampaňským.
154 # křičet na telefon | hledat nabíječku | sedět za mužem # nabíječka | telefon | kočka | čaj # Co hledá muž? # Hledá nabíječku.
156 # utírat si obličej | dostat zlatou medaili | dotýkat se své hrudi # hruď | medaile | vlajky | vlasy # Čeho se muž dotýká? # Dotýká se své hrudi.
157 # otevírat žvýkačku | dívat se na ženu | stát za lidmi # žvýkačka | nápoj | pták | moře # Co otevírá žena? # Otevírá žvýkačku.
158 # dotýkat se svého krku | zvednout jeden prst | jíst ořech # veverka | bonbony | košile | listy # Co dělají ti dva lidé? # Žvýkají na lavičce bonbony.
159 # nést slepici | mít na sobě modrou bundu | mít na sobě zelené tričko # slepice | stůl | bunda | listy # Co nese žena v bílém? # Nese slepici ke stolu.
160 # zobat zrní | usazovat se v hnízdě | nést proutěný košík # slepice | vejce | hnízdo | prkno # Co dělá slepice? # Slepice se usazuje v hnízdě.
161 # zakusovat se do stehýnka | vytahovat pekáč | nakukovat přes pult # stehýnko | bylinky | limetky | talíř # Do čeho se muž zakusuje? # Zakusuje se do kuřecího stehýnka.
162 # ukazovat na svá ústa | mít dlouhé vlasy | stát mezi dvěma lidmi # okno | lžíce | čokoláda | hrnec # Co jí muž? # Jí kousek čokolády.
164 # hltat celý knedlíček | předvádět držení hůlek | obsahovat knedlíčky vařené v páře # lampion | hůlky | miska | knedlíček # Co dělá muž? # Hltá celý knedlíček.
165 # držet krabici s popcornem | mít na sobě modrou bundu | letět ke hvězdám # dívka | chlapec | popcorn | sedadla # Kde jsou dívka a chlapec? # Jsou v kině.
167 # vhodit hlasovací lístek | svírat svůj pas | plnit se odpadky # vlajky | šátek | pas | kardigan # Co svírá občanka? # Občanka svírá svůj pas.
168 # předávat srolované osvědčení | ronit slzy radosti | zvednout svitek nad hlavu # svitek | šerpa | vousy | okno # Co předává úřednice? # Předává srolované osvědčení.
169 # vyrábět hliněný hrnec | sedět na podlaze | stát blízko hrnčířského kruhu # hlína | kočka | hrnčířský kruh | okno # Co vyrábí žena? # Vyrábí hrnec z hlíny.
170 # stlát postel | čistit okno | svítit na obloze # uklízečka | postel | dveře | slunce # Kdo stele postel? # Postel stele uklízečka.
171 # držet mikrofon | dát správnou odpověď | zkřížit si ruce # žena | muž | mikrofon | taška # Co dělá žena? # Má zkřížené ruce.
172 # sprintovat přes hřiště | zarývat se do bláta | svírat fotbalový míč # nepromokavá bunda | kamenná zeď | kopačky | bláto # Na co ukazuje žena? # Ukazuje na své zablácené kopačky.
173 # mít na sobě oranžovou bundu | mít krátké vousy | narážet do tmavých skal # moře | útes | žena | muž # Co dělají ti dva lidé? # Leží na vysokém útesu.
174 # vyplňovat formulář | svírat dřevěnou hůl | blížit se k lékaři # laboratorní plášť | pokojová rostlina | batoh | židle # Co dělá starý muž? # Svírá dřevěnou hůl.
175 # viset na zdi | nastavit hodiny | nosit brýle # šálky | okno | hodiny | kočka # Kde jsou hodiny? # Hodiny visí na zdi.
176 # obsahovat plápolající oheň | vypláznout jazyk | vyprsknout smíchy # uhlí | kamna | okno | rukáv # Co dělá muž? # Dává uhlí do kamen.
177 # obléknout si kabát | zavázat si pásek | držet palec nahoru # kabát | muž | lampa | obloha # Co dělá žena? # Obléká si hnědý kabát.
178 # protřepávat koktejl | nosit velké kruhové náušnice | sedět na baru # koktejl | kočka | třešeň | vousy # Co dělá muž? # Připravuje koktejl s třešní.
179 # napít se kávy | usmívat se na muže | stát na sporáku # káva | žena | závěs | okno # Co pije muž? # Pije šálek kávy.
180 # udělat díru | povytáhnout si šálu | zkřížit si ruce # čepice | šála | vysoké boty | díra # Jak se žena cítí? # Je jí na ledě velká zima.
181 # zvednout si límec | otevřít ústa dokořán | ukazovat na límec # kočka | límec | košile # Co dělá muž v bílém? # Drží si límec oběma rukama.
182 # česat si vlasy | mít na sobě oranžovou šálu | viset na zdi # vlasy | zrcadlo | hřeben | košile # Co dělá tmavovlasý muž? # Češe si vlasy oranžovým hřebenem.
183 # vzlykat do rukávu | utěšovat plačící kamarádku | utírat si slzy # rostlina v květináči | pihy | papírový kapesník | klíče # Co dělá muž? # Utěšuje svou plačící kamarádku.
184 # pískat na píšťalku | zvednout zaťatou pěst | sprintovat před všemi # pěst | píšťalka | vousy | odrazy # Co dělá trenérka? # Přikazuje ostatním, aby sprintovali.
185 # pádit na tramvaj | svírat poutko nad hlavou | přepravovat cestující # poutko | cestující | papírový kelímek | brašna # Co dělá muž? # Cestou do práce svírá poutko.
186 # sedět na tašce | křičet na kapelu | mít krátké vousy # strom | vlajky | pes | taška # Co lidé sledují? # Sledují koncert v parku.
187 # držet dvě desky | ukazovat malé obrázky | stát na čtyřech nohách # žena | okno | stůl | papír # Jak se žena cítí? # Je zmatená z malých obrázků.
"""
out = {}
for line in DATA.strip().splitlines():
    i, p, n, q, a = [x.strip() for x in line.split(' # ')]
    out[i] = {'phrases': [x.strip() for x in p.split(' | ')], 'nouns': [x.strip() for x in n.split(' | ')], 'question': q, 'answer': a}
src = json.load(open(f'{HERE}/source.json'))
out = {i: out[i] for i in src}
json.dump(out, open(f'{HERE}/{CODE}.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
