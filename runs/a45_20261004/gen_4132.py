import json
T=[i*0.5 for i in range(21)]
def keys(f):
    out=[]
    for t in T:
        b=f(t)
        out.append({"t":t,"off":True} if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]))
    return out
def cat(t):
    if t<=2.5: return (0.33,0.07,0.47,0.24)
    if t<=7.0: return (0.70,0.22,0.30,0.66)
    return (0.74,0.16,0.26,0.48)
def lion(t):
    if t<=2.5: return (0.05,0.31,0.90,0.69)
    if t<=7.0: return (0.0,0.17,0.69,0.78)
    return (0.0,0.15,0.74,0.85)
d={"mediaId":4132,"level":"A","keyWord":"brush","defaultVoice":"female",
"taps":[
 {"phrase":"to brush the wet hair","target":"the cat","voice":"female","keys":keys(cat)},
 {"phrase":"to wash the lion's head","target":"the cat","voice":"female","keys":keys(cat)},
 {"phrase":"to sit in a black chair","target":"the lion","voice":"female","keys":keys(lion)}],
"stillS":5.0,
"nouns":[{"word":"a lion","x":0.25,"y":0.33,"voice":"female"},
 {"word":"a cat","x":0.86,"y":0.37,"voice":"female"},
 {"word":"a brush","x":0.58,"y":0.47,"voice":"female"},
 {"word":"a sink","x":0.60,"y":0.88,"voice":"female"}],
"question":"What is the cat doing?",
"answer":["The","cat","is","brushing","the","lion's","hair."],
"answerVoice":"female",
"notes":"Three shots (cuts at 3.0 and 7.5). Cat and lion touch in every shot; boxes split along the line between them (y 0.31 in shot 1, x 0.70 in shot 2, x 0.74 in shot 3), so the lion's right paw in shot 3 lies partly under the cat's box column. The cat sits on a stool in shot 3, not in a black chair. Key word is the verb; the noun 'a brush' is the wooden hairbrush at 5.0 s."}
json.dump(d,open("content/4132.json","w"),indent=1,ensure_ascii=False)
