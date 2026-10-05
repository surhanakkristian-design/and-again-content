import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
man={0.0:(0.33,0.18,0.67,0.56),0.5:(0.33,0.17,0.67,0.57),1.0:(0.30,0.14,0.70,0.56),1.5:(0.30,0.14,0.70,0.56),2.0:(0.28,0.10,0.72,0.62),
 2.5:(0,0.30,0.73,0.70),3.0:(0,0.35,0.70,0.65),3.5:(0,0.34,0.82,0.66),4.0:(0,0.37,0.80,0.63),4.5:(0,0.35,0.74,0.65),
 5.0:(0,0.38,0.66,0.62),5.5:(0,0.43,0.70,0.57),6.0:(0,0.47,0.68,0.53),6.5:(0,0.50,0.68,0.50),7.0:(0,0.50,1.0,0.50),
 7.5:(0,0.49,0.97,0.51),8.0:(0,0.49,1.0,0.51),8.5:(0,0.48,1.0,0.52),9.0:(0,0.52,1.0,0.48)}
sk={4.5:(0.33,0,0.47,0.35),5.0:(0.25,0,0.55,0.38),5.5:(0.30,0,0.47,0.43),6.0:(0.30,0,0.40,0.47),6.5:(0.30,0,0.45,0.50),
 7.0:(0.32,0,0.40,0.50),7.5:(0.35,0,0.38,0.49),8.0:(0.33,0,0.40,0.49),8.5:(0.35,0,0.38,0.48),9.0:(0.35,0,0.38,0.52)}
c={"mediaId":5095,"level":"B","keyWord":"awe","defaultVoice":"male",
"taps":[
 {"phrase":"to sketch the old coins","target":"the young man","voice":"male","keys":K(man)},
 {"phrase":"to gaze up in awe","target":"the young man","voice":"male","keys":K(man)},
 {"phrase":"to hang from the glass roof","target":"the skeleton","voice":"male","keys":K(sk)}],
"stillS":8.0,
"nouns":[{"word":"a glass roof","x":0.80,"y":0.13,"voice":"male"},
 {"word":"a skeleton","x":0.53,"y":0.32,"voice":"male"},
 {"word":"a corduroy shirt","x":0.30,"y":0.74,"voice":"male"},
 {"word":"a notebook","x":0.88,"y":0.80,"voice":"male"}],
"question":"What is the man staring at?",
"answer":["He","is","staring","at","a","huge","skeleton."],"answerVoice":"male",
"notes":"Only one person acts (selfie stick); two phrases on him (sketching 0-2.0, gazing up open-mouthed 2.5-9.0). Skeleton visible 4.5-9.0; its legs/tail hang down beside and behind his head, so the boxes are split horizontally just above his head: the lower part of the skeleton (beside his face) falls into the man's box. Schoolchildren pass at the right edge 5.0-9.0, small and changing, not used. 'to gaze up in awe' carries the key word; at 8.5 one schoolgirl also glances up briefly."}
json.dump(c,open('content/5095.json','w'),indent=1)
