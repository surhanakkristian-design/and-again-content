import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]
W={0.0:(0.46,0.04,0.54,0.96),0.5:(0.48,0.02,0.52,0.98),1.0:(0.48,0.02,0.52,0.98),1.5:(0.48,0.02,0.52,0.98),
2.0:(0.14,0.11,0.86,0.68),2.5:(0.12,0.12,0.88,0.66),3.0:(0.10,0.13,0.90,0.66),3.5:(0.10,0.13,0.90,0.66),
4.0:(0.20,0.50,0.62,0.50),4.5:(0.22,0.48,0.70,0.52),5.0:(0.16,0.46,0.62,0.54),5.5:(0.40,0.40,0.60,0.60),
6.0:(0.38,0.41,0.62,0.59),6.5:(0.38,0.42,0.62,0.58),7.0:(0.30,0.42,0.68,0.58),7.5:(0.37,0.42,0.63,0.58),
8.0:(0.35,0.44,0.63,0.56),8.5:(0.37,0.44,0.63,0.56),9.0:(0.33,0.45,0.62,0.55)}
B={0.0:(0,0.15,0.45,0.60),0.5:(0,0.13,0.47,0.62),1.0:(0,0.13,0.47,0.62),1.5:(0,0.13,0.47,0.62)}
F={5.5:(0,0.17,0.40,0.83),6.0:(0,0.15,0.37,0.85),6.5:(0,0.17,0.37,0.83),7.0:(0,0.17,0.29,0.83),7.5:(0,0.17,0.36,0.83),
8.0:(0,0.18,0.34,0.82),8.5:(0,0.19,0.36,0.81),9.0:(0,0.18,0.32,0.82)}
def keys(D): return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else dict(t=t,off=True) for t in T]
taps=[dict(phrase="to hold up a microphone",target="the woman",voice="female",keys=keys(W)),
dict(phrase="to sing in the forest",target="the bird",voice="female",keys=keys(B)),
dict(phrase="to fall from the rocks",target="the waterfall",voice="female",keys=keys(F))]
c=dict(mediaId=4861,level="A",keyWord="listen",defaultVoice="female",taps=taps,stillS=7.0,
nouns=[dict(word="a microphone",x=0.55,y=0.16,voice="female"),dict(word="a waterfall",x=0.17,y=0.45,voice="female"),
dict(word="headphones",x=0.74,y=0.60,voice="female"),dict(word="a vest",x=0.72,y=0.76,voice="female")],
question="What is the woman holding?",answer=["She","is","holding","a","long","microphone."],answerVoice="female",
notes="Bird only 0-1.5 s (open beak = singing, visible without sound). Waterfall only 5.5-9.0 s; its box is the left part of the falling water, split from the woman on her raised arm. Noun slot 'a microphone' is on the big boom microphone; a small fluffy recorder mic is also visible at the belt (x0.57 y0.83). Answer refers to the long boom microphone (4.0-9.0 s). Key word 'listen' (verb) not used as a noun.")
json.dump(c,open('content/4861.json','w'),indent=1)
