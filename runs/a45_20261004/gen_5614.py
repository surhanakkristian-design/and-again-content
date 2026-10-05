import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) if v else dict(t=t,off=True) for t,v in zip(T,b)]
yel=K([(.33,.35,.40,.48),(.44,.34,.31,.48),(.43,.34,.38,.48),(.40,.34,.40,.52),(.42,.34,.38,.52),(.43,.33,.37,.55),(.36,.33,.42,.60),(.44,.30,.35,.66)])
back=K([(0,.36,.24,.43),(.02,.35,.27,.45),(0,.36,.35,.44),(.02,.35,.31,.45),(.09,.35,.27,.45),(.05,.35,.37,.45),(.17,.35,.19,.45),(.22,.35,.22,.44)])
c=dict(mediaId=5614,level="A",keyWord="be different from",defaultVoice="female",
 taps=[dict(phrase="to carry a yellow bag",target="the woman in yellow",voice="female",keys=yel),
       dict(phrase="to drink a green drink",target="the woman in yellow",voice="female",keys=yel),
       dict(phrase="to walk at the back",target="the woman on the left",voice="female",keys=back)],
 stillS=2.2,
 nouns=[dict(word="a plant",x=.55,y=.31,voice="female"),dict(word="flowers",x=.75,y=.43,voice="female"),
        dict(word="windows",x=.40,y=.17,voice="female"),dict(word="a bag",x=.70,y=.56,voice="female")],
 question="What is the woman in yellow wearing?",
 answer=["She","is","wearing","a","yellow","suit."],answerVoice="female",
 notes="'to walk at the back' = the woman with long black hair, last in the line in every frame; at 3.2/3.7 s she overlaps the woman in yellow, boxes split.")
json.dump(c,open("content/5614.json","w"),indent=1)
