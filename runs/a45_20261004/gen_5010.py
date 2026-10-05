import json
T=[i*0.5 for i in range(25)]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
KG=[(0,0.35,0.70,0.65),(0.20,0.28,0.78,0.72),(0.12,0.38,0.74,0.60),(0.27,0.38,0.52,0.42),(0.32,0.33,0.56,0.44),(0.36,0.25,0.37,0.50),
    (0.24,0.30,0.46,0.52),(0,0.34,0.80,0.66),(0,0.29,1,0.71),(0,0.26,1,0.74),(0,0.17,0.69,0.83),(0,0.15,1,0.85),
    (0,0.10,0.80,0.90),(0,0.16,0.85,0.84),(0,0.25,0.92,0.75),(0,0.25,1,0.75),(0.04,0.30,0.85,0.70),(0.02,0.32,0.90,0.68),(0.03,0.32,0.85,0.68),
    (0.38,0.43,0.21,0.16),(0.38,0.47,0.19,0.15),(0.38,0.51,0.20,0.15),(0.38,0.53,0.19,0.15),(0.38,0.54,0.19,0.15),(0.38,0.55,0.19,0.15)]
OM=[None]*5+[(0.76,0.32,0.24,0.34),(0.75,0.30,0.25,0.62),(0.80,0.26,0.20,0.74),(0.62,0.08,0.38,0.21),(0.48,0.08,0.52,0.18),(0.70,0,0.30,0.62)]+[None]*14
k=K(KG); o=K(OM)
c=dict(mediaId=5010,level="A",keyWord="king",defaultVoice="male",
 taps=[dict(phrase="to walk on a red carpet",target="the king",voice="male",keys=k),
       dict(phrase="to sit on a throne",target="the king",voice="male",keys=k),
       dict(phrase="to hold a gold crown",target="the old man",voice="male",keys=o)],
 stillS=3.0,
 nouns=[dict(word="a flag",x=0.45,y=0.17,voice="male"),dict(word="a crown",x=0.85,y=0.45,voice="male"),
        dict(word="a king",x=0.45,y=0.55,voice="male"),dict(word="a carpet",x=0.45,y=0.88,voice="male")],
 question="Where is the king sitting?",answer=["He","is","sitting","on","a","throne."],answerVoice="male",
 notes="Old man (crown bearer) is only partly visible: at 4.0-5.0 s just his hand/sleeve above the king's head, split from the king's box along the crown line. Crowd not used as a target: it sits right behind the king at 8-9 s and boxes would overlap. 'a flag' labels the hanging red banner behind the throne. King is tiny on the balcony at 9.5-12.0 s.")
json.dump(c,open('content/5010.json','w'),indent=1)
