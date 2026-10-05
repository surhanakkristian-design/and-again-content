import json
T=[i*0.5 for i in range(19)]
G=[(.08,.12,.90,.88),(0,.12,1,.88),(.05,.12,.95,.88),(.08,.07,.92,.93),(0,.03,1,.97),(.18,.09,.62,.53),(.23,.06,.55,.54),(.15,.06,.70,.55),(.16,.05,.74,.52),(.16,.05,.76,.56),
   (.40,.22,.31,.42),(.50,.27,.27,.39),(.56,.25,.24,.40),(.53,.25,.27,.40),(.53,.26,.26,.39),(.54,.26,.25,.39),(.55,.25,.24,.40),(.68,.25,.27,.42),(.82,.26,.18,.42)]
Wt=[None]*10+[(.74,.25,.20,.37),(.78,.25,.18,.36),(.80,.25,.18,.36),(.80,.24,.18,.37),(.79,.26,.18,.36),(.79,.26,.18,.36),(.79,.25,.18,.36),None,(.64,.25,.18,.37)]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
g,w=K(G),K(Wt)
c=dict(mediaId=5386,level="B",keyWord="to tear",defaultVoice="female",
 taps=[dict(phrase="to tear a contract in half",target="the woman in grey",voice="female",keys=g),
       dict(phrase="to walk out of the meeting",target="the woman in grey",voice="female",keys=g),
       dict(phrase="to carry a coffee tray",target="the woman with the tray",voice="female",keys=w)],
 stillS=7.0,
 nouns=[dict(word="a contract",x=.26,y=.32,voice="female"),dict(word="an easel",x=.30,y=.58,voice="female"),
        dict(word="a door",x=.62,y=.18,voice="female"),dict(word="crumpled paper",x=.55,y=.85,voice="female")],
 question="What is the woman in grey doing?",answer=["She","is","tearing","a","contract","in","half."],answerVoice="female",
 notes="Woman with the tray stands in the doorway behind the woman in grey from 5.0 s; boxes split along x where they overlap; at 8.5 s she is almost fully hidden behind the woman in grey (off). Seated men all stare, so none used as a target.")
json.dump(c,open('content/5386.json','w'),indent=1)
