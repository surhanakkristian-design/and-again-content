import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
W={0.0:(0.37,0.20,0.42,0.58),0.5:(0.37,0.21,0.42,0.57),1.0:(0.38,0.21,0.46,0.59),1.5:(0.37,0.17,0.52,0.68),
 2.0:(0.41,0.17,0.46,0.68),2.5:(0.25,0.27,0.65,0.73),3.0:(0.27,0.22,0.62,0.78),3.5:(0.15,0.17,0.85,0.83),
 4.0:(0.20,0.03,0.80,0.97),4.5:(0.10,0.0,0.90,1.0),5.0:(0.0,0.04,1.0,0.96),5.5:(0.15,0.02,0.85,0.98),
 6.0:(0.18,0.03,0.82,0.97),6.5:(0.34,0.23,0.50,0.58),7.0:(0.33,0.31,0.29,0.54),7.5:(0.22,0.28,0.30,0.55),
 8.0:(0.06,0.33,0.34,0.40),8.5:(0.0,0.35,0.36,0.38),9.0:(0.0,0.36,0.35,0.39)}
F={7.0:(0.62,0.36,0.18,0.26),7.5:(0.52,0.31,0.29,0.33),8.0:(0.40,0.38,0.46,0.31),8.5:(0.38,0.40,0.48,0.31),9.0:(0.36,0.40,0.58,0.35)}
c={"mediaId":5469,"level":"B","keyWord":"walker","defaultVoice":"female",
"taps":[{"phrase":"to stride with walking poles","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to glance at her smartwatch","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to spray a jet of water","target":"the fountain","voice":"female","keys":keys(F)}],
"stillS":8.5,
"nouns":[{"word":"a walker","x":0.20,"y":0.50,"voice":"female"},{"word":"a fountain","x":0.62,"y":0.55,"voice":"female"},
{"word":"geese","x":0.84,"y":0.42,"voice":"female"},{"word":"the sky","x":0.50,"y":0.12,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","gripping","two","walking","poles."],"answerVoice":"female",
"notes":"Woman is the only clear person; used for two phrases. Fountain (third target) only from 7.0 s; off before (at 6.5 it is hidden behind her). At 7.0-9.0 her reaching arm/poles touch the fountain, boxes split along the line between them. Birds on the lake look like Canada geese (clear at 3.0-6.0), tiny at the still."}
json.dump(c,open('content/5469.json','w'),indent=1)
