import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
goat=K([(0,.10,.60,.39),(0,.10,.60,.40),(0,.02,.52,.52),(0,.02,.52,.56),(0,.15,.62,.45),(0,.13,.62,.47),(0,.13,.61,.48),(0,.13,.61,.48)])
woman=K([(.60,.29,.31,.54),(.60,.29,.31,.55),(.55,.40,.37,.50),(.58,.44,.36,.52),(.63,.46,.32,.53),(.63,.46,.33,.54),(.62,.46,.33,.54),(.62,.46,.34,.54)])
c=dict(mediaId=6870,level="B",keyWord="billy",defaultVoice="female",taps=[
 dict(phrase="to perch on a car roof",target="the billy goat",voice="female",keys=goat),
 dict(phrase="to snatch a carrot",target="the billy goat",voice="female",keys=goat),
 dict(phrase="to hold out a carrot",target="the woman",voice="female",keys=woman)],
 stillS=3.2,
 nouns=[dict(word="a billy goat",x=.22,y=.33,voice="female"),dict(word="a stone cottage",x=.87,y=.44,voice="female"),
        dict(word="a vintage car",x=.25,y=.78,voice="female"),dict(word="rubber boots",x=.72,y=.93,voice="female")],
 question="What is the billy goat standing on?",
 answer=["It","is","standing","on","a","vintage","car."],answerVoice="female",
 notes="key word 'billy' used as 'billy goat'. Woman holds out the carrot only at 0.2-0.7 s; later she holds it low/looks up. Goat rears up 1.2-1.7 s.")
json.dump(c,open('content/6870.json','w'),indent=1)
