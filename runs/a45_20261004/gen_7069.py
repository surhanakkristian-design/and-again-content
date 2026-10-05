import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(bs):
    out=[]
    for t,b in zip(T,bs):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def tap(p,tg,v,bs): return {"phrase":p,"target":tg,"voice":v,"keys":keys(bs)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
D={}
# 7069
man=[(0.56,0.38,0.24,0.26),(0.53,0.37,0.26,0.30),(0.49,0.37,0.28,0.33),(0.47,0.37,0.29,0.35),(0.44,0.36,0.31,0.34),(0.46,0.34,0.31,0.36),(0.44,0.33,0.32,0.39),(0.43,0.33,0.34,0.41)]
yw=[(0.15,0.38,0.19,0.32),(0.17,0.38,0.19,0.32),(0.17,0.38,0.19,0.33),(0.20,0.38,0.19,0.33),(0.18,0.37,0.20,0.34),(0.19,0.37,0.20,0.34),(0.17,0.37,0.22,0.35),(0.15,0.37,0.24,0.35)]
ow=[(0.07,0.10,0.22,0.15),(0.08,0.10,0.22,0.15),(0.09,0.09,0.22,0.15),(0.10,0.09,0.22,0.15),(0.10,0.09,0.22,0.15),(0.10,0.08,0.22,0.15),(0.09,0.08,0.22,0.15),(0.09,0.08,0.22,0.15)]
D[7069]={"mediaId":7069,"level":"B","keyWord":"drive up","defaultVoice":"male",
 "taps":[tap("to raise his straw hat","the man","male",man),tap("to stand on the doorstep","the young woman","female",yw),tap("to peer from a window","the old woman","female",ow)],
 "stillS":3.7,
 "nouns":[noun("a tractor",0.55,0.68,"male"),noun("sunflowers",0.80,0.54,"male"),noun("a straw hat",0.52,0.38,"male"),noun("gravel",0.50,0.92,"male")],
 "question":"What is the man doing?","answer":["He","is","driving","up","on","a","red","tractor."],"answerVoice":"male",
 "notes":"Man box covers the man only (he sits on the tractor, tractor is not a target). Hat is raised from t=2.2. Old woman is small in the upstairs window."}
# 7761
oc=[(0.05,0.44,0.50,0.29),(0.07,0.44,0.49,0.32),(0.08,0.41,0.48,0.35),(0.13,0.39,0.44,0.38),(0.09,0.39,0.48,0.37),(0.05,0.38,0.51,0.37),(0.00,0.38,0.57,0.38),(0.00,0.36,0.59,0.40)]
wo=[(0.56,0.33,0.17,0.21),(0.57,0.32,0.18,0.18),(0.58,0.33,0.16,0.19),(0.60,0.32,0.15,0.20),(0.60,0.30,0.16,0.21),(0.59,0.29,0.17,0.22),(0.60,0.30,0.16,0.21),(0.60,0.30,0.16,0.21)]
mn=[(0.74,0.30,0.23,0.38),(0.76,0.30,0.23,0.38),(0.76,0.29,0.24,0.40),(0.76,0.28,0.24,0.44),(0.77,0.26,0.23,0.46),(0.77,0.25,0.23,0.47),(0.77,0.25,0.23,0.58),(0.77,0.25,0.23,0.58)]
D[7761]={"mediaId":7761,"level":"B","keyWord":"being","defaultVoice":"male",
 "taps":[tap("to reach into a jar","the octopus","male",oc),tap("to clutch a clipboard","the man","male",mn),tap("to burst out laughing","the woman","female",wo)],
 "stillS":2.2,
 "nouns":[noun("an octopus",0.28,0.47,"male"),noun("a jar",0.38,0.72,"male"),noun("robots",0.45,0.30,"male"),noun("a clipboard",0.84,0.43,"male")],
 "question":"What is the octopus doing?","answer":["It","is","reaching","into","a","glass","jar."],"answerVoice":"male",
 "notes":"Key word 'being' is abstract here and not used as a noun slot. In the clip the octopus opens the jar, reaches in and pulls out a crab (the description says it slides in). Octopus box is cut on the right at t=0.7 and 3.7 so it does not overlap the woman's box (lid / crab partly outside). Two robots stand together -> plural 'robots'."}
# 5626
m5=[(0.50,0.22,0.48,0.62),(0.50,0.23,0.50,0.61),(0.50,0.24,0.48,0.60),(0.50,0.25,0.50,0.59),(0.50,0.25,0.46,0.59),(0.50,0.25,0.50,0.58),(0.54,0.28,0.46,0.56),(0.57,0.35,0.43,0.46)]
cat=[(0.27,0.55,0.19,0.15)]*8
org=[None,(0.16,0.71,0.18,0.14),(0.12,0.76,0.18,0.14),(0.10,0.74,0.18,0.14),(0.06,0.77,0.18,0.14),(0.00,0.78,0.18,0.14),(0.02,0.78,0.18,0.14),(0.01,0.78,0.18,0.14)]
D[5626]={"mediaId":5626,"level":"B","keyWord":"be out of order","defaultVoice":"male",
 "taps":[tap("to kneel on the pavement","the man","male",m5),tap("to sit among the oranges","the cat","male",cat),tap("to roll across the pavement","the loose orange","male",org)],
 "stillS":2.2,
 "nouns":[noun("a cat",0.37,0.61,"male"),noun("a tram",0.33,0.42,"male"),noun("a delivery robot",0.35,0.74,"male"),noun("wind turbines",0.27,0.12,"male")],
 "question":"What is inside the delivery robot?","answer":["A","cat","is","sitting","among","the","oranges."],"answerVoice":"male",
 "notes":"The loose orange is not yet visible at t=0.2 (off). The man kneels until about t=3.2 and sits down at 3.7. The cat sits inside the robot, so 'a cat' and 'a delivery robot' pills are 0.13 apart in y. Key phrase 'be out of order' is not shown literally and is not used."}
# 7929
tr=[(0.00,0.00,1.00,0.31),(0.00,0.00,1.00,0.36),(0.00,0.19,0.97,0.24),(0.00,0.25,0.95,0.24),(0.02,0.27,0.92,0.25),(0.00,0.30,0.95,0.26),(0.00,0.31,0.92,0.25),(0.00,0.31,0.92,0.25)]
m9=[None,None,(0.50,0.00,0.24,0.19),(0.45,0.00,0.34,0.25),(0.46,0.03,0.30,0.24),(0.44,0.04,0.32,0.26),(0.43,0.05,0.35,0.26),(0.43,0.05,0.35,0.26)]
w9=[(0.16,0.32,0.23,0.39),(0.16,0.37,0.23,0.39),(0.16,0.44,0.22,0.37),(0.15,0.50,0.23,0.37),(0.14,0.53,0.23,0.38),(0.15,0.57,0.23,0.36),(0.15,0.57,0.23,0.36),(0.16,0.57,0.22,0.36)]
D[7929]={"mediaId":7929,"level":"B","keyWord":"parking","defaultVoice":"male",
 "taps":[tap("to crush two small cars","the monster truck","male",tr),tap("to raise both fists","the man on the truck","male",m9),tap("to fold her arms","the woman in front","female",w9)],
 "stillS":2.2,
 "nouns":[noun("a monster truck",0.30,0.27,"male"),noun("a red car",0.55,0.61,"male"),noun("a parking space",0.68,0.82,"male"),noun("boots",0.24,0.83,"male")],
 "question":"What is the monster truck doing?","answer":["It","is","crushing","two","small","cars."],"answerVoice":"male",
 "notes":"The man stands on the truck: his box is the upper part (head to knees), the truck box starts below it (split line), so the truck's cab roof left of him is outside the truck box. At t=0.2 and 0.7 only his legs are in the picture -> off; at 1.2 his head is still cut off. Key word 'parking' is used as 'a parking space' on the empty marked bay right of the red car. A second woman (sunglasses) and a blond man appear at the right edge from t=1.2 / 2.7; neither folds arms nor raises fists."}
for i,d in D.items():
    json.dump(d,open(f"content/{i}.json","w"),indent=1,ensure_ascii=False)
