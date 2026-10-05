import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [ ({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)}) for t,b in zip(T,boxes)]
B=[(0.35,0.28,0.69,0.84),(0.34,0.27,0.70,0.86),(0.34,0.26,0.70,0.88),(0.29,0.24,0.70,0.94),(0.27,0.24,0.70,0.98),(0.29,0.21,0.72,1.0),(0.25,0.19,0.72,1.0),(0.27,0.19,0.72,1.0)]
M=[(0.0,0.36,0.31,0.56),(0.0,0.36,0.32,0.56),(0.0,0.37,0.32,0.58),(0.0,0.36,0.28,0.57),(0.0,0.38,0.26,0.56),(0.0,0.38,0.27,0.56),(0.0,0.37,0.24,0.56),(0.0,0.38,0.26,0.56)]
R=[(0.76,0.48,1.0,0.95),(0.75,0.48,1.0,0.95),(0.77,0.47,1.0,0.96),(0.80,0.48,1.0,0.96),(0.77,0.48,1.0,1.0),(0.73,0.46,1.0,1.0),(0.73,0.46,1.0,1.0),(0.73,0.46,1.0,1.0)]
c={"mediaId":6937,"level":"B","keyWord":"chains","defaultVoice":"female",
"taps":[{"phrase":"to hold an iron shackle","target":"the woman in black","voice":"female","keys":K(B)},
{"phrase":"to punch the air","target":"the man in the beanie","voice":"male","keys":K(M)},
{"phrase":"to unfold a foil blanket","target":"the woman in the red jacket","voice":"female","keys":K(R)}],
"stillS":0.2,
"nouns":[{"word":"a street lamp","x":0.12,"y":0.14,"voice":"female"},{"word":"the moon","x":0.54,"y":0.11,"voice":"female"},{"word":"boats","x":0.84,"y":0.33,"voice":"female"},{"word":"chains","x":0.57,"y":0.86,"voice":"female"}],
"question":"What is the woman in black doing?","answer":["She","is","holding","an","iron","shackle."],"answerVoice":"female",
"notes":"The beanie man punches the air only 0.2-1.7 s, then stands. At 2.7-3.7 s the foil blanket reaches left into the chain/shackle area: split at x 0.72/0.73 so the left edge of the foil falls in the woman-in-black box. Red-jacket box also covers the top-hat man behind her (not a target)."}
json.dump(c,open('content/6937.json','w'),ensure_ascii=False,indent=1)
