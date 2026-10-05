import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
man=K([(0,.15,.72,.55),(0,.14,.76,.56),(0,.12,.74,.58),(0,.08,.76,.62),(0,.06,.77,.64),(0,.04,.78,.66),(0,.02,.78,.68),(0,.02,.80,.73)])
cat=K([(.55,.71,.40,.19),(.55,.71,.41,.19),(.56,.71,.42,.21),(.52,.73,.48,.21),(.58,.75,.42,.21),(.58,.76,.42,.22),(.58,.78,.42,.22),(.60,.79,.40,.21)])
lamp=K([(.73,.21,.22,.19),(.77,.21,.20,.19),(.75,.22,.21,.17),(.77,.19,.22,.19),(.79,.18,.21,.17),(.79,.18,.21,.17),(.79,.16,.21,.18),(.81,.17,.19,.18)])
d=dict(mediaId=7112,level="B",keyWord="figure",defaultVoice="male",
taps=[dict(phrase="to paint a tiny figure",target="the man",voice="male",keys=man),
 dict(phrase="to doze on a stool",target="the cat",voice="male",keys=cat),
 dict(phrase="to cast a warm glow",target="the desk lamp",voice="male",keys=lamp)],
stillS=1.2,
nouns=[dict(word="a figure",x=.67,y=.47,voice="male"),dict(word="a desk lamp",x=.84,y=.30,voice="male"),
 dict(word="a glass dome",x=.35,y=.68,voice="male"),dict(word="a cat",x=.78,y=.83,voice="male")],
question="What is the young man doing?",answer=["He","is","painting","a","tiny","figure."],answerVoice="male",
notes="Man paints the figure at 0.2-1.2, then lifts and studies it, sets it down at 3.7. 'a figure' pill on the painted figure in his hand; many grey unpainted figures on the left table are also figures (no other noun on them). Two glass domes (front left one labelled). Lamp box trimmed on its left edge where the man's hand is near.")
json.dump(d,open("content/7112.json","w"),indent=1)
