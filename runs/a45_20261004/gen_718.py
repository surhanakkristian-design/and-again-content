import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={0.0:(0,0.37,0.50,0.63),0.5:(0,0.42,0.33,0.58),1.0:(0,0.58,0.45,0.37),1.5:(0,0.63,0.24,0.18),
3.0:(0.38,0.50,0.26,0.44),3.5:(0.36,0.52,0.30,0.42),4.0:(0.36,0.50,0.30,0.34),4.5:(0.36,0.50,0.30,0.34),5.0:(0.35,0.50,0.30,0.43),
5.5:(0.30,0.53,0.24,0.45),6.0:(0.33,0.54,0.27,0.40),6.5:(0.36,0.54,0.26,0.38),7.0:(0.36,0.54,0.26,0.44),7.5:(0.36,0.54,0.26,0.44),
8.0:(0.36,0.54,0.26,0.34),8.5:(0.36,0.54,0.26,0.34),9.0:(0.36,0.60,0.18,0.22),9.5:(0.36,0.60,0.18,0.18),10.0:(0.36,0.58,0.18,0.16)}
B={0.0:(0.50,0.03,0.50,0.43),0.5:(0.33,0.02,0.67,0.50),1.0:(0,0.05,1.0,0.53),1.5:(0,0.03,1.0,0.57),2.0:(0,0,1.0,0.75),2.5:(0,0,1.0,0.78),
3.0:(0,0.13,1.0,0.36),3.5:(0,0.13,1.0,0.36),4.0:(0,0.13,1.0,0.36),4.5:(0,0.13,1.0,0.36),5.0:(0,0.16,1.0,0.33),
5.5:(0.28,0.05,0.72,0.40),6.0:(0.20,0.04,0.80,0.40),6.5:(0.08,0.02,0.92,0.42),7.0:(0,0.02,1.0,0.41),7.5:(0,0,1.0,0.43),
8.0:(0.28,0,0.72,0.44),8.5:(0.23,0,0.77,0.44),9.0:(0,0.02,1.0,0.44),9.5:(0,0.10,1.0,0.36),10.0:(0,0.17,1.0,0.27)}
S={3.0:(0.72,0.50,0.20,0.14),3.5:(0.72,0.50,0.20,0.14),4.0:(0.72,0.49,0.20,0.14),4.5:(0.72,0.49,0.20,0.14),5.0:(0.70,0.50,0.20,0.14),
9.0:(0.48,0.46,0.20,0.14),9.5:(0.47,0.46,0.20,0.14),10.0:(0.47,0.44,0.20,0.14)}
c={"mediaId":718,"level":"A","keyWord":"south","defaultVoice":"female",
"taps":[
{"phrase":"to point at the birds","target":"the woman in the green coat","voice":"female","keys":keys(W)},
{"phrase":"to fly across the sky","target":"the birds","voice":"female","keys":keys(B)},
{"phrase":"to shine over the field","target":"the sun","voice":"female","keys":keys(S)}],
"stillS":4.5,
"nouns":[{"word":"the sky","x":0.65,"y":0.10,"voice":"female"},{"word":"birds","x":0.30,"y":0.28,"voice":"female"},
{"word":"the sun","x":0.80,"y":0.55,"voice":"female"},{"word":"a wall","x":0.65,"y":0.86,"voice":"female"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","at","the","birds."],"answerVoice":"female",
"notes":"Woman points only at 0.0-1.5 s (later she plants a post and walks); at 0.0-0.5 her outstretched arm is left out of her box because the birds line crosses it. From 1.0-1.5 only her arm is in frame. At 9.0-10.0 she is the middle figure seen from behind (lighter green coat). Key word 'south' is not a visible noun. Sun is a thing target (visible 3.0-5.0 and 9.0-10.0)."}
json.dump(c,open("content/718.json","w"),indent=1)
