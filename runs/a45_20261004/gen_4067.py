import json
times=[i*0.5 for i in range(27)]
man={0.0:(0.67,0.40,0.19,0.14),0.5:(0.63,0.40,0.19,0.14),1.0:(0.56,0.40,0.19,0.14),1.5:(0.45,0.40,0.26,0.14),2.0:(0.38,0.53,0.23,0.15)}
def mk(t):
    if t in man: return man[t]
    if t<5.0: return None
    return (0.27,0.64,0.19,0.14)
def keys(f):
    out=[]
    for t in times:
        b=f(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
lake=lambda t:(0.0,0.71,0.61,0.29) if t<5.0 else (0.0,0.78,0.61,0.22)
rock=lambda t:(0.61,0.54,0.39,0.27)
d={"mediaId":4067,"level":"B","keyWord":"mirror","defaultVoice":"male",
"taps":[
 {"phrase":"to dive into the lake","target":"the man","voice":"male","keys":keys(mk)},
 {"phrase":"to mirror the fir trees","target":"the lake","voice":"male","keys":keys(lake)},
 {"phrase":"to jut out over the water","target":"the rock","voice":"male","keys":keys(rock)}],
"stillS":9.0,
"nouns":[{"word":"the sky","x":0.40,"y":0.22,"voice":"male"},{"word":"fir trees","x":0.30,"y":0.65,"voice":"male"},{"word":"ripples","x":0.35,"y":0.77,"voice":"male"},{"word":"a rock","x":0.80,"y":0.60,"voice":"male"}],
"question":"What does the lake mirror?",
"answer":["The","lake","mirrors","the","dark","fir","trees."],
"answerVoice":"male",
"notes":"Person is a black silhouette; read as a man (shorts, short hair), not certain. Man is off 2.5-4.5 s (under water); from 5.0 s only his head shows, box is minimum size. Lake box is cut below the swimmer's box from 5.0 s on (y 0.78) so the two never overlap; the rock box covers only the rock above its waterline. Question is present simple (a state: the lake mirrors) to use the key verb."}
json.dump(d,open("content/4067.json","w"),indent=1)
