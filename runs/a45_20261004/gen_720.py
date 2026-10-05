import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={2.5:(0,0.15,0.46,0.85),3.0:(0,0.16,0.42,0.84),3.5:(0,0.17,0.40,0.83),4.0:(0,0.17,0.52,0.83),4.5:(0,0.18,0.56,0.82),
5.0:(0,0,0.78,0.54),5.5:(0,0,0.75,0.49),6.0:(0,0,1.0,0.34),6.5:(0,0,0.57,0.46),7.0:(0,0,0.60,0.47),7.5:(0,0,0.60,0.47),
8.0:(0.22,0,0.78,0.42),8.5:(0,0,1.0,0.41),9.0:(0,0.04,1.0,0.68),9.5:(0,0.04,1.0,0.68),10.0:(0,0.04,1.0,0.69)}
M={2.5:(0.46,0,0.54,1.0),3.0:(0.42,0,0.58,1.0),3.5:(0.40,0,0.60,1.0),4.0:(0.52,0,0.48,1.0),4.5:(0.56,0,0.44,1.0),
6.5:(0.57,0,0.43,0.46),7.0:(0.60,0,0.40,0.47),7.5:(0.60,0,0.40,0.47)}
P={5.0:(0.56,0.55,0.44,0.40),5.5:(0,0.49,1.0,0.40),6.0:(0,0.34,1.0,0.60),6.5:(0,0.46,1.0,0.44),7.0:(0,0.47,1.0,0.48),7.5:(0,0.47,1.0,0.48),
8.0:(0,0.42,1.0,0.50),8.5:(0,0.41,1.0,0.50),9.0:(0,0.72,1.0,0.28),9.5:(0,0.72,1.0,0.28),10.0:(0,0.73,1.0,0.27)}
c={"mediaId":720,"level":"B","keyWord":"spice","defaultVoice":"female",
"taps":[
{"phrase":"to sprinkle the red spice","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to sniff the paper cone","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to heat the cooking oil","target":"the frying pan","voice":"female","keys":keys(P)}],
"stillS":7.5,
"nouns":[{"word":"a headscarf","x":0.28,"y":0.07,"voice":"female"},{"word":"a beard","x":0.86,"y":0.38,"voice":"female"},
{"word":"spice","x":0.50,"y":0.66,"voice":"female"},{"word":"a frying pan","x":0.50,"y":0.84,"voice":"female"}],
"question":"What is she doing with the spice?",
"answer":["She","is","sprinkling","it","into","the","frying","pan."],"answerVoice":"female",
"notes":"Many cuts. 0.0-2.0 all targets off: only a blurred street and the vendor's hands (not used as a target). 2.5-4.5 woman and man are cheek to cheek, boxes split along the line between the faces; the hand holding the cone there is probably the woman's but falls partly in the man's box. Man sniffs the cone at 2.5-3.5 (the woman only wafts the smell with her hand at 7.0-7.5). Woman sprinkles at 5.0-6.0; at 6.0 only her hands/apron are visible at the top (teal sleeve at the right edge may be the man: left off for him). 8.0-8.5 woman = apron torso above the pan. Pan box starts at the rim; 'spice' pill is on the red heap inside the pan, 'a frying pan' pill on the metal rim below it. 'a beard' pill sits on the man's chin, small target."}
json.dump(c,open("content/720.json","w"),indent=1)
