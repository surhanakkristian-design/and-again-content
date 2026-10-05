import json
T=[i*0.5 for i in range(25)]
B={0.0:(.17,0,.70,.86),0.5:(.10,0,.82,.72),1.0:(.06,0,.90,.70),1.5:(.08,0,.75,.76),2.0:(.18,0,.52,.88),2.5:(.19,.01,.53,.96),
3.0:(.19,.06,.51,.94),3.5:(.17,.08,.56,.92),4.0:(0,0,.58,.33),4.5:(0,0,.66,.50),5.0:(0,0,.66,.50),5.5:(0,0,.75,.60),
6.0:(0,0,1,.72),6.5:(0,0,1,.72),7.0:(0,0,1,.73),7.5:(.26,.12,.38,.54),8.0:(.26,.14,.40,.54),8.5:(.24,.15,.44,.55),
9.0:(.22,.14,.46,.63),9.5:(.23,.13,.50,.70),10.0:(.23,.11,.54,.78),10.5:(.24,.09,.56,.84),11.0:(.24,.09,.50,.89),
11.5:(.23,.13,.52,.86),12.0:(.23,.10,.54,.89)}
def keys(b):
    out=[]
    for t in T:
        v=b.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W=keys(B)
c={"mediaId":5294,"level":"A","keyWord":"slippers","defaultVoice":"female",
"taps":[{"phrase":"to hug herself","target":"the woman","voice":"female","keys":W},
{"phrase":"to walk down the hall","target":"the woman","voice":"female","keys":W},
{"phrase":"to smile at the camera","target":"the woman","voice":"female","keys":W}],
"stillS":11.0,
"nouns":[{"word":"a woman","x":0.44,"y":0.33,"voice":"female"},{"word":"slippers","x":0.44,"y":0.84,"voice":"female"},
{"word":"a door","x":0.86,"y":0.45,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","walking","in","her","slippers."],"answerVoice":"female",
"notes":"Only one person, so all three phrases use the woman. 4.0-7.0 close-up: only her legs/feet (and the slippers she steps into) are visible; box covers legs, from 6.0 also the slippers she wears. 'to hug herself' at 2.0-3.5; 'to walk down the hall' 7.5-11.0; 'to smile at the camera' 8.0-12.0."}
json.dump(c,open('content/5294.json','w'),indent=1)
