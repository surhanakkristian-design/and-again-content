import json
M=[(0.0,.70,.42),(0.5,.70,.42),(1.0,.68,.42),(1.5,.69,.42),(2.0,.65,.42),(2.5,.65,.42),(3.0,.64,.42),(3.5,.65,.42),
   (4.0,.65,.42),(4.5,.65,.42),(5.0,.65,.42),(5.5,.65,.42),(6.0,.64,.42),(6.5,.64,.42),(7.0,.63,.42),(7.5,.63,.42)]
man=[];cas=[]
for t,x,h in M:
    man.append({"t":t,"x":x,"y":0.0,"w":round(1-x,2),"h":h})
    cx=0.0 if t==7.5 else (0.0 if t in (0.5,3.0,3.5) else 0.06)
    cas.append({"t":t,"x":cx,"y":0.12,"w":round(x-cx,2),"h":0.61})
L=[(8.0,.62,.44,.18,.78,.29),(8.5,.62,.46,.08,.90,.25),(9.0,.60,.48,.08,.86,.22),(9.5,.61,.49,.08,.88,.19),
   (10.0,.58,.49,.06,.88,.19),(10.5,.58,.49,.06,.88,.19),(11.0,.56,.50,.03,.88,.19),(11.5,.55,.50,.03,.88,.19),(12.0,.54,.50,.02,.88,.20)]
for t,x,h,cx,cw,ch in L:
    man.append({"t":t,"x":x,"y":0.0,"w":round(1-x,2),"h":h})
    cas.append({"t":t,"x":cx,"y":h,"w":cw,"h":ch})
d={"mediaId":4701,"level":"A","keyWord":"ruin","defaultVoice":"male",
"taps":[
 {"phrase":"to fall into the sea","target":"the sandcastle","voice":"male","keys":cas},
 {"phrase":"to look at the sandcastle","target":"the man","voice":"male","keys":man},
 {"phrase":"to wear a dark hat","target":"the man","voice":"male","keys":man}],
"stillS":2.0,
"nouns":[{"word":"a hat","x":0.84,"y":0.09,"voice":"male"},{"word":"a sandcastle","x":0.45,"y":0.50,"voice":"male"},
 {"word":"the sea","x":0.17,"y":0.28,"voice":"male"},{"word":"the sky","x":0.35,"y":0.06,"voice":"male"}],
"question":"What is happening to the sandcastle?",
"answer":["It","is","falling","into","the","sea."],"answerVoice":"male",
"notes":"Only two tappable targets (kites too small and overlap the castle top). Castle and man overlap in the picture: until 7.5 s split on a vertical line (castle's right corner tower lies under the man's box and is in neither box below y 0.42); from 8.0 s split on a horizontal line under his knees. 'to wear a dark hat' is a state because the man has only one clear action."}
json.dump(d,open("content/4701.json","w"),indent=1)
