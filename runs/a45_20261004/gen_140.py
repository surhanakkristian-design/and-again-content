import json
T=[i*0.5 for i in range(17)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0,0.06,0.40,0.50),0.5:(0,0.10,0.40,0.46),2.5:(0,0.10,0.20,0.40),3.0:(0,0.19,0.48,0.51),3.5:(0,0.22,0.51,0.52),
4.0:(0,0.17,0.51,0.42),4.5:(0,0.07,0.56,0.59),5.0:(0,0.08,0.56,0.57),5.5:(0,0.08,0.56,0.57),6.0:(0,0.12,0.52,0.50),
6.5:(0,0.12,0.52,0.50),7.0:(0,0.16,0.51,0.50),7.5:(0,0.22,0.52,0.42),8.0:(0,0.22,0.53,0.43)}
wom={0.0:(0.60,0.02,0.40,0.54),0.5:(0.60,0.03,0.40,0.53),2.5:(0.64,0.11,0.36,0.45),3.0:(0.49,0.13,0.51,0.57),3.5:(0.52,0.11,0.48,0.63),
4.0:(0.52,0.07,0.48,0.54),4.5:(0.57,0.12,0.43,0.63),5.0:(0.57,0.08,0.43,0.70),5.5:(0.57,0.08,0.43,0.70),6.0:(0.53,0.11,0.47,0.58),
6.5:(0.53,0.11,0.47,0.60),7.0:(0.52,0.16,0.48,0.67),7.5:(0.53,0.16,0.47,0.54),8.0:(0.53,0.19,0.47,0.49)}
car={0.0:(0.10,0.56,0.76,0.32),0.5:(0.10,0.56,0.76,0.32),1.0:(0,0.38,1,0.52),1.5:(0,0.36,1,0.64),2.0:(0,0.30,1,0.70),
2.5:(0,0.57,1,0.43),3.0:(0,0.71,1,0.29),3.5:(0,0.75,1,0.25),4.0:(0,0.62,1,0.38),4.5:(0,0.67,0.56,0.18),5.0:(0,0.66,0.56,0.17),
5.5:(0,0.66,0.56,0.17),6.0:(0,0.70,1,0.14),6.5:(0,0.72,1,0.14),7.0:(0,0.67,0.51,0.16),7.5:(0,0.71,1,0.14),8.0:(0,0.69,1,0.15)}
c={"mediaId":140,"level":"A","keyWord":"carpet","defaultVoice":"female",
"taps":[{"phrase":"to cover the floor","target":"the carpet","voice":"female","keys":keys(car)},
{"phrase":"to wear a yellow sweater","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to wear a blue sweater","target":"the woman","voice":"female","keys":keys(wom)}],
"stillS":8.0,
"nouns":[{"word":"a carpet","x":0.50,"y":0.74,"voice":"female"},{"word":"the floor","x":0.50,"y":0.90,"voice":"female"},
{"word":"a man","x":0.22,"y":0.44,"voice":"male"},{"word":"a woman","x":0.76,"y":0.44,"voice":"female"}],
"question":"What are they lying on?","answer":["They","are","lying","on","a","green","carpet."],"answerVoice":"female",
"notes":"Man and woman do everything together (push, crawl, lie, high-five), so their two phrases are states (clothes). The woman's hoodie is turquoise (blue-green): 'blue sweater' is the weak spot; the garments are hoodies, 'sweater' chosen for level A. Carpet box = the free carpet part beside/below the people (they lie on it)."}
json.dump(c,open("content/140.json","w"),indent=1)
