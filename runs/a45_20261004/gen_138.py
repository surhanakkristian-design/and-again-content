import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0.39,0.10,0.61,0.90),0.5:(0.40,0.10,0.60,0.90),1.0:(0.38,0.12,0.62,0.88),1.5:(0.31,0.14,0.69,0.86),
2.0:(0.16,0.12,0.84,0.88),2.5:(0.16,0.26,0.84,0.74),3.0:(0.16,0.26,0.84,0.74),3.5:(0.0,0.24,1.0,0.76),4.0:(0.0,0.20,1.0,0.80),
4.5:(0.06,0.20,0.94,0.80),5.0:(0.13,0.22,0.87,0.78),5.5:(0.17,0.22,0.83,0.78),6.0:(0.24,0.21,0.76,0.79),6.5:(0.27,0.18,0.73,0.82),
7.0:(0.27,0.21,0.73,0.79),7.5:(0.38,0.24,0.62,0.76),8.0:(0.40,0.21,0.60,0.79),8.5:(0.36,0.21,0.64,0.79),9.0:(0.65,0.24,0.35,0.76)}
wom={0.0:(0.0,0.21,0.39,0.79),0.5:(0.0,0.25,0.40,0.75),1.0:(0.0,0.26,0.38,0.74),1.5:(0.0,0.28,0.31,0.72),
2.0:(0.0,0.33,0.16,0.67),2.5:(0.0,0.38,0.16,0.62),3.0:(0.0,0.40,0.16,0.45),
5.0:(0.0,0.34,0.13,0.40),5.5:(0.0,0.31,0.17,0.69),6.0:(0.0,0.29,0.24,0.71),6.5:(0.0,0.28,0.27,0.72),
7.0:(0.0,0.30,0.27,0.70),7.5:(0.0,0.31,0.38,0.69),8.0:(0.0,0.29,0.40,0.71),8.5:(0.0,0.27,0.36,0.73),9.0:(0.0,0.28,0.62,0.72),9.5:(0.48,0.23,0.52,0.77)}
c={"mediaId":138,"level":"A","keyWord":"cap","defaultVoice":"male",
"taps":[{"phrase":"to cover his eyes","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to give him a cap","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to turn his cap around","target":"the man","voice":"male","keys":keys(man)}],
"stillS":3.5,
"nouns":[{"word":"a cap","x":0.60,"y":0.33,"voice":"male"},{"word":"a T-shirt","x":0.55,"y":0.80,"voice":"male"},{"word":"a tree","x":0.15,"y":0.55,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","turning","his","cap","around."],"answerVoice":"male",
"notes":"Woman is only a sliver at the left edge 2.0-3.0 and 5.0 (narrow boxes); off at 3.5-4.5. Cat appears only in the last frame, not used. 'a tree' = blurred palm trunk at the left of the still."}
json.dump(c,open("content/138.json","w"),indent=1)
