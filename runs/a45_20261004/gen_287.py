import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
woman={0.0:(0.03,0.42,0.72,0.58),0.5:(0.0,0.42,0.70,0.58),1.0:(0.02,0.38,0.96,0.62),1.5:(0.0,0.40,0.76,0.60),2.0:(0.0,0.42,0.70,0.58),
 2.5:(0.81,0.42,0.19,0.58),3.0:(0.80,0.43,0.20,0.57),3.5:(0.78,0.44,0.22,0.56),4.0:(0.74,0.43,0.26,0.57),4.5:(0.78,0.42,0.22,0.58),5.0:(0.71,0.43,0.29,0.57),5.5:(0.56,0.61,0.18,0.16)}
red={2.5:(0.38,0.41,0.26,0.38),3.0:(0.36,0.41,0.25,0.36),3.5:(0.34,0.41,0.25,0.36),4.0:(0.34,0.41,0.18,0.34),4.5:(0.34,0.43,0.14,0.30),5.0:(0.34,0.44,0.13,0.26),5.5:(0.29,0.61,0.18,0.16)}
green={2.5:(0.65,0.40,0.16,0.40),3.0:(0.62,0.39,0.18,0.45),3.5:(0.60,0.39,0.18,0.61),4.0:(0.52,0.40,0.22,0.55),4.5:(0.48,0.41,0.30,0.50),5.0:(0.47,0.44,0.24,0.56),5.5:(0.47,0.61,0.09,0.16)}
for t in T:
    if t>=6.0:
        woman[t]=(0.56,0.60,0.18,0.16); red[t]=(0.29,0.60,0.18,0.16); green[t]=(0.47,0.60,0.09,0.16)
c={"mediaId":287,"level":"A","keyWord":"far","defaultVoice":"female",
"taps":[
 {"phrase":"to point at a village","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to look back at her","target":"the man in green","voice":"male","keys":K(green)},
 {"phrase":"to wear a red jacket","target":"the person in red","voice":"female","keys":K(red)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.20,"voice":"female"},{"word":"a village","x":0.52,"y":0.53,"voice":"female"},{"word":"grass","x":0.50,"y":0.88,"voice":"female"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","at","a","village","far away."],
"answerVoice":"female",
"notes":"0.0-2.0 s: the two companions are almost fully hidden behind the woman and cannot be told apart, so their boxes are off there. Wide shots (5.5 s on): the three stand shoulder to shoulder, the middle man's box is only 0.09 wide to avoid overlap. The person in red is only seen from behind (gender unclear) -> state phrase and default voice. 'far away.' kept as one chip."}
json.dump(c,open("content/287.json","w"),indent=1)
