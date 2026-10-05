import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
woman={0.0:(0.05,0,0.85,0.8),0.5:(0.05,0,0.95,0.8),1.0:(0,0,0.88,0.88),1.5:(0.05,0,0.82,0.88),2.0:(0,0,0.8,0.78),
2.5:(0,0,0.2,0.76),3.0:(0,0,0.27,0.75),3.5:(0,0,0.3,0.75),4.0:(0,0,0.37,0.76),4.5:(0,0,0.45,0.72),5.0:(0,0,0.45,0.76),
5.5:(0,0,0.48,0.92),6.0:(0,0.42,0.67,0.22),6.5:(0,0.48,0.65,0.2),7.0:(0,0,0.33,0.83),7.5:(0,0,0.37,0.83),8.0:(0,0,0.42,0.76),
8.5:(0,0,0.47,0.77),9.0:(0,0,0.47,0.9)}
man={2.0:(0.82,0.42,0.18,0.33),2.5:(0.25,0,0.75,0.76),3.0:(0.3,0,0.62,0.75),3.5:(0.37,0,0.63,0.75),4.0:(0.45,0,0.55,0.77),
4.5:(0.47,0,0.53,0.78),5.0:(0.47,0,0.53,0.92),5.5:(0.5,0,0.5,0.93),6.0:(0.16,0.22,0.5,0.19),6.5:(0.17,0.3,0.45,0.17),
7.0:(0.37,0,0.63,0.86),7.5:(0.39,0,0.61,0.86),8.0:(0.44,0,0.56,0.74),8.5:(0.48,0,0.52,0.76),9.0:(0.48,0,0.5,0.93),
9.5:(0,0.1,0.4,0.85),10.0:(0.05,0.1,0.46,0.75)}
bird={9.5:(0.76,0.33,0.24,0.14),10.0:(0.78,0.32,0.2,0.14)}
c={"mediaId":635,"level":"A","keyWord":"sandals","defaultVoice":"female",
"taps":[{"phrase":"to put on her sandals","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to wear brown sandals","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to stand on a bench","target":"the bird","voice":"female","keys":keys(bird)}],
"stillS":10.0,
"nouns":[{"word":"the sky","x":0.55,"y":0.1,"voice":"female"},{"word":"a bird","x":0.87,"y":0.385,"voice":"female"},
{"word":"a bench","x":0.8,"y":0.48,"voice":"female"},{"word":"sandals","x":0.3,"y":0.78,"voice":"female"}],
"question":"What are they wearing on their feet?","answer":["They","are","wearing","sandals."],"answerVoice":"female",
"notes":"Man's phrase is a state (he has no action of his own; both walk). 6.0-6.5 s fountain shot: brown sandals = man (back), tan sandals = woman (front); her dress and their legs cross there, so the boxes hold mainly the feet. 9.5-10.0 s: the woman is only a sliver at the left edge -> off. Bird only at 9.5-10.0 s (small, standing on the bench). 'a bird' and 'a bench' pills are close (0.095 apart in y)."}
json.dump(c,open('content/635.json','w'),ensure_ascii=False,indent=1)
