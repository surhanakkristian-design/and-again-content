import json
T=[i*0.5 for i in range(21)]
O=None
wom=[(0,.25,.75,.25),(0,.17,.66,.45),(0,.03,.92,.97),(0,.05,1,.95),(0,0,.22,.14),(0,.04,.22,.14),(0,.08,.20,.14),(0,.09,.22,.14),(0,.58,.72,.30),(0,.45,.88,.55),(0,.62,.78,.38),(0,.15,1,.85),(0,.12,1,.88),(0,.03,1,.97),(0,.05,.97,.95),(0,.05,.80,.95),(0,.17,.67,.83),(0,.20,.54,.80),(0,.18,.54,.66),(0,.18,.61,.64),(0,.17,.59,.64)]
man=[O]*16+[(.68,.10,.32,.63),(.57,.15,.43,.62),(.55,.17,.45,.66),(.62,.17,.38,.64),(.60,.14,.40,.63)]
cat=[O]*16+[(.76,.78,.24,.22),(.55,.79,.45,.21),(.42,.85,.50,.15),(.42,.83,.50,.17),(.38,.82,.62,.18)]
def k(b): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,b)]
d=dict(mediaId=478,level="A",keyWord="milk",defaultVoice="female",
 taps=[dict(phrase="to open the bottle",target="the woman",voice="female",keys=k(wom)),
       dict(phrase="to have a beard",target="the man",voice="male",keys=k(man)),
       dict(phrase="to drink from a bowl",target="the cat",voice="female",keys=k(cat))],
 stillS=10.0,
 nouns=[dict(word="milk",x=.52,y=.65,voice="female"),dict(word="a cat",x=.68,y=.88,voice="female"),
        dict(word="flowers",x=.35,y=.43,voice="female"),dict(word="a window",x=.38,y=.17,voice="female")],
 question="What is the cat doing?",
 answer=["It","is","drinking","milk","from","a","bowl."],answerVoice="female",
 notes="Many cuts. 0-5 s show only the woman's hand/arm (2.0-3.5 s just a bit of her hand top left), so her box there is the hand. Man and cat appear only from 8.0 s. 'to have a beard' is a state: both people drink and clink, no action fits only the man. 'milk' pill sits on the two glasses; the cat's bowl also holds milk but no other noun names the bowl.")
json.dump(d,open("content/478.json","w"),indent=1)
