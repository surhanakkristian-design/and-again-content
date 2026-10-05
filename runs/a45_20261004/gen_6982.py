import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
man=K([(.25,.14,.37,.76),(.25,.15,.38,.76),(.25,.14,.38,.80),(.22,.14,.41,.80),(.19,.13,.44,.82),(.19,.13,.43,.82),(.19,.14,.44,.85),(.19,.14,.45,.85)])
chef=K([(.63,.48,.26,.32),(.64,.48,.26,.32),(.64,.49,.26,.31),(.64,.49,.26,.31),(.64,.48,.26,.32),(.63,.49,.26,.31),(.64,.49,.27,.31),(.65,.48,.26,.32)])
taps=[dict(phrase="to sketch a flowchart",target="the man in the suit",voice="male",keys=man),
      dict(phrase="to scribble on a clipboard",target="the man in the suit",voice="male",keys=man),
      dict(phrase="to fold his arms sceptically",target="the head chef",voice="male",keys=chef)]
c=dict(mediaId=6982,level="B",keyWord="consultant",defaultVoice="male",taps=taps,stillS=2.2,
 nouns=[dict(word="a consultant",x=.32,y=.40,voice="male"),dict(word="a flip chart",x=.78,y=.22,voice="male"),
        dict(word="flames",x=.55,y=.61,voice="male"),dict(word="a ladle",x=.62,y=.93,voice="male")],
 question="What is the consultant doing?",answer="He is scribbling on a clipboard.".split(),answerVoice="male",
 notes="Man's box is cut at the head chef's left edge, so his raised drawing hand (x ~.66-.73, top) at 0.2-1.2 s lies partly outside it. Flowchart drawing only 0.2-1.2 s; clipboard writing 1.7-3.7 s. 'a consultant' is a male-person noun -> male voice.")
json.dump(c,open('content/6982.json','w'),indent=1)
