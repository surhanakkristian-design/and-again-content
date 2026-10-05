import json,sys
def K(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
T=[0.2,0.7,1.2,1.7]
man=K(T,[(0.17,0.40,0.63,0.89),(0.22,0.25,0.72,0.89),(0.0,0.21,0.73,0.90),(0.03,0.21,0.90,0.90)])
crowd=K(T,[(0.0,0.06,1.0,0.39),(0.0,0.06,1.0,0.24),(0.0,0.06,1.0,0.20),(0.0,0.06,1.0,0.20)])
c={"mediaId":5685,"level":"A","keyWord":"brilliant","defaultVoice":"male",
"taps":[{"phrase":"to bow to the crowd","target":"the man","voice":"male","keys":man},
{"phrase":"to open his arms wide","target":"the man","voice":"male","keys":man},
{"phrase":"to clap their hands","target":"the crowd","voice":"male","keys":crowd}],
"stillS":0.7,
"nouns":[{"word":"a crowd","x":0.30,"y":0.15,"voice":"male"},{"word":"a flag","x":0.63,"y":0.35,"voice":"male"},
{"word":"a man","x":0.45,"y":0.47,"voice":"male"},{"word":"a rose","x":0.29,"y":0.84,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","bowing","to","the","crowd."],"answerVoice":"male",
"notes":"Only two targets fit (skater, crowd); roses are scattered around his skates and would overlap his box. Crowd box is shrunk to the upper stands where the man's raised arms cross the lower rows (t 1.2, 1.7). Key word 'brilliant' is an adjective, not used as a noun. Bow happens at 0.2-0.7, open arms at 1.2-1.7."}
json.dump(c,open('content/5685.json','w'),indent=1)
