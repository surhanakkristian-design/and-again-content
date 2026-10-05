import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
N=(None,)*4
def K(l): return [dict(t=t,x=a,y=b,w=c,h=d) if a is not None else dict(t=t,off=True) for t,(a,b,c,d) in zip(T,l)]
pig=K([(.40,.22,.59,.52),(.46,.44,.54,.38),(.56,.45,.44,.38),(.33,.38,.67,.52),(0,.43,.90,.42),(0,.51,.25,.49),(0,.50,.97,.38),(0,.50,1.0,.50)])
wom=K([(0,.38,.40,.24),(.04,.46,.42,.29),(.07,.58,.38,.21),(.08,.55,.25,.21),N,(.25,.47,.23,.24),(.22,.35,.23,.15),(.23,.34,.26,.16)])
c=dict(mediaId=6898,level="B",keyWord="break",defaultVoice="female",
 taps=[dict(phrase="to leap into the air",target="the prize pig",voice="female",keys=pig),
       dict(phrase="to dive after the pig",target="the young woman",voice="female",keys=wom),
       dict(phrase="to scramble over the edge",target="the prize pig",voice="female",keys=pig)],
 stillS=1.2,
 nouns=[dict(word="clouds",x=.50,y=.15,voice="female"),dict(word="clipboards",x=.25,y=.54,voice="female"),
        dict(word="a rosette",x=.64,y=.63,voice="female"),dict(word="a sash",x=.55,y=.77,voice="female")],
 question="What is the prize pig doing?",answer="It is escaping from the show ring.".split(),answerVoice="female",
 notes="Prize pig = the big pink pig with rosettes (other pigs in the background). Young woman = the one in the white coat who dives (background handlers also wear white coats but stand far away). Pig leaps at 0.2 only; scrambles over the ring edge at 2.2 and 3.2-3.7. Woman off at 2.2 (pig fills the frame); at 0.2/0.7/1.7/2.7 her box is split from the pig's at the line between them (pig ear tip at 1.7 cut slightly). At 3.2-3.7 only her upper body shows above the pig. Several rosettes on the pig: the pill sits on the red one on its shoulder; the sash lies on the ground.")
json.dump(c,open('content/6898.json','w'),indent=1)
