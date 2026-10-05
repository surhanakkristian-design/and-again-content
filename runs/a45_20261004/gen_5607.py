import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
horse=K([(0.12,0.41,0.41,0.21),(0.09,0.41,0.46,0.21),(0.09,0.38,0.50,0.25),(0.11,0.38,0.47,0.24),(0.11,0.38,0.47,0.24),(0.09,0.40,0.47,0.22),(0.12,0.40,0.45,0.23),(0.14,0.41,0.42,0.22)])
cart=K([(0.70,0.34,0.22,0.14)]*8)
ban=K([(0.64,0.49,0.36,0.16),(0.64,0.49,0.36,0.14),(0.77,0.50,0.23,0.19),(0.73,0.50,0.27,0.19),(0.70,0.49,0.30,0.18),(0.71,0.49,0.29,0.17),(0.60,0.49,0.40,0.16),(0.62,0.49,0.38,0.16)])
c=dict(mediaId=5607,level="B",keyWord="battlefield",defaultVoice="male",
 taps=[dict(phrase="to graze on dry grass",target="the horse",voice="male",keys=horse),
       dict(phrase="to go up in flames",target="the cart",voice="male",keys=cart),
       dict(phrase="to flutter in the wind",target="the banner",voice="male",keys=ban)],
 stillS=2.2,
 nouns=[dict(word="a castle",x=0.28,y=0.34,voice="male"),dict(word="a horse",x=0.36,y=0.47,voice="male"),
        dict(word="a banner",x=0.86,y=0.58,voice="male"),dict(word="shields",x=0.25,y=0.84,voice="male")],
 question="What is the horse doing?",answer=["The","horse","is","grazing","on","the","battlefield."],answerVoice="male",
 notes="No people; defaultVoice male (evenId false). Cart is small and far (min box); banner box starts below the cart box, pole tip excluded.")
json.dump(c,open('content/5607.json','w'),indent=1)
