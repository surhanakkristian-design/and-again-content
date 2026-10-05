import json
OFF=None
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]

# ---------- 263
t=T(11)
sw={1.5:(.22,.40,.58,.24),2.0:(.10,.25,.68,.50),2.5:(.10,.27,.68,.48),3.0:(.06,.29,.72,.46),3.5:(.02,.28,.77,.47),
    4.0:(0,.28,.78,.47),4.5:(0,.25,.78,.50),5.0:(0,.25,.78,.50)}
bo={0.0:(.72,.19,.28,.14),0.5:(.72,.19,.28,.14),1.0:(.72,.19,.28,.14),1.5:(.72,.21,.28,.14),2.0:(.79,.29,.21,.14),
    2.5:(.79,.30,.21,.14),3.0:(.79,.31,.21,.14),3.5:(.80,.31,.20,.14),4.0:(.79,.30,.21,.14),4.5:(.79,.30,.21,.14),5.0:(.79,.30,.21,.14)}
ks=keys(t,sw); kb=keys(t,bo)
c={"mediaId":263,"level":"B","keyWord":"emerge","defaultVoice":"female",
 "taps":[{"phrase":"to emerge from the lake","target":"the swimmer","voice":"female","keys":ks},
         {"phrase":"to adjust her goggles","target":"the swimmer","voice":"female","keys":ks},
         {"phrase":"to float near the shore","target":"the boat","voice":"female","keys":kb}],
 "stillS":2.5,
 "nouns":[{"word":"goggles","x":.52,"y":.46,"voice":"female"},{"word":"a rowing boat","x":.84,"y":.37,"voice":"female"},
          {"word":"a reflection","x":.50,"y":.86,"voice":"female"},{"word":"mountains","x":.45,"y":.10,"voice":"female"}],
 "question":"What is the swimmer doing?","answer":["She","is","emerging","from","the","lake."],"answerVoice":"female",
 "notes":"Swimmer is under water until 1.5 s (only a splash at 1.0 s) -> off. From 2.0 s her right shoulder / raised arm reaches under the boat; her box is cut at x 0.78 so it does not overlap the boat box. 'mountains' are soft green hills in haze."}
json.dump(c,open("content/263.json","w"),indent=1)

# ---------- 264
t=T(21)
wo={0.0:(.13,.18,.71,.82),0.5:(.13,.18,.71,.82),1.0:(.15,.18,.72,.82),2.5:(.23,.22,.71,.78),3.0:(.16,.25,.84,.75),
    3.5:(.18,.36,.82,.64),4.0:(.04,.29,.94,.71),4.5:(0,.32,.45,.68),5.0:(0,.30,.47,.70),5.5:(.16,.18,.47,.82),
    6.0:(0,.19,.50,.81),6.5:(0,.26,.32,.74),7.0:(0,.15,.36,.85),7.5:(0,.14,.49,.86),8.0:(0,.11,.47,.89),
    8.5:(0,.09,.55,.91),9.0:(0,.10,.66,.90),9.5:(0,.11,.65,.89),10.0:(0,.10,.63,.90)}
ma={1.5:(.08,.21,.76,.66),2.0:(0,.22,.74,.62),4.5:(.45,.27,.45,.30),5.0:(.47,.33,.45,.67),5.5:(.63,.22,.37,.78),
    6.0:(.50,.21,.42,.79),6.5:(.32,.16,.68,.84),7.0:(.36,.16,.64,.84),7.5:(.49,.16,.51,.84),8.0:(.47,.13,.53,.87),
    8.5:(.55,.11,.45,.89),9.0:(.66,.16,.34,.84),9.5:(.65,.16,.35,.84),10.0:(.63,.13,.37,.87)}
kw=keys(t,wo); km=keys(t,ma)
c={"mediaId":264,"level":"B","keyWord":"emotion","defaultVoice":"female",
 "taps":[{"phrase":"to clutch a bouquet","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to lean on the railing","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to push a luggage trolley","target":"the man","voice":"male","keys":km}],
 "stillS":0.0,
 "nouns":[{"word":"a bouquet","x":.50,"y":.47,"voice":"female"},{"word":"a cardigan","x":.28,"y":.58,"voice":"female"},
          {"word":"a railing","x":.72,"y":.68,"voice":"female"},{"word":"jeans","x":.50,"y":.88,"voice":"female"}],
 "question":"What is the woman holding?","answer":["She","is","clutching","a","bouquet","of","yellow","flowers."],"answerVoice":"female",
 "notes":"From 4.5 s the two hug and overlap heavily: boxes are split by a vertical line between the two heads, so each box also loses parts of its person (her arms around his neck fall into his box, his arms around her waist into hers). The three phrases happen before the hug (0-4 s). Background crowd has no box."}
json.dump(c,open("content/264.json","w"),indent=1)

# ---------- 265
em={0.0:(.15,.15,.85,.70),1.5:(.08,.43,.74,.45),2.5:(.49,.26,.51,.54),4.0:(0,.29,.62,.65),4.5:(0,.29,.60,.65),
    5.0:(0,.38,.50,.62),5.5:(0,.36,.48,.64),6.0:(0,.09,.90,.87),6.5:(0,.13,.94,.83),7.0:(0,.08,1,.92),7.5:(0,.08,1,.92),
    8.0:(0,.19,1,.81),8.5:(.40,.21,.60,.79),9.0:(.40,.22,.60,.78),9.5:(.04,.06,.96,.94),10.0:(.01,.04,.99,.96)}
bs={4.0:(.63,0,.37,1),4.5:(.60,0,.40,1),5.0:(.50,.01,.50,.99),5.5:(.48,.01,.52,.99)}
ke=keys(t,em); kb=keys(t,bs)
c={"mediaId":265,"level":"A","keyWord":"employee","defaultVoice":"male",
 "taps":[{"phrase":"to get an envelope","target":"the man with glasses","voice":"male","keys":ke},
         {"phrase":"to put on a jacket","target":"the man with glasses","voice":"male","keys":ke},
         {"phrase":"to touch his shoulder","target":"the woman","voice":"female","keys":kb}],
 "stillS":0.0,
 "nouns":[{"word":"an employee","x":.74,"y":.56,"voice":"male"},{"word":"paper","x":.25,"y":.48,"voice":"male"},
          {"word":"a keyboard","x":.18,"y":.89,"voice":"male"},{"word":"a window","x":.18,"y":.18,"voice":"male"}],
 "question":"What is the employee getting?","answer":["He","is","getting","an","envelope."],"answerVoice":"male",
 "notes":"The packet calls the boss 'his', but the picture shows a grey-haired woman -> target 'the woman', female voice. Many cuts: 0.5 s (a shoe), 1.0, 2.0, 3.0, 3.5 show no person -> off. At 6.0-6.5 s only the boss's hand is in the picture -> woman off. The co-worker with no hair (2.5, 8.5, 9.0 s) has no phrase (everything he does, the employee does too) and no box. 'to put on a jacket' is seen only at 9.5-10.0 s. Keyboard at 0.0 s is cut by the picture edge."}
json.dump(c,open("content/265.json","w"),indent=1)

# ---------- 266
ww={0.0:(.06,.31,.85,.53),0.5:(.11,.06,.80,.78),1.0:(.11,.23,.78,.77),1.5:(.04,.36,.85,.58),2.0:(.06,.07,.83,.90),
    2.5:(.11,.22,.83,.78),3.0:(.11,0,.58,.82),3.5:(.20,0,.47,.64),4.0:(.31,.11,.38,.61),4.5:(.36,.16,.35,.52),
    5.0:(.33,.21,.29,.46),5.5:(.36,.20,.34,.54),6.0:(.26,.11,.48,.54),6.5:(.41,.07,.41,.59),7.0:(.22,.13,.56,.34),
    7.5:(.14,.06,.65,.39),8.0:(.36,.26,.26,.70),8.5:(.21,.20,.41,.71),9.0:(.32,.14,.38,.78),9.5:(.29,.13,.49,.87),
    10.0:(.30,.08,.52,.92)}
mn={6.0:(0,.24,.24,.24),6.5:(.18,.37,.23,.22),7.0:(.25,.47,.18,.24),7.5:(.34,.45,.18,.26),8.0:(.62,.42,.18,.26),
    8.5:(.66,.40,.26,.30),9.0:(.82,.38,.18,.30),9.5:(.82,.43,.18,.29),10.0:(.82,.44,.18,.34)}
kw=keys(t,ww); km=keys(t,mn)
c={"mediaId":266,"level":"A","keyWord":"energy","defaultVoice":"female",
 "taps":[{"phrase":"to run up the steps","target":"the woman in white","voice":"female","keys":kw},
         {"phrase":"to jump up and down","target":"the woman in white","voice":"female","keys":kw},
         {"phrase":"to hold his knees","target":"the man","voice":"male","keys":km}],
 "stillS":4.0,
 "nouns":[{"word":"steps","x":.50,"y":.78,"voice":"female"},{"word":"a street lamp","x":.18,"y":.18,"voice":"female"},
          {"word":"a wall","x":.13,"y":.36,"voice":"female"},{"word":"the sky","x":.62,"y":.07,"voice":"female"}],
 "question":"What is the woman in white doing?","answer":["She","is","running","up","the","steps."],"answerVoice":"female",
 "notes":"'the man' = the man bent over with his hands on his knees behind her (6.0-10.0 s); the other people (edges at 0-2.5 s, the group on the steps at 3.5-5.5 s, the woman in black at 8.5-10 s) have no box. The woman in black also rests on her knees, 'his' is what makes the phrase fit only the man. At 6.5-8.0 s the man stands behind / under the jumping woman: her box is cut so the two do not overlap (7.0 and 7.5 s: only her upper body). 'to run up the steps' is seen at 3.0-4.5 s; at 5.0-5.5 s she runs down."}
json.dump(c,open("content/266.json","w"),indent=1)
