import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
G={0.0:(0.36,0.38,0.64,0.50),0.5:(0.38,0.38,0.62,0.50),1.0:(0.50,0.40,0.50,0.52),1.5:(0.52,0.50,0.48,0.42),2.0:(0.43,0.25,0.57,0.55),
2.5:(0.43,0.18,0.57,0.80),3.0:(0,0.45,0.30,0.55),3.5:(0.02,0.22,0.48,0.78),4.0:(0.40,0.18,0.60,0.82),4.5:(0,0.26,0.45,0.74),
5.0:(0,0.20,0.50,0.80),5.5:(0,0.22,0.50,0.78),6.0:(0,0.24,0.50,0.76),6.5:(0,0.28,0.35,0.72),7.0:(0,0.30,0.36,0.70),7.5:(0,0.33,0.37,0.67),
8.0:(0,0.38,0.36,0.62),8.5:(0,0.48,0.36,0.52),9.0:(0,0.63,0.28,0.37)}
B={0.5:(0.08,0.35,0.20,0.42),1.0:(0.08,0.33,0.40,0.56),1.5:(0,0.26,0.50,0.63),2.0:(0.02,0.25,0.40,0.55),2.5:(0.08,0.18,0.33,0.82),
3.0:(0.32,0.20,0.56,0.80),3.5:(0.52,0.22,0.48,0.78),4.0:(0.21,0.45,0.18,0.55),4.5:(0.47,0.24,0.53,0.76),5.0:(0.51,0.20,0.49,0.80),
5.5:(0.51,0.22,0.49,0.78),6.0:(0.51,0.22,0.49,0.78),6.5:(0.62,0.28,0.38,0.72),7.0:(0.62,0.30,0.38,0.70),7.5:(0.61,0.33,0.39,0.67),
8.0:(0.62,0.38,0.38,0.62),8.5:(0.62,0.48,0.38,0.52),9.0:(0.58,0.63,0.42,0.37)}
W={4.0:(0,0.28,0.20,0.72),6.5:(0.36,0.26,0.25,0.74),7.0:(0.37,0.26,0.24,0.74),7.5:(0.38,0.27,0.22,0.73),8.0:(0.37,0.30,0.24,0.70),
8.5:(0.37,0.38,0.24,0.62),9.0:(0.29,0.60,0.28,0.40),9.5:(0.10,0.70,0.50,0.30)}
c={"mediaId":684,"level":"A","keyWord":"sister","defaultVoice":"female",
"taps":[
{"phrase":"to sit at the table","target":"the girl in green","voice":"female","keys":keys(G)},
{"phrase":"to open the door","target":"the girl in blue","voice":"female","keys":keys(B)},
{"phrase":"to hug the two girls","target":"the old woman","voice":"female","keys":keys(W)}],
"stillS":0.0,
"nouns":[{"word":"a door","x":0.30,"y":0.28,"voice":"female"},{"word":"a girl","x":0.75,"y":0.50,"voice":"female"},
{"word":"a spoon","x":0.45,"y":0.68,"voice":"female"},{"word":"a fork","x":0.33,"y":0.90,"voice":"female"}],
"question":"What are the two sisters doing?",
"answer":["The","two","sisters","are","hugging","each","other."],
"answerVoice":"female",
"notes":"Hug shots 2.0-4.5: the two girls overlap heavily, boxes are split along the line between them (rough at 3.0 and 4.0, where one girl is seen from behind). The old woman's arms reach into the girls' boxes at 7.0-8.5. At 9.5 the faces are faded out; only the old woman is boxed. The people in the wall portrait are not boxed. Key word 'sister' is not a labelable noun on the still (one girl only) - it is used in the question/answer instead."}
json.dump(c,open("content/684.json","w"),indent=1)
