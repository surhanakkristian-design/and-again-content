import json
times=[i*0.5 for i in range(21)]
man={7.0:(0,.05,.12,.75),7.5:(0,0,.30,.90),8.0:(0,0,.32,.85),8.5:(0,0,.35,.85),9.0:(0,.05,.36,.80),9.5:(0,0,.34,.85),10.0:(0,0,.34,.85)}
wom={7.0:(.72,0,.28,.78),7.5:(.70,0,.30,.75),8.0:(.63,0,.37,.80),8.5:(.66,0,.34,.82),9.0:(.55,0,.45,.85),9.5:(.66,0,.34,.85),10.0:(.62,0,.38,.82)}
bird={7.0:(.27,.12,.20,.16),7.5:(.31,.22,.18,.14),8.0:(.33,.25,.18,.14),8.5:(.37,.27,.18,.14),9.0:(.36,.31,.18,.14),9.5:(.35,.27,.18,.14),10.0:(.35,.26,.18,.14)}
def keys(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in times]
c={"mediaId":606,"level":"A","keyWord":"recipe","defaultVoice":"female",
"taps":[{"phrase":"to sit in a cage","target":"the bird","voice":"female","keys":keys(bird)},
{"phrase":"to have a black beard","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to have long curly hair","target":"the woman","voice":"female","keys":keys(wom)}],
"stillS":8.0,
"nouns":[{"word":"a recipe","x":.48,"y":.52,"voice":"female"},{"word":"a bird","x":.42,"y":.31,"voice":"female"},{"word":"pancakes","x":.50,"y":.80,"voice":"female"},{"word":"a man","x":.14,"y":.15,"voice":"male"}],
"question":"What are the man and woman eating?","answer":["They","are","eating","pancakes."],"answerVoice":"female",
"notes":"People appear only from 7.0 s (earlier shots show hands only, owner unknown, so all targets are off there). Man and woman do the same things (smile, hold the card, high five, eat), so their phrases are states (beard / curly hair). At 9.0 the man's raised forearm lies outside his box because the bird box sits between. 'a recipe' = the paper card with drawings."}
json.dump(c,open('content/606.json','w'),indent=1,ensure_ascii=False)
