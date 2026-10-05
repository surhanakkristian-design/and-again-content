import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
blue={0.0:(0.43,0.24,0.47,0.76),0.5:(0.32,0.23,0.48,0.77),1.0:(0.30,0.25,0.44,0.75),1.5:(0.30,0.26,0.44,0.74),2.0:(0.28,0.26,0.40,0.72),
2.5:(0.07,0.12,0.83,0.88),3.0:(0.02,0.12,0.94,0.88),3.5:(0.17,0.10,0.83,0.90),4.0:(0.22,0.06,0.78,0.94),4.5:(0.20,0.15,0.80,0.85),
5.0:(0.10,0.12,0.87,0.88),5.5:(0.20,0.17,0.78,0.83),6.0:(0.23,0.12,0.58,0.88),6.5:(0.13,0.05,0.69,0.95),7.0:(0.08,0.22,0.76,0.78),
7.5:(0.11,0.35,0.77,0.65),8.0:(0.13,0.27,0.80,0.73),8.5:(0.13,0.20,0.77,0.77),9.0:(0.14,0.18,0.72,0.82),9.5:(0.13,0.18,0.75,0.82),10.0:(0.15,0.17,0.76,0.83)}
yellow={0.0:(0.18,0.30,0.25,0.39),0.5:(0.04,0.29,0.28,0.39),1.0:(0.0,0.30,0.30,0.50),1.5:(0.0,0.30,0.25,0.51),2.0:(0.0,0.29,0.22,0.40),
8.0:(0.0,0.48,0.13,0.18),8.5:(0.0,0.03,0.13,0.62),9.0:(0.0,0.05,0.14,0.50),9.5:(0.0,0.08,0.13,0.70),10.0:(0.0,0.08,0.15,0.64)}
c={"mediaId":289,"level":"B","keyWord":"fear","defaultVoice":"female",
"taps":[
 {"phrase":"to clutch her chest","target":"the woman in blue","voice":"female","keys":K(blue)},
 {"phrase":"to cling to a post","target":"the woman in blue","voice":"female","keys":K(blue)},
 {"phrase":"to approach from behind","target":"the woman in yellow","voice":"female","keys":K(yellow)}],
"stillS":0.0,
"nouns":[{"word":"peaks","x":0.52,"y":0.23,"voice":"female"},{"word":"a railing","x":0.86,"y":0.62,"voice":"female"},{"word":"a reflection","x":0.33,"y":0.86,"voice":"female"}],
"question":"What is the woman in blue doing?",
"answer":["She","is","clinging","to","a","post","in fear."],
"answerVoice":"female",
"notes":"Only two people. The woman in yellow is out of frame 2.5-7.5 s; at 8.0 s only her shoe is visible (small box), at 8.5-10.0 s she is cut by the left edge and touches the woman in blue, split by a vertical line (the blue box loses a strip of her left side at 9.0 s). Tiny slivers of yellow at the picture edge at 4.0-5.5 s are ignored (off). 'to crouch' avoided because the woman in yellow also bends down at the end. 'in fear.' kept as one chip. 'peaks' = the mountain peaks in the background."}
json.dump(c,open("content/289.json","w"),indent=1)
