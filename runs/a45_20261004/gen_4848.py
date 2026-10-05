import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
hands={0.0:(0,.2,.68,.4),0.5:(0,.3,.75,.4),1.0:(0,.23,.73,.5),1.5:(0,.21,.78,.54)}
can={2.0:(0,0,.47,.32),2.5:(0,0,.38,.32),3.0:(0,0,.32,.38)}
woman={3.5:(.48,.02,.52,.8),4.0:(.56,.02,.44,.78),4.5:(.62,.28,.38,.4),5.0:(.48,0,.52,.66),5.5:(.6,.25,.4,.75),6.0:(.82,.42,.18,.24),
 6.5:(.08,0,.7,.72),7.0:(0,.18,.85,.72),7.5:(0,0,.97,.8),8.0:(0,.05,.98,.75),8.5:(0,0,1,.95),9.0:(0,.08,.95,.92),9.5:(.06,.17,.88,.83),10.0:(.14,.2,.72,.8)}
c={"mediaId":4848,"level":"A","keyWord":"grow","defaultVoice":"female",
"taps":[
 {"phrase":"to press down the soil","target":"the hands at the pot","voice":"female","keys":keys(hands)},
 {"phrase":"to pour water on flowers","target":"the watering can","voice":"female","keys":keys(can)},
 {"phrase":"to carry a big pumpkin","target":"the woman","voice":"female","keys":keys(woman)}],
"stillS":9.5,
"nouns":[{"word":"the sky","x":0.5,"y":0.07,"voice":"female"},
 {"word":"a woman","x":0.22,"y":0.48,"voice":"female"},
 {"word":"a pumpkin","x":0.73,"y":0.40,"voice":"female"},
 {"word":"leaves","x":0.4,"y":0.85,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","a","big","pumpkin."],
"answerVoice":"female",
"notes":"Main person = the curly-haired woman (digging 3.5-4 s, cutting the hedge 4.5-6 s with only her arms/hands visible, pumpkin 6.5-10 s); she is keyed in every shot where any part of her is visible. Shot 1 shows only gloved hands (gender unclear) -> 'the hands at the pot', default female voice. Watering can held by a person seen only in part; the can is the target. 'grow' (verb) not used as a noun."}
json.dump(c,open('content/4848.json','w'),indent=1)
