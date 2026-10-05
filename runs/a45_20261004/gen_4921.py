import json
T=[i*0.5 for i in range(19)]
N=None
G={0:N,0.5:(0.08,0,0.90,1.0),1:(0,0.19,1.0,0.81),1.5:N,2:N,2.5:(0.51,0.06,0.49,0.94),3:(0.48,0,0.52,1.0),3.5:(0.51,0,0.49,1.0),4:(0.47,0.17,0.53,0.83),
4.5:(0.78,0.20,0.22,0.62),5:(0.45,0.22,0.46,0.78),5.5:(0.50,0,0.50,0.64),6:(0.49,0.10,0.51,0.83),6.5:(0.09,0.42,0.40,0.45),7:(0.23,0.37,0.29,0.49),
7.5:(0.24,0.33,0.32,0.55),8:(0.12,0.46,0.34,0.43),8.5:(0.09,0.47,0.40,0.41),9:(0.11,0.44,0.38,0.42)}
L={0:N,0.5:N,1:N,1.5:N,2:(0.47,0.47,0.22,0.31),2.5:(0,0.09,0.50,0.91),3:(0,0,0.47,1.0),3.5:(0,0.16,0.50,0.84),4:(0,0.22,0.46,0.78),
4.5:(0.02,0.31,0.52,0.65),5:(0,0.26,0.44,0.74),5.5:(0.08,0.06,0.41,0.64),6:(0.03,0.19,0.45,0.67),6.5:(0.52,0.41,0.40,0.44),7:(0.54,0.39,0.30,0.47),
7.5:(0.57,0.33,0.30,0.55),8:(0.58,0.46,0.33,0.43),8.5:(0.56,0.47,0.35,0.41),9:(0.57,0.44,0.33,0.43)}
def keys(d): return [dict(t=t,off=True) if d[t] is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c=dict(mediaId=4921,level="B",keyWord="trail",defaultVoice="male",
 taps=[dict(phrase="to toss a water bottle",target="the bearded man",voice="male",keys=keys(G)),
       dict(phrase="to catch a water bottle",target="the blond man",voice="male",keys=keys(L)),
       dict(phrase="to wear a grey hoodie",target="the bearded man",voice="male",keys=keys(G))],
 stillS=5.0,
 nouns=[dict(word="spruce trees",x=0.15,y=0.20,voice="male"),dict(word="the sky",x=0.47,y=0.06,voice="male"),
        dict(word="a trail",x=0.45,y=0.68,voice="male"),dict(word="a water bottle",x=0.82,y=0.54,voice="male")],
 question="What are the two men doing?",answer=["They","are","hiking","up","a","steep","forest","trail."],answerVoice="male",
 notes="Toss/catch happens at 4.0-4.5 s: the bearded man holds the bottle at 4.0, at 4.5 it flies to the blond man's raised hands. 0.5 s = blurred grey-hoodie torso, taken as the bearded man; 0.0 s boots of unknown hiker (off). From 5.0-6.0 s identities from the sleeves (blue = blond, grey = bearded). 'to wear a grey hoodie' is a state: no other action fits only him.")
json.dump(c,open('content/4921.json','w'),indent=1)
