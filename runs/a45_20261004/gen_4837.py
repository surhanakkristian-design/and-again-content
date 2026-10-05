import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
W={0.0:(.28,0,.72,.58),0.5:(.36,0,.64,.56),1.0:(.32,.04,.68,.48),1.5:(.20,.08,.80,.44),2.0:(.17,.10,.83,.43),2.5:(.40,.16,.60,.33),
4.0:(.80,.06,.20,.30),4.5:(.82,0,.18,.30),5.0:(.82,0,.18,.30),5.5:(.82,0,.18,.30),6.0:(.62,0,.38,.26),6.5:(.72,0,.28,.24),7.0:(.60,0,.40,.30),
7.5:(.28,.05,.18,.40),8.0:(.19,.10,.19,.30),8.5:(0,.08,.17,.34),10.0:(.82,.10,.18,.46)}
M={2.5:(0,.12,.18,.24),3.0:(.03,0,.43,.32),3.5:(.02,0,.38,.33),4.0:(0,0,.24,.17),4.5:(0,0,.18,.14),5.0:(0,0,.18,.14),5.5:(0,0,.18,.14),
7.5:(.58,.04,.30,.32),8.0:(.38,.06,.30,.26),8.5:(.18,.05,.26,.28),9.0:(0,.09,.30,.27),9.5:(0,.18,.18,.14)}
X={6.0:(.28,.38,.72,.50),6.5:(.30,.40,.70,.47),7.0:(.28,.42,.72,.50)}
def keys(D):
    return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else dict(t=t,off=True) for t in T]
c=dict(mediaId=4837,level="A",keyWord="table",defaultVoice="male",
 taps=[dict(phrase="to hand over some pizza",target="the woman in the checked shirt",voice="female",keys=keys(W)),
       dict(phrase="to stand at the table",target="the man in the white T-shirt",voice="male",keys=keys(M)),
       dict(phrase="to wear a watch",target="the man with the watch",voice="male",keys=keys(X))],
 stillS=10.0,
 nouns=[dict(word="a salad",x=.13,y=.45,voice="male"),dict(word="a pizza",x=.58,y=.58,voice="male"),
        dict(word="a chicken",x=.25,y=.80,voice="male"),dict(word="a table",x=.45,y=.93,voice="male")],
 question="What are the friends doing?",
 answer=["They","are","eating","at","a","big","table."],answerVoice="male",
 notes="Fast-cut dinner-party clip, the camera swings round the table so people change place. 'the woman in the checked shirt' = the long-haired woman who hands over the pizza slice (0-2.5 s, top right later); at 7.5-8.5 s a woman in a red checked shirt behind the man in the green shirt is boxed too (may be a different woman, but she also wears a checked shirt). 'the man in the white T-shirt' stands and serves at 3.0-3.5 s, is seated in the background later; 2.5 s left-edge man is a guess. 'the man with the watch' = only an arm with a watch holding the loaf at 6.0-7.0 s; chosen as a state because several hands pass plates and touch the bread.")
json.dump(c,open('content/4837.json','w'),indent=1)
