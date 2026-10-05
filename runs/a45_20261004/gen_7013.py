import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":round(r[2]-r[0],2),"h":round(r[3]-r[1],2)}) for t,r in zip(T,rows)]
man=K([(.08,.42,.65,.97),(.04,.41,.69,.99),(.18,.39,.71,1),(.08,.31,.76,1),(0,.25,.78,1),(0,.19,.80,1),(0,.16,.74,1),(0,.15,.76,1)])
woman=K([(.66,.22,.94,.99),(.70,.16,.97,.99),(.72,.07,1,1),(.77,0,1,1),(.79,0,1,1),(.81,0,1,1),(.75,0,1,1),(.77,0,1,1)])
c={"mediaId":7013,"level":"A","keyWord":"daddy","defaultVoice":"male",
"taps":[{"phrase":"to hold baby shoes","target":"the man with the mohawk","voice":"male","keys":man},
{"phrase":"to kneel in the mud","target":"the man with the mohawk","voice":"male","keys":man},
{"phrase":"to hold a black umbrella","target":"the woman","voice":"female","keys":woman}],
"stillS":0.2,
"nouns":[{"word":"an umbrella","x":0.70,"y":0.27,"voice":"male"},{"word":"a daddy","x":0.52,"y":0.53,"voice":"male"},
{"word":"baby shoes","x":0.60,"y":0.65,"voice":"male"},{"word":"mud","x":0.82,"y":0.91,"voice":"male"}],
"question":"What is the daddy holding?",
"answer":["He","is","holding","baby","shoes."],"answerVoice":"male",
"notes":"Only two clear targets: both men in denim vests put a hand on their chest, so neither gets a unique phrase; the mohawk man takes two phrases. He holds the shoes up against the woman's belly, so his hand/the shoes and her belly overlap in the picture: boxes are split by a vertical line just right of the shoes (shoes in his box until 2.7; at 3.2/3.7 the shoes are partly in her box), so her belly/left side and her umbrella hand fall outside her box. From 2.2 the umbrella is held by a hand near the man's head (most likely hers, check). 'a daddy' pill sits on the man's face; noun voice male (male person)."}
json.dump(c,open('content/7013.json','w'),indent=1)
