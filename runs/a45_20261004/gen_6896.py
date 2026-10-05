import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
N=(None,)*4
def K(l): return [dict(t=t,x=a,y=b,w=c,h=d) if a is not None else dict(t=t,off=True) for t,(a,b,c,d) in zip(T,l)]
cow=K([(.06,.23,.51,.48),(.01,.20,.63,.51),(0,.18,.63,.53),(0,.14,.97,.56),(.21,.21,.79,.50),(.37,.23,.63,.47),(.48,.30,.52,.39),(.50,.32,.50,.37)])
wom=K([(.58,.37,.30,.32),(.66,.37,.24,.31),(.65,.38,.22,.29),N,N,(.19,.40,.18,.25),(.18,.40,.18,.25),(.18,.41,.18,.23)])
man=K([N,N,N,N,(.03,.45,.18,.18),(0,.45,.18,.18),(0,.45,.17,.19),(0,.44,.17,.19)])
c=dict(mediaId=6896,level="B",keyWord="break away",defaultVoice="female",
 taps=[dict(phrase="to charge across the grass",target="the runaway cow",voice="female",keys=cow),
       dict(phrase="to reach for the loose rope",target="the woman with braids",voice="female",keys=wom),
       dict(phrase="to wave a black hat",target="the man with the hat",voice="male",keys=man)],
 stillS=0.2,
 nouns=[dict(word="a cow",x=.22,y=.50,voice="female"),dict(word="a lead rope",x=.50,y=.40,voice="female"),
        dict(word="a white coat",x=.76,y=.50,voice="female"),dict(word="a bucket",x=.57,y=.64,voice="female")],
 question="What is the runaway cow doing?",answer="It is charging across the grass.".split(),answerVoice="female",
 notes="Runaway cow = the ginger Highland cow without a handler (other Highland cattle stand on the right and later along the fence). Woman with braids hidden behind the cow at 1.7-2.2 (off); at 1.2 the cow box is cut at x .63 so the right horn tip is outside, to keep it off her box. Reaching for the rope is only clear at 0.2 (her arm stretched towards the flying rope). The man with the hat is small, left edge, from 2.2 (hat waved at 2.2-2.7, at 3.2-3.7 less clear). Cow pill also covers its body only (no other noun there).")
json.dump(c,open('content/6896.json','w'),indent=1)
