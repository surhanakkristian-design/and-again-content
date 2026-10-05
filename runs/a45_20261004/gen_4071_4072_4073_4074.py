import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o):
    json.dump(o,open('content/%d.json'%o['mediaId'],'w'),indent=1,ensure_ascii=False)

# ---------- 4071
t=T(15)
W={0.0:(.33,.30,.27,.18),0.5:(.37,.33,.27,.16),1.0:(.28,.29,.44,.17),1.5:(.24,.28,.40,.23),2.0:(.24,.36,.24,.18),
   2.5:(.30,.62,.40,.24),3.0:(0,.62,.75,.24),3.5:(0,.63,.72,.17),4.0:(0,.58,.50,.21),4.5:(0,.56,.57,.19),
   5.0:(0,.53,.60,.20),5.5:(0,.49,.62,.18),6.0:(0,.47,.65,.21),6.5:(0,.46,.66,.24),7.0:(0,.45,.68,.16)}
S={0.0:(0,.48,.62,.29),0.5:(0,.49,.55,.30),1.0:(0,.46,.42,.42),1.5:(0,.29,.20,.30)}
save({"mediaId":4071,"level":"B","keyWord":"leap","defaultVoice":"female",
 "taps":[{"phrase":"to leap off a shipwreck","target":"the woman","voice":"female","keys":K(t,W)},
         {"phrase":"to glide beside a shark","target":"the woman","voice":"female","keys":K(t,W)},
         {"phrase":"to rust in shallow water","target":"the shipwreck","voice":"female","keys":K(t,S)}],
 "stillS":1.0,
 "nouns":[{"word":"a shipwreck","x":.16,"y":.62,"voice":"female"},{"word":"clouds","x":.40,"y":.15,"voice":"female"},
          {"word":"a boat","x":.88,"y":.69,"voice":"female"},{"word":"the sea","x":.50,"y":.88,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","leaping","off","a","rusty","shipwreck."],"answerVoice":"female",
 "notes":"Only two targets: the big tiger shark overlaps the woman from 5.5 s and a second shark does the same things, so no shark target. Woman box 2.5 s is on the bubble trail (she is inside it). Shipwreck gone after 1.5 s. The small boat at 1.0 s is at the right edge (pill x 0.88)."})

# ---------- 4072
t=T(22)
Wm={0.0:(.33,.52,.30,.19),0.5:(.33,.52,.30,.19),1.0:(.33,.53,.30,.18),1.5:(.34,.53,.29,.17),2.0:(.35,.51,.29,.16),
    2.5:(.36,.50,.28,.16),3.0:(.37,.49,.28,.16),3.5:(.38,.48,.27,.15),4.0:(.42,.47,.21,.14),4.5:(.43,.46,.20,.14),
    5.0:(.44,.45,.20,.14),5.5:(.44,.44,.20,.14),6.0:(.45,.41,.19,.14),6.5:(.45,.41,.19,.14),7.0:(.46,.41,.18,.14),
    7.5:(.46,.41,.18,.14),8.0:(.46,.41,.18,.14),8.5:(.46,.41,.18,.14),9.0:(.46,.43,.18,.14),9.5:(.46,.43,.18,.14),
    10.0:(.46,.41,.18,.14),10.5:(.46,.41,.18,.14)}
L={2.5:(0,.80,1,.20),3.0:(0,.80,1,.20),3.5:(0,.70,1,.30),4.0:(0,.66,1,.34),4.5:(0,.62,1,.38),5.0:(0,.60,1,.40),
   5.5:(0,.58,1,.42),6.0:(0,.56,1,.44),6.5:(0,.56,1,.44),7.0:(0,.56,1,.44),7.5:(0,.56,1,.44),8.0:(0,.55,1,.45),
   8.5:(0,.55,1,.45),9.0:(.10,.57,.90,.43),9.5:(.10,.57,.90,.43),10.0:(.10,.55,.90,.45),10.5:(.10,.55,.90,.45)}
P={0.0:(0,0,.52,.37),0.5:(0,0,.52,.37),1.0:(0,0,.55,.38),1.5:(.05,0,.53,.38),2.0:(.02,0,.57,.37),2.5:(.06,0,.54,.37),
   3.0:(.08,0,.52,.38),3.5:(.13,.02,.48,.37),4.0:(.16,.02,.43,.37),4.5:(.17,.04,.42,.35),5.0:(.21,.07,.38,.33),
   5.5:(.23,.09,.36,.31),6.0:(.26,.11,.33,.29),6.5:(.27,.12,.32,.28),7.0:(.28,.14,.31,.26),7.5:(.30,.17,.29,.23),
   8.0:(.31,.19,.28,.21),8.5:(.33,.21,.26,.19),9.0:(.34,.23,.25,.19),9.5:(.36,.24,.23,.18),10.0:(.36,.24,.23,.16),
   10.5:(.37,.24,.22,.16)}
save({"mediaId":4072,"level":"B","keyWord":"lagoon","defaultVoice":"female",
 "taps":[{"phrase":"to stroll towards the water","target":"the women","voice":"female","keys":K(t,Wm)},
         {"phrase":"to cover a coral reef","target":"the lagoon","voice":"female","keys":K(t,L)},
         {"phrase":"to lean over the sand","target":"the palm trees","voice":"female","keys":K(t,P)}],
 "stillS":8.0,
 "nouns":[{"word":"a lagoon","x":.50,"y":.74,"voice":"female"},{"word":"a beach","x":.42,"y":.44,"voice":"female"},
          {"word":"palm trees","x":.46,"y":.29,"voice":"female"},{"word":"a cliff","x":.13,"y":.53,"voice":"female"}],
 "question":"What lies between the cliffs?",
 "answer":["A","turquoise","lagoon","lies","between","the","cliffs."],"answerVoice":"female",
 "notes":"The three women walk as one group (one box, they get very small as the drone climbs). The lagoon box starts at 2.5 s when the water comes into the frame. 'to lean over the sand' is true mainly for the left palm. 'a cliff' is placed on the left wall; there is a second wall on the right (no other noun there). The women stand between the beach pill and the lagoon pill at 8.0 s."})

# ---------- 4073
t=T(28)
F=(0,0,1,1)
Pg={0.0:(0,.18,.90,.82),0.5:(.04,.17,.92,.83),1.0:(.01,.17,.95,.83),1.5:(.08,.03,.92,.97),2.0:F,
    4.5:(.33,.11,.67,.89),5.0:(.47,.11,.53,.89),5.5:(.46,.11,.54,.89),6.0:F,6.5:F,7.0:F,7.5:F,8.0:F,
    8.5:(0,.18,.56,.74),9.0:(0,.20,.67,.74),9.5:(0,.24,.72,.76),10.0:(0,.18,.69,.76),10.5:(0,.16,.67,.78),
    11.0:(0,.15,.64,.80),11.5:(0,.18,.64,.78),12.0:(0,.18,.62,.76),12.5:(.54,.16,.46,.84),13.0:(.56,.18,.44,.82),
    13.5:(.55,.22,.45,.78)}
H={2.5:(0,.02,1,.88),3.0:(0,.06,1,.84),3.5:(0,.06,1,.84),4.0:F,
   8.5:(.66,.29,.34,.60),9.0:(.68,.30,.32,.58),9.5:(.72,.30,.28,.54),10.0:(.69,.29,.31,.55),10.5:(.68,.29,.32,.54),
   11.0:(.67,.30,.33,.52),11.5:(.67,.30,.33,.54),12.0:(.66,.29,.34,.55)}
Wp={5.0:(0,.10,.47,.90),5.5:(0,.12,.46,.88),12.5:(0,.13,.54,.87),13.0:(0,.14,.56,.86),13.5:(0,.22,.55,.78)}
save({"mediaId":4073,"level":"B","keyWord":"stick","defaultVoice":"male",
 "taps":[{"phrase":"to cuddle a sleeping chick","target":"the blue pigeon","voice":"male","keys":K(t,Pg)},
         {"phrase":"to guard her three chicks","target":"the hen","voice":"male","keys":K(t,H)},
         {"phrase":"to spread a pale wing","target":"the white pigeon","voice":"male","keys":K(t,Wp)}],
 "stillS":2.5,
 "nouns":[{"word":"a stick","x":.24,"y":.46,"voice":"male"},{"word":"a beak","x":.54,"y":.36,"voice":"male"},
          {"word":"chicks","x":.50,"y":.82,"voice":"male"}],
 "question":"What is the hen doing?",
 "answer":["The","hen","is","threatening","the","pigeon","with","a","stick."],"answerVoice":"male",
 "notes":"Many cuts and close-ups. The stick is not boxed as part of the hen when she is out of the picture (1.5-2.0, 4.5-5.5, 7.5-8.0). In the close-ups 6.0-8.0 the whole frame is the blue pigeon (with the chick in its wing). Two pigeons side by side at 5.0-5.5 and 12.5-13.5 are split along a vertical line; at 13.0-13.5 the white pigeon's wing reaches across into the blue pigeon's half. The hen box at 2.5-3.5 includes the chicks under her (chicks are not a target). The blue pigeon also has a (dark grey) wing out at 6.0-9.5, hence 'pale'. Only 3 nouns; 'a beak' is the hen's beak."})

# ---------- 4074
t=T(31)
Wo={0.0:(0,.34,.82,.66),0.5:(0,.29,.82,.71),1.0:(0,.29,.80,.71),1.5:(0,.33,.80,.67),2.0:(0,.40,.46,.60),2.5:(0,.36,.29,.62)}
Su={0.0:(.82,.36,.18,.14),0.5:(.82,.35,.18,.15),1.0:(.82,.35,.18,.14),1.5:(.82,.36,.18,.15),2.0:(.70,.33,.30,.19),
    2.5:(.61,.34,.33,.17),3.0:(.49,.35,.29,.15),3.5:(.42,.35,.28,.15),4.0:(.38,.35,.28,.14),4.5:(.33,.35,.28,.14),
    5.0:(.28,.35,.28,.15),5.5:(.24,.35,.28,.15),6.0:(.20,.35,.28,.15)}
Ki={6.5:(.13,.25,.83,.37),7.0:(.15,.27,.81,.34),7.5:(.16,.29,.80,.33),8.0:(.15,.26,.79,.38),8.5:(.59,0,.28,.24),
    9.0:(.65,0,.27,.23),9.5:(.64,0,.29,.21),10.0:(.65,0,.24,.17),10.5:(.68,0,.26,.14),11.0:(.34,.20,.18,.15),
    11.5:(.35,.20,.18,.14),12.0:(.35,.20,.18,.14),12.5:(.36,.19,.18,.14),13.0:(.36,.19,.18,.14)}
save({"mediaId":4074,"level":"A","keyWord":"sun","defaultVoice":"female",
 "taps":[{"phrase":"to laugh in the water","target":"the woman","voice":"female","keys":K(t,Wo)},
         {"phrase":"to go down behind a hill","target":"the sun","voice":"female","keys":K(t,Su)},
         {"phrase":"to fly in the sky","target":"the red kites","voice":"female","keys":K(t,Ki)}],
 "stillS":4.5,
 "nouns":[{"word":"the sun","x":.47,"y":.43,"voice":"female"},{"word":"a boat","x":.88,"y":.47,"voice":"female"},
          {"word":"water","x":.50,"y":.75,"voice":"female"},{"word":"the sky","x":.50,"y":.15,"voice":"female"}],
 "question":"What is the sun doing?",
 "answer":["The","sun","is","going","down","behind","a","hill."],"answerVoice":"female",
 "notes":"Six shots. The sun is at the right edge behind the woman at 0.0-1.5 (small box, split from the woman's box at x 0.82). The last shot (13.5-15.0) is the MOON behind wind turbines, not the sun: sun box off there. 'the red kites' = two kites at 6.5-8.0, then the one kite of the man (8.5-13.0). The man on the water is not a target; no target is boxed in the moon shot. The 'hill' is a sand dune. Sun pill and boat pill are 0.40 apart in x."})
