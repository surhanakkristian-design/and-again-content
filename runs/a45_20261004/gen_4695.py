import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0.55,0,0.45,0.90),0.5:(0.70,0,0.30,0.88),1.0:(0.65,0,0.35,0.97),1.5:(0.62,0,0.38,1.0),2.0:(0.58,0,0.42,0.92),
2.5:(0.55,0,0.45,0.58),3.0:(0.45,0,0.55,0.60),3.5:(0.28,0,0.72,0.60),4.0:(0.18,0,0.82,0.50),4.5:(0.20,0,0.80,0.48),
5.0:(0.38,0,0.62,0.50),5.5:(0.25,0,0.75,0.50),6.0:(0.42,0,0.58,0.52),
6.5:(0.30,0.14,0.48,0.22),7.0:(0.22,0.08,0.56,0.23),7.5:(0.18,0.08,0.62,0.25),8.0:(0.20,0.08,0.66,0.31),8.5:(0.20,0.08,0.66,0.30),
9.0:(0.20,0.09,0.62,0.34),9.5:(0.20,0.12,0.60,0.34),10.0:(0.20,0.15,0.62,0.36),10.5:(0.25,0.10,0.65,0.42),
11.0:(0.25,0.08,0.63,0.58),11.5:(0.25,0.08,0.65,0.58),12.0:(0.25,0.09,0.60,0.47)}
box={2.5:(0.08,0.59,0.92,0.41),3.0:(0.02,0.61,0.98,0.39),3.5:(0,0.61,1,0.39),4.0:(0,0.51,0.97,0.49),4.5:(0.03,0.49,0.97,0.51),
5.0:(0,0.51,1,0.49),5.5:(0,0.51,1,0.49),6.0:(0,0.53,0.97,0.47)}
toys={6.5:(0.25,0.37,0.55,0.14),7.0:(0.20,0.32,0.62,0.27),7.5:(0.05,0.34,0.95,0.64),8.0:(0,0.40,1,0.60),8.5:(0,0.42,1,0.58),
9.0:(0,0.45,1,0.55),9.5:(0,0.47,1,0.53),10.0:(0,0.52,1,0.48),10.5:(0,0.53,1,0.47),11.0:(0,0.67,1,0.33),11.5:(0,0.67,1,0.33),12.0:(0,0.57,1,0.43)}
j={"mediaId":4695,"level":"B","keyWord":"chaos","defaultVoice":"male",
"taps":[
{"phrase":"to tip out a drawer","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to stand beneath the drawer","target":"the cardboard box","voice":"male","keys":keys(box)},
{"phrase":"to spill across the floor","target":"the toys","voice":"male","keys":keys(toys)}],
"stillS":12.0,
"nouns":[{"word":"a cap","x":0.67,"y":0.13,"voice":"male"},{"word":"a cabinet","x":0.52,"y":0.36,"voice":"male"},
{"word":"a couch","x":0.88,"y":0.57,"voice":"male"},{"word":"toys","x":0.50,"y":0.80,"voice":"male"}],
"question":"What is the man tipping out?",
"answer":["He","is","tipping","out","a","cabinet","full","of","toys."],
"answerVoice":"male",
"notes":"Key word 'chaos' is abstract, so it is not a noun slot and not in the answer. Three shots: bin (0-2.0), drawer over cardboard box (2.5-6.0), cabinet of toys (6.5-12). Toys box is off in the drawer shot (drawer contents are odds and ends, inside the cardboard-box region). From 11.0 the man stands behind the cabinet he holds; his box includes the cabinet. At 12.0 his feet reach slightly into the toys region (split at y 0.56)."}
json.dump(j,open("content/4695.json","w"),indent=1)
