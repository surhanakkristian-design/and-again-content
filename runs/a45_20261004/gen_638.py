import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0,0,0.5,0.6),0.5:(0,0,0.49,0.62),1.0:(0,0,0.46,0.74),1.5:(0,0,0.42,0.75),2.0:(0,0,0.42,0.72),2.5:(0,0,0.33,0.72),
3.0:(0,0,0.28,0.72),3.5:(0,0.1,0.2,0.55),4.0:(0,0,0.18,0.38),4.5:(0,0.12,0.18,0.3),
7.0:(0,0,0.31,0.85),7.5:(0,0,0.34,0.88),8.0:(0,0,0.37,0.72),8.5:(0,0,0.32,0.52),9.0:(0,0,0.25,0.5),9.5:(0,0,0.22,0.47),10.0:(0,0,0.24,0.48)}
woman={0.0:(0.82,0.25,0.18,0.25),0.5:(0.78,0.33,0.22,0.16),1.0:(0.73,0.3,0.27,0.18),1.5:(0.63,0.26,0.37,0.24),2.0:(0.62,0.22,0.38,0.32),
2.5:(0.56,0.25,0.44,0.3),3.0:(0.56,0.22,0.44,0.34),3.5:(0.22,0.18,0.78,0.32),4.0:(0.6,0.12,0.4,0.38),4.5:(0.62,0.12,0.38,0.4),
5.0:(0.12,0,0.88,0.62),5.5:(0.1,0,0.9,0.67),6.0:(0.12,0,0.88,0.72),6.5:(0.14,0.02,0.86,0.8),
7.0:(0.58,0.08,0.42,0.76),7.5:(0.58,0.05,0.42,0.8),8.0:(0.6,0,0.4,0.66),8.5:(0.58,0,0.42,0.62),9.0:(0.6,0,0.4,0.58),9.5:(0.6,0,0.4,0.5),10.0:(0.62,0,0.38,0.55)}
dog={0.0:(0.51,0.22,0.2,0.2),0.5:(0.5,0.24,0.18,0.2),1.0:(0.47,0.27,0.18,0.2),1.5:(0.43,0.32,0.18,0.2),2.0:(0.43,0.34,0.18,0.19),
2.5:(0.36,0.36,0.18,0.14),3.0:(0.33,0.32,0.2,0.15),4.0:(0.33,0.29,0.18,0.15),
7.0:(0.32,0.45,0.2,0.15),7.5:(0.35,0.44,0.19,0.15),8.0:(0.38,0.38,0.2,0.14),8.5:(0.34,0.36,0.2,0.14),9.0:(0.35,0.33,0.2,0.14),10.0:(0.36,0.3,0.2,0.14)}
c={"mediaId":638,"level":"A","keyWord":"sauce","defaultVoice":"male",
"taps":[{"phrase":"to pour green sauce","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to eat a potato","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to sit on the grass","target":"the dog","voice":"male","keys":keys(dog)}],
"stillS":7.0,
"nouns":[{"word":"a man","x":0.14,"y":0.4,"voice":"male"},{"word":"a woman","x":0.82,"y":0.43,"voice":"female"},
{"word":"a dog","x":0.42,"y":0.52,"voice":"male"},{"word":"sauce","x":0.62,"y":0.81,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","pouring","green","sauce."],"answerVoice":"male",
"notes":"Tight scene: the man's arm with the spoon reaches across the plate the woman holds, so his box holds head, torso and near hand, not the spoon over the plate; her box holds her sleeve / body and, where it fits, the hand on the plate (0.0-4.5 s only her hand and sleeve are in the picture). Man is only a sliver at the left edge 5.0-6.5 s -> off. Dog is small and in the background; off at 3.5, 4.5-6.5 and 9.5 s (hidden); at 7.0-7.5 s it lies rather than sits."}
json.dump(c,open('content/638.json','w'),ensure_ascii=False,indent=1)
