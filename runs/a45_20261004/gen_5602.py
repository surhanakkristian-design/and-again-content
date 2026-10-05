import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(f): return [dict(t=t,**dict(zip("xywh",f(t)))) for t in T]
man=lambda t:(0.15,0.21,0.81,0.48) if t<1.5 else (0.26,0.21,0.70,0.48)
lamp=lambda t:(0.22,0.03,0.32,0.18)
def pup(t):
    if t<1.0: return (0.05,0.80,0.48,0.17)
    if t<2.0: return (0.05,0.81,0.48,0.18)
    if t<3.0: return (0.05,0.85,0.48,0.15)
    return (0.05,0.86,0.48,0.14)
d={"mediaId":5602,"level":"B","keyWord":"balancing","defaultVoice":"male",
"taps":[
 {"phrase":"to sprinkle flour into a pan","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to doze under the counter","target":"the puppy","voice":"male","keys":keys(pup)},
 {"phrase":"to dangle from the ceiling","target":"the lamp","voice":"male","keys":keys(lamp)}],
"stillS":2.2,
"nouns":[{"word":"a brass lamp","x":0.38,"y":0.13,"voice":"male"},
 {"word":"loaves","x":0.45,"y":0.26,"voice":"male"},
 {"word":"an apron","x":0.72,"y":0.53,"voice":"male"},
 {"word":"a puppy","x":0.28,"y":0.92,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","sprinkling","flour","into","a","pan."],
"answerVoice":"male",
"notes":"Man sprinkles flour only until ~1.7 s; then watches the pans. Lamp box ends at y 0.21 where the man's head starts (touching, not overlapping). Balance not a tap target; it sits inside the man's box."}
json.dump(d,open("content/5602.json","w"),indent=1)
