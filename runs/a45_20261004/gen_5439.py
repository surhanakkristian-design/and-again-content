import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
man={0.0:(.08,.25,.90,.75),0.5:(.40,.30,.60,.70),1.0:(.12,.40,.88,.60),1.5:(.18,.40,.80,.60),2.0:(.24,.42,.76,.58),
2.5:(.28,.45,.72,.55),3.0:(.29,.29,.42,.71),3.5:(.29,.29,.42,.71),4.0:(.29,.23,.44,.77),4.5:(.31,.23,.46,.77),
5.0:(.28,.23,.48,.77),5.5:(.17,.44,.40,.56),6.0:(.21,.44,.37,.56),6.5:(.25,.44,.34,.52),7.0:(.27,.48,.30,.44),
7.5:(.29,.47,.30,.42),8.0:(.29,.45,.30,.40),8.5:(.29,.45,.30,.40),9.0:(.28,.45,.28,.38)}
rb={0.5:(.03,.16,.37,.42),1.0:(.34,0,.34,.40),1.5:(0,.01,1,.39),2.0:(0,.13,1,.29),2.5:(0,.22,1,.23)}
gr={3.0:(0,.11,.96,.18),3.5:(0,.08,.99,.21),4.0:(0,.05,1,.18),4.5:(0,.03,1,.20),5.0:(0,.03,1,.20),5.5:(0,.14,1,.30),
6.0:(0,.18,1,.26),6.5:(0,.22,1,.22),7.0:(0,.27,1,.21),7.5:(0,.29,1,.18),8.0:(0,.29,1,.16),8.5:(0,.30,1,.15),9.0:(0,.31,1,.14)}
c={"mediaId":5439,"level":"A","keyWord":"grey","defaultVoice":"male",
"taps":[{"phrase":"to walk in the rain","target":"the man with the umbrella","voice":"male","keys":K(man)},
{"phrase":"to open over his head","target":"the rainbow umbrella","voice":"male","keys":K(rb)},
{"phrase":"to cover four men","target":"the grey umbrella","voice":"male","keys":K(gr)}],
"stillS":4.0,
"nouns":[{"word":"an umbrella","x":0.50,"y":0.13,"voice":"male"},{"word":"a coat","x":0.55,"y":0.63,"voice":"male"},
{"word":"the street","x":0.20,"y":0.75,"voice":"male"},{"word":"shoes","x":0.52,"y":0.88,"voice":"male"}],
"question":"What do the four men share?","answer":["They","share","a","grey","umbrella."],"answerVoice":"male",
"notes":"Man and umbrellas overlap in the picture: split horizontally at the canopy edge, so the man's box starts below the canopy (at 0.5 s the closed rainbow umbrella is diagonal; man box starts at x 0.40 and misses part of his hands). From 5.5 s four men crouch; the target is the one in the middle-left holding the grey umbrella's handle (another man also wears a beige coat, hence 'the man with the umbrella'). 'to walk in the rain' is clearest 3-5 s."}
json.dump(c,open('content/5439.json','w'),indent=1)
