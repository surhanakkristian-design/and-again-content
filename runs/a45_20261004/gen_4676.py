import json
T=[i*0.5 for i in range(25)]
two={0.0:(0.04,0.35,0.76,0.47),0.5:(0.04,0.35,0.86,0.52),1.0:(0.0,0.34,0.9,0.56),1.5:(0,0.3,1,0.67),2.0:(0,0.29,1,0.71),2.5:(0,0.32,1,0.68)}
man={3.0:(0,0.23,0.55,0.77),3.5:(0,0.14,0.68,0.86),4.0:(0.02,0.12,0.70,0.88),4.5:(0.05,0.08,0.82,0.92),5.0:(0.05,0.08,0.65,0.92),5.5:(0,0.08,0.97,0.92),6.0:(0,0.11,0.88,0.89),6.5:(0,0.1,0.95,0.9),7.0:(0,0.19,0.68,0.81),7.5:(0.05,0.15,0.83,0.85),8.0:(0.1,0,0.7,1),8.5:(0.04,0.02,0.82,0.98),9.0:(0,0.15,0.72,0.85),9.5:(0,0.15,0.70,0.85),10.0:(0,0.15,0.70,0.85),10.5:(0,0.16,0.74,0.84),11.0:(0,0.16,0.88,0.84),11.5:(0,0.16,0.95,0.84),12.0:(0,0.22,0.75,0.78)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c={"mediaId":4676,"level":"A","keyWord":"tradition","defaultVoice":"male",
"taps":[
 {"phrase":"to carry cheese together","target":"the two men","voice":"male","keys":keys(two)},
 {"phrase":"to lift a big cheese","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to throw a white hat","target":"the man","voice":"male","keys":keys(man)}],
"stillS":8.5,
"nouns":[{"word":"a hat","x":0.42,"y":0.31,"voice":"male"},{"word":"cheese","x":0.78,"y":0.82,"voice":"male"},{"word":"a flag","x":0.88,"y":0.17,"voice":"male"}],
"question":"What is the man lifting?",
"answer":["He","is","lifting","a","big","cheese."],
"answerVoice":"male",
"notes":"Key word 'tradition' is abstract, not used as a noun. Shot 1 (0-2.5 s) = two carriers ('the two men'); from 3.0 s one young carrier alone ('the man'), probably one of the two. The hat is thrown only at 11.5-12.0 s. At 9.0-10.5 a second person's arms come in from the right (high five), left outside the man's box. 'cheese' pill sits on the front stack; the lifted wheel is cheese too."}
json.dump(c,open("content/4676.json","w"),indent=1)
