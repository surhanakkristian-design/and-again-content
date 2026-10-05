import json
T=[i*0.5 for i in range(25)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
umb={0.0:(0.0,0.64,1.0,0.36),0.5:(0.0,0.69,1.0,0.31),1.0:(0.0,0.64,1.0,0.36),1.5:(0.0,0.65,1.0,0.35),
2.0:(0.0,0.66,1.0,0.34),2.5:(0.0,0.66,1.0,0.34),3.0:(0.0,0.69,1.0,0.31),3.5:(0.0,0.69,1.0,0.31),
4.0:(0.38,0.37,0.28,0.145),4.5:(0.40,0.36,0.28,0.145),5.0:(0.40,0.37,0.28,0.14),5.5:(0.40,0.36,0.28,0.14),
6.0:(0.42,0.33,0.28,0.145),6.5:(0.41,0.33,0.26,0.14),7.0:(0.36,0.33,0.26,0.14),
8.0:(0.44,0.46,0.20,0.14),8.5:(0.40,0.45,0.20,0.14),9.0:(0.38,0.45,0.20,0.14),9.5:(0.36,0.45,0.20,0.14),
10.0:(0.35,0.45,0.20,0.14),10.5:(0.34,0.45,0.20,0.14),11.0:(0.33,0.45,0.20,0.14),11.5:(0.32,0.45,0.20,0.14),12.0:(0.33,0.45,0.20,0.14)}
man={0.0:(0.37,0.47,0.18,0.17),0.5:(0.37,0.49,0.18,0.20),1.0:(0.35,0.50,0.18,0.14),1.5:(0.36,0.50,0.18,0.15),
2.0:(0.28,0.50,0.20,0.16),2.5:(0.26,0.51,0.21,0.15),3.0:(0.18,0.50,0.18,0.19),3.5:(0.23,0.50,0.20,0.19)}
wom={4.0:(0.47,0.515,0.18,0.20),4.5:(0.47,0.505,0.18,0.19),5.0:(0.48,0.51,0.18,0.20),5.5:(0.49,0.50,0.19,0.19),
6.0:(0.50,0.475,0.20,0.16),6.5:(0.50,0.47,0.18,0.15)}
r=lambda b: None if b is None else tuple(round(v,3) for v in b)
U=[k(t,r(umb.get(t))) for t in T]; M=[k(t,man.get(t)) for t in T]; W=[k(t,r(wom.get(t))) for t in T]
c={"mediaId":5412,"level":"B","keyWord":"pillar","defaultVoice":"female",
"taps":[{"phrase":"to stand out in the crowd","target":"the red umbrella","voice":"female","keys":U},
{"phrase":"to carry a black rucksack","target":"the man with the rucksack","voice":"male","keys":M},
{"phrase":"to wave her arms excitedly","target":"the woman in the dark dress","voice":"female","keys":W}],
"stillS":1.0,
"nouns":[{"word":"pillars","x":0.36,"y":0.33,"voice":"female"},
{"word":"the sky","x":0.53,"y":0.22,"voice":"female"},
{"word":"tourists","x":0.52,"y":0.57,"voice":"female"},
{"word":"an umbrella","x":0.50,"y":0.85,"voice":"female"}],
"question":"What are the tourists doing?",
"answer":["The","tourists","are","photographing","the","ancient","ruins."],"answerVoice":"female",
"notes":"Crowd clip, three shots. Umbrella: big foreground 0-3.5 s, held over the guide 4.0-7.0 s, tiny at the viewpoint 8.0-12.0 s; off at 7.5 s (cross-fade shows two ghost umbrellas). Man with the black rucksack only in shot 1 (0-3.5 s; a woman ahead also wears a small teal backpack). Woman in the dark dress (guide-like, waving under the umbrella) 4.0-6.5 s, small, boxes split from the umbrella box along its lower edge; off at 7.0 s (not identifiable). Answer is about shot 2 (many tourists film/photograph with phones). Key word as plural 'pillars' (many pillars across the frame; pill on the centre pillar)."}
json.dump(c,open("content/5412.json","w"),indent=1)
