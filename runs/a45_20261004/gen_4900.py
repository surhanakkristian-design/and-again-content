import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True})
    return out
barrel={0.0:(0,0.18,0.89,0.82),0.5:(0,0.03,1.0,0.9),1.0:(0,0.24,0.95,0.5),1.5:(0.04,0.25,0.88,0.46),2.0:(0.16,0.28,0.71,0.33)}
trolley={4.5:(0,0.13,0.88,0.52),5.0:(0,0.22,0.78,0.48),5.5:(0,0.12,0.78,0.52)}
stack={6.0:(0.28,0,0.54,0.54),6.5:(0.22,0,0.62,0.89),7.0:(0.22,0,0.56,1.0),7.5:(0.13,0.04,0.76,0.96),8.0:(0,0.2,1.0,0.8),8.5:(0,0.33,1.0,0.65),9.0:(0,0.38,1.0,0.62)}
c={"mediaId":4900,"level":"B","keyWord":"stack","defaultVoice":"female",
"taps":[
 {"phrase":"to roll across the lawn","target":"the barrel","voice":"female","keys":keys(barrel)},
 {"phrase":"to spill groceries on the grass","target":"the shopping trolley","voice":"female","keys":keys(trolley)},
 {"phrase":"to collapse into a heap","target":"the stack of pallets","voice":"female","keys":keys(stack)}],
"stillS":6.5,
"nouns":[{"word":"a stack","x":0.52,"y":0.30,"voice":"female"},{"word":"the sky","x":0.90,"y":0.22,"voice":"female"},
 {"word":"a woman","x":0.19,"y":0.55,"voice":"female"},{"word":"grass","x":0.14,"y":0.90,"voice":"female"}],
"question":"What is the tall stack doing?",
"answer":["The","stack","is","collapsing","into","a","heap."],
"answerVoice":"female",
"notes":"Clip is a sequence of separate shots (barrel 0-2.0 s, table 2.5-4.0 s, trolley 4.5-5.5 s, pallet stack 6.0-9.0 s); each target only boxed in its own shot. Table not used as a target. Pallet stack only starts collapsing at 7.5 s."}
json.dump(c,open('content/4900.json','w'),indent=1)
