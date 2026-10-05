import json, sys
HERE='/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004'
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
def write(c):
    json.dump(c,open(f"{HERE}/content/{c['mediaId']}.json",'w'),indent=1,ensure_ascii=False)
V={}
# ---- 4892
man={0.0:(.36,.67,.62,.33),0.5:(.31,.67,.55,.33),1.0:(.15,.64,.60,.36),1.5:(.08,.58,.62,.42),
     2.0:(.0,.62,.80,.38),2.5:(.20,.61,.58,.39),3.0:(.25,.49,.75,.51),3.5:(.18,.52,.82,.48),
     4.0:(.28,.48,.72,.52),4.5:(.23,.70,.55,.30),5.0:(.23,.69,.54,.31),5.5:(.28,.58,.54,.42)}
k=keys(man)
V[4892]={"mediaId":4892,"level":"A","keyWord":"shorts","defaultVoice":"male",
 "taps":[{"phrase":"to wear colourful shorts","target":"the man","voice":"male","keys":k},
         {"phrase":"to smile at the camera","target":"the man","voice":"male","keys":k},
         {"phrase":"to hold the camera","target":"the man","voice":"male","keys":k}],
 "stillS":2.5,
 "nouns":[{"word":"the sky","x":.60,"y":.12,"voice":"male"},{"word":"a palm tree","x":.20,"y":.32,"voice":"male"},
          {"word":"feet","x":.55,"y":.66,"voice":"male"},{"word":"shorts","x":.55,"y":.93,"voice":"male"}],
 "question":"What is the man wearing?","answer":["He","is","wearing","colourful","shorts."],"answerVoice":"male",
 "notes":"Only one clear target: the rider (POV legs 0-2.5 and 4.5-5.5, selfie 3.0-4.0). Final tower shot 6.0-9.0 marked off: the rider cannot be identified among the other sliders and swimmers, and other people there also slide, so phrases avoid 'go down a slide'."}

# ---- 4893
nw=keys({0.0:(.0,.15,.98,.85),0.5:(.0,.16,.95,.84),1.0:(.0,.22,.52,.78)})
gm=keys({2.0:(.64,.27,.36,.73),2.5:(.20,.27,.62,.73),3.0:(.0,.27,.46,.73),3.5:(.0,.45,.30,.55)})
V[4893]={"mediaId":4893,"level":"B","keyWord":"crowded","defaultVoice":"female",
 "taps":[{"phrase":"to gaze into the camera","target":"the woman in the navy T-shirt","voice":"female","keys":nw},
         {"phrase":"to wear a car-print T-shirt","target":"the woman in the navy T-shirt","voice":"female","keys":nw},
         {"phrase":"to sport a green jersey","target":"the man in the green jersey","voice":"male","keys":gm}],
 "stillS":7.0,
 "nouns":[{"word":"the upper tier","x":.50,"y":.06,"voice":"female"},
          {"word":"spectators","x":.55,"y":.62,"voice":"female"},{"word":"a railing","x":.40,"y":.91,"voice":"female"}],
 "question":"How full is the stadium?","answer":["The","stadium","is","crowded","with","spectators."],"answerVoice":"female",
 "notes":"Camera tracks past many fans; few unique targets. Pinstriped jersey avoided (the woman at 1.5-2.5 and a man in a white 'Dayton' jersey both wear pinstripes); cups, caps, glasses and smiles are shared by many fans. Woman in navy T-shirt (red-car print) only 0.0-1.0; green jersey man 2.0-3.5 (only a sliver at 3.5)."}

# ---- 4894
by=keys({2.0:(.42,.0,.32,.67),2.5:(.40,.0,.32,.69),3.0:(.38,.10,.30,.65),3.5:(.38,.21,.30,.55),4.0:(.38,.29,.27,.51),
  4.5:(.38,.37,.25,.46),5.0:(.38,.43,.22,.42),5.5:(.38,.46,.24,.41),6.0:(.40,.50,.20,.35),6.5:(.41,.51,.18,.33),
  7.0:(.41,.51,.18,.30),7.5:(.41,.52,.18,.25),8.0:(.41,.51,.18,.23),8.5:(.41,.51,.18,.19),9.0:(.41,.52,.18,.16)})
hp=keys({3.5:(.38,.0,.20,.14),4.0:(.37,.0,.22,.17),4.5:(.37,.0,.22,.22),5.0:(.37,.0,.20,.27),5.5:(.37,.0,.22,.31),
  6.0:(.37,.03,.21,.31),6.5:(.37,.04,.22,.32),7.0:(.37,.09,.21,.29),7.5:(.38,.12,.20,.28),8.0:(.40,.19,.18,.23),
  8.5:(.40,.22,.18,.20),9.0:(.40,.26,.18,.17)})
V[4894]={"mediaId":4894,"level":"A","keyWord":"still","defaultVoice":"male",
 "taps":[{"phrase":"to stand at the front","target":"the boy at the front","voice":"male","keys":by},
         {"phrase":"to stand in the middle","target":"the boy at the front","voice":"male","keys":by},
         {"phrase":"to hang above the doors","target":"the basketball hoop","voice":"male","keys":hp}],
 "stillS":6.0,
 "nouns":[{"word":"lights","x":.50,"y":.05,"voice":"male"},{"word":"a basketball hoop","x":.47,"y":.30,"voice":"male"},
          {"word":"students","x":.75,"y":.50,"voice":"male"},{"word":"the floor","x":.50,"y":.88,"voice":"male"}],
 "question":"What are the students doing?","answer":["They","are","standing","very","still."],"answerVoice":"male",
 "notes":"Only one person is trackable: the boy in the grey T-shirt at the front centre (from 2.0; 0.0-1.5 show students walking, he cannot be identified - off). Many students wear grey T-shirts, so he is named by position. 'to stand in the middle' and 'to stand at the front' both fit only him. Hoop is off at 0-3.0 (not / barely in frame); side hoops appear at the edges from ~6.5 but only the centre one hangs above the doors."}

# ---- 4895
bm=keys({0.0:(.03,.52,.47,.48),0.5:(.03,.52,.47,.48),1.0:(.0,.53,.50,.47),1.5:(.0,.54,.52,.46),2.0:(.0,.56,.37,.44),2.5:(.0,.59,.22,.41)})
wc=keys({0.0:(.50,.47,.20,.42),0.5:(.50,.47,.20,.42),1.0:(.50,.52,.22,.40),1.5:(.53,.54,.27,.46),2.0:(.65,.51,.35,.40),2.5:(.77,.54,.23,.46)})
om=keys({0.0:(.70,.63,.30,.37),0.5:(.70,.63,.30,.37),1.0:(.72,.64,.28,.36),1.5:(.80,.66,.20,.34)})
V[4895]={"mediaId":4895,"level":"A","keyWord":"opposite","defaultVoice":"male",
 "taps":[{"phrase":"to carry a backpack","target":"the man with the backpack","voice":"male","keys":bm},
         {"phrase":"to wear a hair clip","target":"the woman with the hair clip","voice":"female","keys":wc},
         {"phrase":"to have grey hair","target":"the older man","voice":"male","keys":om}],
 "stillS":7.0,
 "nouns":[{"word":"the sky","x":.50,"y":.12,"voice":"male"},{"word":"a glass building","x":.80,"y":.34,"voice":"male"},
          {"word":"the ground","x":.50,"y":.80,"voice":"male"}],
 "question":"Where are the people standing?","answer":["They","are","standing","opposite","each","other."],"answerVoice":"male",
 "notes":"Targets only identifiable in the close crowd shot 0.0-2.5; from 3.0 the camera rises over identical lines and no single person can be tracked (all off). The three targets overlap at 0.0-1.5: boxes split along the lines between them (backpack man left of x .50, woman with the hair clip middle, older man right/below); older man off at 2.0 (only a corner of his head). Only 3 nouns: people/trees/street lamps appear on both sides, so they were left out. 'each other' answer: 'They are standing opposite each other.'"}
for i in map(int,sys.argv[1:]): write(V[i])
