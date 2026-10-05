import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(d, times):
    out = []
    for t in times:
        b = d.get(t)
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def save(c): json.dump(c, open(f'{HERE}/content/{c["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)

# ---------- 4591
t = T(19)
W = {0.0:(.27,.36,.42,.64),0.5:(.28,.36,.50,.64),1.0:(.20,.32,.48,.68),1.5:(0,.50,.56,.50),2.0:(0,.40,.52,.60),2.5:(0,0,.52,1),
     3.0:(.08,.33,.68,.67),3.5:(0,.46,1,.54),4.0:(.18,.40,.68,.36),4.5:(.20,.42,.66,.45),5.0:(0,.40,.52,.60),5.5:(0,.35,.64,.65),
     6.0:(0,.34,.54,.66),6.5:(0,.33,.65,.67),7.0:(.34,.45,.46,.55),7.5:(.34,.45,.58,.55),8.0:(.22,.43,.78,.57),8.5:(.36,.41,.64,.59),
     9.0:(.14,.40,.86,.60)}
S = {7.0:(.39,.30,.18,.15),7.5:(.39,.30,.18,.15),8.0:(.36,.29,.20,.14),8.5:(.36,.27,.20,.14),9.0:(.37,.26,.20,.14)}
wk = keys(W, t)
save({"mediaId":4591,"level":"A","keyWord":"ship","defaultVoice":"female",
 "taps":[{"phrase":"to pull a suitcase","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to jump into the pool","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to shine over the water","target":"the sun","voice":"female","keys":keys(S,t)}],
 "stillS":0.5,
 "nouns":[{"word":"a ship","x":.50,"y":.20,"voice":"female"},{"word":"a hat","x":.57,"y":.44,"voice":"female"},
          {"word":"a suitcase","x":.74,"y":.76,"voice":"female"},{"word":"a car","x":.12,"y":.63,"voice":"female"}],
 "question":"What is the woman pulling?",
 "answer":["She","is","pulling","a","suitcase","onto","a","ship."],"answerVoice":"female",
 "notes":"Clip with many cuts. 'the ship' not used as a tap target (it is the whole background in most shots). At 4.5 s the woman is under the splash: box kept on the splash. At 8.0-9.0 s the sun sits right above / behind her head: sun box ends where her hat begins. In the first shot she holds the suitcase behind her on the gangway (pulling it up)."})

# ---------- 4592
t = T(25)
W = {0.0:(.08,.15,.92,.85),0.5:(.15,.20,.85,.80),1.0:(.16,.20,.84,.80),1.5:(.17,.20,.83,.80),2.0:(.14,.18,.86,.82),2.5:(.10,.18,.90,.82),
     3.0:(.08,.20,.92,.80),3.5:(0,0,.45,.62),4.0:(0,0,.46,.45),4.5:(0,0,.42,.42),5.0:(0,0,.36,.40),5.5:(.12,0,.76,.60),
     6.0:(.15,0,.82,.58),6.5:(.12,0,.85,.57),7.0:(.04,0,.90,.78),7.5:(.10,0,.78,.78),8.0:(.03,0,.75,.70),8.5:(.07,0,.80,.68),
     9.0:(.10,.17,.38,.74),9.5:(.11,.17,.37,.74),10.0:(.10,.15,.41,.66),10.5:(.11,.15,.38,.66),11.0:(.12,.16,.37,.70),
     11.5:(.12,.16,.37,.70),12.0:(.09,.13,.38,.67)}
M = {3.5:(.66,0,.34,.62),4.0:(.70,0,.30,.47),4.5:(.74,0,.26,.42),5.0:(.80,0,.20,.40),
     9.0:(.49,.19,.45,.71),9.5:(.49,.19,.46,.71),10.0:(.52,.19,.42,.60),10.5:(.50,.19,.42,.60),11.0:(.50,.18,.42,.68),
     11.5:(.50,.18,.44,.68),12.0:(.47,.17,.42,.63)}
wk = keys(W, t)
save({"mediaId":4592,"level":"B","keyWord":"foot","defaultVoice":"female",
 "taps":[{"phrase":"to squeeze ripe grapes","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to throw her head back","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to have a grey moustache","target":"the man","voice":"male","keys":keys(M,t)}],
 "stillS":7.0,
 "nouns":[{"word":"a foot","x":.37,"y":.56,"voice":"female"},{"word":"grapes","x":.50,"y":.73,"voice":"female"},
          {"word":"jeans","x":.70,"y":.10,"voice":"female"},{"word":"a vat","x":.50,"y":.90,"voice":"female"}],
 "question":"What are they doing in the vat?",
 "answer":["They","are","crushing","grapes","with","their","bare","feet."],"answerVoice":"female",
 "notes":"The squeezing hand (0-3.0 s) and the bare legs in light rolled-up jeans (5.5-8.5 s) are taken as the woman's (her face comes in beside the arm at 2.0 s; she wears the light jeans). The man does nothing that only he does, so his phrase is a state. 'a foot': two feet in the still, the pill is on the left one. 'a vat' pill sits on the wooden rim."})

# ---------- 4593
t = T(21)
M = {0.0:(.07,.10,.90,.90),0.5:(.10,.10,.90,.90),1.0:(.05,.12,.92,.88),1.5:(.03,.10,.94,.90),2.0:(.08,.10,.84,.90),2.5:(.15,.13,.75,.87),
     3.0:(.18,.15,.65,.85),3.5:(.22,.17,.60,.83),4.0:(.26,.15,.52,.82),4.5:(.29,.19,.52,.74),5.0:(.30,.20,.44,.77),5.5:(.30,.19,.47,.80),
     6.0:(.31,.18,.42,.66),6.5:(.32,.20,.43,.67),7.0:(.31,.21,.46,.79),7.5:(.33,.19,.40,.80),8.0:(.30,.16,.50,.74),8.5:(.29,.16,.48,.76),
     9.0:(.27,.15,.50,.85),9.5:(.24,.18,.58,.82),10.0:(.24,.16,.60,.84)}
N = {3.0:(0,.35,.18,.60),3.5:(0,.26,.22,.72),4.0:(0,.27,.26,.50),4.5:(.05,.28,.24,.44),5.0:(.10,.30,.20,.50),5.5:(.10,.31,.20,.48),
     6.0:(.12,.30,.19,.36),6.5:(.13,.30,.19,.36),7.0:(.12,.30,.19,.50),7.5:(.15,.29,.18,.50),8.0:(.12,.29,.18,.38),8.5:(.11,.29,.18,.40),
     9.0:(.09,.30,.18,.55),9.5:(.06,.30,.18,.58),10.0:(0,.28,.24,.52)}
nk = keys(N, t)
save({"mediaId":4593,"level":"A","keyWord":"hospital","defaultVoice":"male",
 "taps":[{"phrase":"to walk on crutches","target":"the man","voice":"male","keys":keys(M,t)},
         {"phrase":"to walk behind the man","target":"the nurse","voice":"female","keys":nk},
         {"phrase":"to wear white clothes","target":"the nurse","voice":"female","keys":nk}],
 "stillS":4.0,
 "nouns":[{"word":"a nurse","x":.13,"y":.47,"voice":"female"},{"word":"a boot","x":.52,"y":.80,"voice":"male"},
          {"word":"windows","x":.83,"y":.27,"voice":"male"},{"word":"the floor","x":.78,"y":.92,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","walking","on","crutches","in","a","hospital."],"answerVoice":"male",
 "notes":"'crutches' is above A level but is what the clip shows; no simpler natural word. The nurse is off at 0-2.5 s (only her hand and the clipboard edge are in the picture). Where she walks close behind him the boxes are split along the line between them (9.5-10.0 s tight)."})

# ---------- 4594
t = T(19)
G = {x: (0, 0, 1, 1) for x in t}
gk = keys(G, t)
save({"mediaId":4594,"level":"A","keyWord":"together","defaultVoice":"female",
 "taps":[{"phrase":"to hug each other","target":"the friends","voice":"female","keys":gk},
         {"phrase":"to cry together","target":"the friends","voice":"female","keys":gk},
         {"phrase":"to dry their eyes","target":"the friends","voice":"female","keys":gk}],
 "stillS":2.0,
 "nouns":[{"word":"a tissue","x":.58,"y":.75,"voice":"female"},{"word":"a ring","x":.45,"y":.87,"voice":"female"},
          {"word":"a man","x":.86,"y":.30,"voice":"male"},{"word":"hair","x":.33,"y":.11,"voice":"female"}],
 "question":"What are the friends doing?",
 "answer":["They","are","crying","together."],"answerVoice":"female",
 "notes":"WEAK SPOT: the clip cuts every second between close-ups of different crying people (several look-alike blonde women, several men); everybody cries, laughs and wipes tears, so no phrase fits only one person and identities across shots are unclear. One target is used for all three phrases: 'the friends' = the people of the group, box = whole picture in every frame. The hug is only at 8.0-9.0 s. 'a man' in the still is the blurred bearded man on the right."})
