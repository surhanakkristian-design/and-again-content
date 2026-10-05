import json
T=[i*0.5 for i in range(21)]
R={0:(0.08,0.27,0.36,0.63),0.5:(0,0.28,0.44,0.72),1:(0,0.22,0.51,0.78),1.5:(0,0.13,0.46,0.87),2:(0,0.16,0.49,0.80),2.5:(0,0.31,0.45,0.64),
3:(0.18,0.33,0.28,0.35),3.5:(0.18,0.34,0.27,0.28),4:(0.18,0.30,0.42,0.40),4.5:(0,0.27,0.45,0.55),5:(0.20,0.36,0.48,0.46),5.5:(0.13,0.34,0.53,0.48),
6:(0.10,0.18,0.90,0.45),6.5:(0.10,0.29,0.85,0.66),7:(0,0.32,0.50,0.68),7.5:(0,0.42,0.26,0.34),8:(0,0.20,0.50,0.77),8.5:(0,0.18,0.51,0.61),
9:(0.02,0.28,0.50,0.51),9.5:(0.13,0.30,0.47,0.53),10:(0.10,0.29,0.49,0.66)}
B={0:(0.60,0.27,0.40,0.63),0.5:(0.55,0.29,0.45,0.71),1:(0.52,0.23,0.48,0.75),1.5:(0.54,0.14,0.46,0.86),2:(0.62,0.14,0.38,0.86),2.5:(0.60,0.31,0.40,0.66),
3:(0.50,0.33,0.32,0.38),3.5:(0.50,0.34,0.30,0.28),4:None,4.5:None,5:None,5.5:None,6:None,6.5:None,7:(0.51,0.26,0.42,0.55),7.5:(0.27,0.11,0.71,0.89),
8:(0.51,0.10,0.49,0.68),8.5:(0.53,0.26,0.44,0.46),9:(0.53,0.37,0.40,0.39),9.5:(0.61,0.43,0.30,0.30),10:(0.60,0.55,0.32,0.22)}
def keys(d): return [dict(t=t,off=True) if d[t] is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c=dict(mediaId=4917,level="A",keyWord="shoot",defaultVoice="male",
 taps=[dict(phrase="to shoot the man in blue",target="the man in red",voice="male",keys=keys(R)),
       dict(phrase="to climb over a wall",target="the man in red",voice="male",keys=keys(R)),
       dict(phrase="to kneel on the ground",target="the man in blue",voice="male",keys=keys(B))],
 stillS=9.5,
 nouns=[dict(word="the sky",x=0.50,y=0.15,voice="male"),dict(word="a fence",x=0.88,y=0.40,voice="male"),
        dict(word="a gun",x=0.21,y=0.62,voice="male"),dict(word="paint",x=0.69,y=0.58,voice="male")],
 question="What is the man in red doing?",answer=["He","is","shooting","the","man","in","blue."],answerVoice="male",
 notes="'a wall' = the wooden barrier he climbs over at 6.0-6.5 s. 'a fence' = net fence at the right edge. 'paint' = pink splash on the blue chest. Blue man is off-screen 4.0-6.5 s; at 7.5 s only the red man's arm and gun are visible (bottom left).")
json.dump(c,open('content/4917.json','w'),indent=1)
