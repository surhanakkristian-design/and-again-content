import json
T=lambda n:[round(i*0.5,1) for i in range(n)]
def keys(times,d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def dump(o):
    json.dump(o,open("content/%d.json"%o["mediaId"],"w"),ensure_ascii=False,indent=1)

# ---------- 4529
t=T(19)
W={0.5:(.20,.33,.62,.67),1.0:(0,.32,1,.68),1.5:(0,.27,1,.73),2.0:(0,.25,1,.75),
2.5:(.28,.35,.33,.65),3.0:(.19,.31,.40,.69),3.5:(.08,.26,.54,.74),4.0:(.13,.21,.49,.79),4.5:(.07,.16,.71,.84),5.0:(.02,.11,.77,.89),
5.5:(.30,0,.32,.26),6.0:(.33,.11,.32,.48),6.5:(.28,.29,.38,.55),7.0:(.23,.48,.43,.52),7.5:(.24,.50,.48,.50),
8.0:(.24,.34,.55,.66),8.5:(.24,.34,.62,.66),9.0:(.24,.36,.60,.64)}
C={2.5:(.62,.37,.38,.29),3.0:(.60,.36,.40,.32),3.5:(.63,.33,.37,.37),4.0:(.63,.28,.37,.46),4.5:(.79,.52,.21,.28),5.0:(.80,.57,.20,.39)}
kw=keys(t,W)
dump({"mediaId":4529,"level":"A","keyWord":"color","defaultVoice":"female",
"taps":[{"phrase":"to open the doors","target":"the woman","voice":"female","keys":kw},
{"phrase":"to light a candle","target":"the woman","voice":"female","keys":kw},
{"phrase":"to burn on the stand","target":"the candles","voice":"female","keys":keys(t,C)}],
"stillS":9.0,
"nouns":[{"word":"windows","x":.72,"y":.25,"voice":"female"},{"word":"a candle","x":.74,"y":.63,"voice":"female"},
{"word":"a dress","x":.50,"y":.90,"voice":"female"},{"word":"colors","x":.20,"y":.80,"voice":"female"}],
"question":"What is the woman looking at?",
"answer":["She","is","looking","up","at","the","windows."],"answerVoice":"female",
"notes":"Target 'the candles' = the burning candles on the iron stand (2.5-5.0 s); at 4.5/5.0 s only the right-hand pair is boxed because the candle she is lighting sits inside her hands/box. She also carries a small burning candle from 6.0 s (phrase says 'on the stand'). 'colors' pill sits on the coloured light on the floor; 'a candle' pill on the small candle in her hands."})

# ---------- 4531
W={0.0:(.20,.23,.52,.45),0.5:(.14,.20,.68,.50),1.5:(.05,.20,.66,.80),2.0:(0,.20,.98,.80),2.5:(0,.18,1,.82),3.0:(0,.22,.96,.78),
3.5:(0,.23,1,.77),4.0:(0,.21,.97,.79),4.5:(0,.26,1,.74),6.0:(.15,.55,.72,.45),6.5:(.24,.43,.56,.57),7.0:(.16,.42,.68,.58),
7.5:(.16,.40,.73,.60),8.0:(.14,.37,.78,.63),8.5:(.08,.36,.88,.64),9.0:(.06,.34,.90,.66)}
kw=keys(t,W)
dump({"mediaId":4531,"level":"A","keyWord":"popcorn","defaultVoice":"female",
"taps":[{"phrase":"to show her ticket","target":"the woman","voice":"female","keys":kw},
{"phrase":"to carry the popcorn","target":"the woman","voice":"female","keys":kw},
{"phrase":"to smile at the camera","target":"the woman","voice":"female","keys":kw}],
"stillS":7.0,
"nouns":[{"word":"a screen","x":.50,"y":.38,"voice":"female"},{"word":"a T-shirt","x":.30,"y":.64,"voice":"female"},
{"word":"popcorn","x":.55,"y":.73,"voice":"female"},{"word":"a seat","x":.86,"y":.62,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","carrying","popcorn","to","her","seat."],"answerVoice":"female",
"notes":"Only one clear target (the woman filming herself); all three phrases use her. 1.0 s shows only hands and the ticket, 5.0/5.5 s only the dark cinema: off. At 6.0 s she is a dark silhouette at the bottom (box kept). The employee's hand at 0.0/0.5 s is not a target."})

# ---------- 4532
t=T(21)
W={0.0:(0,.10,.88,.64),0.5:(0,.10,.92,.64),1.0:(0,.10,.94,.76),1.5:(0,.10,.94,.76),2.0:(0,.10,.95,.70),
2.5:(0,.18,.46,.70),3.0:(0,.13,.40,.85),3.5:(0,.16,.46,.84),4.0:(0,.14,.42,.82),
4.5:(0,.09,1,.91),5.0:(0,.10,1,.90),5.5:(0,.10,1,.90),6.0:(0,.10,1,.90),6.5:(0,.10,1,.90),7.0:(0,.15,1,.85),7.5:(0,.22,1,.78),
8.0:(0,.28,.93,.72),8.5:(0,.39,.82,.61),9.0:(.02,.41,.72,.59),9.5:(.04,.44,.62,.56),10.0:(.09,.46,.55,.54)}
kw=keys(t,W)
dump({"mediaId":4532,"level":"B","keyWord":"trash","defaultVoice":"female",
"taps":[{"phrase":"to cast her ballot","target":"the woman in the headwrap","voice":"female","keys":kw},
{"phrase":"to use a litter picker","target":"the woman in the headwrap","voice":"female","keys":kw},
{"phrase":"to clutch her passport","target":"the woman in the headwrap","voice":"female","keys":kw}],
"stillS":4.0,
"nouns":[{"word":"a headwrap","x":.28,"y":.23,"voice":"female"},{"word":"a cardigan","x":.48,"y":.38,"voice":"female"},
{"word":"a litter picker","x":.42,"y":.60,"voice":"female"},{"word":"trash","x":.78,"y":.85,"voice":"female"}],
"question":"What are the three women collecting?",
"answer":["They","are","collecting","trash","in","the","park."],"answerVoice":"female",
"notes":"All three phrases use the main woman (she alone does each action in its scene; the other women only hold bags / sit in the background, nothing unique at B level). Park scene 2.5-4.0 s: her box holds her body, not the whole length of the litter picker. 'trash' pill sits on the rubbish inside the translucent bag; 'a cardigan' = the orange cardigan of the woman at the back."})

# ---------- 4534
t=T(25)
W={0.0:(.52,.30,.40,.70),0.5:(.54,.30,.40,.70),1.0:(.50,.30,.42,.70),1.5:(.50,.30,.42,.70),2.0:(.46,.29,.44,.71),2.5:(.46,.26,.46,.74),
3.0:(.43,.26,.51,.74),3.5:(.46,.22,.54,.78),4.0:(.70,.26,.30,.74),
6.5:(.74,.21,.26,.79),7.0:(.47,.26,.23,.74),
8.0:(.06,.14,.71,.86),8.5:(.04,.13,.61,.87),9.0:(0,.10,.92,.90),9.5:(0,.11,.94,.89),10.0:(0,.13,.98,.87),10.5:(0,.08,1,.92),
11.0:(0,.06,1,.94),11.5:(.08,.06,.92,.94),12.0:(.17,.18,.70,.82)}
O={5.5:(0,.08,.66,.92),6.0:(0,.08,.78,.92),6.5:(0,.06,.56,.94),7.0:(0,.06,.46,.94),7.5:(0,.06,.78,.94),
8.0:(.78,.72,.22,.26),8.5:(.66,.70,.34,.30)}
kw=keys(t,W)
dump({"mediaId":4534,"level":"B","keyWord":"official","defaultVoice":"female",
"taps":[{"phrase":"to hand over a certificate","target":"the official","voice":"male","keys":keys(t,O)},
{"phrase":"to weep with joy","target":"the woman in yellow","voice":"female","keys":kw},
{"phrase":"to clutch her certificate","target":"the woman in yellow","voice":"female","keys":kw}],
"stillS":6.0,
"nouns":[{"word":"an official","x":.22,"y":.22,"voice":"male"},{"word":"windows","x":.68,"y":.10,"voice":"female"},
{"word":"a certificate","x":.48,"y":.61,"voice":"female"},{"word":"a handshake","x":.68,"y":.75,"voice":"female"}],
"question":"What is the official doing?",
"answer":["He","is","handing","a","certificate","to","the","woman."],"answerVoice":"male",
"notes":"The official = the man in the dark suit with the chain of office. The small figure at the lectern at the far left edge (0.0-1.0 s) cannot be identified as him: off. At 8.0/8.5 s only his hand and sleeve are in the picture (box on the hand giving the certificate). The woman in yellow is mostly hidden at 7.5 s (off) and half hidden behind the dark-haired woman at 7.0 s."})
