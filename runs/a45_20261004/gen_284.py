import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
purple={1.5:(0,0,.78,1),2.0:(0,0,1,1),2.5:(0,0,1,1),3.0:(0,.06,.48,.94),3.5:(0,.08,.30,.92),4.0:(0,.08,.36,.92),4.5:(0,.11,.43,.89),
5.0:(0,.15,.45,.85),5.5:(0,.15,.43,.85),6.0:(0,.13,.45,.87),6.5:(0,.13,.45,.87),7.0:(0,.15,.45,.85),7.5:(0,.15,.43,.85),8.0:(0,.13,.45,.87),
8.5:(0,.13,.43,.87),9.0:(0,.15,.41,.85),9.5:(0,.15,.54,.85),10.0:(0,.15,.40,.85)}
grey={1.0:(.12,0,.88,1),1.5:(.80,0,.20,1),3.0:(.50,.03,.50,.97),3.5:(.54,.06,.46,.94),4.0:(.59,.08,.41,.80),4.5:(.65,.10,.35,.78),
5.0:(.66,.14,.34,.78),5.5:(.66,.14,.34,.76),6.0:(.66,.12,.34,.78),6.5:(.66,.12,.34,.78),7.0:(.66,.14,.34,.78),7.5:(.66,.14,.34,.76),8.0:(.66,.12,.34,.78),
8.5:(.63,.12,.37,.78),9.0:(.63,.14,.37,.80),9.5:(.56,.12,.44,.80),10.0:(.63,.12,.37,.70)}
dog={3.5:(.31,.34,.22,.14),4.0:(.37,.33,.21,.14),4.5:(.44,.33,.20,.14),5.0:(.46,.34,.19,.14),5.5:(.45,.34,.20,.14),6.0:(.46,.33,.19,.14),
6.5:(.46,.33,.19,.14),7.0:(.46,.33,.19,.14),7.5:(.45,.33,.20,.14),8.0:(.46,.33,.19,.14),8.5:(.44,.31,.19,.14),9.0:(.42,.34,.20,.14),10.0:(.41,.34,.21,.14)}
c={"mediaId":284,"level":"B","keyWord":"face mask","defaultVoice":"female",
"taps":[
 {"phrase":"to wear a fluffy headband","target":"the woman in purple","voice":"female","keys":keys(purple)},
 {"phrase":"to point at her friend","target":"the woman in grey","voice":"female","keys":keys(grey)},
 {"phrase":"to rest on a cushion","target":"the dog","voice":"female","keys":keys(dog)}],
"stillS":6.0,
"nouns":[{"word":"a headband","x":.18,"y":.20,"voice":"female"},{"word":"a face mask","x":.77,"y":.34,"voice":"female"},
 {"word":"a dog","x":.54,"y":.43,"voice":"female"},{"word":"a bowl","x":.61,"y":.84,"voice":"female"}],
"question":"What are the women wearing?",
"answer":["They","are","wearing","green","face","masks."],
"answerVoice":"female",
"notes":"The dog lies between the two women, so the women's boxes are cut at the dog's column: the grey woman's left arm and (at 8.5-9.0) her pointing hand lie partly outside her box, the purple woman's right shoulder at 3.5-4.0 too. 'to wear a fluffy headband' is a state (she has no action of her own that the other does not share: both laugh and clap). Pointing is visible only at 8.5-9.0. At 1.0 the grey woman is a faceless torso holding the spatula. 'a face mask' pill is on the grey woman's face (both wear one; no other noun sits on the other face)."}
json.dump(c,open('content/284.json','w'),indent=1)
