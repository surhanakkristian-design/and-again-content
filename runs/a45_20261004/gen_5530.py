import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
man=[(0,.14,.63,.86),(0,.14,.63,.86),(0,.15,.63,.85),(.02,.14,.63,.86),(.06,.14,.53,.86),(.06,.15,.50,.85),(.22,.19,.34,.81),(.29,.22,.33,.78)]
wom=[(.64,.24,.36,.76),(.64,.24,.36,.76),(.64,.25,.36,.75),(.65,.25,.35,.75),(.60,.24,.40,.76),(.66,.24,.34,.76),(.60,.27,.40,.73),(.63,.31,.32,.69)]
d={"mediaId":5530,"level":"A","keyWord":"admit","defaultVoice":"male",
"taps":[{"phrase":"to point at the man","target":"the woman","voice":"female","keys":K(wom)},
{"phrase":"to raise his hand","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to look down at the ground","target":"the man","voice":"male","keys":K(man)}],
"stillS":2.2,
"nouns":[{"word":"the sky","x":0.50,"y":0.08,"voice":"male"},
{"word":"a man","x":0.30,"y":0.42,"voice":"male"},
{"word":"a woman","x":0.82,"y":0.55,"voice":"female"},
{"word":"flowers","x":0.64,"y":0.77,"voice":"male"}],
"question":"What is the woman doing?",
"answer":["She","is","pointing","at","the","man."],
"answerVoice":"female",
"notes":"0.2-1.7 her pointing arm lies across the man's body; boxes split at x~0.64 so her hand is inside his box. 'look down' = man at 2.7-3.7. Marmot too tiny (3.7 only) to use."}
json.dump(d,open("content/5530.json","w"),indent=1)
