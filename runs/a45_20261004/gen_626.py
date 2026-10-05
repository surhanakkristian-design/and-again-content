import json
T=[i*0.5 for i in range(21)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
r={0.0:(0.22,0.12,0.78,0.88),0.5:(0.25,0.14,0.75,0.86),1.0:(0.28,0.07,0.72,0.93),1.5:(0.0,0.09,1.0,0.91),2.0:(0.44,0.12,0.56,0.88),
2.5:(0.18,0.12,0.82,0.88),3.0:(0.08,0.12,0.92,0.88),3.5:(0.10,0.11,0.90,0.89),4.0:(0.22,0.09,0.70,0.91),4.5:(0.20,0.09,0.75,0.91),
5.0:(0.20,0.07,0.77,0.93),5.5:(0.28,0.12,0.72,0.88),6.0:(0.26,0.07,0.74,0.93),6.5:(0.23,0.11,0.77,0.89),7.0:(0.31,0.21,0.40,0.58),
7.5:(0.39,0.19,0.39,0.64),8.0:(0.37,0.19,0.43,0.72),8.5:(0.36,0.14,0.44,0.70),9.0:(0.35,0.18,0.44,0.79),9.5:(0.31,0.14,0.42,0.80),10.0:(0.32,0.14,0.45,0.72)}
p={7.0:(0.0,0.18,0.30,0.22),7.5:(0.0,0.14,0.38,0.24),8.0:(0.0,0.11,0.36,0.21),8.5:(0.0,0.07,0.35,0.22),9.0:(0.0,0.14,0.34,0.20),9.5:(0.0,0.09,0.30,0.20),10.0:(0.0,0.08,0.31,0.18)}
c=dict(mediaId=626,level="A",keyWord="runner",defaultVoice="female",taps=[
 dict(phrase="to drink from a cup",target="the runner in orange",voice="female",keys=keys(r)),
 dict(phrase="to watch the race",target="the people",voice="female",keys=keys(p)),
 dict(phrase="to look at her watch",target="the runner in orange",voice="female",keys=keys(r))],
 stillS=2.5,nouns=[dict(word="a cup",x=0.42,y=0.33,voice="female"),dict(word="a watch",x=0.80,y=0.66,voice="female"),dict(word="the sky",x=0.30,y=0.06,voice="female"),dict(word="a runner",x=0.64,y=0.48,voice="female")],
 question="What is the runner doing?",answer=["She","is","drinking","from","a","cup."],answerVoice="female",
 notes="'the people' = the crowd behind the barrier on the left, only in the last shot (7.0-10.0); the box covers the left part of the crowd, cut where the runner starts. Other runners far behind and helpers at the drinks table (1.0-4.0) are not targets. Noun 'a runner' sits on her top, apart from the cup and the watch.")
json.dump(c,open('content/626.json','w'),indent=1)
