import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
wom=K([(.15,.36,.73,.90),(.17,.40,.74,.90),(.15,.47,.70,.97),(.17,.52,.74,.97),(.15,.54,.74,.96),(.14,.56,.75,.97),(.11,.61,.74,1),(.11,.61,.75,1)])
ship=K([(.74,.02,1,.75),(.75,.02,1,.75),(.71,.02,1,.75),(.75,.05,1,.75),(.75,.07,1,.75),(.76,.11,1,.77),(.75,.14,1,.79),(.76,.14,1,.81)])
c={"mediaId":7394,"level":"B","keyWord":"open up","defaultVoice":"female",
"taps":[{"phrase":"to heave an iron lever","target":"the woman","voice":"female","keys":wom},
{"phrase":"to glide through the gap","target":"the sailing ship","voice":"female","keys":ship},
{"phrase":"to stretch out one leg","target":"the woman","voice":"female","keys":wom}],
"stillS":2.2,
"nouns":[{"word":"a drawbridge","x":0.36,"y":0.30,"voice":"female"},{"word":"a sailing ship","x":0.84,"y":0.68,"voice":"female"},
{"word":"a knitted hat","x":0.24,"y":0.62,"voice":"female"},{"word":"cobblestones","x":0.45,"y":0.92,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","heaving","an","iron","lever."],
"answerVoice":"female",
"notes":"Ship box starts at x~.75 so it never overlaps the woman's boot; it also covers the right raised bridge half in early frames (ship mostly behind it). Ship moves slowly, 'glide through the gap' is true but subtle in 4 s. Key word 'open up' not used: the bridge is already raised and it is unclear the lever opens it. Woman target used twice."}
json.dump(c,open('content/7394.json','w'),indent=1)
