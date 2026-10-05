import json
T=[round(i*0.5,1) for i in range(25)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
W={0.0:(0.24,0.11,0.46,0.89),0.5:(0.27,0.06,0.43,0.94),1.0:(0.27,0.12,0.40,0.88),1.5:(0.25,0.08,0.45,0.92),
 2.0:(0.12,0.13,0.76,0.87),2.5:(0.04,0.33,0.96,0.67),3.0:(0.0,0.39,0.79,0.61),3.5:(0.0,0.40,0.70,0.60),
 4.0:(0.0,0.44,0.64,0.50),4.5:(0.0,0.44,0.58,0.48),5.0:(0.0,0.41,0.53,0.48),5.5:(0.0,0.41,0.54,0.48),
 6.0:(0.0,0.39,0.51,0.43),6.5:(0.0,0.39,0.51,0.43),7.0:(0.0,0.38,0.48,0.41),7.5:(0.0,0.38,0.47,0.42),
 8.0:(0.0,0.38,0.48,0.41),8.5:(0.0,0.38,0.51,0.41),9.0:(0.0,0.28,0.57,0.52),9.5:(0.0,0.15,0.59,0.69),
 10.0:(0.0,0.15,0.60,0.72),10.5:(0.02,0.08,0.52,0.81),11.0:(0.10,0.10,0.44,0.81),11.5:(0.0,0.22,0.60,0.68),12.0:(0.0,0.25,0.70,0.64)}
C={3.0:(0.79,0.80,0.21,0.20),3.5:(0.70,0.69,0.30,0.31),4.0:(0.64,0.66,0.36,0.31),4.5:(0.58,0.63,0.42,0.30),
 5.0:(0.53,0.57,0.39,0.33),5.5:(0.54,0.54,0.42,0.34),6.0:(0.51,0.52,0.46,0.33),6.5:(0.51,0.51,0.48,0.34),
 7.0:(0.48,0.50,0.50,0.34),7.5:(0.47,0.50,0.53,0.34),8.0:(0.48,0.52,0.52,0.31),8.5:(0.51,0.53,0.49,0.30),
 9.0:(0.57,0.57,0.32,0.28),9.5:(0.59,0.59,0.33,0.29),10.0:(0.61,0.63,0.31,0.27),10.5:(0.54,0.66,0.40,0.26),
 11.0:(0.55,0.67,0.38,0.28),11.5:(0.61,0.68,0.32,0.27),12.0:(0.71,0.68,0.25,0.26)}
c={"mediaId":5355,"level":"B","keyWord":"trainer","defaultVoice":"female",
 "taps":[
  {"phrase":"to lead a morning workout","target":"the trainer","voice":"female","keys":keys(W)},
  {"phrase":"to arch its back","target":"the ginger cat","voice":"female","keys":keys(C)},
  {"phrase":"to sit calmly at her feet","target":"the ginger cat","voice":"female","keys":keys(C)}],
 "stillS":12.0,
 "nouns":[{"word":"a tree trunk","x":0.58,"y":0.15,"voice":"female"},{"word":"a trainer","x":0.30,"y":0.42,"voice":"female"},
          {"word":"a ginger cat","x":0.82,"y":0.81,"voice":"female"},{"word":"a stone ledge","x":0.35,"y":0.94,"voice":"female"}],
 "question":"What is the trainer doing?",
 "answer":["She","is","leading","a","morning","workout."],
 "answerVoice":"female",
 "notes":"Cat only a sliver in the bottom-right corner at 2.5 s (set off). Trainer and cat touch at many frames (her hands/shoe, its tail); boxes split vertically between them, so the trainer's outstretched arm tip is clipped at 3.5, 9.5-12.0. Cat sits (not at her feet) at 4.0 too; 'sit calmly at her feet' refers to 10.0-12.0. Background group also bends and raises arms, so no group-shared action used."}
json.dump(c,open('content/5355.json','w'),indent=1)
