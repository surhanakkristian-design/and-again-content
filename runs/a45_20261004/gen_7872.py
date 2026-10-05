import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
man=K([(0.27,0.31,0.28,0.63),(0.27,0.29,0.31,0.67),(0.26,0.29,0.36,0.71),(0.30,0.28,0.42,0.72),(0.37,0.27,0.45,0.73),(0.43,0.27,0.46,0.73),(0.46,0.27,0.41,0.73),(0.47,0.24,0.53,0.76)])
wo=K([(0.55,0.35,0.25,0.54),(0.58,0.34,0.20,0.54),(0.62,0.35,0.18,0.52),None,None,(0.25,0.36,0.18,0.44),(0.27,0.37,0.19,0.42),(0.25,0.37,0.20,0.40)])
c=dict(mediaId=7872,level="B",keyWord="ill",defaultVoice="male",
taps=[dict(phrase="to wear an ill-fitting suit",target="the man",voice="male",keys=man),
dict(phrase="to burst out laughing",target="the woman in the red dress",voice="female",keys=wo),
dict(phrase="to carry two glasses",target="the woman in the red dress",voice="female",keys=wo)],
stillS=3.2,
nouns=[dict(word="a chandelier",x=0.20,y=0.22,voice="male"),dict(word="a marble pillar",x=0.82,y=0.11,voice="male"),
dict(word="a revolving door",x=0.18,y=0.42,voice="male"),dict(word="a tie",x=0.67,y=0.50,voice="male")],
question="What is the man wearing?",answer="He is wearing an ill-fitting suit.".split(),answerVoice="male",
notes="Keyword 'ill' used as ill-fitting. Woman hidden behind the man at 1.7-2.2 (off); at 1.2 and 2.7-3.7 she is partly behind him, boxes split at his edge (her head cut at 1.2). She laughs hardest 0.2-1.2, smiles later. Man phrase is a state (the suit is the point of the clip); other guests also walk.")
json.dump(c,open('content/7872.json','w'),indent=1)
