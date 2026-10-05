import json
T=[i*0.5 for i in range(31)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
Wt={0.0:(.31,.17,.34,.44),0.5:(.31,.17,.36,.46),1.0:(.31,.18,.33,.48),1.5:(.36,.17,.33,.42),2.0:(.50,.17,.32,.15),2.5:(.82,.18,.18,.14)}
M={0.0:(.66,.30,.34,.38),0.5:(.68,.30,.32,.38),1.0:(.66,.31,.34,.38),1.5:(.70,.31,.30,.40),2.0:(.56,.33,.44,.36),2.5:(.52,.33,.48,.36)}
W={0.0:(0,.33,.30,.36),0.5:(0,.33,.30,.36),1.0:(0,.34,.30,.36),1.5:(0,.34,.35,.36),2.0:(0,.33,.40,.36),2.5:(0,.33,.40,.36)}
for t in (3.0,3.5,4.0,4.5,5.0,5.5):
    M[t]=(.52,.30,.48,.40); W[t]=(0,.33,.40,.38)
for t in (6.0,6.5,7.0,7.5,8.0,8.5,9.0):
    M[t]=(0,.08,1.0,.76)
M[9.5]=(.52,.30,.48,.36); W[9.5]=(0,.34,.42,.30)
for t in (10.0,10.5):
    M[t]=(.52,.30,.48,.39); W[t]=(0,.33,.43,.36)
M[11.0]=(.45,.30,.55,.39); W[11.0]=(0,.33,.43,.36)
M[11.5]=(.41,.30,.59,.39); W[11.5]=(0,.33,.40,.36)
M[12.0]=(.42,.30,.58,.39); W[12.0]=(0,.33,.40,.36)
for t in (12.5,13.0):
    M[t]=(.44,.30,.56,.39); W[t]=(0,.33,.42,.36)
for t in (13.5,14.0,14.5,15.0):
    M[t]=(.50,.30,.50,.39); W[t]=(0,.33,.42,.37)
d={"mediaId":4040,"level":"A","keyWord":"meal","defaultVoice":"male",
"taps":[{"phrase":"to bring the food","target":"the waiter","voice":"male","keys":K(Wt)},
{"phrase":"to eat a burger","target":"the man at the table","voice":"male","keys":K(M)},
{"phrase":"to hold a fork","target":"the woman","voice":"female","keys":K(W)}],
"stillS":10.0,
"nouns":[{"word":"a woman","x":.18,"y":.47,"voice":"female"},{"word":"a burger","x":.72,"y":.64,"voice":"male"},
{"word":"a salad","x":.30,"y":.65,"voice":"male"},{"word":"a table","x":.50,"y":.85,"voice":"male"}],
"question":"What are the man and woman doing?",
"answer":["They","are","having","a","meal","at","a","table."],"answerVoice":"male",
"notes":"Key word 'meal' is in the answer, not a noun slot (it would label the same place as the burger / salad). The waiter leaves at 2.0-2.5 s; there he stands behind the seated man, so his box covers only head and shoulders above the man's box. 6.0-9.0 s is a close-up of the man alone (woman off). At the end (11.0-15.0 s) the man swaps the plates and the woman gets the burger - not said in the packet description; she never eats it, so 'to eat a burger' fits only the man. The woman holds the fork only in 0-5.5 s. Still 10.0 s: burger and salad are at the same height, pills 0.42 apart in x."}
json.dump(d,open("content/4040.json","w"),indent=1)
