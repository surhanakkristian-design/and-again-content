import json
T=[i*0.5 for i in range(21)]
N=None
path=[(.12,0,.88,1),(.42,.05,.58,.95),(.40,.28,.60,.72),(.38,.36,.62,.64),(.25,.33,.75,.67),(.25,.38,.75,.62),(.20,.48,.80,.52),(.15,.55,.85,.45)]+[N]*13
wom=[N]*16+[(.29,.51,.21,.34),(.26,.53,.25,.25),(.28,.56,.22,.21),(.30,.57,.18,.18),(.32,.57,.18,.17)]
man=[N]*16+[(.50,.49,.22,.36),(.51,.52,.24,.26),(.50,.55,.22,.22),(.48,.56,.19,.19),(.50,.57,.18,.17)]
def keys(b):
    return [({"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} if k else {"t":t,"off":True}) for t,k in zip(T,b)]
d={"mediaId":486,"level":"A","keyWord":"a mountain","defaultVoice":"female",
"taps":[
 {"phrase":"to go up the mountain","target":"the path","voice":"female","keys":keys(path)},
 {"phrase":"to wear a red jacket","target":"the woman","voice":"female","keys":keys(wom)},
 {"phrase":"to wear a yellow jacket","target":"the man","voice":"male","keys":keys(man)}],
"stillS":9.0,
"nouns":[{"word":"the sky","x":.50,"y":.15,"voice":"female"},{"word":"a mountain","x":.65,"y":.46,"voice":"female"},{"word":"clouds","x":.22,"y":.60,"voice":"female"},{"word":"snow","x":.62,"y":.92,"voice":"female"}],
"question":"Where are the two people standing?",
"answer":["They","are","standing","on","a","mountain."],"answerVoice":"female",
"notes":"Three shots. The woman and the man appear only 8.0-10.0 s, small and side by side, and do the same things (stand, raise their poles), so each gets a state phrase (jacket colour). Their boxes touch at about x 0.50; at 8.5 s his arm reaches behind her. Third target is a thing: the zigzag path in the drone shot 0.0-3.5 s (wide box, no other target there); in the walking shot 4.0-7.5 s a thin far-away trail is still faintly visible but marked off. The legs of the walking person were not used as a target. 'a mountain' pill sits on the brown mountain in the middle distance; the people also stand on one."}
json.dump(d,open("content/486.json","w"),indent=1,ensure_ascii=False)
