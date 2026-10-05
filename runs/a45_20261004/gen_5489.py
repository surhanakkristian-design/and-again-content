import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
w={0.0:(.17,.09,.70,.91),0.5:(.18,.10,.68,.90),1.0:(.12,.09,.68,.91),1.5:(.11,.05,.68,.95),2.0:(0,.10,.93,.90),
2.5:(0,.12,.90,.88),3.0:(.01,.12,.81,.88),3.5:(0,.12,.71,.88),4.0:(.18,.08,.80,.92),4.5:(.20,.07,.57,.93),
5.0:(.27,.07,.43,.93),5.5:(.10,.05,.78,.95),6.0:(.27,.12,.50,.88),6.5:(.28,.12,.50,.88),7.0:(.27,.12,.47,.88),
7.5:(.21,.05,.79,.95),8.0:(.10,.06,.90,.94),8.5:(.12,.05,.88,.95),9.0:(.17,.07,.83,.93)}
c={"mediaId":5489,"level":"A","keyWord":"wear","defaultVoice":"female",
"taps":[
 {"phrase":"to wear a red coat","target":"the woman in front","voice":"female","keys":keys(w)},
 {"phrase":"to wear a silver dress","target":"the woman in front","voice":"female","keys":keys(w)},
 {"phrase":"to smile at the camera","target":"the woman in front","voice":"female","keys":keys(w)}],
"stillS":4.5,
"nouns":[{"word":"a window","x":0.27,"y":0.17,"voice":"female"},
 {"word":"a dress","x":0.48,"y":0.45,"voice":"female"},
 {"word":"clothes","x":0.12,"y":0.62,"voice":"female"}],
"question":"What is the woman in front doing?",
"answer":["She","is","trying","on","different","clothes."],
"answerVoice":"female",
"notes":"Only one clear target (the posing woman); background shoppers are small and partly hidden. AI glitch: at 6.0-7.0 s a second copy of the woman in the feather coat and hat stands in the background on the right (kept outside the box). 'trying on' is inferred from the cuts between outfits; shop staff/shoppers in black behind her."}
json.dump(c,open('content/5489.json','w'),indent=1)
