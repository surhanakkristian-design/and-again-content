import json
T=[i*0.5 for i in range(25)]
def keys(spec):
    out=[]
    for t in T:
        b=None
        for (a,z,box) in spec:
            if a<=t+1e-9 and t<=z+1e-9: b=box
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man=keys([(0,0,(0.66,0.48,0.34,0.30)),(0.5,0.5,(0.40,0.38,0.60,0.42)),(1.0,1.5,(0.64,0.38,0.36,0.42)),(2.0,3.0,(0.58,0.38,0.42,0.42))])
ws=keys([(3.5,3.5,(0.22,0.36,0.66,0.64)),(4.0,4.0,(0.20,0.40,0.68,0.60)),(4.5,4.5,(0.20,0.40,0.72,0.60)),(5.0,5.0,(0.53,0.40,0.38,0.60)),(5.5,5.5,(0.57,0.40,0.40,0.60)),(6.0,6.0,(0.59,0.41,0.38,0.59))])
wd=keys([(6.5,12.0,(0.38,0.58,0.28,0.33))])
d={"mediaId":5022,"level":"A","keyWord":"shine","defaultVoice":"female",
"taps":[{"phrase":"to sit at a desk","target":"the man","voice":"male","keys":man},
{"phrase":"to hold a tall lamp","target":"the woman in the shirt","voice":"female","keys":ws},
{"phrase":"to wear a long dress","target":"the woman in the dress","voice":"female","keys":wd}],
"stillS":5.0,
"nouns":[{"word":"a lamp","x":0.27,"y":0.40,"voice":"female"},{"word":"a woman","x":0.72,"y":0.62,"voice":"female"},{"word":"a sofa","x":0.14,"y":0.85,"voice":"female"},{"word":"books","x":0.55,"y":0.94,"voice":"female"}],
"question":"What is the man doing?","answer":["He","is","sitting","at","a","desk."],"answerVoice":"male",
"notes":"Three shots. Man also switches on the desk lamp at 0.5 s, so 'to hold a tall lamp' could be argued for him too (he touches the lamp head); kept for the woman in the shirt, whose action is clearer. Man very dark at 0.0 s."}
json.dump(d,open("content/5022.json","w"),indent=1)
