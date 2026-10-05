import json
T=[i*0.5 for i in range(21)]
W={0:(0.51,0,0.47,0.6),0.5:(0.50,0,0.50,0.55),1:(0.47,0,0.51,0.70),1.5:(0.60,0.15,0.40,0.85),2:(0.42,0.27,0.58,0.73),2.5:(0.65,0.43,0.35,0.57),
3:(0.46,0.33,0.32,0.62),3.5:(0.52,0.32,0.48,0.68),4:(0.53,0.28,0.44,0.72),4.5:(0,0.27,0.50,0.70),5:(0,0.28,0.45,0.72),5.5:(0,0.30,0.50,0.66),
6:(0.08,0.54,0.84,0.46),6.5:(0,0.58,1.0,0.42),7:(0.02,0.51,0.95,0.49),7.5:(0,0.20,0.52,0.73),8:(0.17,0.29,0.31,0.68),8.5:(0.11,0.33,0.38,0.67),
9:(0,0.33,0.51,0.67),9.5:(0,0.32,0.53,0.68),10:(0,0.35,0.52,0.65)}
M={0:(0.03,0,0.47,0.62),0.5:(0,0,0.49,0.58),1:(0.02,0,0.44,0.62),1.5:(0,0.03,0.59,0.97),2:(0,0.12,0.41,0.88),2.5:(0,0.24,0.64,0.76),
3:(0,0.27,0.45,0.73),3.5:(0,0.26,0.51,0.74),4:(0.24,0.25,0.28,0.68),4.5:(0.51,0.17,0.35,0.83),5:(0.46,0.20,0.42,0.80),5.5:(0.51,0.23,0.37,0.77),
6:(0.25,0.22,0.37,0.31),6.5:(0.16,0.33,0.74,0.24),7:(0.18,0.21,0.60,0.29),7.5:(0.53,0.14,0.30,0.86),8:(0.49,0.21,0.40,0.79),8.5:(0.50,0.23,0.43,0.77),
9:(0.52,0.16,0.48,0.84),9.5:(0.54,0.10,0.46,0.90),10:(0.53,0.10,0.47,0.90)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c=dict(mediaId=4916,level="A",keyWord="bicycle",defaultVoice="female",
 taps=[dict(phrase="to spin around",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to catch the woman",target="the man",voice="male",keys=keys(M)),
       dict(phrase="to lean back",target="the woman",voice="female",keys=keys(W))],
 stillS=8.0,
 nouns=[dict(word="the sun",x=0.17,y=0.31,voice="female"),dict(word="a bicycle",x=0.10,y=0.76,voice="female"),
        dict(word="a dress",x=0.36,y=0.85,voice="female"),dict(word="a T-shirt",x=0.68,y=0.55,voice="female")],
 question="What are they riding?",answer=["They","are","riding","bicycles."],answerVoice="female",
 notes="Man and woman overlap heavily during the spin and dip (4.0-7.5 s); boxes split along the line between them. 'to lean back' = her backward dip at 6.0-7.0 s.")
json.dump(c,open('content/4916.json','w'),indent=1)
