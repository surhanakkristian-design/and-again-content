import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0,0,0.78,0.8),0.5:(0,0,0.83,0.84),1.0:(0,0,0.75,0.93),1.5:(0,0,0.8,1.0),2.0:(0,0,0.92,1.0),
2.5:(0,0.22,1,0.65),3.0:(0,0.08,1,0.85),3.5:(0,0.08,1,0.85),4.0:(0,0.08,1,0.86),4.5:(0,0,1,0.76),
6.5:(0.63,0,0.37,0.38),7.0:(0.62,0,0.38,0.5),7.5:(0.61,0,0.39,0.46),8.0:(0.56,0,0.44,0.46),8.5:(0.48,0,0.52,0.36),
9.0:(0.47,0,0.53,0.35),9.5:(0.45,0,0.55,0.25),10.0:(0.4,0,0.42,0.22)}
woman={6.0:(0,0,1,0.66),6.5:(0,0,0.6,0.5),7.0:(0,0.03,0.61,0.62),7.5:(0,0,0.6,0.46),8.0:(0,0,0.55,0.46),8.5:(0,0,0.45,0.4),
9.0:(0,0,0.4,0.35),9.5:(0,0,0.4,0.24),10.0:(0,0,0.3,0.22)}
wave={8.5:(0.58,0.37,0.42,0.63),9.0:(0.2,0.36,0.8,0.64),9.5:(0,0.27,1,0.73),10.0:(0,0.23,1,0.77)}
c={"mediaId":634,"level":"A","keyWord":"sand","defaultVoice":"male",
"taps":[{"phrase":"to pour dry sand","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to draw with a stick","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to cover the drawing","target":"the wave","voice":"male","keys":keys(wave)}],
"stillS":8.5,
"nouns":[{"word":"a woman","x":0.2,"y":0.15,"voice":"female"},{"word":"a man","x":0.76,"y":0.15,"voice":"male"},
{"word":"a wave","x":0.84,"y":0.43,"voice":"male"},{"word":"sand","x":0.33,"y":0.86,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","pouring","sand","into","his","hand."],"answerVoice":"male",
"notes":"2.5-4.5 s: close-up of two hands holding sand with pebbles, boxed as the man (description says so; not provable from the picture). 5.0-5.5 s: only bare feet, owners unclear -> both people off. 6.0 s: the woman's body and arm with the stick fill the frame, the foot at the right edge is left unboxed. Wave boxed from 8.5 s (at 8.0 only a sliver at the edge)."}
json.dump(c,open('content/634.json','w'),ensure_ascii=False,indent=1)
