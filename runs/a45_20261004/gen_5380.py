import json
T=[i*0.5 for i in range(17)]
CY={0.0:(.23,.08,.77,.92),0.5:(.22,.08,.78,.92),1.0:(.11,.09,.87,.91)}
NU={1.5:(.32,.15,.68,.85),2.0:(.36,.18,.62,.82)}
YM={4.5:(.22,.14,.62,.56),5.0:(.16,.13,.58,.60),5.5:(.13,.13,.64,.60),6.0:(.06,.25,.84,.63),6.5:(.08,.16,.82,.66),
7.0:(.22,.15,.76,.70),7.5:(.33,.18,.67,.82),8.0:(.56,.19,.44,.78)}
def keys(B):
    return [{"t":t,"off":True} if t not in B else {"t":t,"x":B[t][0],"y":B[t][1],"w":B[t][2],"h":B[t][3]} for t in T]
c={"mediaId":5380,"level":"B","keyWord":"take","defaultVoice":"female",
"taps":[{"phrase":"to pull out a table lamp","target":"the cyclist","voice":"male","keys":keys(CY)},
{"phrase":"to grab a stack of books","target":"the nurse","voice":"female","keys":keys(NU)},
{"phrase":"to carry off the box","target":"the man with the backpack","voice":"male","keys":keys(YM)}],
"stillS":6.0,
"nouns":[{"word":"a white house","x":0.80,"y":0.18,"voice":"female"},{"word":"passers-by","x":0.75,"y":0.38,"voice":"female"},
{"word":"a cardboard box","x":0.50,"y":0.68,"voice":"female"},{"word":"a stone pillar","x":0.45,"y":0.92,"voice":"female"}],
"question":"What is the cyclist doing?",
"answer":["He","is","pulling","out","a","table","lamp."],"answerVoice":"male",
"notes":"The clip differs from the packet description: after the cyclist (0-1 s) a nurse in blue scrubs takes a stack of books (1.5-2 s), then the bearded man takes the football (2.5-3 s), the elderly woman the plant pot (3.5-4 s) and the young man with a backpack carries the box itself away (4.5-8 s). Bearded man and elderly woman are not used as targets. defaultVoice female: mixed group, evenId true. 'passers-by' = the small group of people on the far pavement at 6.0 s."}
json.dump(c,open('content/5380.json','w'),indent=1)
