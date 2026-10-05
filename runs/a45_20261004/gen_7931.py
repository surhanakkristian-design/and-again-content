import json
T=[0.2,0.7,1.2,1.7,2.2]
wom=[(.71,.43,.24,.42),(.64,.45,.23,.40),(.57,.46,.22,.40),(.50,.46,.20,.38),(.35,.45,.27,.37)]
man=[(.29,.39,.19,.32),(.32,.43,.18,.28),(.38,.45,.18,.26),(.32,.46,.18,.24),None]
def K(b): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,b)]
c=dict(mediaId=7931,level="A",keyWord="past",defaultVoice="female",
 taps=[dict(phrase="to ride past a tractor",target="the woman",voice="female",keys=K(wom)),
       dict(phrase="to wear a helmet",target="the woman",voice="female",keys=K(wom)),
       dict(phrase="to drive a tractor",target="the man",voice="male",keys=K(man))],
 stillS=0.7,
 nouns=[dict(word="the sky",x=.35,y=.10,voice="female"),dict(word="mountains",x=.25,y=.32,voice="female"),
        dict(word="a tractor",x=.15,y=.62,voice="female"),dict(word="a bike",x=.78,y=.76,voice="female")],
 question="What is the woman doing?",answer=["She","is","riding","past","a","tractor."],answerVoice="female",
 notes="Key word 'past' used in phrase 1 and the answer. The man sits in the tractor cab; at 1.7 s the woman starts to cover him (box cut at her edge) and at 2.2 s he is hidden behind her -> off. 'to wear a helmet' is a state, but only she wears one. The cow appears only at the very left edge at 2.2 s and is not used.")
json.dump(c,open('content/7931.json','w'),indent=1)
