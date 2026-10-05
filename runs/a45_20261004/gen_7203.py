import json, sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(boxes):
    out=[]
    for t,b in zip(T,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
hd=keys([(0.28,0.29,0.47,0.41)]*8)
vol=keys([(0.22,0.05,0.42,0.23)]*8)
lava=keys([(0.0,0.37,0.27,0.38)]*8)
c={"mediaId":7203,"level":"B","keyWord":"hard drive","defaultVoice":"male",
"taps":[
 {"phrase":"to stand on cooled lava","target":"the hard drive","voice":"male","keys":hd},
 {"phrase":"to spew fire and smoke","target":"the volcano","voice":"male","keys":vol},
 {"phrase":"to flow across the ground","target":"the lava river","voice":"male","keys":lava}],
"stillS":2.2,
"nouns":[{"word":"smoke","x":0.55,"y":0.10,"voice":"male"},
 {"word":"a volcano","x":0.42,"y":0.24,"voice":"male"},
 {"word":"a hard drive","x":0.50,"y":0.45,"voice":"male"},
 {"word":"lava","x":0.15,"y":0.55,"voice":"male"}],
"question":"Where is the hard drive standing?",
"answer":["It","is","standing","on","a","block","of","cooled","lava."],
"answerVoice":"male",
"notes":"No person; evenId false -> male. Static shot with slight camera drift. The lava river target = the bright flow left of the drive (box only on the left part so it does not overlap the drive); lava also flows right of the drive behind it. The small glowing lava drop at the drive's base is not used."}
json.dump(c,open('content/7203.json','w'),indent=1)
