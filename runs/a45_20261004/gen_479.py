import json
T=[i*0.5 for i in range(21)]
O=None
F=(0,0,1,1)
girl=[(0,.30,.53,.47),(0,.30,.56,.45),(0,.30,.50,.55),(.02,.30,.58,.56),(0,.27,.78,.60),(.02,.27,.96,.62),(0,.34,.95,.66),O,O,O,O,(0,.31,1,.69),(0,.17,1,.83),(0,0,.88,.72),(0,.22,.23,.78),(0,.27,.18,.73),(0,.22,.18,.76),(0,.22,.18,.31),(0,.32,1,.68),(0,.32,1,.68),(0,.30,1,.70)]
man=[(.55,.18,.45,.82),(.57,.18,.43,.82),(.52,.18,.48,.82),(.62,.18,.38,.82)]+[O]*10+[(.25,.22,.75,.58),(.28,.22,.72,.58),(.25,.19,.75,.60),(.14,.54,.86,.27),O,O,O]
bub=[O]*6+[(.17,0,.64,.33),F,F,F,F,(.15,0,.68,.30),(.17,0,.66,.16),O,(0,0,.18,.19),(0,0,.18,.16),(0,0,.18,.18),(0,0,.18,.16),(.15,0,.70,.31),(.17,0,.70,.31),O]
def k(b): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,b)]
d=dict(mediaId=479,level="B",keyWord="mind",defaultVoice="female",
 taps=[dict(phrase="to tap her temple",target="the girl",voice="female",keys=k(girl)),
       dict(phrase="to slump onto the chessboard",target="the man",voice="male",keys=k(man)),
       dict(phrase="to float above her head",target="the thought bubble",voice="female",keys=k(bub))],
 stillS=3.0,
 nouns=[dict(word="a thought bubble",x=.48,y=.14,voice="female"),dict(word="glasses",x=.57,y=.52,voice="female"),
        dict(word="chess pieces",x=.55,y=.86,voice="female"),dict(word="curly hair",x=.20,y=.43,voice="female")],
 question="What is the girl picturing?",
 answer=["She","is","picturing","the","chessboard","in","her","mind."],answerVoice="female",
 notes="Cuts: 3.5-5.0 s the thought bubble fills the whole picture (box = full frame, girl off). 7.0-8.5 s only the edge of the girl (hair, sleeve) at the left and a corner of the bubble top left are in the picture; boxes kept small there, verifier may prefer 'off'. The opponent is a shaved-headed young man/teen, called 'the man'. 'chess pieces' pill sits on the pieces on the table; the bubble also shows pieces. 'mind' is not a visible noun, it is used in the answer.")
json.dump(d,open("content/479.json","w"),indent=1)
