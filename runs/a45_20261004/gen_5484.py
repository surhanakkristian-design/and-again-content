import json
T=[i*0.5 for i in range(21)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
B={t:(0,0.55,0.35,0.31) for t in T}; B[3.0]=B[3.5]=(0,0.5,0.35,0.36)
Wm={t:(0.36,0.53,0.27,0.42) for t in T}
F={0.0:(0.22,0,0.6,0.35),0.5:(0.15,0,0.75,0.4),1.0:(0.15,0,0.8,0.4),1.5:(0.18,0,0.75,0.5),2.0:(0.18,0,0.78,0.5),
   2.5:(0.3,0.05,0.5,0.45),3.0:(0.42,0.12,0.25,0.38),3.5:(0.38,0.06,0.35,0.44),4.0:(0.3,0,0.5,0.5),4.5:(0.2,0,0.7,0.5),
   5.0:(0.05,0,0.9,0.5),5.5:(0.05,0,0.95,0.5),6.0:(0.05,0,0.9,0.5),6.5:(0.1,0,0.9,0.5),7.0:(0.15,0,0.85,0.5),
   7.5:(0.15,0,0.85,0.5),8.0:(0.05,0,0.95,0.5),8.5:(0.05,0,0.95,0.5),9.0:(0,0,1.0,0.5),9.5:(0,0,1.0,0.5),10.0:(0.05,0,0.95,0.5)}
c={"mediaId":5484,"level":"B","keyWord":"gaze","defaultVoice":"female",
 "taps":[
  {"phrase":"to point at the sky","target":"the boy","voice":"male","keys":K(B)},
  {"phrase":"to wear a rust-coloured cardigan","target":"the woman","voice":"female","keys":K(Wm)},
  {"phrase":"to light up the night sky","target":"the fireworks","voice":"female","keys":K(F)}],
 "stillS":0.0,
 "nouns":[{"word":"fireworks","x":0.52,"y":0.17,"voice":"female"},{"word":"smoke","x":0.66,"y":0.47,"voice":"female"},
   {"word":"roofs","x":0.12,"y":0.61,"voice":"female"},{"word":"a railing","x":0.2,"y":0.94,"voice":"female"}],
 "question":"What are the three people doing?",
 "answer":["They","are","gazing","at","the","fireworks."],
 "answerVoice":"female",
 "notes":"All three people gaze up, lean on the railing and open their mouths, so no shared action can be a phrase; the woman gets a state phrase (her cardigan is rust/terracotta; the boy wears a green hoodie, the man an olive hoodie). The boy points up only at 3.0-3.5 (hand at the left edge, box raised there). Boxes are near-static (static camera): boy and woman split at x~0.35 (her left hand on the railing lies inside the boy's box), the man is not a target. Fireworks boxes end at y 0.50, above the heads."}
json.dump(c,open('content/5484.json','w'),indent=1)
