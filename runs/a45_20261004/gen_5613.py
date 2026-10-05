import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
front=K([(0.0,0.12,0.75,0.88),(0.0,0.19,0.62,0.81),(0.0,0.21,0.58,0.79),(0.0,0.21,0.58,0.79),(0.0,0.21,0.58,0.79),(0.0,0.21,0.59,0.79),(0.0,0.21,0.58,0.79),(0.0,0.21,0.58,0.79)])
back=K([(0.76,0.29,0.24,0.60),(0.63,0.29,0.35,0.62),(0.59,0.29,0.35,0.61),(0.59,0.29,0.36,0.61),(0.59,0.29,0.36,0.61),(0.60,0.30,0.34,0.60),(0.59,0.29,0.34,0.61),(0.59,0.29,0.35,0.60)])
c=dict(mediaId=5613,level="B",keyWord="be capable of",defaultVoice="female",
 taps=[dict(phrase="to grin at the camera",target="the woman with the braid",voice="female",keys=front),
       dict(phrase="to point over her shoulder",target="the woman with the braid",voice="female",keys=front),
       dict(phrase="to strain under the weight",target="the woman in black",voice="female",keys=back)],
 stillS=3.7,
 nouns=[dict(word="a boulder",x=0.66,y=0.37,voice="female"),dict(word="arches",x=0.85,y=0.25,voice="female"),
        dict(word="a braid",x=0.31,y=0.62,voice="female"),dict(word="a fence",x=0.42,y=0.16,voice="female")],
 question="What is the woman in black carrying?",answer=["She","is","carrying","a","boulder","on","her","shoulder."],answerVoice="female",
 notes="The braid woman's thumb reaches into the other woman's region from 1.2 s; boxes split at x~0.58/0.59, so the left edge of the boulder is outside the back woman's box. Thumb point starts ~1.2 s.")
json.dump(c,open('content/5613.json','w'),indent=1)
