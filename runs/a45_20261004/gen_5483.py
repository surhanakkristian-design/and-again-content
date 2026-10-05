import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
W={0.0:(0,0.27,0.65,0.73),0.5:(0,0.27,0.62,0.73),1.0:(0,0.28,0.77,0.72),1.5:(0,0.29,0.78,0.71),2.0:(0,0.32,0.7,0.68),
   2.5:(0,0.34,0.82,0.66),3.0:(0,0.34,0.84,0.66),3.5:(0,0.36,0.82,0.64),4.0:(0,0.37,0.9,0.63),4.5:(0,0.41,0.98,0.59),
   5.0:(0,0.47,0.88,0.53),5.5:(0,0.49,0.78,0.51),6.0:(0.04,0.53,0.76,0.47),6.5:(0.12,0.56,0.55,0.44),7.0:(0.18,0.6,0.46,0.4),
   7.5:(0.18,0.62,0.5,0.38),8.0:(0.22,0.66,0.48,0.34),8.5:(0.22,0.66,0.48,0.34),9.0:(0.2,0.66,0.42,0.34)}
F={6.0:(0.3,0.07,0.18,0.43),6.5:(0.28,0.13,0.68,0.42),7.0:(0.15,0.06,0.85,0.52),7.5:(0.12,0.0,0.88,0.6),
   8.0:(0,0,1.0,0.5),8.5:(0,0,1.0,0.6),9.0:(0,0,1.0,0.55)}
c={"mediaId":5483,"level":"B","keyWord":"scan","defaultVoice":"female",
 "taps":[
  {"phrase":"to scan the beach","target":"the woman in yellow","voice":"female","keys":K(W)},
  {"phrase":"to shade her eyes","target":"the woman in yellow","voice":"female","keys":K(W)},
  {"phrase":"to burst above the stadium","target":"the fireworks","voice":"female","keys":K(F)}],
 "stillS":6.5,
 "nouns":[{"word":"fireworks","x":0.5,"y":0.46,"voice":"female"},{"word":"a stadium","x":0.17,"y":0.6,"voice":"female"},
   {"word":"a crowd","x":0.85,"y":0.72,"voice":"female"},{"word":"binoculars","x":0.5,"y":0.92,"voice":"female"}],
 "question":"What is she doing on the seafront?",
 "answer":["She","is","scanning","the","beach","with","binoculars."],
 "answerVoice":"female",
 "notes":"Cut at ~4.0 from the seafront to a stadium. 'to shade her eyes' only at 0.0-0.5 (hand over her brow), before she lifts the binoculars. Fireworks: at 6.0 only one rising rocket trail, bursts from 6.5; fireworks box stops above her head (no overlap). In the stadium other women also look up, so no phrase about staring at the sky; the woman's box shrinks as the camera tilts up. Noun 'binoculars' on the pair she holds at chest height at 6.5."}
json.dump(c,open('content/5483.json','w'),indent=1)
