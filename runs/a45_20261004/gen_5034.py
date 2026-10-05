import json
T=[i*0.5 for i in range(21)]
O=None
W=[(0.41,0.04,0.59,0.62),(0.42,0.03,0.58,0.62),(0.41,0.03,0.59,0.62),(0.41,0.0,0.59,0.66),(0.39,0.0,0.61,0.66),
   (0.35,0.0,0.65,0.70),(0.40,0.0,0.60,0.72),(0.47,0.08,0.53,0.90),(0.50,0.18,0.50,0.70),(0.51,0.06,0.49,0.80),
   (0.53,0.05,0.47,0.80),(0.52,0.05,0.48,0.80),(0.53,0.08,0.47,0.80),(0.51,0.08,0.49,0.85),(0.37,0.60,0.63,0.40),
   (0.30,0.44,0.58,0.56),(0.36,0.47,0.38,0.44),(0.37,0.48,0.37,0.42),(0.37,0.50,0.34,0.37),(0.38,0.50,0.30,0.36),(0.40,0.52,0.25,0.33)]
C=[(0.10,0.25,0.31,0.47),(0.12,0.24,0.30,0.47),(0.10,0.22,0.31,0.50),(0.08,0.17,0.33,0.54),(0.04,0.14,0.35,0.58),
   (0.0,0.16,0.35,0.60),(0.01,0.22,0.39,0.56),(0.15,0.0,0.32,0.35)]+[O]*6+[(0.28,0.20,0.25,0.18)]+[O]*6
P=[O]*7+[(0.08,0.66,0.38,0.34),(0.08,0.26,0.42,0.34),(0.08,0.10,0.43,0.40),(0.09,0.10,0.44,0.38),(0.09,0.10,0.43,0.38),
   (0.09,0.10,0.44,0.39),(0.09,0.17,0.42,0.35),(0.0,0.70,0.36,0.30)]+[O]*6
def k(L): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,L)]
c=dict(mediaId=5034,level="B",keyWord="spill",defaultVoice="female",taps=[
 dict(phrase="to crouch under the sink",target="the woman",voice="female",keys=k(W)),
 dict(phrase="to leak onto the table",target="the milk carton",voice="female",keys=k(C)),
 dict(phrase="to drip into a bucket",target="the grey pipe",voice="female",keys=k(P))],
 stillS=2.5,nouns=[dict(word="a milk carton",x=0.18,y=0.45,voice="female"),dict(word="a bathrobe",x=0.64,y=0.56,voice="female"),
 dict(word="a puddle",x=0.56,y=0.80,voice="female"),dict(word="a table",x=0.25,y=0.92,voice="female")],
 question="What is dripping into the bucket?",answer=["Water","is","dripping","from","the","pipe."],answerVoice="female",
 notes="Three shots: milk carton at the table (0-3.0), under the sink (3.5-7.0), room with hanging bowls (7.5-10). Woman box split from the carton at the carton's right edge (her hand holding the carton on its left is left out). 3.5 and 7.0 are transition frames (carton above the table edge, woman under it). Grey pipe = the grey drain trap whose bend drips into the bucket; the white pipe below is outside the box where possible. Key word 'spill' is a verb, not used as a noun.")
json.dump(c,open('content/5034.json','w'),indent=1)
