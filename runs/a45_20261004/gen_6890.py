import json,sys
def K(rows): return [dict(t=t,x=x,y=y,w=w,h=h) if x is not None else dict(t=t,off=True) for t,x,y,w,h in rows]
car=K([(0.2,0,.30,1.0,.33),(0.7,0,.33,.84,.32),(1.2,0,.33,.84,.32),(1.7,0,.35,.98,.30),(2.2,.24,.35,.64,.29),(2.7,.10,.37,.90,.27),(3.2,.04,.37,.96,.28),(3.7,0,.37,1.0,.28)])
ty=K([(0.2,0,.78,1,.22),(0.7,0,.79,1,.21),(1.2,0,.78,1,.22),(1.7,0,.77,1,.23),(2.2,0,.76,1,.24),(2.7,0,.74,1,.26),(3.2,0,.71,1,.29),(3.7,0,.71,1,.29)])
c=dict(mediaId=6890,level="B",keyWord="brakes",defaultVoice="female",
taps=[dict(phrase="to brake hard on the track",target="the blue car",voice="female",keys=car),
      dict(phrase="to slide along the kerb",target="the blue car",voice="female",keys=car),
      dict(phrase="to lie stacked in the foreground",target="the old tyres",voice="female",keys=ty)],
stillS=3.2,
nouns=[dict(word="a sports car",x=.62,y=.46,voice="female"),dict(word="brakes",x=.43,y=.56,voice="female"),
       dict(word="tyres",x=.50,y=.86,voice="female"),dict(word="a floodlight",x=.85,y=.18,voice="female")],
question="What is the blue car doing?",answer=["The","car","is","sliding","along","the","kerb."],answerVoice="female",
notes="'brakes' pill sits on the glowing front brake disc (one disc visible clearly, rear brake partly). Only target with an action is the car; tyres phrase is a state. Floodlight pill on the top-right light mast.")
json.dump(c,open('content/6890.json','w'),indent=1)
