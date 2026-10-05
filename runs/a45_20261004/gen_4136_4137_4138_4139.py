import json
def keys(T,tab):
    out=[]
    for t in T:
        b=tab.get(t)
        out.append({"t":t,"off":True} if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]))
    return out
def save(d): json.dump(d,open("content/%d.json"%d["mediaId"],"w"),indent=1,ensure_ascii=False)

# ---------- 4136
T=[i*0.5 for i in range(24)]
man={}
for t in T[:8]: man[t]=(0.10,0.18,0.90,0.78)
man.update({4.0:(0.27,0.28,0.42,0.42),4.5:(0.25,0.24,0.47,0.50),5.0:(0.22,0.36,0.50,0.56),5.5:(0.18,0.34,0.60,0.64),
 6.0:(0.05,0.50,0.95,0.50),6.5:(0.05,0.66,0.95,0.34),
 10.0:(0.15,0.38,0.68,0.30),10.5:(0.17,0.23,0.67,0.45),11.0:(0.17,0.38,0.66,0.30),11.5:(0.17,0.34,0.66,0.34)})
dog={}
for t in (7.0,7.5,8.0,8.5,9.0,9.5):
    man[t]=(0.30,0.18,0.54,0.82); dog[t]=(0.0,0.26,0.30,0.36)
mk=keys(T,man)
save({"mediaId":4136,"level":"A","keyWord":"to exercise","defaultVoice":"male",
"taps":[
 {"phrase":"to exercise on the floor","target":"the man","voice":"male","keys":mk},
 {"phrase":"to lift heavy weights","target":"the man","voice":"male","keys":mk},
 {"phrase":"to stand on the bench","target":"the dog behind the man","voice":"male","keys":keys(T,dog)}],
"stillS":9.0,
"nouns":[{"word":"a bench","x":0.15,"y":0.54,"voice":"male"},
 {"word":"a curtain","x":0.62,"y":0.15,"voice":"male"},
 {"word":"trousers","x":0.42,"y":0.70,"voice":"male"},
 {"word":"the floor","x":0.17,"y":0.88,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","exercising","with","the","dogs."],
"answerVoice":"male",
"notes":"Four shots (cuts at 4.0, 7.0, 10.0). Several golden retrievers that look alike, so the only dog target is the one standing on the red bench in the bench shot (7.0-9.5); it is off in the other shots. In that shot the man's raised left arm and dumbbell pass in front of the dog: boxes split at x 0.30, the dog's head (above the man's head) lies in the man's box. In shot 1 the man's box includes the dogs he hugs (no dog target there). defaultVoice male = main person, the dog phrase uses it. Nouns avoid 'a dog' because two dogs are visible at 9.0 s."})

# ---------- 4137
T=[i*0.5 for i in range(25)]
D={0.0:(0.17,0.46,0.23,0.28),0.5:(0.17,0.46,0.22,0.28),1.0:(0.14,0.47,0.24,0.40),1.5:(0.10,0.47,0.28,0.38),
 2.0:(0.10,0.46,0.29,0.28),2.5:(0.10,0.46,0.29,0.28),3.0:(0.10,0.47,0.29,0.40),3.5:(0.09,0.46,0.34,0.40),
 4.0:(0.12,0.46,0.35,0.28),4.5:(0.12,0.46,0.34,0.28),5.0:(0.12,0.47,0.33,0.40),5.5:(0.12,0.47,0.32,0.40),
 6.0:(0.12,0.46,0.33,0.28),6.5:(0.12,0.46,0.33,0.28),7.0:(0.12,0.47,0.33,0.40),7.5:(0.12,0.47,0.33,0.40),
 8.0:(0.12,0.46,0.32,0.28),8.5:(0.12,0.46,0.35,0.28),9.0:(0.12,0.46,0.37,0.40),9.5:(0.12,0.46,0.37,0.40),
 10.0:(0.12,0.45,0.37,0.29),10.5:(0.12,0.45,0.37,0.29),11.0:(0.12,0.46,0.36,0.40),11.5:(0.12,0.46,0.36,0.40),12.0:(0.12,0.45,0.36,0.28)}
M={0.0:(0.40,0.30,0.60,0.42),0.5:(0.39,0.32,0.61,0.40),1.0:(0.38,0.34,0.62,0.52),1.5:(0.38,0.34,0.62,0.52),
 2.0:(0.39,0.34,0.61,0.39),2.5:(0.39,0.34,0.61,0.39),3.0:(0.39,0.35,0.61,0.51),3.5:(0.43,0.33,0.57,0.53),
 4.0:(0.48,0.38,0.52,0.40),4.5:(0.47,0.36,0.53,0.42),5.0:(0.45,0.38,0.55,0.54),5.5:(0.44,0.33,0.56,0.59),
 6.0:(0.46,0.34,0.54,0.52),6.5:(0.46,0.34,0.54,0.52),7.0:(0.45,0.36,0.55,0.60),7.5:(0.45,0.36,0.55,0.60),
 8.0:(0.44,0.36,0.56,0.51),8.5:(0.48,0.35,0.52,0.52),9.0:(0.49,0.37,0.51,0.63),9.5:(0.49,0.37,0.51,0.63),
 10.0:(0.49,0.40,0.51,0.49),10.5:(0.49,0.40,0.51,0.49),11.0:(0.48,0.42,0.52,0.58),11.5:(0.48,0.42,0.52,0.58),12.0:(0.48,0.42,0.52,0.47)}
mk=keys(T,M)
save({"mediaId":4137,"level":"A","keyWord":"yellow","defaultVoice":"male",
"taps":[
 {"phrase":"to wear a yellow dress","target":"the man","voice":"male","keys":mk},
 {"phrase":"to pick up a toy","target":"the man","voice":"male","keys":mk},
 {"phrase":"to bite a yellow toy","target":"the dog","voice":"male","keys":keys(T,D)}],
"stillS":10.0,
"nouns":[{"word":"a dog","x":0.27,"y":0.63,"voice":"male"},
 {"word":"a dress","x":0.75,"y":0.72,"voice":"male"},
 {"word":"a bed","x":0.36,"y":0.43,"voice":"male"},
 {"word":"a chair","x":0.87,"y":0.43,"voice":"male"}],
"question":"What is the dog holding?",
"answer":["The","dog","is","holding","a","yellow","toy."],
"answerVoice":"male",
"notes":"One shot, the camera zooms slightly in and out. The man leans over the dog: boxes split along a vertical line just right of the dog's nose / the toy, so the man's outstretched arm and, in the first 3 s, part of his head lie over the dog's box column. 'to wear a yellow dress' is a state, chosen for the key word. 'to bite a yellow toy' = the dog holds the yellow rubber bone in its mouth from 8.5 s; the man holds it in his hand before that (he does not bite it). 'a bed' = the white cot. Key word 'yellow' is a colour, so it is in the phrases and the answer, not a noun pill."})

# ---------- 4138
T=[i*0.5 for i in range(24)]
M={0.0:(0.0,0.12,0.68,0.74),0.5:(0.0,0.10,0.67,0.74),1.0:(0.0,0.08,0.62,0.76),1.5:(0.0,0.08,0.60,0.74),
 2.0:(0.0,0.07,0.50,0.75),2.5:(0.0,0.08,0.50,0.75),3.0:(0.0,0.09,0.46,0.86),3.5:(0.0,0.14,0.50,0.82),
 4.0:(0.0,0.13,0.52,0.71),4.5:(0.0,0.13,0.52,0.71),
 10.0:(0.07,0.0,0.90,0.39),10.5:(0.07,0.03,0.90,0.28),11.0:(0.12,0.09,0.74,0.37),11.5:(0.17,0.17,0.60,0.24)}
D={0.0:(0.80,0.28,0.20,0.20),0.5:(0.69,0.25,0.31,0.28),1.0:(0.63,0.26,0.37,0.32),1.5:(0.60,0.25,0.40,0.33),
 2.0:(0.50,0.28,0.50,0.36),2.5:(0.50,0.28,0.48,0.38),3.0:(0.46,0.30,0.50,0.36),3.5:(0.50,0.31,0.47,0.53),
 4.0:(0.52,0.30,0.43,0.42),4.5:(0.52,0.30,0.45,0.43),
 8.5:(0.44,0.24,0.24,0.19),9.0:(0.43,0.19,0.28,0.23),9.5:(0.33,0.12,0.39,0.39),
 10.0:(0.58,0.39,0.42,0.61),10.5:(0.25,0.31,0.75,0.61),11.0:(0.24,0.46,0.60,0.36),11.5:(0.10,0.41,0.78,0.50)}
for t in (5.0,5.5,6.0,6.5,7.0,7.5,8.0):
    D[t]=(0.0,0.22,0.53,0.76); M[t]=(0.53,0.11,0.47,0.89)
mk=keys(T,M)
save({"mediaId":4138,"level":"A","keyWord":"pet","defaultVoice":"male",
"taps":[
 {"phrase":"to pet the dog","target":"the man","voice":"male","keys":mk},
 {"phrase":"to hold an ice cream","target":"the man","voice":"male","keys":mk},
 {"phrase":"to run across the grass","target":"the dog","voice":"male","keys":keys(T,D)}],
"stillS":6.0,
"nouns":[{"word":"a dog","x":0.25,"y":0.60,"voice":"male"},
 {"word":"a cap","x":0.80,"y":0.22,"voice":"male"},
 {"word":"an ice cream","x":0.50,"y":0.44,"voice":"male"},
 {"word":"trousers","x":0.72,"y":0.85,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","petting","the","dog."],
"answerVoice":"male",
"notes":"Three scenes (cuts at 5.0 and 8.5; the man is out of frame 8.5-9.5 while the dog runs towards the camera). Man and dog touch in most frames: boxes split along a vertical line in the drive and car shots (the man's hands on the dog's head / his hand with the ice cream reach into the dog's column) and along a horizontal line in the garden (10.0-11.5: the man's upper body above, the dog below; his legs are behind the dog). 'a cap' and 'trousers' are both on the man but far apart in the close car shot."})

# ---------- 4139
T=[i*0.5 for i in range(25)]
M={};S={};R={}
for t in (0.0,0.5,1.0,1.5): S[t]=(0.02,0.36,0.43,0.28); M[t]=(0.45,0.44,0.31,0.28)
for t in (2.0,2.5,3.0,3.5): S[t]=(0.02,0.36,0.44,0.28); M[t]=(0.46,0.44,0.30,0.28)
S[4.0]=(0.04,0.36,0.44,0.28); M[4.0]=(0.48,0.44,0.29,0.28)
R.update({4.5:(0.21,0.05,0.51,0.46),5.0:(0.21,0.07,0.51,0.46),5.5:(0.21,0.09,0.51,0.45),6.0:(0.22,0.10,0.50,0.42),
 6.5:(0.22,0.11,0.50,0.42),7.0:(0.22,0.13,0.50,0.42),7.5:(0.22,0.14,0.50,0.42),
 11.0:(0.23,0.14,0.52,0.36),11.5:(0.23,0.14,0.52,0.36),12.0:(0.22,0.14,0.53,0.35)})
M.update({11.0:(0.46,0.52,0.28,0.34),11.5:(0.46,0.53,0.27,0.31),12.0:(0.47,0.53,0.26,0.27)})
save({"mediaId":4139,"level":"B","keyWord":"path","defaultVoice":"male",
"taps":[
 {"phrase":"to hike up a narrow path","target":"the man","voice":"male","keys":keys(T,M)},
 {"phrase":"to flutter above the grass","target":"the white sheet","voice":"male","keys":keys(T,S)},
 {"phrase":"to tower above the hillside","target":"the rock tower","voice":"male","keys":keys(T,R)}],
"stillS":12.0,
"nouns":[{"word":"a path","x":0.45,"y":0.90,"voice":"male"},
 {"word":"a rucksack","x":0.60,"y":0.63,"voice":"male"},
 {"word":"a peak","x":0.45,"y":0.25,"voice":"male"},
 {"word":"grass","x":0.80,"y":0.78,"voice":"male"}],
"question":"Where is the man hiking?",
"answer":["He","is","hiking","up","a","narrow","path."],
"answerVoice":"male",
"notes":"Four shots (cuts at 4.5, 8.0, 11.0). The man is boxed in shot 1 (with the sheet) and shot 4 (on the path); the grey legs and orange trainers of the point-of-view shot 2 are probably his but show no identifiable person, so he is 'off' there. Shot 3 (road, ginkgo trees, pagoda) has no target. The sheet is held by the man: boxes split at his raised left hand, the part of the sheet behind his body lies in his box. The rock tower is boxed in shots 2 and 4; in shot 4 its box ends where the green hillside begins. Doubt: the hazy cliff behind the pagoda in shot 3 also 'towers', but there is no hillside there. 'a peak' = the top of the rock tower."})
