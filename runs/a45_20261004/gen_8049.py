import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def box(a): return dict(x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2))
def keys(b): return [dict(t=t,**box(a)) for t,a in zip(T,b)]
keeper=[(0.31,0.28,0.86,0.91),(0.32,0.28,0.86,0.91),(0.31,0.28,0.86,0.91),(0.32,0.27,0.87,0.91),
        (0.33,0.26,0.89,0.91),(0.36,0.25,0.91,0.91),(0.38,0.24,0.91,0.92),(0.38,0.22,0.93,0.92)]
ledge=[(0.38,0.14,0.62,0.28),(0.38,0.14,0.62,0.28),(0.37,0.14,0.63,0.28),(0.36,0.13,0.69,0.27),
       (0.34,0.13,0.68,0.26),(0.33,0.10,0.67,0.25),(0.33,0.09,0.67,0.24),(0.32,0.07,0.67,0.22)]
roll=[(0.08,0.60,0.31,0.91),(0.10,0.62,0.32,0.91),(0.10,0.66,0.31,0.92),(0.10,0.66,0.32,0.92),
      (0.10,0.66,0.33,0.92),(0.12,0.66,0.36,0.92),(0.12,0.68,0.38,0.93),(0.12,0.68,0.38,0.93)]
d=dict(mediaId=8049,level="B",keyWord="keeper",defaultVoice="male",
 taps=[dict(phrase="to grip a metal bucket",target="the keeper",voice="male",keys=keys(keeper)),
       dict(phrase="to prowl along the ledge",target="the leopard on the ledge",voice="male",keys=keys(ledge)),
       dict(phrase="to sprawl on the gravel",target="the leopard on its back",voice="male",keys=keys(roll))],
 stillS=2.2,
 nouns=[dict(word="a keeper",x=0.42,y=0.37,voice="male"),
        dict(word="a bucket",x=0.79,y=0.46,voice="male"),
        dict(word="visitors",x=0.14,y=0.54,voice="male"),
        dict(word="mountains",x=0.82,y=0.22,voice="male")],
 question="What is the keeper doing?",
 answer=["The","keeper","is","gripping","a","metal","bucket."],answerVoice="male",
 notes="The leopard on the ledge sits behind the keeper's head, so its box is cut along the keeper's head top (keeper's raised bucket hand at 0.2-1.7 s is cut off). It only starts walking around 1.7 s. The rolling leopard's body goes behind the keeper's legs; boxes split at the leg line. The standing (third) leopard is not a target.")
json.dump(d,open("content/8049.json","w"),indent=1)
