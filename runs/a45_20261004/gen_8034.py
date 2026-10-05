import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
cyc=K([(0.36,0.41,0.31,0.33),(0.35,0.41,0.33,0.32),(0.38,0.41,0.29,0.34),(0.35,0.40,0.24,0.35),
       (0.32,0.41,0.26,0.31),(0.37,0.41,0.26,0.31),(0.43,0.40,0.27,0.31),(0.49,0.39,0.26,0.29)])
hands=K([(0.0,0.76,1.0,0.20)]*8)
wf=K([(0.38,0.21,0.18,0.14),(0.39,0.21,0.18,0.14),(0.39,0.22,0.18,0.14),(0.39,0.22,0.18,0.14),
      (0.35,0.22,0.18,0.14),(0.28,0.23,0.18,0.14),(0.20,0.24,0.18,0.14),(0.12,0.25,0.18,0.14)])
c=dict(mediaId=8034,level="B",keyWord="velocity",defaultVoice="female",
 taps=[dict(phrase="to lean into the bend",target="the cyclist in green",voice="female",keys=cyc),
       dict(phrase="to grip the handlebars",target="the gloved hands",voice="female",keys=hands),
       dict(phrase="to pour down the mountainside",target="the waterfall",voice="female",keys=wf)],
 stillS=3.7,
 nouns=[dict(word="a waterfall",x=0.21,y=0.32,voice="female"),
        dict(word="a hut",x=0.84,y=0.32,voice="female"),
        dict(word="cows",x=0.42,y=0.40,voice="female"),
        dict(word="a cyclist",x=0.63,y=0.53,voice="female")],
 question="What is the cyclist in green doing?",
 answer=["She","is","leaning","into","the","bend."],
 answerVoice="female",
 notes="POV clip from a racing bike. Key word 'velocity' is abstract, not placed as a noun. 'the gloved hands' = the camera rider's hands (only arms/gloves visible, gender unclear, default voice). The cyclist leans clearly into the bend at 0.2-1.2 s and rides straighter later, still on the bend. Waterfall is small: box at the 0.18 x 0.14 minimum. Cow pill sits on the middle cow of a small herd (bare plural).")
json.dump(c,open('content/8034.json','w'),indent=1)
