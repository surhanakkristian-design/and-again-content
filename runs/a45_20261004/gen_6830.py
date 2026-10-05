import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l):
    return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,l)]
hull=K([(0.08,0,0.62,0.70),(0.11,0,0.61,0.74),(0.14,0,0.61,0.78),(0.16,0.01,0.61,0.80),(0.16,0.02,0.64,0.82),(0.17,0.03,0.62,0.81),(0.16,0.05,0.63,0.78),(0.15,0.05,0.66,0.79)])
fork=K([(0.70,0.56,0.18,0.15),(0.72,0.61,0.18,0.15),(0.75,0.65,0.18,0.15),(0.77,0.70,0.18,0.15),(0.80,0.71,0.18,0.17),(0.79,0.74,0.19,0.16),(0.79,0.75,0.18,0.14),(0.81,0.76,0.18,0.14)])
c=dict(mediaId=6830,level="B",keyWord="aluminum",defaultVoice="female",
 taps=[dict(phrase="to hang from ropes",target="the boat hull",voice="female",keys=hull),
       dict(phrase="to turn slowly in the air",target="the boat hull",voice="female",keys=hull),
       dict(phrase="to stand idle by the doors",target="the forklift",voice="female",keys=fork)],
 stillS=3.2,
 nouns=[dict(word="aluminum",x=0.45,y=0.35,voice="female"),dict(word="a corrugated roof",x=0.80,y=0.13,voice="female"),
        dict(word="a forklift",x=0.86,y=0.82,voice="female"),dict(word="a hard hat",x=0.10,y=0.82,voice="female")],
 question="What is the boat hull doing?",answer=["The","hull","is","hanging","from","ropes."],answerVoice="female",
 notes="No main person (several small workers who all hold ropes and look up, so no worker phrase fits only one) -> targets are the hull and the forklift; defaultVoice female (evenId). The hull box is cut on the right where its rectangle would cover the forklift (0.2-0.7 the hull's upper right edge, x>0.70, is outside its box). The orange worker stands in front of the forklift at 0.2-0.7, so his tap lands in the forklift box. Key word 'aluminum' placed on the shiny hull at the still.")
json.dump(c,open('content/6830.json','w'),indent=1)
