import json
def keys(lst):
    out=[]
    for row in lst:
        t=row[0]
        if row[1] is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=row[1:]
            w=min(w,1-x); h=min(h,1-y)
            out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
man=keys([
(0.0,0,0,0.68,0.80),(0.5,0,0,0.58,0.80),(1.0,0,0,0.80,0.86),(1.5,0,0.02,0.80,0.84),
(2.0,0,0,0.74,0.82),(2.5,0,0,0.90,0.84),(3.0,0,0,0.82,0.86),(3.5,0,0,0.83,0.68),
(4.0,0,0,0.70,0.76),(4.5,0,0,0.62,0.70),(5.0,0,0,0.70,0.66),(5.5,0,0,0.70,0.62),
(6.0,0,0,0.68,0.64),(6.5,0,0,0.67,0.64),(7.0,0,0,0.70,0.76),(7.5,0,0.08,0.85,0.77),
(8.0,0,0.09,0.72,0.76),(8.5,0,0.06,0.62,0.83),(9.0,0,0.06,0.75,0.88),(9.5,0,0.11,0.66,0.89),
(10.0,0,0,0.52,0.98),(10.5,0,0.04,0.56,0.84),(11.0,0,0.08,0.52,0.86),(11.5,0,0.10,0.70,0.90),(12.0,0,0.10,0.67,0.90)])
c={"mediaId":5490,"level":"B","keyWord":"weed","defaultVoice":"male",
"taps":[{"phrase":"to dig into the soil","target":"the man","voice":"male","keys":man},
{"phrase":"to pull out a weed","target":"the man","voice":"male","keys":man},
{"phrase":"to wear gardening gloves","target":"the man","voice":"male","keys":man}],
"stillS":12.0,
"nouns":[{"word":"a straw hat","x":0.14,"y":0.14,"voice":"male"},
{"word":"a weed","x":0.66,"y":0.30,"voice":"male"},
{"word":"a cornfield","x":0.72,"y":0.50,"voice":"male"},
{"word":"soil","x":0.62,"y":0.92,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","pulling","a","weed","out","of","the","soil."],
"answerVoice":"male",
"notes":"Only one person, so all three phrases target the man. Close, shaky handheld shots; he is often only partly in frame (hat, arm, gloves). The weed pill sits on the leafy weed he holds up at 12.0; a second uprooted plant lies in the bed at the lower right (x 0.75, y 0.72) - verifier: check 'a weed' is not ambiguous there."}
json.dump(c,open('/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/content/5490.json','w'),indent=1)
