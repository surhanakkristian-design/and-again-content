import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
M={0.0:(0,0,1,.72),0.5:(0,0,1,.70),1.0:(0,0,1,.62),1.5:(0,0,1,.62),2.0:(0,0,1,.68),2.5:(0,0,1,.70),3.0:(0,0,1,.76),
 3.5:(0,.28,.31,.72),4.0:(0,.30,.36,.70),4.5:(0,.24,.60,.76),5.0:(0,.08,.72,.92),5.5:(0,.03,.92,.97),6.0:(0,.30,.97,.70),
 6.5:(0,.22,.58,.78),7.0:(0,.24,.58,.76),7.5:(0,.28,.62,.72),8.0:(0,.29,.57,.71),8.5:(0,.29,.58,.71),9.0:(0,.30,.40,.70)}
P={6.5:(.58,0,.42,1),7.0:(.58,.05,.42,.95),7.5:(.62,.05,.38,.95),8.0:(.57,.03,.43,.97),8.5:(.58,0,.42,1),9.0:(.45,.07,.55,.93)}
c={"mediaId":5169,"level":"B","keyWord":"mail","defaultVoice":"male",
"taps":[{"phrase":"to mail a postcard","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to pick out some postcards","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to be painted bright yellow","target":"the postbox","voice":"male","keys":K(P)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.20,"y":0.12,"voice":"male"},{"word":"glasses","x":0.33,"y":0.44,"voice":"male"},
{"word":"a cardigan","x":0.14,"y":0.82,"voice":"male"},{"word":"a postbox","x":0.76,"y":0.62,"voice":"male"}],
"question":"What is he doing at the postbox?","answer":["He","is","mailing","a","postcard."],"answerVoice":"male",
"notes":"Only one person; the postbox phrase is a state (no action fits a thing). At 6.0 s only his hands with a fan of cards are visible; the yellow at the right at 6.0 s is a door, not the postbox (off)."}
json.dump(c,open('content/5169.json','w'),indent=1)
