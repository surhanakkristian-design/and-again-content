import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) if v else dict(t=t,off=True) for t,v in zip(T,b)]
man=K([(0,.22,.66,.78),(0,.21,.65,.79),(0,.22,.70,.78),(0,.32,.68,.68),(0,.34,.68,.66),(0,.28,.69,.72),(0,.24,.70,.76),(0,.21,.72,.79)])
c=dict(mediaId=5617,level="A",keyWord="be good at",defaultVoice="male",
 taps=[dict(phrase="to cut wood",target="the bearded man",voice="male",keys=man),
       dict(phrase="to hold a wooden hammer",target="the bearded man",voice="male",keys=man),
       dict(phrase="to look at his tool",target="the bearded man",voice="male",keys=man)],
 stillS=0.2,
 nouns=[dict(word="a saw",x=.65,y=.14,voice="male"),dict(word="a hammer",x=.40,y=.46,voice="male"),
        dict(word="a table",x=.75,y=.62,voice="male"),dict(word="an apron",x=.27,y=.66,voice="male")],
 question="What is the bearded man doing?",
 answer=["He","is","cutting","wood."],answerVoice="male",
 notes="All three phrases on the bearded man: the four young men only watch and lean on benches, no action fits only one of them. 'a hammer' = the wooden mallet (A level). 'to look at his tool' = 2.7-3.7 s he lifts the chisel and looks at it.")
json.dump(c,open("content/5617.json","w"),indent=1)
