import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True}); continue
        x,y,w,h=b; w=min(w,1-x); h=min(h,1-y)
        out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
man=keys({0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0.37,0.02,0.63,0.98),2.0:(0.66,0.1,0.34,0.9),2.5:(0.3,0.1,0.7,0.9),
 3.0:(0,0,1,1),3.5:(0,0,1,1),4.0:(0,0,1,1),6.5:(0.68,0.29,0.31,0.58),7.0:(0.5,0.3,0.48,0.7),7.5:(0.6,0.52,0.4,0.48),
 8.0:(0.6,0.67,0.4,0.33),8.5:(0.66,0.73,0.34,0.27),9.0:(0.7,0.76,0.3,0.24)})
tyre=keys({5.0:(0,0.02,0.18,0.48),5.5:(0,0,0.65,0.52),6.0:(0.35,0,0.65,0.5),6.5:(0,0.1,0.68,0.82),7.0:(0,0.27,0.5,0.73),
 7.5:(0,0.5,0.6,0.5),8.0:(0,0.64,0.6,0.36),8.5:(0,0.7,0.66,0.3),9.0:(0,0.72,0.7,0.28)})
wheel=keys({7.0:(0,0,1,0.27),7.5:(0,0,1,0.5),8.0:(0,0,1,0.64),8.5:(0,0,1,0.7),9.0:(0,0,1,0.72)})
c={"mediaId":5493,"level":"B","keyWord":"hub","defaultVoice":"male",
"taps":[{"phrase":"to flip a bicycle over","target":"the young man","voice":"male","keys":man},
{"phrase":"to sit on a yellow rim","target":"the tractor tyre","voice":"male","keys":tyre},
{"phrase":"to tower over the tyre","target":"the ferris wheel","voice":"male","keys":wheel}],
"stillS":6.5,
"nouns":[{"word":"a hub","x":0.4,"y":0.51,"voice":"male"},
{"word":"a rim","x":0.42,"y":0.73,"voice":"male"},
{"word":"a tractor tyre","x":0.25,"y":0.87,"voice":"male"},
{"word":"work boots","x":0.8,"y":0.79,"voice":"male"}],
"question":"What is the man staring at?",
"answer":["He","is","staring","at","a","huge","tractor","tyre."],
"answerVoice":"male",
"notes":"Many cuts: 0-1.0 close-up with the scooter wheel (man fills the frame), 1.5-2.5 he flips the blue bike, 3.0-4.0 face behind the bike hub (whole frame), 4.5-6.0 low floor shots (man off; tractor tyre at the left edge 5.0, upper left 5.5, behind the bike wheel 6.0), 6.5 man next to the tractor tyre, 7.0-9.0 ferris wheel above the tyre and the man's back. 'to sit on a yellow rim' is a state (the tyre has no action). Ferris wheel box = everything above the tyre/man."}
json.dump(c,open('/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/content/5493.json','w'),indent=1)
