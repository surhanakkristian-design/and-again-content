import json
T=[i*0.5 for i in range(24)]
F=(0,0,1,1)
W={0:(0,.07,1,.93),.5:(.14,.02,.72,.98),1:F,1.5:F,2:F,9.5:F,10:F,10.5:F}
M={2.5:F,3:F,4:(.32,.17,.38,.75),4.5:(.22,.2,.5,.69),5:(0,.27,.72,.71),5.5:(0,.27,.82,.59),6:(0,.27,.65,.35),6.5:(0,.1,.22,.3),
7:(.57,.12,.3,.17),8.5:(0,.14,1,.36),9:(0,.15,1,.36),11:(0,.07,1,.78),11.5:(0,.07,1,.78)}
P={5.5:(0,.87,1,.13),6:(0,.63,1,.37),6.5:(0,.41,1,.59),7:(0,.3,1,.7),7.5:(0,.26,1,.74),8:(0,.46,1,.54),8.5:(0,.51,1,.49),9:(0,.52,1,.48),
11:(0,.86,1,.14),11.5:(0,.86,1,.14)}
def keys(b):
    return [({"t":t,"off":True} if t not in b else {"t":t,"x":b[t][0],"y":b[t][1],"w":b[t][2],"h":b[t][3]}) for t in T]
d={"mediaId":4234,"level":"B","keyWord":"closet","defaultVoice":"female",
"taps":[{"phrase":"to fling her arms up","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to empty the whole closet","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to form a huge heap","target":"the pile of clothes","voice":"female","keys":keys(P)}],
"stillS":4.0,
"nouns":[{"word":"dresses","x":.84,"y":.38,"voice":"female"},{"word":"pyjamas","x":.47,"y":.52,"voice":"female"},
{"word":"sweaters","x":.28,"y":.14,"voice":"female"}],
"question":"What is the man standing on?","answer":["He","is","standing","on","a","heap","of","clothes."],"answerVoice":"male",
"notes":"Cartoon clip with cuts: woman (0-2.0, 9.5-10.5), man close-up (2.5-3.0), empty closet (3.5, nobody), man in the closet (4.0-9.0, 11.0-11.5; hidden at 7.5-8.0). Man and woman never share a shot; defaultVoice female by evenId (mixed pair). Key word 'closet' is the whole room, no single place for a pill, so it is in phrase 2 instead of the nouns. The man stands on the pile: boxes split along the pile's top edge (pile top clipped by about 0.03 at 6.5 and 7.0; man's foot inside the pile box at 5.5). 'sweaters' and 'pyjamas' follow the majority usage in the other content files. Dresses hang in three groups, pill on the right group."}
json.dump(d,open("content/4234.json","w"),indent=1)
