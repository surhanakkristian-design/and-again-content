import json
def keys(T,d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
def fix(d):
    return {k:tuple(round(v,2) for v in b) for k,b in d.items()}
T21=[i*0.5 for i in range(21)]; T19=[i*0.5 for i in range(19)]
# ---------- 456
L={0.0:(0,.21,.58,.33),0.5:(0,.21,.60,.36),1.0:(0,.30,.47,.33),1.5:(0,0,.28,.44),2.0:(0,0,.32,.54),2.5:(0,0,.30,.63),
   3.0:(0,0,.38,.80),3.5:(0,.03,.33,.65),4.0:(0,.05,.44,.39),4.5:(0,.05,.42,.41),5.0:(0,.08,.41,.42),5.5:(0,.08,.42,.42),
   6.0:(0,.08,.38,.37),6.5:(0,.08,.36,.37),7.0:(0,.05,.48,.75),7.5:(0,.05,.45,.77),8.0:(0,.05,.32,.72),8.5:(0,.05,.34,.72),
   9.0:(0,.05,.34,.77),9.5:(0,.05,.37,.80),10.0:(0,.08,.36,.87)}
C={0.0:(.22,.03,.42,.17),0.5:(.24,.03,.48,.17),1.0:(.29,.08,.47,.21),1.5:(.34,.17,.47,.22),2.0:(.33,.20,.37,.14),
   2.5:(.31,.29,.33,.14),3.5:(.34,.39,.38,.14),4.0:(.32,.45,.39,.14),4.5:(.32,.47,.34,.14),5.0:(.31,.51,.38,.14),
   5.5:(.31,.51,.36,.14),6.0:(.32,.46,.30,.14),6.5:(.33,.46,.33,.14),8.0:(.33,.47,.38,.14),8.5:(.35,.47,.38,.14),
   9.0:(.35,.48,.41,.15),9.5:(.38,.47,.40,.14),10.0:(.37,.47,.42,.14)}
R={0.0:(.66,0,.34,.42),0.5:(.74,0,.26,.42),1.0:(.77,0,.23,.50),1.5:(.82,.05,.18,.47),2.0:(.82,.08,.18,.47),2.5:(.74,0,.26,.62),
   3.0:(.76,.18,.24,.60),3.5:(.82,.13,.18,.62),4.0:(.72,.08,.28,.60),4.5:(.67,.10,.33,.60),5.0:(.70,.10,.30,.60),
   5.5:(.68,.10,.32,.62),6.0:(.63,.13,.37,.57),6.5:(.67,.12,.33,.58),7.0:(.70,.10,.30,.70),7.5:(.75,.17,.25,.68),
   8.0:(.74,.18,.26,.62),8.5:(.78,.18,.22,.62),9.0:(.77,.13,.23,.72),9.5:(.80,.17,.20,.72),10.0:(.80,.15,.20,.65)}
c={"mediaId":456,"level":"A","keyWord":"magazine","defaultVoice":"female",
 "taps":[{"phrase":"to turn the pages","target":"the woman in brown","voice":"female","keys":keys(T21,L)},
  {"phrase":"to sleep on a chair","target":"the cat","voice":"female","keys":keys(T21,C)},
  {"phrase":"to wear a blue top","target":"the woman in blue","voice":"female","keys":keys(T21,R)}],
 "stillS":10.0,
 "nouns":[{"word":"a window","x":.36,"y":.17,"voice":"female"},{"word":"a plant","x":.62,"y":.36,"voice":"female"},
  {"word":"a cat","x":.56,"y":.55,"voice":"female"},{"word":"magazines","x":.62,"y":.87,"voice":"female"}],
 "question":"What are the two women doing?","answer":["They","are","looking","at","a","magazine."],"answerVoice":"female",
 "notes":"The cat lies on a round stool; 'chair' used as the A-level word. Cat off at 3.0, 7.0, 7.5 (hidden behind the open magazine). 4.0-6.5: the woman in brown's box is head and shoulders only, because the cat lies in front of her body column and the boxes may not overlap. 0.0-1.0: only arms/hands of the woman in brown are in the picture. The woman in blue only watches: her phrase is a state (blue = turquoise top). Key word as the plural 'magazines' on the pile on the table at 10.0 (no held magazine at that moment)."}
json.dump(c,open('content/456.json','w'),indent=1)
# ---------- 458
Y={0.0:(.12,.24,.62,.66),0.5:(.15,.21,.63,.70),1.0:(.25,.22,.42,.78),1.5:(0,.17,.85,.83),2.0:(.22,.19,.48,.81),
   7.5:(.65,.33,.35,.34),8.0:(.30,.18,.70,.82),8.5:(.51,.15,.49,.85),9.0:(.48,.18,.40,.82),9.5:(.50,.17,.45,.83),10.0:(.51,.15,.49,.85)}
S={6.0:(.80,.19,.20,.36),6.5:(.62,.20,.31,.41),7.0:(.39,.21,.34,.60),7.5:(.03,.21,.42,.76),8.0:(0,.21,.29,.79),
   8.5:(0,.18,.50,.82),9.0:(.10,.18,.37,.82),9.5:(.08,.19,.41,.81),10.0:(0,.19,.50,.81)}
B={3.5:(.52,.19,.48,.72),4.0:(.19,.17,.60,.71),4.5:(.03,.27,.78,.65),5.0:(0,.24,.70,.76),5.5:(0,0,.32,.97)}
c={"mediaId":458,"level":"A","keyWord":"man","defaultVoice":"male",
 "taps":[{"phrase":"to run after the birds","target":"the young man","voice":"male","keys":keys(T21,Y)},
  {"phrase":"to carry a big box","target":"the big man","voice":"male","keys":keys(T21,B)},
  {"phrase":"to wear a dark tie","target":"the man in the suit","voice":"male","keys":keys(T21,S)}],
 "stillS":0.0,
 "nouns":[{"word":"the sky","x":.55,"y":.06,"voice":"male"},{"word":"a building","x":.28,"y":.22,"voice":"male"},
  {"word":"a man","x":.47,"y":.48,"voice":"male"},{"word":"birds","x":.50,"y":.86,"voice":"male"}],
 "question":"What is the young man doing?","answer":["He","is","running","after","the","birds."],"answerVoice":"male",
 "notes":"Clip with cuts: young man 0.0-2.0 and 7.5-10.0 (7.5 only his arm at the right edge); big man 3.5-5.5; man in the suit 6.0-10.0. The two old chess players are not targets (two of them, so 'to play chess' fits no single target). Suit man's phrase is a state: his actions (run, shake hands, hug) are shared with the young man. Handshake/hug frames split the two boxes along the line between the men. 'a man' at 0.0 sits on the young man; the other people there are tiny background figures."}
json.dump(c,open('content/458.json','w'),indent=1)
# ---------- 459
M={1.5:(0,.27,.45,.73),2.0:(.09,.09,.82,.91),2.5:(.10,.09,.83,.91),3.0:(0,.31,.24,.23),3.5:(0,.35,.22,.20),4.0:(0,.38,.35,.19),
   5.5:(0,.11,.65,.89),6.0:(0,.14,.50,.66),6.5:(.15,.11,.83,.74),7.0:(0,.11,.95,.76),7.5:(0,.12,.92,.74),8.0:(0,.15,.72,.67),
   8.5:(0,.12,.36,.69),9.0:(.70,.34,.24,.56),9.5:(.69,.34,.25,.56),10.0:(.70,.33,.24,.58)}
G={0.0:(.09,.57,.30,.24),0.5:(.31,.55,.33,.24),1.0:(.54,.54,.31,.35),4.0:(.36,.19,.64,.81),6.0:(.51,.20,.49,.60),
   8.5:(.60,.20,.40,.42),9.0:(.50,.36,.19,.25),9.5:(.46,.36,.22,.26),10.0:(.49,.30,.20,.30)}
Bd={0.5:(0,.52,.18,.27),1.0:(.14,.50,.25,.39),3.0:(.25,.17,.40,.83),4.5:(.12,.15,.66,.85),9.0:(.07,.27,.24,.73),
   9.5:(.08,.28,.24,.70),10.0:(.08,.24,.26,.68)}
c={"mediaId":459,"level":"B","keyWord":"manager","defaultVoice":"female",
 "taps":[{"phrase":"to write on a clipboard","target":"the manager","voice":"female","keys":keys(T21,M)},
  {"phrase":"to give a thumbs up","target":"the man in glasses","voice":"male","keys":keys(T21,G)},
  {"phrase":"to have a shaved head","target":"the bald man","voice":"male","keys":keys(T21,Bd)}],
 "stillS":7.0,
 "nouns":[{"word":"a manager","x":.28,"y":.40,"voice":"female"},{"word":"a clipboard","x":.78,"y":.47,"voice":"female"},
  {"word":"crates","x":.42,"y":.72,"voice":"female"},{"word":"flowers","x":.50,"y":.93,"voice":"female"}],
 "question":"What is the manager doing?","answer":["She","is","writing","on","a","clipboard."],"answerVoice":"female",
 "notes":"Manager = woman in the green uniform (off 0.0-1.0, 4.5, 5.0; at 3.0-4.0 only her pointing arm is in the picture, boxed as her). Thumbs up: man in glasses at 9.0 only. Bald man's phrase is a state: his action (stacking crates, 4.5) is shared with the man in glasses (8.5). The hand with the hose at 5.0 belongs to nobody identifiable: no box. Group shots 9.0-10.0: narrow boxes split between the man in glasses and the manager; at 10.0 her raised arm crosses into his box. The manager wears glasses pushed up on her head; 'the man in glasses' is the only man with glasses."}
json.dump(c,open('content/459.json','w'),indent=1)
# ---------- 462
Gi={1.5:(.15,.37,.44,.34),2.0:(.05,.37,.52,.29),2.5:(.14,.38,.44,.22),3.0:(0,.38,.30,.24),3.5:(0,.38,.31,.27),
   6.5:(.17,.41,.33,.45),7.0:(.14,.43,.29,.48),7.5:(.24,.36,.20,.33),8.0:(0,.45,.37,.43),8.5:(0,.38,.40,.50)}
Mn={1.5:(.60,.07,.38,.64),2.0:(.58,.08,.42,.58),2.5:(.59,.10,.41,.50),3.0:(.31,0,.69,.62),3.5:(.32,0,.68,.65),
   6.5:(.51,.27,.30,.65),7.0:(.44,.29,.30,.71),7.5:(.53,.27,.32,.38),8.0:(.58,.19,.42,.68),8.5:(.56,.17,.44,.70)}
Mp={0.0:(.22,.07,.56,.88),0.5:(0,.07,1,.90),1.0:(0,.08,1,.90),1.5:(0,.72,1,.26),2.0:(0,.67,1,.20),2.5:(0,.61,1,.26),
   3.0:(0,.63,1,.37),3.5:(0,.66,1,.34),4.0:(0,0,1,1),4.5:(0,0,1,1),5.0:(0,0,1,1),5.5:(0,0,1,1),6.0:(0,0,1,1),
   6.5:(.82,.44,.18,.24),7.0:(.75,.38,.25,.22),8.5:(.11,.12,.44,.25),9.0:(.38,.20,.50,.38)}
c={"mediaId":462,"level":"A","keyWord":"map","defaultVoice":"female",
 "taps":[{"phrase":"to wear a red hat","target":"the girl","voice":"female","keys":keys(T19,Gi)},
  {"phrase":"to run with a map","target":"the man","voice":"male","keys":keys(T19,Mn)},
  {"phrase":"to fly in the air","target":"the map","voice":"female","keys":keys(T19,Mp)}],
 "stillS":2.0,
 "nouns":[{"word":"a hat","x":.38,"y":.44,"voice":"female"},{"word":"glasses","x":.36,"y":.55,"voice":"female"},
  {"word":"a shirt","x":.78,"y":.56,"voice":"female"},{"word":"a map","x":.50,"y":.76,"voice":"female"}],
 "question":"What are they looking at?","answer":["They","are","looking","at","a","map."],"answerVoice":"female",
 "notes":"Man + girl = mixed pair, defaultVoice by evenId. The man runs holding the map at 6.5-7.0 (the girl runs without it); the map flies at 8.5-9.0. Girl's phrase is a state: her actions (hold the map, run, cheer) are shared with the man. 1.5-3.5: man, girl and map overlap, boxes split (map = lower band, girl left, man right; some of his hair falls outside). 0.0: POV hands with red sleeves on the map, girl not boxed. 4.0-6.0: the map fills the frame (a finger of an unseen person on it). 8.0: the blank sheet they hold behind the fountain is not boxed as the map (at 8.5 it is still held while the map flies)."}
json.dump(c,open('content/462.json','w'),indent=1)
