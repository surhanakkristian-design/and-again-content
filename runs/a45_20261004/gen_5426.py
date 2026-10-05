import json
T=[i*0.5 for i in range(19)]
O=None
W=[(.04,.39,.42,.34),(.01,.39,.44,.37),(.01,.39,.45,.35),(.40,.02,.60,.50),(.40,.00,.60,.58),(.40,.00,.60,.58),(.40,.02,.60,.56),(.46,.02,.54,.58),
(.46,.00,.54,.55),(.48,.05,.52,.52),(.48,.08,.52,.50),(.50,.08,.50,.50),(.50,.06,.50,.50),(.00,.40,.48,.36),(.00,.24,.45,.56),(.00,.25,.47,.55),
(.03,.23,.46,.52),(.02,.24,.43,.50),(.02,.24,.43,.50)]
M=[(.52,.38,.47,.35),(.52,.37,.48,.40),(.50,.37,.50,.37),(.68,.58,.32,.40),(.68,.60,.32,.40),(.68,.60,.32,.40),(.52,.60,.48,.40),(.10,.62,.90,.38),
(.40,.58,.60,.42),(.58,.60,.42,.40),(.58,.60,.42,.40),O,O,(.50,.42,.50,.35),(.52,.18,.48,.62),(.52,.21,.48,.60),
(.50,.16,.50,.58),(.45,.18,.55,.56),(.45,.18,.55,.56)]
def keys(L): return [dict(t=t,off=True) if k is None else dict(t=t,x=k[0],y=k[1],w=k[2],h=k[3]) for t,k in zip(T,L)]
c=dict(mediaId=5426,level="B",keyWord="delegation",defaultVoice="female",
taps=[dict(phrase="to glance up at the camera",target="the woman",voice="female",keys=keys(W)),
dict(phrase="to wear a teal blazer",target="the woman",voice="female",keys=keys(W)),
dict(phrase="to grasp the woman's hand",target="the man",voice="male",keys=keys(M))],
stillS=0.0,
nouns=[dict(word="a hedge",x=.15,y=.22,voice="female"),dict(word="a delegation",x=.55,y=.32,voice="female"),
dict(word="desk flags",x=.45,y=.76,voice="female"),dict(word="a table",x=.50,y=.88,voice="female")],
question="What is the woman wearing?",answer=["She","is","wearing","a","teal","blazer."],answerVoice="female",
notes="Cuts: wide 0.0-1.0, close-up 1.5-6.0 (woman signing; she glances up at the camera with a smile at 2.5), wide 6.5-9.0 (stand up, handshake from 8.0). In the close-up the man is only his grey sleeves and hands signing at bottom right (boxed 1.5-5.0); his hair blob at 1.5-2.5 sits inside the woman's box and is left out; off at 5.5-6.0 where several colleagues' hands with stamps crowd the frame. Handshake boxes split at the clasped hands. 'a delegation' pill is on the standing group behind the signers (the colleagues as a group) - check it reads clearly. Mixed main pair -> defaultVoice female (evenId true).")
json.dump(c,open('content/5426.json','w'),indent=1)
