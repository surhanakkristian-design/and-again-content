import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(.18,0,.82,1.0),0.5:(.70,0,.30,.74),1.0:(.82,0,.18,.52),1.5:(.82,0,.18,.50),2.0:(.55,0,.45,.70),2.5:(.45,0,.55,.66),
3.0:(.12,0,.88,.78),3.5:(.33,0,.67,.80),4.0:(.26,0,.74,.76),4.5:(.26,0,.74,.76),5.0:(.26,0,.74,.82),5.5:(.43,0,.57,.82),
6.0:(.43,0,.57,.78),6.5:(.52,0,.48,.78),7.0:(.35,0,.65,.56),7.5:(.28,0,.72,.56),8.0:(.24,0,.76,.56),8.5:(0,0,1.0,.60),
9.0:(0,0,1.0,.70),9.5:(0,0,1.0,.68),10.0:(0,0,1.0,.56),10.5:(0,0,1.0,.54),11.0:(0,0,1.0,.62),11.5:(0,0,1.0,.64),12.0:(0,0,1.0,.58)}
stove={0.5:(0,.74,1.0,.20),1.0:(0,.72,1.0,.25),1.5:(0,.72,1.0,.25),2.0:(0,.74,1.0,.22),2.5:(0,.70,.92,.26),3.0:(0,.80,.84,.20),
3.5:(0,.82,.84,.18),4.0:(0,.78,.86,.22),4.5:(0,.78,.88,.22),5.0:(0,.84,.84,.16),5.5:(0,.84,.82,.16),6.0:(0,.78,.82,.22),
6.5:(0,.78,.82,.22),10.0:(.32,.68,.56,.20),10.5:(.16,.69,.70,.23),11.0:(.18,.84,.44,.14),11.5:(.22,.85,.40,.14),12.0:(.14,.76,.56,.17)}
c={"mediaId":4761,"level":"B","keyWord":"bacon","defaultVoice":"male",
"taps":[
 {"phrase":"to crack an egg","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to add strips of bacon","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to heat a frying pan","target":"the stove","voice":"male","keys":keys(stove)}],
"stillS":6.0,
"nouns":[{"word":"a beard","x":.80,"y":.24,"voice":"male"},{"word":"a parka","x":.76,"y":.47,"voice":"male"},
 {"word":"bacon","x":.36,"y":.74,"voice":"male"},{"word":"a gas stove","x":.30,"y":.93,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","frying","bacon","on","a","portable","stove."],
"answerVoice":"male",
"notes":"Second target is the gas stove under the pan; its box is the strip below the pan and is cut where the man stands. 7.0-9.5 s the stove is hidden under the big pan (off); at 11.0 and 11.5 s only a small part shows under the pan. 'a beard' and 'a parka' are both on the man (face / chest, 0.23 apart in y)."}
json.dump(c,open("content/4761.json","w"),indent=1)
