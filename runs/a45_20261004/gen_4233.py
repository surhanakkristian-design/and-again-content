import json
T=[i*0.5 for i in range(24)]
# (train_y, train_h) shot 1
s1={0:(.37,.14),0.5:(.37,.14),1:(.37,.14),1.5:(.37,.14),2:(.36,.14),2.5:(.36,.14),3:(.36,.14),3.5:(.35,.13),4:(.35,.13),4.5:(.33,.14),5:(.33,.14)}
train=[];water=[];bridge=[]
for t in T:
    if t<=5.0:
        y,h=s1[t]; b=round(y+h+.01,2)
        train.append((0,y,1,h)); water.append((0,0,1,round(y-.01,2))); bridge.append((0,b,1,round(1-b,2)))
    elif t==5.5:
        train.append((0,.43,1,.08)); water.append((.25,0,.6,.42)); bridge.append((.05,.52,.9,.32))
    else:
        train.append((0,.41,1,.07)); water.append((.22,0,.62,.4)); bridge.append((.05,.49,.9,.31))
def keys(b):
    return [{"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,b)]
d={"mediaId":4233,"level":"A","keyWord":"stone","defaultVoice":"male",
"taps":[{"phrase":"to cross the bridge","target":"the train","voice":"male","keys":keys(train)},
{"phrase":"to fall down the rocks","target":"the water","voice":"male","keys":keys(water)},
{"phrase":"to be made of stone","target":"the bridge","voice":"male","keys":keys(bridge)}],
"stillS":10.5,
"nouns":[{"word":"a train","x":.62,"y":.45,"voice":"male"},{"word":"a bridge","x":.3,"y":.55,"voice":"male"},
{"word":"water","x":.42,"y":.2,"voice":"male"},{"word":"trees","x":.16,"y":.78,"voice":"male"}],
"question":"What is the train doing?","answer":["It","is","crossing","a","stone","bridge."],"answerVoice":"male",
"notes":"No people. Key word 'stone' is a material here: used in phrase 3 and in the answer, not as a noun pill (it would label the same place as 'a bridge'). 'the water' box = the waterfall ABOVE the train only; the water seen through the arches lies inside the bridge box (cannot be split). Phrase 3 is a state (no action fits only the bridge). Train is a thin band in the wide shot (from 5.5 s), its box is only 0.07-0.08 high so it does not overlap the water and bridge boxes."}
json.dump(d,open("content/4233.json","w"),indent=1)
