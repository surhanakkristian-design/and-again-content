import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W1=(0,0.13,0.92,0.47); C1=(0.26,0.61,0.36,0.39); C2=(0.26,0.60,0.61,0.40)
wom={0.0:W1,0.5:W1,1.0:(0,0.15,0.92,0.58),1.5:(0,0.15,0.92,0.58),2.0:W1,
3.5:(0,0.13,0.94,0.57),4.0:(0,0.13,0.92,0.46),4.5:(0,0.13,0.92,0.46),5.0:(0,0.13,0.92,0.46),5.5:(0,0.13,0.92,0.46),6.0:(0,0.13,0.92,0.46),6.5:(0,0.13,0.92,0.46),
7.0:(0.36,0.23,0.57,0.51),7.5:(0.40,0.23,0.54,0.54),8.0:(0.42,0.17,0.52,0.50),8.5:(0.38,0.22,0.58,0.52),
9.0:(0.41,0.25,0.53,0.64),9.5:(0.40,0.08,0.54,0.85),10.0:(0.40,0.10,0.54,0.68),10.5:(0.40,0.12,0.56,0.71),
11.0:(0.37,0.13,0.58,0.85),11.5:(0.35,0.13,0.62,0.86),12.0:(0.34,0.10,0.62,0.74)}
cr={0.0:C1,0.5:C1,1.0:(0.26,0.74,0.38,0.26),1.5:(0.26,0.74,0.38,0.26),2.0:C1,
2.5:(0.05,0.36,0.95,0.64),3.0:(0.02,0.37,0.98,0.63),3.5:(0.30,0.71,0.58,0.29),
4.0:C2,4.5:C2,5.0:C2,5.5:C2,6.0:C2,6.5:C2,
7.0:(0,0.75,0.82,0.25),7.5:(0,0.78,0.80,0.22),8.0:(0,0.68,0.82,0.32),8.5:(0,0.75,0.82,0.25),
9.0:(0,0.72,0.40,0.28),9.5:(0,0.84,0.39,0.16),10.0:(0,0.79,0.76,0.21),10.5:(0,0.84,0.80,0.16),
11.0:(0,0.84,0.36,0.16),11.5:(0,0.86,0.34,0.14),12.0:(0,0.85,0.78,0.15)}
j={"mediaId":4696,"level":"B","keyWord":"encourage","defaultVoice":"female",
"taps":[
{"phrase":"to grip a red hold","target":"the older woman","voice":"female","keys":keys(wom)},
{"phrase":"to scale an overhanging wall","target":"the older woman","voice":"female","keys":keys(wom)},
{"phrase":"to encourage the climber","target":"the crowd","voice":"female","keys":keys(cr)}],
"stillS":0.0,
"nouns":[{"word":"glasses","x":0.30,"y":0.26,"voice":"female"},{"word":"chalk","x":0.72,"y":0.33,"voice":"female"},
{"word":"an elbow","x":0.28,"y":0.47,"voice":"female"},{"word":"a climbing wall","x":0.72,"y":0.10,"voice":"female"}],
"question":"What is the crowd doing?",
"answer":["They","are","encouraging","the","older","woman."],
"answerVoice":"female",
"notes":"All spectators cheer alike, so they are one target ('the crowd'); the only other target is the climbing woman (two phrases). In the close shots (0-2.0, 3.5-6.5) the woman's box covers head, arm and upper body only: her hips and legs run down the left edge beside the crowd and are outside both boxes. In the wide shot (7.0+) the crowd's raised arms reach up beside her legs; boxes are split, at 9.0, 9.5, 11.0, 11.5 the crowd box is only the left part (two women bottom centre under her feet are left out). 'chalk' = the white chalk on her hand; 'an elbow' is a body-part noun, a weaker slot. Background wall is also a climbing wall."}
json.dump(j,open("content/4696.json","w"),indent=1)
