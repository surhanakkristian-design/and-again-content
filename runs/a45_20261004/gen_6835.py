import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
hawk=K([(.75,.12,.20,.16),(.73,.13,.20,.16),(.70,.12,.20,.16),(.67,.12,.20,.16),(.63,.11,.20,.16),(.58,.11,.20,.16),(.53,.12,.20,.16),(.47,.10,.20,.16)])
horses=K([(.52,.35,.42,.14),(.47,.35,.48,.14),(.42,.35,.52,.14),(.35,.35,.56,.14),(.29,.35,.60,.15),(.27,.35,.62,.15),(.24,.35,.60,.15),(.02,.35,.79,.15)])
pod=K([(.22,.52,.26,.18),(.22,.52,.26,.18),(.20,.54,.28,.20),(.16,.54,.28,.20),(.00,.56,.44,.24),(.06,.56,.38,.24),(.00,.58,.40,.26),(.00,.62,.35,.34)])
c=dict(mediaId=6835,level="B",keyWord="annual",defaultVoice="male",
 taps=[dict(phrase="to scatter tiny seeds",target="the seed pod",voice="male",keys=pod),
       dict(phrase="to gallop across the plain",target="the horses",voice="male",keys=horses),
       dict(phrase="to soar above the mountains",target="the hawk",voice="male",keys=hawk)],
 stillS=2.2,
 nouns=[dict(word="a hawk",x=.72,y=.19,voice="male"),dict(word="horses",x=.55,y=.43,voice="male"),
        dict(word="poppies",x=.45,y=.58,voice="male"),dict(word="a tortoise",x=.90,y=.69,voice="male")],
 question="What are the horses doing?",
 answer=["The","horses","are","galloping","across","the","plain."],answerVoice="male",
 notes="Key word 'annual' (plant) not a placeable noun, left out. Seed pod bursts at 0.2-0.7 s; later frames show the open pod only.")
json.dump(c,open("content/6835.json","w"),indent=1)
