import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
W={0.0:(.43,.33,.27,.67),0.5:(.45,.33,.27,.67),1.0:(.41,.34,.30,.66),1.5:(.42,.33,.38,.67),2.0:(.34,.33,.34,.67),
   2.5:(.28,.33,.43,.67),3.0:(0,.52,.18,.48),7.0:(0,.37,.45,.63),7.5:(.37,.37,.42,.63),8.0:(.21,.27,.68,.50),
   8.5:(.27,.33,.40,.50),9.0:(.13,.30,.77,.55),9.5:(0,.30,1,.55),10.0:(.03,.28,.90,.57)}
B={0.0:(.17,.43,.25,.45),0.5:(.17,.44,.28,.42),1.0:(.10,.50,.31,.46),1.5:(.09,.53,.33,.45),2.0:(.01,.48,.33,.47),
   2.5:(0,.48,.28,.52),7.5:(.16,.74,.20,.26),8.0:(.15,.78,.27,.22),8.5:(.13,.84,.24,.16),9.0:(.12,.86,.24,.14),
   9.5:(.13,.86,.22,.14),10.0:(.12,.86,.24,.14)}
c={"mediaId":356,"level":"A","keyWord":"gym","defaultVoice":"female",
 "taps":[{"phrase":"to carry a big bag","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to look around the gym","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to hang from her shoulder","target":"the bag","voice":"female","keys":keys(B)}],
 "stillS":8.0,
 "nouns":[{"word":"the ceiling","x":.50,"y":.10,"voice":"female"},{"word":"weights","x":.80,"y":.53,"voice":"female"},
  {"word":"a T-shirt","x":.52,"y":.62,"voice":"female"},{"word":"a bag","x":.28,"y":.84,"voice":"female"}],
 "question":"What is the woman carrying?","answer":["She","is","carrying","a","bag","into","the","gym."],"answerVoice":"female",
 "notes":"Only two usable targets: the runners and other gym users are small, several and all do the same, the man at the cable machine is in one frame only. So the woman has two phrases. The bag hangs on her back 0.0-2.5: the box is split on a vertical line, bag left, woman right (her head sits a little over the line at 2.0-2.5). From 7.5 the bag stands on the floor at her feet; the woman's box then stops above the bag, so her lower legs are outside. The hand on the weights (4.0-5.0) is not boxed. 3.0 is only the edge of her T-shirt."}
json.dump(c,open('content/356.json','w'),indent=1)
