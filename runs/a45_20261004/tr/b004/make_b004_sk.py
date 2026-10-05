import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CODE = 'sk'
DATA = """
52 # niesť tašky | fotiť | stáť na skale # asistent | fotoaparát | taška | šaty # Kto nesie tašky? # Tašky nesie asistent.
53 # preskakovať prekážku | skákať do piesku | vrhať ťažkú guľu # prekážky | výsledková tabuľa | oblaky | bežecká dráha # Čo robí žena v zelenom? # Preskakuje prekážku.
55 # prihadzovať s číslom devätnásť | objímať drevenú tabuľku | mať na sebe pruhovaný top # stojace hodiny | plochá čiapka | tabuľka | okno # Čo robí ryšavá žena? # Prihadzuje na aukcii.
56 # skákať do lístia | chytať list | držať hrable # lístie | hrable | kabát | stromy # Čo robí žena? # Skáče do lístia.
58 # baliť si oblečenie | nasadiť si batoh | kráčať hore schodmi # dievča | oblečenie | fľaša | batoh # Čo robí dievča? # Balí si oblečenie do batoha.
61 # mať na sebe dlhý šál | sedieť na lavičke | pozorovať ľudí # lampa | muž | lavička | kačka # Čo robia tí dvaja ľudia? # Kráčajú pospiatky.
65 # ukladať zeleninu | ochutnávať pečený zemiak | ležať na podlahových doskách # husky | chňapka | kockovaná košeľa | plech na pečenie # Čo robí muž? # Ochutnáva pečený zemiak.
66 # vyberať chlieb | mať krátku bradu | ležať pri okne # okno | muž | žena | chlieb # Čo robí žena? # Pečie v kuchyni chlieb.
67 # šúpať banán | ukazovať na banán | jesť banán # muž | banán | papagáj # Čo robí muž? # Je banán.
69 # dvíhať ťažkú činku | mať hustú bradu | vystrieť nohy # svah | vrkoč | brada | činka # Čo robí blondínka? # Dvíha ťažkú činku.
71 # klopať na kmeň | držať sa kmeňa | odlupovať brezovú kôru # kôra | muž | žena | ďateľ # Čo robí žena? # Odlupuje kôru z brezy.
74 # držať pálku | letieť vzduchom | sedieť na tráve # strom | pálka | tričko | tráva # Čo drží žena? # Drží pálku.
75 # mávať kožovitými krídlami | rojiť sa po oblohe | odrážať západ slnka # netopier | obloha | stromy | jazero # Čo robí veľký netopier? # Máva krídlami nad jazerom.
76 # držať baterku | mať na sebe sivú čiapku | vkladať nové batérie # batérie | šálka | čiapka | žena # Čo drží žena? # Drží baterku.
78 # držať žlté vedierko | kopať lopatkou | byť z piesku # vedierko | lopatka | hrad z piesku | obloha # Čo stavajú? # Stavajú na pláži hrad z piesku.
79 # kráčať v rieke | stáť na dvoch nohách | letieť ponad stromy # medveď | vták | stromy | rieka # Čo robí medveď? # Kráča v rieke.
80 # česať si dlhú bradu | držať telefón | mať na sebe bielu košeľu # brada | hrebeň | čaj | kvety # Čo robí muž v bielom? # Češe si dlhú bradu.
81 # tancovať v šatách | mať na sebe modrú košeľu | svietiť nad morom # slnko | more | žena | muž # Čo robí žena? # Tancuje v bielych šatách.
83 # nalievať pivo | mať dlhé vlasy | spať pod stolom # pivo | chlieb | pes | lampy # Čo robí muž? # Nalieva pivo do pohára.
84 # pridržiavať si nohavice | nasadiť si opasok | šťastne tancovať # košeľa | opasok | nohavice | stolička # Čo má muž na sebe? # Má na sebe hnedý opasok.
85 # padať do sena | sebavedomo si založiť ruky | šibalsky sa škeriť # cyprusy | drdol | nohavice na traky | balík sena # Čo robí muž? # Padá do sena.
86 # rozkladať dlhý účet | odpočítavať bankovky | mať na sebe čiernu zásteru # čašník | účet | bankovky | karafa # Čo robí žena? # Rozkladá dlhý účet.
87 # spievať pieseň | sedieť na konári | letieť ponad trávu # vták | konár | tráva | obloha # Čo robí vták? # Vták spieva na konári.
88 # pozerať sa do kamery | otáčať hlavu | mať dlhé uši # pes | obloha | dom # Čo robí pes? # Pes sa pozerá do kamery.
89 # skákať z veže | sedieť pod inou mačkou | visieť zo stropu # mačka | lano | dvere | zrkadlo # Čo robí čierna mačka? # Skáče z veže.
90 # stáť na dvoch nohách | tancovať vo vode | ukazovať ružový jazyk # šteniatko | voda | fľaše # Čo robí šteniatko? # Tancuje vo vode.
91 # obviňovať chlapca | prekrížiť si ruky | olizovať si labku # zástera | odtlačky labiek | mikina s kapucňou | slúchadlá # Čo robí žena? # Obviňuje chlapca z neporiadku.
96 # skenovať palubný lístok | vítať cestujúcich na palube | listovať v časopise # časopis | závesy | ulička # Čo robí žena v žltom? # Nastupuje do lietadla.
97 # nalievať horúcu vodu | vrieť v hrnci | horieť pod hrncom # dievča | hrniec | oheň | hora # Čo robí dievča? # Varí vodu v hrnci.
99 # čítať zelenú knihu | držať veľkú šálku | spať na deke # okno | kniha | mačka | deka # Čo robí ryšavá žena? # Číta zelenú knihu.
101 # hrať sa s kľúčmi | vyzerať veľmi znudene | ukazovať čas # hodiny | kľúče | kniha | stolička # Ako vyzerá žena? # Vyzerá veľmi znudene.
103 # rozvaliť sa cez stoličky | točiť sa na pulte | visieť nad bielou tabuľou # hodiny | biela tabuľa | práčky | sandále # Kde leží muž? # Leží cez stoličky v práčovni.
104 # plávať ku dnu | zdvihnúť kameň | držať kameň hore # maska | kameň | dno # Čo robí žena? # Berie kameň z dna.
106 # mieriť na terč | slúžiť ako terč | pozorovať mladého lukostrelca # luk | balík sena | šíp | lukostrelec # Čo robí lukostrelec? # Mieri na balík sena.
107 # brať modrú misku | piť z misky | ležať na stole # okuliare | miska | lyžica | stôl # Čo robí chlapec? # Pije mlieko z misky.
110 # niesť veľkú škatuľu | dotýkať sa chrbta mačky | sedieť na škatuli # polica | mačka | žena | škatule # Čo robí žena? # Balí veľkú škatuľu.
111 # udierať do veľkého vreca | držať dve čierne lapy | visieť na reťaziach # vrece | okno | žena | rukavica # Čo robí žena? # Udiera do veľkého vreca.
112 # roztiahnuť krídla | kráčať k husi | niesť muža # hus | dievča | strom | košík # Čo robí dievča? # Kráča k husi.
114 # klopať na chlieb | horieť v peci | stáť na podlahe # chlieb | muž | žena | stôl # Čo robí muž? # Klope na chlieb.
115 # rozbiť vajce | jesť hrianku s vajcom | stáť na plote # strom | plot | hrianka | mlieko # Čo robia? # Raňajkujú v záhrade.
116 # držať kladivo | šťastne sa smiať | padať na podlahu # kladivo | muž | dlaždica | okno # Čo robí muž? # Rozbíja dlaždice kladivom.
117 # baliť taniere do látky | ukazovať hotovú mozaiku | sedieť na polici # mozaika | mačka | palička | šatka # Čo ukazuje muž? # Ukazuje hotovú mozaiku.
120 # piecť mäso | jesť veľký burger | sedieť pri stole # žena | ruka | burger # Čo žena je? # Je veľký burger.
123 # zbierať bobule | stáť za ženou | vyletieť z kríka # ruka | miska | krík # Čo zbiera žena? # Zbiera bobule z kríka.
125 # jesť chlieb s maslom | dotýkať sa masla | sedieť pri okne # muž | mačka | maslo | chlieb # Čo žena je? # Je chlieb s maslom.
126 # mať na sebe modrú košeľu | upravovať mužovu košeľu | ležať na polici # gombík | okno | prst # Čo robí žena? # Upravuje mužovu košeľu.
127 # ukazovať na tŕne | mať na sebe kaki košeľu | týčiť sa nad dvojicou # kaktus | tŕne | klobúk proti slnku | obloha # Na čo ukazuje žena? # Ukazuje na tŕnistý kaktus.
128 # sfúknuť sviečky | pozerať sa na stôl | mať navrchu bobule # torta | pes | balón | koruna # Na čo sa pozerá pes? # Pes sa pozerá na tortu.
129 # hovoriť do kamery | mať na sebe sivú mikinu s kapucňou | ukazovať čísla # stôl | kalkulačka | ruka # Čo stláča muž? # Stláča tlačidlo na kalkulačke.
130 # držať červenú voskovku | mať na sebe žltý sveter | visieť na stene # okno | kalendár | srdce | žena # Na čo sa pozerá žena? # Pozerá sa na veľký kalendár.
131 # hovoriť po telefóne | smiať sa na balkóne | sedieť na stoličke # obloha | kvety | telefón | šálka # Čo robí žena? # Telefonuje.
132 # šliapať na rotopede | kontrolovať stopky | osvetľovať miestnosť # žiarovka | stopky | rotoped | vedro # Čo robí muž? # Spaľuje kalórie na rotopede.
133 # kráčať po piesku | ľahnúť si na piesok | pozerať sa do kamery # ťava | slnko | piesok | obloha # Čo robí ťava? # Ťava leží na piesku.
134 # používať kladivo | ležať v stane | visieť v stane # stan | stromy | tráva # Čo robia tí dvaja ľudia? # Stanujú v lese.
135 # zatínať päsť | škeriť sa od radosti | zobrazovať textovú správu # kučeravé vlasy | sveter | smartfón # Čo robí muž? # Škerí sa a zatína päsť.
136 # horieť na stole | mať dlhé vlasy | ležať na lavici # sviečka | mačka | dym | žena # Čo horí na stole? # Na stole horí sviečka.
138 # zakrývať si oči | dať mu šiltovku | otočiť si šiltovku # šiltovka | tričko | strom # Čo robí muž? # Otáča si šiltovku.
139 # kráčať hore kopcom | svietiť na mape | držať mapu # obloha | mesto | chlapec | mapa # Čo drží chlapec? # Drží mapu.
140 # pokrývať podlahu | mať kučeravé vlasy | mať na sebe modrý sveter # koberec | podlaha | muž | žena # Na čom ležia? # Ležia na zelenom koberci.
141 # vyťahovať mrkvu | liať vodu | stáť v klietke # obloha | žena | mrkva | králik # Čo žena je? # Je veľkú mrkvu.
145 # padať na piesok | mať na sebe čierne plavky | letieť vzduchom # obloha | more | lopta | piesok # Čo robí muž? # Chytá loptu.
146 # liezť po liste | letieť lesom | visieť z konára # konár | motýľ | húsenica | list # Čo robí húsenica? # Húsenica lezie po liste.
147 # vojsť do jaskyne ako prvý | mať na sebe žltú prilbu | mať na sebe modrú bundu # listy | jaskyňa | skala # Kam idú tí dvaja ľudia? # Vchádzajú do tmavej jaskyne.
148 # sfúknuť sviečky | priniesť tortu | mať na sebe košeľu # lampy | chlapec | torta | stôl # Čo robia tí traja kamaráti? # Oslavujú narodeniny s tortou.
149 # cenzurovať list | zvierať slamený klobúk | byť otvorený dokorán # list | zásuvka | slamený klobúk | tienidlo # Čo robí žena? # Cenzuruje mužov list.
150 # jesť lyžicou | nalievať mlieko | zavrieť oči # cereálie | lyžica | fľaša | stôl # Čo muž je? # Je cereálie lyžicou.
151 # držať ťažkú reťaz | stáť za bránou | sedieť na múre # reťaz | mačka | brána | múr # Čo robia tí dvaja muži? # Zamykajú bránu reťazou.
152 # roztiahnuť ruky doširoka | prekrížiť si ruky | ležať pri okne # stolička | mačka | muž | žena # Čo robí žena? # Sedí na stoličke.
153 # chladiť sa vo vedierku s ľadom | plniť sa šampanským | túlať sa po terase # šampanské | podnos | obrúsok | žiarovka # Čím sa plnia poháre? # Poháre sa plnia šampanským.
154 # kričať na telefón | hľadať nabíjačku | sedieť za mužom # nabíjačka | telefón | mačka | čaj # Čo hľadá muž? # Hľadá nabíjačku.
156 # utierať si tvár | dostať zlatú medailu | dotýkať sa svojej hrude # hruď | medaila | vlajky | vlasy # Čoho sa muž dotýka? # Dotýka sa svojej hrude.
157 # otvárať žuvačku | pozerať sa na ženu | stáť za ľuďmi # žuvačka | nápoj | vták | more # Čo otvára žena? # Otvára žuvačku.
158 # dotýkať sa svojho krku | zdvihnúť jeden prst | jesť orech # veverička | cukríky | košeľa | listy # Čo robia tí dvaja ľudia? # Žujú na lavičke cukríky.
159 # niesť sliepku | mať na sebe modrú bundu | mať na sebe zelené tričko # sliepka | stôl | bunda | listy # Čo nesie žena v bielom? # Nesie sliepku k stolu.
160 # zobať zrno | usádzať sa v hniezde | niesť prútený košík # sliepka | vajce | hniezdo | doska # Čo robí sliepka? # Sliepka sa usádza v hniezde.
161 # zahrýzať sa do stehienka | vyberať pekáč | nakúkať ponad pult # stehienko | bylinky | limetky | tanier # Do čoho sa muž zahrýza? # Zahrýza sa do kuracieho stehienka.
162 # ukazovať na svoje ústa | mať dlhé vlasy | stáť medzi dvoma ľuďmi # okno | lyžica | čokoláda | hrniec # Čo muž je? # Je kúsok čokolády.
164 # hltať celú knedličku | predvádzať držanie paličiek | obsahovať knedličky varené v pare # lampión | paličky | miska | knedlička # Čo robí muž? # Hltá celú knedličku.
165 # držať škatuľu s pukancami | mať na sebe modrú bundu | letieť ku hviezdam # dievča | chlapec | pukance | sedadlá # Kde sú dievča a chlapec? # Sú v kine.
167 # vhodiť hlasovací lístok | zvierať svoj pas | plniť sa odpadkami # vlajky | šatka | pas | kardigán # Čo zviera občianka? # Občianka zviera svoj pas.
168 # odovzdávať zvinuté osvedčenie | roniť slzy radosti | zdvihnúť zvitok nad hlavu # zvitok | šerpa | brada | okno # Čo odovzdáva úradníčka? # Odovzdáva zvinuté osvedčenie.
169 # vyrábať hlinený hrniec | sedieť na podlahe | stáť blízko hrnčiarskeho kruhu # hlina | mačka | hrnčiarsky kruh | okno # Čo vyrába žena? # Vyrába hrniec z hliny.
170 # stlať posteľ | čistiť okno | svietiť na oblohe # upratovačka | posteľ | dvere | slnko # Kto stelie posteľ? # Posteľ stelie upratovačka.
171 # držať mikrofón | dať správnu odpoveď | prekrížiť si ruky # žena | muž | mikrofón | taška # Čo robí žena? # Má prekrížené ruky.
172 # šprintovať cez ihrisko | zarývať sa do blata | zvierať futbalovú loptu # nepremokavá bunda | kamenný múr | kopačky | blato # Na čo ukazuje žena? # Ukazuje na svoje zablatené kopačky.
173 # mať na sebe oranžovú bundu | mať krátku bradu | narážať do tmavých skál # more | útes | žena | muž # Čo robia tí dvaja ľudia? # Ležia na vysokom útese.
174 # vypĺňať formulár | zvierať drevenú palicu | blížiť sa k lekárovi # laboratórny plášť | izbová rastlina | batoh | stolička # Čo robí starý muž? # Zviera drevenú palicu.
175 # visieť na stene | nastaviť hodiny | nosiť okuliare # šálky | okno | hodiny | mačka # Kde sú hodiny? # Hodiny visia na stene.
176 # obsahovať plápolajúci oheň | vyplaziť jazyk | vyprsknúť smiechom # uhlie | kachle | okno | rukáv # Čo robí muž? # Dáva uhlie do kachlí.
177 # obliecť si kabát | zaviazať si opasok | držať palec hore # kabát | muž | lampa | obloha # Čo robí žena? # Oblieka si hnedý kabát.
178 # pretrepávať kokteil | nosiť veľké kruhové náušnice | sedieť na bare # kokteil | mačka | čerešňa | brada # Čo robí muž? # Pripravuje kokteil s čerešňou.
179 # napiť sa kávy | usmievať sa na muža | stáť na sporáku # káva | žena | záves | okno # Čo pije muž? # Pije šálku kávy.
180 # urobiť dieru | povytiahnuť si šál | prekrížiť si ruky # čiapka | šál | čižmy | diera # Ako sa žena cíti? # Je jej na ľade veľmi zima.
181 # zdvihnúť si golier | otvoriť ústa dokorán | ukazovať na golier # mačka | golier | košeľa # Čo robí muž v bielom? # Drží si golier oboma rukami.
182 # česať si vlasy | mať na sebe oranžový šál | visieť na stene # vlasy | zrkadlo | hrebeň | košeľa # Čo robí tmavovlasý muž? # Češe si vlasy oranžovým hrebeňom.
183 # vzlykať do rukáva | utešovať plačúcu kamarátku | utierať si slzy # rastlina v kvetináči | pehy | papierová vreckovka | kľúče # Čo robí muž? # Utešuje svoju plačúcu kamarátku.
184 # pískať na píšťalke | zdvihnúť zaťatú päsť | šprintovať pred všetkými # päsť | píšťalka | brada | odrazy # Čo robí trénerka? # Prikazuje ostatným, aby šprintovali.
185 # utekať na električku | zvierať pútko nad hlavou | prepravovať cestujúcich # pútko | cestujúci | papierový pohár | kapsa # Čo robí muž? # Cestou do práce zviera pútko.
186 # sedieť na taške | kričať na kapelu | mať krátku bradu # strom | vlajky | pes | taška # Čo ľudia sledujú? # Sledujú koncert v parku.
187 # držať dve dosky | ukazovať malé obrázky | stáť na štyroch nohách # žena | okno | stôl | papier # Ako sa žena cíti? # Je zmätená z malých obrázkov.
"""
out = {}
for line in DATA.strip().splitlines():
    i, p, n, q, a = [x.strip() for x in line.split(' # ')]
    out[i] = {'phrases': [x.strip() for x in p.split(' | ')], 'nouns': [x.strip() for x in n.split(' | ')], 'question': q, 'answer': a}
src = json.load(open(f'{HERE}/source.json'))
out = {i: out[i] for i in src}
json.dump(out, open(f'{HERE}/{CODE}.json', 'w'), ensure_ascii=False, indent=1)
print(len(out))
