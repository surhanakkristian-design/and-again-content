import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
N=(None,)*4
def K(l): return [dict(t=t,x=a,y=b,w=c,h=d) if a is not None else dict(t=t,off=True) for t,(a,b,c,d) in zip(T,l)]
cr=K([(.48,.39,.45,.44),(.47,.39,.47,.45),(.44,.39,.50,.52),(.41,.38,.55,.56),(.37,.37,.61,.62),(.34,.34,.66,.66),(.28,.32,.72,.68),(.28,.31,.72,.69)])
lp=K([(.46,.24,.22,.14),(.48,.25,.21,.14),(.43,.20,.25,.18),(.41,.21,.35,.16),(.50,.20,.32,.17),N,N,N])
c=dict(mediaId=6897,level="B",keyWord="break up",defaultVoice="male",
 taps=[dict(phrase="to turn the valve key",target="the crouching man",voice="male",keys=cr),
       dict(phrase="to leap over a hedge",target="the jumping man",voice="male",keys=lp),
       dict(phrase="to stare into the camera",target="the crouching man",voice="male",keys=cr)],
 stillS=0.2,
 nouns=[dict(word="a gazebo",x=.38,y=.21,voice="male"),dict(word="a blanket",x=.30,y=.30,voice="male"),
        dict(word="a rainbow",x=.22,y=.70,voice="male"),dict(word="a flip-flop",x=.87,y=.87,voice="male")],
 question="What is the crouching man doing?",answer="He is turning the valve key.".split(),answerVoice="male",
 notes="Jumping man = the man in the grey T-shirt and black shorts who runs towards and leaps over the hedge (clear leap at 1.2-1.7); at 1.7-2.2 his legs are behind the crouching man's head, so his box is cut there; off from 2.7 (only a blurred sliver at the right edge at 2.7). Dog and the two women with the blanket not used as targets (women are a pair). 'Valve key' = the T-shaped metal key in the sprinkler valve.")
json.dump(c,open('content/6897.json','w'),indent=1)
