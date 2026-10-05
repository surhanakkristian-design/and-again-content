import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
wave={0.0:(0.28,0,0.72,0.6),0.5:(0.1,0.3,0.9,0.46),1.0:(0.08,0.72,0.92,0.28),1.5:(0.05,0.6,0.95,0.37),2.0:(0,0.32,1,0.34),
2.5:(0,0.17,1,0.48),3.0:(0,0.37,1,0.37)}
woman={3.5:(0.1,0.37,0.44,0.57),4.0:(0.09,0.36,0.44,0.44),4.5:(0.07,0.36,0.42,0.45),5.0:(0.03,0.38,0.51,0.53),5.5:(0.12,0.4,0.39,0.5),
6.0:(0.17,0.43,0.36,0.33),6.5:(0.22,0.42,0.33,0.26),7.0:(0.27,0.47,0.24,0.2),8.0:(0.22,0.51,0.2,0.15),8.5:(0.21,0.5,0.2,0.16),
9.0:(0.2,0.53,0.22,0.16),9.5:(0.13,0.53,0.3,0.15),10.0:(0.1,0.54,0.3,0.15)}
man={3.5:(0.55,0.37,0.42,0.58),4.0:(0.54,0.4,0.36,0.47),4.5:(0.5,0.36,0.44,0.54),5.0:(0.55,0.36,0.37,0.58),5.5:(0.52,0.38,0.31,0.52),
6.0:(0.54,0.42,0.27,0.32),6.5:(0.56,0.43,0.29,0.24),7.0:(0.57,0.46,0.22,0.2),8.5:(0.64,0.49,0.2,0.15),
9.0:(0.65,0.51,0.2,0.15),9.5:(0.66,0.52,0.2,0.15),10.0:(0.66,0.52,0.2,0.15)}
c={"mediaId":652,"level":"A","keyWord":"sea","defaultVoice":"female",
"taps":[{"phrase":"to hit the rocks","target":"the wave","voice":"female","keys":keys(wave)},
{"phrase":"to wear a white shirt","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to have short hair","target":"the man","voice":"male","keys":keys(man)}],
"stillS":4.0,
"nouns":[{"word":"the sea","x":0.6,"y":0.3,"voice":"female"},{"word":"a woman","x":0.28,"y":0.52,"voice":"female"},
{"word":"a man","x":0.7,"y":0.57,"voice":"male"},{"word":"rocks","x":0.45,"y":0.88,"voice":"female"}],
"question":"What are they doing?","answer":["They","are","jumping","into","the","sea."],"answerVoice":"female",
"notes":"The two people do the same things (run, jump, swim), so their phrases are states. The wave is boxed only in the first shot (0.0-3.0 s, white water on the rocks); later white water is the splash of the jump and is not boxed. The bare feet in the first shot belong to the camera person and are not boxed. 7.5 s both under water -> off; 8.0 s only one dark head comes up on the left, boxed as the woman (she is on the left at 8.5 s)."}
json.dump(c,open('content/652.json','w'),ensure_ascii=False,indent=1)
