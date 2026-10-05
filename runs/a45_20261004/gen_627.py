import json
T=[i*0.5 for i in range(21)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
D={0.0:(0.27,0.11,0.71,0.89),0.5:(0.24,0.09,0.60,0.91),1.0:(0.20,0.07,0.80,0.93),1.5:(0.04,0.05,0.64,0.95),2.0:(0.04,0.04,0.96,0.96),
2.5:(0.18,0.0,0.74,1.0),3.0:(0.13,0.02,0.70,0.98),3.5:(0.09,0.04,0.63,0.96),4.0:(0.18,0.02,0.43,0.97),4.5:(0.07,0.02,0.54,0.94),
5.0:(0.06,0.05,0.56,0.95),5.5:(0.13,0.05,0.49,0.95),6.0:(0.25,0.09,0.50,0.89),6.5:(0.33,0.13,0.32,0.72),7.0:(0.33,0.18,0.33,0.68),
7.5:(0.37,0.18,0.30,0.62),8.0:(0.38,0.19,0.26,0.46),8.5:(0.36,0.20,0.18,0.42),9.0:(0.35,0.19,0.18,0.52),9.5:(0.35,0.19,0.18,0.52),10.0:(0.33,0.19,0.18,0.42)}
R={0.0:(0.0,0.17,0.26,0.58),0.5:(0.0,0.18,0.23,0.50),1.0:(0.0,0.19,0.18,0.46),3.5:(0.73,0.26,0.18,0.24),4.0:(0.62,0.25,0.20,0.14),4.5:(0.62,0.25,0.20,0.14),
5.0:(0.63,0.26,0.20,0.14),5.5:(0.63,0.26,0.20,0.14),8.5:(0.56,0.21,0.18,0.24),9.0:(0.55,0.22,0.18,0.24),9.5:(0.55,0.22,0.18,0.24),10.0:(0.54,0.21,0.18,0.27)}
C={4.0:(0.63,0.40,0.18,0.14),4.5:(0.64,0.40,0.18,0.14),5.0:(0.63,0.41,0.18,0.14),5.5:(0.63,0.41,0.18,0.14),8.5:(0.54,0.46,0.18,0.14),9.0:(0.53,0.47,0.18,0.14),9.5:(0.53,0.48,0.18,0.14),10.0:(0.52,0.49,0.18,0.14)}
c=dict(mediaId=627,level="B",keyWord="runway",defaultVoice="female",taps=[
 dict(phrase="to strut along the rug",target="the woman in the blue dress",voice="female",keys=keys(D)),
 dict(phrase="to film her friend",target="the red-haired woman",voice="female",keys=keys(R)),
 dict(phrase="to sit upright on the rug",target="the cat",voice="female",keys=keys(C))],
 stillS=7.5,nouns=[dict(word="a rug",x=0.50,y=0.85,voice="female"),dict(word="fairy lights",x=0.33,y=0.19,voice="female"),dict(word="a fireplace",x=0.14,y=0.37,voice="female"),dict(word="a floor lamp",x=0.86,y=0.28,voice="female")],
 question="What is the woman in blue doing?",answer=["She","is","strutting","along","the","rug."],answerVoice="female",
 notes="Red-haired woman films with a phone (flash) at the start on the left (0.0-1.0) and at the far end of the rug from 3.5; possibly two different friends, both red-haired and both filming, never visible together - one target. Far end: the three targets are small and close; boxes split between them (woman in blue cut at her right arm from 8.5). Red-haired woman and cat marked off at 6.0-8.0 (hidden behind her / only a sliver); cat also off at 3.5 (hidden / unclear). Key word 'runway' is not a literal thing in the picture (the rug stands in for it), so it is not a noun.")
json.dump(c,open('content/627.json','w'),indent=1)
