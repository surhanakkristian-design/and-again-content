import json
D={0.0:(.60,.41),0.5:(.59,.41),1.0:(.57,.42),1.5:(.59,.42),2.0:(.58,.41),2.5:(.59,.41),3.0:(.58,.42),3.5:(.59,.42),
4.0:(.61,.41),4.5:(.62,.41),5.0:(.61,.42),5.5:(.61,.42),6.0:(.61,.42),6.5:(.62,.42),7.0:(.64,.43),7.5:(.63,.43),
8.0:(.60,.41),8.5:(.60,.41),9.0:(.63,.43),9.5:(.65,.43)}
dk=[];pk=[];tk=[]
for t in sorted(D):
    sx,ty=D[t]
    dk.append({"t":t,"x":round(sx-0.32,2),"y":0.15,"w":0.32,"h":round(ty-0.15,2)})
    pk.append({"t":t,"x":sx,"y":0.13,"w":0.18,"h":round(ty-0.13,2)})
    tk.append({"t":t,"x":0.02,"y":ty,"w":0.96,"h":round(0.85-ty,2)})
c={"mediaId":4218,"level":"B","keyWord":"engine","defaultVoice":"female",
"taps":[
 {"phrase":"to steer a rusty tractor","target":"the dog","voice":"female","keys":dk},
 {"phrase":"to puff out black smoke","target":"the exhaust pipe","voice":"female","keys":pk},
 {"phrase":"to roll along the road","target":"the tractor","voice":"female","keys":tk}],
"stillS":8.0,
"nouns":[{"word":"smoke","x":0.50,"y":0.07,"voice":"female"},{"word":"a vineyard","x":0.18,"y":0.24,"voice":"female"},
 {"word":"an exhaust pipe","x":0.72,"y":0.34,"voice":"female"},{"word":"a tractor","x":0.48,"y":0.52,"voice":"female"}],
"question":"What is the dog doing?",
"answer":["It","is","steering","a","rusty","tractor."],"answerVoice":"female",
"notes":"Key word 'engine' is not a visible thing (it is behind the grille), so it is not used as a noun or in the phrases. The dog sits on the tractor and the exhaust pipe is part of it: the tractor box is only the part below the dog's paws, the pipe box the upright pipe right of the dog, split from the dog on a vertical line. Smoke comes out only from about 7.0 to 8.5 s. No person, evenId true -> female voice."}
json.dump(c,open('content/4218.json','w'),indent=1,ensure_ascii=False)
