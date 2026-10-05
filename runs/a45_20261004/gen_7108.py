import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
top={0.2:(0.09,0.30,0.65,0.36),0.7:(0.15,0.18,0.60,0.48),1.2:(0.15,0.18,0.58,0.48),1.7:(0.15,0.18,0.58,0.48),
     2.2:(0.13,0.17,0.60,0.49),2.7:(0.12,0.17,0.62,0.49),3.2:(0.09,0.18,0.63,0.48),3.7:(0.08,0.18,0.66,0.48)}
# friend below: from y 0.67 to bottom, right edge split from the older woman
fr={0.2:(0.16,0.67,0.49,0.33),0.7:(0.15,0.67,0.51,0.33),1.2:(0.16,0.67,0.50,0.33),1.7:(0.15,0.67,0.51,0.33),
    2.2:(0.15,0.67,0.50,0.33),2.7:(0.15,0.67,0.54,0.33),3.2:(0.12,0.67,0.53,0.33),3.7:(0.10,0.67,0.57,0.33)}
old={0.2:(0.66,0.67,0.32,0.33),0.7:(0.67,0.67,0.31,0.33),1.2:(0.67,0.67,0.31,0.33),1.7:(0.67,0.67,0.31,0.33),
     2.2:(0.66,0.67,0.32,0.33),2.7:(0.70,0.67,0.28,0.33),3.2:(0.66,0.67,0.32,0.33),3.7:(0.68,0.67,0.30,0.33)}
k=lambda B:[dict(t=t,x=B[t][0],y=B[t][1],w=B[t][2],h=B[t][3]) for t in T]
taps=[dict(phrase="to perch on someone's shoulders",target="the woman on top",voice="female",keys=k(top)),
      dict(phrase="to support her friend's weight",target="the woman below",voice="female",keys=k(fr)),
      dict(phrase="to be moved to tears",target="the older woman",voice="female",keys=k(old))]
c=dict(mediaId=7108,level="B",keyWord="feminist",defaultVoice="female",taps=taps,stillS=2.2,
 nouns=[dict(word="buildings",x=0.82,y=0.15,voice="female"),
        dict(word="a scarf",x=0.36,y=0.29,voice="female"),
        dict(word="a denim jacket",x=0.28,y=0.58,voice="female"),
        dict(word="a cardboard sign",x=0.88,y=0.55,voice="female")],
 question="What is the woman on top doing?",
 answer="She is perching on her friend's shoulders.".split(),
 answerVoice="female",
 notes="Key word 'feminist' not placed: every marcher could be 'a feminist', so the slot would be ambiguous. Top woman's legs hang beside the friend's head; boxes split at y 0.66/0.67 (top woman above, friend + older woman below), friend/older split around x 0.65-0.70. The older grey-haired woman cries the whole clip.")
json.dump(c,open('content/7108.json','w'),indent=1)
