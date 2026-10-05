import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
man=keys({0.0:(0.18,0.18,0.82,0.62),0.5:(0.10,0.17,0.90,0.66),2.0:(0.0,0.07,1.0,0.93),2.5:(0.0,0.05,1.0,0.95),3.0:(0.0,0.05,1.0,0.95),
 3.5:(0.40,0.33,0.55,0.50),4.0:(0.40,0.34,0.52,0.50),4.5:(0.40,0.34,0.55,0.50),5.0:(0.24,0.36,0.76,0.64),5.5:(0.08,0.38,0.92,0.62),6.0:(0.0,0.35,0.92,0.65)})
woman=keys({3.5:(0.10,0.26,0.30,0.50),4.0:(0.05,0.27,0.35,0.48),4.5:(0.08,0.26,0.32,0.48)})
check=keys({t:(0.30,0.19,0.46,0.24) for t in (8.5,9.0,9.5,10.0)})
c=dict(mediaId=4868,level="B",keyWord="program",defaultVoice="male",taps=[
 dict(phrase="to clench his fist",target="the man in the hoodie",voice="male",keys=man),
 dict(phrase="to point at the laptop screen",target="the woman in the denim shirt",voice="female",keys=woman),
 dict(phrase="to appear on the main screen",target="the green check mark",voice="male",keys=check)],
 stillS=4.0,
 nouns=[dict(word="windows",x=0.62,y=0.12,voice="male"),dict(word="a hoodie",x=0.72,y=0.62,voice="male"),
        dict(word="a laptop",x=0.22,y=0.77,voice="male"),dict(word="a computer mouse",x=0.52,y=0.87,voice="male")],
 question="What is the woman in denim doing?",answer=["She","is","pointing","at","the","laptop","screen."],answerVoice="female",
 notes="Hoodie man boxed only in his own shots (0-0.5, 2-6 s); in the dark team shots (6.5-10 s) a man in a dark top on the right may be him but is unclear, so OFF. At 3.5-4.5 his hands reach left under the woman's arm; boxes split at x=0.40.")
json.dump(c,open('content/4868.json','w'),indent=1)
