import json
def K(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
split=[0.40,0.38,0.36,0.35,0.40,0.38,0.45,0.56]
wtop=[0.35,0.34,0.34,0.33,0.32,0.32,0.31,0.31]
mtop=[0.29,0.28,0.32,0.32,0.31,0.29,0.23,0.20]
woman=K(T,[(0.02,wtop[i],split[i],1.0) for i in range(8)])
man=K(T,[(split[i],mtop[i],0.96 if i<3 else 1.0,1.0) for i in range(8)])
c={"mediaId":5686,"level":"B","keyWord":"bring around","defaultVoice":"female",
"taps":[{"phrase":"to cradle a puppy","target":"the woman","voice":"female","keys":woman},
{"phrase":"to scratch the puppy's chin","target":"the man","voice":"male","keys":man},
{"phrase":"to lean in towards the puppy","target":"the man","voice":"male","keys":man}],
"stillS":0.7,
"nouns":[{"word":"grapes","x":0.16,"y":0.10,"voice":"female"},{"word":"a lantern","x":0.80,"y":0.30,"voice":"female"},
{"word":"a puppy","x":0.29,"y":0.55,"voice":"female"},{"word":"a water bowl","x":0.57,"y":0.72,"voice":"female"}],
"question":"What is the man doing?","answer":["He","is","scratching","the","puppy's","chin."],"answerVoice":"male",
"notes":"Puppy not used as a tap target: she holds it against her chest and his hands are on it, so its box could not be split cleanly. Woman/man boxes are split vertically at the man's reaching hand; at 1.2-2.7 his fingertips lie slightly inside the woman's box and at 3.2-3.7 his outstretched hand is in her box. Key word 'bring around' (phrasal verb) is not a visible noun."}
json.dump(c,open('content/5686.json','w'),indent=1)
