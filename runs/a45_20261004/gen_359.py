import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
ham={0.0:(.03,.36,.93,.36),0.5:(.08,.36,.88,.36),1.0:(.06,.37,.90,.31),1.5:(.04,.37,.80,.37),
2.0:(.23,.42,.77,.26),2.5:(.17,.34,.50,.31),3.0:(.18,.27,.58,.34),3.5:(.15,.35,.65,.35),4.0:(.15,.29,.60,.33),
4.5:(.13,.30,.65,.33),5.0:(.09,.37,.89,.28),5.5:(.10,.37,.90,.29),6.0:(.10,.33,.88,.36),6.5:(.25,.37,.60,.33),
7.0:(.25,.41,.52,.32),7.5:(.38,.47,.40,.20),8.0:(.34,.45,.44,.20),8.5:(.25,.42,.48,.25),9.0:(.25,.37,.50,.32),
9.5:(.23,.37,.54,.34),10.0:(.25,.43,.52,.28)}
bowl={2.0:(.36,.68,.64,.30),2.5:(.0,.65,.84,.31),3.0:(.08,.61,.92,.32),3.5:(.04,.70,.92,.27),4.0:(.03,.62,.93,.33),
4.5:(.02,.63,.92,.33),5.0:(.0,.65,.86,.31),5.5:(.0,.66,.33,.22)}
c={"mediaId":359,"level":"A","keyWord":"hamster","defaultVoice":"male",
"taps":[{"phrase":"to run in a wheel","target":"the hamster","voice":"male","keys":keys(ham)},
{"phrase":"to eat some seeds","target":"the hamster","voice":"male","keys":keys(ham)},
{"phrase":"to be full of seeds","target":"the bowl","voice":"male","keys":keys(bowl)}],
"stillS":2.0,
"nouns":[{"word":"a hamster","x":.60,"y":.55,"voice":"male"},{"word":"a wheel","x":.20,"y":.33,"voice":"male"},{"word":"a bowl","x":.68,"y":.84,"voice":"male"}],
"question":"What is the hamster doing?",
"answer":["It","is","eating","seeds","from","a","bowl."],"answerVoice":"male",
"notes":"Bowl phrase is a state (bowl does nothing); bowl looks nearly empty at 2.0 s, full of seeds from 2.5 s. Hamster and bowl overlap 2.0-5.5 s, boxes split along the bowl rim. At 3.5 s the hamster's head is inside the bowl. Wheel not used as tap target because the hamster is inside it."}
json.dump(c,open("content/359.json","w"),indent=1)
