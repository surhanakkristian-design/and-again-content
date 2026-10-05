import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
f={0.0:(0,0,1,.88),0.5:(0,0,1,.80),1.0:(0,0,.97,.90),1.5:(0,0,1,.88),2.0:(0,0,1,.78),2.5:(0,0,1,.72),
   3.0:(.33,.12,.56,.63),3.5:(.27,.17,.58,.58),4.0:(.22,.30,.48,.34),4.5:(.25,.29,.63,.47),5.0:(.30,.15,.58,.60),
   5.5:(.26,.11,.69,.64),6.0:(.35,.29,.57,.29),6.5:(.20,.27,.64,.33),7.0:(.27,.27,.53,.33),7.5:(.25,.27,.52,.33),
   8.0:(.27,.27,.50,.34),8.5:(.25,.26,.75,.36),9.0:(.22,.26,.78,.38)}
cart={6.0:(0,.58,.88,.42),6.5:(0,.60,.90,.40),7.0:(0,.60,.88,.40),7.5:(0,.60,.86,.40),8.0:(0,.61,.86,.39),8.5:(0,.62,.88,.38),9.0:(0,.64,.85,.36)}
c={"mediaId":4726,"level":"A","keyWord":"farmer","defaultVoice":"male",
 "taps":[
  {"phrase":"to pull out carrots","target":"the farmer","voice":"male","keys":keys(f)},
  {"phrase":"to carry a wooden box","target":"the farmer","voice":"male","keys":keys(f)},
  {"phrase":"to have a big wheel","target":"the cart","voice":"male","keys":keys(cart)}],
 "stillS":7.5,
 "nouns":[{"word":"a farmer","x":.50,"y":.38,"voice":"male"},{"word":"carrots","x":.38,"y":.51,"voice":"male"},
          {"word":"sunflowers","x":.82,"y":.47,"voice":"male"},{"word":"a wheel","x":.68,"y":.90,"voice":"male"}],
 "question":"What is the farmer carrying?",
 "answer":["He","is","carrying","a","box","of","carrots."],
 "answerVoice":"male",
 "notes":"Two targets: the farmer (pulls carrots 0-2.5 s, carries the box 4.5-6.0 s) and the cart in the last shot ('to have a big wheel' is a state - the cart does nothing). The hens (3.0-5.5 s) were not used as a target: they overlap the farmer almost completely and are not clearly doing one thing. In the last shot the farmer box ends at the top rail of the cart; the box with carrots lying on the cart falls partly in his box. 0-2.5 s are close-ups, so his box is nearly the whole picture (cap/face only at 0 s)."}
json.dump(c,open('content/4726.json','w'),indent=1,ensure_ascii=False)
