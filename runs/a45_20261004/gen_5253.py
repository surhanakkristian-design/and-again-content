import json
times=[i*0.5 for i in range(19)]
def K(B): return [dict(t=t,x=B[t][0],y=B[t][1],w=B[t][2],h=B[t][3]) if t in B else dict(t=t,off=True) for t in times]
CAP={0.0:(.00,.03,1.0,.97),0.5:(.20,.05,.80,.95),1.0:(.30,.09,.70,.91),1.5:(.08,.07,.76,.93),2.0:(.00,.04,.95,.96),2.5:(.15,.10,.65,.90)}
FL={3.0:(.02,.06,.62,.64),3.5:(.00,.06,.68,.64),4.0:(.00,.06,.68,.60)}
BI={4.5:(.03,.17,.97,.64),5.0:(.00,.19,1.0,.67),5.5:(.00,.20,.97,.70)}
c=dict(mediaId=5253,level="A",keyWord="senior",defaultVoice="male",
taps=[dict(phrase="to wear a grey cap",target="the man in the cap",voice="male",keys=K(CAP)),
dict(phrase="to touch orange flowers",target="the woman by the flowers",voice="female",keys=K(FL)),
dict(phrase="to ride a bike",target="the man on the bike",voice="male",keys=K(BI))],
stillS=4.5,nouns=[dict(word="trees",x=.50,y=.10,voice="male"),dict(word="a man",x=.38,y=.38,voice="male"),
dict(word="a bike",x=.78,y=.68,voice="male"),dict(word="a path",x=.40,y=.88,voice="male")],
question="What is the woman doing with flowers?",answer=["She","is","touching","orange","flowers."],answerVoice="female",
notes="Four shots: man in flat cap bouncing along the path (0.0-2.5), white-haired woman touching marigolds (3.0-4.0, not in the description), cyclist (4.5-5.5), dance group (6.0-9.0, no single target, so no phrase there). Cap man: a state phrase because his bouncing walk/arm swing resembles the dancers' moves; nobody else wears a cap. The dancers are many white-haired women, so the question names 'the woman by the flowers'. defaultVoice male: mixed group, evenId false.")
json.dump(c,open('content/5253.json','w'),indent=1)
