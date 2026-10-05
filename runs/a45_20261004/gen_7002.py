import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
fish=K([(0.40,0.55,0.20,0.17),(0.41,0.55,0.20,0.17),(0.41,0.55,0.20,0.16),(0.40,0.55,0.20,0.16),(0.38,0.55,0.24,0.14),(0.37,0.54,0.27,0.14),(0.36,0.53,0.30,0.14),(0.38,0.53,0.30,0.14)])
bird=[(0.33,0.26,0.19,0.14)]*8
fall=[(0.53,0.00,0.47,0.48)]*8
c={"mediaId":7002,"level":"B","keyWord":"cup","defaultVoice":"female",
"taps":[
 {"phrase":"to glide through clear water","target":"the trout","voice":"female","keys":fish},
 {"phrase":"to cascade into the pool","target":"the waterfall","voice":"female","keys":K(fall)},
 {"phrase":"to perch on a ledge","target":"the small bird","voice":"female","keys":K(bird)}],
"stillS":2.7,
"nouns":[{"word":"a waterfall","x":0.62,"y":0.11,"voice":"female"},
 {"word":"a log","x":0.44,"y":0.22,"voice":"female"},
 {"word":"a trout","x":0.51,"y":0.61,"voice":"female"},
 {"word":"pine needles","x":0.15,"y":0.80,"voice":"female"}],
"question":"What is the trout doing?",
"answer":["The","trout","is","gliding","through","clear","water."],
"answerVoice":"female",
"notes":"No people. Key word 'cup' = the cup-shaped hollow in the rock; not used as a noun pill (it is only like a cup, a learner would not call it 'a cup'). The small bird (a dipper) sits still on the rock left of the falls all clip long: phrase is a state-like action, box at minimum size. Waterfall box starts at x 0.53 to stay clear of the bird box, so the upper left strip of the falls (x 0.35-0.53) is outside the box. The trout is small and faint, box at minimum size."}
json.dump(c,open('content/7002.json','w'),indent=1,ensure_ascii=False)
