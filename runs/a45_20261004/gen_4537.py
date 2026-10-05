import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
w={0.0:(0.05,0.27,0.83,0.58),0.5:(0.05,0.25,0.87,0.60),1.0:(0,0.25,0.88,0.72),1.5:(0,0.25,0.90,0.72),2.0:(0,0.23,0.88,0.68),
2.5:(0.09,0.14,0.79,0.76),3.0:(0.09,0.21,0.69,0.79),3.5:(0.18,0.23,0.50,0.68),4.0:(0.11,0.36,0.57,0.46),4.5:(0.12,0.38,0.58,0.42),
5.0:(0.31,0.36,0.47,0.52),5.5:(0.07,0.24,0.55,0.54),6.0:(0.09,0.21,0.63,0.50),6.5:(0,0.03,0.72,0.51),7.0:(0,0.03,0.71,0.70),
11.0:(0.11,0.36,0.89,0.64),11.5:(0.14,0.38,0.86,0.62),12.0:(0.11,0.37,0.89,0.63)}
k=keys(w)
c={"mediaId":4537,"level":"B","keyWord":"clear","defaultVoice":"female",
"taps":[
 {"phrase":"to wipe a wooden shelf","target":"the woman","voice":"female","keys":k},
 {"phrase":"to pick up scattered clothes","target":"the woman","voice":"female","keys":k},
 {"phrase":"to collapse onto the sofa","target":"the woman","voice":"female","keys":k}],
"stillS":10.0,
"nouns":[{"word":"an air conditioner","x":0.35,"y":0.16,"voice":"female"},{"word":"a sofa","x":0.20,"y":0.46,"voice":"female"},
 {"word":"a coffee table","x":0.60,"y":0.58,"voice":"female"},{"word":"a rug","x":0.48,"y":0.76,"voice":"female"}],
"question":"What is she clearing off the floor?",
"answer":["She","is","clearing","scattered","clothes","off","the","floor."],
"answerVoice":"female",
"notes":"Only one person, so all three phrases share the woman (no thing in the clip does anything). Key word 'clear' (verb) is in the question and answer. She picks clothes off the floor at 3.5-5.0 s; she is already lying on the sofa when the last shot starts (11.0 s), so 'to collapse onto the sofa' shows as the result rather than the fall itself. Woman is off 7.5-10.5 s (empty room)."}
json.dump(c,open("content/4537.json","w"),indent=1)
