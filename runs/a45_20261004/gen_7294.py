import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,boxes)]
woman=K([(0.06,0.28,0.62,0.35),(0.05,0.29,0.64,0.35),(0.05,0.31,0.63,0.37),(0.06,0.32,0.66,0.38),
         (0.03,0.30,0.69,0.43),(0.01,0.29,0.73,0.46),(0.01,0.25,0.71,0.49),(0.23,0.25,0.54,0.49)])
dog=K([(0.42,0.12,0.18,0.14),(0.42,0.12,0.18,0.14),(0.43,0.14,0.18,0.14),(0.45,0.12,0.18,0.14),
       (0.46,0.08,0.18,0.14),(0.46,0.07,0.18,0.14),(0.46,0.07,0.18,0.14),(0.48,0.04,0.18,0.14)])
hx=[0.69,0.70,0.69,0.73,0.73,0.75,0.73,0.78]
hose=K([(x,0.59,round(1-x,2),0.14) for x in hx])
c=dict(mediaId=7294,level="B",keyWord="lining",defaultVoice="female",
 taps=[dict(phrase="to smooth out the creases",target="the woman in white",voice="female",keys=woman),
       dict(phrase="to peek over the edge",target="the dog",voice="female",keys=dog),
       dict(phrase="to spray the pond lining",target="the garden hose",voice="female",keys=hose)],
 stillS=0.7,
 nouns=[dict(word="a dog",x=0.52,y=0.19,voice="female"),
        dict(word="lining",x=0.80,y=0.33,voice="female"),
        dict(word="a brick",x=0.59,y=0.76,voice="female"),
        dict(word="a spade",x=0.83,y=0.86,voice="female")],
 question="What is the woman in white doing?",
 answer=["She","is","smoothing","out","the","creases."],
 answerVoice="female",
 notes="Main person is the woman in the pond (white top); other two women at the rim wear grey/dark tops, the man at the rim wears a white T-shirt (man, not woman). Hose box sits right of the woman's box (split at her shorts/feet).")
json.dump(c,open('content/7294.json','w'),indent=1)
