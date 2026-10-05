import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(bs): return [({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)}) for t,b in zip(T,bs)]
woman=K([(0,.12,.68,1.0),(0,.13,.68,1.0),(0,.10,.68,1.0),(0,.07,.68,1.0),(0,.05,.68,1.0),(0,.04,.69,1.0),(0,.03,.69,1.0),(0,.03,.70,1.0)])
man=K([(.80,.30,1.0,.47),(.79,.30,1.0,.46),(.80,.29,1.0,.46),(.80,.29,1.0,.46),(.72,.29,1.0,.47),(.72,.28,1.0,.47),(.72,.29,1.0,.47),(.72,.29,1.0,.47)])
d=dict(mediaId=7229,level="B",keyWord="hormone",defaultVoice="female",
 taps=[dict(phrase="to use a pipette",target="the woman",voice="female",keys=woman),
       dict(phrase="to study a printed graph",target="the woman",voice="female",keys=woman),
       dict(phrase="to examine a test tube",target="the young man",voice="male",keys=man)],
 stillS=2.2,
 nouns=[dict(word="safety glasses",x=.33,y=.11,voice="female"),dict(word="a centrifuge",x=.65,y=.53,voice="female"),
        dict(word="test tubes",x=.73,y=.63,voice="female"),dict(word="a graph",x=.45,y=.87,voice="female")],
 question="What is the woman doing?",
 answer=["She","is","studying","a","printed","graph."],answerVoice="female",
 notes="Key word 'hormone' is not a visible noun, so not among the nouns. The young man only holds up the tube from about 2.2 s; before that he works with his head down. Pipette is used 0.2-1.7 s, then lies aside.")
json.dump(d,open("content/7229.json","w"),indent=1)
