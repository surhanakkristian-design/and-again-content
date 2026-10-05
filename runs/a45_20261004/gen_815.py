import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
B={0.0:(0,.33,1,.80),0.5:(0,.31,1,.85),1.0:(0,.31,1,.93),1.5:(0,.29,.95,.92),2.0:(0,.25,.90,.97),2.5:(0,.26,1,.90),
3.0:(0,.23,1,.98),3.5:(0,.17,.95,1),4.0:(0,.11,1,.97),4.5:(0,.19,1,.92),5.0:(0,.18,1,.88),5.5:(0,.28,1,1),
6.0:(0,.21,1,.73),6.5:(0,.29,.98,.70),7.0:(0,.34,1,.87),7.5:(0,.37,.88,.95),8.0:(.03,.28,.85,.87),8.5:(.05,.22,.92,.95),
9.0:(.10,.28,.92,.97),9.5:(0,.15,1,.95),10.0:(0,.42,1,1)}
k=keys(B)
c={"mediaId":815,"level":"A","keyWord":"turtle","defaultVoice":"male",
"taps":[{"phrase":"to walk across the sand","target":"the turtle","voice":"male","keys":k},
{"phrase":"to go into the sea","target":"the turtle","voice":"male","keys":k},
{"phrase":"to swim under the water","target":"the turtle","voice":"male","keys":k}],
"stillS":1.0,
"nouns":[{"word":"the sky","x":.60,"y":.09,"voice":"male"},{"word":"a turtle","x":.40,"y":.50,"voice":"male"},
{"word":"sand","x":.50,"y":.90,"voice":"male"}],
"question":"Where is the turtle going?","answer":["It","is","going","into","the","sea."],"answerVoice":"male",
"notes":"The turtle is the only clear target (a few tiny fish pass at 7.0-8.0 s only), so all three phrases use it; they describe three different moments (sand, entering the water, underwater). Only 3 nouns: there are two separate rocks, so 'a rock' was left out. The box leaves out the turtle's reflection on the water surface at 8.5-10.0 s. At 5.5 s (camera dips under water) the turtle is a dark shape."}
json.dump(c,open('content/815.json','w'),indent=1)
