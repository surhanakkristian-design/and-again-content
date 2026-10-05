import json
times=[i*0.5 for i in range(21)]
M={0.0:(0,.23,.34,1),0.5:(0,.23,.33,1),1.0:(0,.24,.31,1),3.0:(0,0,.75,1),3.5:(0,0,.95,1),4.0:(0,.23,.31,1),4.5:(0,.23,.31,1),5.0:(0,.24,.31,1),5.5:(0,.24,.27,1),
6.0:(0,.03,1,1),6.5:(0,.03,1,1),7.0:(0,.03,1,1),7.5:(0,.03,1,1),8.0:(0,.08,1,.85),8.5:(0,.08,1,.85),9.0:(.05,.12,1,.95),9.5:(.09,.16,.88,.88),10.0:(.45,.33,.86,.86)}
Wm={0.0:(.63,.25,1,.72),0.5:(.63,.25,1,.70),1.0:(.65,.26,1,.78),4.0:(.58,.26,1,.72),4.5:(.59,.26,1,.72),5.0:(.55,.26,1,.72),5.5:(.63,.26,1,.74)}
R={0.0:(.35,.38,.62,.60),0.5:(.34,.38,.62,.60),1.0:(.33,.38,.64,.62),1.5:(.03,.18,1,1),2.0:(0,.18,1,1),2.5:(0,.18,1,1),4.0:(.33,.37,.57,.63),4.5:(.33,.37,.58,.63),5.0:(.33,.39,.54,.64),5.5:(.34,.33,.62,.47)}
def keys(d):
    out=[]
    for t in times:
        if t in d:
            a,b,c,e=d[t]; out.append({"t":t,"x":a,"y":b,"w":round(c-a,2),"h":round(e-b,2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":604,"level":"A","keyWord":"receipt","defaultVoice":"male",
"taps":[
 {"phrase":"to hold a red apple","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to sell fruit","target":"the woman","voice":"female","keys":keys(Wm)},
 {"phrase":"to print a long receipt","target":"the cash register","voice":"male","keys":keys(R)}],
"stillS":4.5,
"nouns":[{"word":"a receipt","x":.16,"y":.52,"voice":"male"},{"word":"apples","x":.42,"y":.66,"voice":"male"},{"word":"pears","x":.72,"y":.75,"voice":"male"},{"word":"bottles","x":.90,"y":.27,"voice":"male"}],
"question":"What is the man looking at?",
"answer":["He","is","looking","at","a","long","receipt."],
"answerVoice":"male",
"notes":"Cartoon with cuts. Man holds the red apple only at 6.0-7.5 (reading the receipt). 3.0-3.5 show only his legs with the receipt winding around them (box on). 1.5-2.0 only the woman's hand at the register: woman off. The woman's hands lie on/in front of the register at 4.0-5.5, boxes split left of her body; at 5.5 the register is mostly hidden behind her arms (small box on its top). 'to sell fruit' is inferred from her role behind the counter."}
json.dump(c,open('content/604.json','w'),indent=1,ensure_ascii=False)
