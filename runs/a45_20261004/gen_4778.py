import json
T=[round(i*0.5,1) for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
W={}
for t in [5.0,5.5,6.0,6.5,7.0,7.5,8.0]: W[t]=(0.0,0.0,1.0,1.0)
W.update({8.5:(0.28,0.40,0.83,1.0),9.0:(0.29,0.36,0.86,1.0),9.5:(0.32,0.36,0.86,1.0),10.0:(0.30,0.36,0.87,1.0),
 10.5:(0.33,0.36,0.86,1.0),11.0:(0.31,0.37,0.86,1.0),11.5:(0.33,0.38,0.84,1.0),12.0:(0.30,0.39,0.78,1.0)})
C={8.5:(0.08,0.02,0.55,0.40),9.0:(0.04,0.02,0.51,0.35),9.5:(0.01,0.02,0.44,0.35),10.0:(0.0,0.02,0.45,0.35),
 10.5:(0.0,0.02,0.45,0.35),11.0:(0.0,0.02,0.44,0.36),11.5:(0.0,0.02,0.44,0.37),12.0:(0.0,0.02,0.42,0.38)}
M={8.5:(0.83,0.30,1.0,1.0),9.0:(0.86,0.36,1.0,1.0),9.5:(0.86,0.36,1.0,1.0),10.0:(0.87,0.36,1.0,1.0),10.5:(0.86,0.36,1.0,1.0),
 11.0:(0.86,0.36,1.0,1.0),11.5:(0.84,0.36,1.0,1.0),12.0:(0.78,0.36,1.0,1.0)}
c={"mediaId":4778,"level":"B","keyWord":"workshop","defaultVoice":"female",
"taps":[
 {"phrase":"to adjust tiny brass gears","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to hang on a wooden pillar","target":"the cuckoo clock","voice":"female","keys":keys(C)},
 {"phrase":"to applaud his colleague","target":"the young man","voice":"male","keys":keys(M)}],
"stillS":12.0,
"nouns":[{"word":"a cuckoo clock","x":0.22,"y":0.16,"voice":"female"},
 {"word":"spanners","x":0.50,"y":0.34,"voice":"female"},
 {"word":"a colleague","x":0.88,"y":0.55,"voice":"male"},
 {"word":"a workbench","x":0.37,"y":0.73,"voice":"female"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","up","at","the","carved","cuckoo","clock."],
"answerVoice":"female",
"notes":"0-4.5 s show only hands at a spanner board (owner unclear, likely the woman) -> marked off for all targets. 'workshop' is the whole scene, not placeable as a noun slot. Man applauds only at 12.0 s; he is partly hidden behind the woman 9.0-11.5 s (split line ~0.86). 'spanners' (BrE) = wrenches on the wall board."}
json.dump(c,open("content/4778.json","w"),indent=1)
