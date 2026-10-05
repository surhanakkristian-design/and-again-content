import json
G=[(0.0,.34,.12,.58,.88),(0.5,.34,.12,.58,.88),(1.0,.34,.12,.58,.88),(1.5,.34,.09,.66,.91),(2.0,.30,.11,.70,.89),
(2.5,.20,.08,.73,.92),(3.0,.22,.21,.78,.79),(3.5,.22,.23,.74,.77),(4.0,.08,.16,.92,.84),(4.5,0,.14,1,.86),(5.0,0,.38,1,.62),
(5.5,0,.28,.76,.72),(6.0,.15,.39,.64,.56),(6.5,.47,.35,.50,.46),(7.0,.32,.34,.62,.64),(7.5,.26,.38,.72,.62),
(8.0,.45,.37,.46,.45),(8.5,.26,.38,.50,.51),(9.0,.37,.41,.33,.52),(9.5,.41,.43,.31,.45),(10.0,.41,.46,.28,.31),
(10.5,.39,.46,.22,.26),(11.0,.48,.43,.18,.21),(11.5,.46,.44,.18,.20),(12.0,.46,.43,.18,.20)]
goat=[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,x,y,w,h in G]
F={5.5:(.78,.19,.22,.25),6.0:(.30,.16,.38,.23),6.5:(0,.03,.45,.45)}
far=[]
for t,*_ in G:
    if t in F:
        x,y,w,h=F[t]; far.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    else: far.append({"t":t,"off":True})
d={"mediaId":4702,"level":"B","keyWord":"escape","defaultVoice":"female",
"taps":[
 {"phrase":"to squeeze through the gate","target":"the goat","voice":"female","keys":goat},
 {"phrase":"to lean over the sacks","target":"the farmer","voice":"male","keys":far},
 {"phrase":"to race down a dirt track","target":"the goat","voice":"female","keys":goat}],
"stillS":6.5,
"nouns":[{"word":"a straw hat","x":0.30,"y":0.11,"voice":"female"},{"word":"a fence","x":0.78,"y":0.31,"voice":"female"},
 {"word":"a goat","x":0.72,"y":0.53,"voice":"female"},{"word":"a sack","x":0.25,"y":0.62,"voice":"female"}],
"question":"What is the goat doing?",
"answer":["It","is","escaping","down","a","dirt","track."],"answerVoice":"female",
"notes":"The farmer is in the picture only at 5.5-6.5 s (at 7.0 s only a sliver at the left edge, set off); he leans over the sacks at 5.5 and 6.0 s and has straightened up, hat in hand, at 6.5 s. At 6.0 s goat and farmer overlap: split on a horizontal line at y 0.39 (his hands fall below it). Other goats stand in the pen behind the gate in the first shots but are hardly visible; target named just 'the goat'. defaultVoice female by evenId (main subject is an animal). Still 6.5 s has some motion."}
json.dump(d,open("content/4702.json","w"),indent=1)
