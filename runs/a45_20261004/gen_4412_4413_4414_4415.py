import json
def keys(T,d): return [({"t":t,"off":True} if t not in d else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
def save(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1,ensure_ascii=False)

# ---------- 4412 ----------
T=[i/2 for i in range(25)]
D={0.0:(.15,.36,.41,.42),0.5:(.18,.35,.41,.42),1.0:(.15,.36,.40,.46),1.5:(.14,.38,.38,.46),2.0:(.10,.36,.32,.36),
2.5:(0,.38,.20,.22),3.0:(0,.40,.27,.30),5.0:(0,.18,1,.82),5.5:(0,.15,1,.85),6.0:(0,.15,1,.85),6.5:(0,.15,1,.85),
7.0:(0,.42,.45,.48),9.5:(0,.28,.27,.70),10.0:(.10,.25,.40,.50),10.5:(.10,.29,.43,.48),11.0:(.08,.28,.42,.56),
11.5:(.08,.28,.46,.56),12.0:(.08,.28,.42,.50)}
L={0.0:(.56,0,.44,1),0.5:(.59,0,.41,1),1.0:(.55,0,.45,1),1.5:(.53,0,.47,1),2.0:(.44,0,.56,1)}
S={7.5:(.10,.38,.90,.32),8.0:(0,.40,.55,.28),8.5:(0,.44,1,.38),9.0:(0,.44,1,.56),9.5:(.28,.42,.72,.58),
10.0:(.50,.38,.50,.62),10.5:(.53,.38,.47,.62),11.0:(.50,.40,.50,.60),11.5:(.54,.55,.46,.45),12.0:(.50,.56,.50,.44)}
save({"mediaId":4412,"level":"B","keyWord":"block","defaultVoice":"male",
"taps":[{"phrase":"to yell from his van","target":"the driver","voice":"male","keys":keys(T,D)},
{"phrase":"to block the narrow street","target":"the lorry","voice":"male","keys":keys(T,L)},
{"phrase":"to press against the van","target":"the sheep","voice":"male","keys":keys(T,S)}],
"stillS":10.0,
"nouns":[{"word":"a shepherd","x":.45,"y":.36,"voice":"male"},{"word":"a hi-vis vest","x":.25,"y":.55,"voice":"male"},
{"word":"a wing mirror","x":.40,"y":.76,"voice":"male"},{"word":"a bell","x":.67,"y":.87,"voice":"male"}],
"question":"What is blocking the mountain road?","answer":["A","flock","of","sheep","is","blocking","the","road."],"answerVoice":"male",
"notes":"Three shots (street, market, mountain road). Targets: the driver, the lorry (0-2 s only), the sheep (flock, from 7.5 s). The shepherd is not a target; at 9.5-11 s part of him lies inside the driver's box (he stands right behind the driver's head). 11.5-12 s: the driver's stretched arm crosses above the flock, so the sheep box starts below the arm. Driver off at 3.5-4.5 (hidden behind the windscreen / out of frame) and 7.5-9.0. 'a shepherd' pill is on the man in the straw hat, close to the driver's face. The sheep also block a road, but 'the narrow street' is only the lorry's shot."})

# ---------- 4413 ----------
W={0.0:(0,0,1,.37),0.5:(0,0,1,.40),1.0:(0,0,1,.41),1.5:(0,0,1,.43),2.0:(0,0,1,.48),2.5:(0,0,1,.53),3.0:(0,0,1,.54),
3.5:(.15,.03,.75,.51),4.0:(.30,.26,.50,.29),4.5:(.10,.36,.80,.64),5.0:(.15,.46,.62,.54),5.5:(.17,.53,.53,.47),
6.0:(.13,.56,.52,.44),6.5:(.22,.60,.48,.40),7.0:(.29,.64,.45,.36),7.5:(.29,.66,.44,.34),8.0:(.31,.67,.45,.33),
8.5:(.32,.67,.43,.33),9.0:(.31,.63,.34,.37),9.5:(.35,.61,.35,.39),10.0:(.27,.61,.46,.39),10.5:(.07,.61,.88,.39),
11.0:(.02,.62,.96,.38),11.5:(.02,.61,.96,.39),12.0:(.02,.61,.96,.39)}
B={0.0:(.36,.37,.26,.17),0.5:(.34,.40,.26,.16),1.0:(.32,.41,.26,.16),1.5:(.38,.43,.26,.16),2.0:(.40,.48,.26,.15),
2.5:(.39,.53,.27,.14),3.0:(.39,.54,.26,.14),3.5:(.44,.54,.20,.14),4.0:(.38,.55,.20,.14)}
save({"mediaId":4413,"level":"A","keyWord":"smell","defaultVoice":"female",
"taps":[{"phrase":"to smell the flowers","target":"the woman","voice":"female","keys":keys(T,W)},
{"phrase":"to open her arms wide","target":"the woman","voice":"female","keys":keys(T,W)},
{"phrase":"to sit on a flower","target":"the bee","voice":"female","keys":keys(T,B)}],
"stillS":3.0,
"nouns":[{"word":"a nose","x":.50,"y":.30,"voice":"female"},{"word":"a bee","x":.52,"y":.60,"voice":"female"},
{"word":"a mouth","x":.50,"y":.41,"voice":"female"},{"word":"a coat","x":.52,"y":.93,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","smelling","the","pink","flowers."],"answerVoice":"female",
"notes":"Two targets: the woman and the bee. In the close-up (0-3 s) the bee sits on the flowers in front of her face, so the woman's box is the strip above the bee (her face) and her hands below are in neither box. 3.5-4.0 s: the bee is tiny on the flowers she holds (box on that cluster, the woman's box is her head above it); from 4.5 s the bee is not visible. Key word 'smell' is a noun in the packet; the phrase and answer use the verb. No 'flowers' noun on the still: the bee sits on the flowers, the two slots could not be told apart."})

# ---------- 4414 ----------
T=[i/2 for i in range(21)]
M={0.0:(0,.23,.86,.77),0.5:(0,.23,.86,.77),1.0:(0,.24,.86,.76),1.5:(0,.24,.85,.76),2.0:(0,.20,.82,.80),2.5:(0,.22,.80,.78),
3.0:(0,.24,.79,.76),3.5:(0,.23,.82,.77),4.0:(0,.21,.85,.79),4.5:(0,.22,.91,.78),5.0:(0,.23,.91,.77),5.5:(0,.29,1,.71),
6.0:(0,.37,.88,.63),6.5:(0,.33,.87,.67),7.0:(0,.32,.84,.68),7.5:(0,.31,.84,.69),8.0:(.02,.28,.82,.66),8.5:(.06,.27,.76,.67),
9.0:(0,.30,.76,.68),9.5:(0,.30,.79,.68),10.0:(0,.27,.82,.69)}
SEA={0.0:(0,.08,1,.15),0.5:(0,.08,1,.15),1.0:(0,.08,1,.16),1.5:(0,.08,1,.16),2.0:(0,.06,1,.14),2.5:(0,.07,1,.15),
3.0:(0,.08,1,.16),3.5:(0,.08,1,.15),4.0:(0,.07,1,.14),4.5:(0,.08,1,.14),5.0:(0,.08,1,.15),5.5:(0,.10,1,.19),
6.0:(0,.10,1,.27),6.5:(0,.08,1,.25),7.0:(0,.10,1,.22),7.5:(0,.10,1,.21),8.0:(0,.05,1,.23),8.5:(0,.05,1,.22),
9.0:(0,.08,1,.22),9.5:(0,.08,1,.22),10.0:(0,.06,1,.21)}
save({"mediaId":4414,"level":"B","keyWord":"struggle","defaultVoice":"male",
"taps":[{"phrase":"to clutch his woollen hat","target":"the man","voice":"male","keys":keys(T,M)},
{"phrase":"to struggle against the wind","target":"the man","voice":"male","keys":keys(T,M)},
{"phrase":"to stretch to the horizon","target":"the sea","voice":"male","keys":keys(T,SEA)}],
"stillS":8.5,
"nouns":[{"word":"the sea","x":.45,"y":.15,"voice":"male"},{"word":"a beanie","x":.76,"y":.33,"voice":"male"},
{"word":"a scarf","x":.42,"y":.50,"voice":"male"},{"word":"grass","x":.70,"y":.88,"voice":"male"}],
"question":"What is the man struggling against?","answer":["He","is","struggling","against","the","strong","wind."],"answerVoice":"male",
"notes":"One person. Second target: the sea. The man stands in front of it, so the sea box is only the strip of open water above his head (the surf to his left and right is in no box). The wind is seen only through its effects (scarf, hood, grass, his posture). Key word 'struggle' is a noun in the packet; phrase and answer use the verb. He grabs his hat at 4.5-5.0 s."})

# ---------- 4415 ----------
T=[i/2 for i in range(19)]
G={2.0:(0,.15,1,.85),2.5:(0,.15,1,.85),8.5:(0,.30,.33,.68),9.0:(0,.34,.34,.66)}
N={4.5:(0,.08,1,.92),5.0:(0,.07,1,.93),5.5:(0,.07,1,.93),8.0:(.72,.28,.28,.42),8.5:(.73,.32,.16,.30)}
H={3.0:(0,.08,1,.92),3.5:(0,.08,1,.92),4.0:(0,.08,1,.92),7.0:(0,.13,1,.87),7.5:(.12,.22,.76,.50),8.0:(.26,.29,.45,.32),
8.5:(.42,.33,.31,.29),9.0:(.42,.39,.24,.19)}
save({"mediaId":4415,"level":"B","keyWord":"compliment","defaultVoice":"male",
"taps":[{"phrase":"to give an embarrassed wave","target":"the woman in green","voice":"female","keys":keys(T,G)},
{"phrase":"to read a handwritten note","target":"the woman with the note","voice":"female","keys":keys(T,N)},
{"phrase":"to wear a grey hoodie","target":"the man in the hoodie","voice":"male","keys":keys(T,H)}],
"stillS":5.5,
"nouns":[{"word":"a necklace","x":.58,"y":.65,"voice":"male"},{"word":"a denim jacket","x":.19,"y":.56,"voice":"male"},
{"word":"a note","x":.42,"y":.86,"voice":"male"}],
"question":"What is the woman in denim reading?","answer":["She","is","reading","a","handwritten","note."],"answerVoice":"female",
"notes":"Many cuts, a different face in almost every shot: long-haired woman (0-1.5, 6.5 s, no target), woman in the green jacket (2.0-2.5 s), man in the grey hoodie (3.0-4.0, 7.0-7.5 s), woman with the note (4.5-5.5 s), woman in a cream jumper (6.0 s, no target), group at the table (8.0-9.0 s). Group shots: boxes only where the person is recognisable by clothes - please check the identities at 8.0-9.0 s (green jacket on the left at 8.5/9.0; hoodie man in the middle; the denim-jacket woman on the right at 8.0/8.5 taken as the note reader; her 8.5 box is narrow because the cream-jumper woman is beside her). 'to wear a grey hoodie' is a state: everything the man does (covering his face, laughing) is also done by others; the bearded man in the group wears a denim jacket. Key word 'compliment' is not visible, so it is in no text. defaultVoice male: mixed group, evenId false. Only 3 nouns."})
