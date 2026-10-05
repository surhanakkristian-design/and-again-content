import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
A=K([(0,0.29,0.43,0.60),(0,0.06,0.40,0.84),(0,0.09,0.40,0.84),(0,0.07,0.40,0.86),(0,0.26,0.40,0.70),(0,0.31,0.45,0.66),(0,0.34,0.46,0.66),(0,0.32,0.44,0.68)])
B=K([(0.44,0.26,0.30,0.31),(0.43,0.26,0.38,0.31),(0.43,0.27,0.38,0.34),(0.44,0.28,0.40,0.34),(0.46,0.28,0.38,0.34),(0.46,0.28,0.38,0.34),(0.47,0.29,0.35,0.35),(0.45,0.28,0.39,0.36)])
C=K([(0.47,0.73,0.40,0.27),(0.49,0.75,0.39,0.25),(0.48,0.77,0.34,0.23),(0.49,0.79,0.36,0.21),(0.46,0.79,0.39,0.21),(0.47,0.79,0.38,0.21),(0.48,0.82,0.31,0.18),(0.47,0.83,0.32,0.17)])
c=dict(mediaId=5706,level="B",keyWord="cards",defaultVoice="female",
 taps=[dict(phrase="to raise her arm in triumph",target="the dark-haired woman",voice="female",keys=A),
       dict(phrase="to roll his eyes",target="the man",voice="male",keys=B),
       dict(phrase="to lie beneath the table",target="the spaniel",voice="female",keys=C)],
 stillS=3.2,
 nouns=[dict(word="a luggage rack",x=0.70,y=0.10,voice="female"),dict(word="paper cups",x=0.32,y=0.56,voice="female"),
        dict(word="cards",x=0.58,y=0.65,voice="female"),dict(word="a spaniel",x=0.62,y=0.92,voice="female")],
 question="What is the man doing?",answer=["He","is","rolling","his","eyes."],answerVoice="male",
 notes="Eye-roll clearest 1.7-2.7 s; dark-haired woman's raised arm partly leaves frame at 1.2-1.7 s. Red-haired standing woman not used as a target.")
json.dump(c,open('content/5706.json','w'),indent=1)
