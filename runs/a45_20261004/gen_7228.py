import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(bs): return [({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)}) for t,b in zip(T,bs)]
bride=K([(.35,.18,1.0,.82),(.37,.19,1.0,.82),(.50,.03,1.0,.86),(.53,0,1.0,.93),(.62,0,1.0,.80),(.82,0,1.0,.72),(.70,.03,1.0,.72),(.70,.08,1.0,.68)])
guests=K([(.33,0,.92,.17),(.33,0,1.0,.18),(.33,0,.49,.36),(.33,0,.52,.36),(.35,0,.60,.34),(.34,0,.81,.32),(.30,0,.68,.28),(.27,0,.68,.27)])
swan=K([(.16,.37,.34,.51),(.18,.36,.36,.50),(.17,.36,.36,.50),(.16,.36,.34,.50),(.13,.34,.31,.48),(.10,.33,.28,.47),(.06,.31,.24,.45),(.02,.29,.20,.43)])
d=dict(mediaId=7228,level="B",keyWord="hook",defaultVoice="female",
 taps=[dict(phrase="to fasten a tow hook",target="the bride",voice="female",keys=bride),
       dict(phrase="to applaud from the roof",target="the guests",voice="female",keys=guests),
       dict(phrase="to glide across the floodwater",target="the swan",voice="female",keys=swan)],
 stillS=0.2,
 nouns=[dict(word="a tractor",x=.13,y=.34,voice="female"),dict(word="a swan",x=.29,y=.44,voice="female"),
        dict(word="a bride",x=.62,y=.35,voice="female"),dict(word="a tow hook",x=.74,y=.70,voice="female")],
 question="What is the bride doing?",
 answer=["She","is","fastening","a","tow","hook","to","the","bumper."],answerVoice="female",
 notes="Key word 'hook' is a verb here; used 'to fasten a tow hook' + noun 'a tow hook'. Guests group box split from bride where they overlap (1.2-3.7 only left part of the guests). Swan small, min-size boxes.")
json.dump(d,open("content/7228.json","w"),indent=1)
