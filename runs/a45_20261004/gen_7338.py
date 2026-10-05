import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W=[(0.29,0.41,0.44,0.33)]*8
H=[(0.80,0.35,0.19,0.15)]*4+[None]*4
def k(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
w=k(W); h=k(H)
c={"mediaId":7338,"level":"B","keyWord":"marsh","defaultVoice":"female",
"taps":[
 {"phrase":"to paddle along the channel","target":"the woman","voice":"female","keys":w},
 {"phrase":"to kneel on the board","target":"the woman","voice":"female","keys":w},
 {"phrase":"to graze in the distance","target":"the white horse","voice":"female","keys":h}],
"stillS":0.2,
"nouns":[{"word":"flamingos","x":0.50,"y":0.25,"voice":"female"},{"word":"a watchtower","x":0.39,"y":0.395,"voice":"female"},
 {"word":"a paddle board","x":0.70,"y":0.71,"voice":"female"},{"word":"reeds","x":0.88,"y":0.85,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","paddling","through","the","marsh."],"answerVoice":"female",
"notes":"Horse is small at the right edge and only in frame 0.2-1.7 (off after the pan). Marsh = whole landscape, so it is in the answer, not a pill. Flamingos are a flock, no single bird used as a target."}
json.dump(c,open('content/7338.json','w'),indent=1)
