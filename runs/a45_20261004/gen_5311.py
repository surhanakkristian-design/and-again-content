import json
def keys(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]
def fill(d): return [(t,)+d[t] if t in d else (t,None) for t in T]
cry=fill({1.0:(0,0,.92,1.0),1.5:(0,0,.92,1.0),2.0:(0,0,.88,1.0),2.5:(0,0,.88,1.0)})
green=fill({6.0:(.52,.03,.48,.62),6.5:(.50,.10,.50,.55),7.0:(.62,.27,.38,.36),7.5:(.62,.28,.38,.34),
 8.0:(.60,.30,.40,.29),8.5:(.60,.30,.40,.23),9.0:(.57,.30,.43,.22)})
red=fill({7.0:(.78,.12,.22,.14),7.5:(.74,.14,.26,.14),8.0:(.72,.15,.27,.14),8.5:(.75,.15,.25,.14),9.0:(.67,.16,.27,.14)})
d={"mediaId":5311,"level":"B","keyWord":"calm","defaultVoice":"female",
"taps":[{"phrase":"to wince in pain","target":"the crying woman","voice":"female","keys":keys(cry)},
{"phrase":"to snuggle under a chunky blanket","target":"the woman in green","voice":"female","keys":keys(green)},
{"phrase":"to wear a pale blue hoodie","target":"the red-haired woman","voice":"female","keys":keys(red)}],
"stillS":8.0,
"nouns":[{"word":"fairy lights","x":0.17,"y":0.11,"voice":"female"},{"word":"a potted plant","x":0.12,"y":0.22,"voice":"female"},
{"word":"a cushion","x":0.90,"y":0.36,"voice":"female"},{"word":"a tassel","x":0.40,"y":0.59,"voice":"female"}],
"question":"What are the friends doing?","answer":["They","are","lying","close","together."],"answerVoice":"female",
"notes":"Many cuts and the casting is not consistent: the crying woman (braids, 1.0-2.5) never reappears clearly; 0.0-0.5 (shoulder with aloe), 3.0-5.5 (back view, blanket, mug) are off for all targets. Woman in green = brown-haired woman under the cream chunky-knit blanket in the middle pair (closeup 6.0-6.5 on the right, group 7.0-9.0); the front-left woman is under a cream cable-knit blanket, verifier may check 'chunky' is distinctive enough. Red-haired woman in the light blue hoodie peeks over the back of the sofa 7.0-9.0. Key word 'calm' (adjective) not used."}
json.dump(d,open("content/5311.json","w"),indent=1)
