import json
T=[i/2 for i in range(21)]
TOP=[.75,.72,.72,.72,.71,.71,.73,.72,.67,.71,.72,.71,.70,.70,.70,.54,.39,.63,.68,.68,.69]
k=[dict(t=t,x=0.0,y=y,w=1.0,h=round(1-y,2)) for t,y in zip(T,TOP)]
c=dict(mediaId=4832,level="B",keyWord="ridge",defaultVoice="male",
 taps=[dict(phrase="to walk along a narrow ridge",target="the climber",voice="male",keys=k),
       dict(phrase="to grip two trekking poles",target="the climber",voice="male",keys=k),
       dict(phrase="to follow a trail of footprints",target="the climber",voice="male",keys=k)],
 stillS=1.0,
 nouns=[dict(word="the sky",x=.50,y=.15,voice="male"),dict(word="a summit",x=.55,y=.41,voice="male"),
        dict(word="clouds",x=.15,y=.50,voice="male"),dict(word="a ridge",x=.45,y=.63,voice="male")],
 question="What is the climber doing?",
 answer=["He","is","walking","along","a","narrow","ridge."],answerVoice="male",
 notes="Helmet-camera view: the only target is the climber himself (red legs, boots, gloved hands and poles at the bottom), so all three phrases use him; his box spans the full width because his hands and poles appear at both edges. Poles are clearly visible at e.g. 0.0, 2.5, 4.5, 8.0, 8.5 s.")
json.dump(c,open('content/4832.json','w'),indent=1)
