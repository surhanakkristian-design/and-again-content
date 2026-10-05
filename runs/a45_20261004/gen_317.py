import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
C={0.0:(0,0,.36,.62),0.5:(0,0,.38,.62),1.0:(0,0,.39,.70),1.5:(0,0,.41,.64),2.0:(0,0,.41,.53),2.5:(0,0,.43,.56),
3.0:(0,0,.44,.70),3.5:(0,0,.47,.74),4.0:(0,0,.42,.67),4.5:(0,0,.34,.64),5.0:(0,0,.29,.64),5.5:(0,.10,.18,.48),6.0:(0,.10,.18,.38)}
H={4.0:(.82,.28,.18,.30),4.5:(.56,.07,.44,.50),5.0:(.43,0,.57,.48),5.5:(.33,0,.67,1),6.0:(.36,0,.64,.92),
6.5:(.03,0,.97,1),7.0:(0,0,1,1),7.5:(0,0,1,1),8.0:(0,0,1,1),8.5:(0,0,1,1),9.0:(0,.07,1,.93),9.5:(0,.07,1,.93),10.0:(.12,.08,.88,.92)}
c={"mediaId":317,"level":"A","keyWord":"french fries","defaultVoice":"male",
"taps":[
{"phrase":"to cook french fries","target":"the cook","voice":"male","keys":keys(C)},
{"phrase":"to eat french fries","target":"the man in the hat","voice":"male","keys":keys(H)},
{"phrase":"to wear a black hat","target":"the man in the hat","voice":"male","keys":keys(H)}],
"stillS":9.0,
"nouns":[{"word":"french fries","x":.52,"y":.68,"voice":"male"},{"word":"a hat","x":.70,"y":.15,"voice":"male"},
{"word":"bikes","x":.14,"y":.53,"voice":"male"},{"word":"lights","x":.25,"y":.33,"voice":"male"}],
"question":"What is the cook doing?",
"answer":["He","is","cooking","french","fries."],
"answerVoice":"male",
"notes":"Two men: the cook (bearded, black T-shirt and apron, 0.0-6.0 s) and the customer (black hat, black hoodie, face from 6.5 s). 4.0-6.0 s: the arm in a long black sleeve that sprinkles salt and the hand holding the paper cone are taken as the customer's (the cook has bare forearms) and boxed as 'the man in the hat', although his hat is not yet in the picture there. 'to wear a black hat' is a state (second phrase for the same target). A pigeon stands in the background (1.0-4.0 s, 10.0 s), not used."}
json.dump(c,open("content/317.json","w"),indent=1,ensure_ascii=False)
