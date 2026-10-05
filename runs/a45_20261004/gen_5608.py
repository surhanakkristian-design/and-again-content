import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
diver=K([(0.10,0.0,0.76,0.70),(0.02,0.0,0.85,0.69),(0.07,0.0,0.80,0.68),(0.20,0.03,0.57,0.62),(0.26,0.05,0.45,0.58),(0.22,0.12,0.55,0.51),(0.18,0.09,0.61,0.52),(0.24,0.10,0.45,0.50)])
coach=K([(0.92,0.45,0.08,0.25),(0.92,0.45,0.08,0.25),(0.88,0.45,0.12,0.26),(0.86,0.45,0.14,0.25),(0.84,0.46,0.16,0.24),(0.80,0.47,0.20,0.23),(0.80,0.47,0.20,0.23),(0.77,0.47,0.20,0.21)])
c=dict(mediaId=5608,level="B",keyWord="be about to",defaultVoice="female",
 taps=[dict(phrase="to bend her knees",target="the diver",voice="female",keys=diver),
       dict(phrase="to spread her arms wide",target="the diver",voice="female",keys=diver),
       dict(phrase="to signal to the diver",target="the coach",voice="male",keys=coach)],
 stillS=3.2,
 nouns=[dict(word="a swimsuit",x=0.47,y=0.32,voice="female"),dict(word="a diving board",x=0.47,y=0.82,voice="female"),
        dict(word="a coach",x=0.87,y=0.57,voice="male"),dict(word="a lane rope",x=0.15,y=0.72,voice="female")],
 question="What is the diver about to do?",answer=["She","is","about","to","dive","into","the","pool."],answerVoice="female",
 notes="Coach only a sliver at the right edge at 0.2/0.7 (narrow edge boxes). Coach raises one arm towards her: 'to signal to the diver' is the weakest phrase. At 0.7 the diver's hands sit at both picture edges, so her box is wide.")
json.dump(c,open('content/5608.json','w'),indent=1)
