import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
W={0.0:(0.30,0.0,0.52,0.54),0.5:(0.36,0.0,0.54,0.57),1.0:(0.16,0.0,0.64,0.69),1.5:(0.22,0.0,0.67,1.0),
 2.0:(0.08,0.0,0.72,1.0),2.5:(0.15,0.11,0.76,0.89),3.0:(0.01,0.16,0.89,0.84)}
H={3.5:(0.07,0.40,0.68,0.60),4.0:(0.15,0.44,0.55,0.56),4.5:(0.15,0.47,0.50,0.53),5.0:(0.14,0.46,0.48,0.54),5.5:(0.18,0.47,0.46,0.53)}
D={6.0:(0.38,0.52,0.48,0.18),6.5:(0.36,0.52,0.48,0.19),7.0:(0.31,0.53,0.51,0.21),7.5:(0.28,0.53,0.58,0.22)}
c={"mediaId":5470,"level":"B","keyWord":"downtown","defaultVoice":"female",
"taps":[{"phrase":"to stride in nude high heels","target":"the woman in the suit","voice":"female","keys":keys(W)},
{"phrase":"to hike up a forest trail","target":"the hiker","voice":"male","keys":keys(H)},
{"phrase":"to trot along on a leash","target":"the golden retriever","voice":"female","keys":keys(D)}],
"stillS":8.0,
"nouns":[{"word":"billboards","x":0.45,"y":0.12,"voice":"female"},{"word":"a traffic light","x":0.80,"y":0.34,"voice":"female"},
{"word":"a zebra crossing","x":0.30,"y":0.46,"voice":"female"},{"word":"a crowd","x":0.50,"y":0.86,"voice":"female"}],
"question":"What is the hiker carrying?","answer":["He","is","carrying","a","heavy","backpack."],"answerVoice":"male",
"notes":"Montage with cuts: woman 0-3.0 s, hiker 3.5-5.5 s, dog 6.0-7.5 s, crowd crossing 8.0-10.0 (no tap target). At 0.5 s a woman in black heels walks behind; the phrase says nude heels to keep it unique. Key word 'downtown' is not a placeable noun; the still is the downtown crossing. defaultVoice female (mixed people, evenId true). Bottom of the still also has zebra stripes under the crowd; the crossing pill sits on the empty upper stripes."}
json.dump(c,open('content/5470.json','w'),indent=1)
