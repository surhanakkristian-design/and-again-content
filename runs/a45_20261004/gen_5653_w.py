import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [dict(t=t,x=a,y=b,w=round(c-a,2),h=round(d-b,2)) for t,(a,b,c,d) in zip(T,l)]
woman=K([(.47,.18,.95,.73),(.47,.19,.97,.72),(.47,.20,.95,.73),(.47,.17,.93,.76),(.56,.13,.98,.73),(.54,.11,.96,.71),(.55,.12,.98,.73),(.54,.11,.96,.73)])
pump=K([(.08,.40,.47,.69),(.10,.40,.47,.69),(.09,.40,.47,.69),(.09,.40,.47,.69),(.09,.40,.55,.70),(.09,.40,.53,.70),(.07,.40,.52,.71),(.07,.40,.52,.71)])
spec=K([(.0,.11,.40,.40)]*2+[(.0,.11,.38,.40)]*2+[(.0,.11,.42,.40)]*4)
c=dict(mediaId=5653,level="B",keyWord="bigger",defaultVoice="female",
 taps=[dict(phrase="to push a giant pumpkin",target="the woman",voice="female",keys=woman),
       dict(phrase="to tower over a small pumpkin",target="the giant pumpkin",voice="female",keys=pump),
       dict(phrase="to shade their eyes",target="the spectators",voice="female",keys=spec)],
 stillS=3.7,
 nouns=[dict(word="spectators",x=0.17,y=0.22,voice="female"),dict(word="a chalkboard",x=0.37,y=0.37,voice="female"),
        dict(word="a giant pumpkin",x=0.33,y=0.52,voice="female"),dict(word="a pallet",x=0.52,y=0.71,voice="female")],
 question="What is the woman doing?",
 answer="She is pushing a giant pumpkin onto a pallet.".split(),
 answerVoice="female",
 notes="Key word 'bigger' is an adjective, not used as a noun. Spectators = group of older people behind the rope (several shade their eyes / hold their heads). Woman's hands overlap the pumpkin while pushing: boxes split at x 0.47.")
json.dump(c,open('content/5653.json','w'),indent=1)
