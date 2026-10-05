import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,l)]
woman=[(.31,.31,.36,.51),(.44,.31,.29,.51),(.45,.38,.38,.36),(.44,.37,.40,.35),(.78,.35,.18,.27),None,None,None]
man=[(.67,.27,.17,.45),(.73,.27,.15,.45),(.66,.23,.18,.14),(.66,.23,.18,.14),(.48,.24,.30,.48),(.58,.33,.27,.22),(.66,.38,.19,.16),None]
lamp=[(.64,.03,.18,.14),(.63,.02,.18,.14),(.62,.01,.19,.14),(.61,0,.19,.14),(.62,0,.18,.14),(.62,0,.18,.14),(.62,0,.18,.14),(.62,0,.18,.14)]
c=dict(mediaId=5597,level="B",keyWord="back door",defaultVoice="female",taps=[
 dict(phrase="to signal for silence",target="the woman",voice="female",keys=K(woman)),
 dict(phrase="to pull the door shut",target="the man",voice="male",keys=K(man)),
 dict(phrase="to glow above the door",target="the wall lamp",voice="female",keys=K(lamp))],
 stillS=0.2,nouns=[dict(word="a back door",x=.56,y=.29,voice="female"),dict(word="a fire escape",x=.30,y=.19,voice="female"),
 dict(word="a wall lamp",x=.72,y=.09,voice="female"),dict(word="crates",x=.80,y=.83,voice="female")],
 question="What is the woman doing?",answer=["She","is","sneaking","through","the","back","door."],answerVoice="female",
 notes="Cut-free clip. The man's dark-jacket arm pulls the door shut from 2.2 (zoom-checked); at 2.2 the woman's face peeks out right under his head, so the split is at x .78: his head is half in his box, her face in hers. At 1.2/1.7 his head is just above hers, his box is the strip above her (y .23-.37). Woman gone from 2.7, man gone at 3.7 (door closed). Phrase 1 = her finger on her lips (0.2-1.7).")
json.dump(c,open('content/5597.json','w'),indent=1)
