import json
T=[i*0.5 for i in range(25)]
M=[(0,.37,.88,.63),(0,.37,.92,.63),(0,.39,.90,.61),(0,.39,.90,.61),(0,.39,.90,.61),
(0,.27,.76,.73),(0,.26,.77,.74),(0,.25,.79,.75),(0,.24,.79,.76),(0,.24,.81,.76),(0,.24,.81,.76),(0,.24,.83,.76),(0,.24,.83,.76),(0,.24,.83,.76),(0,.25,.83,.75),(0,.25,.83,.75),
(.03,.31,.77,.69),(.02,.30,.78,.70),(0,.30,.78,.70),(.01,.32,.80,.68),(.04,.30,.80,.70),(.07,.31,.76,.69),(.09,.35,.73,.65),(.05,.34,.77,.66),(.03,.33,.78,.67)]
TW={0.0:(.21,0,.42,.36),0.5:(.23,0,.41,.36),1.0:(.23,.01,.41,.37),1.5:(.23,.01,.41,.37),2.0:(.23,0,.41,.38)}
def k(t,b): return dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3])
man=[k(t,b) for t,b in zip(T,M)]
tower=[k(t,TW[t]) if t in TW else dict(t=t,off=True) for t in T]
taps=[dict(phrase="to tilt to one side",target="the tower",voice="male",keys=tower),
dict(phrase="to lean out of a gondola",target="the man",voice="male",keys=man),
dict(phrase="to grip a giant cone",target="the man",voice="male",keys=man)]
c=dict(mediaId=4997,level="B",keyWord="laugh",defaultVoice="male",taps=taps,stillS=6.0,
nouns=[dict(word="laundry",x=.45,y=.17,voice="male"),dict(word="a bridge",x=.52,y=.46,voice="male"),dict(word="a canal",x=.75,y=.68,voice="male"),dict(word="a gondola",x=.40,y=.90,voice="male")],
question="What is the man holding?",answer="He is holding a giant ice cream cone.".split(),answerVoice="male",
notes="Tower box cut at y .36-.38 where the man's hair starts (t 0-2). Gondolier visible only 2.5-3.5 s, small, not used. Key word 'laugh' (noun) not a visible thing; not in the texts.")
json.dump(c,open('content/4997.json','w'),indent=1)
