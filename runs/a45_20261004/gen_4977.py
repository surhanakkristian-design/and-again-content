import json
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
M={0.0:(0.24,0.31,0.75,0.69),0.5:(0.18,0.33,0.80,0.67),1.0:(0.10,0.32,0.77,0.68),1.5:(0.16,0.32,0.78,0.68),2.0:(0.15,0.30,0.73,0.70),
 2.5:(0.16,0.33,0.72,0.67),3.0:(0.16,0.33,0.76,0.67),3.5:(0.16,0.34,0.72,0.66),4.0:(0.20,0.36,0.80,0.64),
 4.5:(0.55,0.42,0.40,0.58),5.0:(0.50,0.44,0.50,0.56),5.5:(0.46,0.45,0.54,0.55),6.0:(0.43,0.46,0.57,0.54),6.5:(0.40,0.46,0.60,0.54),
 7.0:(0.40,0.46,0.60,0.54),7.5:(0.40,0.46,0.60,0.54),8.0:(0.40,0.46,0.60,0.54),
 8.5:(0.08,0.54,0.86,0.46),9.0:(0.18,0.56,0.60,0.44),9.5:(0.29,0.56,0.45,0.38),10.0:(0.35,0.57,0.40,0.29),10.5:(0.31,0.55,0.42,0.33),
 11.0:(0.34,0.51,0.41,0.35),11.5:(0.30,0.49,0.42,0.34),12.0:(0.27,0.50,0.47,0.38)}
Y={4.5:(0.34,0.30,0.20,0.31),5.0:(0.15,0.38,0.33,0.30),5.5:(0.08,0.45,0.36,0.24),6.0:(0.04,0.46,0.38,0.22),6.5:(0.08,0.45,0.30,0.24),
 7.0:(0.08,0.46,0.30,0.22),7.5:(0.08,0.46,0.30,0.22),8.0:(0.08,0.46,0.30,0.22)}
c={"mediaId":4977,"level":"A","keyWord":"a hand","defaultVoice":"male",
 "taps":[
  {"phrase":"to walk through the fields","target":"the man","voice":"male","keys":K(M)},
  {"phrase":"to ride a big swing","target":"the man","voice":"male","keys":K(M)},
  {"phrase":"to have a long tail","target":"the monkey","voice":"male","keys":K(Y)}],
 "stillS":3.0,
 "nouns":[{"word":"the sky","x":0.30,"y":0.10,"voice":"male"},{"word":"palm trees","x":0.75,"y":0.24,"voice":"male"},
  {"word":"a hand","x":0.85,"y":0.56,"voice":"male"},{"word":"a path","x":0.12,"y":0.75,"voice":"male"}],
 "question":"What is the man sitting next to?",
 "answer":["He","is","sitting","next","to","a","monkey."],"answerVoice":"male",
 "notes":"Only two targets (man, monkey), so the man has two phrases. Monkey phrase is a state (tail) because the man also sits/looks; tail clearly visible 4.5-6.0. In the temple shot (4.5-8.0) the man's box is cut at the split line with the monkey (his hands/arm at left are partly outside). Foreground arm in shot 1 is the man's own selfie arm (wrist only); the noun 'a hand' sits on his open right hand."}
json.dump(c,open('content/4977.json','w'),indent=1)
