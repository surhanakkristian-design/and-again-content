import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(0.16,0.34,0.47,0.80),(0.15,0.34,0.47,0.80),(0.13,0.41,0.50,0.92),(0.11,0.40,0.48,0.92),(0.07,0.26,0.53,0.82),(0.01,0.23,0.53,0.86),(0.0,0.31,0.50,0.98),(0.0,0.31,0.50,0.97)])
lamb=K([(0.47,0.59,0.65,0.84),(0.47,0.55,0.65,0.82),(0.50,0.55,0.68,0.91),(0.48,0.54,0.66,0.92),(0.53,0.52,0.72,0.88),(0.53,0.52,0.73,0.90),(0.50,0.51,0.72,0.97),(0.50,0.50,0.76,1.0)])
ewe=K([(0.65,0.58,1.0,0.93),(0.65,0.57,1.0,0.96),(0.68,0.57,1.0,1.0),(0.66,0.55,1.0,1.0),(0.72,0.55,1.0,1.0),(0.73,0.54,1.0,1.0),(0.72,0.53,1.0,1.0),(0.76,0.52,1.0,1.0)])
c=dict(mediaId=6864,level="B",keyWord="bear",defaultVoice="female",
 taps=[dict(phrase="to kneel in the straw",target="the woman",voice="female",keys=woman),
       dict(phrase="to stand on shaky legs",target="the lamb",voice="female",keys=lamb),
       dict(phrase="to lick the newborn lamb",target="the ewe",voice="female",keys=ewe)],
 stillS=0.7,
 nouns=[dict(word="a lantern",x=0.70,y=0.22,voice="female"),dict(word="a bucket",x=0.12,y=0.75,voice="female"),
        dict(word="a lamb",x=0.55,y=0.63,voice="female"),dict(word="straw",x=0.35,y=0.90,voice="female")],
 question="What is the ewe doing?",answer=["It","is","licking","the","newborn","lamb."],answerVoice="female",
 notes="Key word 'bear' (verb, to give birth) is not a visible noun, so not among the nouns. Lamb and ewe overlap (ewe's head against the lamb); boxes split along the vertical line between them. The ewe licks the lamb clearly at 1.7-2.2 and 3.7. Woman's knees touch the lamb box edge at 0.7-1.7.")
json.dump(c,open('content/6864.json','w'),indent=1)
