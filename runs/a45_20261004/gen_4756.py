import json
def keys(times, d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"t":t,"off":True} for t in times]
times=[i*0.5 for i in range(25)]
W={0.0:(.22,.30,.78,.70),0.5:(.35,.28,.65,.72),1.0:(.35,.27,.65,.73),1.5:(.30,.28,.70,.72),2.0:(.28,.28,.72,.72),
2.5:(.15,.33,.72,.64),3.0:(.16,.33,.70,.65),3.5:(.18,.33,.71,.65),4.0:(.18,.33,.72,.60),4.5:(.31,.33,.64,.60),
5.0:(.24,.33,.62,.67),5.5:(0,.33,1,.67),6.0:(.24,.30,.45,.70),6.5:(0,.29,1,.71)}
M={}
for t in times[14:]:
    W[t]=(.20,.20,.76,.70); M[t]=(0,.38,.20,.17)
W[7.0]=(.20,.20,.76,.74)
c={"mediaId":4756,"level":"A","keyWord":"france","defaultVoice":"female",
"taps":[
{"phrase":"to ride a bike","target":"the woman","voice":"female","keys":keys(times,W)},
{"phrase":"to eat a croissant","target":"the woman","voice":"female","keys":keys(times,W)},
{"phrase":"to sit behind the woman","target":"the man with glasses","voice":"male","keys":keys(times,M)}],
"stillS":2.0,
"nouns":[{"word":"a tower","x":.56,"y":.18,"voice":"female"},{"word":"a river","x":.16,"y":.52,"voice":"female"},
{"word":"bread","x":.24,"y":.65,"voice":"female"},{"word":"a basket","x":.14,"y":.85,"voice":"female"}],
"question":"What is the woman eating?",
"answer":["She","is","eating","a","croissant."],
"answerVoice":"female",
"notes":"Key word 'France' is not a thing to label; the Eiffel Tower is given as 'a tower'. Two phrases share the woman (the only main target); third target is the man with glasses at the next cafe table (7.0-12.0 s, small, left edge). In the cafe shot the woman's box starts at x 0.20 so it does not overlap his box; her right arm (x 0.05-0.20) falls outside. The waiter passing at 10.5-11.5 stands, so 'to sit behind the woman' fits only the man with glasses; the waiter lies inside the woman's box. 'croissant' kept as the natural everyday word although it is not strictly A1."}
json.dump(c,open("content/4756.json","w"),indent=1,ensure_ascii=False)
