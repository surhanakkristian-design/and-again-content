import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
mouse={0.0:(.36,.35,.20,.15),0.5:(.37,.35,.26,.19),1.0:(.36,.36,.27,.18),1.5:(.36,.36,.27,.18),2.0:(.36,.34,.28,.20),
2.5:(.26,.31,.46,.38),3.0:(.10,.30,.67,.44),3.5:(.12,.29,.68,.45),4.0:(.10,.29,.68,.46),4.5:(.12,.24,.67,.52),
5.0:(.10,.21,.68,.50),5.5:(.10,.21,.70,.50),6.0:(.08,.27,.78,.55),6.5:(.10,.27,.77,.64),7.0:(.08,.24,.75,.54),
7.5:(.08,.24,.77,.54),8.0:(.06,.24,.80,.56),8.5:(.06,.24,.83,.56),9.0:(.0,.27,.84,.42),9.5:(.08,.42,.66,.23)}
lamp={0.0:(.18,0,.26,.24),0.5:(.18,0,.26,.24),1.0:(.15,0,.26,.24),1.5:(.15,0,.26,.24),2.0:(.12,0,.27,.19),2.5:(.08,0,.30,.14)}
c={"mediaId":487,"level":"A","keyWord":"mouse","defaultVoice":"male",
"taps":[
{"phrase":"to eat the cheese","target":"the mouse","voice":"male","keys":keys(mouse)},
{"phrase":"to run into a hole","target":"the mouse","voice":"male","keys":keys(mouse)},
{"phrase":"to give yellow light","target":"the lamp","voice":"male","keys":keys(lamp)}],
"stillS":4.5,
"nouns":[{"word":"a mouse","x":.45,"y":.50,"voice":"male"},{"word":"cheese","x":.50,"y":.82,"voice":"male"},{"word":"a hole","x":.84,"y":.38,"voice":"male"}],
"question":"What is the mouse doing?",
"answer":["The","mouse","is","eating","the","cheese."],
"answerVoice":"male",
"notes":"Only the mouse really acts; third target is the hanging lamp (visible 0-2.5 s only). A moth flies near the lamp early on, not used. Cheese not used as tap target because it sits inside the mouse's box while eaten. At 9.5 s only the tail is visible."}
json.dump(c,open("content/487.json","w"),indent=1,ensure_ascii=False)
