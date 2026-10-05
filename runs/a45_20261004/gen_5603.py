import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(f):
    out=[]
    for t in T:
        b=f(t)
        out.append({"t":t,"off":True} if b is None else dict(t=t,**dict(zip("xywh",b))))
    return out
def man(t):
    if t<2.0: return (0.0,0.22,0.32,0.78)
    if t<2.5: return (0.0,0.23,0.37,0.77)
    if t<3.0: return (0.10,0.24,0.82,0.76)
    if t<3.5: return (0.13,0.24,0.82,0.76)
    return (0.12,0.24,0.82,0.76)
def wom(t):
    if t<0.5: return (0.32,0.37,0.32,0.31)
    if t<2.0: return (0.32,0.37,0.37,0.32)
    if t<2.5: return (0.37,0.39,0.25,0.29)
    return None
d={"mediaId":5603,"level":"A","keyWord":"banking","defaultVoice":"male",
"taps":[
 {"phrase":"to put money in a drawer","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to stand behind the man","target":"the woman","voice":"female","keys":keys(wom)},
 {"phrase":"to push the drawer back","target":"the man","voice":"male","keys":keys(man)}],
"stillS":0.2,
"nouns":[{"word":"a light","x":0.36,"y":0.19,"voice":"male"},
 {"word":"a woman","x":0.44,"y":0.55,"voice":"female"},
 {"word":"money","x":0.58,"y":0.76,"voice":"male"},
 {"word":"a drawer","x":0.70,"y":0.88,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","putting","money","in","a","drawer."],
"answerVoice":"male",
"notes":"Man and woman overlap heavily; split: man box = his left part (torso/head) up to x~0.32-0.37 while she is visible, woman box = her head and upper body right of that line, above his arms. Woman is hidden behind the man from 2.7 s (off). Man's hands/money lie outside his box 0.2-2.2 s. Man also turns a key later, so the woman got 'to stand behind the man' rather than a key phrase."}
json.dump(d,open("content/5603.json","w"),indent=1)
